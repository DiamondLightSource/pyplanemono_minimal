import unittest
from pyplanemono_minimal.elements.grating import Grating
from pyplanemono_minimal.geometry import Point3D, Vector3D, Ray3D

class TestGrating(unittest.TestCase):

    def setUp(self):
        # Create a Grating instance with default values
        self.grating = Grating()

    def test_line_density(self):
        # Test if line density is set correctly
        self.grating.line_density = 800
        self.assertEqual(self.grating.line_density, 800)

    def test_energy(self):
        # Test if energy is set correctly
        self.grating.energy = 3000
        self.assertEqual(self.grating.energy, 3000)

    def test_cff(self):
        # Test if cff is set correctly
        self.grating.cff = 3
        self.assertEqual(self.grating.cff, 3)

    def test_order(self):
        # Test if order is set correctly
        self.grating.order = 2
        self.assertEqual(self.grating.order, 2)

    def test_dimensions(self):
        # Test if dimensions are set correctly
        dimensions = [250, 50, 60]
        self.grating.dimensions = dimensions
        self.assertEqual(self.grating.dimensions, dimensions)

    def test_borders(self):
        # Test if borders are set correctly
        borders = [10, 20, 30, 40]
        self.grating.borders = borders
        self.assertEqual(self.grating.borders, borders)

    def test_set_angles(self):
        # Test if angles are set correctly
        self.grating.set_angles(30, 45)
        self.assertEqual(self.grating.alpha, 30)
        self.assertEqual(self.grating.beta, 45)

    def test_compute_corners(self):
        # Test if corners are computed correctly
        corners = self.grating.compute_corners()
        self.assertEqual(len(corners), 8)

    def test_diffract(self):
        # Test if rays are diffracted correctly
        ray1 = Ray3D(Point3D(0, 0, 0), Vector3D(1, 0, 0))
        ray2 = Ray3D(Point3D(0, 0, 0), Vector3D(0, 1, 0))
        diffracted_rays = self.grating.diffract(ray1, ray2)
        self.assertEqual(len(diffracted_rays), 2)

    def test_reflect(self):
        # Test if rays are reflected correctly
        ray1 = Ray3D(Point3D(0, 0, 0), Vector3D(1, 0, 0))
        ray2 = Ray3D(Point3D(0, 0, 0), Vector3D(0, 1, 0))
        reflected_rays = self.grating.reflect(ray1, ray2)
        self.assertEqual(len(reflected_rays), 2)

if __name__ == '__main__':
    unittest.main()