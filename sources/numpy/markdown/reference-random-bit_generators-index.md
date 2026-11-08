[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/index.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/index.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/index.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/index.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/index.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/index.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/index.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/index.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/index.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/index.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/index.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/index.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/index.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/index.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/index.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/index.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/index.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/index.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/index.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Bit generators[#](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#bit-generators "Link to this heading")

=================================================================================================================================

The random values produced by [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 originate in a BitGenerator. The BitGenerators do not directly provide random numbers and only contains methods used for seeding, getting or setting the state, jumping or advancing the state, and for accessing low-level wrappers for consumption by code that can efficiently access the functions provided, e.g., [numba](https://numba.pydata.org/)
.

Supported BitGenerators[#](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#supported-bitgenerators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The included BitGenerators are:

*   PCG-64 - The default. A fast generator that can be advanced by an arbitrary amount. See the documentation for [`advance`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.advance.html#numpy.random.PCG64.advance "numpy.random.PCG64.advance")
    . PCG-64 has a period of . See the [PCG author’s page](https://www.pcg-random.org/)
     for more details about this class of PRNG.
    
*   PCG-64 DXSM - An upgraded version of PCG-64 with better statistical properties in parallel contexts. See [Upgrading PCG64 with PCG64DXSM](https://numpy.org/doc/stable/reference/random/upgrading-pcg64.html#upgrading-pcg64)
     for more information on these improvements.
    
*   MT19937 - The standard Python BitGenerator. Adds a [`MT19937.jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#numpy.random.MT19937.jumped "numpy.random.MT19937.jumped")
     function that returns a new generator with state as-if 2^{128} draws have been made.
    
*   Philox - A counter-based generator capable of being advanced an arbitrary number of steps or generating independent streams. See the [Random123](https://www.deshawresearch.com/resources_random123.html)
     page for more details about this class of bit generators.
    
*   SFC64 - A fast generator based on random invertible mappings. Usually the fastest generator of the four. See the [SFC author’s page](https://pracrand.sourceforge.net/RNG_engines.txt)
     for (a little) more detail.
    

|     |     |
| --- | --- |
| [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")<br>(\[seed\]) | Base Class for generic BitGenerators, which provide a stream of random bits based on different algorithms. |

*   [MT19937](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html)
    
*   [PCG64](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html)
    
*   [PCG64DXSM](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html)
    
*   [Philox](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html)
    
*   [SFC64](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html)
    

Seeding and entropy[#](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#seeding-and-entropy "Link to this heading")

===========================================================================================================================================

A BitGenerator provides a stream of random values. In order to generate reproducible streams, BitGenerators support setting their initial state via a seed. All of the provided BitGenerators will take an arbitrary-sized non-negative integer, or a list of such integers, as a seed. BitGenerators need to take those inputs and process them into a high-quality internal state for the BitGenerator. All of the BitGenerators in numpy delegate that task to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
, which uses hashing techniques to ensure that even low-quality seeds generate high-quality initial states.

from numpy.random import PCG64

bg \= PCG64(12345678903141592653589793)

Copy to clipboard

[`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 is designed to be convenient for implementing best practices. We recommend that a stochastic program defaults to using entropy from the OS so that each run is different. The program should print out or log that entropy. In order to reproduce a past value, the program should allow the user to provide that value through some mechanism, a command-line argument is common, so that the user can then re-enter that entropy to reproduce the result. [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 can take care of everything except for communicating with the user, which is up to you.

from numpy.random import PCG64, SeedSequence

\# Get the user's seed somehow, maybe through \`argparse\`.
\# If the user did not provide a seed, it should return \`None\`.
seed \= get\_user\_seed()
ss \= SeedSequence(seed)
print(f'seed = {ss.entropy}')
bg \= PCG64(ss)

Copy to clipboard

We default to using a 128-bit integer using entropy gathered from the OS. This is a good amount of entropy to initialize all of the generators that we have in numpy. We do not recommend using small seeds below 32 bits for general use. Using just a small set of seeds to instantiate larger state spaces means that there are some initial states that are impossible to reach. This creates some biases if everyone uses such values.

There will not be anything _wrong_ with the results, per se; even a seed of 0 is perfectly fine thanks to the processing that [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 does. If you just need _some_ fixed value for unit tests or debugging, feel free to use whatever seed you like. But if you want to make inferences from the results or publish them, drawing from a larger set of seeds is good practice.

If you need to generate a good seed “offline”, then `SeedSequence().entropy` or using `secrets.randbits(128)` from the standard library are both convenient ways.

If you need to run several stochastic simulations in parallel, best practice is to construct a random generator instance for each simulation. To make sure that the random streams have distinct initial states, you can use the _spawn_ method of [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
. For instance, here we construct a list of 12 instances:

from numpy.random import PCG64, SeedSequence

\# High quality initial entropy
entropy \= 0x87351080e25cb0fad77a44a3be03b491
base\_seq \= SeedSequence(entropy)
child\_seqs \= base\_seq.spawn(12)    \# a list of 12 SeedSequences
generators \= \[PCG64(seq) for seq in child\_seqs\]

Copy to clipboard

If you already have an initial random generator instance, you can shorten the above by using the [`spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#numpy.random.BitGenerator.spawn "numpy.random.BitGenerator.spawn")
 method:

from numpy.random import PCG64, SeedSequence
\# High quality initial entropy
entropy \= 0x87351080e25cb0fad77a44a3be03b491
base\_bitgen \= PCG64(entropy)
generators \= base\_bitgen.spawn(12)

Copy to clipboard

An alternative way is to use the fact that a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 can be initialized by a tuple of elements. Here we use a base entropy value and an integer `worker_id`

from numpy.random import PCG64, SeedSequence

\# High quality initial entropy
entropy \= 0x87351080e25cb0fad77a44a3be03b491
sequences \= \[SeedSequence((entropy, worker\_id)) for worker\_id in range(12)\]
generators \= \[PCG64(seq) for seq in sequences\]

Copy to clipboard

Note that the sequences produced by the latter method will be distinct from those constructed via [`spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
.

|     |     |
| --- | --- |
| [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")<br>(\[entropy, spawn\_key, ...\]) | SeedSequence mixes sources of entropy in a reproducible way to set the initial state for independent and very probably non-overlapping BitGenerators. |

On this page