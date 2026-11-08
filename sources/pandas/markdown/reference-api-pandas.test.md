[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.test.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.test[#](https://pandas.pydata.org/docs/reference/api/pandas.test.html#pandas-test "Link to this heading")

=================================================================================================================

pandas.test(_extra\_args\=None_, _run\_doctests\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/util/_tester.py#L16-L56)
[#](https://pandas.pydata.org/docs/reference/api/pandas.test.html#pandas.test "Link to this definition")

Run the pandas test suite using pytest.

By default, runs with the marks -m “not slow and not network and not db”

Parameters:

**extra\_args**list\[str\], default None

Extra marks to run the tests.

**run\_doctests**bool, default False

Whether to only run the Python and Cython doctests. If you would like to run both doctests/regular tests, just append “–doctest-modules”/”–doctest-cython” to extra\_args.

See also

`pytest.main`

The main entry point for pytest testing framework.

Examples

\>>> pd.test()
running: pytest...

Copy to clipboard

On this page