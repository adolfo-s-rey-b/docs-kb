[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_pad\_or\_backfill[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html#pandas-api-extensions-extensionarray-pad-or-backfill "Link to this heading")

=================================================================================================================================================================================================================================================

ExtensionArray.\_pad\_or\_backfill(_\*_, _method_, _limit\=None_, _limit\_area\=None_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1303-L1391)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html#pandas.api.extensions.ExtensionArray._pad_or_backfill "Link to this definition")

Pad or backfill values, used by Series/DataFrame ffill and bfill.

This method propagates the last valid observation forward (pad/ffill) or the next valid observation backward (backfill/bfill) to fill NaN values.

Parameters:

**method**{‘backfill’, ‘bfill’, ‘pad’, ‘ffill’}

Method to use for filling holes in reindexed Series:

*   pad / ffill: propagate last valid observation forward to next valid.
    
*   backfill / bfill: use NEXT valid observation to fill gap.
    

**limit**int, default None

This is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled.

**limit\_area**{‘inside’, ‘outside’} or None, default None

Specifies which area to limit filling. - ‘inside’: Limit the filling to the area within the gaps. - ‘outside’: Limit the filling to the area outside the gaps. If None, no limitation is applied.

**copy**bool, default True

Whether to make a copy of the data before filling. If False, then the original should be modified and no new memory should be allocated. For ExtensionArray subclasses that cannot do this, it is at the author’s discretion whether to ignore “copy=False” or to raise. The base class implementation ignores the keyword if any NAs are present.

Returns:

Same type as self

The filled array with the same type as the original.

See also

`Series.ffill`

Forward fill missing values.

`Series.bfill`

Backward fill missing values.

`DataFrame.ffill`

Forward fill missing values in DataFrame.

`DataFrame.bfill`

Backward fill missing values in DataFrame.

`api.types.isna`

Check for missing values.

`api.types.isnull`

Check for missing values.

Examples

\>>> arr \= pd.array(\[np.nan, np.nan, 2, 3, np.nan, np.nan\])
\>>> arr.\_pad\_or\_backfill(method\="backfill", limit\=1)
<IntegerArray>
\[<NA>, 2, 2, 3, <NA>, <NA>\]
Length: 6, dtype: Int64

Copy to clipboard

On this page