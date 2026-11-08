[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.TooHardError.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.exceptions.TooHardError.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.TooHardError.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.exceptions.TooHardError.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.exceptions.TooHardError.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.exceptions.TooHardError.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.exceptions.TooHardError.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.exceptions.TooHardError.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.exceptions.TooHardError.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.exceptions.TooHardError.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.exceptions.TooHardError.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.exceptions.TooHardError.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.exceptions.TooHardError.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.exceptions.TooHardError.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.exceptions.TooHardError.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.exceptions.TooHardError.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.exceptions.TooHardError.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.exceptions.TooHardError.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.exceptions.TooHardError.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.exceptions.TooHardError.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.exceptions.TooHardError.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.exceptions.TooHardError.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.exceptions.TooHardError[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.TooHardError.html#numpy-exceptions-tooharderror "Link to this heading")

===========================================================================================================================================================================

_exception_ exceptions.TooHardError[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/exceptions.py#L96-L105)
[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.TooHardError.html#numpy.exceptions.TooHardError "Link to this definition")

`max_work` was exceeded.

This is raised whenever the maximum number of candidate solutions to consider specified by the `max_work` parameter is exceeded. Assigning a finite number to `max_work` may have caused the operation to fail.

On this page