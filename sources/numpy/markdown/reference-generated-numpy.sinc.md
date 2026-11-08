[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.sinc.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.sinc.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.sinc.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.sinc.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.sinc.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.sinc.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.sinc.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.sinc.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.sinc.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.sinc.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.sinc.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.sinc.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.sinc.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.sinc.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.sinc.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.sinc.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.sinc.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.sinc.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.sinc.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.sinc.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sinc[#](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy-sinc "Link to this heading")

==================================================================================================================

numpy.sinc(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3742-L3824)
[#](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy.sinc "Link to this definition")

Return the normalized sinc function.

The sinc function is equal to \\(\\sin(\\pi x)/(\\pi x)\\) for any argument \\(x\\ne 0\\). `sinc(0)` takes the limit value 1, making `sinc` not only everywhere continuous but also infinitely differentiable.

Note

Note the normalization factor of `pi` used in the definition. This is the most commonly used definition in signal processing. Use `sinc(x / np.pi)` to obtain the unnormalized sinc function \\(\\sin(x)/x\\) that is more common in mathematics.

Parameters:

**x**ndarray

Array (possibly multi-dimensional) of values for which to calculate `sinc(x)`.

Returns:

**out**ndarray

`sinc(x)`, which has the same shape as the input.

Notes

The name sinc is short for “sine cardinal” or “sinus cardinalis”.

The sinc function is used in various signal processing applications, including in anti-aliasing, in the construction of a Lanczos resampling filter, and in interpolation.

For bandlimited interpolation of discrete-time signals, the ideal interpolation kernel is proportional to the sinc function.

**Array API Standard Support**

[`sinc`](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy.sinc "numpy.sinc")
 has experimental support for Python Array API Standard compatible backends in addition to NumPy. Please consider testing these features by setting an environment variable `SCIPY_ARRAY_API=1` and providing CuPy, PyTorch, JAX, or Dask arrays as array arguments. The following combinations of backend and device (or other capability) are supported.

| Library | CPU | GPU |
| --- | --- | --- |
| NumPy | ✅   | n/a |
| CuPy | n/a | ✅   |
| PyTorch | ✅   | ✅   |
| JAX | ✅   | ⛔   |
| Dask | ✅   | n/a |

See [Support for the array API standard](https://docs.scipy.org/doc/scipy/dev/api-dev/array_api.html#dev-arrayapi "(in SciPy v1.18.0)")
 for more information.

References

\[1\]

Weisstein, Eric W. “Sinc Function.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/SincFunction.html](https://mathworld.wolfram.com/SincFunction.html)

\[2\]

Wikipedia, “Sinc function”, [https://en.wikipedia.org/wiki/Sinc\_function](https://en.wikipedia.org/wiki/Sinc_function)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> x \= np.linspace(\-4, 4, 41)
\>>> np.sinc(x)
 array(\[-3.89804309e-17,  -4.92362781e-02,  -8.40918587e-02, # may vary\
        -8.90384387e-02,  -5.84680802e-02,   3.89804309e-17,\
        6.68206631e-02,   1.16434881e-01,   1.26137788e-01,\
        8.50444803e-02,  -3.89804309e-17,  -1.03943254e-01,\
        -1.89206682e-01,  -2.16236208e-01,  -1.55914881e-01,\
        3.89804309e-17,   2.33872321e-01,   5.04551152e-01,\
        7.56826729e-01,   9.35489284e-01,   1.00000000e+00,\
        9.35489284e-01,   7.56826729e-01,   5.04551152e-01,\
        2.33872321e-01,   3.89804309e-17,  -1.55914881e-01,\
       -2.16236208e-01,  -1.89206682e-01,  -1.03943254e-01,\
       -3.89804309e-17,   8.50444803e-02,   1.26137788e-01,\
        1.16434881e-01,   6.68206631e-02,   3.89804309e-17,\
        -5.84680802e-02,  -8.90384387e-02,  -8.40918587e-02,\
        -4.92362781e-02,  -3.89804309e-17\])

Copy to clipboard

\>>> plt.plot(x, np.sinc(x))
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.title("Sinc Function")
Text(0.5, 1.0, 'Sinc Function')
\>>> plt.ylabel("Amplitude")
Text(0, 0.5, 'Amplitude')
\>>> plt.xlabel("X")
Text(0.5, 0, 'X')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-sinc-1.png](https://numpy.org/doc/stable/_images/numpy-sinc-1.png)

Go BackOpen In Tab

On this page