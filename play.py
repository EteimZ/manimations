from manim import *

# Playful manim scripts

class SquareOnPlane(Scene):
    def construct(self):
        square = Square(side_length=1.0, fill_color=GREEN, fill_opacity=0.5 ).move_to(0.5)
        plane = NumberPlane().add_coordinates()

        self.add(plane)
        self.play(square.animate.shift(RIGHT))
        self.wait()


class ManimLogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        self.play(Create(triangle))
        self.play(Create(square))
        self.play(Create(circle))
        self.play(Create(ds_m))
        self.wait()


class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(RED)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")

        self.add(line, b1, b2,  dot, dot2, b1text, b2text)


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [3, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(3, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


class LoadImage(Scene):
    def construct(self):
        image = ImageMobject("arduino-logo-1.png").scale(0.5)
        self.add(image)

