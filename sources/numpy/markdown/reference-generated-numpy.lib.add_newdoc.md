[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.add_newdoc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.add\_newdoc[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.add_newdoc.html#numpy-lib-add-newdoc "Link to this heading")

=================================================================================================================================================

lib.add\_newdoc(_place_, _obj_, _doc_, _warn\_on\_python\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/function_base.py#L490-L547)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.add_newdoc.html#numpy.lib.add_newdoc "Link to this definition")

Add documentation to an existing object, typically one defined in C

The purpose is to allow easier editing of the docstrings without requiring a re-compile. This exists primarily for internal use within numpy itself.

Parameters:

**place**str

The absolute name of the module to import from

**obj**str | None

The name of the object to add documentation to, typically a class or function name.

**doc**str | tuple\[str, str\] | list\[tuple\[str, str\]\]

If a string, the documentation to apply to _obj_

If a tuple, then the first element is interpreted as an attribute of _obj_ and the second as the docstring to apply - `(method, docstring)`

If a list, then each element of the list should be a tuple of length two - `[(method1, docstring1), (method2, docstring2), ...]`

**warn\_on\_python**bool

If True, the default, emit _UserWarning_ if this is used to attach documentation to a pure-python object.

Notes

This routine never raises an error if the docstring can’t be written, but will raise an error if the object being documented does not exist.

This routine cannot modify read-only docstrings, as appear in new-style classes or built-in functions. Because this routine never raises an error the caller must check manually that the docstrings were changed.

Since this function grabs the `char *` from a c-level str object and puts it into the `tp_doc` slot of the type of _obj_, it violates a number of C-API best-practices, by:

*   modifying a _PyTypeObject_ after calling _PyType\_Ready_
    
*   calling _Py\_INCREF_ on the str and losing the reference, so the str will never be released
    

If possible it should be avoided.

On this page