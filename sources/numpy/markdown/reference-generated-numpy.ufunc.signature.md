[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.signature.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.signature.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.signature.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.signature.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.signature.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.signature.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.signature.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.signature.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.signature.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.signature.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.signature.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.signature.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.signature.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.signature.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.signature.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.signature.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.signature.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.signature.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.signature.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.signature.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.signature[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html#numpy-ufunc-signature "Link to this heading")

===================================================================================================================================================

attribute

ufunc.signature[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html#numpy.ufunc.signature "Link to this definition")

Definition of the core elements a generalized ufunc operates on.

The signature determines how the dimensions of each input/output array are split into core and loop dimensions:

1.  Each dimension in the signature is matched to a dimension of the corresponding passed-in array, starting from the end of the shape tuple.
    
2.  Core dimensions assigned to the same label in the signature must have exactly matching sizes, no broadcasting is performed.
    
3.  The core dimensions are removed from all inputs and the remaining dimensions are broadcast together, defining the loop dimensions.
    

Notes

Generalized ufuncs are used internally in many linalg functions, and in the testing suite; the examples below are taken from these. For ufuncs that operate on scalars, the signature is None, which is equivalent to ‘()’ for every argument.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.linalg.\_umath\_linalg.det.signature
'(m,m)->()'
\>>> np.matmul.signature
'(n?,k),(k,m?)->(n?,m?)'
\>>> np.add.signature is None
True  # equivalent to '(),()->()'

Copy to clipboard

Go BackOpen In Tab

On this page