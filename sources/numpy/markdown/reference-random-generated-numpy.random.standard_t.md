[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.standard_t.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.standard_t.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.standard_t.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.standard_t.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.standard_t.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.standard_t.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.standard_t.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.standard_t.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.standard_t.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.standard_t.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.standard_t.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.standard_t.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.standard_t.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.standard_t.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.standard_t.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.standard_t.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.standard_t.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.standard_t.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.standard_t.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.standard_t.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.standard\_t[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#numpy-random-standard-t "Link to this heading")

=================================================================================================================================================================

random.standard\_t(_df_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#numpy.random.standard_t "Link to this definition")

Draw samples from a standard Student’s t distribution with _df_ degrees of freedom.

A special case of the hyperbolic distribution. As _df_ gets large, the result resembles that of the standard normal distribution ([`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")
).

Note

New code should use the [`standard_t`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_t.html#numpy.random.Generator.standard_t "numpy.random.Generator.standard_t")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**df**float or array\_like of floats

Degrees of freedom, must be > 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `df` is a scalar. Otherwise, `np.array(df).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized standard Student’s t distribution.

See also

[`random.Generator.standard_t`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_t.html#numpy.random.Generator.standard_t "numpy.random.Generator.standard_t")

which should be used for new code.

Notes

The probability density function for the t distribution is

The t test is based on an assumption that the data come from a Normal distribution. The t test provides a way to test whether the sample mean (that is the mean calculated from the data) is a good estimate of the true mean.

The derivation of the t-distribution was first published in 1908 by William Gosset while working for the Guinness Brewery in Dublin. Due to proprietary issues, he had to publish under a pseudonym, and so he used the name Student.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#id3)\
\]

Dalgaard, Peter, “Introductory Statistics With R”, Springer, 2002.

\[2\]

Wikipedia, “Student’s t-distribution” [https://en.wikipedia.org/wiki/Student’s\_t-distribution](https://en.wikipedia.org/wiki/Student's_t-distribution)

Examples

Try it in your browser!

From Dalgaard page 83 [\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#r755c9bae090e-1)
, suppose the daily energy intake for 11 women in kilojoules (kJ) is:

\>>> intake \= np.array(\[5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \\\
...                    7515, 8230, 8770\])

Copy to clipboard

Does their energy intake deviate systematically from the recommended value of 7725 kJ? Our null hypothesis will be the absence of deviation, and the alternate hypothesis will be the presence of an effect that could be either positive or negative, hence making our test 2-tailed.

Because we are estimating the mean and we have N=11 values in our sample, we have N-1=10 degrees of freedom. We set our significance level to 95% and compute the t statistic using the empirical mean and empirical standard deviation of our intake. We use a ddof of 1 to base the computation of our empirical standard deviation on an unbiased estimate of the variance (note: the final estimate is not unbiased due to the concave nature of the square root).

\>>> np.mean(intake)
6753.636363636364
\>>> intake.std(ddof\=1)
1142.1232221373727
\>>> t \= (np.mean(intake)\-7725)/(intake.std(ddof\=1)/np.sqrt(len(intake)))
\>>> t
\-2.8207540608310198

Copy to clipboard

We draw 1000000 samples from Student’s t distribution with the adequate degrees of freedom.

\>>> import matplotlib.pyplot as plt
\>>> s \= np.random.standard\_t(10, size\=1000000)
\>>> h \= plt.hist(s, bins\=100, density\=True)

Copy to clipboard

Does our t statistic land in one of the two critical regions found at both tails of the distribution?

\>>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
0.018318  #random < 0.05, statistic is in critical region

Copy to clipboard

The probability value for this 2-tailed test is about 1.83%, which is lower than the 5% pre-determined significance threshold.

Therefore, the probability of observing values as extreme as our intake conditionally on the null hypothesis being true is too low, and we reject the null hypothesis of no deviation.

![../../../_images/numpy-random-standard_t-1.png](https://numpy.org/doc/stable/_images/numpy-random-standard_t-1.png)

Go BackOpen In Tab

On this page