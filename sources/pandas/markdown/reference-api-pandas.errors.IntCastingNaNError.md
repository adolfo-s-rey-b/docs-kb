[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.IntCastingNaNError.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.IntCastingNaNError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.IntCastingNaNError.html#pandas-errors-intcastingnanerror "Link to this heading")

================================================================================================================================================================================

exception pandas.errors.IntCastingNaNError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L21-L40)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.IntCastingNaNError.html#pandas.errors.IntCastingNaNError "Link to this definition")

Exception raised when converting (`astype`) an array with NaN to an integer type.

This error occurs when attempting to cast a data structure containing non-finite values (such as NaN or infinity) to an integer data type. Integer types do not support non-finite values, so such conversions are explicitly disallowed to prevent silent data corruption or unexpected behavior.

See also

`DataFrame.astype`

Method to cast a pandas DataFrame object to a specified dtype.

`Series.astype`

Method to cast a pandas Series object to a specified dtype.

Examples

\>>> pd.DataFrame(np.array(\[\[1, np.nan\], \[2, 3\]\]), dtype\="i8")
Traceback (most recent call last):
IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer

Copy to clipboard

On this page