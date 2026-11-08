[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.rundocs.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.rundocs.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.rundocs.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.rundocs.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.rundocs.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.rundocs.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.rundocs.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.rundocs.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.rundocs.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.rundocs.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.rundocs.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.rundocs.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.rundocs.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.rundocs.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.rundocs.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.rundocs.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.rundocs.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.rundocs.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.rundocs.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.rundocs.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.rundocs[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html#numpy-testing-rundocs "Link to this heading")

===================================================================================================================================================

testing.rundocs(_filename\=None_, _raise\_on\_error\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1426-L1472)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html#numpy.testing.rundocs "Link to this definition")

Run doctests found in the given file.

By default [`rundocs`](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html#numpy.testing.rundocs "numpy.testing.rundocs")
 raises an AssertionError on failure.

Parameters:

**filename**str

The path to the file for which the doctests are run.

**raise\_on\_error**bool

Whether to raise an AssertionError when a doctest fails. Default is True.

Notes

The doctests can be run by the user/developer by adding the `doctests` argument to the `test()` call. For example, to run all tests (including doctests) for `numpy.lib`:

\>>> np.lib.test(doctests\=True)  

Copy to clipboard

On this page