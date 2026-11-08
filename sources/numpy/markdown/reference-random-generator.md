[Skip to main content](https://numpy.org/doc/stable/reference/random/generator.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generator.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generator.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generator.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generator.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generator.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generator.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generator.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generator.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generator.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generator.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generator.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generator.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generator.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generator.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generator.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generator.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generator.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generator.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generator.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generator.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generator.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Random `Generator`[#](https://numpy.org/doc/stable/reference/random/generator.html#random-generator "Link to this heading")

============================================================================================================================

The [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 provides access to a wide range of distributions, and served as a replacement for [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
. The main difference between the two is that [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 relies on an additional BitGenerator to manage state and generate the random bits, which are then transformed into random values from useful distributions. The default BitGenerator used by [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 is [`PCG64`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64")
. The BitGenerator can be changed by passing an instantized BitGenerator to [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
.

numpy.random.default\_rng(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "Link to this definition")

Construct a new Generator with the default BitGenerator (PCG64).

Parameters:

**seed**{None, int, array\_like\[ints\], SeedSequence, BitGenerator, Generator, RandomState}, optional

A seed to initialize the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. If None, then fresh, unpredictable entropy will be pulled from the OS. If an `int` or `array_like[ints]` is passed, then all values must be non-negative and will be passed to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to derive the initial [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 state. One may also pass in a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 instance. Additionally, when passed a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
, it will be wrapped by [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
. If passed a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
, it will be returned unaltered. When passed a legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 instance it will be coerced to a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
.

Returns:

Generator

The initialized generator object.

Notes

If `seed` is not a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 or a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
, a new [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 is instantiated. This function does not manage a default global instance.

See [Seeding and entropy](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#seeding-and-entropy)
 for more information about seeding.

Examples

Try it in your browser!

[`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 is the recommended constructor for the random number class [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
. Here are several ways we can construct a random number generator using [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 and the [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 class.

Here we use [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 to generate a random float:

\>>> import numpy as np
\>>> rng \= np.random.default\_rng(12345)
\>>> print(rng)
Generator(PCG64)
\>>> rfloat \= rng.random()
\>>> rfloat
0.22733602246716966
\>>> type(rfloat)
<class 'float'>

Copy to clipboard

Here we use [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 to generate 3 random integers between 0 (inclusive) and 10 (exclusive):

\>>> import numpy as np
\>>> rng \= np.random.default\_rng(12345)
\>>> rints \= rng.integers(low\=0, high\=10, size\=3)
\>>> rints
array(\[6, 2, 7\])
\>>> type(rints\[0\])
<class 'numpy.int64'>

Copy to clipboard

Here we specify a seed so that we have reproducible results:

\>>> import numpy as np
\>>> rng \= np.random.default\_rng(seed\=42)
\>>> print(rng)
Generator(PCG64)
\>>> arr1 \= rng.random((3, 3))
\>>> arr1
array(\[\[0.77395605, 0.43887844, 0.85859792\],\
       \[0.69736803, 0.09417735, 0.97562235\],\
       \[0.7611397 , 0.78606431, 0.12811363\]\])

Copy to clipboard

If we exit and restart our Python interpreter, we’ll see that we generate the same random numbers again:

\>>> import numpy as np
\>>> rng \= np.random.default\_rng(seed\=42)
\>>> arr2 \= rng.random((3, 3))
\>>> arr2
array(\[\[0.77395605, 0.43887844, 0.85859792\],\
       \[0.69736803, 0.09417735, 0.97562235\],\
       \[0.7611397 , 0.78606431, 0.12811363\]\])

Copy to clipboard

Go BackOpen In Tab

_class_ numpy.random.Generator(_bit\_generator_)[#](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "Link to this definition")

Container for the BitGenerators.

[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 exposes a number of methods for generating random numbers drawn from a variety of probability distributions. In addition to the distribution-specific arguments, each method takes a keyword argument _size_ that defaults to `None`. If _size_ is `None`, then a single value is generated and returned. If _size_ is an integer, then a 1-D array filled with generated values is returned. If _size_ is a tuple, then an array with that shape is filled and returned.

The function [`numpy.random.default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 will instantiate a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 with numpy’s default [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
.

**No Compatibility Guarantee**

[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 does not provide a version compatibility guarantee. In particular, as better algorithms evolve the bit stream may change.

Parameters:

**bit\_generator**BitGenerator

BitGenerator to use as the core generator.

See also

[`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")

Recommended constructor for [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
.

Notes

The Python stdlib module [`random`](https://docs.python.org/3/library/random.html#module-random "(in Python v3.14)")
 contains pseudo-random number generator with a number of methods that are similar to the ones available in [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
. It uses Mersenne Twister, and this bit generator can be accessed using [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
. [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
, besides being NumPy-aware, has the advantage that it provides a much larger number of probability distributions to choose from.

Examples

Try it in your browser!

\>>> from numpy.random import Generator, PCG64
\>>> rng \= Generator(PCG64())
\>>> rng.standard\_normal()
\-0.203  # random

Copy to clipboard

Go BackOpen In Tab

Accessing the BitGenerator and spawning[#](https://numpy.org/doc/stable/reference/random/generator.html#accessing-the-bitgenerator-and-spawning "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`bit_generator`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.bit_generator.html#numpy.random.Generator.bit_generator "numpy.random.Generator.bit_generator") | Gets the bit generator instance used by the generator |
| [`spawn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy.random.Generator.spawn "numpy.random.Generator.spawn")<br>(n\_children) | Create new independent child generators. |

Simple random data[#](https://numpy.org/doc/stable/reference/random/generator.html#simple-random-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")<br>(low\[, high, size, dtype, endpoint\]) | Return random integers from _low_ (inclusive) to _high_ (exclusive), or if endpoint=True, _low_ (inclusive) to _high_ (inclusive). |
| [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")<br>(\[size, dtype, out\]) | Return random floats in the half-open interval \[0.0, 1.0). |\
| [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice "numpy.random.Generator.choice")<br>(a\[, size, replace, p, axis, shuffle\]) | Generates a random sample from a given array |\
| [`bytes`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.bytes.html#numpy.random.Generator.bytes "numpy.random.Generator.bytes")<br>(length) | Return random bytes. |\
\
Permutations[#](https://numpy.org/doc/stable/reference/random/generator.html#permutations "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------\
\
The methods for randomly permuting a sequence are\
\
|     |     |\
| --- | --- |\
| [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")<br>(x\[, axis\]) | Modify an array or sequence in-place by shuffling its contents. |\
| [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")<br>(x\[, axis\]) | Randomly permute a sequence, or return a permuted range. |\
| [`permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")<br>(x\[, axis, out\]) | Randomly permute _x_ along axis _axis_. |\
\
The following table summarizes the behaviors of the methods.\
\
| method | copy/in-place | axis handling |\
| --- | --- | --- |\
| shuffle | in-place | as if 1d |\
| permutation | copy | as if 1d |\
| permuted | either (use ‘out’ for in-place) | axis independent |\
\
The following subsections provide more details about the differences.\
\
### In-place vs. copy[#](https://numpy.org/doc/stable/reference/random/generator.html#in-place-vs-copy "Link to this heading")\
\
The main difference between [`Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")\
 and [`Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")\
 is that [`Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")\
 operates in-place, while [`Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")\
 returns a copy.\
\
By default, [`Generator.permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")\
 returns a copy. To operate in-place with [`Generator.permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")\
, pass the same array as the first argument _and_ as the value of the `out` parameter. For example,\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> rng \= np.random.default\_rng()\
\>>> x \= np.arange(0, 15).reshape(3, 5)\
\>>> x \
array(\[\[ 0,  1,  2,  3,  4\],\
       \[ 5,  6,  7,  8,  9\],\
       \[10, 11, 12, 13, 14\]\])\
\>>> y \= rng.permuted(x, axis\=1, out\=x)\
\>>> x \
array(\[\[ 1,  0,  2,  4,  3\],  # random\
       \[ 6,  7,  8,  9,  5\],\
       \[10, 14, 11, 13, 12\]\])\
\
Copy to clipboard\
\
Note that when `out` is given, the return value is `out`:\
\
\>>> y is x\
True\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
### Handling the `axis` parameter[#](https://numpy.org/doc/stable/reference/random/generator.html#handling-the-axis-parameter "Link to this heading")\
\
An important distinction for these methods is how they handle the `axis` parameter. Both [`Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")\
 and [`Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")\
 treat the input as a one-dimensional sequence, and the `axis` parameter determines which dimension of the input array to use as the sequence. In the case of a two-dimensional array, `axis=0` will, in effect, rearrange the rows of the array, and `axis=1` will rearrange the columns. For example\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> rng \= np.random.default\_rng()\
\>>> x \= np.arange(0, 15).reshape(3, 5)\
\>>> x\
array(\[\[ 0,  1,  2,  3,  4\],\
       \[ 5,  6,  7,  8,  9\],\
       \[10, 11, 12, 13, 14\]\])\
\>>> rng.permutation(x, axis\=1) \
array(\[\[ 1,  3,  2,  0,  4\],  # random\
       \[ 6,  8,  7,  5,  9\],\
       \[11, 13, 12, 10, 14\]\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
Note that the columns have been rearranged “in bulk”: the values within each column have not changed.\
\
The method [`Generator.permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")\
 treats the `axis` parameter similar to how [`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")\
 treats it. Each slice along the given axis is shuffled independently of the others. Compare the following example of the use of [`Generator.permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")\
 to the above example of [`Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")\
:\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> rng \= np.random.default\_rng()\
\>>> rng.permuted(x, axis\=1) \
array(\[\[ 1,  0,  2,  4,  3\],  # random\
       \[ 5,  7,  6,  9,  8\],\
       \[10, 14, 12, 13, 11\]\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
In this example, the values within each row (i.e. the values along `axis=1`) have been shuffled independently. This is not a “bulk” shuffle of the columns.\
\
### Shuffling non-NumPy sequences[#](https://numpy.org/doc/stable/reference/random/generator.html#shuffling-non-numpy-sequences "Link to this heading")\
\
[`Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")\
 works on non-NumPy sequences. That is, if it is given a sequence that is not a NumPy array, it shuffles that sequence in-place.\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> rng \= np.random.default\_rng()\
\>>> a \= \['A', 'B', 'C', 'D', 'E'\]\
\>>> rng.shuffle(a)  \# shuffle the list in-place\
\>>> a \
\['B', 'D', 'A', 'E', 'C'\]  # random\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
Distributions[#](https://numpy.org/doc/stable/reference/random/generator.html#distributions "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`beta`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html#numpy.random.Generator.beta "numpy.random.Generator.beta")<br>(a, b\[, size\]) | Draw samples from a Beta distribution. |\
| [`binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html#numpy.random.Generator.binomial "numpy.random.Generator.binomial")<br>(n, p\[, size\]) | Draw samples from a binomial distribution. |\
| [`chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.chisquare.html#numpy.random.Generator.chisquare "numpy.random.Generator.chisquare")<br>(df\[, size\]) | Draw samples from a chi-square distribution. |\
| [`dirichlet`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.dirichlet.html#numpy.random.Generator.dirichlet "numpy.random.Generator.dirichlet")<br>(alpha\[, size\]) | Draw samples from the Dirichlet distribution. |\
| [`exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html#numpy.random.Generator.exponential "numpy.random.Generator.exponential")<br>(\[scale, size\]) | Draw samples from an exponential distribution. |\
| [`f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#numpy.random.Generator.f "numpy.random.Generator.f")<br>(dfnum, dfden\[, size\]) | Draw samples from an F distribution. |\
| [`gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gamma.html#numpy.random.Generator.gamma "numpy.random.Generator.gamma")<br>(shape\[, scale, size\]) | Draw samples from a Gamma distribution. |\
| [`geometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html#numpy.random.Generator.geometric "numpy.random.Generator.geometric")<br>(p\[, size\]) | Draw samples from the geometric distribution. |\
| [`gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gumbel.html#numpy.random.Generator.gumbel "numpy.random.Generator.gumbel")<br>(\[loc, scale, size\]) | Draw samples from a Gumbel distribution. |\
| [`hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.hypergeometric.html#numpy.random.Generator.hypergeometric "numpy.random.Generator.hypergeometric")<br>(ngood, nbad, nsample\[, size\]) | Draw samples from a Hypergeometric distribution. |\
| [`laplace`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html#numpy.random.Generator.laplace "numpy.random.Generator.laplace")<br>(\[loc, scale, size\]) | Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay). |\
| [`logistic`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logistic.html#numpy.random.Generator.logistic "numpy.random.Generator.logistic")<br>(\[loc, scale, size\]) | Draw samples from a logistic distribution. |\
| [`lognormal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.lognormal.html#numpy.random.Generator.lognormal "numpy.random.Generator.lognormal")<br>(\[mean, sigma, size\]) | Draw samples from a log-normal distribution. |\
| [`logseries`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#numpy.random.Generator.logseries "numpy.random.Generator.logseries")<br>(p\[, size\]) | Draw samples from a logarithmic series distribution. |\
| [`multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#numpy.random.Generator.multinomial "numpy.random.Generator.multinomial")<br>(n, pvals\[, size\]) | Draw samples from a multinomial distribution. |\
| [`multivariate_hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_hypergeometric.html#numpy.random.Generator.multivariate_hypergeometric "numpy.random.Generator.multivariate_hypergeometric")<br>(colors, nsample) | Generate variates from a multivariate hypergeometric distribution. |\
| [`multivariate_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#numpy.random.Generator.multivariate_normal "numpy.random.Generator.multivariate_normal")<br>(mean, cov\[, size, ...\]) | Draw random samples from a multivariate normal distribution. |\
| [`negative_binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#numpy.random.Generator.negative_binomial "numpy.random.Generator.negative_binomial")<br>(n, p\[, size\]) | Draw samples from a negative binomial distribution. |\
| [`noncentral_chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_chisquare.html#numpy.random.Generator.noncentral_chisquare "numpy.random.Generator.noncentral_chisquare")<br>(df, nonc\[, size\]) | Draw samples from a noncentral chi-square distribution. |\
| [`noncentral_f`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html#numpy.random.Generator.noncentral_f "numpy.random.Generator.noncentral_f")<br>(dfnum, dfden, nonc\[, size\]) | Draw samples from the noncentral F distribution. |\
| [`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")<br>(\[loc, scale, size\]) | Draw random samples from a normal (Gaussian) distribution. |\
| [`pareto`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#numpy.random.Generator.pareto "numpy.random.Generator.pareto")<br>(a\[, size\]) | Draw samples from a Pareto II (AKA Lomax) distribution with specified shape. |\
| [`poisson`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html#numpy.random.Generator.poisson "numpy.random.Generator.poisson")<br>(\[lam, size\]) | Draw samples from a Poisson distribution. |\
| [`power`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html#numpy.random.Generator.power "numpy.random.Generator.power")<br>(a\[, size\]) | Draws samples in \[0, 1\] from a power distribution with positive exponent a - 1. |\
| [`rayleigh`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html#numpy.random.Generator.rayleigh "numpy.random.Generator.rayleigh")<br>(\[scale, size\]) | Draw samples from a Rayleigh distribution. |\
| [`standard_cauchy`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_cauchy.html#numpy.random.Generator.standard_cauchy "numpy.random.Generator.standard_cauchy")<br>(\[size\]) | Draw samples from a standard Cauchy distribution with mode = 0. |\
| [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")<br>(\[size, dtype, method, out\]) | Draw samples from the standard exponential distribution. |\
| [`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html#numpy.random.Generator.standard_gamma "numpy.random.Generator.standard_gamma")<br>(shape\[, size, dtype, out\]) | Draw samples from a standard Gamma distribution. |\
| [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")<br>(\[size, dtype, out\]) | Draw samples from a standard Normal distribution (mean=0, stdev=1). |\
| [`standard_t`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_t.html#numpy.random.Generator.standard_t "numpy.random.Generator.standard_t")<br>(df\[, size\]) | Draw samples from a standard Student's t distribution with _df_ degrees of freedom. |\
| [`triangular`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html#numpy.random.Generator.triangular "numpy.random.Generator.triangular")<br>(left, mode, right\[, size\]) | Draw samples from the triangular distribution over the interval `[left, right]`. |\
| [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")<br>(\[low, high, size\]) | Draw samples from a uniform distribution. |\
| [`vonmises`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html#numpy.random.Generator.vonmises "numpy.random.Generator.vonmises")<br>(mu, kappa\[, size\]) | Draw samples from a von Mises distribution. |\
| [`wald`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html#numpy.random.Generator.wald "numpy.random.Generator.wald")<br>(mean, scale\[, size\]) | Draw samples from a Wald, or inverse Gaussian, distribution. |\
| [`weibull`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html#numpy.random.Generator.weibull "numpy.random.Generator.weibull")<br>(a\[, size\]) | Draw samples from a Weibull distribution. |\
| [`zipf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.zipf.html#numpy.random.Generator.zipf "numpy.random.Generator.zipf")<br>(a\[, size\]) | Draw samples from a Zipf distribution. |\
\
On this page