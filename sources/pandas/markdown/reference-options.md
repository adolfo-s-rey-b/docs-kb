[Skip to main content](https://pandas.pydata.org/docs/reference/options.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Options and settings[#](https://pandas.pydata.org/docs/reference/options.html#options-and-settings "Link to this heading")

===========================================================================================================================

API for configuring global behavior. See [the User Guide](https://pandas.pydata.org/docs/user_guide/options.html#options)
 for more.

Working with options[#](https://pandas.pydata.org/docs/reference/options.html#working-with-options "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`describe_option`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")<br>(\[pat, \_print\_desc\]) | Print the description for one or more registered options. |
| [`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")<br>(pat) | Reset one or more options to their default value. |
| [`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")<br>(pat) | Retrieve the value of the specified option. |
| [`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")<br>(\*args) | Set the value of the specified option or options. |
| [`option_context`](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")<br>(\*args) | Context manager to temporarily set options in a `with` statement. |

Numeric formatting[#](https://pandas.pydata.org/docs/reference/options.html#numeric-formatting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`set_eng_float_format`](https://pandas.pydata.org/docs/reference/api/pandas.set_eng_float_format.html#pandas.set_eng_float_format "pandas.set_eng_float_format")<br>(\[accuracy, use\_eng\_prefix\]) | (DEPRECATED) Format float representation in DataFrame with SI notation. |

On this page