[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.seed.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.seed.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.seed.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.seed.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.seed.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.seed.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.seed.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.seed.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.seed.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.seed.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.seed.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.seed.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.seed.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.seed.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.seed.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.seed.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.seed.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.seed.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.seed.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.seed.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.seed[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy-random-seed "Link to this heading")

==============================================================================================================================================

random.seed(_seed\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "Link to this definition")

Reseed the singleton RandomState instance.

See also

[`numpy.random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")

Notes

This is a convenience, legacy function that exists to support older code that uses the singleton RandomState. Best practice is to use a dedicated `Generator` instance rather than the random variate generation methods exposed directly in the random module.

On this page