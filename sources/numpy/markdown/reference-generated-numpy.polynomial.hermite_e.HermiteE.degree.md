[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.degree.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.HermiteE.degree[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.degree.html#numpy-polynomial-hermite-e-hermitee-degree "Link to this heading")

===================================================================================================================================================================================================================

method

polynomial.hermite\_e.HermiteE.degree()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L670-L702)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.degree.html#numpy.polynomial.hermite_e.HermiteE.degree "Link to this definition")

The degree of the series.

Returns:

**degree**int

Degree of the series, one less than the number of coefficients.

Examples

Try it in your browser!

Create a polynomial object for `1 + 7*x + 4*x**2`:

\>>> np.polynomial.set\_default\_printstyle("unicode")
\>>> poly \= np.polynomial.Polynomial(\[1, 7, 4\])
\>>> print(poly)
1.0 + 7.0·x + 4.0·x²
\>>> poly.degree()
2

Copy to clipboard

Note that this method does not check for non-zero coefficients. You must trim the polynomial to remove any trailing zeroes:

\>>> poly \= np.polynomial.Polynomial(\[1, 7, 0\])
\>>> print(poly)
1.0 + 7.0·x + 0.0·x²
\>>> poly.degree()
2
\>>> poly.trim().degree()
1

Copy to clipboard

Go BackOpen In Tab

On this page