from manim import *

class ThreeDGraph(Scene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-4, 4),
            y_range=(-4, 4),
            z_range=(-2, 2),
            axis_config={"color": BLUE},
        )

        # Create a parametric surface
        surface = ParametricSurface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=(-2, 2),
            v_range=(-2, 2),
            color=YELLOW,
        )

        # Show axes and surface
        self.play(Create(axes), Create(surface))

        # Move camera to view the 3D graph
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
