# Numerical solution of Black Hole Perturbations in Light-Cone Coordinates - The quasinormal modes

In this computational study, we embark on a detailed exploration of the numerical solution for a wave-like equation that arises from perturbing a black hole, employing the Einstein-Hilbert action. The specific equation under consideration is given by:

$$\frac{\partial^2 \Phi}{\partial t^2} - \frac{\partial^2 \Phi}{\partial x^2} + V(x) \Phi = 0$$

Where $x$ is the tortoise coordinate and $t$ represents the time coordinate. The potential $V(x)$ encapsulates the underlying physics governing the perturbation dynamics of the black hole. In this instance, the Regge-Wheeler potential is employed, a choice that allows for a comprehensive understanding of the system's behavior.

The numerical solution to this wave-like equation is pursued within the light-cone coordinates $(u, v)$, which are defined as $u = t - x$ and $v = t + x$. These coordinates are a powerful tool for analyzing the dynamics of perturbation near the black hole. They effectively segregate the behavior into the inward-moving characteristic $du$ and the outward-moving characteristic $dv$. This separation greatly simplifies our analysis, facilitating a more explicit interpretation of the perturbation's behavior.

## About the Code

The code implementation commences by defining the potential in terms of the radial coordinates, subsequently calculating it in both the spatial $x$-coordinates and the light-cone $uv$-coordinates. This dual representation allows for a comprehensive examination of the perturbation dynamics.

The code introduces a small Gaussian pulse at $t=0$. This serves as the initial condition, from which the simulation proceeds to track the evolution of the perturbation over time. Through each time step, the code accurately computes the state of the system based on its previous state, employing a second-order finite difference scheme.

## Output and Visualization

The code generates a two-dimensional grid with dimensions $npoints \times npoints$, comprehensively representing the perturbation field. The output is further visualized through a plot, depicting the evolution of the perturbation. Notably, this visualization is presented while holding the radial coordinates fixed at a value of $10 \times rs$. This choice of visualization aids in capturing the nuances of the perturbation's evolution at a specific radial distance from the black hole.

## References 

Section III.E of [Konoplya and Zhidenko](https://arxiv.org/abs/1102.4014v2)
