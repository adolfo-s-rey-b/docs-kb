[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.Hermite.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.Hermite.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.Hermite.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.Hermite[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy-polynomial-hermite-hermite "Link to this heading")

====================================================================================================================================================================================

_class_ numpy.polynomial.hermite.Hermite(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L1751-L1794)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "Link to this definition")

A Hermite series class.

The Hermite class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

Hermite coefficients in order of increasing degree, i.e, `(1, 2, 3)` gives `1*H_0(x) + 2*H_1(x) + 3*H_2(x)`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[-1., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.domain.html#numpy.polynomial.hermite.Hermite.domain "numpy.polynomial.hermite.Hermite.domain")
 for its use. The default value is \[-1., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.__call__.html#numpy.polynomial.hermite.Hermite.__call__ "numpy.polynomial.hermite.Hermite.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.basis.html#numpy.polynomial.hermite.Hermite.basis "numpy.polynomial.hermite.Hermite.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.cast.html#numpy.polynomial.hermite.Hermite.cast "numpy.polynomial.hermite.Hermite.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.convert.html#numpy.polynomial.hermite.Hermite.convert "numpy.polynomial.hermite.Hermite.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.copy.html#numpy.polynomial.hermite.Hermite.copy "numpy.polynomial.hermite.Hermite.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.cutdeg.html#numpy.polynomial.hermite.Hermite.cutdeg "numpy.polynomial.hermite.Hermite.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.degree.html#numpy.polynomial.hermite.Hermite.degree "numpy.polynomial.hermite.Hermite.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html#numpy.polynomial.hermite.Hermite.deriv "numpy.polynomial.hermite.Hermite.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.fit.html#numpy.polynomial.hermite.Hermite.fit "numpy.polynomial.hermite.Hermite.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.fromroots.html#numpy.polynomial.hermite.Hermite.fromroots "numpy.polynomial.hermite.Hermite.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.has_samecoef.html#numpy.polynomial.hermite.Hermite.has_samecoef "numpy.polynomial.hermite.Hermite.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.has_samedomain.html#numpy.polynomial.hermite.Hermite.has_samedomain "numpy.polynomial.hermite.Hermite.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.has_sametype.html#numpy.polynomial.hermite.Hermite.has_sametype "numpy.polynomial.hermite.Hermite.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.has_samewindow.html#numpy.polynomial.hermite.Hermite.has_samewindow "numpy.polynomial.hermite.Hermite.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.identity.html#numpy.polynomial.hermite.Hermite.identity "numpy.polynomial.hermite.Hermite.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.integ.html#numpy.polynomial.hermite.Hermite.integ "numpy.polynomial.hermite.Hermite.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.linspace.html#numpy.polynomial.hermite.Hermite.linspace "numpy.polynomial.hermite.Hermite.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.mapparms.html#numpy.polynomial.hermite.Hermite.mapparms "numpy.polynomial.hermite.Hermite.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.roots.html#numpy.polynomial.hermite.Hermite.roots "numpy.polynomial.hermite.Hermite.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.trim.html#numpy.polynomial.hermite.Hermite.trim "numpy.polynomial.hermite.Hermite.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.truncate.html#numpy.polynomial.hermite.Hermite.truncate "numpy.polynomial.hermite.Hermite.truncate")<br>(size) | Truncate series to length _size_. |

On this page