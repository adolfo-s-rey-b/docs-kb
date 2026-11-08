[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.anomalies.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.anomalies.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.anomalies.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.anomalies.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.anomalies.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.anomalies.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.anomalies.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.anomalies.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.anomalies.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.anomalies.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.anomalies.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.anomalies.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.anomalies.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.anomalies.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.anomalies.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.anomalies.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.anomalies.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.anomalies.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.anomalies.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.anomalies.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.anomalies.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.anomalies.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.anomalies[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.anomalies.html#numpy-ma-anomalies "Link to this heading")

==========================================================================================================================================

ma.anomalies(_self_, _axis\=None_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.anomalies.html#numpy.ma.anomalies "Link to this definition")

Compute the anomalies (deviations from the arithmetic mean) along the given axis.

Returns an array of anomalies, with the same shape as the input and where the arithmetic mean is computed along the given axis.

Parameters:

**axis**int, optional

Axis over which the anomalies are taken. The default is to use the mean of the flattened array as reference.

**dtype**dtype, optional

Type to use in computing the variance. For arrays of integer type the default is float32; for arrays of float types it is the same as the array type.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

Compute the mean of the array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1,2,3\])
\>>> a.anom()
masked\_array(data=\[-1.,  0.,  1.\],
             mask=False,
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page