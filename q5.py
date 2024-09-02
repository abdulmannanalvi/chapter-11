class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        result = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to calculate dot product.")
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def __repr__(self):
        return f"Vector{self.components}"

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = v1 + v2  # Vector addition
dot_product = v1 * v2  # Dot product

print(f"v1 + v2 = {v3}")
print(f"v1 . v2 = {dot_product}")
