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

def create_textbox(string):
    # https://stackoverflow.com/questions/70142914/how-to-put-text-inside-a-rectangle-in-manim-community
    result = VGroup()
    box = Square()
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result


class BubbleSort(Scene):
    def construct(self):
        # plane = NumberPlane().add_coordinates()
        sq_1 = create_textbox("5").shift(4*LEFT)
        sq_2 = create_textbox("3").next_to(sq_1, RIGHT)
        sq_3 = create_textbox("1").next_to(sq_2, RIGHT)
        sq_4 = create_textbox("2").next_to(sq_3, RIGHT)
        sq_5 = create_textbox("4").next_to(sq_4, RIGHT)

        # self.add(plane)
        self.add(sq_1, sq_2, sq_3, sq_4, sq_5)

        self.play(sq_1.animate.shift(2.1*UP))
        self.play(sq_2.animate.shift(LEFT * 2.2))
        self.play(sq_1.animate.shift(RIGHT * 2.2))
        self.play(sq_1.animate.shift(2.1 *DOWN))

        self.play(sq_1.animate.shift(2.1*UP))
        self.play(sq_3.animate.shift(LEFT * 2.2))
        self.play(sq_1.animate.shift(RIGHT * 2.3))
        self.play(sq_1.animate.shift(2.1 *DOWN))

        self.play(sq_1.animate.shift(2.1*UP))
        self.play(sq_4.animate.shift(LEFT * 2.2))
        self.play(sq_1.animate.shift(RIGHT * 2.3))
        self.play(sq_1.animate.shift(2.1 *DOWN))

        self.play(sq_1.animate.shift(2.1 *UP))
        self.play(sq_5.animate.shift(LEFT * 2.2))
        self.play(sq_1.animate.shift(RIGHT * 2.3))
        self.play(sq_1.animate.shift(2.1 *DOWN))

        self.play(sq_2.animate.shift(2.1 *UP))
        self.play(sq_3.animate.shift(LEFT * 2.2))
        self.play(sq_2.animate.shift(RIGHT * 2.3))
        self.play(sq_2.animate.shift(2.1 *DOWN))

        self.play(sq_2.animate.shift(2.1 *UP))
        self.play(sq_4.animate.shift(LEFT * 2.2))
        self.play(sq_2.animate.shift(RIGHT * 2.3))
        self.play(sq_2.animate.shift(2.1 *DOWN))

        self.wait()


class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Booolean Operations</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height*3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))


class BuffTest(Scene):
    def construct(self):
        plane = NumberPlane()
        sq_1 = Square(color=GREEN, fill_opacity=0.5)
        sq_2 = Square(color=YELLOW, fill_opacity=0.5).next_to(sq_1, RIGHT, buff=0)
        sq_3 = Square(color=RED, fill_opacity=0.5).next_to(sq_2, RIGHT)
        sq_4 = Square(color=PINK, fill_opacity=0.5).next_to(sq_1, LEFT, buff=1)

        self.add(sq_1)
        self.add(sq_2)
        self.add(sq_3)
        self.add(sq_4)
        self.add(plane)

class ObjectPosition(Scene):
    def construct(self):
        plane = NumberPlane()

        sq = Square(color=PINK, fill_opacity=0.7).move_to([1.0, 1.0, 0])
        self.add(plane)
        self.add(sq)

class PointMovingOnSquare(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()

class AddAndSubstractVisualizer(Scene):
    def construct(self):
        plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_opacity": 0.2
            }
        ).add_coordinates(range(-7, 7, 1))
        dot = Dot([0, 0, 0], color=GREEN)
        t1 = Text("+2", color=GREEN).move_to(2*UP)
        t2 = Text("+3", color=GREEN).move_to(2*UP)
        t3 = Text("-4", color=RED).move_to(2*UP)


        self.add(plane)

        self.play(Write(t1))
        self.play(dot.animate.move_to(RIGHT*2))
        self.play(FadeOut(t1))

        self.play(Write(t2))
        self.play(dot.animate.move_to(RIGHT*5))
        self.play(FadeOut(t2))

        self.play(Write(t3))
        self.play(dot.animate.move_to(RIGHT))
        self.play(dot.animate.set_color(RED))
        self.play(FadeOut(t3))

        self.wait()

class PIVisualization(Scene):
    def construct(self):
        circ  = Circle(color=WHITE)
        lin = Line(color=RED).move_to(UP*2)
        lin2= Line(color=GREEN).next_to(lin, RIGHT)
        lin3= Line(color=BLUE).next_to(lin2, RIGHT)
        lin4= Line(color=YELLOW).next_to(lin3, RIGHT).set_length(0.28318530717958623)

        arc = Arc(start_angle=0, angle=2).set_color(GREEN)
        arc2= Arc(start_angle=2, angle=2).set_color(RED)
        arc3= Arc(start_angle=4, angle=2).set_color(BLUE)
        arc4= Arc(start_angle=6, angle=0.28318530717958623).set_color(YELLOW)

        self.add(circ)

        self.add(lin, lin2, lin3, lin4)
        #self.add(arc, arc2, arc3, arc4)

        self.play(Transform(lin, arc2))
        self.play(Transform(lin2, arc))
        self.play(Transform(lin3, arc3))
        self.play(Transform(lin4, arc4))
        self.wait()

class LinearTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.add_title("Linear Transformation")
        self.apply_matrix(matrix)
        self.wait()
