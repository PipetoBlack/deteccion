# Detección y Seguimiento de Objetos con YOLO

Proyecto educativo para el canal de YouTube. Analiza un video y detecta + sigue objetos usando **YOLO11** de Ultralytics con el dataset **COCO** (80 clases).

---

## ¿Qué hace este proyecto?

- Carga un video `.mp4` desde la carpeta del proyecto
- Detecta objetos en cada frame usando YOLO11l (modelo Large preentrenado)
- Sigue cada objeto a lo largo del video con un ID persistente (ByteTrack)
- Guarda el video resultante con cajas, etiquetas e IDs dibujados
- Imprime en consola un resumen de cuántos objetos únicos se detectaron

---

## Requisitos previos

- Python 3.10 o superior
- Git (opcional, para clonar el repo)

Verificá tu versión de Python:

```bash
python --version        # Windows
python3 --version       # Linux / macOS
```

---

## Instalación paso a paso

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/PipetoBlack/deteccion
cd deteccion
```

O simplemente descargá el ZIP y descomprimilo.

---

### 2. Crear el entorno virtual

Un entorno virtual aísla las dependencias del proyecto del resto del sistema.

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (CMD)**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> Si PowerShell te bloquea el script, ejecutá primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Cuando el entorno esté activo, verás `(.venv)` al inicio del prompt.

---

### 3. Instalar dependencias

```bash
pip install ultralytics
```

Esto instala automáticamente: PyTorch, OpenCV, NumPy, y todo lo necesario.

> La primera vez puede tardar varios minutos dependiendo de tu conexión.

---

### 4. Agregar tu video

Copiá el video que querés analizar dentro de la carpeta del proyecto y nombralo `2.mp4`, o cambiá esta línea en `yolo.py`:

```python
VIDEO_ENTRADA = "2.mp4"   # <-- cambiá este nombre por el tuyo
```

---

### 5. Ejecutar el script

```bash
python yolo.py        # Windows
python3 yolo.py       # Linux / macOS
```

La primera ejecución descarga el modelo `yolo11l.pt` (~50 MB). A partir de la segunda, usa el archivo local.

---

## Estructura del proyecto

```
deteccion/
├── yolo.py             # Script principal
├── yolo11l.pt          # Modelo descargado automáticamente (se crea al correr)
├── 2.mp4               # Tu video de entrada
├── resultados/
│   └── deteccion/
│       └── 2.mp4       # Video de salida con detecciones y tracking
└── README.md
```

---

## Configuración

Todas las variables de configuración están al tope de `yolo.py`:

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `VIDEO_ENTRADA` | `"2.mp4"` | Nombre del video a analizar |
| `CARPETA_SALIDA` | `resultados/` | Dónde se guarda el resultado |
| `CONFIANZA_MINIMA` | `0.25` | Umbral mínimo de confianza (0.0 – 1.0) |

---

## Modelos disponibles

Podés cambiar el modelo según tus necesidades. A mayor modelo, más preciso pero más lento:

| Modelo | Velocidad | Precisión | Uso recomendado |
|---|---|---|---|
| `yolo11n.pt` | Muy rápido | Básica | Webcam en tiempo real |
| `yolo11s.pt` | Rápido | Buena | Videos cortos |
| `yolo11m.pt` | Medio | Mejor | Balance general |
| `yolo11l.pt` | Lento | Alta | Videos grabados |
| `yolo11x.pt` | Muy lento | Máxima | Análisis exhaustivo |

Para cambiar el modelo, editá esta línea en `yolo.py`:

```python
modelo = YOLO("yolo11n.pt")   # <-- cambiá por el modelo deseado
```

---

## Clases que detecta COCO

El modelo detecta 80 objetos del día a día, entre ellos:

`person` · `car` · `truck` · `bus` · `motorcycle` · `bicycle` · `dog` · `cat` · `chair` · `bottle` · `laptop` · `cell phone` · `backpack` · `umbrella` · `traffic light` · y 65 más.

---

## Solución de problemas

**"No se detectó ningún objeto"**
- Bajá la confianza mínima a `0.1` para ver qué detecta el modelo con menos filtro
- Verificá que el video tenga objetos de las 80 clases de COCO
- Probá con un modelo más grande (`yolo11x.pt`)

**Error al activar el entorno en Windows**
- Usá CMD en lugar de PowerShell, o ejecutá el comando de `Set-ExecutionPolicy` indicado arriba

**La instalación de ultralytics falla**
- Asegurate de tener pip actualizado: `pip install --upgrade pip`
- En Ubuntu/Debian, no uses pip del sistema: siempre instalá dentro del entorno virtual

---

## Tecnologías usadas

- [Ultralytics YOLO](https://docs.ultralytics.com/) — Framework de detección
- [YOLO11](https://docs.ultralytics.com/tasks/detect/) — Modelo de detección
- [ByteTrack](https://docs.ultralytics.com/reference/trackers/) — Algoritmo de tracking
- [COCO Dataset](https://cocodataset.org/) — Dataset de entrenamiento
