import unittest
import numpy as np
import sys

sys.path.append('../')
from cvtools.filters import convolve, sobel_x, sobel_y, canny_edge_detector, laplacian_filter

class TestFilters(unittest.TestCase):
    
    def setUp(self):
        self.sample_image = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
    
    def test_convolve(self):
        kernel = np.ones((3,3), np.float32)/9
        result = convolve(self.sample_image, kernel)
        self.assertEqual(result.shape, self.sample_image.shape)
    
    def test_sobel_x(self):
        result = sobel_x(self.sample_image)
        self.assertEqual(result.shape, self.sample_image.shape)
    
    def test_sobel_y(self):
        result = sobel_y(self.sample_image)
        self.assertEqual(result.shape, self.sample_image.shape)
    
    def test_canny(self):
        result = canny_edge_detector(self.sample_image)
        self.assertEqual(result.shape, self.sample_image.shape)
    
    def test_laplacian(self):
        result = laplacian_filter(self.sample_image)
        self.assertEqual(result.shape, self.sample_image.shape)

if __name__ == '__main__':
    unittest.main()
