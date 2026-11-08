[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.mid.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.mid.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.mid.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.mid.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.mid.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.mid.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.mid.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.mid.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.mid.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.mid.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.mid.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.mid.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.mid[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html#pandas-interval-mid "Link to this heading")

=========================================================================================================================================

Interval.mid[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html#pandas.Interval.mid "Link to this definition")

Return the midpoint of the Interval.

The midpoint is the average of the left and right bounds, or equivalently the left bound plus half of [`length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length")
.

See also

[`Interval.left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "pandas.Interval.left")

Return the left bound for the interval.

[`Interval.right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "pandas.Interval.right")

Return the right bound for the interval.

[`Interval.length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length")

Return the length of the interval.

Examples

\>>> iv \= pd.Interval(0, 5)
\>>> iv.mid
2.5

Copy to clipboard

On this page