from utils import find_modular_inverse


class FieldElement:
    field_modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583

    def __init__(self, val):
        self.val = val % self.field_modulus

    def __add__(self, other):
        return FieldElement((self.val + other.val) % self.field_modulus)

    def __mul__(self, other):
        return FieldElement((self.val * other.val) % self.field_modulus)

    def __sub__(self, other):
        return FieldElement((self.val - other.val) % self.field_modulus)

    def __div__(self, other):
        return FieldElement((self.val * find_modular_inverse(other.val, self.field_modulus)) % self.field_modulus)

