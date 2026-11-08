[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.get\_option[#](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas-get-option "Link to this heading")

====================================================================================================================================

pandas.get\_option(_pat_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_config/config.py#L146-L190)
[#](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "Link to this definition")

Retrieve the value of the specified option.

This method allows users to query the current value of a given option in the pandas configuration system. Options control various display, performance, and behavior-related settings within pandas.

Parameters:

**pat**str

Regexp which should match a single option.

Warning

Partial matches are supported for convenience, but unless you use the full option name (e.g. x.y.z.option\_name), your code may break in future versions if new options with similar names are introduced.

Returns:

Any

The value of the option.

Raises:

**OptionError**if no such option exists

See also

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option or options.

[`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")

Reset one or more options to their default value.

[`describe_option`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")

Print the description for one or more registered options.

Notes

For all available options, please view the [User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
 or use `pandas.describe_option()`.

Examples

\>>> pd.get\_option("display.max\_columns")
4

Copy to clipboard

On this page