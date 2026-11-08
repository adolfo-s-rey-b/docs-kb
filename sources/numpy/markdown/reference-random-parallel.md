[Skip to main content](https://numpy.org/doc/stable/reference/random/parallel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/parallel.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/parallel.html)
[2.4](https://numpy.org/doc/2.4/reference/random/parallel.html)
[2.3](https://numpy.org/doc/2.3/reference/random/parallel.html)
[2.2](https://numpy.org/doc/2.2/reference/random/parallel.html)
[2.1](https://numpy.org/doc/2.1/reference/random/parallel.html)
[2.0](https://numpy.org/doc/2.0/reference/random/parallel.html)
[1.26](https://numpy.org/doc/1.26/reference/random/parallel.html)
[1.25](https://numpy.org/doc/1.25/reference/random/parallel.html)
[1.24](https://numpy.org/doc/1.24/reference/random/parallel.html)
[1.23](https://numpy.org/doc/1.23/reference/random/parallel.html)
[1.22](https://numpy.org/doc/1.22/reference/random/parallel.html)
[1.21](https://numpy.org/doc/1.21/reference/random/parallel.html)
[1.20](https://numpy.org/doc/1.20/reference/random/parallel.html)
[1.19](https://numpy.org/doc/1.19/reference/random/parallel.html)
[1.18](https://numpy.org/doc/1.18/reference/random/parallel.html)
[1.17](https://numpy.org/doc/1.17/reference/random/parallel.html)
[1.16](https://numpy.org/doc/1.16/reference/random/parallel.html)
[1.15](https://numpy.org/doc/1.15/reference/random/parallel.html)
[1.14](https://numpy.org/doc/1.14/reference/random/parallel.html)
[1.13](https://numpy.org/doc/1.13/reference/random/parallel.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Parallel random number generation[#](https://numpy.org/doc/stable/reference/random/parallel.html#parallel-random-number-generation "Link to this heading")

===========================================================================================================================================================

There are four main strategies implemented that can be used to produce repeatable pseudo-random numbers across multiple processes (local or distributed).

[`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 spawning[#](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy allows you to spawn new (with very high probability) independent [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 and [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instances via their `spawn()` method. This spawning is implemented by the [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 used for initializing the bit generators random stream.

[`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 [implements an algorithm](https://www.pcg-random.org/posts/developing-a-seed_seq-alternative.html)
 to process a user-provided seed, typically as an integer of some size, and to convert it into an initial state for a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. It uses hashing techniques to ensure that low-quality seeds are turned into high quality initial states (at least, with very high probability).

For example, [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 has a state consisting of 624 `uint32` integers. A naive way to take a 32-bit integer seed would be to just set the last element of the state to the 32-bit seed and leave the rest 0s. This is a valid state for [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
, but not a good one. The Mersenne Twister algorithm [suffers if there are too many 0s](http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/MT2002/emt19937ar.html)
. Similarly, two adjacent 32-bit integer seeds (i.e. `12345` and `12346`) would produce very similar streams.

[`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 avoids these problems by using successions of integer hashes with good [avalanche properties](https://en.wikipedia.org/wiki/Avalanche_effect)
 to ensure that flipping any bit in the input has about a 50% chance of flipping any bit in the output. Two input seeds that are very close to each other will produce initial states that are very far from each other (with very high probability). It is also constructed in such a way that you can provide arbitrary-sized integers or lists of integers. [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 will take all of the bits that you provide and mix them together to produce however many bits the consuming [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 needs to initialize itself.

These properties together mean that we can safely mix together the usual user-provided seed with simple incrementing counters to get [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 states that are (to very high probability) independent of each other. We can wrap this together into an API that is easy to use and difficult to misuse. Note that while [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 attempts to solve many of the issues related to user-provided small seeds, we still [recommend](https://numpy.org/doc/stable/reference/random/index.html#recommend-secrets-randbits)
 using [`secrets.randbits`](https://docs.python.org/3/library/secrets.html#secrets.randbits "(in Python v3.14)")
 to generate seeds with 128 bits of entropy to avoid the remaining biases introduced by human-chosen seeds.

from numpy.random import SeedSequence, default\_rng

ss \= SeedSequence(12345)

\# Spawn off 10 child SeedSequences to pass to child processes.
child\_seeds \= ss.spawn(10)
streams \= \[default\_rng(s) for s in child\_seeds\]

Copy to clipboard

For convenience the direct use of [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 is not necessary. The above `streams` can be spawned directly from a parent generator via [`spawn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy.random.Generator.spawn "numpy.random.Generator.spawn")
:

parent\_rng \= default\_rng(12345)
streams \= parent\_rng.spawn(10)

Copy to clipboard

Child objects can also spawn to make grandchildren, and so on. Each child has a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 with its position in the tree of spawned child objects mixed in with the user-provided seed to generate independent (with very high probability) streams.

grandchildren \= streams\[0\].spawn(4)

Copy to clipboard

This feature lets you make local decisions about when and how to split up streams without coordination between processes. You do not have to preallocate space to avoid overlapping or request streams from a common global service. This general “tree-hashing” scheme is [not unique to numpy](https://www.iro.umontreal.ca/~lecuyer/myftp/papers/parallel-rng-imacs.pdf)
 but not yet widespread. Python has increasingly-flexible mechanisms for parallelization available, and this scheme fits in very well with that kind of use.

Using this scheme, an upper bound on the probability of a collision can be estimated if one knows the number of streams that you derive. [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 hashes its inputs, both the seed and the spawn-tree-path, down to a 128-bit pool by default. The probability that there is a collision in that pool, pessimistically-estimated ([\[1\]](https://numpy.org/doc/stable/reference/random/parallel.html#id3)
), will be about \\(n^2\*2^{-128}\\) where _n_ is the number of streams spawned. If a program uses an aggressive million streams, about \\(2^{20}\\), then the probability that at least one pair of them are identical is about \\(2^{-88}\\), which is in solidly-ignorable territory ([\[2\]](https://numpy.org/doc/stable/reference/random/parallel.html#id4)
).

Sequence of integer seeds[#](https://numpy.org/doc/stable/reference/random/parallel.html#sequence-of-integer-seeds "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

As discussed in the previous section, [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 can not only take an integer seed, it can also take an arbitrary-length sequence of (non-negative) integers. If one exercises a little care, one can use this feature to design _ad hoc_ schemes for getting safe parallel PRNG streams with similar safety guarantees as spawning.

For example, one common use case is that a worker process is passed one root seed integer for the whole calculation and also an integer worker ID (or something more granular like a job ID, batch ID, or something similar). If these IDs are created deterministically and uniquely, then one can derive reproducible parallel PRNG streams by combining the ID and the root seed integer in a list.

\# default\_rng() and each of the BitGenerators use SeedSequence underneath, so
\# they all accept sequences of integers as seeds the same way.
from numpy.random import default\_rng

def worker(root\_seed, worker\_id):
    rng \= default\_rng(\[worker\_id, root\_seed\])
    \# Do work ...

root\_seed \= 0x8c3c010cb4754c905776bdac5ee7501
results \= \[worker(root\_seed, worker\_id) for worker\_id in range(10)\]

Copy to clipboard

This can be used to replace a number of unsafe strategies that have been used in the past which try to combine the root seed and the ID back into a single integer seed value. For example, it is common to see users add the worker ID to the root seed, especially with the legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 code.

\# UNSAFE! Do not do this!
worker\_seed \= root\_seed + worker\_id
rng \= np.random.RandomState(worker\_seed)

Copy to clipboard

It is true that for any one run of a parallel program constructed this way, each worker will have distinct streams. However, it is quite likely that multiple invocations of the program with different seeds will get overlapping sets of worker seeds. It is not uncommon (in the author’s self-experience) to change the root seed merely by an increment or two when doing these repeat runs. If the worker seeds are also derived by small increments of the worker ID, then subsets of the workers will return identical results, causing a bias in the overall ensemble of results.

Combining the worker ID and the root seed as a list of integers eliminates this risk. Lazy seeding practices will still be fairly safe.

This scheme does require that the extra IDs be unique and deterministically created. This may require coordination between the worker processes. It is recommended to place the varying IDs _before_ the unvarying root seed. [`spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 _appends_ integers after the user-provided seed, so if you might be mixing both this _ad hoc_ mechanism and spawning, or passing your objects down to library code that might be spawning, then it is a little bit safer to prepend your worker IDs rather than append them to avoid a collision.

\# Good.
worker\_seed \= \[worker\_id, root\_seed\]

\# Less good. It will \*work\*, but it's less flexible.
worker\_seed \= \[root\_seed, worker\_id\]

Copy to clipboard

With those caveats in mind, the safety guarantees against collision are about the same as with spawning, discussed in the previous section. The algorithmic mechanisms are the same.

Independent streams[#](https://numpy.org/doc/stable/reference/random/parallel.html#independent-streams "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

[`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")
 is a counter-based RNG based which generates values by encrypting an incrementing counter using weak cryptographic primitives. The seed determines the key that is used for the encryption. Unique keys create unique, independent streams. [`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")
 lets you bypass the seeding algorithm to directly set the 128-bit key. Similar, but different, keys will still create independent streams.

import secrets
from numpy.random import Philox

\# 128-bit number as a seed
root\_seed \= secrets.getrandbits(128)
streams \= \[Philox(key\=root\_seed + stream\_id) for stream\_id in range(10)\]

Copy to clipboard

This scheme does require that you avoid reusing stream IDs. This may require coordination between the parallel processes.

Jumping the BitGenerator state[#](https://numpy.org/doc/stable/reference/random/parallel.html#jumping-the-bitgenerator-state "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

`jumped` advances the state of the BitGenerator _as-if_ a large number of random numbers have been drawn, and returns a new instance with this state. The specific number of draws varies by BitGenerator, and ranges from \\(2^{64}\\) to \\(2^{128}\\). Additionally, the _as-if_ draws also depend on the size of the default random number produced by the specific BitGenerator. The BitGenerators that support `jumped`, along with the period of the BitGenerator, the size of the jump and the bits in the default unsigned random are listed below.

| BitGenerator | Period | Jump Size | Bits per Draw |
| --- | --- | --- | --- |
| [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937") | \\(2^{19937}-1\\) | \\(2^{128}\\) | 32  |
| [`PCG64`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64") | \\(2^{128}\\) | \\(~2^{127}\\) ([\[3\]](https://numpy.org/doc/stable/reference/random/parallel.html#id8)<br>) | 64  |
| [`PCG64DXSM`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#numpy.random.PCG64DXSM "numpy.random.PCG64DXSM") | \\(2^{128}\\) | \\(~2^{127}\\) ([\[3\]](https://numpy.org/doc/stable/reference/random/parallel.html#id8)<br>) | 64  |
| [`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox") | \\(2^{256}\\) | \\(2^{128}\\) | 64  |

`jumped` can be used to produce long blocks which should be long enough to not overlap.

import secrets
from numpy.random import PCG64

seed \= secrets.getrandbits(128)
blocked\_rng \= \[\]
rng \= PCG64(seed)
for i in range(10):
    blocked\_rng.append(rng.jumped(i))

Copy to clipboard

When using `jumped`, one does have to take care not to jump to a stream that was already used. In the above example, one could not later use `blocked_rng[0].jumped()` as it would overlap with `blocked_rng[1]`. Like with the independent streams, if the main process here wants to split off 10 more streams by jumping, then it needs to start with `range(10, 20)`, otherwise it would recreate the same streams. On the other hand, if you carefully construct the streams, then you are guaranteed to have streams that do not overlap.

On this page