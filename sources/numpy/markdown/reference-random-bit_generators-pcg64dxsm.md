[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/pcg64dxsm.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/pcg64dxsm.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/pcg64dxsm.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/pcg64dxsm.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/pcg64dxsm.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/pcg64dxsm.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/pcg64dxsm.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/pcg64dxsm.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/pcg64dxsm.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/pcg64dxsm.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/pcg64dxsm.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/pcg64dxsm.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/pcg64dxsm.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/pcg64dxsm.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/pcg64dxsm.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/pcg64dxsm.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/pcg64dxsm.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/pcg64dxsm.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/pcg64dxsm.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/pcg64dxsm.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Permuted congruential generator (64-bit, PCG64 DXSM)[#](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#permuted-congruential-generator-64-bit-pcg64-dxsm "Link to this heading")

==============================================================================================================================================================================================================

_class_ numpy.random.PCG64DXSM(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#numpy.random.PCG64DXSM "Link to this definition")

BitGenerator for the PCG-64 DXSM pseudo-random number generator.

Parameters:

**seed**{None, int, array\_like\[ints\], SeedSequence}, optional

A seed to initialize the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. If None, then fresh, unpredictable entropy will be pulled from the OS. If an `int` or `array_like[ints]` is passed, then it will be passed to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to derive the initial [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 state. One may also pass in a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 instance.

Notes

PCG-64 DXSM is a 128-bit implementation of O’Neill’s permutation congruential generator ([\[1\]](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#rad26d0f7d970-1)
, [\[2\]](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#rad26d0f7d970-2)
). PCG-64 DXSM has a period of and supports advancing an arbitrary number of steps as well as 2^{127} streams. The specific member of the PCG family that we use is PCG CM DXSM 128/64. It differs from [`PCG64`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64")
 in that it uses the stronger DXSM output function, a 64-bit “cheap multiplier” in the LCG, and outputs from the state before advancing it rather than advance-then-output.

[`PCG64DXSM`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#numpy.random.PCG64DXSM "numpy.random.PCG64DXSM")
 provides a capsule containing function pointers that produce doubles, and unsigned 32 and 64- bit integers. These are not directly consumable in Python and must be consumed by a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 or similar object that supports low-level access.

Supports the method [`advance`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.advance.html#numpy.random.PCG64DXSM.advance "numpy.random.PCG64DXSM.advance")
 to advance the RNG an arbitrary number of steps. The state of the PCG-64 DXSM RNG is represented by 2 128-bit unsigned integers.

**State and Seeding**

The [`PCG64DXSM`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#numpy.random.PCG64DXSM "numpy.random.PCG64DXSM")
 state vector consists of 2 unsigned 128-bit values, which are represented externally as Python ints. One is the state of the PRNG, which is advanced by a linear congruential generator (LCG). The second is a fixed odd increment used in the LCG.

The input seed is processed by [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to generate both values. The increment is not independently settable.

**Parallel Features**

The preferred way to use a BitGenerator in parallel applications is to use the [`SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 method to obtain entropy values, and to use these to generate new BitGenerators:

\>>> from numpy.random import Generator, PCG64DXSM, SeedSequence
\>>> sg \= SeedSequence(1234)
\>>> rg \= \[Generator(PCG64DXSM(s)) for s in sg.spawn(10)\]

Copy to clipboard

**Compatibility Guarantee**

[`PCG64DXSM`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#numpy.random.PCG64DXSM "numpy.random.PCG64DXSM")
 makes a guarantee that a fixed seed will always produce the same random integer stream.

References

\[[1](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#id1)\
\]

[“PCG, A Family of Better Random Number Generators”](http://www.pcg-random.org/)

\[[2](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#id2)\
\]

O’Neill, Melissa E. [“PCG: A Family of Simple Fast Space-Efficient Statistically Good Algorithms for Random Number Generation”](https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf)

State[#](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#state "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.state.html#numpy.random.PCG64DXSM.state "numpy.random.PCG64DXSM.state") | Get or set the PRNG state |

Parallel generation[#](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#parallel-generation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`advance`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.advance.html#numpy.random.PCG64DXSM.advance "numpy.random.PCG64DXSM.advance")<br>(delta) | Advance the underlying RNG as-if delta draws have occurred. |
| [`jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.jumped.html#numpy.random.PCG64DXSM.jumped "numpy.random.PCG64DXSM.jumped")<br>(\[jumps\]) | Returns a new bit generator with the state jumped. |

Extending[#](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64dxsm.html#extending "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.cffi.html#numpy.random.PCG64DXSM.cffi "numpy.random.PCG64DXSM.cffi") | CFFI interface |
| [`ctypes`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64DXSM.ctypes.html#numpy.random.PCG64DXSM.ctypes "numpy.random.PCG64DXSM.ctypes") | ctypes interface |

On this page