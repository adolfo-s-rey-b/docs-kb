[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Philox.jumped[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#numpy-random-philox-jumped "Link to this heading")

========================================================================================================================================================================================

method

random.Philox.jumped(_jumps\=1_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.Philox.jumped.html#numpy.random.Philox.jumped "Link to this definition")

Returns a new bit generator with the state jumped

The state of the returned bit generator is jumped as-if (2\*\*128) \* jumps random numbers have been generated.

Parameters:

**jumps**integer, positive

Number of times to jump the state of the bit generator returned

Returns:

**bit\_generator**Philox

New instance of generator jumped iter times

On this page