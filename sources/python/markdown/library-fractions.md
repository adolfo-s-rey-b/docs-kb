### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/random.html "random — Generate pseudo-random numbers")
     |
*   [previous](https://docs.python.org/3/library/decimal.html "decimal — Decimal fixed-point and floating-point arithmetic")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)
     »
*   [`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`fractions` — Rational numbers[¶](https://docs.python.org/3/library/fractions.html#module-fractions "Link to this heading")

============================================================================================================================

**Source code:** [Lib/fractions.py](https://github.com/python/cpython/tree/3.15/Lib/fractions.py)

* * *

The `fractions` module provides support for rational number arithmetic.

A Fraction instance can be constructed from a pair of rational numbers, from a single number, or from a string.

class fractions.Fraction(_numerator\=0_, _denominator\=1_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction "Link to this definition")

class fractions.Fraction(_number_)

class fractions.Fraction(_string_)

The first version requires that _numerator_ and _denominator_ are instances of [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
 and returns a new `Fraction` instance with a value equal to `numerator/denominator`. If _denominator_ is zero, it raises a [`ZeroDivisionError`](https://docs.python.org/3/builtins/exceptions.html#ZeroDivisionError "ZeroDivisionError")
.

The second version requires that _number_ is an instance of [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
 or has the `as_integer_ratio()` method (this includes [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 and [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
). It returns a `Fraction` instance with exactly the same value. Assumed, that the `as_integer_ratio()` method returns a pair of coprime integers and last one is positive. Note that due to the usual issues with binary point (see [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues)
), the argument to `Fraction(1.1)` is not exactly equal to 11/10, and so `Fraction(1.1)` does _not_ return `Fraction(11, 10)` as one might expect. (But see the documentation for the [`limit_denominator()`](https://docs.python.org/3/library/fractions.html#fractions.Fraction.limit_denominator "fractions.Fraction.limit_denominator")
 method below.)

The last version of the constructor expects a string. The usual form for this instance is:

Copy

\[sign\] numerator \['/' denominator\]

where the optional `sign` may be either ‘+’ or ‘-’ and `numerator` and `denominator` (if present) are strings of decimal digits (underscores may be used to delimit digits as with integral literals in code). In addition, any string that represents a finite value and is accepted by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 constructor is also accepted by the `Fraction` constructor. In either form the input string may also have leading and/or trailing whitespace. Here are some examples:

Copy

\>>> from fractions import Fraction
\>>> Fraction(16, \-10)
Fraction(-8, 5)
\>>> Fraction(123)
Fraction(123, 1)
\>>> Fraction()
Fraction(0, 1)
\>>> Fraction('3/7')
Fraction(3, 7)
\>>> Fraction(' -3/7 ')
Fraction(-3, 7)
\>>> Fraction('1.414213 \\t\\n')
Fraction(1414213, 1000000)
\>>> Fraction('-.125')
Fraction(-1, 8)
\>>> Fraction('7e-6')
Fraction(7, 1000000)
\>>> Fraction(2.25)
Fraction(9, 4)
\>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
\>>> from decimal import Decimal
\>>> Fraction(Decimal('1.1'))
Fraction(11, 10)

The `Fraction` class inherits from the abstract base class [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
, and implements all of the methods and operations from that class. `Fraction` instances are [hashable](https://docs.python.org/3/glossary.html#term-hashable)
, and should be treated as immutable. In addition, `Fraction` has the following properties and methods:

Changed in version 3.2: The `Fraction` constructor now accepts [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 and [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
 instances.

Changed in version 3.9: The [`math.gcd()`](https://docs.python.org/3/library/math.html#math.gcd "math.gcd")
 function is now used to normalize the _numerator_ and _denominator_. `math.gcd()` always returns an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 type. Previously, the GCD type depended on _numerator_ and _denominator_.

Changed in version 3.11: Underscores are now permitted when creating a `Fraction` instance from a string, following [**PEP 515**](https://peps.python.org/pep-0515/)
 rules.

Changed in version 3.11: `Fraction` implements `__int__` now to satisfy `typing.SupportsInt` instance checks.

Changed in version 3.12: Space is allowed around the slash for string inputs: `Fraction('2 / 3')`.

Changed in version 3.12: `Fraction` instances now support float-style formatting, with presentation types `"e"`, `"E"`, `"f"`, `"F"`, `"g"`, `"G"` and `"%"`.

Changed in version 3.13: Formatting of `Fraction` instances without a presentation type now supports fill, alignment, sign handling, minimum width and grouping.

Changed in version 3.14: The `Fraction` constructor now accepts any objects with the `as_integer_ratio()` method.

numerator[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.numerator "Link to this definition")

Numerator of the Fraction in lowest term.

denominator[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.denominator "Link to this definition")

Denominator of the Fraction in lowest terms. Guaranteed to be positive.

as\_integer\_ratio()[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.as_integer_ratio "Link to this definition")

Return a tuple of two integers, whose ratio is equal to the original Fraction. The ratio is in lowest terms and has a positive denominator.

Added in version 3.8.

is\_integer()[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.is_integer "Link to this definition")

Return `True` if the Fraction is an integer.

Added in version 3.12.

classmethod from\_float(_f_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.from_float "Link to this definition")

Alternative constructor which only accepts instances of [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 or [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
. Beware that `Fraction.from_float(0.3)` is not the same value as `Fraction(3, 10)`.

Note

From Python 3.2 onwards, you can also construct a `Fraction` instance directly from a [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
.

classmethod from\_decimal(_dec_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.from_decimal "Link to this definition")

Alternative constructor which only accepts instances of [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
 or [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
.

Note

From Python 3.2 onwards, you can also construct a `Fraction` instance directly from a [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
 instance.

classmethod from\_number(_number_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.from_number "Link to this definition")

Alternative constructor which only accepts instances of [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
, [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 or [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
, and objects with the `as_integer_ratio()` method, but not strings.

Added in version 3.14.

limit\_denominator(_max\_denominator\=1000000_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.limit_denominator "Link to this definition")

Finds and returns the closest `Fraction` to `self` that has denominator at most max\_denominator. This method is useful for finding rational approximations to a given floating-point number:

Copy

\>>> from fractions import Fraction
\>>> Fraction('3.1415926535897932').limit\_denominator(1000)
Fraction(355, 113)

or for recovering a rational number that’s represented as a float:

Copy

\>>> from math import pi, cos
\>>> Fraction(cos(pi/3))
Fraction(4503599627370497, 9007199254740992)
\>>> Fraction(cos(pi/3)).limit\_denominator()
Fraction(1, 2)
\>>> Fraction(1.1).limit\_denominator()
Fraction(11, 10)

\_\_floor\_\_()[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.__floor__ "Link to this definition")

Returns the greatest [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 `<= self`. This method can also be accessed through the [`math.floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor")
 function:

Copy

\>>> from math import floor
\>>> floor(Fraction(355, 113))
3

\_\_ceil\_\_()[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.__ceil__ "Link to this definition")

Returns the least [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 `>= self`. This method can also be accessed through the [`math.ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
 function.

\_\_round\_\_()[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.__round__ "Link to this definition")

\_\_round\_\_(_ndigits_)

The first version returns the nearest [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 to `self`, rounding half to even. The second version rounds `self` to the nearest multiple of `Fraction(1, 10**ndigits)` (logically, if `ndigits` is negative), again rounding half toward even. This method can also be accessed through the [`round()`](https://docs.python.org/3/builtins/functions.html#round "round")
 function.

\_\_format\_\_(_format\_spec_, _/_)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction.__format__ "Link to this definition")

Provides support for formatting of `Fraction` instances via the [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
 method, the [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
 built-in function, or [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
.

If the `format_spec` format specification string does not end with one of the presentation types `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'%'` then formatting follows the general rules for fill, alignment, sign handling, minimum width, and grouping as described in the [format specification mini-language](https://docs.python.org/3/library/string.html#formatspec)
. The “alternate form” flag `'#'` is supported: if present, it forces the output string to always include an explicit denominator, even when the value being formatted is an exact integer. The zero-fill flag `'0'` is not supported.

If the `format_spec` format specification string ends with one of the presentation types `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'%'` then formatting follows the rules outlined for the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type in the [Format specification mini-language](https://docs.python.org/3/library/string.html#formatspec)
 section.

Here are some examples:

Copy

\>>> from fractions import Fraction
\>>> format(Fraction(103993, 33102), '\_')
'103\_993/33\_102'
\>>> format(Fraction(1, 7), '.^+10')
'...+1/7...'
\>>> format(Fraction(3, 1), '')
'3'
\>>> format(Fraction(3, 1), '#')
'3/1'
\>>> format(Fraction(1, 7), '.40g')
'0.1428571428571428571428571428571428571429'
\>>> format(Fraction('1234567.855'), '\_.2f')
'1\_234\_567.86'
\>>> f"{Fraction(355, 113):\*>20.6e}"
'\*\*\*\*\*\*\*\*3.141593e+00'
\>>> old\_price, new\_price \= 499, 672
\>>> "{:.2%} price increase".format(Fraction(new\_price, old\_price) \- 1)
'34.67% price increase'

See also

Module [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).")

The abstract base classes making up the numeric tower.

#### Previous topic

[`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html "previous chapter")

#### Next topic

[`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fractions+%E2%80%94+Rational+numbers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffractions.html&pagesource=library%2Ffractions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/fractions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/random.html "random — Generate pseudo-random numbers")
     |
*   [previous](https://docs.python.org/3/library/decimal.html "decimal — Decimal fixed-point and floating-point arithmetic")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)
     »
*   [`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html)
    
*    
    
    |
*   Theme Auto Light Dark |