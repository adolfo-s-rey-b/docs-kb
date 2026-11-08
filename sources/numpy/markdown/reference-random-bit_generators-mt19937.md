[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/mt19937.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/mt19937.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/mt19937.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/mt19937.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/mt19937.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/mt19937.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/mt19937.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/mt19937.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/mt19937.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/mt19937.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/mt19937.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/mt19937.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/mt19937.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/mt19937.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/mt19937.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/mt19937.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/mt19937.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/mt19937.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/mt19937.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/mt19937.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Mersenne Twister (MT19937)[#](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#mersenne-twister-mt19937 "Link to this heading")

=========================================================================================================================================================

_class_ numpy.random.MT19937(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "Link to this definition")

Container for the Mersenne Twister pseudo-random number generator.

Parameters:

**seed**{None, int, array\_like\[ints\], SeedSequence}, optional

A seed to initialize the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. If None, then fresh, unpredictable entropy will be pulled from the OS. If an `int` or `array_like[ints]` is passed, then it will be passed to [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to derive the initial [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 state. One may also pass in a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 instance.

Attributes:

**lock: threading.Lock**

Lock instance that is shared so that the same bit git generator can be used in multiple Generators without corrupting the state. Code that generates values from a bit generator should hold the bit generator’s lock.

Notes

[`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 provides a capsule containing function pointers that produce doubles, and unsigned 32 and 64- bit integers [\[1\]](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#r312276d80bfa-1)
. These are not directly consumable in Python and must be consumed by a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 or similar object that supports low-level access.

The Python stdlib module “random” also contains a Mersenne Twister pseudo-random number generator.

**State and Seeding**

The [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 state vector consists of a 624-element array of 32-bit unsigned integers plus a single integer value between 0 and 624 that indexes the current position within the main array.

The input seed is processed by [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 to fill the whole state. The first element is reset such that only its most significant bit is set.

**Parallel Features**

The preferred way to use a BitGenerator in parallel applications is to use the [`SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 method to obtain entropy values, and to use these to generate new BitGenerators:

\>>> from numpy.random import Generator, MT19937, SeedSequence
\>>> sg \= SeedSequence(1234)
\>>> rg \= \[Generator(MT19937(s)) for s in sg.spawn(10)\]

Copy to clipboard

Another method is to use [`MT19937.jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#numpy.random.MT19937.jumped "numpy.random.MT19937.jumped")
 which advances the state as-if \\(2^{128}\\) random numbers have been generated ([\[1\]](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#r312276d80bfa-1)
, [\[2\]](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#r312276d80bfa-2)
). This allows the original sequence to be split so that distinct segments can be used in each worker process. All generators should be chained to ensure that the segments come from the same sequence.

\>>> from numpy.random import Generator, MT19937, SeedSequence
\>>> sg \= SeedSequence(1234)
\>>> bit\_generator \= MT19937(sg)
\>>> rg \= \[\]
\>>> for \_ in range(10):
...    rg.append(Generator(bit\_generator))
...    \# Chain the BitGenerators
...    bit\_generator \= bit\_generator.jumped()

Copy to clipboard

**Compatibility Guarantee**

[`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")
 makes a guarantee that a fixed seed will always produce the same random integer stream.

References

\[1\] ([1](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#id1)
,[2](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#id2)
)

Hiroshi Haramoto, Makoto Matsumoto, and Pierre L’Ecuyer, “A Fast Jump Ahead Algorithm for Linear Recurrences in a Polynomial Space”, Sequences and Their Applications - SETA, 290–298, 2008.

\[[2](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#id3)\
\]

Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François Panneton, Pierre L’Ecuyer, “Efficient Jump Ahead for F2-Linear Random Number Generators”, INFORMS JOURNAL ON COMPUTING, Vol. 20, No. 3, Summer 2008, pp. 385-390.

State[#](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#state "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.state.html#numpy.random.MT19937.state "numpy.random.MT19937.state") | Get or set the PRNG state |

Parallel generation[#](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#parallel-generation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`jumped`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#numpy.random.MT19937.jumped "numpy.random.MT19937.jumped")<br>(\[jumps\]) | Returns a new bit generator with the state jumped |

Extending[#](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#extending "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html#numpy.random.MT19937.cffi "numpy.random.MT19937.cffi") | CFFI interface |
| [`ctypes`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.ctypes.html#numpy.random.MT19937.ctypes "numpy.random.MT19937.ctypes") | ctypes interface |

On this page