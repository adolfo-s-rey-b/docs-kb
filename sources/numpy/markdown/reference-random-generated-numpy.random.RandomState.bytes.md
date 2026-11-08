[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.bytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.bytes.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.bytes.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.bytes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.bytes[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.bytes.html#numpy-random-randomstate-bytes "Link to this heading")

=====================================================================================================================================================================================

method

random.RandomState.bytes(_length_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.bytes.html#numpy.random.RandomState.bytes "Link to this definition")

Return random bytes.

Note

New code should use the [`bytes`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.bytes.html#numpy.random.Generator.bytes "numpy.random.Generator.bytes")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**length**int

Number of random bytes.

Returns:

**out**bytes

String of length _length_.

See also

[`random.Generator.bytes`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.bytes.html#numpy.random.Generator.bytes "numpy.random.Generator.bytes")

which should be used for new code.

Examples

Try it in your browser!

\>>> np.random.bytes(10)
b' eh\\x85\\x022SZ\\xbf\\xa4' #random

Copy to clipboard

Go BackOpen In Tab

On this page