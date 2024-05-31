import unittest
from pyplanemono_minimal.elements import PGM, Plane_Mirror, Grating

class TestPGM(unittest.TestCase):

    def setUp(self):
        # Create a PGM instance with default values
        self.pgm = PGM()

    def test_generate_rays(self):
        # Test if rays are generated correctly
        self.pgm.generate_rays()
        self.assertEqual(len(self.pgm.rays), 5)

    def test_set_theta(self):
        # Test if theta is set correctly
        self.pgm.set_theta()
        self.assertEqual(self.pgm.theta, 0.5 * (self.pgm.grating.alpha - self.pgm.grating.beta))

    def test_energy(self):
        # Test if energy is set correctly
        self.pgm.energy = 2000
        self.assertEqual(self.pgm.energy, 2000)

    def test_grating(self):
        # Test if grating is set correctly
        grating = Grating(line_density=1000, energy=2000, cff=2, order=1, dimensions=(10, 10))
        self.pgm.grating = grating
        self.assertEqual(self.pgm.grating, grating)

    def test_mirror(self):
        # Test if mirror is set correctly
        mirror = Plane_Mirror(voffset=1, hoffset=2, axis_voffset=3, axis_hoffset=4, dimensions=(10, 10), theta=0.5)
        self.pgm.mirror = mirror
        self.assertEqual(self.pgm.mirror, mirror)

    def test_propagate(self):
        # Test if rays are propagated correctly
        self.pgm.generate_rays()
        grating_ray, mirror_intercept, grating_intercept = self.pgm.propagate(*self.pgm.rays)
        self.assertEqual(len(grating_ray), 5)
        self.assertEqual(len(mirror_intercept), 5)
        self.assertEqual(len(grating_intercept), 5)

if __name__ == '__main__':
    unittest.main()