class Vector:
    def __init__(self, input_vals):
        values2 = input_vals
        self.values = map(float, input_vals)

    def __str__(self):
        return ', '.join(
            map(str, self.values)
            )

    def scalar_mult(self, scalar):
        for val_index in range(len(self.values)):
            self.values[val_index]*=scalar

    def magnitude(self):
        squares = map(lambda x: x**2, self.values)
        return sum(squares)**0.5
