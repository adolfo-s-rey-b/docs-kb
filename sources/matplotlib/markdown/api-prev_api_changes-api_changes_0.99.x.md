[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.99.x.html#main-content)

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
    

Changes beyond 0.99.x[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.99.x.html#changes-beyond-0-99-x "Link to this heading")

==================================================================================================================================================

*   The default behavior of [`matplotlib.axes.Axes.set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
    , [`matplotlib.axes.Axes.set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
    , and [`matplotlib.axes.Axes.axis()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
    , and their corresponding pyplot functions, has been changed: when view limits are set explicitly with one of these methods, autoscaling is turned off for the matching axis. A new _auto_ kwarg is available to control this behavior. The limit kwargs have been renamed to _left_ and _right_ instead of _xmin_ and _xmax_, and _bottom_ and _top_ instead of _ymin_ and _ymax_. The old names may still be used, however.
    
*   There are five new Axes methods with corresponding pyplot functions to facilitate autoscaling, tick location, and tick label formatting, and the general appearance of ticks and tick labels:
    
    *   [`matplotlib.axes.Axes.autoscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
         turns autoscaling on or off, and applies it.
        
    *   [`matplotlib.axes.Axes.margins()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
         sets margins used to autoscale the `matplotlib.axes.Axes.viewLim` based on the `matplotlib.axes.Axes.dataLim`.
        
    *   [`matplotlib.axes.Axes.locator_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params")
         allows one to adjust axes locator parameters such as _nbins_.
        
    *   [`matplotlib.axes.Axes.ticklabel_format()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
         is a convenience method for controlling the [`matplotlib.ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
         that is used by default with linear axes.
        
    *   [`matplotlib.axes.Axes.tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
         controls direction, size, visibility, and color of ticks and their labels.
        
*   The [`matplotlib.axes.Axes.bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     method accepts a _error\_kw_ kwarg; it is a dictionary of kwargs to be passed to the errorbar function.
    
*   The [`matplotlib.axes.Axes.hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     _color_ kwarg now accepts a sequence of color specs to match a sequence of datasets.
    
*   The [`EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
     has been changed in two ways:
    
    *   There is a new _units_ option, 'xy', that scales the ellipse with the data units. This matches the :class:'~matplotlib.patches.Ellipse\` scaling.
        
    *   The _height_ and _width_ kwargs have been changed to specify the height and width, again for consistency with [`Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
        , and to better match their names; previously they specified the half-height and half-width.
        
*   There is a new rc parameter `axes.color_cycle`, and the color cycle is now independent of the rc parameter `lines.color`. `matplotlib.Axes.set_default_color_cycle` is deprecated.
    
*   You can now print several figures to one pdf file and modify the document information dictionary of a pdf file. See the docstrings of the class [`matplotlib.backends.backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
     for more information.
    
*   Removed [configobj](https://configobj.readthedocs.io/en/latest/)
     and [enthought.traits](http://code.enthought.com/pages/traits.html)
     packages, which are only required by the experimental traited config and are somewhat out of date. If needed, install them independently.
    

*   The new rc parameter `savefig.extension` sets the filename extension that is used by [`matplotlib.figure.Figure.savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
     if its _fname_ argument lacks an extension.
    
*   In an effort to simplify the backend API, all clipping rectangles and paths are now passed in using GraphicsContext objects, even on collections and images. Therefore:
    
    draw\_path\_collection(self, master\_transform, cliprect, clippath,
                         clippath\_trans, paths, all\_transforms, offsets,
                         offsetTrans, facecolors, edgecolors, linewidths,
                         linestyles, antialiaseds, urls)
    
    \# is now
    
    draw\_path\_collection(self, gc, master\_transform, paths, all\_transforms,
                         offsets, offsetTrans, facecolors, edgecolors,
                         linewidths, linestyles, antialiaseds, urls)
    
    draw\_quad\_mesh(self, master\_transform, cliprect, clippath,
                   clippath\_trans, meshWidth, meshHeight, coordinates,
                   offsets, offsetTrans, facecolors, antialiased,
                   showedges)
    
    \# is now
    
    draw\_quad\_mesh(self, gc, master\_transform, meshWidth, meshHeight,
                   coordinates, offsets, offsetTrans, facecolors,
                   antialiased, showedges)
    
    draw\_image(self, x, y, im, bbox, clippath\=None, clippath\_trans\=None)
    
    \# is now
    
    draw\_image(self, gc, x, y, im)
    
*   There are four new Axes methods with corresponding pyplot functions that deal with unstructured triangular grids:
    
    *   [`matplotlib.axes.Axes.tricontour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
         draws contour lines on a triangular grid.
        
    *   [`matplotlib.axes.Axes.tricontourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
         draws filled contours on a triangular grid.
        
    *   [`matplotlib.axes.Axes.tripcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tripcolor.html#matplotlib.axes.Axes.tripcolor "matplotlib.axes.Axes.tripcolor")
         draws a pseudocolor plot on a triangular grid.
        
    *   [`matplotlib.axes.Axes.triplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
         draws a triangular grid as lines and/or markers.