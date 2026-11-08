[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.show_config.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.show\_config[#](https://numpy.org/doc/stable/reference/generated/numpy.show_config.html#numpy-show-config "Link to this heading")

========================================================================================================================================

numpy.show\_config(_mode\='stdout'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__config__.py#L165-L166)
[#](https://numpy.org/doc/stable/reference/generated/numpy.show_config.html#numpy.show_config "Link to this definition")

Show libraries and system information on which NumPy was built and is being used

Parameters:

**mode**{_‘stdout’_, _‘dicts’_}, optional.

Indicates how to display the config information. _‘stdout’_ prints to console, _‘dicts’_ returns a dictionary of the configuration.

Returns:

**out**{_dict_, _None_}

If mode is _‘dicts’_, a dict is returned, else None

See also

[`get_include`](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#numpy.get_include "numpy.get_include")

Returns the directory containing NumPy C header files.

Notes

1.  The _‘stdout’_ mode will give more readable output if `pyyaml` is installed
    

On this page