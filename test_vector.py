import unittest
import vector
import random

class TestVectorClass(unittest.TestCase):
    def test_meta(self):
        self.assertTrue(True)

    def test_scalar_mult(self):
        vec = vector.Vector([1,2,0])
        vec2 = vector.Vector([3,2,-7])
        vec.scalar_mult(3)
        self.assertEqual(3, vec.values[0])
        self.assertEqual(6, vec.values[1])
        self.assertEqual(0, vec.values[2])
        vec2.scalar_mult(-.5)
        self.assertEqual(-1.5, vec2.values[0])
        self.assertEqual(-1.0, vec2.values[1])
        self.assertEqual(3.5, vec2.values[2])

    def test_vector_magnitude(self):
        vec1 = vector.Vector([3,2,-7])
        scalar = 3.4-random.random()*4
        first_mag = vec1.magnitude()
        vec1.scalar_mult(scalar)
        difference = first_mag*scalar-vec1.magnitude()
        print(scalar)
        rel_err = abs(difference/vec1.magnitude())
        self.assertLess(rel_err, 10**-12)

if __name__ == "__main__":
    unittest.main()
