[Skip to main content](https://numpy.org/doc/stable/reference/random/legacy.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/legacy.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/legacy.html)
[2.4](https://numpy.org/doc/2.4/reference/random/legacy.html)
[2.3](https://numpy.org/doc/2.3/reference/random/legacy.html)
[2.2](https://numpy.org/doc/2.2/reference/random/legacy.html)
[2.1](https://numpy.org/doc/2.1/reference/random/legacy.html)
[2.0](https://numpy.org/doc/2.0/reference/random/legacy.html)
[1.26](https://numpy.org/doc/1.26/reference/random/legacy.html)
[1.25](https://numpy.org/doc/1.25/reference/random/legacy.html)
[1.24](https://numpy.org/doc/1.24/reference/random/legacy.html)
[1.23](https://numpy.org/doc/1.23/reference/random/legacy.html)
[1.22](https://numpy.org/doc/1.22/reference/random/legacy.html)
[1.21](https://numpy.org/doc/1.21/reference/random/legacy.html)
[1.20](https://numpy.org/doc/1.20/reference/random/legacy.html)
[1.19](https://numpy.org/doc/1.19/reference/random/legacy.html)
[1.18](https://numpy.org/doc/1.18/reference/random/legacy.html)
[1.17](https://numpy.org/doc/1.17/reference/random/legacy.html)
[1.16](https://numpy.org/doc/1.16/reference/random/legacy.html)
[1.15](https://numpy.org/doc/1.15/reference/random/legacy.html)
[1.14](https://numpy.org/doc/1.14/reference/random/legacy.html)
[1.13](https://numpy.org/doc/1.13/reference/random/legacy.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Legacy random generation[#](https://numpy.org/doc/stable/reference/random/legacy.html#legacy-random-generation "Link to this heading")

=======================================================================================================================================

The [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 provides access to legacy generators. This generator is considered frozen and will have no further improvements. It is guaranteed to produce the same values as the final point release of NumPy v1.16. These all depend on Box-Muller normals or inverse CDF exponentials or gammas. This class should only be used if it is essential to have randoms that are identical to what would have been produced by previous versions of NumPy.

[`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 adds additional information to the state which is required when using Box-Muller normals since these are produced in pairs. It is important to use [`RandomState.get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.get_state.html#numpy.random.RandomState.get_state "numpy.random.RandomState.get_state")
, and not the underlying bit generators _state_, when accessing the state so that these extra values are saved.

Although we provide the [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 BitGenerator for use independent of [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
, note that its default seeding uses [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 rather than the legacy seeding algorithm. [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 will use the legacy seeding algorithm. The methods to use the legacy seeding algorithm are currently private as the main reason to use them is just to implement [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
. However, one can reset the state of [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 using the state of the [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
:

from numpy.random import MT19937
from numpy.random import RandomState

rs \= RandomState(12345)
mt19937 \= MT19937()
mt19937.state \= rs.get\_state()
rs2 \= RandomState(mt19937)

\# Same output
rs.standard\_normal()
rs2.standard\_normal()

rs.random()
rs2.random()

rs.standard\_exponential()
rs2.standard\_exponential()

Copy to clipboard

_class_ numpy.random.RandomState(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "Link to this definition")

Container for the slow Mersenne Twister pseudo-random number generator. Consider using a different BitGenerator with the Generator container instead.

[`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 and [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 expose a number of methods for generating random numbers drawn from a variety of probability distributions. In addition to the distribution-specific arguments, each method takes a keyword argument _size_ that defaults to `None`. If _size_ is `None`, then a single value is generated and returned. If _size_ is an integer, then a 1-D array filled with generated values is returned. If _size_ is a tuple, then an array with that shape is filled and returned.

**Compatibility Guarantee**

A fixed bit generator using a fixed seed and a fixed series of calls to ‘RandomState’ methods using the same parameters will always produce the same results up to roundoff error except when the values were incorrect. [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 is effectively frozen and will only receive updates that are required by changes in the internals of Numpy. More substantial changes, including algorithmic improvements, are reserved for [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
.

Parameters:

**seed**{None, int, array\_like, BitGenerator}, optional

Random seed used to initialize the pseudo-random number generator or an instantized BitGenerator. If an integer or array, used as a seed for the MT19937 BitGenerator. Values can be any integer between 0 and 2\*\*32 - 1 inclusive, an array (or other sequence) of such integers, or `None` (the default). If [`seed`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
 is `None`, then the [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 BitGenerator is initialized by reading data from `/dev/urandom` (or the Windows analogue) if available or seed from the clock otherwise.

See also

[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")

[`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")

[`numpy.random.BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")

Notes

The Python stdlib module “random” also contains a Mersenne Twister pseudo-random number generator with a number of methods that are similar to the ones available in [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
. [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
, besides being NumPy-aware, has the advantage that it provides a much larger number of probability distributions to choose from.

Seeding and state[#](https://numpy.org/doc/stable/reference/random/legacy.html#seeding-and-state "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.get_state.html#numpy.random.RandomState.get_state "numpy.random.RandomState.get_state")<br>(\[legacy\]) | Return a tuple representing the internal state of the generator. |
| [`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#numpy.random.RandomState.set_state "numpy.random.RandomState.set_state")<br>(state) | Set the internal state of the generator from a tuple. |
| [`seed`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.seed.html#numpy.random.RandomState.seed "numpy.random.RandomState.seed")<br>(\[seed\]) | Reseed a legacy MT19937 BitGenerator |

Simple random data[#](https://numpy.org/doc/stable/reference/random/legacy.html#simple-random-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#numpy.random.RandomState.rand "numpy.random.RandomState.rand")<br>(d0, d1, ..., dn) | Random values in a given shape. |
| [`randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randn.html#numpy.random.RandomState.randn "numpy.random.RandomState.randn")<br>(d0, d1, ..., dn) | Return a sample (or samples) from the "standard normal" distribution. |
| [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randint.html#numpy.random.RandomState.randint "numpy.random.RandomState.randint")<br>(low\[, high, size, dtype\]) | Return random integers from _low_ (inclusive) to _high_ (exclusive). |
| [`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_integers.html#numpy.random.RandomState.random_integers "numpy.random.RandomState.random_integers")<br>(low\[, high, size\]) | Random integers of type [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")<br> between _low_ and _high_, inclusive. |
| [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample "numpy.random.RandomState.random_sample")<br>(\[size\]) | Return random floats in the half-open interval \[0.0, 1.0). |\
| [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.choice.html#numpy.random.RandomState.choice "numpy.random.RandomState.choice")<br>(a\[, size, replace, p\]) | Generates a random sample from a given 1-D array |\
| [`bytes`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.bytes.html#numpy.random.RandomState.bytes "numpy.random.RandomState.bytes")<br>(length) | Return random bytes. |\
\
Permutations[#](https://numpy.org/doc/stable/reference/random/legacy.html#permutations "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html#numpy.random.RandomState.shuffle "numpy.random.RandomState.shuffle")<br>(x) | Modify a sequence in-place by shuffling its contents. |\
| [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html#numpy.random.RandomState.permutation "numpy.random.RandomState.permutation")<br>(x) | Randomly permute a sequence, or return a permuted range. |\
\
Distributions[#](https://numpy.org/doc/stable/reference/random/legacy.html#distributions "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`beta`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.beta.html#numpy.random.RandomState.beta "numpy.random.RandomState.beta")<br>(a, b\[, size\]) | Draw samples from a Beta distribution. |\
| [`binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.binomial.html#numpy.random.RandomState.binomial "numpy.random.RandomState.binomial")<br>(n, p\[, size\]) | Draw samples from a binomial distribution. |\
| [`chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.chisquare.html#numpy.random.RandomState.chisquare "numpy.random.RandomState.chisquare")<br>(df\[, size\]) | Draw samples from a chi-square distribution. |\
| [`dirichlet`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.dirichlet.html#numpy.random.RandomState.dirichlet "numpy.random.RandomState.dirichlet")<br>(alpha\[, size\]) | Draw samples from the Dirichlet distribution. |\
| [`exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.exponential.html#numpy.random.RandomState.exponential "numpy.random.RandomState.exponential")<br>(\[scale, size\]) | Draw samples from an exponential distribution. |\
| [`f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.f.html#numpy.random.RandomState.f "numpy.random.RandomState.f")<br>(dfnum, dfden\[, size\]) | Draw samples from an F distribution. |\
| [`gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gamma.html#numpy.random.RandomState.gamma "numpy.random.RandomState.gamma")<br>(shape\[, scale, size\]) | Draw samples from a Gamma distribution. |\
| [`geometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.geometric.html#numpy.random.RandomState.geometric "numpy.random.RandomState.geometric")<br>(p\[, size\]) | Draw samples from the geometric distribution. |\
| [`gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gumbel.html#numpy.random.RandomState.gumbel "numpy.random.RandomState.gumbel")<br>(\[loc, scale, size\]) | Draw samples from a Gumbel distribution. |\
| [`hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.hypergeometric.html#numpy.random.RandomState.hypergeometric "numpy.random.RandomState.hypergeometric")<br>(ngood, nbad, nsample\[, size\]) | Draw samples from a Hypergeometric distribution. |\
| [`laplace`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.laplace.html#numpy.random.RandomState.laplace "numpy.random.RandomState.laplace")<br>(\[loc, scale, size\]) | Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay). |\
| [`logistic`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logistic.html#numpy.random.RandomState.logistic "numpy.random.RandomState.logistic")<br>(\[loc, scale, size\]) | Draw samples from a logistic distribution. |\
| [`lognormal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.lognormal.html#numpy.random.RandomState.lognormal "numpy.random.RandomState.lognormal")<br>(\[mean, sigma, size\]) | Draw samples from a log-normal distribution. |\
| [`logseries`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logseries.html#numpy.random.RandomState.logseries "numpy.random.RandomState.logseries")<br>(p\[, size\]) | Draw samples from a logarithmic series distribution. |\
| [`multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multinomial.html#numpy.random.RandomState.multinomial "numpy.random.RandomState.multinomial")<br>(n, pvals\[, size\]) | Draw samples from a multinomial distribution. |\
| [`multivariate_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multivariate_normal.html#numpy.random.RandomState.multivariate_normal "numpy.random.RandomState.multivariate_normal")<br>(mean, cov\[, size, ...\]) | Draw random samples from a multivariate normal distribution. |\
| [`negative_binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.negative_binomial.html#numpy.random.RandomState.negative_binomial "numpy.random.RandomState.negative_binomial")<br>(n, p\[, size\]) | Draw samples from a negative binomial distribution. |\
| [`noncentral_chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.noncentral_chisquare.html#numpy.random.RandomState.noncentral_chisquare "numpy.random.RandomState.noncentral_chisquare")<br>(df, nonc\[, size\]) | Draw samples from a noncentral chi-square distribution. |\
| [`noncentral_f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.noncentral_f.html#numpy.random.RandomState.noncentral_f "numpy.random.RandomState.noncentral_f")<br>(dfnum, dfden, nonc\[, size\]) | Draw samples from the noncentral F distribution. |\
| [`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#numpy.random.RandomState.normal "numpy.random.RandomState.normal")<br>(\[loc, scale, size\]) | Draw random samples from a normal (Gaussian) distribution. |\
| [`pareto`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.pareto.html#numpy.random.RandomState.pareto "numpy.random.RandomState.pareto")<br>(a\[, size\]) | Draw samples from a Pareto II or Lomax distribution with specified shape. |\
| [`poisson`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.poisson.html#numpy.random.RandomState.poisson "numpy.random.RandomState.poisson")<br>(\[lam, size\]) | Draw samples from a Poisson distribution. |\
| [`power`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.power.html#numpy.random.RandomState.power "numpy.random.RandomState.power")<br>(a\[, size\]) | Draws samples in \[0, 1\] from a power distribution with positive exponent a - 1. |\
| [`rayleigh`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rayleigh.html#numpy.random.RandomState.rayleigh "numpy.random.RandomState.rayleigh")<br>(\[scale, size\]) | Draw samples from a Rayleigh distribution. |\
| [`standard_cauchy`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_cauchy.html#numpy.random.RandomState.standard_cauchy "numpy.random.RandomState.standard_cauchy")<br>(\[size\]) | Draw samples from a standard Cauchy distribution with mode = 0. |\
| [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html#numpy.random.RandomState.standard_exponential "numpy.random.RandomState.standard_exponential")<br>(\[size\]) | Draw samples from the standard exponential distribution. |\
| [`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_gamma.html#numpy.random.RandomState.standard_gamma "numpy.random.RandomState.standard_gamma")<br>(shape\[, size\]) | Draw samples from a standard Gamma distribution. |\
| [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_normal.html#numpy.random.RandomState.standard_normal "numpy.random.RandomState.standard_normal")<br>(\[size\]) | Draw samples from a standard Normal distribution (mean=0, stdev=1). |\
| [`standard_t`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_t.html#numpy.random.RandomState.standard_t "numpy.random.RandomState.standard_t")<br>(df\[, size\]) | Draw samples from a standard Student's t distribution with _df_ degrees of freedom. |\
| [`triangular`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.triangular.html#numpy.random.RandomState.triangular "numpy.random.RandomState.triangular")<br>(left, mode, right\[, size\]) | Draw samples from the triangular distribution over the interval `[left, right]`. |\
| [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.uniform.html#numpy.random.RandomState.uniform "numpy.random.RandomState.uniform")<br>(\[low, high, size\]) | Draw samples from a uniform distribution. |\
| [`vonmises`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.vonmises.html#numpy.random.RandomState.vonmises "numpy.random.RandomState.vonmises")<br>(mu, kappa\[, size\]) | Draw samples from a von Mises distribution. |\
| [`wald`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.wald.html#numpy.random.RandomState.wald "numpy.random.RandomState.wald")<br>(mean, scale\[, size\]) | Draw samples from a Wald, or inverse Gaussian, distribution. |\
| [`weibull`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.weibull.html#numpy.random.RandomState.weibull "numpy.random.RandomState.weibull")<br>(a\[, size\]) | Draw samples from a Weibull distribution. |\
| [`zipf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.zipf.html#numpy.random.RandomState.zipf "numpy.random.RandomState.zipf")<br>(a\[, size\]) | Draw samples from a Zipf distribution. |\
\
Functions in [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
[#](https://numpy.org/doc/stable/reference/random/legacy.html#functions-in-numpy-random "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Many of the RandomState methods above are exported as functions in [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
 This usage is discouraged, as it is implemented via a global [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
 instance which is not advised on two counts:\
\
*   It uses global state, which means results will change as the code changes\
    \
*   It uses a [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
     rather than the more modern [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
    .\
    \
\
For backward compatible legacy reasons, we will not change this.\
\
|     |     |\
| --- | --- |\
| [`beta`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html#numpy.random.beta "numpy.random.beta")<br>(a, b\[, size\]) | Draw samples from a Beta distribution. |\
| [`binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html#numpy.random.binomial "numpy.random.binomial")<br>(n, p\[, size\]) | Draw samples from a binomial distribution. |\
| [`bytes`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.bytes.html#numpy.random.bytes "numpy.random.bytes")<br>(length) | Return random bytes. |\
| [`chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html#numpy.random.chisquare "numpy.random.chisquare")<br>(df\[, size\]) | Draw samples from a chi-square distribution. |\
| [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html#numpy.random.choice "numpy.random.choice")<br>(a\[, size, replace, p\]) | Generates a random sample from a given 1-D array |\
| [`dirichlet`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.dirichlet.html#numpy.random.dirichlet "numpy.random.dirichlet")<br>(alpha\[, size\]) | Draw samples from the Dirichlet distribution. |\
| [`exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#numpy.random.exponential "numpy.random.exponential")<br>(\[scale, size\]) | Draw samples from an exponential distribution. |\
| [`f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.f.html#numpy.random.f "numpy.random.f")<br>(dfnum, dfden\[, size\]) | Draw samples from an F distribution. |\
| [`gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gamma.html#numpy.random.gamma "numpy.random.gamma")<br>(shape\[, scale, size\]) | Draw samples from a Gamma distribution. |\
| [`geometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.geometric.html#numpy.random.geometric "numpy.random.geometric")<br>(p\[, size\]) | Draw samples from the geometric distribution. |\
| [`get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html#numpy.random.get_state "numpy.random.get_state")<br>(\[legacy\]) | Return a tuple representing the internal state of the generator. |\
| [`gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gumbel.html#numpy.random.gumbel "numpy.random.gumbel")<br>(\[loc, scale, size\]) | Draw samples from a Gumbel distribution. |\
| [`hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.hypergeometric.html#numpy.random.hypergeometric "numpy.random.hypergeometric")<br>(ngood, nbad, nsample\[, size\]) | Draw samples from a Hypergeometric distribution. |\
| [`laplace`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html#numpy.random.laplace "numpy.random.laplace")<br>(\[loc, scale, size\]) | Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay). |\
| [`logistic`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.logistic.html#numpy.random.logistic "numpy.random.logistic")<br>(\[loc, scale, size\]) | Draw samples from a logistic distribution. |\
| [`lognormal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html#numpy.random.lognormal "numpy.random.lognormal")<br>(\[mean, sigma, size\]) | Draw samples from a log-normal distribution. |\
| [`logseries`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.logseries.html#numpy.random.logseries "numpy.random.logseries")<br>(p\[, size\]) | Draw samples from a logarithmic series distribution. |\
| [`multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multinomial.html#numpy.random.multinomial "numpy.random.multinomial")<br>(n, pvals\[, size\]) | Draw samples from a multinomial distribution. |\
| [`multivariate_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html#numpy.random.multivariate_normal "numpy.random.multivariate_normal")<br>(mean, cov\[, size, ...\]) | Draw random samples from a multivariate normal distribution. |\
| [`negative_binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.negative_binomial.html#numpy.random.negative_binomial "numpy.random.negative_binomial")<br>(n, p\[, size\]) | Draw samples from a negative binomial distribution. |\
| [`noncentral_chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html#numpy.random.noncentral_chisquare "numpy.random.noncentral_chisquare")<br>(df, nonc\[, size\]) | Draw samples from a noncentral chi-square distribution. |\
| [`noncentral_f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_f.html#numpy.random.noncentral_f "numpy.random.noncentral_f")<br>(dfnum, dfden, nonc\[, size\]) | Draw samples from the noncentral F distribution. |\
| [`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")<br>(\[loc, scale, size\]) | Draw random samples from a normal (Gaussian) distribution. |\
| [`pareto`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#numpy.random.pareto "numpy.random.pareto")<br>(a\[, size\]) | Draw samples from a Pareto II or Lomax distribution with specified shape. |\
| [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html#numpy.random.permutation "numpy.random.permutation")<br>(x) | Randomly permute a sequence, or return a permuted range. |\
| [`poisson`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html#numpy.random.poisson "numpy.random.poisson")<br>(\[lam, size\]) | Draw samples from a Poisson distribution. |\
| [`power`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.power.html#numpy.random.power "numpy.random.power")<br>(a\[, size\]) | Draws samples in \[0, 1\] from a power distribution with positive exponent a - 1. |\
| [`rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")<br>(d0, d1, ..., dn) | Random values in a given shape. |\
| [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")<br>(low\[, high, size, dtype\]) | Return random integers from _low_ (inclusive) to _high_ (exclusive). |\
| [`randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")<br>(d0, d1, ..., dn) | Return a sample (or samples) from the "standard normal" distribution. |\
| [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")<br>(\[size\]) | Return random floats in the half-open interval \[0.0, 1.0). |\
| [`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers")<br>(low\[, high, size\]) | Random integers of type [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")<br> between _low_ and _high_, inclusive. |\
| [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")<br>(\[size\]) | Return random floats in the half-open interval \[0.0, 1.0). |\
| [`ranf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.ranf.html#numpy.random.ranf "numpy.random.ranf")<br>(\*args, \*\*kwargs) | This is an alias of [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")<br>. |\
| [`rayleigh`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rayleigh.html#numpy.random.rayleigh "numpy.random.rayleigh")<br>(\[scale, size\]) | Draw samples from a Rayleigh distribution. |\
| [`sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.sample.html#numpy.random.sample "numpy.random.sample")<br>(\*args, \*\*kwargs) | This is an alias of [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")<br>. |\
| [`seed`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")<br>(\[seed\]) | Reseed the singleton RandomState instance. |\
| [`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.set_state.html#numpy.random.set_state "numpy.random.set_state")<br>(state) | Set the internal state of the generator from a tuple. |\
| [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#numpy.random.shuffle "numpy.random.shuffle")<br>(x) | Modify a sequence in-place by shuffling its contents. |\
| [`standard_cauchy`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html#numpy.random.standard_cauchy "numpy.random.standard_cauchy")<br>(\[size\]) | Draw samples from a standard Cauchy distribution with mode = 0. |\
| [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_exponential.html#numpy.random.standard_exponential "numpy.random.standard_exponential")<br>(\[size\]) | Draw samples from the standard exponential distribution. |\
| [`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_gamma.html#numpy.random.standard_gamma "numpy.random.standard_gamma")<br>(shape\[, size\]) | Draw samples from a standard Gamma distribution. |\
| [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")<br>(\[size\]) | Draw samples from a standard Normal distribution (mean=0, stdev=1). |\
| [`standard_t`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html#numpy.random.standard_t "numpy.random.standard_t")<br>(df\[, size\]) | Draw samples from a standard Student's t distribution with _df_ degrees of freedom. |\
| [`triangular`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.triangular.html#numpy.random.triangular "numpy.random.triangular")<br>(left, mode, right\[, size\]) | Draw samples from the triangular distribution over the interval `[left, right]`. |\
| [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")<br>(\[low, high, size\]) | Draw samples from a uniform distribution. |\
| [`vonmises`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.vonmises.html#numpy.random.vonmises "numpy.random.vonmises")<br>(mu, kappa\[, size\]) | Draw samples from a von Mises distribution. |\
| [`wald`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.wald.html#numpy.random.wald "numpy.random.wald")<br>(mean, scale\[, size\]) | Draw samples from a Wald, or inverse Gaussian, distribution. |\
| [`weibull`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.weibull.html#numpy.random.weibull "numpy.random.weibull")<br>(a\[, size\]) | Draw samples from a Weibull distribution. |\
| [`zipf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.zipf.html#numpy.random.zipf "numpy.random.zipf")<br>(a\[, size\]) | Draw samples from a Zipf distribution. |\
\
On this page