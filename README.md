# Integration of the wavelike equations

In this code, we address the solution of a wave-like equation that arises from perturbing a black hole, utilizing the Einstein-Hilbert action. The specific equation under consideration is as follows:
$$\frac{\partial^2 \Phi}{\partial t^2} - \frac{\partial^2 \Phi}{\partial x^2} + V(x) \Phi = 0$$

Here, $x$ represents the tortoise coordinate, $t$ denotes the time coordinate, and $V(x)$ characterizes the potential governing the perturbation of the black hole. In this instance, the potential $V(x)$ corresponds to the Regge-Wheeler potential.

The solution to this wave-like equation is performed within the light-cone coordinates $(u, v)$ given by: $u = t - x$ and $v = t + x$.
These coordinates are particularly useful for analyzing the disturbance's dynamics. They break down the behavior into two components: 
$du$, representing inward-moving characteristics, and $dv$, representing outward-moving characteristics. This separation simplifies our analysis and aids in interpreting the disturbance's behavior.

## References 

Section III.E of [Konoplya and Zhidenko](https://arxiv.org/abs/1102.4014v2)
