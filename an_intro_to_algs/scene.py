from manim import *

class AnIntroToAlgs(Scene):
    def construct(self):
        width = 6

        rectangle = Rectangle(width=width, height=1.0, grid_xstep=1.0)

        top_line = Line(UP, UP + RIGHT*width)
        left_line = Line(UP, ORIGIN)
        bottom_line = Line(ORIGIN, RIGHT*width)
        right_line = Line(UP + RIGHT * width, RIGHT*width)
        inner_lines = [Line(UP + i * RIGHT, i * RIGHT) for i in range(1, width)]

        array = VGroup(top_line, left_line, bottom_line, right_line, *inner_lines)
        array.shift(3*LEFT+0.5*DOWN)

        # self.add(start_dot)
        # self.play(DrawBorderThenFill(array,)

        # self.play(Create(top_line, run_time=0.5), Create(left_line,run_time=0.5))
        # self.play(Create(bottom_line,run_time=0.5), Create(right_line,run_time=0.5))
        # self.play(*map(lambda l: Create(l, run_time=0.5), inner_lines))
        # self.play(Transform(start_dot, top_line), duration=5.0)
        # self.play(Transform(top_line, array), duration=5.0)
        # self.remove(array)
        # self.add(rectangle)

        self.play(DrawBorderThenFill(rectangle, run_time=2))

