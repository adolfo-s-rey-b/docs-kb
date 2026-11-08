[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas-timestamp-quarter "Link to this heading")

========================================================================================================================================================

Timestamp.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "Link to this definition")

Return the quarter of the year for the Timestamp.

This property returns an integer representing the quarter of the year in which the Timestamp falls. The quarters are defined as follows: - Q1: January 1 to March 31 - Q2: April 1 to June 30 - Q3: July 1 to September 30 - Q4: October 1 to December 31

Returns:

int

The quarter of the year (1 through 4).

See also

[`Timestamp.month`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#pandas.Timestamp.month "pandas.Timestamp.month")

Returns the month of the Timestamp.

[`Timestamp.year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.year.html#pandas.Timestamp.year "pandas.Timestamp.year")

Returns the year of the Timestamp.

Examples

Get the quarter for a Timestamp:

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.quarter
1

Copy to clipboard

For a Timestamp in the fourth quarter:

\>>> ts \= pd.Timestamp(2020, 10, 14)
\>>> ts.quarter
4

Copy to clipboard

On this page