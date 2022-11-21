from manim import *

class ExampleVector(VectorScene):
    def construct(self):
        self.add_axes()
        self.add_plane()
        self.get_basis_vectors()
