[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.classes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.classes.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.classes.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.classes.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.classes.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.classes.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.classes.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.classes.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.classes.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.classes.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.classes.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.classes.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.classes.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.classes.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.classes.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.classes.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.classes.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.classes.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.classes.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.classes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using the convenience classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#using-the-convenience-classes "Link to this heading")

================================================================================================================================================================

The convenience classes provided by the polynomial package are:

| Name | Provides |
| --- | --- |
| [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial") | Power series |
| [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev") | Chebyshev series |
| [`Legendre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "numpy.polynomial.legendre.Legendre") | Legendre series |
| [`Laguerre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "numpy.polynomial.laguerre.Laguerre") | Laguerre series |
| [`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite") | Hermite series |
| [`HermiteE`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "numpy.polynomial.hermite_e.HermiteE") | HermiteE series |

The series in this context are finite sums of the corresponding polynomial basis functions multiplied by coefficients. For instance, a power series looks like

\\\[p(x) = 1 + 2x + 3x^2\\\]

and has coefficients \\(\[1, 2, 3\]\\). The Chebyshev series with the same coefficients looks like

\\\[p(x) = 1 T\_0(x) + 2 T\_1(x) + 3 T\_2(x)\\\]

and more generally

\\\[p(x) = \\sum\_{i=0}^n c\_i T\_i(x)\\\]

where in this case the \\(T\_n\\) are the Chebyshev functions of degree \\(n\\), but could just as easily be the basis functions of any of the other classes. The convention for all the classes is that the coefficient \\(c\[i\]\\) goes with the basis function of degree i.

All of the classes are immutable and have the same methods, and especially they implement the Python numeric operators +, -, \*, //, %, divmod, \*\*, ==, and !=. The last two can be a bit problematic due to floating point roundoff errors. We now give a quick demonstration of the various operations using NumPy version 1.7.0.

Basics[#](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#basics "Link to this heading")

------------------------------------------------------------------------------------------------------------------

First we need a polynomial class and a polynomial instance to play with. The classes can be imported directly from the polynomial package or from the module of the relevant type. Here we import from the package and use the conventional Polynomial class because of its familiarity:

\>>> from numpy.polynomial import Polynomial as P
\>>> p \= P(\[1,2,3\])
\>>> p
Polynomial(\[1., 2., 3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Note that there are three parts to the long version of the printout. The first is the coefficients, the second is the domain, and the third is the window:

\>>> p.coef
array(\[1., 2., 3.\])
\>>> p.domain
array(\[-1.,  1.\])
\>>> p.window
array(\[-1.,  1.\])

Copy to clipboard

Printing a polynomial yields the polynomial expression in a more familiar format:

\>>> print(p)
1.0 + 2.0·x + 3.0·x²

Copy to clipboard

Note that the string representation of polynomials uses Unicode characters by default (except on Windows) to express powers and subscripts. An ASCII-based representation is also available (default on Windows). The polynomial string format can be toggled at the package-level with the [`set_default_printstyle`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html#numpy.polynomial.set_default_printstyle "numpy.polynomial.set_default_printstyle")
 function:

\>>> np.polynomial.set\_default\_printstyle('ascii')
\>>> print(p)
1.0 + 2.0 x + 3.0 x\*\*2

Copy to clipboard

or controlled for individual polynomial instances with string formatting:

\>>> print(f"{p:unicode}")
1.0 + 2.0·x + 3.0·x²

Copy to clipboard

We will deal with the domain and window when we get to fitting, for the moment we ignore them and run through the basic algebraic and arithmetic operations.

Addition and Subtraction:

\>>> p + p
Polynomial(\[2., 4., 6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p \- p
Polynomial(\[0.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Multiplication:

\>>> p \* p
Polynomial(\[ 1.,   4.,  10.,  12.,   9.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Powers:

\>>> p\*\*2
Polynomial(\[ 1.,   4., 10., 12.,  9.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Division:

Floor division, ‘//’, is the division operator for the polynomial classes, polynomials are treated like integers in this regard. For Python versions < 3.x the ‘/’ operator maps to ‘//’, as it does for Python, for later versions the ‘/’ will only work for division by scalars. At some point it will be deprecated:

\>>> p // P(\[\-1, 1\])
Polynomial(\[5.,  3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Remainder:

\>>> p % P(\[\-1, 1\])
Polynomial(\[6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Divmod:

\>>> quo, rem \= divmod(p, P(\[\-1, 1\]))
\>>> quo
Polynomial(\[5.,  3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> rem
Polynomial(\[6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Evaluation:

\>>> x \= np.arange(5)
\>>> p(x)
array(\[  1.,   6.,  17.,  34.,  57.\])
\>>> x \= np.arange(6).reshape(3,2)
\>>> p(x)
array(\[\[ 1.,   6.\],\
       \[17.,  34.\],\
       \[57.,  86.\]\])

Copy to clipboard

Substitution:

Substitute a polynomial for x and expand the result. Here we substitute p in itself leading to a new polynomial of degree 4 after expansion. If the polynomials are regarded as functions this is composition of functions:

\>>> p(p)
Polynomial(\[ 6., 16., 36., 36., 27.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Roots:

\>>> p.roots()
array(\[-0.33333333-0.47140452j, -0.33333333+0.47140452j\])

Copy to clipboard

It isn’t always convenient to explicitly use Polynomial instances, so tuples, lists, arrays, and scalars are automatically cast in the arithmetic operations:

\>>> p + \[1, 2, 3\]
Polynomial(\[2., 4., 6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> \[1, 2, 3\] \* p
Polynomial(\[ 1.,  4., 10., 12.,  9.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p / 2
Polynomial(\[0.5, 1. , 1.5\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Polynomials that differ in domain, window, or class can’t be mixed in arithmetic:

\>>> from numpy.polynomial import Chebyshev as T
\>>> p + P(\[1\], domain\=\[0,1\])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 213, in \_\_add\_\_
TypeError: Domains differ
\>>> p + P(\[1\], window\=\[0,1\])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 215, in \_\_add\_\_
TypeError: Windows differ
\>>> p + T(\[1\])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 211, in \_\_add\_\_
TypeError: Polynomial types differ

Copy to clipboard

But different types can be used for substitution. In fact, this is how conversion of Polynomial classes among themselves is done for type, domain, and window casting:

\>>> p(T(\[0, 1\]))
Chebyshev(\[2.5, 2. , 1.5\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Which gives the polynomial _p_ in Chebyshev form. This works because \\(T\_1(x) = x\\) and substituting \\(x\\) for \\(x\\) doesn’t change the original polynomial. However, all the multiplications and divisions will be done using Chebyshev series, hence the type of the result.

It is intended that all polynomial instances are immutable, therefore augmented operations (`+=`, `-=`, etc.) and any other functionality that would violate the immutablity of a polynomial instance are intentionally unimplemented.

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#calculus "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Polynomial instances can be integrated and differentiated.:

\>>> from numpy.polynomial import Polynomial as P
\>>> p \= P(\[2, 6\])
\>>> p.integ()
Polynomial(\[0., 2., 3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p.integ(2)
Polynomial(\[0., 0., 1., 1.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

The first example integrates _p_ once, the second example integrates it twice. By default, the lower bound of the integration and the integration constant are 0, but both can be specified.:

\>>> p.integ(lbnd\=-1)
Polynomial(\[-1.,  2.,  3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p.integ(lbnd\=-1, k\=1)
Polynomial(\[0., 2., 3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

In the first case the lower bound of the integration is set to -1 and the integration constant is 0. In the second the constant of integration is set to 1 as well. Differentiation is simpler since the only option is the number of times the polynomial is differentiated:

\>>> p \= P(\[1, 2, 3\])
\>>> p.deriv(1)
Polynomial(\[2., 6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p.deriv(2)
Polynomial(\[6.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Other polynomial constructors[#](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#other-polynomial-constructors "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Constructing polynomials by specifying coefficients is just one way of obtaining a polynomial instance, they may also be created by specifying their roots, by conversion from other polynomial types, and by least squares fits. Fitting is discussed in its own section, the other methods are demonstrated below:

\>>> from numpy.polynomial import Polynomial as P
\>>> from numpy.polynomial import Chebyshev as T
\>>> p \= P.fromroots(\[1, 2, 3\])
\>>> p
Polynomial(\[-6., 11., -6.,  1.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p.convert(kind\=T)
Chebyshev(\[-9.  , 11.75, -3.  ,  0.25\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

The convert method can also convert domain and window:

\>>> p.convert(kind\=T, domain\=\[0, 1\])
Chebyshev(\[-2.4375 ,  2.96875, -0.5625 ,  0.03125\], domain=\[0.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p.convert(kind\=P, domain\=\[0, 1\])
Polynomial(\[-1.875,  2.875, -1.125,  0.125\], domain=\[0.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

In numpy versions >= 1.7.0 the _basis_ and _cast_ class methods are also available. The cast method works like the convert method while the basis method returns the basis polynomial of given degree:

\>>> P.basis(3)
Polynomial(\[0., 0., 0., 1.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> T.cast(p)
Chebyshev(\[-9.  , 11.75, -3. ,  0.25\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Conversions between types can be useful, but it is _not_ recommended for routine use. The loss of numerical precision in passing from a Chebyshev series of degree 50 to a Polynomial series of the same degree can make the results of numerical evaluation essentially random.

Fitting[#](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html#fitting "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Fitting is the reason that the _domain_ and _window_ attributes are part of the convenience classes. To illustrate the problem, the values of the Chebyshev polynomials up to degree 5 are plotted below.

\>>> import matplotlib.pyplot as plt
\>>> from numpy.polynomial import Chebyshev as T
\>>> x \= np.linspace(\-1, 1, 100)
\>>> for i in range(6):
...     ax \= plt.plot(x, T.basis(i)(x), lw\=2, label\=f"$T\_{i}$")
...
\>>> plt.legend(loc\="upper left")
\>>> plt.show()

Copy to clipboard

![../_images/routines-polynomials-classes-1.png](https://numpy.org/doc/stable/_images/routines-polynomials-classes-1.png)

In the range -1 <= _x_ <= 1 they are nice, equiripple functions lying between +/- 1. The same plots over the range -2 <= _x_ <= 2 look very different:

\>>> import matplotlib.pyplot as plt
\>>> from numpy.polynomial import Chebyshev as T
\>>> x \= np.linspace(\-2, 2, 100)
\>>> for i in range(6):
...     ax \= plt.plot(x, T.basis(i)(x), lw\=2, label\=f"$T\_{i}$")
...
\>>> plt.legend(loc\="lower right")
\>>> plt.show()

Copy to clipboard

![../_images/routines-polynomials-classes-2.png](https://numpy.org/doc/stable/_images/routines-polynomials-classes-2.png)

As can be seen, the “good” parts have shrunk to insignificance. In using Chebyshev polynomials for fitting we want to use the region where _x_ is between -1 and 1 and that is what the _window_ specifies. However, it is unlikely that the data to be fit has all its data points in that interval, so we use _domain_ to specify the interval where the data points lie. When the fit is done, the domain is first mapped to the window by a linear transformation and the usual least squares fit is done using the mapped data points. The window and domain of the fit are part of the returned series and are automatically used when computing values, derivatives, and such. If they aren’t specified in the call the fitting routine will use the default window and the smallest domain that holds all the data points. This is illustrated below for a fit to a noisy sine curve.

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> from numpy.polynomial import Chebyshev as T
\>>> np.random.seed(11)
\>>> x \= np.linspace(0, 2\*np.pi, 20)
\>>> y \= np.sin(x) + np.random.normal(scale\=.1, size\=x.shape)
\>>> p \= T.fit(x, y, 5)
\>>> plt.plot(x, y, 'o')
\>>> xx, yy \= p.linspace()
\>>> plt.plot(xx, yy, lw\=2)
\>>> p.domain
array(\[0.        ,  6.28318531\])
\>>> p.window
array(\[-1.,  1.\])
\>>> plt.show()

Copy to clipboard

![../_images/routines-polynomials-classes-3.png](https://numpy.org/doc/stable/_images/routines-polynomials-classes-3.png)

On this page