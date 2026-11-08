[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.suppress_warnings.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.suppress_warnings.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.suppress_warnings.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.suppress_warnings.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.suppress_warnings.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.suppress_warnings.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.suppress_warnings.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.suppress_warnings.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.suppress_warnings.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.suppress_warnings.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.suppress_warnings.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.suppress_warnings.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.suppress_warnings.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.suppress_warnings.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.suppress_warnings.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.suppress_warnings.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.suppress_warnings.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.suppress_warnings.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.suppress_warnings.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.suppress_warnings.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.suppress\_warnings[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.html#numpy-testing-suppress-warnings "Link to this heading")

==================================================================================================================================================================================

_class_ numpy.testing.suppress\_warnings(_forwarding\_rule\='always'_, _\_warn\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2291-L2577)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.html#numpy.testing.suppress_warnings "Link to this definition")

Context manager and decorator doing much the same as `warnings.catch_warnings`.

However, it also provides a filter mechanism to work around [https://bugs.python.org/issue4180](https://bugs.python.org/issue4180)
.

This bug causes Python before 3.4 to not reliably show warnings again after they have been ignored once (even within catch\_warnings). It means that no “ignore” filter can be used easily, since following tests might need to see the warning. Additionally it allows easier specificity for testing warnings and can be nested.

Deprecated since version 2.4: This is deprecated. Use [`warnings.filterwarnings`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "(in Python v3.14)")
 or `pytest.filterwarnings` instead.

Parameters:

**forwarding\_rule**str, optional

One of “always”, “once”, “module”, or “location”. Analogous to the usual warnings module filter mode, it is useful to reduce noise mostly on the outmost level. Unsuppressed and unrecorded warnings will be forwarded based on this rule. Defaults to “always”. “location” is equivalent to the warnings “default”, match by exact location the warning warning originated from.

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.__call__.html#numpy.testing.suppress_warnings.__call__ "numpy.testing.suppress_warnings.__call__")<br>(func) | Function decorator to apply certain suppressions to a whole function. |
| [`filter`](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.filter.html#numpy.testing.suppress_warnings.filter "numpy.testing.suppress_warnings.filter")<br>(\[category, message, module\]) | Add a new suppressing filter or apply it if the state is entered. |
| [`record`](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.record.html#numpy.testing.suppress_warnings.record "numpy.testing.suppress_warnings.record")<br>(\[category, message, module\]) | Append a new recording filter or apply it if the state is entered. |

Notes

Filters added inside the context manager will be discarded again when leaving it. Upon entering all filters defined outside a context will be applied automatically.

When a recording filter is added, matching warnings are stored in the `log` attribute as well as in the list returned by `record`.

If filters are added and the `module` keyword is given, the warning registry of this module will additionally be cleared when applying it, entering the context, or exiting it. This could cause warnings to appear a second time after leaving the context if they were configured to be printed once (default) and were already printed before the context was entered.

Nesting this context manager will work as expected when the forwarding rule is “always” (default). Unfiltered and unrecorded warnings will be passed out and be matched by the outer level. On the outmost level they will be printed (or caught by another warnings context). The forwarding rule argument can modify this behaviour.

Like `catch_warnings` this context manager is not threadsafe.

Examples

Try it in your browser!

With a context manager:

with np.testing.suppress\_warnings() as sup:
    sup.filter(DeprecationWarning, "Some text")
    sup.filter(module\=np.ma.core)
    log \= sup.record(FutureWarning, "Does this occur?")
    command\_giving\_warnings()
    \# The FutureWarning was given once, the filtered warnings were
    \# ignored. All other warnings abide outside settings (may be
    \# printed/error)
    assert\_(len(log) \== 1)
    assert\_(len(sup.log) \== 1)  \# also stored in log attribute

Copy to clipboard

Or as a decorator:

sup \= np.testing.suppress\_warnings()
sup.filter(module\=np.ma.core)  \# module must match exactly
@sup
def some\_function():
    \# do something which causes a warning in np.ma.core
    pass

Copy to clipboard

Go BackOpen In Tab

On this page