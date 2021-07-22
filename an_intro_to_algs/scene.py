from manim import *
# config.background_color = WHITE
config.tex_template = TexTemplateLibrary.simple

class AnIntroToAlgs(Scene):
    def construct(self):
        pass

# class GraphSTuff(Scene):
#     def construct(self):
# 	x = Axes(
#             x_range=[-2, 6], y_range=[-1, 5], axis_config={"include_tip": False}
#         )
#         plane = NumberPlane(
#             x_range = (-2, 6),
#             y_range = (-1, 5),
#             axis_config={"include_numbers": False, 
#             "color": RED,
#             },
#         )
#         plane.center()
    
#         self.add(plane)

#         def funcf(x):
#             return x**2 - 3*x + 2
#         graphf = ax.get_graph(funcf, color=BLUE)

#         def funcg(x):
#             return x**2 - 3
#         graphg = ax.get_graph(funcg, color=RED)

#         anno = [MathTex("f(t)"), MathTex("g(t)")]

#         x_values = [3, 2]
#         y_values = [2, 1]
#         z_values = [0, 1]
#         s_values = [2*RIGHT, 1.5*DOWN]
#         g_values = [graphf, graphg]

#         dots = VGroup()
#         for x, y, z, s, g in zip(x_values, y_values, z_values, s_values, g_values):
#           self.play(Write(g))
#           dot = Dot(plane.coords_to_point(x, y))
#           self.play(Write(dot))
#           self.play(Write(anno[z].shift(s)))
#           dots.add(dot)
#           self.wait()

class ConnectPeople(Scene):
    def construct(self):
        stickman = ImageMobject("./stick_1.png").set_color(WHITE)
        self.play(FadeIn(stickman))

class TimeCalculation(Scene):
    def construct(self):
        # my_template = TexTemplate()
        # my_template.add_to_preamble(r'\usepackage{xcolor}')

        lines = [
            MathTex(r"1.000.000.000 = ", "10^9", r"\text{ people}"),
            # Tex(r"people"), #, tex_template=my_template),
            Tex(r'10 connections per person $ = 10^{10}$ connections'),
            # Tex(r'10 operations per person per connection'),
            # Tex(r'4.6Ghz processor $= 4.6 \times 10^9$ operations per second'),
            # Tex(r"$10^9 \times 10 \times 10^{10} = 10^{20}$ operations"),
            # Tex(r"$\frac{10^{20}}{4.6\times 10^9} = 2.1939\times 10^{10} = $"),
            # Tex("688 years 316 days 19 hours")
        ]

        lines[0].align_on_border(UP).shift(LEFT * 2)
        # lines[1].next_to(lines[0], RIGHT)
        # lines[2].next_to(lines[0], DOWN, aligned_edge=LEFT)


        for i in range(1, len(lines)):
            lines[i].next_to(lines[i-1], DOWN, aligned_edge=LEFT) 

        speed_multi = 0.2
        animation = Write

        for line in lines:
            self.play(animation(line, run_time = speed_multi * line.width))

        self.play(lines[0].animate.set_color_by_tex(r"10^9", color=YELLOW))
        
        # animations = []
        # for line in lines:
        #     animations.append(ApplyMethod(line.scale, 0.2))
        #     animations.append(ApplyMethod(line.shift, 2 * (UP+RIGHT)))
        # print(animations)
        # self.play(*animations)
        
        # operations_total_text = Tex("Operations in total:").next_to(operations_num, DOWN).shift(DOWN)
        # operations_total_calc = MathTex(r"10^9 people \times 10 operations per person \times 10^{10} joins = (10^{10})^2 = 10^{20}").next_to(operations_total_text, DOWN)
           
        # seconds_calc = MathTex(r"\frac{10^{20}}{4.6\times 10^9} = 2.1939\times 10^{10} = ").next_to(operations_per_sec_text, DOWN)
        # years_text = Tex("688 years 316 days 19 hours").next_to(seconds_calc, DOWN, aligned_edge=LEFT)
        

        # self.add(Group(people_num, join_num, operations_num, operations_total_text, operations_per_sec_text,
        #     seconds_calc, years_text).arrange(DOWN).align(LEFT))
        # self.add(stickman)
        # self.add(join_text)
        # self.add(operations_text)
        # self.wait()


        # test = Tex("Hello ", r"$x^2 = x\cdot x$")
        # self.play(Write(test))

        # self.play(Write(full_text, run_time=6))

        # self.play(Write(people_num))
        # self.add(stickman)
        # self.play(Write(join_num))
        # self.play(Write(join_text))
        # self.play(Write(operations_num))
        # self.play(Write(operations_text))
        # self.play(Write(operations_total_text))
        # self.play(Write(operations_total_calc))
        # self.play(Write(operations_per_sec_text))
        # self.play(Write(seconds_calc))
        # self.play(Write(years_text))
        
        
        
        
            

        # graph = NumberPlane(x_range=[-1, 5, 1], y_range=[-1, 5, 1]) #x_length=100, y_length=100)
        # dot = Dot(graph.get_center_point())
        # self.play(FadeIn(graph))
        # self.play(FadeIn(dot))
        # self.wait()

class CanWeDoBetter(Scene):
    def construct(self):
        
        but_text = Text("But")
        dot_text = Text("...").next_to(but_text).shift(0.1*LEFT + 0.2*DOWN)
        do_better_text = Text("Can we do better?")


        self.add(but_text)
        self.wait(1)
        self.play(AddTextLetterByLetter(dot_text,run_time=2.5))
        self.wait(1)
        self.remove(but_text)
        self.remove(dot_text)
        self.add(do_better_text)
        self.wait(1)


class Array(Scene):
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


