from ultralytics import YOLO
from pathlib import Path

# Configuración
VIDEO_ENTRADA = "2.mp4"          # Video a analizar (debe estar en esta carpeta)
CARPETA_SALIDA = Path(__file__).parent / "resultados"
CONFIANZA_MINIMA = 0.25          # Solo mostrar detecciones con ≥25% de confianza

def main():
    CARPETA_SALIDA.mkdir(exist_ok=True)

    # Carga el modelo (se descarga automáticamente la primera vez)
    modelo = YOLO("yolo11l.pt")

    ruta_video = Path(__file__).parent / VIDEO_ENTRADA
    if not ruta_video.exists():
        print(f"[ERROR] No se encontró el video: {ruta_video}")
        return

    print(f"\n Analizando: {ruta_video.name}")
    print(f" Modelo: YOLO11l | Dataset: COCO (80 clases)\n")

    # Tracking: detecta Y sigue cada objeto con un ID persistente entre frames
    resultados = modelo.track(
        source=str(ruta_video),
        conf=CONFIANZA_MINIMA,
        save=True,                  # Guarda el video con cajas y IDs dibujados
        project=str(CARPETA_SALIDA),
        name="deteccion",
        exist_ok=True,
        stream=True,                # Procesa frame a frame (ahorra RAM)
        verbose=True,
        tracker="bytetrack.yaml",  # Algoritmo de tracking (viene incluido en ultralytics)
    )

    # Recorre los frames y muestra un resumen por consola
    conteo_ids: dict[str, set] = {}  # clase -> conjunto de IDs únicos vistos

    for resultado in resultados:
        if resultado.boxes is None:
            continue
        for box in resultado.boxes:
            nombre_clase = modelo.names[int(box.cls)]
            track_id = int(box.id) if box.id is not None else -1

            if nombre_clase not in conteo_ids:
                conteo_ids[nombre_clase] = set()
            conteo_ids[nombre_clase].add(track_id)

    # Resumen final
    print("\n── Resumen de objetos rastreados ────────────────────")
    if conteo_ids:
        for clase, ids in sorted(conteo_ids.items(), key=lambda x: -len(x[1])):
            print(f"  {clase:<20} {len(ids)} objeto(s) único(s)")
    else:
        print("  No se detectó ningún objeto con la confianza mínima requerida.")

    print(f"\n Video guardado en: {CARPETA_SALIDA / 'deteccion'}")


if __name__ == "__main__":
    main()
