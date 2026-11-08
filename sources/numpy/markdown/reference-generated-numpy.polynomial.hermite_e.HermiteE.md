[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.HermiteE.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.HermiteE[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy-polynomial-hermite-e-hermitee "Link to this heading")

==============================================================================================================================================================================================

_class_ numpy.polynomial.hermite\_e.HermiteE(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L1649-L1692)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "Link to this definition")

A HermiteE series class.

The HermiteE class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

HermiteE coefficients in order of increasing degree, i.e, `(1, 2, 3)` gives `1*He_0(x) + 2*He_1(X) + 3*He_2(x)`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[-1., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.domain.html#numpy.polynomial.hermite_e.HermiteE.domain "numpy.polynomial.hermite_e.HermiteE.domain")
 for its use. The default value is \[-1., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.__call__.html#numpy.polynomial.hermite_e.HermiteE.__call__ "numpy.polynomial.hermite_e.HermiteE.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.basis.html#numpy.polynomial.hermite_e.HermiteE.basis "numpy.polynomial.hermite_e.HermiteE.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.cast.html#numpy.polynomial.hermite_e.HermiteE.cast "numpy.polynomial.hermite_e.HermiteE.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html#numpy.polynomial.hermite_e.HermiteE.convert "numpy.polynomial.hermite_e.HermiteE.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.copy.html#numpy.polynomial.hermite_e.HermiteE.copy "numpy.polynomial.hermite_e.HermiteE.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.cutdeg.html#numpy.polynomial.hermite_e.HermiteE.cutdeg "numpy.polynomial.hermite_e.HermiteE.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.degree.html#numpy.polynomial.hermite_e.HermiteE.degree "numpy.polynomial.hermite_e.HermiteE.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.deriv.html#numpy.polynomial.hermite_e.HermiteE.deriv "numpy.polynomial.hermite_e.HermiteE.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.fit.html#numpy.polynomial.hermite_e.HermiteE.fit "numpy.polynomial.hermite_e.HermiteE.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.fromroots.html#numpy.polynomial.hermite_e.HermiteE.fromroots "numpy.polynomial.hermite_e.HermiteE.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.has_samecoef.html#numpy.polynomial.hermite_e.HermiteE.has_samecoef "numpy.polynomial.hermite_e.HermiteE.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.has_samedomain.html#numpy.polynomial.hermite_e.HermiteE.has_samedomain "numpy.polynomial.hermite_e.HermiteE.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.has_sametype.html#numpy.polynomial.hermite_e.HermiteE.has_sametype "numpy.polynomial.hermite_e.HermiteE.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.has_samewindow.html#numpy.polynomial.hermite_e.HermiteE.has_samewindow "numpy.polynomial.hermite_e.HermiteE.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.identity.html#numpy.polynomial.hermite_e.HermiteE.identity "numpy.polynomial.hermite_e.HermiteE.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.integ.html#numpy.polynomial.hermite_e.HermiteE.integ "numpy.polynomial.hermite_e.HermiteE.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.linspace.html#numpy.polynomial.hermite_e.HermiteE.linspace "numpy.polynomial.hermite_e.HermiteE.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.mapparms.html#numpy.polynomial.hermite_e.HermiteE.mapparms "numpy.polynomial.hermite_e.HermiteE.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.roots.html#numpy.polynomial.hermite_e.HermiteE.roots "numpy.polynomial.hermite_e.HermiteE.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.trim.html#numpy.polynomial.hermite_e.HermiteE.trim "numpy.polynomial.hermite_e.HermiteE.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.truncate.html#numpy.polynomial.hermite_e.HermiteE.truncate "numpy.polynomial.hermite_e.HermiteE.truncate")<br>(size) | Truncate series to length _size_. |

On this page