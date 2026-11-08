### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/math.html "math — Mathematical functions")
     |
*   [previous](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules")
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
*   [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`numbers` — Numeric abstract base classes[¶](https://docs.python.org/3/library/numbers.html#module-numbers "Link to this heading")

===================================================================================================================================

**Source code:** [Lib/numbers.py](https://github.com/python/cpython/tree/3.15/Lib/numbers.py)

* * *

The `numbers` module ([**PEP 3141**](https://peps.python.org/pep-3141/)
) defines a hierarchy of numeric [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 which progressively define more operations. None of the types defined in this module are intended to be instantiated.

class numbers.Number[¶](https://docs.python.org/3/library/numbers.html#numbers.Number "Link to this definition")

The root of the numeric hierarchy. If you just want to check if an argument _x_ is a number, without caring what kind, use `isinstance(x, Number)`.

The numeric tower[¶](https://docs.python.org/3/library/numbers.html#the-numeric-tower "Link to this heading")

--------------------------------------------------------------------------------------------------------------

class numbers.Complex[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex "Link to this definition")

Subclasses of this type describe complex numbers and include the operations that work on the built-in [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 type. These are: conversions to `complex` and [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
, [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real")
, [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag")
, `+`, `-`, `*`, `/`, `**`, [`abs()`](https://docs.python.org/3/builtins/functions.html#abs "abs")
, [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate")
, `==`, and `!=`. All except `-` and `!=` are abstract.

real[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "Link to this definition")

Abstract. Retrieves the real component of this number.

imag[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "Link to this definition")

Abstract. Retrieves the imaginary component of this number.

abstractmethod conjugate()[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "Link to this definition")

Abstract. Returns the complex conjugate. For example, `(1+3j).conjugate() == (1-3j)`.

class numbers.Real[¶](https://docs.python.org/3/library/numbers.html#numbers.Real "Link to this definition")

To [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
, `Real` adds the operations that work on real numbers.

In short, those are: a conversion to [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`math.trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc")
, [`round()`](https://docs.python.org/3/builtins/functions.html#round "round")
, [`math.floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor")
, [`math.ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
, [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
, `//`, `%`, `<`, `<=`, `>`, and `>=`.

Real also provides defaults for [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
, [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real")
, [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag")
, and [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate")
.

class numbers.Rational[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational "Link to this definition")

Subtypes [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
 and adds [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator")
 and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator")
 properties. It also provides a default for [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
.

The [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator")
 and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator")
 values should be instances of [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
 and should be in lowest terms with `denominator` positive.

numerator[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "Link to this definition")

Abstract. The numerator of this rational number.

denominator[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "Link to this definition")

Abstract. The denominator of this rational number.

class numbers.Integral[¶](https://docs.python.org/3/library/numbers.html#numbers.Integral "Link to this definition")

Subtypes [`Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
 and adds a conversion to [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. Provides defaults for [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator")
, and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator")
. Adds abstract methods for [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
 with modulus and bit-string operations: `<<`, `>>`, `&`, `^`, `|`, `~`.

Notes for type implementers[¶](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Implementers should be careful to make equal numbers equal and hash them to the same values. This may be subtle if there are two different extensions of the real numbers. See also [Hashing of numeric types](https://docs.python.org/3/builtins/stdtypes.html#numeric-hash)
.

### Adding more numeric ABCs[¶](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs "Link to this heading")

There are, of course, more possible ABCs for numbers, and this would be a poor hierarchy if it precluded the possibility of adding those. You can add `MyFoo` between [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
 and [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
 with:

Copy

class MyFoo(Complex): ...
MyFoo.register(Real)

### Implementing the arithmetic operations[¶](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations "Link to this heading")

We want to implement the arithmetic operations so that mixed-mode operations either call an implementation whose author knew about the types of both arguments, or convert both to the nearest built in type and do the operation there. For subtypes of [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
, this means that [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
 and [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
 should be defined as:

Copy

class MyIntegral(Integral):

    def \_\_add\_\_(self, other):
        if isinstance(other, MyIntegral):
            return do\_my\_adding\_stuff(self, other)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do\_my\_other\_adding\_stuff(self, other)
        else:
            return NotImplemented

    def \_\_radd\_\_(self, other):
        if isinstance(other, MyIntegral):
            return do\_my\_adding\_stuff(other, self)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do\_my\_other\_adding\_stuff(other, self)
        elif isinstance(other, Integral):
            return int(other) + int(self)
        elif isinstance(other, Real):
            return float(other) + float(self)
        elif isinstance(other, Complex):
            return complex(other) + complex(self)
        else:
            return NotImplemented

There are 5 different cases for a mixed-type operation on subclasses of [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
. All of the above code that doesn’t refer to `MyIntegral` and `OtherTypeIKnowAbout` is referred to as “boilerplate”.

In this description, `a` is an instance of `A` and `b` is an instance of `B`, where `A` and `B` are both subtypes of [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
. Consider `a + b`:

1.  If `A` defines an [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
     which accepts `b`, all is well.
    
2.  If `A` falls back to the boilerplate code, and it were to return a value from [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
    , we’d miss the possibility that `B` defines a more intelligent [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
    , so the boilerplate should return [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
     from `__add__()`. (Or `A` may not implement `__add__()` at all.)
    
3.  Then `B`’s [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
     gets a chance. If it accepts `a`, all is well.
    
4.  If it falls back to the boilerplate, there are no more possible methods to try, so this is where the default implementation should live.
    
5.  If `B` is a subtype of `A`, Python tries `B.__radd__` before `A.__add__`. This is ok, because it was implemented with knowledge of `A`, so it can handle those instances before delegating to [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
    .
    

If `A` is a subtype of [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
 and `B` is a subtype of [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
 without sharing any other knowledge, then the appropriate shared operation is the one involving the built in [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
, and both [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
 s land there, so `a+b == b+a`.

Because most of the operations on any given type will be very similar, it can be useful to define a helper function which generates the forward and reverse instances of any given operator. For example, [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
 uses:

Copy

def \_operator\_fallbacks(monomorphic\_operator, fallback\_operator):
    def forward(a, b):
        if isinstance(b, (int, Fraction)):
            return monomorphic\_operator(a, b)
        elif isinstance(b, float):
            return fallback\_operator(float(a), b)
        elif isinstance(b, complex):
            return fallback\_operator(complex(a), b)
        else:
            return NotImplemented
    forward.\_\_name\_\_ \= '\_\_' + fallback\_operator.\_\_name\_\_ + '\_\_'
    forward.\_\_doc\_\_ \= monomorphic\_operator.\_\_doc\_\_

    def reverse(b, a):
        if isinstance(a, Rational):
            \# Includes ints.
            return monomorphic\_operator(a, b)
        elif isinstance(a, Real):
            return fallback\_operator(float(a), float(b))
        elif isinstance(a, Complex):
            return fallback\_operator(complex(a), complex(b))
        else:
            return NotImplemented
    reverse.\_\_name\_\_ \= '\_\_r' + fallback\_operator.\_\_name\_\_ + '\_\_'
    reverse.\_\_doc\_\_ \= monomorphic\_operator.\_\_doc\_\_

    return forward, reverse

def \_add(a, b):
    """a + b"""
    return Fraction(a.numerator \* b.denominator +
                    b.numerator \* a.denominator,
                    a.denominator \* b.denominator)

\_\_add\_\_, \_\_radd\_\_ \= \_operator\_fallbacks(\_add, operator.add)

\# ...

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html#)
    *   [The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
        
    *   [Notes for type implementers](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers)
        *   [Adding more numeric ABCs](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs)
            
        *   [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)
            

#### Previous topic

[Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html "previous chapter")

#### Next topic

[`math` — Mathematical functions](https://docs.python.org/3/library/math.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=numbers+%E2%80%94+Numeric+abstract+base+classes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumbers.html&pagesource=library%2Fnumbers.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/numbers.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/math.html "math — Mathematical functions")
     |
*   [previous](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules")
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
*   [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    
*    
    
    |
*   Theme Auto Light Dark |