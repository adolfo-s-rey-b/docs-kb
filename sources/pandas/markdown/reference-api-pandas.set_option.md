[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.set_option.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.set_option.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.set_option.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.set_option.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.set_option.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.set_option.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.set_option.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.set_option.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.set_option.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.set_option.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.set_option.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.set_option.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.set\_option[#](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas-set-option "Link to this heading")

====================================================================================================================================

pandas.set\_option(_\*args_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_config/config.py#L227-L301)
[#](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "Link to this definition")

Set the value of the specified option or options.

This method allows fine-grained control over the behavior and display settings of pandas. Options affect various functionalities such as output formatting, display limits, and operational behavior. Settings can be modified at runtime without requiring changes to global configurations or environment variables.

Parameters:

**\*args**str | object | dict

Arguments provided in pairs, which will be interpreted as (pattern, value), or as a single dictionary containing multiple option-value pairs. pattern: str Regexp which should match a single option value: object New value of option

Warning

Partial pattern matches are supported for convenience, but unless you use the full option name (e.g. x.y.z.option\_name), your code may break in future versions if new options with similar names are introduced.

Returns:

None

No return value.

Raises:

ValueError if odd numbers of non-keyword arguments are provided

TypeError if keyword arguments are provided

OptionError if no such option exists

See also

[`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")

Retrieve the value of the specified option.

[`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")

Reset one or more options to their default value.

[`describe_option`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")

Print the description for one or more registered options.

[`option_context`](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")

Context manager to temporarily set options in a `with` statement.

Notes

For all available options, please view the [User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
 or use `pandas.describe_option()`.

Examples

Option-Value Pair Input:

\>>> pd.set\_option("display.max\_columns", 4)
\>>> df \= pd.DataFrame(\[\[1, 2, 3, 4, 5\], \[6, 7, 8, 9, 10\]\])
\>>> df
0  1  ...  3   4
0  1  2  ...  4   5
1  6  7  ...  9  10
\[2 rows x 5 columns\]
\>>> pd.reset\_option("display.max\_columns")

Copy to clipboard

Dictionary Input:

\>>> pd.set\_option({"display.max\_columns": 4, "display.precision": 1})
\>>> df \= pd.DataFrame(\[\[1, 2, 3, 4, 5\], \[6, 7, 8, 9, 10\]\])
\>>> df
0  1  ...  3   4
0  1  2  ...  4   5
1  6  7  ...  9  10
\[2 rows x 5 columns\]
\>>> pd.reset\_option("display.max\_columns")
\>>> pd.reset\_option("display.precision")

Copy to clipboard

On this page