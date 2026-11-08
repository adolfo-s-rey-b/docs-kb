[Skip to main content](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#sphx-glr-download-gallery-ticks-ticks-too-many-py)
 to download the full example code.

Fixing too many ticks[#](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#fixing-too-many-ticks "Link to this heading")

=======================================================================================================================================

One common cause for unexpected tick behavior is passing a list of strings instead of numbers or datetime objects. This can easily happen without notice when reading in a comma-delimited text file. Matplotlib treats lists of strings as _categorical_ variables ([Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)
), and by default puts one tick per category, and plots them in the order in which they are supplied. If this is not desired, the solution is to convert the strings to a numeric type as in the following examples.

Example 1: Strings can lead to an unexpected order of number ticks[#](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#example-1-strings-can-lead-to-an-unexpected-order-of-number-ticks "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained', figsize\=(6, 2.5))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \['1', '5', '2', '3'\]
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 4, 2, 3\]
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'd')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].tick\_params(axis\='x', color\='r', labelcolor\='r')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_xlabel('Categories')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Ticks seem out of order / misplaced')

\# convert to numbers:
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, dtype\='float')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'd')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_xlabel('Floats')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('Ticks as expected')

![Ticks seem out of order / misplaced, Ticks as expected](https://matplotlib.org/stable/_images/sphx_glr_ticks_too_many_001_2_00x.png)

Example 2: Strings can lead to very many ticks[#](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#example-2-strings-can-lead-to-very-many-ticks "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If _x_ has 100 elements, all strings, then we would have 100 (unreadable) ticks, and again the solution is to convert the strings to floats:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(6, 2.5))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[f'{xx}' for xx in [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(100)\]
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100)
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].tick\_params(axis\='x', color\='r', labelcolor\='r')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Too many ticks')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_xlabel('Categories')

[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, float), [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('x converted to numbers')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_xlabel('Floats')

![Too many ticks, x converted to numbers](https://matplotlib.org/stable/_images/sphx_glr_ticks_too_many_002_2_00x.png)

Example 3: Strings can lead to an unexpected order of datetime ticks[#](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html#example-3-strings-can-lead-to-an-unexpected-order-of-datetime-ticks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common case is when dates are read from a CSV file, they need to be converted from strings to datetime objects to get the proper date locators and formatters.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained', figsize\=(6, 2.75))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01'\]
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 2, 3, 1\]
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'd')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].tick\_params(axis\='x', labelrotation\=90, color\='r', labelcolor\='r')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Dates out of order')

\# convert to datetime64
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, dtype\='datetime64\[s\]')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'd')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].tick\_params(axis\='x', labelrotation\=90)
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('x converted to datetimes')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Dates out of order, x converted to datetimes](https://matplotlib.org/stable/_images/sphx_glr_ticks_too_many_003_2_00x.png)

**Total running time of the script:** (0 minutes 2.345 seconds)

[`Download Jupyter notebook: ticks_too_many.ipynb`](https://matplotlib.org/stable/_downloads/7d15979e196145f0d7805e9b6cfdd1f0/ticks_too_many.ipynb)

[`Download Python source code: ticks_too_many.py`](https://matplotlib.org/stable/_downloads/bf27e73826393797c5d906c0afefb14d/ticks_too_many.py)

[`Download zipped: ticks_too_many.zip`](https://matplotlib.org/stable/_downloads/8d497cb85fa6ce09838ef45423ac5bb7/ticks_too_many.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page