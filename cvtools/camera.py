import numpy as np
import cv2

def radial_distortion(points, k1, k2):
    """
    Aplica distorsión radial a puntos proyectados
    
    Args:
        points: array de puntos (N, 2) en coordenadas de imagen
        k1: coeficiente de distorsión radial 1
        k2: coeficiente de distorsión radial 2
    
    Returns:
        puntos distorsionados (N, 2)
    """
    points = np.array(points, dtype=np.float32)
    distorted_points = []
    
    for x, y in points:
        r2 = x**2 + y**2
        r4 = r2**2
        distortion = 1 + k1 * r2 + k2 * r4
        
        x_distorted = x * distortion
        y_distorted = y * distortion
        
        distorted_points.append([x_distorted, y_distorted])
    
    return np.array(distorted_points)

def change_focal_length(points, original_focal, new_focal):
    """
    Cambia la longitud focal y ajusta los puntos proyectados
    
    Args:
        points: array de puntos (N, 2)
        original_focal: longitud focal original
        new_focal: nueva longitud focal
    
    Returns:
        puntos ajustados (N, 2)
    """
    points = np.array(points, dtype=np.float32)
    scale = new_focal / original_focal
    
    return points * scale

# Ejemplo de uso
if __name__ == "__main__":
    # Puntos de ejemplo
    points = np.array([[100, 100], [200, 150], [300, 200]])
    
    # Aplicar distorsión radial
    distorted = radial_distortion(points, k1=0.1, k2=0.01)
    print("Puntos distorsionados:", distorted)
    
    # Cambiar longitud focal
    adjusted = change_focal_length(points, 500, 800)
    print("Puntos con nueva focal:", adjusted)
