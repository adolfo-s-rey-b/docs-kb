[Skip to main content](https://numpy.org/doc/stable/reference/random/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/index.html)
[2.4](https://numpy.org/doc/2.4/reference/random/index.html)
[2.3](https://numpy.org/doc/2.3/reference/random/index.html)
[2.2](https://numpy.org/doc/2.2/reference/random/index.html)
[2.1](https://numpy.org/doc/2.1/reference/random/index.html)
[2.0](https://numpy.org/doc/2.0/reference/random/index.html)
[1.26](https://numpy.org/doc/1.26/reference/random/index.html)
[1.25](https://numpy.org/doc/1.25/reference/random/index.html)
[1.24](https://numpy.org/doc/1.24/reference/random/index.html)
[1.23](https://numpy.org/doc/1.23/reference/random/index.html)
[1.22](https://numpy.org/doc/1.22/reference/random/index.html)
[1.21](https://numpy.org/doc/1.21/reference/random/index.html)
[1.20](https://numpy.org/doc/1.20/reference/random/index.html)
[1.19](https://numpy.org/doc/1.19/reference/random/index.html)
[1.18](https://numpy.org/doc/1.18/reference/random/index.html)
[1.17](https://numpy.org/doc/1.17/reference/random/index.html)
[1.16](https://numpy.org/doc/1.16/reference/random/index.html)
[1.15](https://numpy.org/doc/1.15/reference/random/index.html)
[1.14](https://numpy.org/doc/1.14/reference/random/index.html)
[1.13](https://numpy.org/doc/1.13/reference/random/index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Random sampling[#](https://numpy.org/doc/stable/reference/random/index.html#random-sampling "Link to this heading")

====================================================================================================================

Quick start[#](https://numpy.org/doc/stable/reference/random/index.html#quick-start "Link to this heading")

------------------------------------------------------------------------------------------------------------

The [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")
 module implements pseudo-random number generators (PRNGs or RNGs, for short) with the ability to draw samples from a variety of probability distributions. In general, users will create a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance with [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 and call the various methods on it to obtain samples from different distributions.

Try it in your browser!

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()

Copy to clipboard

Generate one random float uniformly distributed over the range :

\>>> rng.random()  
0.06369197489564249  # may vary

Copy to clipboard

Generate an array of 10 numbers according to a unit Gaussian distribution:

\>>> rng.standard\_normal(10)  
array(\[-0.31018314, -1.8922078 , -0.3628523 , -0.63526532,  0.43181166,  # may vary\
        0.51640373,  1.25693945,  0.07779185,  0.84090247, -2.13406828\])

Copy to clipboard

Generate an array of 5 integers uniformly over the range \[0, 10):\
\
\>>> rng.integers(low\=0, high\=10, size\=5)  \
array(\[8, 7, 6, 2, 0\])  # may vary\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
Our RNGs are deterministic sequences and can be reproduced by specifying a seed integer to derive its initial state. By default, with no seed provided, [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")\
 will seed the RNG from nondeterministic data from the operating system and therefore generate different numbers each time. The pseudo-random sequences will be independent for all practical purposes, at least those purposes for which our pseudo-randomness was good for in the first place.\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> rng1 \= np.random.default\_rng()\
\>>> rng1.random()  \
0.6596288841243357  # may vary\
\>>> rng2 \= np.random.default\_rng()\
\>>> rng2.random()  \
0.11885628817151628  # may vary\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
Warning\
\
The pseudo-random number generators implemented in this module are designed for statistical modeling and simulation. They are not suitable for security or cryptographic purposes. See the [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "(in Python v3.14)")\
 module from the standard library for such use cases.\
\
Seeds should be large positive integers. [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")\
 can take positive integers of any size. We recommend using very large, unique numbers to ensure that your seed is different from anyone else’s. This is good practice to ensure that your results are statistically independent from theirs unless you are intentionally _trying_ to reproduce their result. A convenient way to get such a seed number is to use [`secrets.randbits`](https://docs.python.org/3/library/secrets.html#secrets.randbits "(in Python v3.14)")\
 to get an arbitrary 128-bit integer.\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> import secrets\
\>>> secrets.randbits(128)  \
122807528840384100672342137672332424406  # may vary\
\>>> rng1 \= np.random.default\_rng(122807528840384100672342137672332424406)\
\>>> rng1.random()\
0.5363922081269535\
\>>> rng2 \= np.random.default\_rng(122807528840384100672342137672332424406)\
\>>> rng2.random()\
0.5363922081269535\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
See the documentation on [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")\
 and [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")\
 for more advanced options for controlling the seed in specialized scenarios.\
\
[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 and its associated infrastructure was introduced in NumPy version 1.17.0. There is still a lot of code that uses the older [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
 and the functions in [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
. While there are no plans to remove them at this time, we do recommend transitioning to [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 as you can. The algorithms are faster, more flexible, and will receive more improvements in the future. For the most part, [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 can be used as a replacement for [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
. See [Legacy random generation](https://numpy.org/doc/stable/reference/random/legacy.html#legacy)\
 for information on the legacy infrastructure, [What’s new or different](https://numpy.org/doc/stable/reference/random/new-or-different.html#new-or-different)\
 for information on transitioning, and [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html#nep19 "(in NumPy Enhancement Proposals)")\
 for some of the reasoning for the transition.\
\
Design[#](https://numpy.org/doc/stable/reference/random/index.html#design "Link to this heading")\
\
--------------------------------------------------------------------------------------------------\
\
Users primarily interact with [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 instances. Each [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 instance owns a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")\
 instance that implements the core RNG algorithm. The [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")\
 has a limited set of responsibilities. It manages state and provides functions to produce random doubles and random unsigned 32- and 64-bit values.\
\
The [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 takes the bit generator-provided stream and transforms them into more useful distributions, e.g., simulated normal random values. This structure allows alternative bit generators to be used with little code duplication.\
\
NumPy implements several different [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")\
 classes implementing different RNG algorithms. [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")\
 currently uses [`PCG64`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64")\
 as the default [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")\
. It has better statistical properties and performance than the [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")\
 algorithm used in the legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
. See [Bit generators](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#random-bit-generators)\
 for more details on the supported BitGenerators.\
\
[`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")\
 and BitGenerators delegate the conversion of seeds into RNG states to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")\
 internally. [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")\
 implements a sophisticated algorithm that intermediates between the user’s input and the internal implementation details of each [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")\
 algorithm, each of which can require different amounts of bits for its state. Importantly, it lets you use arbitrary-sized integers and arbitrary sequences of such integers to mix together into the RNG state. This is a useful primitive for constructing a [flexible pattern for parallel RNG streams](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawn)\
.\
\
For backward compatibility, we still maintain the legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
 class. It continues to use the [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")\
 algorithm by default, and old seeds continue to reproduce the same results. The convenience [Functions in numpy.random](https://numpy.org/doc/stable/reference/random/legacy.html#functions-in-numpy-random)\
 are still aliases to the methods on a single global [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
 instance. See [Legacy random generation](https://numpy.org/doc/stable/reference/random/legacy.html#legacy)\
 for the complete details. See [What’s new or different](https://numpy.org/doc/stable/reference/random/new-or-different.html#new-or-different)\
 for a detailed comparison between [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 and [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
.\
\
### Parallel Generation[#](https://numpy.org/doc/stable/reference/random/index.html#parallel-generation "Link to this heading")\
\
The included generators can be used in parallel, distributed applications in a number of ways:\
\
*   [SeedSequence spawning](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawn)\
    \
*   [Sequence of integer seeds](https://numpy.org/doc/stable/reference/random/parallel.html#sequence-of-seeds)\
    \
*   [Independent streams](https://numpy.org/doc/stable/reference/random/parallel.html#independent-streams)\
    \
*   [Jumping the BitGenerator state](https://numpy.org/doc/stable/reference/random/parallel.html#parallel-jumped)\
    \
\
Users with a very large amount of parallelism will want to consult [Upgrading PCG64 with PCG64DXSM](https://numpy.org/doc/stable/reference/random/upgrading-pcg64.html#upgrading-pcg64)\
.\
\
Concepts[#](https://numpy.org/doc/stable/reference/random/index.html#concepts "Link to this heading")\
\
------------------------------------------------------------------------------------------------------\
\
*   [Random `Generator`](https://numpy.org/doc/stable/reference/random/generator.html)\
    \
*   [Legacy Generator (RandomState)](https://numpy.org/doc/stable/reference/random/legacy.html)\
    \
*   [Bit generators](https://numpy.org/doc/stable/reference/random/bit_generators/index.html)\
    \
*   [Seeding and entropy](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#seeding-and-entropy)\
    \
*   [Upgrading PCG64 with PCG64DXSM](https://numpy.org/doc/stable/reference/random/upgrading-pcg64.html)\
    \
*   [Compatibility policy](https://numpy.org/doc/stable/reference/random/compatibility.html)\
    \
\
Features[#](https://numpy.org/doc/stable/reference/random/index.html#features "Link to this heading")\
\
------------------------------------------------------------------------------------------------------\
\
*   [Parallel Applications](https://numpy.org/doc/stable/reference/random/parallel.html)\
    *   [`SeedSequence` spawning](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning)\
        \
    *   [Sequence of integer seeds](https://numpy.org/doc/stable/reference/random/parallel.html#sequence-of-integer-seeds)\
        \
    *   [Independent streams](https://numpy.org/doc/stable/reference/random/parallel.html#independent-streams)\
        \
    *   [Jumping the BitGenerator state](https://numpy.org/doc/stable/reference/random/parallel.html#jumping-the-bitgenerator-state)\
        \
*   [Multithreaded Generation](https://numpy.org/doc/stable/reference/random/multithreading.html)\
    \
*   [New or Different](https://numpy.org/doc/stable/reference/random/new-or-different.html)\
    \
*   [Comparing Performance](https://numpy.org/doc/stable/reference/random/performance.html)\
    *   [Recommendation](https://numpy.org/doc/stable/reference/random/performance.html#recommendation)\
        \
    *   [Timings](https://numpy.org/doc/stable/reference/random/performance.html#timings)\
        \
    *   [Performance on different operating systems](https://numpy.org/doc/stable/reference/random/performance.html#performance-on-different-operating-systems)\
        \
*   [C API](https://numpy.org/doc/stable/reference/random/c-api.html)\
    \
*   [Examples of using Numba, Cython, CFFI](https://numpy.org/doc/stable/reference/random/extending.html)\
    *   [Numba](https://numpy.org/doc/stable/reference/random/extending.html#numba)\
        \
    *   [Cython](https://numpy.org/doc/stable/reference/random/extending.html#cython)\
        \
    *   [CFFI](https://numpy.org/doc/stable/reference/random/extending.html#id2)\
        \
    *   [New BitGenerators](https://numpy.org/doc/stable/reference/random/extending.html#new-bitgenerators)\
        \
    *   [Examples](https://numpy.org/doc/stable/reference/random/extending.html#examples)\
        \
\
### Original Source of the Generator and BitGenerators[#](https://numpy.org/doc/stable/reference/random/index.html#original-source-of-the-generator-and-bitgenerators "Link to this heading")\
\
This package was developed independently of NumPy and was integrated in version 1.17.0. The original repo is at [bashtage/randomgen](https://github.com/bashtage/randomgen)\
.\
\
On this page