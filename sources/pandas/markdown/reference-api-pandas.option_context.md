[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.option\_context[#](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas-option-context "Link to this heading")

================================================================================================================================================

pandas.option\_context(_\*args_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_config/config.py#L468-L537)
[#](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context "Link to this definition")

Context manager to temporarily set options in a `with` statement.

This method allows users to set one or more pandas options temporarily within a controlled block. The previous options’ values are restored once the block is exited. This is useful when making temporary adjustments to pandas’ behavior without affecting the global state.

Parameters:

**\*args**str | object | dict

An even amount of arguments provided in pairs which will be interpreted as (pattern, value) pairs. Alternatively, a single dictionary of {pattern: value} may be provided.

Returns:

None

No return value.

Yields:

None

No yield value.

See also

[`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")

Retrieve the value of the specified option.

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option.

[`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")

Reset one or more options to their default value.

[`describe_option`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")

Print the description for one or more registered options.

Notes

For all available options, please view the [User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
 or use `pandas.describe_option()`.

Examples

\>>> from pandas import option\_context
\>>> with option\_context("display.max\_rows", 10, "display.max\_columns", 5):
...     pass
\>>> with option\_context({"display.max\_rows": 10, "display.max\_columns": 5}):
...     pass

Copy to clipboard

On this page