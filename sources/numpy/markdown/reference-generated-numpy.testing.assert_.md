[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_.html#numpy-testing-assert "Link to this heading")

===================================================================================================================================================

testing.assert\_(_val_, _msg\=''_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L114-L131)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_.html#numpy.testing.assert_ "Link to this definition")

Assert that works in release mode. Accepts callable msg to allow deferring evaluation until failure.

The Python built-in `assert` does not work when executing code in optimized mode (the `-O` flag) - no byte-code is generated for it.

For documentation on usage, refer to the Python documentation.

On this page