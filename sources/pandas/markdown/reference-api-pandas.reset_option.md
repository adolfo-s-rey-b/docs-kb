[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.reset_option.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.reset_option.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.reset_option.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.reset_option.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.reset_option.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.reset_option.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.reset_option.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.reset_option.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.reset_option.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.reset_option.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.reset_option.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.reset_option.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.reset\_option[#](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas-reset-option "Link to this heading")

==========================================================================================================================================

pandas.reset\_option(_pat_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_config/config.py#L357-L411)
[#](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "Link to this definition")

Reset one or more options to their default value.

This method resets the specified pandas option(s) back to their default values. It allows partial string matching for convenience, but users should exercise caution to avoid unintended resets due to changes in option names in future versions.

Parameters:

**pat**str/regex

If specified only options matching `pat*` will be reset. Pass `"all"` as argument to reset all options.

Warning

Partial matches are supported for convenience, but unless you use the full option name (e.g. x.y.z.option\_name), your code may break in future versions if new options with similar names are introduced.

Returns:

None

No return value.

See also

[`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")

Retrieve the value of the specified option.

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option or options.

[`describe_option`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")

Print the description for one or more registered options.

Notes

For all available options, please view the [User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
.

Examples

\>>> pd.reset\_option("display.max\_columns")

Copy to clipboard

On this page