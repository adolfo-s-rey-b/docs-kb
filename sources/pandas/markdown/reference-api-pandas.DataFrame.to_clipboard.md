[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_clipboard.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_clipboard.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_clipboard.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_clipboard.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_clipboard.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_clipboard.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_clipboard.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_clipboard.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_clipboard.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_clipboard.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_clipboard.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_clipboard.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_clipboard[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas-dataframe-to-clipboard "Link to this heading")

========================================================================================================================================================================

DataFrame.to\_clipboard(_\*_, _excel\=True_, _sep\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L3185-L3259)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard "Link to this definition")

Copy object to the system clipboard.

Write a text representation of object to the system clipboard. This can be pasted into Excel, for example.

Parameters:

**excel**bool, default True

Produce output in a csv format for easy pasting into excel.

*   True, use the provided separator for csv pasting.
    
*   False, write a string representation of the object to the clipboard.
    

**sep**str, default `'\t'`

Field delimiter.

**\*\*kwargs**

These parameters will be passed to DataFrame.to\_csv. If csv output is not produced (`excel=False` or an invalid `sep`), they are passed to DataFrame.to\_string instead, or ignored for a Series.

See also

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write a DataFrame to a comma-separated values (csv) file.

[`read_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#pandas.read_clipboard "pandas.read_clipboard")

Read text from clipboard and pass to read\_csv.

Notes

Requirements for your platform.

> *   Linux : xclip, or xsel (with PyQt4 modules)
>     
> *   Windows : none
>     
> *   macOS : none
>     

This method uses the processes developed for the package pyperclip. A solution to render any output string format is given in the examples.

Examples

Copy the contents of a DataFrame to the clipboard.

\>>> df \= pd.DataFrame(\[\[1, 2, 3\], \[4, 5, 6\]\], columns\=\["A", "B", "C"\])

Copy to clipboard

\>>> df.to\_clipboard(sep\=",")
... \# Wrote the following to the system clipboard:
... \# ,A,B,C
... \# 0,1,2,3
... \# 1,4,5,6

Copy to clipboard

We can omit the index by passing the keyword index and setting it to false.

\>>> df.to\_clipboard(sep\=",", index\=False)
... \# Wrote the following to the system clipboard:
... \# A,B,C
... \# 1,2,3
... \# 4,5,6

Copy to clipboard

Using the original pyperclip package for any string output format.

import pyperclip

html \= df.style.to\_html()
pyperclip.copy(html)

Copy to clipboard

On this page