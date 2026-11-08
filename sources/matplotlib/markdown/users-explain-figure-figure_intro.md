[Skip to main content](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#main-content)

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
    

Introduction to Figures[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#introduction-to-figures "Link to this heading")

================================================================================================================================================

fig \= plt.figure(figsize\=(2, 2), facecolor\='lightskyblue',
                 layout\='constrained')
fig.suptitle('Figure')
ax \= fig.add\_subplot()
ax.set\_title('Axes', loc\='left', fontstyle\='oblique', fontsize\='medium')

([`Source code`](https://matplotlib.org/stable/_downloads/fe3eb619a0be641995de83bbadb31f16/figure_intro-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e2fbe22b037282fb4afdb23e16d55323/figure_intro-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/885ef77bf2c33e3f4c4b53677ea363cb/figure_intro-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-1.2x.png)

When looking at Matplotlib visualization, you are almost always looking at Artists placed on a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. In the example above, the figure is the blue region and [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 has added an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 artist to the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 (see [Parts of a Figure](https://matplotlib.org/stable/users/explain/quick_start.html#figure-parts)
). A more complicated visualization can add multiple Axes to the Figure, colorbars, legends, annotations, and the Axes themselves can have multiple Artists added to them (e.g. `ax.plot` or `ax.imshow`).

[Viewing Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id10)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#viewing-figures "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will discuss how to create Figures in more detail below, but first it is helpful to understand how to view a Figure. This varies based on how you are using Matplotlib, and what [Backend](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
 you are using.

### [Notebooks and IDEs](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id11)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#notebooks-and-ides "Link to this heading")

[![Image of figure generated in Jupyter Notebook with inline backend.](https://matplotlib.org/stable/_images/FigureInline.png)](https://matplotlib.org/stable/_images/FigureInline.png)

Screenshot of a [Jupyter Notebook](https://jupyter.org/)
, with a figure generated via the default [inline](https://github.com/ipython/matplotlib-inline)
 backend.[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id7 "Link to this image")

If you are using a Notebook (e.g. [Jupyter](https://jupyter.org/)
) or an IDE that renders Notebooks (PyCharm, VSCode, etc), then they have a backend that will render the Matplotlib Figure when a code cell is executed. The default Jupyter backend (`%matplotlib inline`) creates static plots that by default trim or expand the figure size to have a tight box around Artists added to the Figure (see [Saving Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#saving-figures)
, below). For interactive plots in Jupyter you will need to use an ipython "magic" like `%matplotlib widget` for the [ipympl](https://matplotlib.org/ipympl/)
 backend in `jupyter lab` or `notebook>=7`, or `%matplotlib notebook` for the Matplotlib [notebook](https://matplotlib.org/stable/users/explain/figure/interactive.html#jupyter-notebooks-jupyterlab)
 in `notebook<7` or `nbclassic`.

Note

The [ipympl](https://matplotlib.org/ipympl/)
 backend is in a separate package, see [Installing ipympl](https://matplotlib.org/stable/users/explain/figure/backends.html#ipympl-install)
.

[![Image of figure generated in Jupyter Notebook with notebook backend, including a toolbar.](https://matplotlib.org/stable/_images/FigureNotebook.png)](https://matplotlib.org/stable/_images/FigureNotebook.png)

Screenshot of a Jupyter Notebook with an interactive figure generated via the `%matplotlib notebook` magic. Users should also try the similar [widget](https://matplotlib.org/ipympl/)
 backend if using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
.[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id8 "Link to this image")

See also

[Interactive figures](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-figures)
.

### [Standalone scripts and interactive use](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id12)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#standalone-scripts-and-interactive-use "Link to this heading")

If the user is on a client with a windowing system, there are a number of [Backends](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
 that can be used to render the Figure to the screen, usually using a Python Qt, Tk, or Wx toolkit, or the native MacOS backend. These are typically chosen either in the user's [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
, or by calling, for example, `matplotlib.use('QtAgg')` at the beginning of a session or script.

[![Image of figure generated from a script via the QtAgg backend.](https://matplotlib.org/stable/_images/FigureQtAgg.png)](https://matplotlib.org/stable/_images/FigureQtAgg.png)

Screenshot of a Figure generated via a python script and shown using the QtAgg backend.[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id9 "Link to this image")

When run from a script, or interactively (e.g. from an [IPython shell](https://ipython.readthedocs.io/en/stable/)
) the Figure will not be shown until we call `plt.show()`. The Figure will appear in a new GUI window, and usually will have a toolbar with Zoom, Pan, and other tools for interacting with the Figure. By default, `plt.show()` blocks further interaction from the script or shell until the Figure window is closed, though that can be toggled off for some purposes. For more details, please see [Interactive mode](https://matplotlib.org/stable/users/explain/figure/interactive.html#controlling-interactive)
.

Note that if you are on a client that does not have access to a windowing system, the Figure will fallback to being drawn using the "Agg" backend, and cannot be viewed, though it can be [saved](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#saving-figures)
.

See also

[Interactive figures](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-figures)
.

[Creating Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id13)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#creating-figures "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By far the most common way to create a figure is using the [pyplot](https://matplotlib.org/stable/tutorials/pyplot.html#pyplot-tutorial)
 interface. As noted in [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
, the pyplot interface serves two purposes. One is to spin up the Backend and keep track of GUI windows. The other is a global state for Axes and Artists that allow a short-form API to plotting methods. In the example above, we use pyplot for the first purpose, and create the Figure object, `fig`. As a side effect `fig` is also added to pyplot's global state, and can be accessed via [`gcf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf")
.

Users typically want an Axes or a grid of Axes when they create a Figure, so in addition to [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, there are convenience methods that return both a Figure and some Axes. A simple grid of Axes can be achieved with [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 (which simply wraps [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
):

fig, axs \= plt.subplots(2, 2, figsize\=(4, 3), layout\='constrained')

([`Source code`](https://matplotlib.org/stable/_downloads/bb2713a8473eaff5f2de9a2eeb41dc4c/figure_intro-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d7d7f2ad2e3438a5f825edcda0a967ac/figure_intro-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/05e1df65d0ed01b1d6c3d68a6175a5c2/figure_intro-2.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-2.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-2.2x.png)

More complex grids can be achieved with [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 (which wraps [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
):

fig, axs \= plt.subplot\_mosaic(\[\['A', 'right'\], \['B', 'right'\]\],
                              figsize\=(4, 3), layout\='constrained')
for ax\_name, ax in axs.items():
    ax.text(0.5, 0.5, ax\_name, ha\='center', va\='center')

([`Source code`](https://matplotlib.org/stable/_downloads/91b412f845131bc816a423e9b446ddb0/figure_intro-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d9643f1989e7a555b16286301efff325/figure_intro-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d85323214861797e9cfc412f442000ba/figure_intro-3.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-3.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-3.2x.png)

Sometimes we want to have a nested layout in a Figure, with two or more sets of Axes that do not share the same subplot grid. We can use [`add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 or [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 to create virtual figures inside a parent Figure; see [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
 for more details.

fig \= plt.figure(layout\='constrained', facecolor\='lightskyblue')
fig.suptitle('Figure')
figL, figR \= fig.subfigures(1, 2)
figL.set\_facecolor('thistle')
axL \= figL.subplots(2, 1, sharex\=True)
axL\[1\].set\_xlabel('x \[m\]')
figL.suptitle('Left subfigure')
figR.set\_facecolor('paleturquoise')
axR \= figR.subplots(1, 2, sharey\=True)
axR\[0\].set\_title('Axes 1')
figR.suptitle('Right subfigure')

([`Source code`](https://matplotlib.org/stable/_downloads/6ac4020b6f0da02175f868398120a939/figure_intro-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/942876daa965acde69f73ecad3838cbd/figure_intro-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7638a6cf245028c9f4f79218f149d5e5/figure_intro-4.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-4.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-4.2x.png)

It is possible to directly instantiate a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance without using the pyplot interface. This is usually only necessary if you want to create your own GUI application or service that you do not want carrying the pyplot global state. See the embedding examples in [Embedding Matplotlib in graphical user interfaces](https://matplotlib.org/stable/gallery/user_interfaces/index.html#user-interfaces)
 for examples of how to do this.

### [Figure options](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id14)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-options "Link to this heading")

There are a few options available when creating figures. The Figure size on the screen is set by _figsize_ and _dpi_. _figsize_ is the `(width, height)` of the Figure in inches (or, if preferred, units of 72 typographic points). _dpi_ are how many pixels per inch the figure will be rendered at. To make your Figures appear on the screen at the physical size you requested, you should set _dpi_ to the same _dpi_ as your graphics system. Note that many graphics systems now use a "dpi ratio" to specify how many screen pixels are used to represent a graphics pixel. Matplotlib applies the dpi ratio to the _dpi_ passed to the figure to make it have higher resolution, so you should pass the lower number to the figure.

The _facecolor_, _edgecolor_, _linewidth_, and _frameon_ options all change the appearance of the figure in expected ways, with _frameon_ making the figure transparent if set to _False_.

Finally, the user can specify a layout engine for the figure with the _layout_ parameter. Currently Matplotlib supplies ["constrained"](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
, ["compressed"](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#compressed-layout)
 and ["tight"](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
 layout engines. These rescale axes inside the Figure to prevent overlap of ticklabels, and try and align axes, and can save significant manual adjustment of artists on a Figure for many common cases.

### [Adding Artists](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id15)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#adding-artists "Link to this heading")

The [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class has a number of methods for adding artists to a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
. By far the most common are to add Axes of various configurations ([`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
, [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
, [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
, [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
) and subfigures ([`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
). Colorbars are added to Axes or group of Axes at the Figure level ([`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
). It is also possible to have a Figure-level legend ([`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
). Other Artists include figure-wide labels ([`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
, [`supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel")
, [`supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel")
) and text ([`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
). Finally, low-level Artists can be added directly using [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 usually with care being taken to use the appropriate transform. Usually these include `Figure.transFigure` which ranges from 0 to 1 in each direction, and represents the fraction of the current Figure size, or `Figure.dpi_scale_trans` which will be in physical units of inches from the bottom left corner of the Figure (see [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
 for more details).

[Saving Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#id16)
[#](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#saving-figures "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, Figures can be saved to disk using the [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 method. `fig.savefig('MyFigure.png', dpi=200)` will save a PNG formatted figure to the file `MyFigure.png` in the current directory on disk with 200 dots-per-inch resolution. Note that the filename can include a relative or absolute path to any place on the file system.

Many types of output are supported, including raster formats like PNG, GIF, JPEG, TIFF and vector formats like PDF, EPS, and SVG.

By default, the size of the saved Figure is set by the Figure size (in inches) and, for the raster formats, the _dpi_. If _dpi_ is not set, then the _dpi_ of the Figure is used. Note that _dpi_ still has meaning for vector formats like PDF if the Figure includes Artists that have been [rasterized](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
; the _dpi_ specified will be the resolution of the rasterized objects.

It is possible to change the size of the Figure using the _bbox\_inches_ argument to savefig. This can be specified manually, again in inches. However, by far the most common use is `bbox_inches='tight'`. This option "shrink-wraps", trimming or expanding as needed, the size of the figure so that it is tight around all the artists in a figure, with a small pad that can be specified by _pad\_inches_, which defaults to 0.1 inches. The dashed box in the plot below shows the portion of the figure that would be saved if `bbox_inches='tight'` were used in savefig.

([`Source code`](https://matplotlib.org/stable/_downloads/85c147b6446efd4b87a2e3040efdcbd8/figure_intro-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/8b3496e04092dd357c86dbff14d3e86a/figure_intro-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/acd92db5db80c16ad46152e69561cc6b/figure_intro-5.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-5.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-figure_intro-5.2x.png)

On this page