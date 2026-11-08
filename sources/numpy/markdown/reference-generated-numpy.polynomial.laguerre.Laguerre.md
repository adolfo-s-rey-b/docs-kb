[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.Laguerre.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.Laguerre.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.Laguerre[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy-polynomial-laguerre-laguerre "Link to this heading")

==========================================================================================================================================================================================

_class_ numpy.polynomial.laguerre.Laguerre(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/laguerre.py#L1686-L1729)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "Link to this definition")

A Laguerre series class.

The Laguerre class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

Laguerre coefficients in order of increasing degree, i.e, `(1, 2, 3)` gives `1*L_0(x) + 2*L_1(X) + 3*L_2(x)`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[0., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.domain.html#numpy.polynomial.laguerre.Laguerre.domain "numpy.polynomial.laguerre.Laguerre.domain")
 for its use. The default value is \[0., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.__call__.html#numpy.polynomial.laguerre.Laguerre.__call__ "numpy.polynomial.laguerre.Laguerre.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.basis.html#numpy.polynomial.laguerre.Laguerre.basis "numpy.polynomial.laguerre.Laguerre.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cast.html#numpy.polynomial.laguerre.Laguerre.cast "numpy.polynomial.laguerre.Laguerre.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.convert.html#numpy.polynomial.laguerre.Laguerre.convert "numpy.polynomial.laguerre.Laguerre.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.copy.html#numpy.polynomial.laguerre.Laguerre.copy "numpy.polynomial.laguerre.Laguerre.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html#numpy.polynomial.laguerre.Laguerre.cutdeg "numpy.polynomial.laguerre.Laguerre.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.degree.html#numpy.polynomial.laguerre.Laguerre.degree "numpy.polynomial.laguerre.Laguerre.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.deriv.html#numpy.polynomial.laguerre.Laguerre.deriv "numpy.polynomial.laguerre.Laguerre.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.fit.html#numpy.polynomial.laguerre.Laguerre.fit "numpy.polynomial.laguerre.Laguerre.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.fromroots.html#numpy.polynomial.laguerre.Laguerre.fromroots "numpy.polynomial.laguerre.Laguerre.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.has_samecoef.html#numpy.polynomial.laguerre.Laguerre.has_samecoef "numpy.polynomial.laguerre.Laguerre.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.has_samedomain.html#numpy.polynomial.laguerre.Laguerre.has_samedomain "numpy.polynomial.laguerre.Laguerre.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.has_sametype.html#numpy.polynomial.laguerre.Laguerre.has_sametype "numpy.polynomial.laguerre.Laguerre.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.has_samewindow.html#numpy.polynomial.laguerre.Laguerre.has_samewindow "numpy.polynomial.laguerre.Laguerre.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.identity.html#numpy.polynomial.laguerre.Laguerre.identity "numpy.polynomial.laguerre.Laguerre.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.integ.html#numpy.polynomial.laguerre.Laguerre.integ "numpy.polynomial.laguerre.Laguerre.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.linspace.html#numpy.polynomial.laguerre.Laguerre.linspace "numpy.polynomial.laguerre.Laguerre.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.mapparms.html#numpy.polynomial.laguerre.Laguerre.mapparms "numpy.polynomial.laguerre.Laguerre.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.roots.html#numpy.polynomial.laguerre.Laguerre.roots "numpy.polynomial.laguerre.Laguerre.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.trim.html#numpy.polynomial.laguerre.Laguerre.trim "numpy.polynomial.laguerre.Laguerre.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.truncate.html#numpy.polynomial.laguerre.Laguerre.truncate "numpy.polynomial.laguerre.Laguerre.truncate")<br>(size) | Truncate series to length _size_. |

On this page