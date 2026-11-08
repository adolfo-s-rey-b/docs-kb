[Skip to main content](https://matplotlib.org/stable/users/faq.html#main-content)

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
    

Frequently Asked Questions[#](https://matplotlib.org/stable/users/faq.html#frequently-asked-questions "Link to this heading")

==============================================================================================================================

I don't see a figure window[#](https://matplotlib.org/stable/users/faq.html#i-don-t-see-a-figure-window "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Please see [Debugging the figure windows not showing](https://matplotlib.org/stable/users/explain/figure/backends.html#figures-not-showing)
.

Why do I have so many ticks, and/or why are they out of order?[#](https://matplotlib.org/stable/users/faq.html#why-do-i-have-so-many-ticks-and-or-why-are-they-out-of-order "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

One common cause for unexpected tick behavior is passing a _list of strings instead of numbers or datetime objects_. This can easily happen without notice when reading in a comma-delimited text file. Matplotlib treats lists of strings as _categorical_ variables ([Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)
), and by default puts one tick per category, and plots them in the order in which they are supplied.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots(1, 2, layout\='constrained', figsize\=(6, 2))

ax\[0\].set\_title('Ticks seem out of order / misplaced')
x \= \['5', '20', '1', '9'\]  \# strings
y \= \[5, 20, 1, 9\]
ax\[0\].plot(x, y, 'd')
ax\[0\].tick\_params(axis\='x', labelcolor\='red', labelsize\=14)

ax\[1\].set\_title('Many ticks')
x \= \[str(xx) for xx in np.arange(100)\]  \# strings
y \= np.arange(100)
ax\[1\].plot(x, y)
ax\[1\].tick\_params(axis\='x', labelcolor\='red', labelsize\=14)

([`Source code`](https://matplotlib.org/stable/_downloads/5a1bd6b33d2fad4b4fde85b7d0324aa9/faq-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/156cbc0e2a724bcbf8ea4dfbca668dcd/faq-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e7ff1e5d25c51f435350824e98cb7d73/faq-1.png)
)

[![](https://matplotlib.org/stable/_images/users-faq-1.2x.png)](https://matplotlib.org/stable/_images/users-faq-1.2x.png)

The solution is to convert the list of strings to numbers or datetime objects (often `np.asarray(numeric_strings, dtype='float')` or `np.asarray(datetime_strings, dtype='datetime64[s]')`).

For more information see [Fixing too many ticks](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html)
.

Determine the extent of Artists in the Figure[#](https://matplotlib.org/stable/users/faq.html#determine-the-extent-of-artists-in-the-figure "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes we want to know the extent of an Artist. Matplotlib [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 objects have a method [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 that will usually return the extent of the artist in pixels. However, some artists, in particular text, must be rendered at least once before their extent is known. Matplotlib supplies [`Figure.draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
, which should be called before calling `get_window_extent`.

Check whether a figure is empty[#](https://matplotlib.org/stable/users/faq.html#check-whether-a-figure-is-empty "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Empty can actually mean different things. Does the figure contain any artists? Does a figure with an empty [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 still count as empty? Is the figure empty if it was rendered pure white (there may be artists present, but they could be outside the drawing area or transparent)?

For the purpose here, we define empty as: "The figure does not contain any artists except its background patch." The exception for the background is necessary, because by default every figure contains a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 as its background patch. This definition could be checked via:

def is\_empty(figure):
    """
    Return whether the figure contains no Artists (other than the default
    background patch).
    """
    contained\_artists \= figure.get\_children()
    return len(contained\_artists) <= 1

We've decided not to include this as a figure method because this is only one way of defining empty, and checking the above is only rarely necessary. Whether or not something has been added to the figure is usually defined within the context of the program.

The only reliable way to check whether a figure would render empty is to actually perform such a rendering and inspect the result.

Find all objects in a figure of a certain type[#](https://matplotlib.org/stable/users/faq.html#find-all-objects-in-a-figure-of-a-certain-type "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Every Matplotlib artist (see [Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html#artists-tutorial)
) has a method called [`findobj()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.findobj.html#matplotlib.artist.Artist.findobj "matplotlib.artist.Artist.findobj")
 that can be used to recursively search the artist for any artists it may contain that meet some criteria (e.g., match all [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances or match some arbitrary filter function). For example, the following snippet finds every object in the figure which has a `set_color` property and makes the object blue:

def myfunc(x):
    return hasattr(x, 'set\_color')

for o in fig.findobj(myfunc):
    o.set\_color('blue')

You can also filter on class instances:

import matplotlib.text as text
for o in fig.findobj(text.Text):
    o.set\_fontstyle('italic')

Prevent ticklabels from having an offset[#](https://matplotlib.org/stable/users/faq.html#prevent-ticklabels-from-having-an-offset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

The default formatter will use an offset to reduce the length of the ticklabels. To turn this feature off on a per-axis basis:

ax.xaxis.get\_major\_formatter().set\_useOffset(False)

set `[rcParams["axes.formatter.useoffset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.useoffset#rcparam-axes-formatter-useoffset) ` (default: `True`), or use a different formatter. See [`ticker`](https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker "matplotlib.ticker")
 for details.

Save transparent figures[#](https://matplotlib.org/stable/users/faq.html#save-transparent-figures "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The [`savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 command has a keyword argument _transparent_ which, if 'True', will make the figure and axes backgrounds transparent when saving, but will not affect the displayed image on the screen.

If you need finer grained control, e.g., you do not want full transparency or you want to affect the screen displayed version as well, you can set the alpha properties directly. The figure has a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 instance called _patch_ and the axes has a Rectangle instance called _patch_. You can set any property on them directly (_facecolor_, _edgecolor_, _linewidth_, _linestyle_, _alpha_). e.g.:

fig \= plt.figure()
fig.patch.set\_alpha(0.5)
ax \= fig.add\_subplot(111)
ax.patch.set\_alpha(0.5)

If you need _all_ the figure elements to be transparent, there is currently no global alpha setting, but you can set the alpha channel on individual elements, e.g.:

ax.plot(x, y, alpha\=0.5)
ax.set\_xlabel('volts', alpha\=0.5)

Save multiple plots to one pdf file[#](https://matplotlib.org/stable/users/faq.html#save-multiple-plots-to-one-pdf-file "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Many image file formats can only have one image per file, but some formats support multi-page files. Currently, Matplotlib only provides multi-page output to pdf files, using either the pdf or pgf backends, via the [`backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 and [`backend_pgf.PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
 classes.

Make room for tick labels[#](https://matplotlib.org/stable/users/faq.html#make-room-for-tick-labels "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

By default, Matplotlib uses fixed percentage margins around subplots. This can lead to labels overlapping or being cut off at the figure boundary. There are multiple ways to fix this:

*   Manually adapt the subplot parameters using [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
     / [`pyplot.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
    .
    
*   Use one of the automatic layout mechanisms:
    
    *   constrained layout ([Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
        )
        
    *   tight layout ([Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
        )
        
*   Calculate good values from the size of the plot elements yourself ([Programmatically control subplot adjustment](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html)
    )
    

Align my ylabels across multiple subplots[#](https://matplotlib.org/stable/users/faq.html#align-my-ylabels-across-multiple-subplots "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have multiple subplots over one another, and the y data have different scales, you can often get ylabels that do not align vertically across the multiple subplots, which can be unattractive. By default, Matplotlib positions the x location of the ylabel so that it does not overlap any of the y ticks. You can override this default behavior by specifying the coordinates of the label. To learn how, see [Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Control the draw order of plot elements[#](https://matplotlib.org/stable/users/faq.html#control-the-draw-order-of-plot-elements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

The draw order of plot elements, and thus which elements will be on top, is determined by the [`set_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder")
 property. See [Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)
 for a detailed description.

Make the aspect ratio for plots equal[#](https://matplotlib.org/stable/users/faq.html#make-the-aspect-ratio-for-plots-equal "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

The Axes property [`set_aspect()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
 controls the aspect ratio of the axes. You can set it to be 'auto', 'equal', or some ratio which controls the ratio:

ax \= fig.add\_subplot(111, aspect\='equal')

See [Equal axis aspect ratio](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html)
 for a complete example.

Draw multiple y-axis scales[#](https://matplotlib.org/stable/users/faq.html#draw-multiple-y-axis-scales "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

A frequent request is to have two scales for the left and right y-axis, which is possible using [`twinx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twinx.html#matplotlib.pyplot.twinx "matplotlib.pyplot.twinx")
 (more than two scales are not currently supported, though it is on the wish list). This works pretty well, though there are some quirks when you are trying to interactively pan and zoom, because both scales do not get the signals.

The approach uses [`twinx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twinx.html#matplotlib.pyplot.twinx "matplotlib.pyplot.twinx")
 (and its sister [`twiny()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twiny.html#matplotlib.pyplot.twiny "matplotlib.pyplot.twiny")
) to use _2 different axes_, turning the axes rectangular frame off on the 2nd axes to keep it from obscuring the first, and manually setting the tick locs and labels as desired. You can use separate `matplotlib.ticker` formatters and locators as desired because the two axes are independent.

([`Source code`](https://matplotlib.org/stable/_downloads/44b5432bcc59ab8b9b8a6545b0ae281f/faq-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5b35eae77b9d97177298700c52e5d640/faq-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f55704b6a74aaf141da69633eba9787e/faq-2.png)
)

[![](https://matplotlib.org/stable/_images/users-faq-2.2x.png)](https://matplotlib.org/stable/_images/users-faq-2.2x.png)

See [Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
 for a complete example.

Generate images without having a window appear[#](https://matplotlib.org/stable/users/faq.html#generate-images-without-having-a-window-appear "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The recommended approach since Matplotlib 3.1 is to explicitly create a Figure instance:

from matplotlib.figure import Figure
fig \= Figure()
ax \= fig.subplots()
ax.plot(\[1, 2, 3\])
fig.savefig('myfig.png')

This prevents any interaction with GUI frameworks and the window manager.

It's alternatively still possible to use the pyplot interface: instead of calling [`matplotlib.pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
, call [`matplotlib.pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
. In that case, you must close the figure after saving it. Not closing the figure causes a memory leak, because pyplot keeps references to all not-yet-shown figures.

import matplotlib.pyplot as plt
plt.plot(\[1, 2, 3\])
plt.savefig('myfig.png')
plt.close()

See also

[Embed in a web application server (Flask)](https://matplotlib.org/stable/gallery/user_interfaces/web_application_server_sgskip.html)
 for information about running matplotlib inside of a web application.

Work with threads[#](https://matplotlib.org/stable/users/faq.html#work-with-threads "Link to this heading")

------------------------------------------------------------------------------------------------------------

Matplotlib is not thread-safe: in fact, there are known race conditions that affect certain artists. Hence, if you work with threads, it is your responsibility to set up the proper locks to serialize access to Matplotlib artists.

You may be able to work on separate figures from separate threads. However, you must in that case use a _non-interactive backend_ (typically Agg), because most GUI backends _require_ being run from the main thread as well.

Get help[#](https://matplotlib.org/stable/users/faq.html#get-help "Link to this heading")

------------------------------------------------------------------------------------------

There are a number of good resources for getting help with Matplotlib. There is a good chance your question has already been asked:

*   The [mailing list archive](https://discourse.matplotlib.org/c/community/matplotlib-users/6)
    .
    
*   [GitHub issues](https://github.com/matplotlib/matplotlib/issues)
    .
    
*   Stackoverflow questions tagged [matplotlib](https://stackoverflow.com/questions/tagged/matplotlib)
    .
    

If you are unable to find an answer to your question through search, please provide the following information in your e-mail to the [mailing list](https://mail.python.org/mailman/listinfo/matplotlib-users)
:

*   Your operating system (Linux/Unix users: post the output of `uname -a`).
    
*   Matplotlib version:
    
    python \-c "import matplotlib; print(matplotlib.\_\_version\_\_)"
    
*   Where you obtained Matplotlib (e.g., your Linux distribution's packages, GitHub, PyPI, or [Anaconda](https://www.anaconda.com/)
    ).
    
*   Any customizations to your `matplotlibrc` file (see [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
    ).
    
*   If the problem is reproducible, please try to provide a _minimal_, standalone Python script that demonstrates the problem. This is _the_ critical step. If you can't post a piece of code that we can run and reproduce your error, the chances of getting help are significantly diminished. Very often, the mere act of trying to minimize your code to the smallest bit that produces the error will help you find a bug in _your_ code that is causing the problem.
    
*   Matplotlib provides debugging information through the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")
     library, and a helper function to set the logging level: one can call
    
    plt.set\_loglevel("INFO")  \# or "DEBUG" for more info
    
    to obtain this debugging information.
    
    Standard functions from the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")
     module are also applicable; e.g. one could call `logging.basicConfig(level="DEBUG")` even before importing Matplotlib (this is in particular necessary to get the logging info emitted during Matplotlib's import), or attach a custom handler to the "matplotlib" logger. This may be useful if you use a custom logging configuration.
    

If you compiled Matplotlib yourself, please also provide:

*   your compiler version -- e.g., `gcc --version`.
    
*   the output of:
    
    pip install \--verbose
    
    The beginning of the build output contains lots of details about your platform that are useful for the Matplotlib developers to diagnose your problem.
    

If you compiled an older version of Matplotlib using the pre-Meson build system, instead provide:

*   any changes you have made to `setup.py`/`setupext.py`,
    
*   the output of:
    
    rm \-rf build
    python setup.py build
    

Including this information in your first e-mail to the mailing list will save a lot of time.

You will likely get a faster response writing to the mailing list than filing a bug in the bug tracker. Most developers check the bug tracker only periodically. If your problem has been determined to be a bug and cannot be quickly solved, you may be asked to file a bug in the tracker so the issue doesn't get lost.

On this page