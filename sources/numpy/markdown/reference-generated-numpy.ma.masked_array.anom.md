[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.anom.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.anom[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.anom.html#numpy-ma-masked-array-anom "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.anom(_axis\=None_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5432-L5468)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.anom.html#numpy.ma.masked_array.anom "Link to this definition")

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