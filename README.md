# Sistema Inteligente para la Detección de Grietas en Infraestructuras

## 🎥 Video de demostración

Antes de revisar el código, se recomienda visualizar el video donde se muestra el funcionamiento completo del sistema:

📹 **Video:** https://youtu.be/gIQ55_KijW4

En el video se puede observar:
- Carga de imágenes de estructuras.
- Procesamiento mediante visión por computador.
- Detección de posibles grietas.
- Clasificación automática del nivel de daño.
- Visualización de resultados en la interfaz gráfica.

---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un prototipo de software capaz de detectar posibles grietas en infraestructuras mediante técnicas de visión por computador implementadas en Python.

El sistema permite analizar imágenes cargadas por el usuario, identificar patrones compatibles con grietas y clasificar el nivel de deterioro estructural en tres categorías:

- 🟢 Bajo
- 🟡 Medio
- 🔴 Alto

El objetivo es apoyar procesos de inspección estructural de manera rápida y automatizada.

---

## Funcionalidades

- Carga de imágenes desde el equipo.
- Visualización de la imagen seleccionada.
- Procesamiento digital de imágenes.
- Detección de bordes y posibles grietas.
- Cálculo del porcentaje de área afectada.
- Clasificación automática del nivel de daño.
- Interfaz gráfica amigable desarrollada con Tkinter.

---

## Tecnologías utilizadas

- Python 3
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter


##  Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
cd REPOSITORIO
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
```

### 3. Activar entorno virtual

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install opencv-python pillow numpy
```

### 5. Ejecutar el programa

```bash
python main.py
```

---

##  Clasificación del daño

El sistema clasifica el estado de la estructura según el porcentaje de afectación detectado:

| Porcentaje detectado | Nivel |
|---------------------|--------|
| Menor a 1% | Bajo |
| Entre 1% y 3% | Medio |
| Mayor a 3% | Alto |




##  Autor

**Juan Jose Quevedo Morales**

Universidad Sergio Arboleda
