[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.Polynomial.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.Polynomial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.Polynomial[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy-polynomial-polynomial-polynomial "Link to this heading")

======================================================================================================================================================================================================

_class_ numpy.polynomial.polynomial.Polynomial(_coef_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1615-L1683)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "Link to this definition")

A power series class.

The Polynomial class provides the standard Python numerical methods ‘+’, ‘-’, ‘\*’, ‘//’, ‘%’, ‘divmod’, ‘\*\*’, and ‘()’ as well as the attributes and methods listed below.

Parameters:

**coef**array\_like

Polynomial coefficients in order of increasing degree, i.e., `(1, 2, 3)` give `1 + 2*x + 3*x**2`.

**domain**(2,) array\_like, optional

Domain to use. The interval `[domain[0], domain[1]]` is mapped to the interval `[window[0], window[1]]` by shifting and scaling. The default value is \[-1., 1.\].

**window**(2,) array\_like, optional

Window, see [`domain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.domain.html#numpy.polynomial.polynomial.Polynomial.domain "numpy.polynomial.polynomial.Polynomial.domain")
 for its use. The default value is \[-1., 1.\].

**symbol**str, optional

Symbol used to represent the independent variable in string representations of the polynomial expression, e.g. for printing. The symbol must be a valid Python identifier. Default value is ‘x’.

New in version 1.24.

Attributes:

**basis\_name**

**symbol**

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.__call__.html#numpy.polynomial.polynomial.Polynomial.__call__ "numpy.polynomial.polynomial.Polynomial.__call__")<br>(arg) | Call self as a function. |
| [`basis`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.basis.html#numpy.polynomial.polynomial.Polynomial.basis "numpy.polynomial.polynomial.Polynomial.basis")<br>(deg\[, domain, window, symbol\]) | Series basis polynomial of degree _deg_. |
| [`cast`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.cast.html#numpy.polynomial.polynomial.Polynomial.cast "numpy.polynomial.polynomial.Polynomial.cast")<br>(series\[, domain, window\]) | Convert series to series of this class. |
| [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.convert.html#numpy.polynomial.polynomial.Polynomial.convert "numpy.polynomial.polynomial.Polynomial.convert")<br>(\[domain, kind, window\]) | Convert series to a different kind and/or domain and/or window. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.copy.html#numpy.polynomial.polynomial.Polynomial.copy "numpy.polynomial.polynomial.Polynomial.copy")<br>() | Return a copy. |
| [`cutdeg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.cutdeg.html#numpy.polynomial.polynomial.Polynomial.cutdeg "numpy.polynomial.polynomial.Polynomial.cutdeg")<br>(deg) | Truncate series to the given degree. |
| [`degree`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.degree.html#numpy.polynomial.polynomial.Polynomial.degree "numpy.polynomial.polynomial.Polynomial.degree")<br>() | The degree of the series. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.deriv.html#numpy.polynomial.polynomial.Polynomial.deriv "numpy.polynomial.polynomial.Polynomial.deriv")<br>(\[m\]) | Differentiate. |
| [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit "numpy.polynomial.polynomial.Polynomial.fit")<br>(x, y, deg\[, domain, rcond, full, w, ...\]) | Least squares fit to data. |
| [`fromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fromroots.html#numpy.polynomial.polynomial.Polynomial.fromroots "numpy.polynomial.polynomial.Polynomial.fromroots")<br>(roots\[, domain, window, symbol\]) | Return series instance that has the specified roots. |
| [`has_samecoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.has_samecoef.html#numpy.polynomial.polynomial.Polynomial.has_samecoef "numpy.polynomial.polynomial.Polynomial.has_samecoef")<br>(other) | Check if coefficients match. |
| [`has_samedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.has_samedomain.html#numpy.polynomial.polynomial.Polynomial.has_samedomain "numpy.polynomial.polynomial.Polynomial.has_samedomain")<br>(other) | Check if domains match. |
| [`has_sametype`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.has_sametype.html#numpy.polynomial.polynomial.Polynomial.has_sametype "numpy.polynomial.polynomial.Polynomial.has_sametype")<br>(other) | Check if types match. |
| [`has_samewindow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.has_samewindow.html#numpy.polynomial.polynomial.Polynomial.has_samewindow "numpy.polynomial.polynomial.Polynomial.has_samewindow")<br>(other) | Check if windows match. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.identity.html#numpy.polynomial.polynomial.Polynomial.identity "numpy.polynomial.polynomial.Polynomial.identity")<br>(\[domain, window, symbol\]) | Identity function. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.integ.html#numpy.polynomial.polynomial.Polynomial.integ "numpy.polynomial.polynomial.Polynomial.integ")<br>(\[m, k, lbnd\]) | Integrate. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.linspace.html#numpy.polynomial.polynomial.Polynomial.linspace "numpy.polynomial.polynomial.Polynomial.linspace")<br>(\[n, domain\]) | Return x, y values at equally spaced points in domain. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.mapparms.html#numpy.polynomial.polynomial.Polynomial.mapparms "numpy.polynomial.polynomial.Polynomial.mapparms")<br>() | Return the mapping parameters. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.roots.html#numpy.polynomial.polynomial.Polynomial.roots "numpy.polynomial.polynomial.Polynomial.roots")<br>() | Return the roots of the series polynomial. |
| [`trim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.trim.html#numpy.polynomial.polynomial.Polynomial.trim "numpy.polynomial.polynomial.Polynomial.trim")<br>(\[tol\]) | Remove trailing coefficients |
| [`truncate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.truncate.html#numpy.polynomial.polynomial.Polynomial.truncate "numpy.polynomial.polynomial.Polynomial.truncate")<br>(size) | Truncate series to length _size_. |

On this page