import unittest
import vector

class TestVectorClass(unittest.TestCase):
    def test_meta(self):
        self.assertTrue(True)

    def test_scalar_mult(self):
        vec = vector.Vector([1,2,0])
        vec.scalar_mult(3)
        self.assertEqual(3, vec.values[0])
        self.assertEqual(6, vec.values[1])
        self.assertEqual(1, vec.values[2])


if __name__ == "__main__":
    unittest.main()
