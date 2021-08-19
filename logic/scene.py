from manim import *


class SimpleExpression(Scene):
    def construct(self):
        exp = MathTex(r"p \land (q \lor r) = (p \land q) \lor (p \land r)")
        self.play(Write(exp))



