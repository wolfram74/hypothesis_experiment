class Vector:
    def __init__(self, input_vals):
        values2 = input_vals
        self.values = input_vals

    def __str__(self):
        return ', '.join(
            map(str, self.values)
            )

    def scalar_mult(self, scalar):
        for val_index in range(len(self.values)):
            self.values[val_index]*=scalar

vec1 = Vector([1,2,3])
print(vec1)
print(vec1.values)
print(vec1.scalar_mult(3))
print(vec1.values)
