import unittest
import numpy as np
import sys
import cv2

sys.path.append('../')
from cvtools.color import rgb_to_hsv, rgb_to_lab, quantize_image

class TestColor(unittest.TestCase):
    
    def setUp(self):
        self.sample_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    
    def test_rgb_to_hsv(self):
        hsv = rgb_to_hsv(self.sample_image)
        self.assertEqual(hsv.shape, self.sample_image.shape)
    
    def test_rgb_to_lab(self):
        lab = rgb_to_lab(self.sample_image)
        self.assertEqual(lab.shape, self.sample_image.shape)
    
    def test_quantize_image(self):
        quantized = quantize_image(self.sample_image, 16)
        self.assertEqual(quantized.shape, self.sample_image.shape)
        
        # Verificar que tiene menos colores únicos
        unique_colors = len(np.unique(quantized.reshape(-1, quantized.shape[2]), axis=0))
        self.assertLessEqual(unique_colors, 16)

if __name__ == '__main__':
    unittest.main()
