[Skip to main content](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#sphx-glr-download-gallery-ticks-multilevel-ticks-py)
 to download the full example code.

Multilevel (nested) ticks[#](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#multilevel-nested-ticks "Link to this heading")

===============================================================================================================================================

Sometimes we want another level of tick labels on an axis, perhaps to indicate a grouping of the ticks.

Matplotlib does not provide an automated way to do this, but it is relatively straightforward to annotate below the main axis.

These examples use [`Axes.secondary_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
, which is one approach. It has the advantage that we can use Matplotlib Locators and Formatters on the axis that does the grouping if we want.

This first example creates a secondary xaxis and manually adds the ticks and labels using [`Axes.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
. Note that the tick labels have a newline (e.g. `" Oughts"`) at the beginning of them to put the second-level tick labels below the main tick labels.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained', figsize\=(4, 4))

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(30))

sec \= [ax.secondary\_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
(location\=0)
sec.set\_xticks(\[5, 15, 25\], labels\=\['\\nOughts', '\\nTeens', '\\nTwenties'\])

![multilevel ticks](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_001_2_00x.png)

This second example adds a second level of annotation to a categorical axis. Here we need to note that each animal (category) is assigned an integer, so `cats` is at x=0, `dogs` at x=1 etc. Then we place the ticks on the second level on an x that is at the middle of the animal class we are trying to delineate.

This example also adds tick marks between the classes by adding a second secondary xaxis, and placing long, wide ticks at the boundaries between the animal classes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained', figsize\=(7, 4))

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\['cats', 'dogs', 'pigs', 'snakes', 'lizards', 'chickens',\
         'eagles', 'herons', 'buzzards'\],
        [rng.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")
(size\=9), 'o')

\# label the classes:
sec \= [ax.secondary\_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
(location\=0)
sec.set\_xticks(\[1, 3.5, 6.5\], labels\=\['\\n\\nMammals', '\\n\\nReptiles', '\\n\\nBirds'\])
sec.tick\_params('x', length\=0)

\# lines between the classes:
sec2 \= [ax.secondary\_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
(location\=0)
sec2.set\_xticks(\[\-0.5, 2.5, 4.5, 8.5\], labels\=\[\])
sec2.tick\_params('x', length\=40, width\=1.5)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-0.6, 8.6)

![multilevel ticks](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_002_2_00x.png)

Dates are another common place where we may want to have a second level of tick labels. In this last example, we take advantage of the ability to add an automatic locator and formatter to the secondary xaxis, which means we do not need to set the ticks manually.

This example also differs from the above, in that we placed it at a location below the main axes `location=-0.075` and then we hide the spine by setting the line width to zero. That means that our formatter no longer needs the carriage returns of the previous two examples.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained', figsize\=(7, 4))

[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2020-01-01'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2020-03-31'),
                 [np.timedelta64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
(1, 'D'))

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [rng.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")
(size\=len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)))

\# just format the days:
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([mdates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%d'))

\# label the months:
sec \= [ax.secondary\_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
(location\=-0.075)
[sec.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([mdates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
(bymonthday\=1))

\# note the extra spaces in the label to align the month label inside the month.
\# Note that this could have been done by changing \`\`bymonthday\`\` above as well:
[sec.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([mdates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('  %b'))
sec.tick\_params('x', length\=0)
[sec.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\['bottom'\].set\_linewidth(0)

\# label the xaxis, but note for this to look good, it needs to be on the
\# secondary xaxis.
sec.set\_xlabel('Dates (2020)')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![multilevel ticks](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_003_2_00x.png)

**Total running time of the script:** (0 minutes 1.967 seconds)

[`Download Jupyter notebook: multilevel_ticks.ipynb`](https://matplotlib.org/stable/_downloads/4682a146596d1ac2bf1237e25e627854/multilevel_ticks.ipynb)

[`Download Python source code: multilevel_ticks.py`](https://matplotlib.org/stable/_downloads/3525cc5d1774b69b18d51894d36a5368/multilevel_ticks.py)

[`Download zipped: multilevel_ticks.zip`](https://matplotlib.org/stable/_downloads/a80943a536c67696432889a61a4d9574/multilevel_ticks.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)