[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.SeedSequence.generate\_state[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html#numpy-random-seedsequence-generate-state "Link to this heading")

===================================================================================================================================================================================================================================

method

random.SeedSequence.generate\_state(_n\_words_, _dtype\=np.uint32_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html#numpy.random.SeedSequence.generate_state "Link to this definition")

Return the requested number of words for PRNG seeding.

A BitGenerator should call this method in its constructor with an appropriate _n\_words_ parameter to properly seed itself.

Parameters:

**n\_words**int

**dtype**np.uint32 or np.uint64, optional

The size of each word. This should only be either [`uint32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint32 "numpy.uint32")
 or [`uint64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint64 "numpy.uint64")
. Strings (_‘uint32’_, _‘uint64’_) are fine. Note that requesting [`uint64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint64 "numpy.uint64")
 will draw twice as many bits as [`uint32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint32 "numpy.uint32")
 for the same _n\_words_. This is a convenience for _BitGenerator_s that express their states as [`uint64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint64 "numpy.uint64")
 arrays.

Returns:

**state**uint32 or uint64 array, shape=(n\_words,)

On this page