import unittest
import vector
import random
# from hypothesis import * # bad move, hard to deduce later
import hypothesis

class TestVectorClass(unittest.TestCase):

    @hypothesis.strategies.composite
    def arbitrary_vector(draw):
        output = []
        for loop in range(3):
            output.append(
                draw(
                    hypothesis.strategies.floats(min_value=-.2, max_value=2.0)
                    )
                )
        return vector.Vector(output)

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

    @hypothesis.given(
        scalar=hypothesis.strategies.floats(
            min_value=-.2, max_value=2.0
            )
        )
    def test_vector_magnitude(self, scalar):
        vec1 = vector.Vector([3,2,-7])
        # scalar = 3.4-random.random()*4
        first_mag = vec1.magnitude()
        vec1.scalar_mult(scalar)
        difference = first_mag*abs(scalar)-vec1.magnitude()
        # print(scalar, vec1.values, vec1.magnitude(), first_mag*scalar)
        if scalar != 0:
            rel_err = abs(difference/vec1.magnitude())
            self.assertLess(rel_err, 10**-12)
        else:
            self.assertEqual(0, vec1.magnitude())

    # @hypothesis.given(
    #     vec1=hypothesis.strategies.lists(
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0),
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0),
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0)
    #         ),
    #     vec2=hypothesis.strategies.lists(
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0),
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0),
    #         hypothesis.strategies.floats(min_value=-.2, max_value=2.0)
    #         )
    #     )
    @hypothesis.given(
        vec1=arbitrary_vector(),
        vec2=arbitrary_vector()
        )
    def test_dot_product(self, vec1, vec2):
        self.assertLessEqual(
            vec1.dot(vec2),
            vec1.magnitude()*vec2.magnitude()
            )

if __name__ == "__main__":
    unittest.main()
