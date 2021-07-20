from manim import * 

class SquareToCircle(Scene):
    def construct(self): 
        circle = Circle()
        square = Square()
        triangle = Triangle()

        text = Text("Alice")

        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1,1, 0]
        p4 = [-1, 1, 0]

        a = Line(p1, p2).append_points(Line(p2, p3).get_points())

        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeIn(circle), FadeIn(triangle), duration=2)
        self.wait(1)
        self.play(ApplyMethod(circle.shift, LEFT), ApplyMethod(triangle.shift, LEFT), duration=2)


        # self.wait(1)
        # self.add(a)
        # self.wait(1)
        # self.remove(a)
        # self.wait(1)


        tex_text = MathTex(r"\sum^{10}_{i=0}{i} = 55").shift(2*UP)
        #self.add(tex_text, Tex("こんいちは", tex_template=TexTemplateLibrary.ctex, color=BLUE).shift(2*DOWN))
        self.wait()
