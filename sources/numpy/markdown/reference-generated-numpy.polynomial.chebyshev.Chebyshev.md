[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.Chebyshev[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy-polynomial-chebyshev-chebyshev "Link to this heading")

================================================================================================================================================================================================

_class_ numpy.polynomial.chebyshev.Chebyshev(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1970-L2053)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "Link to this definition")

A Chebyshev series class.

The Chebyshev class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

Chebyshev coefficients in order of increasing degree, i.e., `(1, 2, 3)` gives `1*T_0(x) + 2*T_1(x) + 3*T_2(x)`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[-1., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.domain.html#numpy.polynomial.chebyshev.Chebyshev.domain "numpy.polynomial.chebyshev.Chebyshev.domain")
 for its use. The default value is \[-1., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.__call__.html#numpy.polynomial.chebyshev.Chebyshev.__call__ "numpy.polynomial.chebyshev.Chebyshev.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.basis.html#numpy.polynomial.chebyshev.Chebyshev.basis "numpy.polynomial.chebyshev.Chebyshev.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html#numpy.polynomial.chebyshev.Chebyshev.cast "numpy.polynomial.chebyshev.Chebyshev.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.convert.html#numpy.polynomial.chebyshev.Chebyshev.convert "numpy.polynomial.chebyshev.Chebyshev.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.copy.html#numpy.polynomial.chebyshev.Chebyshev.copy "numpy.polynomial.chebyshev.Chebyshev.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cutdeg.html#numpy.polynomial.chebyshev.Chebyshev.cutdeg "numpy.polynomial.chebyshev.Chebyshev.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.degree.html#numpy.polynomial.chebyshev.Chebyshev.degree "numpy.polynomial.chebyshev.Chebyshev.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.deriv.html#numpy.polynomial.chebyshev.Chebyshev.deriv "numpy.polynomial.chebyshev.Chebyshev.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fit.html#numpy.polynomial.chebyshev.Chebyshev.fit "numpy.polynomial.chebyshev.Chebyshev.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html#numpy.polynomial.chebyshev.Chebyshev.fromroots "numpy.polynomial.chebyshev.Chebyshev.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.has_samecoef.html#numpy.polynomial.chebyshev.Chebyshev.has_samecoef "numpy.polynomial.chebyshev.Chebyshev.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.has_samedomain.html#numpy.polynomial.chebyshev.Chebyshev.has_samedomain "numpy.polynomial.chebyshev.Chebyshev.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.has_sametype.html#numpy.polynomial.chebyshev.Chebyshev.has_sametype "numpy.polynomial.chebyshev.Chebyshev.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.has_samewindow.html#numpy.polynomial.chebyshev.Chebyshev.has_samewindow "numpy.polynomial.chebyshev.Chebyshev.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.identity.html#numpy.polynomial.chebyshev.Chebyshev.identity "numpy.polynomial.chebyshev.Chebyshev.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.integ.html#numpy.polynomial.chebyshev.Chebyshev.integ "numpy.polynomial.chebyshev.Chebyshev.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`interpolate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.interpolate.html#numpy.polynomial.chebyshev.Chebyshev.interpolate "numpy.polynomial.chebyshev.Chebyshev.interpolate")<br>(func, deg\[, domain, args\]) | Interpolate a function at the Chebyshev points of the first kind. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.linspace.html#numpy.polynomial.chebyshev.Chebyshev.linspace "numpy.polynomial.chebyshev.Chebyshev.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.mapparms.html#numpy.polynomial.chebyshev.Chebyshev.mapparms "numpy.polynomial.chebyshev.Chebyshev.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.roots.html#numpy.polynomial.chebyshev.Chebyshev.roots "numpy.polynomial.chebyshev.Chebyshev.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.trim.html#numpy.polynomial.chebyshev.Chebyshev.trim "numpy.polynomial.chebyshev.Chebyshev.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.truncate.html#numpy.polynomial.chebyshev.Chebyshev.truncate "numpy.polynomial.chebyshev.Chebyshev.truncate")<br>(size) | Truncate series to length _size_. |

On this page