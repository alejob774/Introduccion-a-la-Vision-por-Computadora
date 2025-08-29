import numpy as np
import cv2

def convolve(image, kernel):
    """
    Aplica convolución a una imagen con un kernel dado
    """
    return cv2.filter2D(image, -1, kernel)

def sobel_x(image):
    """
    Aplica filtro Sobel en dirección X
    """
    return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

def sobel_y(image):
    """
    Aplica filtro Sobel en dirección Y
    """
    return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

def canny_edge_detector(image, threshold1=100, threshold2=200):
    """
    Aplica detector de bordes Canny
    """
    return cv2.Canny(image, threshold1, threshold2)

def laplacian_filter(image):
    """
    Aplica filtro Laplaciano para resaltar bordes y detalles
    Resalta: bordes y regiones de rápida variación de intensidad
    """
    return cv2.Laplacian(image, cv2.CV_64F)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar imagen en escala de grises
    image = cv2.imread('../data/ejemplo1.jpg', 0)
    
    # Kernel de ejemplo (filtro de suavizado)
    kernel = np.ones((5,5), np.float32)/25
    
    # Aplicar convolución
    convolved = convolve(image, kernel)
    
    # Aplicar Sobel
    sobel_x_result = sobel_x(image)
    sobel_y_result = sobel_y(image)
    
    # Aplicar Canny
    edges = canny_edge_detector(image)
    
    # Aplicar Laplaciano
    laplacian = laplacian_filter(image)
    
    print("Filtros aplicados exitosamente")
