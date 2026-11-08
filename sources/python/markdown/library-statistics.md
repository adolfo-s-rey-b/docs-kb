### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/functional.html "Functional Programming Modules")
     |
*   [previous](https://docs.python.org/3/library/random.html "random — Generate pseudo-random numbers")
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
*   [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`statistics` — Mathematical statistics functions[¶](https://docs.python.org/3/library/statistics.html#module-statistics "Link to this heading")

================================================================================================================================================

Added in version 3.4.

**Source code:** [Lib/statistics.py](https://github.com/python/cpython/tree/3.15/Lib/statistics.py)

* * *

This module provides functions for calculating mathematical statistics of numeric ([`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
\-valued) data.

The module is not intended to be a competitor to third-party libraries such as [NumPy](https://numpy.org/)
, [SciPy](https://scipy.org/)
, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

Unless explicitly noted, these functions support [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
 and [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
. Behaviour with other types (whether in the numeric tower or not) is currently unsupported. Collections with a mix of types are also undefined and implementation-dependent. If your input data consists of mixed types, you may be able to use [`map()`](https://docs.python.org/3/builtins/functions.html#map "map")
 to ensure a consistent result, for example: `map(float, input_data)`.

Some datasets use `NaN` (not a number) values to represent missing data. Since NaNs have unusual comparison semantics, they cause surprising or undefined behaviors in the statistics functions that sort data or that count occurrences. The functions affected are `median()`, `median_low()`, `median_high()`, `median_grouped()`, `mode()`, `multimode()`, and `quantiles()`. The `NaN` values should be stripped before calling these functions:

Copy

\>>> from statistics import median
\>>> from math import isnan
\>>> from itertools import filterfalse

\>>> data \= \[20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4\]
\>>> sorted(data)  \# This has surprising behavior
\[20.7, nan, 14.4, 18.3, 19.2, nan\]
\>>> median(data)  \# This result is unexpected
16.35

\>>> sum(map(isnan, data))    \# Number of missing values
2
\>>> clean \= list(filterfalse(isnan, data))  \# Strip NaN values
\>>> clean
\[20.7, 19.2, 18.3, 14.4\]
\>>> sorted(clean)  \# Sorting now works as expected
\[14.4, 18.3, 19.2, 20.7\]
\>>> median(clean)       \# This result is now well defined
18.75

Averages and measures of central location[¶](https://docs.python.org/3/library/statistics.html#averages-and-measures-of-central-location "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

These functions calculate an average or typical value from a population or sample.

|     |     |
| --- | --- |
| [`mean()`](https://docs.python.org/3/library/statistics.html#statistics.mean "statistics.mean") | Arithmetic mean (“average”) of data. |
| [`fmean()`](https://docs.python.org/3/library/statistics.html#statistics.fmean "statistics.fmean") | Fast, floating-point arithmetic mean, with optional weighting. |
| [`geometric_mean()`](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean "statistics.geometric_mean") | Geometric mean of data. |
| [`harmonic_mean()`](https://docs.python.org/3/library/statistics.html#statistics.harmonic_mean "statistics.harmonic_mean") | Harmonic mean of data. |
| [`kde()`](https://docs.python.org/3/library/statistics.html#statistics.kde "statistics.kde") | Estimate the probability density distribution of the data. |
| [`kde_random()`](https://docs.python.org/3/library/statistics.html#statistics.kde_random "statistics.kde_random") | Random sampling from the PDF generated by kde(). |
| [`median()`](https://docs.python.org/3/library/statistics.html#statistics.median "statistics.median") | Median (middle value) of data. |
| [`median_low()`](https://docs.python.org/3/library/statistics.html#statistics.median_low "statistics.median_low") | Low median of data. |
| [`median_high()`](https://docs.python.org/3/library/statistics.html#statistics.median_high "statistics.median_high") | High median of data. |
| [`median_grouped()`](https://docs.python.org/3/library/statistics.html#statistics.median_grouped "statistics.median_grouped") | Median (50th percentile) of grouped data. |
| [`mode()`](https://docs.python.org/3/library/statistics.html#statistics.mode "statistics.mode") | Single mode (most common value) of discrete or nominal data. |
| [`multimode()`](https://docs.python.org/3/library/statistics.html#statistics.multimode "statistics.multimode") | List of modes (most common values) of discrete or nominal data. |
| [`quantiles()`](https://docs.python.org/3/library/statistics.html#statistics.quantiles "statistics.quantiles") | Divide data into intervals with equal probability. |

Measures of spread[¶](https://docs.python.org/3/library/statistics.html#measures-of-spread "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

These functions calculate a measure of how much the population or sample tends to deviate from the typical or average values.

|     |     |
| --- | --- |
| [`pstdev()`](https://docs.python.org/3/library/statistics.html#statistics.pstdev "statistics.pstdev") | Population standard deviation of data. |
| [`pvariance()`](https://docs.python.org/3/library/statistics.html#statistics.pvariance "statistics.pvariance") | Population variance of data. |
| [`stdev()`](https://docs.python.org/3/library/statistics.html#statistics.stdev "statistics.stdev") | Sample standard deviation of data. |
| [`variance()`](https://docs.python.org/3/library/statistics.html#statistics.variance "statistics.variance") | Sample variance of data. |

Statistics for relations between two inputs[¶](https://docs.python.org/3/library/statistics.html#statistics-for-relations-between-two-inputs "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

These functions calculate statistics regarding relations between two inputs.

|     |     |
| --- | --- |
| [`covariance()`](https://docs.python.org/3/library/statistics.html#statistics.covariance "statistics.covariance") | Sample covariance for two variables. |
| [`correlation()`](https://docs.python.org/3/library/statistics.html#statistics.correlation "statistics.correlation") | Pearson and Spearman’s correlation coefficients. |
| [`linear_regression()`](https://docs.python.org/3/library/statistics.html#statistics.linear_regression "statistics.linear_regression") | Slope and intercept for simple linear regression. |

Function details[¶](https://docs.python.org/3/library/statistics.html#function-details "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Note: The functions do not require the data given to them to be sorted. However, for reading convenience, most of the examples show sorted sequences.

statistics.mean(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.mean "Link to this definition")

Return the sample arithmetic mean of _data_ which can be a sequence or iterable.

The arithmetic mean is the sum of the data divided by the number of data points. It is commonly called “the average”, although it is only one of many different mathematical averages. It is a measure of the central location of the data.

If _data_ is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 will be raised.

Some examples of use:

Copy

\>>> mean(\[1, 2, 3, 4, 4\])
2.8
\>>> mean(\[\-1.0, 2.5, 3.25, 5.75\])
2.625

\>>> from fractions import Fraction as F
\>>> mean(\[F(3, 7), F(1, 21), F(5, 3), F(1, 3)\])
Fraction(13, 21)

\>>> from decimal import Decimal as D
\>>> mean(\[D("0.5"), D("0.75"), D("0.625"), D("0.375")\])
Decimal('0.5625')

Note

The mean is strongly affected by [outliers](https://en.wikipedia.org/wiki/Outlier)
 and is not necessarily a typical example of the data points. For a more robust, although less efficient, measure of [central tendency](https://en.wikipedia.org/wiki/Central_tendency)
, see [`median()`](https://docs.python.org/3/library/statistics.html#statistics.median "statistics.median")
.

The sample mean gives an unbiased estimate of the true population mean, so that when taken on average over all the possible samples, `mean(sample)` converges on the true mean of the entire population. If _data_ represents the entire population rather than a sample, then `mean(data)` is equivalent to calculating the true population mean μ.

statistics.fmean(_data_, _weights\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.fmean "Link to this definition")

Convert _data_ to floats and compute the arithmetic mean.

This runs faster than the [`mean()`](https://docs.python.org/3/library/statistics.html#statistics.mean "statistics.mean")
 function and it always returns a [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
. The _data_ may be a sequence or iterable. If the input dataset is empty, raises a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
.

Copy

\>>> fmean(\[3.5, 4.0, 5.25\])
4.25

Optional weighting is supported. For example, a professor assigns a grade for a course by weighting quizzes at 20%, homework at 20%, a midterm exam at 30%, and a final exam at 30%:

Copy

\>>> grades \= \[85, 92, 83, 91\]
\>>> weights \= \[0.20, 0.20, 0.30, 0.30\]
\>>> fmean(grades, weights)
87.6

If _weights_ is supplied, it must be the same length as the _data_ or a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised.

Added in version 3.8.

Changed in version 3.11: Added support for _weights_.

statistics.geometric\_mean(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean "Link to this definition")

Convert _data_ to floats and compute the geometric mean.

The geometric mean indicates the central tendency or typical value of the _data_ using the product of the values (as opposed to the arithmetic mean which uses their sum).

Raises a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 if the input dataset is empty, if it contains a zero, or if it contains a negative value. The _data_ may be a sequence or iterable.

No special efforts are made to achieve exact results. (However, this may change in the future.)

Copy

\>>> round(geometric\_mean(\[54, 24, 36\]), 1)
36.0

Added in version 3.8.

statistics.harmonic\_mean(_data_, _weights\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.harmonic_mean "Link to this definition")

Return the harmonic mean of _data_, a sequence or iterable of real-valued numbers. If _weights_ is omitted or `None`, then equal weighting is assumed.

The harmonic mean is the reciprocal of the arithmetic [`mean()`](https://docs.python.org/3/library/statistics.html#statistics.mean "statistics.mean")
 of the reciprocals of the data. For example, the harmonic mean of three values _a_, _b_ and _c_ will be equivalent to `3/(1/a + 1/b + 1/c)`. If one of the values is zero, the result will be zero.

The harmonic mean is a type of average, a measure of the central location of the data. It is often appropriate when averaging ratios or rates, for example speeds.

Suppose a car travels 10 km at 40 km/hr, then another 10 km at 60 km/hr. What is the average speed?

Copy

\>>> harmonic\_mean(\[40, 60\])
48.0

Suppose a car travels 40 km/hr for 5 km, and when traffic clears, speeds-up to 60 km/hr for the remaining 30 km of the journey. What is the average speed?

Copy

\>>> harmonic\_mean(\[40, 60\], weights\=\[5, 30\])
56.0

[`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised if _data_ is empty, any element is less than zero, or if the weighted sum isn’t positive.

The current algorithm has an early-out when it encounters a zero in the input. This means that the subsequent inputs are not tested for validity. (This behavior may change in the future.)

Added in version 3.6.

Changed in version 3.10: Added support for _weights_.

statistics.kde(_data_, _h_, _kernel\='normal'_, _\*_, _cumulative\=False_)[¶](https://docs.python.org/3/library/statistics.html#statistics.kde "Link to this definition")

[Kernel Density Estimation (KDE)](https://www.itm-conferences.org/articles/itmconf/pdf/2018/08/itmconf_sam2018_00037.pdf)
: Create a continuous probability density function or cumulative distribution function from discrete samples.

The basic idea is to smooth the data using [a kernel function](https://en.wikipedia.org/wiki/Kernel_(statistics))
. to help draw inferences about a population from a sample.

The degree of smoothing is controlled by the scaling parameter _h_ which is called the bandwidth. Smaller values emphasize local features while larger values give smoother results.

The _kernel_ determines the relative weights of the sample data points. Generally, the choice of kernel shape does not matter as much as the more influential bandwidth smoothing parameter.

Kernels that give some weight to every sample point include _normal_ (_gauss_), _logistic_, and _sigmoid_.

Kernels that only give weight to sample points within the bandwidth include _rectangular_ (_uniform_), _triangular_, _parabolic_ (_epanechnikov_), _quartic_ (_biweight_), _triweight_, and _cosine_.

If _cumulative_ is true, will return a cumulative distribution function.

A [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 will be raised if the _data_ sequence is empty.

[Wikipedia has an example](https://en.wikipedia.org/wiki/Kernel_density_estimation#Example)
 where we can use `kde()` to generate and plot a probability density function estimated from a small sample:

Copy

\>>> sample \= \[\-2.1, \-1.3, \-0.4, 1.9, 5.1, 6.2\]
\>>> f\_hat \= kde(sample, h\=1.5)
\>>> xarr \= \[i/100 for i in range(\-750, 1100)\]
\>>> yarr \= \[f\_hat(x) for x in xarr\]

The points in `xarr` and `yarr` can be used to make a PDF plot:

![Scatter plot of the estimated probability density function.](https://docs.python.org/3/_images/kde_example.png)

Added in version 3.13.

statistics.kde\_random(_data_, _h_, _kernel\='normal'_, _\*_, _seed\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.kde_random "Link to this definition")

Return a function that makes a random selection from the estimated probability density function produced by `kde(data, h, kernel)`.

Providing a _seed_ allows reproducible selections. In the future, the values may change slightly as more accurate kernel inverse CDF estimates are implemented. The seed may be an integer, float, str, or bytes.

A [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 will be raised if the _data_ sequence is empty.

Continuing the example for [`kde()`](https://docs.python.org/3/library/statistics.html#statistics.kde "statistics.kde")
, we can use `kde_random()` to generate new random selections from an estimated probability density function:

Copy

\>>> data \= \[\-2.1, \-1.3, \-0.4, 1.9, 5.1, 6.2\]
\>>> rand \= kde\_random(data, h\=1.5, seed\=8675309)
\>>> new\_selections \= \[rand() for i in range(10)\]
\>>> \[round(x, 1) for x in new\_selections\]
\[0.7, 6.2, 1.2, 6.9, 7.0, 1.8, 2.5, -0.5, -1.8, 5.6\]

Added in version 3.13.

statistics.median(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.median "Link to this definition")

Return the median (middle value) of numeric data, using the common “mean of middle two” method. If _data_ is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised. _data_ can be a sequence or iterable.

The median is a robust measure of central location and is less affected by the presence of outliers. When the number of data points is odd, the middle data point is returned:

Copy

\>>> median(\[1, 3, 5\])
3

When the number of data points is even, the median is interpolated by taking the average of the two middle values:

Copy

\>>> median(\[1, 3, 5, 7\])
4.0

This is suited for when your data is discrete, and you don’t mind that the median may not be an actual data point.

If the data is ordinal (supports order operations) but not numeric (doesn’t support addition), consider using [`median_low()`](https://docs.python.org/3/library/statistics.html#statistics.median_low "statistics.median_low")
 or [`median_high()`](https://docs.python.org/3/library/statistics.html#statistics.median_high "statistics.median_high")
 instead.

statistics.median\_low(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.median_low "Link to this definition")

Return the low median of numeric data. If _data_ is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised. _data_ can be a sequence or iterable.

The low median is always a member of the data set. When the number of data points is odd, the middle value is returned. When it is even, the smaller of the two middle values is returned.

Copy

\>>> median\_low(\[1, 3, 5\])
3
\>>> median\_low(\[1, 3, 5, 7\])
3

Use the low median when your data are discrete and you prefer the median to be an actual data point rather than interpolated.

statistics.median\_high(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.median_high "Link to this definition")

Return the high median of data. If _data_ is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised. _data_ can be a sequence or iterable.

The high median is always a member of the data set. When the number of data points is odd, the middle value is returned. When it is even, the larger of the two middle values is returned.

Copy

\>>> median\_high(\[1, 3, 5\])
3
\>>> median\_high(\[1, 3, 5, 7\])
5

Use the high median when your data are discrete and you prefer the median to be an actual data point rather than interpolated.

statistics.median\_grouped(_data_, _interval\=1.0_)[¶](https://docs.python.org/3/library/statistics.html#statistics.median_grouped "Link to this definition")

Estimates the median for numeric data that has been [grouped or binned](https://en.wikipedia.org/wiki/Data_binning)
 around the midpoints of consecutive, fixed-width intervals.

The _data_ can be any iterable of numeric data with each value being exactly the midpoint of a bin. At least one value must be present.

The _interval_ is the width of each bin.

For example, demographic information may have been summarized into consecutive ten-year age groups with each group being represented by the 5-year midpoints of the intervals:

Copy

\>>> from collections import Counter
\>>> demographics \= Counter({
...    25: 172,   \# 20 to 30 years old
...    35: 484,   \# 30 to 40 years old
...    45: 387,   \# 40 to 50 years old
...    55:  22,   \# 50 to 60 years old
...    65:   6,   \# 60 to 70 years old
... })
...

The 50th percentile (median) is the 536th person out of the 1071 member cohort. That person is in the 30 to 40 year old age group.

The regular [`median()`](https://docs.python.org/3/library/statistics.html#statistics.median "statistics.median")
 function would assume that everyone in the tricenarian age group was exactly 35 years old. A more tenable assumption is that the 484 members of that age group are evenly distributed between 30 and 40. For that, we use `median_grouped()`:

Copy

\>>> data \= list(demographics.elements())
\>>> median(data)
35
\>>> round(median\_grouped(data, interval\=10), 1)
37.5

The caller is responsible for making sure the data points are separated by exact multiples of _interval_. This is essential for getting a correct result. The function does not check this precondition.

Inputs may be any numeric type that can be coerced to a float during the interpolation step.

statistics.mode(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.mode "Link to this definition")

Return the single most common data point from discrete or nominal _data_. The mode (when it exists) is the most typical value and serves as a measure of central location.

If there are multiple modes with the same frequency, returns the first one encountered in the _data_. If the smallest or largest of those is desired instead, use `min(multimode(data))` or `max(multimode(data))`. If the input _data_ is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised.

`mode` assumes discrete data and returns a single value. This is the standard treatment of the mode as commonly taught in schools:

Copy

\>>> mode(\[1, 1, 2, 3, 3, 3, 3, 4\])
3

The mode is unique in that it is the only statistic in this package that also applies to nominal (non-numeric) data:

Copy

\>>> mode(\["red", "blue", "blue", "red", "green", "red", "red"\])
'red'

Only hashable inputs are supported. To handle type [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, consider casting to [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
. To handle type [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, consider casting to [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
. For mixed or nested inputs, consider using this slower quadratic algorithm that only depends on equality tests: `max(data, key=data.count)`.

Changed in version 3.8: Now handles multimodal datasets by returning the first mode encountered. Formerly, it raised [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 when more than one mode was found.

statistics.multimode(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.multimode "Link to this definition")

Return a list of the most frequently occurring values in the order they were first encountered in the _data_. Will return more than one result if there are multiple modes or an empty list if the _data_ is empty:

Copy

\>>> multimode('aabbbbccddddeeffffgg')
\['b', 'd', 'f'\]
\>>> multimode('')
\[\]

Added in version 3.8.

statistics.pstdev(_data_, _mu\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.pstdev "Link to this definition")

Return the population standard deviation (the square root of the population variance). See [`pvariance()`](https://docs.python.org/3/library/statistics.html#statistics.pvariance "statistics.pvariance")
 for arguments and other details.

Copy

\>>> pstdev(\[1.5, 2.5, 2.5, 2.75, 3.25, 4.75\])
0.986893273527251

statistics.pvariance(_data_, _mu\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.pvariance "Link to this definition")

Return the population variance of _data_, a non-empty sequence or iterable of real-valued numbers. Variance, or second moment about the mean, is a measure of the variability (spread or dispersion) of data. A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.

If the optional second argument _mu_ is given, it should be the _population_ mean of the _data_. It can also be used to compute the second moment around a point that is not the mean. If it is missing or `None` (the default), the arithmetic mean is automatically calculated.

Use this function to calculate the variance from the entire population. To estimate the variance from a sample, the [`variance()`](https://docs.python.org/3/library/statistics.html#statistics.variance "statistics.variance")
 function is usually a better choice.

Raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 if _data_ is empty.

Examples:

Copy

\>>> data \= \[0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25\]
\>>> pvariance(data)
1.25

If you have already calculated the mean of your data, you can pass it as the optional second argument _mu_ to avoid recalculation:

Copy

\>>> mu \= mean(data)
\>>> pvariance(data, mu)
1.25

Decimals and Fractions are supported:

Copy

\>>> from decimal import Decimal as D
\>>> pvariance(\[D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")\])
Decimal('24.815')

\>>> from fractions import Fraction as F
\>>> pvariance(\[F(1, 4), F(5, 4), F(1, 2)\])
Fraction(13, 72)

Note

When called with the entire population, this gives the population variance σ². When called on a sample instead, this is the biased sample variance s², also known as variance with N degrees of freedom.

If you somehow know the true population mean μ, you may use this function to calculate the variance of a sample, giving the known population mean as the second argument. Provided the data points are a random sample of the population, the result will be an unbiased estimate of the population variance.

statistics.stdev(_data_, _xbar\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.stdev "Link to this definition")

Return the sample standard deviation (the square root of the sample variance). See [`variance()`](https://docs.python.org/3/library/statistics.html#statistics.variance "statistics.variance")
 for arguments and other details.

Copy

\>>> stdev(\[1.5, 2.5, 2.5, 2.75, 3.25, 4.75\])
1.0810874155219827

statistics.variance(_data_, _xbar\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.variance "Link to this definition")

Return the sample variance of _data_, an iterable of at least two real-valued numbers. Variance, or second moment about the mean, is a measure of the variability (spread or dispersion) of data. A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.

If the optional second argument _xbar_ is given, it should be the _sample_ mean of _data_. If it is missing or `None` (the default), the mean is automatically calculated.

Use this function when your data is a sample from a population. To calculate the variance from the entire population, see [`pvariance()`](https://docs.python.org/3/library/statistics.html#statistics.pvariance "statistics.pvariance")
.

Raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 if _data_ has fewer than two values.

Examples:

Copy

\>>> data \= \[2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5\]
\>>> variance(data)
1.3720238095238095

If you have already calculated the sample mean of your data, you can pass it as the optional second argument _xbar_ to avoid recalculation:

Copy

\>>> m \= mean(data)
\>>> variance(data, m)
1.3720238095238095

This function does not attempt to verify that you have passed the actual mean as _xbar_. Using arbitrary values for _xbar_ can lead to invalid or impossible results.

Decimal and Fraction values are supported:

Copy

\>>> from decimal import Decimal as D
\>>> variance(\[D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")\])
Decimal('31.01875')

\>>> from fractions import Fraction as F
\>>> variance(\[F(1, 6), F(1, 2), F(5, 3)\])
Fraction(67, 108)

Note

This is the sample variance s² with Bessel’s correction, also known as variance with N-1 degrees of freedom. Provided that the data points are representative (e.g. independent and identically distributed), the result should be an unbiased estimate of the true population variance.

If you somehow know the actual population mean μ you should pass it to the [`pvariance()`](https://docs.python.org/3/library/statistics.html#statistics.pvariance "statistics.pvariance")
 function as the _mu_ parameter to get the variance of a sample.

statistics.quantiles(_data_, _\*_, _n\=4_, _method\='exclusive'_)[¶](https://docs.python.org/3/library/statistics.html#statistics.quantiles "Link to this definition")

Divide _data_ into _n_ continuous intervals with equal probability. Returns a list of `n - 1` cut points separating the intervals.

Set _n_ to 4 for quartiles (the default). Set _n_ to 10 for deciles. Set _n_ to 100 for percentiles which gives the 99 cuts points that separate _data_ into 100 equal sized groups. Raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 if _n_ is not least 1.

The _data_ can be any iterable containing sample data. For meaningful results, the number of data points in _data_ should be larger than _n_. Raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 if there is not at least one data point.

The cut points are linearly interpolated from the two nearest data points. For example, if a cut point falls one-third of the distance between two sample values, `100` and `112`, the cut-point will evaluate to `104`.

The _method_ for computing quantiles can be varied depending on whether the _data_ includes or excludes the lowest and highest possible values from the population.

The default _method_ is “exclusive” and is used for data sampled from a population that can have more extreme values than found in the samples. The portion of the population falling below the _i-th_ of _m_ sorted data points is computed as `i / (m + 1)`. Given nine sample values, the method sorts them and assigns the following percentiles: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%.

Setting the _method_ to “inclusive” is used for describing population data or for samples that are known to include the most extreme values from the population. The minimum value in _data_ is treated as the 0th percentile and the maximum value is treated as the 100th percentile. The portion of the population falling below the _i-th_ of _m_ sorted data points is computed as `(i - 1) / (m - 1)`. Given 11 sample values, the method sorts them and assigns the following percentiles: 0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%.

Copy

\# Decile cut points for empirically sampled data
\>>> data \= \[105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,\
...         100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,\
...         106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,\
...         111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,\
...         103, 107, 101, 81, 109, 104\]
\>>> \[round(q, 1) for q in quantiles(data, n\=10)\]
\[81.0, 86.2, 89.0, 99.4, 102.5, 103.6, 106.0, 109.8, 111.0\]

Added in version 3.8.

Changed in version 3.13: No longer raises an exception for an input with only a single data point. This allows quantile estimates to be built up one sample point at a time becoming gradually more refined with each new data point.

statistics.covariance(_x_, _y_, _/_)[¶](https://docs.python.org/3/library/statistics.html#statistics.covariance "Link to this definition")

Return the sample covariance of two sequence inputs _x_ and _y_. Covariance is a measure of the joint variability of two inputs.

Both inputs must be of the same length (no less than two), otherwise [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised.

Examples:

Copy

\>>> x \= \[1, 2, 3, 4, 5, 6, 7, 8, 9\]
\>>> y \= \[1, 2, 3, 1, 2, 3, 1, 2, 3\]
\>>> covariance(x, y)
0.75
\>>> z \= \[9, 8, 7, 6, 5, 4, 3, 2, 1\]
\>>> covariance(x, z)
\-7.5
\>>> covariance(z, x)
\-7.5

Added in version 3.10.

statistics.correlation(_x_, _y_, _/_, _\*_, _method\='linear'_)[¶](https://docs.python.org/3/library/statistics.html#statistics.correlation "Link to this definition")

Return the [Pearson’s correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
 for two sequence inputs. Pearson’s correlation coefficient _r_ takes values between -1 and +1. It measures the strength and direction of a linear relationship.

If _method_ is “ranked”, computes [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
 for two inputs. The data is replaced by ranks. Ties are averaged so that equal values receive the same rank. The resulting coefficient measures the strength of a monotonic relationship.

Spearman’s correlation coefficient is appropriate for ordinal data or for continuous data that doesn’t meet the linear proportion requirement for Pearson’s correlation coefficient.

Both inputs must be of the same length (no less than two), and need not to be constant, otherwise [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised.

Example with [Kepler’s laws of planetary motion](https://en.wikipedia.org/wiki/Kepler's_laws_of_planetary_motion)
:

Copy

\>>> \# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and  Neptune
\>>> orbital\_period \= \[88, 225, 365, 687, 4331, 10\_756, 30\_687, 60\_190\]    \# days
\>>> dist\_from\_sun \= \[58, 108, 150, 228, 778, 1\_400, 2\_900, 4\_500\] \# million km

\>>> \# Show that a perfect monotonic relationship exists
\>>> correlation(orbital\_period, dist\_from\_sun, method\='ranked')
1.0

\>>> \# Observe that a linear relationship is imperfect
\>>> round(correlation(orbital\_period, dist\_from\_sun), 4)
0.9882

\>>> \# Demonstrate Kepler's third law: There is a linear correlation
\>>> \# between the square of the orbital period and the cube of the
\>>> \# distance from the sun.
\>>> period\_squared \= \[p \* p for p in orbital\_period\]
\>>> dist\_cubed \= \[d \* d \* d for d in dist\_from\_sun\]
\>>> round(correlation(period\_squared, dist\_cubed), 4)
1.0

Added in version 3.10.

Changed in version 3.12: Added support for Spearman’s rank correlation coefficient.

statistics.linear\_regression(_x_, _y_, _/_, _\*_, _proportional\=False_)[¶](https://docs.python.org/3/library/statistics.html#statistics.linear_regression "Link to this definition")

Return the slope and intercept of [simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression)
 parameters estimated using ordinary least squares. Simple linear regression describes the relationship between an independent variable _x_ and a dependent variable _y_ in terms of this linear function:

> _y = slope \* x + intercept + noise_

where `slope` and `intercept` are the regression parameters that are estimated, and `noise` represents the variability of the data that was not explained by the linear regression (it is equal to the difference between predicted and actual values of the dependent variable).

Both inputs must be sequences of the same length (no less than two), and the independent variable _x_ cannot be constant; otherwise a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 is raised.

For example, we can use the [release dates of the Monty Python films](https://en.wikipedia.org/wiki/Monty_Python#Films)
 to predict the cumulative number of Monty Python films that would have been produced by 2019 assuming that they had kept the pace.

Copy

\>>> year \= \[1971, 1975, 1979, 1982, 1983\]
\>>> films\_total \= \[1, 2, 3, 4, 5\]
\>>> slope, intercept \= linear\_regression(year, films\_total)
\>>> round(slope \* 2019 + intercept)
16

If _proportional_ is true, the independent variable _x_ and the dependent variable _y_ are assumed to be directly proportional. The data is fit to a line passing through the origin. Since the _intercept_ will always be 0.0, the underlying linear function simplifies to:

> _y = slope \* x + noise_

Continuing the example from [`correlation()`](https://docs.python.org/3/library/statistics.html#statistics.correlation "statistics.correlation")
, we look to see how well a model based on major planets can predict the orbital distances for dwarf planets:

Copy

\>>> model \= linear\_regression(period\_squared, dist\_cubed, proportional\=True)
\>>> slope \= model.slope

\>>> \# Dwarf planets:   Pluto,  Eris,    Makemake, Haumea, Ceres
\>>> orbital\_periods \= \[90\_560, 204\_199, 111\_845, 103\_410, 1\_680\]  \# days
\>>> predicted\_dist \= \[math.cbrt(slope \* (p \* p)) for p in orbital\_periods\]
\>>> list(map(round, predicted\_dist))
\[5912, 10166, 6806, 6459, 414\]

\>>> \[5\_906, 10\_152, 6\_796, 6\_450, 414\]  \# actual distance in million km
\[5906, 10152, 6796, 6450, 414\]

Added in version 3.10.

Changed in version 3.11: Added support for _proportional_.

Exceptions[¶](https://docs.python.org/3/library/statistics.html#exceptions "Link to this heading")

---------------------------------------------------------------------------------------------------

A single exception is defined:

exception statistics.StatisticsError[¶](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "Link to this definition")

Subclass of [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 for statistics-related exceptions.

[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist")
 objects[¶](https://docs.python.org/3/library/statistics.html#normaldist-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist")
 is a tool for creating and manipulating normal distributions of a [random variable](http://www.stat.yale.edu/Courses/1997-98/101/ranvar.htm)
. It is a class that treats the mean and standard deviation of data measurements as a single entity.

Normal distributions arise from the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
 and have a wide range of applications in statistics.

class statistics.NormalDist(_mu\=0.0_, _sigma\=1.0_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "Link to this definition")

Returns a new _NormalDist_ object where _mu_ represents the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean)
 and _sigma_ represents the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)
.

If _sigma_ is negative, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
.

mean[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mean "Link to this definition")

A read-only property for the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean)
 of a normal distribution.

median[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.median "Link to this definition")

A read-only property for the [median](https://en.wikipedia.org/wiki/Median)
 of a normal distribution.

mode[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mode "Link to this definition")

A read-only property for the [mode](https://en.wikipedia.org/wiki/Mode_(statistics))
 of a normal distribution.

stdev[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.stdev "Link to this definition")

A read-only property for the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)
 of a normal distribution.

variance[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.variance "Link to this definition")

A read-only property for the [variance](https://en.wikipedia.org/wiki/Variance)
 of a normal distribution. Equal to the square of the standard deviation.

classmethod from\_samples(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.from_samples "Link to this definition")

Makes a normal distribution instance with _mu_ and _sigma_ parameters estimated from the _data_ using [`fmean()`](https://docs.python.org/3/library/statistics.html#statistics.fmean "statistics.fmean")
 and [`stdev()`](https://docs.python.org/3/library/statistics.html#statistics.stdev "statistics.stdev")
.

The _data_ can be any [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 and should consist of values that can be converted to type [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
. If _data_ does not contain at least two elements, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError")
 because it takes at least one point to estimate a central value and at least two points to estimate dispersion.

samples(_n_, _\*_, _seed\=None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.samples "Link to this definition")

Generates _n_ random samples for a given mean and standard deviation. Returns a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 of [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 values.

If _seed_ is given, creates a new instance of the underlying random number generator. This is useful for creating reproducible results, even in a multi-threading context.

Changed in version 3.13.

Switched to a faster algorithm. To reproduce samples from previous versions, use [`random.seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed")
 and [`random.gauss()`](https://docs.python.org/3/library/random.html#random.gauss "random.gauss")
.

pdf(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.pdf "Link to this definition")

Using a [probability density function (pdf)](https://en.wikipedia.org/wiki/Probability_density_function)
, compute the relative likelihood that a random variable _X_ will be near the given value _x_. Mathematically, it is the limit of the ratio `P(x <= X < x+dx) / dx` as _dx_ approaches zero.

The relative likelihood is computed as the probability of a sample occurring in a narrow range divided by the width of the range (hence the word “density”). Since the likelihood is relative to other points, its value can be greater than `1.0`.

cdf(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.cdf "Link to this definition")

Using a [cumulative distribution function (cdf)](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
, compute the probability that a random variable _X_ will be less than or equal to _x_. Mathematically, it is written `P(X <= x)`.

inv\_cdf(_p_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.inv_cdf "Link to this definition")

Compute the inverse cumulative distribution function, also known as the [quantile function](https://en.wikipedia.org/wiki/Quantile_function)
 or the [percent-point](https://web.archive.org/web/20190203145224/https://www.statisticshowto.datasciencecentral.com/inverse-distribution-function/)
 function. Mathematically, it is written `x : P(X <= x) = p`.

Finds the value _x_ of the random variable _X_ such that the probability of the variable being less than or equal to that value equals the given probability _p_.

overlap(_other_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.overlap "Link to this definition")

Measures the agreement between two normal probability distributions. Returns a value between 0.0 and 1.0 giving [the overlapping area for the two probability density functions](https://www.rasch.org/rmt/rmt101r.htm)
.

quantiles(_n\=4_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.quantiles "Link to this definition")

Divide the normal distribution into _n_ continuous intervals with equal probability. Returns a list of (n - 1) cut points separating the intervals.

Set _n_ to 4 for quartiles (the default). Set _n_ to 10 for deciles. Set _n_ to 100 for percentiles which gives the 99 cuts points that separate the normal distribution into 100 equal sized groups.

zscore(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.zscore "Link to this definition")

Compute the [Standard Score](https://www.statisticshowto.com/probability-and-statistics/z-score/)
 describing _x_ in terms of the number of standard deviations above or below the mean of the normal distribution: `(x - mean) / stdev`.

Added in version 3.9.

Instances of `NormalDist` support addition, subtraction, multiplication and division by a constant. These operations are used for translation and scaling. For example:

Copy

\>>> temperature\_february \= NormalDist(5, 2.5)             \# Celsius
\>>> temperature\_february \* (9/5) + 32                     \# Fahrenheit
NormalDist(mu=41.0, sigma=4.5)

Dividing a constant by an instance of `NormalDist` is not supported because the result wouldn’t be normally distributed.

Since normal distributions arise from additive effects of independent variables, it is possible to [add and subtract two independent normally distributed random variables](https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables)
 represented as instances of `NormalDist`. For example:

Copy

\>>> birth\_weights \= NormalDist.from\_samples(\[2.5, 3.1, 2.1, 2.4, 2.7, 3.5\])
\>>> drug\_effects \= NormalDist(0.4, 0.15)
\>>> combined \= birth\_weights + drug\_effects
\>>> round(combined.mean, 1)
3.1
\>>> round(combined.stdev, 1)
0.5

Added in version 3.8.

Examples and Recipes[¶](https://docs.python.org/3/library/statistics.html#examples-and-recipes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

### Classic probability problems[¶](https://docs.python.org/3/library/statistics.html#classic-probability-problems "Link to this heading")

[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist")
 readily solves classic probability problems.

For example, given [historical data for SAT exams](https://nces.ed.gov/programs/digest/d17/tables/dt17_226.40.asp)
 showing that scores are normally distributed with a mean of 1060 and a standard deviation of 195, determine the percentage of students with test scores between 1100 and 1200, after rounding to the nearest whole number:

Copy

\>>> sat \= NormalDist(1060, 195)
\>>> fraction \= sat.cdf(1200 + 0.5) \- sat.cdf(1100 \- 0.5)
\>>> round(fraction \* 100.0, 1)
18.4

Find the [quartiles](https://en.wikipedia.org/wiki/Quartile)
 and [deciles](https://en.wikipedia.org/wiki/Decile)
 for the SAT scores:

Copy

\>>> list(map(round, sat.quantiles()))
\[928, 1060, 1192\]
\>>> list(map(round, sat.quantiles(n\=10)))
\[810, 896, 958, 1011, 1060, 1109, 1162, 1224, 1310\]

### Monte Carlo inputs for simulations[¶](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations "Link to this heading")

To estimate the distribution for a model that isn’t easy to solve analytically, [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist")
 can generate input samples for a [Monte Carlo simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method)
:

Copy

\>>> def model(x, y, z):
...     return (3\*x + 7\*x\*y \- 5\*y) / (11 \* z)
...
\>>> n \= 100\_000
\>>> X \= NormalDist(10, 2.5).samples(n, seed\=3652260728)
\>>> Y \= NormalDist(15, 1.75).samples(n, seed\=4582495471)
\>>> Z \= NormalDist(50, 1.25).samples(n, seed\=6582483453)
\>>> quantiles(map(model, X, Y, Z))
\[1.4591308524824727, 1.8035946855390597, 2.175091447274739\]

### Approximating binomial distributions[¶](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions "Link to this heading")

Normal distributions can be used to approximate [Binomial distributions](https://mathworld.wolfram.com/BinomialDistribution.html)
 when the sample size is large and when the probability of a successful trial is near 50%.

For example, an open source conference has 750 attendees and two rooms with a 500 person capacity. There is a talk about Python and another about Ruby. In previous conferences, 65% of the attendees preferred to listen to Python talks. Assuming the population preferences haven’t changed, what is the probability that the Python room will stay within its capacity limits?

Copy

\>>> n \= 750             \# Sample size
\>>> p \= 0.65            \# Preference for Python
\>>> q \= 1.0 \- p         \# Preference for Ruby
\>>> k \= 500             \# Room capacity

\>>> \# Approximation using the cumulative normal distribution
\>>> from math import sqrt
\>>> round(NormalDist(mu\=n\*p, sigma\=sqrt(n\*p\*q)).cdf(k + 0.5), 4)
0.8402

\>>> \# Exact solution using the cumulative binomial distribution
\>>> from math import comb, fsum
\>>> round(fsum(comb(n, r) \* p\*\*r \* q\*\*(n\-r) for r in range(k+1)), 4)
0.8402

\>>> \# Approximation using a simulation
\>>> from random import seed, binomialvariate
\>>> seed(8675309)
\>>> mean(binomialvariate(n, p) <= k for i in range(10\_000))
0.8406

### Naive bayesian classifier[¶](https://docs.python.org/3/library/statistics.html#naive-bayesian-classifier "Link to this heading")

Normal distributions commonly arise in machine learning problems.

Wikipedia has a [nice example of a Naive Bayesian Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Person_classification)
. The challenge is to predict a person’s gender from measurements of normally distributed features including height, weight, and foot size.

We’re given a training dataset with measurements for eight people. The measurements are assumed to be normally distributed, so we summarize the data with [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist")
:

Copy

\>>> height\_male \= NormalDist.from\_samples(\[6, 5.92, 5.58, 5.92\])
\>>> height\_female \= NormalDist.from\_samples(\[5, 5.5, 5.42, 5.75\])
\>>> weight\_male \= NormalDist.from\_samples(\[180, 190, 170, 165\])
\>>> weight\_female \= NormalDist.from\_samples(\[100, 150, 130, 150\])
\>>> foot\_size\_male \= NormalDist.from\_samples(\[12, 11, 12, 10\])
\>>> foot\_size\_female \= NormalDist.from\_samples(\[6, 8, 7, 9\])

Next, we encounter a new person whose feature measurements are known but whose gender is unknown:

Copy

\>>> ht \= 6.0        \# height
\>>> wt \= 130        \# weight
\>>> fs \= 8          \# foot size

Starting with a 50% [prior probability](https://en.wikipedia.org/wiki/Prior_probability)
 of being male or female, we compute the posterior as the prior times the product of likelihoods for the feature measurements given the gender:

Copy

\>>> prior\_male \= 0.5
\>>> prior\_female \= 0.5
\>>> posterior\_male \= (prior\_male \* height\_male.pdf(ht) \*
...                   weight\_male.pdf(wt) \* foot\_size\_male.pdf(fs))

\>>> posterior\_female \= (prior\_female \* height\_female.pdf(ht) \*
...                     weight\_female.pdf(wt) \* foot\_size\_female.pdf(fs))

The final prediction goes to the largest posterior. This is known as the [maximum a posteriori](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)
 or MAP:

Copy

\>>> 'male' if posterior\_male \> posterior\_female else 'female'
'female'

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html#)
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

[`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html "previous chapter")

#### Next topic

[Functional Programming Modules](https://docs.python.org/3/library/functional.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=statistics+%E2%80%94+Mathematical+statistics+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstatistics.html&pagesource=library%2Fstatistics.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/statistics.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/functional.html "Functional Programming Modules")
     |
*   [previous](https://docs.python.org/3/library/random.html "random — Generate pseudo-random numbers")
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
*   [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
    
*    
    
    |
*   Theme Auto Light Dark |