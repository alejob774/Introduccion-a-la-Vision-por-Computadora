import cv2
import numpy as np
import matplotlib.pyplot as plt
from cvtools.camera import radial_distortion, change_focal_length
from cvtools.color import rgb_to_hsv, rgb_to_lab, plot_color_histogram, quantize_image, reduce_image_size
from cvtools.filters import convolve, sobel_x, sobel_y, canny_edge_detector, laplacian_filter

def main():
    print("=== Demostración de cvtools ===")
    
    # Cargar imagen de ejemplo
    try:
        image = cv2.imread('data/ejemplo1.jpg')
        if image is None:
            raise FileNotFoundError
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    except:
        print("Creando imagen de ejemplo...")
        image = np.random.randint(0, 255, (300, 400, 3), dtype=np.uint8)
        gray_image = np.random.randint(0, 255, (300, 400), dtype=np.uint8)
    
    # 1. Demostración módulo camera
    print("\n1. Módulo Camera:")
    points = np.array([[100, 100], [200, 150], [300, 200]])
    distorted = radial_distortion(points, 0.1, 0.01)
    focal_adjusted = change_focal_length(points, 500, 800)
    print("   Distorsión radial y cambio de focal aplicados")
    
    # 2. Demostración módulo color
    print("\n2. Módulo Color:")
    hsv_image = rgb_to_hsv(image)
    lab_image = rgb_to_lab(image)
    quantized = quantize_image(image, 16)
    print("   Conversiones de color y cuantización completadas")
    
    # 3. Demostración módulo filters
    print("\n3. Módulo Filters:")
    kernel = np.ones((5,5), np.float32)/25
    convolved = convolve(gray_image, kernel)
    sobel_x_img = sobel_x(gray_image)
    sobel_y_img = sobel_y(gray_image)
    edges = canny_edge_detector(gray_image)
    laplacian = laplacian_filter(gray_image)
    print("   Filtros aplicados exitosamente")
    
    # 4. Mostrar algunos resultados
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.imshow(image)
    plt.title('Imagen Original')
    
    plt.subplot(2, 3, 2)
    plt.imshow(quantized)
    plt.title('Imagen Cuantizada (16 colores)')
    
    plt.subplot(2, 3, 3)
    plt.imshow(edges, cmap='gray')
    plt.title('Bordes Canny')
    
    plt.subplot(2, 3, 4)
    plt.imshow(np.abs(sobel_x_img), cmap='gray')
    plt.title('Sobel X')
    
    plt.subplot(2, 3, 5)
    plt.imshow(np.abs(sobel_y_img), cmap='gray')
    plt.title('Sobel Y')
    
    plt.subplot(2, 3, 6)
    plt.imshow(np.abs(laplacian), cmap='gray')
    plt.title('Laplaciano')
    
    plt.tight_layout()
    plt.savefig('resultados_demo.png')
    print("\nResultados guardados en 'resultados_demo.png'")
    
    # 5. Mostrar histograma
    plot_color_histogram(image)
    
    print("\n=== Demostración completada ===")

if __name__ == "__main__":
    main()
