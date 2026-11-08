[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.degree.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.Hermite.degree.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.Hermite.degree[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.degree.html#numpy-polynomial-hermite-hermite-degree "Link to this heading")

=========================================================================================================================================================================================================

method

polynomial.hermite.Hermite.degree()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L670-L702)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.degree.html#numpy.polynomial.hermite.Hermite.degree "Link to this definition")

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