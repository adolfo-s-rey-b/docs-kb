[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/philox.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/philox.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/philox.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/philox.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/philox.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/philox.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/philox.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/philox.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/philox.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/philox.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/philox.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/philox.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/philox.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/philox.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/philox.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/philox.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/philox.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/philox.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/philox.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/philox.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Philox counter-based RNG[#](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#philox-counter-based-rng "Link to this heading")

======================================================================================================================================================

_class_ numpy.random.Philox(_seed\=None_, _counter\=None_, _key\=None_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "Link to this definition")

Container for the Philox (4x64) pseudo-random number generator.

Parameters:

**seed**{None, int, array\_like\[ints\], SeedSequence}, optional

A seed to initialize the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. If None, then fresh, unpredictable entropy will be pulled from the OS. If an `int` or `array_like[ints]` is passed, then it will be passed to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to derive the initial [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 state. One may also pass in a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 instance.

**counter**{None, int, array\_like}, optional

Counter to use in the Philox state. Can be either a Python int (long in 2.x) in \[0, 2\*\*256) or a 4-element uint64 array. If not provided, the RNG is initialized at 0.\
\
**key**{None, int, array\_like}, optional\
\
Key to use in the Philox state. Unlike `seed`, the value in key is directly set. Can be either a Python int in \[0, 2\*\*128) or a 2-element uint64 array. _key_ and `seed` cannot both be used.\
\
Attributes:\
\
**lock: threading.Lock**\
\
Lock instance that is shared so that the same bit git generator can be used in multiple Generators without corrupting the state. Code that generates values from a bit generator should hold the bit generator’s lock.\
\
Notes\
\
Philox is a 64-bit PRNG that uses a counter-based design based on weaker (and faster) versions of cryptographic functions [\[1\]](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#r40f8e2ad755a-1)\
. Instances using different values of the key produce independent sequences. Philox has a period of and supports arbitrary advancing and jumping the sequence in increments of 2^{128}. These features allow multiple non-overlapping sequences to be generated.\
\
[`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")\
 provides a capsule containing function pointers that produce doubles, and unsigned 32 and 64- bit integers. These are not directly consumable in Python and must be consumed by a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 or similar object that supports low-level access.\
\
**State and Seeding**\
\
The [`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")\
 state vector consists of a 256-bit value encoded as a 4-element uint64 array and a 128-bit value encoded as a 2-element uint64 array. The former is a counter which is incremented by 1 for every 4 64-bit randoms produced. The second is a key which determined the sequence produced. Using different keys produces independent sequences.\
\
The input `seed` is processed by [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")\
 to generate the key. The counter is set to 0.\
\
Alternately, one can omit the `seed` parameter and set the `key` and `counter` directly.\
\
**Parallel Features**\
\
The preferred way to use a BitGenerator in parallel applications is to use the [`SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")\
 method to obtain entropy values, and to use these to generate new BitGenerators:\
\
\>>> from numpy.random import Generator, Philox, SeedSequence\
\>>> sg \= SeedSequence(1234)\
\>>> rg \= \[Generator(Philox(s)) for s in sg.spawn(10)\]\
\
Copy to clipboard\
\
[`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")\
 can be used in parallel applications by calling the [`jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#numpy.random.Philox.jumped "numpy.random.Philox.jumped")\
 method to advance the state as-if 2^{128} random numbers have been generated. Alternatively, [`advance`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.advance.html#numpy.random.Philox.advance "numpy.random.Philox.advance")\
 can be used to advance the counter for any positive step in \[0, 2\*\*256). When using [`jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#numpy.random.Philox.jumped "numpy.random.Philox.jumped")\
, all generators should be chained to ensure that the segments come from the same sequence.\
\
\>>> from numpy.random import Generator, Philox\
\>>> bit\_generator \= Philox(1234)\
\>>> rg \= \[\]\
\>>> for \_ in range(10):\
...    rg.append(Generator(bit\_generator))\
...    bit\_generator \= bit\_generator.jumped()\
\
Copy to clipboard\
\
Alternatively, [`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")\
 can be used in parallel applications by using a sequence of distinct keys where each instance uses different key.\
\
\>>> key \= 2\*\*96 + 2\*\*33 + 2\*\*17 + 2\*\*9\
\>>> rg \= \[Generator(Philox(key\=key+i)) for i in range(10)\]\
\
Copy to clipboard\
\
**Compatibility Guarantee**\
\
[`Philox`](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#numpy.random.Philox "numpy.random.Philox")\
 makes a guarantee that a fixed `seed` will always produce the same random integer stream.\
\
References\
\
\[[1](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#id1)\
\]\
\
John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw, “Parallel Random Numbers: As Easy as 1, 2, 3,” Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC11), New York, NY: ACM, 2011.\
\
Examples\
\
Try it in your browser!\
\
\>>> from numpy.random import Generator, Philox\
\>>> rg \= Generator(Philox(1234))\
\>>> rg.standard\_normal()\
0.123  # random\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
State[#](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#state "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.state.html#numpy.random.Philox.state "numpy.random.Philox.state") | Get or set the PRNG state |\
\
Parallel generation[#](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#parallel-generation "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`advance`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.advance.html#numpy.random.Philox.advance "numpy.random.Philox.advance")<br>(delta) | Advance the underlying RNG as-if delta draws have occurred. |\
| [`jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#numpy.random.Philox.jumped "numpy.random.Philox.jumped")<br>(\[jumps\]) | Returns a new bit generator with the state jumped |\
\
Extending[#](https://numpy.org/doc/stable/reference/random/bit_generators/philox.html#extending "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.cffi.html#numpy.random.Philox.cffi "numpy.random.Philox.cffi") | CFFI interface |\
| [`ctypes`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.ctypes.html#numpy.random.Philox.ctypes "numpy.random.Philox.ctypes") | ctypes interface |\
\
On this page