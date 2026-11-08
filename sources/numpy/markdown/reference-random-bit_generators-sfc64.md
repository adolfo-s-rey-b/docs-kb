[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/sfc64.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/sfc64.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/sfc64.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/sfc64.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/sfc64.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/sfc64.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/sfc64.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/sfc64.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/sfc64.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/sfc64.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/sfc64.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/sfc64.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/sfc64.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/sfc64.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/sfc64.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/sfc64.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/sfc64.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/sfc64.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/sfc64.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/sfc64.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

SFC64 Small Fast Chaotic PRNG[#](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#sfc64-small-fast-chaotic-prng "Link to this heading")

===============================================================================================================================================================

_class_ numpy.random.SFC64(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "Link to this definition")

BitGenerator for Chris Doty-Humphrey’s Small Fast Chaotic PRNG.

Parameters:

**seed**{None, int, array\_like\[ints\], SeedSequence}, optional

A seed to initialize the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. If None, then fresh, unpredictable entropy will be pulled from the OS. If an `int` or `array_like[ints]` is passed, then it will be passed to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to derive the initial [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 state. One may also pass in a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 instance.

Notes

[`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 is a 256-bit implementation of Chris Doty-Humphrey’s Small Fast Chaotic PRNG ([\[1\]](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#r50352647a6aa-1)
). [`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 has a few different cycles that one might be on, depending on the seed; the expected period will be about \\(2^{255}\\) ([\[2\]](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#r50352647a6aa-2)
). [`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 incorporates a 64-bit counter which means that the absolute minimum cycle length is \\(2^{64}\\) and that distinct seeds will not run into each other for at least \\(2^{64}\\) iterations.

[`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 provides a capsule containing function pointers that produce doubles, and unsigned 32 and 64- bit integers. These are not directly consumable in Python and must be consumed by a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 or similar object that supports low-level access.

**State and Seeding**

The [`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 state vector consists of 4 unsigned 64-bit values. The last is a 64-bit counter that increments by 1 each iteration.

The input seed is processed by [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to generate the first 3 values, then the [`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 algorithm is iterated a small number of times to mix.

**Compatibility Guarantee**

[`SFC64`](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#numpy.random.SFC64 "numpy.random.SFC64")
 makes a guarantee that a fixed seed will always produce the same random integer stream.

References

\[[1](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#id1)\
\]

[“PractRand”](https://pracrand.sourceforge.net/RNG_engines.txt)

\[[2](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#id2)\
\]

[“Random Invertible Mapping Statistics”](https://www.pcg-random.org/posts/random-invertible-mapping-statistics.html)

State[#](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#state "Link to this heading")

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SFC64.state.html#numpy.random.SFC64.state "numpy.random.SFC64.state") | Get or set the PRNG state |

Extending[#](https://numpy.org/doc/stable/reference/random/bit_generators/sfc64.html#extending "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SFC64.cffi.html#numpy.random.SFC64.cffi "numpy.random.SFC64.cffi") | CFFI interface |
| [`ctypes`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SFC64.ctypes.html#numpy.random.SFC64.ctypes "numpy.random.SFC64.ctypes") | ctypes interface |

On this page