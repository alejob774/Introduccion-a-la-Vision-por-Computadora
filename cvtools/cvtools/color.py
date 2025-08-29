import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import Counter
import os

def rgb_to_hsv(image):
    """Convierte imagen RGB a HSV"""
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

def rgb_to_lab(image):
    """Convierte imagen RGB a LAB"""
    return cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

def plot_color_histogram(image, title="Histograma de Colores"):
    """
    Calcula y grafica el histograma de colores de una imagen
    """
    if len(image.shape) == 3:
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histogram, color=color)
    else:
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
        plt.plot(histogram, color='gray')
    
    plt.title(title)
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()

def quantize_image(image, num_colors):
    """
    Reduce la imagen a un número limitado de colores usando k-means
    """
    # Reformatear la imagen
    data = image.reshape((-1, 3))
    data = np.float32(data)
    
    # Criterio y aplicar k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(data, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convertir de nuevo a uint8
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    quantized = quantized.reshape(image.shape)
    
    return quantized

def reduce_image_size(image_path, num_colors):
    """
    Reduce el peso de la imagen disminuyendo la cantidad de colores
    Retorna el nuevo tamaño en KB
    """
    # Leer imagen
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Cuantizar imagen
    quantized = quantize_image(image, num_colors)
    
    # Guardar temporalmente y calcular tamaño
    temp_path = "temp_quantized.jpg"
    cv2.imwrite(temp_path, cv2.cvtColor(quantized, cv2.COLOR_RGB2BGR))
    
    # Obtener tamaño
    size_kb = os.path.getsize(temp_path) / 1024
    
    # Eliminar archivo temporal
    os.remove(temp_path)
    
    return size_kb

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar imagen de ejemplo
    image = cv2.imread('../data/ejemplo1.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convertir espacios de color
    hsv_image = rgb_to_hsv(image)
    lab_image = rgb_to_lab(image)
    
    # Mostrar histograma
    plot_color_histogram(image)
    
    # Cuantizar imagen
    quantized = quantize_image(image, 16)
    
    # Reducir tamaño
    size_kb = reduce_image_size('../data/ejemplo1.jpg', 64)
    print(f"Nuevo tamaño: {size_kb:.2f} KB")
