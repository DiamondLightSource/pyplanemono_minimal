import unittest
from pyplanemono_minimal.elements.mirror import Plane_Mirror
from pyplanemono_minimal.geometry import Ray3D, Point3D, Vector3D
class TestPlaneMirror(unittest.TestCase):

    def setUp(self):
        # Create a Plane_Mirror instance with default values
        self.mirror = Plane_Mirror()

    def test_set_position(self):
        # Test if position is set correctly
        position = Point3D(1, 2, 3)
        self.mirror.set_position(position)
        self.assertEqual(self.mirror.plane.position, position)

    def test_set_normal(self):
        # Test if normal is set correctly
        normal = Vector3D(0, 0, 1)
        self.mirror.set_normal(normal)
        self.assertEqual(self.mirror.plane.normal, normal)

    def test_set_dimensions(self):
        # Test if dimensions are set correctly
        dimensions = [450, 70, 50]
        self.mirror.set_dimensions(dimensions)
        self.assertEqual(self.mirror.dimensions, dimensions)

    def test_set_offsets(self):
        # Test if offsets are set correctly
        voffset = 13
        hoffset = 40
        axis_voffset = 6.5
        axis_hoffset = 0
        self.mirror.set_offsets(voffset, hoffset, axis_voffset, axis_hoffset)
        self.assertEqual(self.mirror.voffset, voffset)
        self.assertEqual(self.mirror.hoffset, hoffset)
        self.assertEqual(self.mirror.axis_voffset, axis_voffset)
        self.assertEqual(self.mirror.axis_hoffset, axis_hoffset)

    def test_compute_corners(self):
        # Test if corners are computed correctly
        corners = self.mirror.compute_corners()
        self.assertEqual(len(corners), 8)

    def test_reflect(self):
        # Test if rays are reflected correctly
        ray1 = Ray3D(Point3D(0, 0, 0), Vector3D(1, 0, 0))
        ray2 = Ray3D(Point3D(0, 0, 0), Vector3D(0, 1, 0))
        reflected_rays = self.mirror.reflect(ray1, ray2)
        self.assertEqual(len(reflected_rays), 2)
        self.assertIsInstance(reflected_rays[0], Ray3D)
        self.assertIsInstance(reflected_rays[1], Ray3D)

if __name__ == '__main__':
    unittest.main()