from manim import *
import math
# config.background_color = WHITE
config.tex_template = TexTemplateLibrary.simple

class TestingABC(Rectangle):
    def __init__(
            self, 
            height=2, 
            width=4, 
            grid_xstep=None, 
            color = '#FFFFFF', 
            **kwargs
    ):
        super().__init__(color=color, height=height, width=width, grid_xstep=grid_xstep, **kwargs)

    def pointwise_become_partial(self, vmobject, a, b):
        print(a, b)
        self.set_points([[0,0,0], [0,0,0]])

class MyAnimation(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)


    def interpolate_mobject(self, alpha):
        print(alpha)
        if alpha < 0.2:
            self.mobject.set_color(WHITE)
        elif alpha < 0.5: 
            self.mobject.set_color(BLUE)
        elif alpha < 0.7: 
            self.mobject.set_color(RED)
        elif alpha < 0.9: 
            self.mobject.set_color(GREEN)
        else:
            self.mobject.set_color(BLACK)




class AnIntroToAlgs(Scene):
    def construct(self):
        array = TestingABC(color='#FFFFFF', height=1, width=5, grid_xstep=1)
        self.play(MyAnimation(array))
        self.wait()

class TimeGraph(Scene):
    def construct(self):
        x_top = 10
        y_top = 10**4

        ax = Axes(
            x_range=[0, x_top, x_top/10],
            y_range=[0, y_top, y_top/10],
            # x_axis_config={"numbers_to_include": np.arange(0, x_top+1, x_top/10), "include_ticks": False},
            # y_axis_config={"unit_size": 10**3}, 
            # y_length = round(config.frame_height / 2),
            # x_length = round(config.frame_width / 2),
            # tips=False,
        )

        labels = ax.get_axis_labels("People", "Seconds")

        curve = ax.get_graph(lambda x: 100 * x**2, x_range=[0,9], color=BLUE_C)

        # line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        # area_1 = ax.get_area(curve_1, x_range=[0.3, 0.6], dx_scaling=40, color=BLUE)
            
        # ax.x_axis.add_numbers([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        
        group = VGroup(ax, labels, curve)
        group.scale(0.5)
        
        

        self.play(Create(ax))
        self.play(Create(labels))
        self.play(Create(curve))
        # self.play(Create(group, run_time=2))
        self.wait()

def ParallelCreateLine(line=None, lag_ratio = 1.0, run_time = 1.0, **kwargs):
    run_time = run_time * 2
    copy = Line(line.get_start(), line.get_end())
    g = VGroup(line, copy)
    return Create(g, lag_ratio, run_time = run_time)

class ConnectPeople(Scene):
    def construct(self):
        names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Faythe"] 
        people = []
        distance = 3
        for i in range(6): 
            col = i % 3
            row = -(i // 3)
            person = Tex(names[i]).move_to([distance * col, distance * row, 0 ])
            people.append(person)

        group = VGroup(*people)
        group.center()

        lines = []
        lines.append(Line(people[2].get_edge_center(DOWN), people[5].get_edge_center(UP)).scale(0.6))
        # lines.append(Line(people[5].get_edge_center(UP), people[2].get_edge_center(DOWN)).scale(0.6))
        lines.append(Line(people[0].get_edge_center(RIGHT), people[1].get_edge_center(LEFT)).scale(0.6))
        # lines.append(Line(people[1].get_edge_center(LEFT), people[0].get_edge_center(RIGHT)).scale(0.6))
        lines.append(Line(people[0].get_edge_center(DR), people[4].get_edge_center(UL)).scale(0.6))
        # lines.append(Line(people[4].get_edge_center(UL), people[0].get_edge_center(DR)).scale(0.6))



        self.play(*map(FadeIn, people))
        self.play(*map(ParallelCreateLine, lines))

        # stickmen = []
        # for i in range(6):
        #     col = i % 3
        #     row = i // 3
        #     man = ImageMobject("./stick_1.png").set_color(WHITE).move_to([2 * col, 2 * row, 0 ])
        #     stickmen.append(man)

        # line = Line(stickmen[2].get_edge_center(UP), stickmen[5].get_edge_center(DOWN))
        # line = Line(stickmen[0].get_edge_center(RIGHT), stickmen[1].get_edge_center(LEFT))
        # line = Line(stickmen[0].get_edge_center(UR), stickmen[4].get_edge_center(DL))
        
        # self.play(*map(FadeIn, stickmen))
        # self.play(Create(line))

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


