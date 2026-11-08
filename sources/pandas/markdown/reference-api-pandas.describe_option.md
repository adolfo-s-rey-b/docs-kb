[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.describe\_option[#](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas-describe-option "Link to this heading")

===================================================================================================================================================

pandas.describe\_option(_pat\=''_, _\_print\_desc\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_config/config.py#L304-L354)
[#](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "Link to this definition")

Print the description for one or more registered options.

Call with no arguments to get a listing for all registered options.

Parameters:

**pat**str, default “”

String or string regexp pattern. Empty string will return all options. For regexp strings, all matching keys will have their description displayed.

**\_print\_desc**bool, default True

If True (default) the description(s) will be printed to stdout. Otherwise, the description(s) will be returned as a string (for testing).

Returns:

None

If `_print_desc=True`.

str

If the description(s) as a string if `_print_desc=False`.

See also

[`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")

Retrieve the value of the specified option.

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option or options.

[`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")

Reset one or more options to their default value.

Notes

For all available options, please view the [User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
.

Examples

\>>> pd.describe\_option("display.max\_columns")
display.max\_columns : int
    If max\_cols is exceeded, switch to truncate view...

Copy to clipboard

On this page