### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/numbers.html "numbers — Numeric abstract base classes")
     |
*   [previous](https://docs.python.org/3/library/graphlib.html "graphlib — Functionality to operate with graph-like structures")
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
    
*    
    
    |
*   Theme Auto Light Dark |

Numeric and Mathematical Modules[¶](https://docs.python.org/3/library/numeric.html#numeric-and-mathematical-modules "Link to this heading")

============================================================================================================================================

The modules described in this chapter provide numeric and math-related functions and data types. The [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).")
 module defines an abstract hierarchy of numeric types. The [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 and [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
 modules contain various mathematical functions for floating-point and complex numbers. The [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module supports exact representations of decimal numbers, using arbitrary precision arithmetic.

The following modules are documented in this chapter:

*   [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    *   [The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
        
    *   [Notes for type implementers](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers)
        *   [Adding more numeric ABCs](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs)
            
        *   [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)
            
*   [`math` — Mathematical functions](https://docs.python.org/3/library/math.html)
    *   [Floating point arithmetic](https://docs.python.org/3/library/math.html#floating-point-arithmetic)
        
    *   [Floating point manipulation functions](https://docs.python.org/3/library/math.html#floating-point-manipulation-functions)
        
    *   [Power, exponential and logarithmic functions](https://docs.python.org/3/library/math.html#power-exponential-and-logarithmic-functions)
        
    *   [Summation and product functions](https://docs.python.org/3/library/math.html#summation-and-product-functions)
        
    *   [Angular conversion](https://docs.python.org/3/library/math.html#angular-conversion)
        
    *   [Trigonometric functions](https://docs.python.org/3/library/math.html#trigonometric-functions)
        
    *   [Hyperbolic functions](https://docs.python.org/3/library/math.html#hyperbolic-functions)
        
    *   [Special functions](https://docs.python.org/3/library/math.html#special-functions)
        
    *   [Number-theoretic functions](https://docs.python.org/3/library/math.html#number-theoretic-functions)
        
    *   [Constants](https://docs.python.org/3/library/math.html#constants)
        
*   [`math.integer` — integer-specific mathematics functions](https://docs.python.org/3/library/math.integer.html)
    
*   [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
    *   [Conversions to and from polar coordinates](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates)
        
    *   [Power and logarithmic functions](https://docs.python.org/3/library/cmath.html#power-and-logarithmic-functions)
        
    *   [Trigonometric functions](https://docs.python.org/3/library/cmath.html#trigonometric-functions)
        
    *   [Hyperbolic functions](https://docs.python.org/3/library/cmath.html#hyperbolic-functions)
        
    *   [Classification functions](https://docs.python.org/3/library/cmath.html#classification-functions)
        
    *   [Constants](https://docs.python.org/3/library/cmath.html#constants)
        
*   [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
    *   [Quick-start tutorial](https://docs.python.org/3/library/decimal.html#quick-start-tutorial)
        
    *   [Decimal objects](https://docs.python.org/3/library/decimal.html#decimal-objects)
        *   [Logical operands](https://docs.python.org/3/library/decimal.html#logical-operands)
            
    *   [Context objects](https://docs.python.org/3/library/decimal.html#context-objects)
        
    *   [Constants](https://docs.python.org/3/library/decimal.html#constants)
        
    *   [Rounding modes](https://docs.python.org/3/library/decimal.html#rounding-modes)
        
    *   [Signals](https://docs.python.org/3/library/decimal.html#signals)
        
    *   [Floating-point notes](https://docs.python.org/3/library/decimal.html#floating-point-notes)
        *   [Mitigating round-off error with increased precision](https://docs.python.org/3/library/decimal.html#mitigating-round-off-error-with-increased-precision)
            
        *   [Special values](https://docs.python.org/3/library/decimal.html#special-values)
            
    *   [Working with threads](https://docs.python.org/3/library/decimal.html#working-with-threads)
        
    *   [Recipes](https://docs.python.org/3/library/decimal.html#recipes)
        
    *   [Decimal FAQ](https://docs.python.org/3/library/decimal.html#decimal-faq)
        
*   [`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html)
    
*   [`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
    *   [Bookkeeping functions](https://docs.python.org/3/library/random.html#bookkeeping-functions)
        
    *   [Functions for bytes](https://docs.python.org/3/library/random.html#functions-for-bytes)
        
    *   [Functions for integers](https://docs.python.org/3/library/random.html#functions-for-integers)
        
    *   [Functions for sequences](https://docs.python.org/3/library/random.html#functions-for-sequences)
        
    *   [Discrete distributions](https://docs.python.org/3/library/random.html#discrete-distributions)
        
    *   [Real-valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions)
        
    *   [Alternative Generator](https://docs.python.org/3/library/random.html#alternative-generator)
        
    *   [Notes on Reproducibility](https://docs.python.org/3/library/random.html#notes-on-reproducibility)
        
    *   [Examples](https://docs.python.org/3/library/random.html#examples)
        
    *   [Recipes](https://docs.python.org/3/library/random.html#recipes)
        
    *   [Command-line usage](https://docs.python.org/3/library/random.html#command-line-usage)
        
    *   [Command-line example](https://docs.python.org/3/library/random.html#command-line-example)
        
*   [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
    *   [Averages and measures of central location](https://docs.python.org/3/library/statistics.html#averages-and-measures-of-central-location)
        
    *   [Measures of spread](https://docs.python.org/3/library/statistics.html#measures-of-spread)
        
    *   [Statistics for relations between two inputs](https://docs.python.org/3/library/statistics.html#statistics-for-relations-between-two-inputs)
        
    *   [Function details](https://docs.python.org/3/library/statistics.html#function-details)
        
    *   [Exceptions](https://docs.python.org/3/library/statistics.html#exceptions)
        
    *   [`NormalDist` objects](https://docs.python.org/3/library/statistics.html#normaldist-objects)
        
    *   [Examples and Recipes](https://docs.python.org/3/library/statistics.html#examples-and-recipes)
        *   [Classic probability problems](https://docs.python.org/3/library/statistics.html#classic-probability-problems)
            
        *   [Monte Carlo inputs for simulations](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations)
            
        *   [Approximating binomial distributions](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions)
            
        *   [Naive bayesian classifier](https://docs.python.org/3/library/statistics.html#naive-bayesian-classifier)
            

#### Previous topic

[`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html "previous chapter")

#### Next topic

[`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Numeric+and+Mathematical+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumeric.html&pagesource=library%2Fnumeric.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/numeric.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/numbers.html "numbers — Numeric abstract base classes")
     |
*   [previous](https://docs.python.org/3/library/graphlib.html "graphlib — Functionality to operate with graph-like structures")
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
    
*    
    
    |
*   Theme Auto Light Dark |