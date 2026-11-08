[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#main-content)

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
    

What's new in Matplotlib 2.2 (Mar 06, 2018)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#what-s-new-in-matplotlib-2-2-mar-06-2018 "Link to this heading")

========================================================================================================================================================================================

Constrained Layout Manager[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#constrained-layout-manager "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

Constrained Layout is **experimental**. The behaviour and API are subject to change, or the whole functionality may be removed without a deprecation period.

A new method to automatically decide spacing between subplots and their organizing `GridSpec` instances has been added. It is meant to replace the venerable `tight_layout` method. It is invoked via a new `constrained_layout=True` kwarg to [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
.

There are new [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 for this package, and spacing can be more finely tuned with the new [`set_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "matplotlib.figure.Figure.set_constrained_layout_pads")
.

Features include:

*   Automatic spacing for subplots with a fixed-size padding in inches around subplots and all their decorators, and space between as a fraction of subplot size between subplots.
    
*   Spacing for [`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
    , and colorbars that are attached to more than one axes.
    
*   Nested [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
     layouts using [`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
    .
    

For more details and capabilities please see the new tutorial: [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)

Note the new API to access this:

### New `plt.figure` and `plt.subplots` kwarg: `constrained_layout`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#new-plt-figure-and-plt-subplots-kwarg-constrained-layout "Link to this heading")

[`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 and [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 can now be called with `constrained_layout=True` kwarg to enable constrained\_layout.

### New `ax.set_position` behaviour[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#new-ax-set-position-behaviour "Link to this heading")

[`Axes.set_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position")
 now makes the specified axis no longer responsive to `constrained_layout`, consistent with the idea that the user wants to place an axis manually.

Internally, this means that old `ax.set_position` calls _inside_ the library are changed to private `ax._set_position` calls so that `constrained_layout` will still work with these axes.

### New `figure` kwarg for `GridSpec`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#new-figure-kwarg-for-gridspec "Link to this heading")

In order to facilitate `constrained_layout`, `GridSpec` now accepts a `figure` keyword. This is backwards compatible, in that not supplying this will simply cause `constrained_layout` to not operate on the subplots organized by this `GridSpec` instance. Routines that use `GridSpec` (e.g. `fig.subplots`) have been modified to pass the figure to `GridSpec`.

xlabels and ylabels can now be automatically aligned[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#xlabels-and-ylabels-can-now-be-automatically-aligned "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Subplot axes `ylabels` can be misaligned horizontally if the tick labels are very different widths. The same can happen to `xlabels` if the ticklabels are rotated on one subplot (for instance). The new methods on the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class: [`Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")
 and [`Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")
 will now align these labels horizontally or vertically. If the user only wants to align some axes, a list of axes can be passed. If no list is passed, the algorithm looks at all the labels on the figure.

Only labels that have the same subplot locations are aligned. i.e. the ylabels are aligned only if the subplots are in the same column of the subplot layout.

Alignment is persistent and automatic after these are called.

A convenience wrapper [`Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")
 calls both functions at once.

([`Source code`](https://matplotlib.org/stable/_downloads/b6cdbfb7be9560f41c55b29ec7ea3b73/whats_new_2-2-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/feb389cb12e47b0e2d28e9388a64a095/whats_new_2-2-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/82fcbf5882c88646759bcc56b3f4a567/whats_new_2-2-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-2-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-2-1.2x.png)

Axes legends now included in tight\_bbox[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#axes-legends-now-included-in-tight-bbox "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legends created via `ax.legend` can sometimes overspill the limits of the axis. Tools like `fig.tight_layout()` and `fig.savefig(bbox_inches='tight')` would clip these legends. A change was made to include them in the `tight` calculations.

Cividis colormap[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#cividis-colormap "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

A new dark blue/yellow colormap named 'cividis' was added. Like viridis, cividis is perceptually uniform and colorblind friendly. However, cividis also goes a step further: not only is it usable by colorblind users, it should actually look effectively identical to colorblind and non-colorblind users. For more details see [Nuñez J, Anderton C, and Renslow R: "Optimizing colormaps with consideration for color vision deficiency to enable accurate interpretation of scientific data"](https://doi.org/10.1371/journal.pone.0199239)
.

([`Source code`](https://matplotlib.org/stable/_downloads/046f1c80c0109fac5b0bf8b9004449e5/whats_new_2-2-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/bb1798dd4e4c39043f1066eff754d3ec/whats_new_2-2-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c84b6a7cc7d85cb4912f5edbbd5c244c/whats_new_2-2-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-2-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-2-2.2x.png)

New style colorblind-friendly color cycle[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#new-style-colorblind-friendly-color-cycle "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new style defining a color cycle has been added, tableau-colorblind10, to provide another option for colorblind-friendly plots. A demonstration of this new style can be found in the [reference](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html)
 of style sheets. To load this color cycle in place of the default one:

import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

Support for numpy.datetime64[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#support-for-numpy-datetime64 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib has supported [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 dates for a long time in [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
. We now support [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 dates as well. Anywhere that [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 could be used, [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 can be used. eg:

time \= np.arange('2005-02-01', '2005-02-02', dtype\='datetime64\[h\]')
plt.plot(time)

Writing animations with Pillow[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#writing-animations-with-pillow "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

It is now possible to use Pillow as an animation writer. Supported output formats are currently gif (Pillow>=3.4) and webp (Pillow>=5.0). Use e.g. as

from \_\_future\_\_ import division

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

fig, ax \= plt.subplots()
line, \= plt.plot(\[0, 1\])

def animate(i):
   line.set\_ydata(\[0, i / 20\])
   return \[line\]

anim \= FuncAnimation(fig, animate, 20, blit\=True)
anim.save("movie.gif", writer\=PillowWriter(fps\=24))
plt.show()

Slider UI widget can snap to discrete values[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#slider-ui-widget-can-snap-to-discrete-values "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The slider UI widget can take the optional argument _valstep_. Doing so forces the slider to take on only discrete values, starting from _valmin_ and counting up to _valmax_ with steps of size _valstep_.

If _closedmax==True_, then the slider will snap to _valmax_ as well.

`capstyle` and `joinstyle` attributes added to [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#capstyle-and-joinstyle-attributes-added-to-collection "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 class now has customizable `capstyle` and `joinstyle` attributes. This allows the user for example to set the `capstyle` of errorbars.

_pad_ kwarg added to ax.set\_title[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#pad-kwarg-added-to-ax-set-title "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The method [`Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
 now has a _pad_ kwarg, that specifies the distance from the top of an axes to where the title is drawn. The units of _pad_ is points, and the default is the value of the (already-existing) `[rcParams["axes.titlepad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlepad#rcparam-axes-titlepad) ` (default: `6.0`).

Comparison of 2 colors in Matplotlib[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#comparison-of-2-colors-in-matplotlib "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As the colors in Matplotlib can be specified with a wide variety of ways, the [`matplotlib.colors.same_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.same_color.html#matplotlib.colors.same_color "matplotlib.colors.same_color")
 method has been added which checks if two [`colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
 are the same.

Autoscaling a polar plot snaps to the origin[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#autoscaling-a-polar-plot-snaps-to-the-origin "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setting the limits automatically in a polar plot now snaps the radial limit to zero if the automatic limit is nearby. This means plotting from zero doesn't automatically scale to include small negative values on the radial axis.

The limits can still be set manually in the usual way using [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

PathLike support[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#pathlike-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

On Python 3.6+, [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
, [`imsave`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave "matplotlib.pyplot.imsave")
, [`imread`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread")
, and animation writers now accept [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
s as input.

[`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 can set gridline properties[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#axes-tick-params-can-set-gridline-properties "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
 objects hold gridlines as well as the tick mark and its label. [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
, [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 and [`pyplot.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")
 now have keyword arguments 'grid\_color', 'grid\_alpha', 'grid\_linewidth', and 'grid\_linestyle' for overriding the defaults in [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
: 'grid.color', etc.

[`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 clips RGB values to the valid range[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#axes-imshow-clips-rgb-values-to-the-valid-range "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 is passed an RGB or RGBA value with out-of-range values, it now logs a warning and clips them to the valid range. The old behaviour, wrapping back in to the range, often hid outliers and made interpreting RGB images unreliable.

Properties in `matplotlibrc` to place xaxis and yaxis tick labels[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#properties-in-matplotlibrc-to-place-xaxis-and-yaxis-tick-labels "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Introducing four new boolean properties in `matplotlibrc` for default positions of xaxis and yaxis tick labels, namely, `[rcParams["xtick.labeltop"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.labeltop#rcparam-xtick-labeltop) ` (default: `False`), `[rcParams["xtick.labelbottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.labelbottom#rcparam-xtick-labelbottom) ` (default: `True`), `[rcParams["ytick.labelright"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.labelright#rcparam-ytick-labelright) ` (default: `False`) and `[rcParams["ytick.labelleft"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.labelleft#rcparam-ytick-labelleft) ` (default: `True`). These can also be changed in rcParams.

PGI bindings for gtk3[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#pgi-bindings-for-gtk3 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

The GTK3 backends can now use [PGI](https://pgi.readthedocs.io/en/latest/)
 instead of [PyGObject](https://pygobject.readthedocs.io/en/latest/)
. PGI is a fairly incomplete binding for GObject, thus its use is not recommended; its main benefit is its availability on Travis (thus allowing CI testing for the gtk3agg and gtk3cairo backends).

The binding selection rules are as follows: - if `gi` has already been imported, use it; else - if `pgi` has already been imported, use it; else - if `gi` can be imported, use it; else - if `pgi` can be imported, use it; else - error out.

Thus, to force usage of PGI when both bindings are installed, import it first.

Cairo rendering for Qt, WX, and Tk canvases[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#cairo-rendering-for-qt-wx-and-tk-canvases "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The new `Qt4Cairo`, `Qt5Cairo`, `WXCairo`, and `TkCairo` backends allow Qt, Wx, and Tk canvases to use Cairo rendering instead of Agg.

Added support for QT in new ToolManager[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#added-support-for-qt-in-new-toolmanager "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now it is possible to use the ToolManager with Qt5 For example:

import matplotlib

matplotlib.use('QT5AGG')
matplotlib.rcParams\['toolbar'\] \= 'toolmanager'
import matplotlib.pyplot as plt

plt.plot(\[1,2,3\])
plt.show()

Treat the new Tool classes experimental for now, the API will likely change and perhaps the rcParam as well

The main example [Tool Manager](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html)
 shows more details, just adjust the header to use QT instead of GTK3

TkAgg backend reworked to support PyPy[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#tkagg-backend-reworked-to-support-pypy "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[PyPy](https://www.pypy.org/)
 can now plot using the TkAgg backend, supported on PyPy 5.9 and greater (both PyPy for python 2.7 and PyPy for python 3.5).

Python logging library used for debug output[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#python-logging-library-used-for-debug-output "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib has in the past (sporadically) used an internal verbose-output reporter. This version converts those calls to using the standard python [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")
 library.

Support for the old [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 `verbose.level` and `verbose.fileo` is dropped.

The command-line options `--verbose-helpful` and `--verbose-debug` are still accepted, but deprecated. They are now equivalent to setting `logging.INFO` and `logging.DEBUG`.

The logger's root name is `matplotlib` and can be accessed from programs as:

import logging
mlog \= logging.getLogger('matplotlib')

Instructions for basic usage are in [Troubleshooting](https://matplotlib.org/stable/devel/troubleshooting.html#troubleshooting-faq)
 and for developers in [Contributing guide](https://matplotlib.org/stable/devel/contribute.html#contributing)
.

Improved [`repr`](https://docs.python.org/3/library/functions.html#repr "(in Python v3.14)")
 for [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
s[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.2.html#improved-repr-for-transforms "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
s now indent their [`repr`](https://docs.python.org/3/library/functions.html#repr "(in Python v3.14)")
s in a more legible manner:

In \[1\]: l, \= plt.plot(\[\]); l.get\_transform()
Out\[1\]:
CompositeGenericTransform(
   TransformWrapper(
      BlendedAffine2D(
            IdentityTransform(),
            IdentityTransform())),
   CompositeGenericTransform(
      BboxTransformFrom(
            TransformedBbox(
               Bbox(x0=-0.05500000000000001, y0=-0.05500000000000001, x1=0.05500000000000001, y1=0.05500000000000001),
               TransformWrapper(
                  BlendedAffine2D(
                        IdentityTransform(),
                        IdentityTransform())))),
      BboxTransformTo(
            TransformedBbox(
               Bbox(x0=0.125, y0=0.10999999999999999, x1=0.9, y1=0.88),
               BboxTransformTo(
                  TransformedBbox(
                        Bbox(x0=0.0, y0=0.0, x1=6.4, y1=4.8),
                        Affine2D(
                           \[\[ 100.    0.    0.\]\
                           \[   0.  100.    0.\]\
                           \[   0.    0.    1.\]\])))))))

On this page