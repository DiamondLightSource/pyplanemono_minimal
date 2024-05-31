import unittest
from pyplanemono_minimal.geometry import Vector3D

class TestVector3D(unittest.TestCase):

    def setUp(self):
        # Create a Vector3D instance with default values
        self.vector = Vector3D(1, 2, 3)

    def test_add(self):
        # Test vector addition
        other = Vector3D(4, 5, 6)
        result = self.vector + other
        self.assertEqual(result.x, 5)
        self.assertEqual(result.y, 7)
        self.assertEqual(result.z, 9)

    def test_subtract(self):
        # Test vector subtraction
        other = Vector3D(4, 5, 6)
        result = self.vector - other
        self.assertEqual(result.x, -3)
        self.assertEqual(result.y, -3)
        self.assertEqual(result.z, -3)

    def test_dot_product(self):
        # Test dot product
        other = Vector3D(4, 5, 6)
        result = self.vector * other
        self.assertEqual(result, 32)

    def test_cross_product(self):
        # Test cross product
        other = Vector3D(4, 5, 6)
        result = self.vector / other
        self.assertEqual(result.x, -3)
        self.assertEqual(result.y, 6)
        self.assertEqual(result.z, -3)

    def test_magnitude(self):
        # Test vector magnitude
        result = abs(self.vector)
        self.assertEqual(result, 3.7416573867739413)

    def test_negative(self):
        # Test vector negation
        result = -self.vector
        self.assertEqual(result.x, -1)
        self.assertEqual(result.y, -2)
        self.assertEqual(result.z, -3)

    def test_equality(self):
        # Test vector equality
        other = Vector3D(1, 2, 3)
        self.assertEqual(self.vector, other)

    def test_inequality(self):
        # Test vector inequality
        other = Vector3D(4, 5, 6)
        self.assertNotEqual(self.vector, other)

    def test_get_component(self):
        # Test getting vector component
        self.assertEqual(self.vector[0], 1)
        self.assertEqual(self.vector[1], 2)
        self.assertEqual(self.vector[2], 3)

    def test_set_component(self):
        # Test setting vector component
        self.vector[0] = 4
        self.vector[1] = 5
        self.vector[2] = 6
        self.assertEqual(self.vector.x, 4)
        self.assertEqual(self.vector.y, 5)
        self.assertEqual(self.vector.z, 6)

    def test_iterator(self):
        # Test vector iteration
        components = [component for component in self.vector]
        self.assertEqual(components, [1, 2, 3])

    def test_length(self):
        # Test vector length
        result = len(self.vector)
        self.assertEqual(result, 3)

    def test_hash(self):
        # Test vector hash
        result = hash(self.vector)
        self.assertIsInstance(result, int)

    def test_copy(self):
        # Test vector copy
        result = self.vector.copy()
        self.assertEqual(result.x, 1)
        self.assertEqual(result.y, 2)
        self.assertEqual(result.z, 3)

    def test_deepcopy(self):
        # Test vector deep copy
        import copy
        result = copy.deepcopy(self.vector)
        self.assertEqual(result.x, 1)
        self.assertEqual(result.y, 2)
        self.assertEqual(result.z, 3)

    def test_normalize(self):
        # Test vector normalization
        result = self.vector.normalize()
        self.assertAlmostEqual(result.x, 0.2672612419124244)
        self.assertAlmostEqual(result.y, 0.5345224838248488)
        self.assertAlmostEqual(result.z, 0.8017837257372732)

    def test_angle(self):
        # Test angle between vectors
        other = Vector3D(4, 5, 6)
        result = self.vector.angle(other)
        self.assertAlmostEqual(result, 0.2257261285527342)

    def test_rotate(self):
        # Test vector rotation
        axis = Vector3D(1, 1, 1)
        angle = 0.5
        result = self.vector.rotate(axis, angle)
        self.assertAlmostEqual(result.x, 1.0)
        self.assertAlmostEqual(result.y, 1.0)
        self.assertAlmostEqual(result.z, 1.0)

    def test_rotate_x(self):
        # Test vector rotation around x-axis
        angle = 0.5
        result = self.vector.rotate_x(angle)
        self.assertAlmostEqual(result.x, 1.0)
        self.assertAlmostEqual(result.y, -0.3660254037844386)
        self.assertAlmostEqual(result.z, 2.232050807568877)

    def test_rotate_y(self):
        # Test vector rotation around y-axis
        angle = 0.5
        result = self.vector.rotate_y(angle)
        self.assertAlmostEqual(result.x, 2.232050807568877)
        self.assertAlmostEqual(result.y, 2.0)
        self.assertAlmostEqual(result.z, -0.3660254037844386)

    def test_rotate_z(self):
        # Test vector rotation around z-axis
        angle = 0.5
        result = self.vector.rotate_z(angle)
        self.assertAlmostEqual(result.x, -0.3660254037844386)
        self.assertAlmostEqual(result.y, 2.232050807568877)
        self.assertAlmostEqual(result.z, 2.0)

if __name__ == '__main__':
    unittest.main()