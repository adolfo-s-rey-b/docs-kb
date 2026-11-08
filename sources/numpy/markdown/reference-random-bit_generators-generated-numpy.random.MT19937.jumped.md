[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.MT19937.jumped[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#numpy-random-mt19937-jumped "Link to this heading")

===========================================================================================================================================================================================

method

random.MT19937.jumped(_jumps\=1_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.jumped.html#numpy.random.MT19937.jumped "Link to this definition")

Returns a new bit generator with the state jumped

The state of the returned bit generator is jumped as-if 2\*\*(128 \* jumps) random numbers have been generated.

Parameters:

**jumps**integer, positive

Number of times to jump the state of the bit generator returned

Returns:

**bit\_generator**MT19937

New instance of generator jumped iter times

Notes

The jump step is computed using a modified version of Matsumoto’s implementation of Horner’s method. The step polynomial is precomputed to perform 2\*\*128 steps. The jumped state has been verified to match the state produced using Matsumoto’s original code.

References

\[1\]

Matsumoto, M, Generating multiple disjoint streams of pseudorandom number sequences. Accessed on: May 6, 2020. [http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/JUMP/](http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/JUMP/)

\[2\]

Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François Panneton, Pierre L’Ecuyer, “Efficient Jump Ahead for F2-Linear Random Number Generators”, INFORMS JOURNAL ON COMPUTING, Vol. 20, No. 3, Summer 2008, pp. 385-390.

On this page