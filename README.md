# Taller de Visión por Computador - cvtools

Librería Python para procesamiento de imágenes y visión por computador.

## Estructura del proyecto
# Taller de Visión por Computador - Librería cvtools

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Librería Python para procesamiento de imágenes y visión por computador desarrollada como parte del taller del curso de Computer Vision.

## 📋 Características

- **Módulo Cámara**: Modelado de cámara, distorsión radial y ajuste de longitud focal
- **Módulo Color**: Conversión entre espacios de color, cuantización y manipulación de colores
- **Módulo Filtros**: Convoluciones, detección de bordes y operadores de imagen

## 🚀 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de dependencias

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/computer-vision-taller.git
cd computer-vision-taller

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias principales
- numpy==1.24.3
- opencv-python==4.8.0.76
- matplotlib==3.7.2
- scipy==1.10.1

## 📁 Estructura del proyecto

```
computer-vision-taller/
├── cvtools/                 # Librería principal
│   ├── __init__.py         # Inicialización del paquete
│   ├── camera.py           # Funciones de modelado de cámara
│   ├── color.py            # Funciones de manejo de color
│   └── filters.py          # Funciones de filtrado de imágenes
├── tests/                  # Tests unitarios
│   ├── test_camera.py
│   ├── test_color.py
│   └── test_filters.py
├── data/                   # Imágenes de prueba
│   ├── ejemplo1.jpg
│   └── ejemplo2.png
├── main.py                 # Script de demostración
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## 🧩 Módulos y Funcionalidades

### Módulo camera.py

#### `radial_distortion(points, k1, k2)`
Aplica distorsión radial a puntos proyectados usando los coeficientes k1 y k2.

**Parámetros:**
- `points`: Array de puntos (N, 2) en coordenadas de imagen
- `k1`: Coeficiente de distorsión radial de primer orden
- `k2`: Coeficiente de distorsión radial de segundo orden

**Retorna:**
- Array de puntos distorsionados (N, 2)

#### `change_focal_length(points, original_focal, new_focal)`
Ajusta puntos proyectados al cambiar la longitud focal.

**Parámetros:**
- `points`: Array de puntos (N, 2)
- `original_focal`: Longitud focal original
- `new_focal`: Nueva longitud focal

**Retorna:**
- Array de puntos ajustados (N, 2)

### Módulo color.py

#### `rgb_to_hsv(image)`
Convierte una imagen del espacio de color RGB a HSV.

#### `rgb_to_lab(image)`
Convierte una imagen del espacio de color RGB a LAB.

#### `plot_color_histogram(image, title)`
Calcula y grafica el histograma de colores de una imagen.

#### `quantize_image(image, num_colors)`
Reduce la imagen a un número limitado de colores usando algoritmo k-means.

#### `reduce_image_size(image_path, num_colors)`
Reduce el peso de la imagen disminuyendo la cantidad de colores y retorna el nuevo tamaño en KB.

### Módulo filters.py

#### `convolve(image, kernel)`
Aplica convolución a una imagen con un kernel dado.

#### `sobel_x(image)`
Aplica filtro Sobel en dirección X para detección de bordes verticales.

#### `sobel_y(image)`
Aplica filtro Sobel en dirección Y para detección de bordes horizontales.

#### `canny_edge_detector(image, threshold1, threshold2)`
Aplica detector de bordes Canny con thresholds especificados.

#### `laplacian_filter(image)`
Aplica filtro Laplaciano para resaltar bordes y regiones de rápida variación de intensidad.

## 💻 Uso básico

```python
# Importar la librería
from cvtools.camera import radial_distortion, change_focal_length
from cvtools.color import rgb_to_hsv, plot_color_histogram, quantize_image
from cvtools.filters import sobel_x, sobel_y, canny_edge_detector

# Cargar una imagen
import cv2
image = cv2.imread('data/ejemplo1.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convertir a HSV
hsv_image = rgb_to_hsv(image_rgb)

# Aplicar cuantización de colores
quantized = quantize_image(image_rgb, 16)

# Aplicar detección de bordes
edges = canny_edge_detector(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

# Mostrar histograma
plot_color_histogram(image_rgb, "Histograma de imagen")
```

## 🧪 Ejecutar tests

Para verificar que todas las funciones funcionan correctamente:

```bash
# Ejecutar todos los tests
python -m unittest discover tests/

# Ejecutar tests específicos
python -m unittest tests/test_camera.py
python -m unittest tests/test_color.py
python -m unittest tests/test_filters.py
```

## 🎯 Script de demostración

El archivo `main.py` contiene ejemplos de uso de todas las funciones:

```bash
python main.py
```

Este script generará:
- Visualizaciones de las transformaciones aplicadas
- Gráficos de histogramas
- Imágenes resultantes de los filtros aplicados
- Información en consola sobre el funcionamiento

## 📊 Resultados esperados

Al ejecutar el script principal, se generarán:

1. **Transformaciones geométricas**: Puntos con distorsión radial aplicada
2. **Conversiones de color**: Imágenes en espacios HSV y LAB
3. **Cuantización**: Imágenes reducidas a 16, 64 y 256 colores
4. **Filtros**: Imágenes con operadores Sobel, Canny y Laplaciano aplicados
5. **Histogramas**: Representación gráfica de la distribución de colores
6. **Métricas**: Tamaño de archivo antes y después de la cuantización

## 👨‍💻 Autor

**Tu Nombre**  
Estudiante de Computer Vision  
Universidad [Nombre de tu Universidad]  

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lee las [guías de contribución](CONTRIBUTING.md) antes de enviar un pull request.

## 📞 Contacto

Para preguntas sobre este proyecto, puedes contactarme a través de:
- Email: tu.email@universidad.edu
- LinkedIn: [Tu Perfil](https://linkedin.com/in/tuperfil)

---

**Fecha de entrega:** 29 de agosto de 2025  
**Curso:** Computer Vision - Pregrado
