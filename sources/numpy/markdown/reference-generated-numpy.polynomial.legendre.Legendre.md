[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.Legendre.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.Legendre.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.Legendre.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.Legendre[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy-polynomial-legendre-legendre "Link to this heading")

==========================================================================================================================================================================================

_class_ numpy.polynomial.legendre.Legendre(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L1612-L1655)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "Link to this definition")

A Legendre series class.

The Legendre class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

Legendre coefficients in order of increasing degree, i.e., `(1, 2, 3)` gives `1*P_0(x) + 2*P_1(x) + 3*P_2(x)`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[-1., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.domain.html#numpy.polynomial.legendre.Legendre.domain "numpy.polynomial.legendre.Legendre.domain")
 for its use. The default value is \[-1., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.__call__.html#numpy.polynomial.legendre.Legendre.__call__ "numpy.polynomial.legendre.Legendre.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.basis.html#numpy.polynomial.legendre.Legendre.basis "numpy.polynomial.legendre.Legendre.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.cast.html#numpy.polynomial.legendre.Legendre.cast "numpy.polynomial.legendre.Legendre.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.convert.html#numpy.polynomial.legendre.Legendre.convert "numpy.polynomial.legendre.Legendre.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.copy.html#numpy.polynomial.legendre.Legendre.copy "numpy.polynomial.legendre.Legendre.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.cutdeg.html#numpy.polynomial.legendre.Legendre.cutdeg "numpy.polynomial.legendre.Legendre.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.degree.html#numpy.polynomial.legendre.Legendre.degree "numpy.polynomial.legendre.Legendre.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.deriv.html#numpy.polynomial.legendre.Legendre.deriv "numpy.polynomial.legendre.Legendre.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.fit.html#numpy.polynomial.legendre.Legendre.fit "numpy.polynomial.legendre.Legendre.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.fromroots.html#numpy.polynomial.legendre.Legendre.fromroots "numpy.polynomial.legendre.Legendre.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.has_samecoef.html#numpy.polynomial.legendre.Legendre.has_samecoef "numpy.polynomial.legendre.Legendre.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.has_samedomain.html#numpy.polynomial.legendre.Legendre.has_samedomain "numpy.polynomial.legendre.Legendre.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.has_sametype.html#numpy.polynomial.legendre.Legendre.has_sametype "numpy.polynomial.legendre.Legendre.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.has_samewindow.html#numpy.polynomial.legendre.Legendre.has_samewindow "numpy.polynomial.legendre.Legendre.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.identity.html#numpy.polynomial.legendre.Legendre.identity "numpy.polynomial.legendre.Legendre.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.integ.html#numpy.polynomial.legendre.Legendre.integ "numpy.polynomial.legendre.Legendre.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html#numpy.polynomial.legendre.Legendre.linspace "numpy.polynomial.legendre.Legendre.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html#numpy.polynomial.legendre.Legendre.mapparms "numpy.polynomial.legendre.Legendre.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.roots.html#numpy.polynomial.legendre.Legendre.roots "numpy.polynomial.legendre.Legendre.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.trim.html#numpy.polynomial.legendre.Legendre.trim "numpy.polynomial.legendre.Legendre.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.truncate.html#numpy.polynomial.legendre.Legendre.truncate "numpy.polynomial.legendre.Legendre.truncate")<br>(size) | Truncate series to length _size_. |

On this page