import unittest
import numpy as np
import sys
import os

sys.path.append('../')
from cvtools.camera import radial_distortion, change_focal_length

class TestCamera(unittest.TestCase):
    
    def test_radial_distortion(self):
        points = np.array([[100, 100], [200, 200]])
        distorted = radial_distortion(points, 0.1, 0.01)
        
        self.assertEqual(distorted.shape, points.shape)
        self.assertIsInstance(distorted, np.ndarray)
    
    def test_change_focal_length(self):
        points = np.array([[100, 100], [200, 200]])
        adjusted = change_focal_length(points, 500, 800)
        
        self.assertEqual(adjusted.shape, points.shape)
        self.assertTrue(np.all(adjusted > points))  # Debería escalar hacia arriba

if __name__ == '__main__':
    unittest.main()
