[Skip to main content](https://numpy.org/doc/stable/user/how-to-print.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/how-to-print.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/how-to-print.html)
[2.4](https://numpy.org/doc/2.4/user/how-to-print.html)
[2.3](https://numpy.org/doc/2.3/user/how-to-print.html)
[2.2](https://numpy.org/doc/2.2/user/how-to-print.html)
[2.1](https://numpy.org/doc/2.1/user/how-to-print.html)
[2.0](https://numpy.org/doc/2.0/user/how-to-print.html)
[1.26](https://numpy.org/doc/1.26/user/how-to-print.html)
[1.25](https://numpy.org/doc/1.25/user/how-to-print.html)
[1.24](https://numpy.org/doc/1.24/user/how-to-print.html)
[1.23](https://numpy.org/doc/1.23/user/how-to-print.html)
[1.22](https://numpy.org/doc/1.22/user/how-to-print.html)
[1.21](https://numpy.org/doc/1.21/user/how-to-print.html)
[1.20](https://numpy.org/doc/1.20/user/how-to-print.html)
[1.19](https://numpy.org/doc/1.19/user/how-to-print.html)
[1.18](https://numpy.org/doc/1.18/user/how-to-print.html)
[1.17](https://numpy.org/doc/1.17/user/how-to-print.html)
[1.16](https://numpy.org/doc/1.16/user/how-to-print.html)
[1.15](https://numpy.org/doc/1.15/user/how-to-print.html)
[1.14](https://numpy.org/doc/1.14/user/how-to-print.html)
[1.13](https://numpy.org/doc/1.13/user/how-to-print.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Printing NumPy Arrays[#](https://numpy.org/doc/stable/user/how-to-print.html#printing-numpy-arrays "Link to this heading")

===========================================================================================================================

This page explains how to control the formatting of printed NumPy arrays. Note that these printing options apply only to arrays, not to scalars.

Defining printing options[#](https://numpy.org/doc/stable/user/how-to-print.html#defining-printing-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

### Applying settings globally[#](https://numpy.org/doc/stable/user/how-to-print.html#applying-settings-globally "Link to this heading")

Use [`numpy.set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
 to change printing options for the entire runtime session. To inspect current print settings, use [`numpy.get_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions")
:

\>>> np.set\_printoptions(precision\=2)
\>>> np.get\_printoptions()
{'edgeitems': 3, 'threshold': 1000, 'floatmode': 'maxprec', 'precision': 2, 'suppress': False, 'linewidth': 75, 'nanstr': 'nan', 'infstr': 'inf', 'sign': '-', 'formatter': None, 'legacy': False, 'override\_repr': None}

Copy to clipboard

To restore the default settings, use:

\>>> np.set\_printoptions(edgeitems\=3, infstr\='inf',
... linewidth\=75, nanstr\='nan', precision\=8,
... suppress\=False, threshold\=1000, formatter\=None)

Copy to clipboard

### Applying settings temporarily[#](https://numpy.org/doc/stable/user/how-to-print.html#applying-settings-temporarily "Link to this heading")

Use [`numpy.printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
 as a context manager to temporarily override print settings within a specific scope:

\>>> arr \= np.array(\[0.155, 0.184, 0.173\])
\>>> with np.printoptions(precision\=2):
...     print(arr)
\[0.15 0.18 0.17\]

Copy to clipboard

All keywords that apply to [`numpy.set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
 also apply to [`numpy.printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
.

Changing the number of digits of precision[#](https://numpy.org/doc/stable/user/how-to-print.html#changing-the-number-of-digits-of-precision "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default number of fractional digits displayed is 8. You can change this number using `precision` keyword.

\>>> arr \= np.array(\[0.1, 0.184, 0.17322\])
\>>> with np.printoptions(precision\=2):
...     print(arr)
\[0.1 0.18 0.17\]

Copy to clipboard

The `floatmode` option determines how the `precision` setting is interpreted. By default, `floatmode=maxprec_equal` displays values with the minimal number of digits needed to uniquely represent them, using the same number of digits across all elements. If you want to show exactly the same number of digits specified by `precision`, use `floatmode=fixed`:

\>>> arr \= np.array(\[0.1, 0.184, 0.173\], dtype\=np.float32)
\>>> with np.printoptions(precision\=2, floatmode\="fixed"):
...     print(arr)
\[0.10 0.18 0.17\]

Copy to clipboard

Changing how _nan_ and _inf_ are displayed[#](https://numpy.org/doc/stable/user/how-to-print.html#changing-how-nan-and-inf-are-displayed "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, [`numpy.nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
 is displayed as _nan_ and [`numpy.inf`](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")
 is displayed as _inf_. You can override these representations using the `nanstr` and `infstr` options:

\>>> arr \= np.array(\[np.inf, np.nan, 0\])
\>>> with np.printoptions(nanstr\="NAN", infstr\="INF"):
...     print(arr)
\[INF NAN  0.\]

Copy to clipboard

Controlling scientific notations[#](https://numpy.org/doc/stable/user/how-to-print.html#controlling-scientific-notations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

By default, NumPy uses scientific notation when:

*   The absolute value of the smallest number is less than `1e-4`, or
    
*   The ratio of the largest to the smallest absolute value is greater than `1e3`
    
    \>>> arr \= np.array(\[0.00002, 210000.0, 3.14\])
    \>>> print(arr)
    \[2.00e-05 2.10e+05 3.14e+00\]
    
    Copy to clipboard
    

To suppress scientific notation and always use fixed-point notation, set `suppress=True`:

\>>> arr \= np.array(\[0.00002, 210000.0, 3.14\])
\>>> with np.printoptions(suppress\=True):
...     print(arr)
\[     0.00002 210000.           3.14   \]

Copy to clipboard

Applying custom formatting functions[#](https://numpy.org/doc/stable/user/how-to-print.html#applying-custom-formatting-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

You can apply custom formatting functions to specific or all data types using `formatter` keyword. See [`numpy.set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
 for more details on supported format keys.

For example, to format _datetime64_ values with a custom function:

\>>> arr \= np.array(\[np.datetime64("2025-01-01"), np.datetime64("2024-01-01")\])
\>>> with np.printoptions(formatter\={"datetime":lambda x: f"(Year: {x.item().year}, Month: {x.item().month})"}):
...     print(arr)
\[(Year: 2025, Month: 1) (Year: 2024, Month: 1)\]

Copy to clipboard

On this page