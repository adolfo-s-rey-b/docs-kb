[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.trimseq.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polyutils.trimseq[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.trimseq.html#numpy-polynomial-polyutils-trimseq "Link to this heading")

==========================================================================================================================================================================================

polynomial.polyutils.trimseq(_seq_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L34-L60)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.trimseq.html#numpy.polynomial.polyutils.trimseq "Link to this definition")

Remove small Poly series coefficients.

Parameters:

**seq**sequence

Sequence of Poly series coefficients.

Returns:

**series**sequence

Subsequence with trailing zeros removed. If the resulting sequence would be empty, return the first element. The returned sequence may or may not be a view.

Notes

Do not lose the type info if the sequence contains unknown objects.

On this page