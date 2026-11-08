[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.OptionError.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.OptionError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OptionError.html#pandas-errors-optionerror "Link to this heading")

===========================================================================================================================================================

exception pandas.errors.OptionError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OptionError.html#pandas.errors.OptionError "Link to this definition")

Exception raised for pandas.options.

Backwards compatible with KeyError checks.

See also

`options`

Access and modify global pandas settings.

Examples

\>>> pd.options.context
Traceback (most recent call last):
OptionError: No such option

Copy to clipboard

On this page