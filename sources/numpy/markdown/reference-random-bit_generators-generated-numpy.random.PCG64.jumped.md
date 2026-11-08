[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.jumped.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.PCG64.jumped[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.jumped.html#numpy-random-pcg64-jumped "Link to this heading")

=====================================================================================================================================================================================

method

random.PCG64.jumped(_jumps\=1_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.jumped.html#numpy.random.PCG64.jumped "Link to this definition")

Returns a new bit generator with the state jumped.

Jumps the state as-if jumps \* 210306068529402873165736369884012333109 random numbers have been generated.

Parameters:

**jumps**integer, positive

Number of times to jump the state of the bit generator returned

Returns:

**bit\_generator**PCG64

New instance of generator jumped iter times

Notes

The step size is phi-1 when multiplied by 2\*\*128 where phi is the golden ratio.

On this page