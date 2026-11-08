[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.x.html#main-content)

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
    

Changes for 0.98.x[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.x.html#changes-for-0-98-x "Link to this heading")

============================================================================================================================================

*   `psd()`, `csd()`, and `cohere()` will now automatically wrap negative frequency components to the beginning of the returned arrays. This is much more sensible behavior and makes them consistent with `specgram()`. The previous behavior was more of an oversight than a design decision.
    
*   Added new keyword parameters _nonposx_, _nonposy_ to [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     methods that set log scale parameters. The default is still to mask out non-positive values, but the kwargs accept 'clip', which causes non-positive values to be replaced with a very small positive value.
    
*   Added new [`matplotlib.pyplot.fignum_exists()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fignum_exists.html#matplotlib.pyplot.fignum_exists "matplotlib.pyplot.fignum_exists")
     and [`matplotlib.pyplot.get_fignums()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums "matplotlib.pyplot.get_fignums")
    ; they merely expose information that had been hidden in `matplotlib._pylab_helpers`.
    
*   Deprecated numerix package.
    
*   Added new [`matplotlib.image.imsave()`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imsave "matplotlib.image.imsave")
     and exposed it to the [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     interface.
    
*   Remove support for pyExcelerator in exceltools -- use xlwt instead
    
*   Changed the defaults of acorr and xcorr to use usevlines=True, maxlags=10 and normed=True since these are the best defaults
    
*   Following keyword parameters for [`matplotlib.legend.Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
     are now deprecated and new set of parameters are introduced. The new parameters are given as a fraction of the font-size. Also, _scatteryoffsets_, _fancybox_ and _columnspacing_ are added as keyword parameters.
    
    | Deprecated | New |
    | --- | --- |
    | pad | borderpad |
    | labelsep | labelspacing |
    | handlelen | handlelength |
    | handlestextsep | handletextpad |
    | axespad | borderaxespad |
    
*   Removed the configobj and experimental traits rc support
    
*   Modified [`matplotlib.mlab.psd()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")
    , [`matplotlib.mlab.csd()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")
    , [`matplotlib.mlab.cohere()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.cohere "matplotlib.mlab.cohere")
    , and [`matplotlib.mlab.specgram()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")
     to scale one-sided densities by a factor of 2. Also, optionally scale the densities by the sampling frequency, which gives true values of densities that can be integrated by the returned frequency values. This also gives better MATLAB compatibility. The corresponding [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     methods and [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     functions were updated as well.
    
*   Font lookup now uses a nearest-neighbor approach rather than an exact match. Some fonts may be different in plots, but should be closer to what was requested.
    
*   [`matplotlib.axes.Axes.set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
    , [`matplotlib.axes.Axes.set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
     now return a copy of the `viewlim` array to avoid modify-in-place surprises.
    
*   `matplotlib.afm.AFM.get_fullname` and `matplotlib.afm.AFM.get_familyname` no longer raise an exception if the AFM file does not specify these optional attributes, but returns a guess based on the required FontName attribute.
    
*   Changed precision kwarg in [`matplotlib.pyplot.spy()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy "matplotlib.pyplot.spy")
    ; default is 0, and the string value 'present' is used for sparse arrays only to show filled locations.
    
*   [`matplotlib.collections.EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
     added.
    
*   Added `angles` kwarg to [`matplotlib.pyplot.quiver()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
     for more flexible specification of the arrow angles.
    
*   Deprecated (raise NotImplementedError) all the mlab2 functions from [`matplotlib.mlab`](https://matplotlib.org/stable/api/mlab_api.html#module-matplotlib.mlab "matplotlib.mlab")
     out of concern that some of them were not clean room implementations.
    
*   Methods [`matplotlib.collections.Collection.get_offsets()`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_offsets "matplotlib.collections.Collection.get_offsets")
     and [`matplotlib.collections.Collection.set_offsets()`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets")
     added to [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
     base class.
    
*   `matplotlib.figure.Figure.figurePatch` renamed `matplotlib.figure.Figure.patch`; `matplotlib.axes.Axes.axesPatch` renamed `matplotlib.axes.Axes.patch`; `matplotlib.axes.Axes.axesFrame` renamed `matplotlib.axes.Axes.frame`. `matplotlib.axes.Axes.get_frame`, which returns `matplotlib.axes.Axes.patch`, is deprecated.
    
*   Changes in the [`matplotlib.contour.ContourLabeler`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler "matplotlib.contour.ContourLabeler")
     attributes ([`matplotlib.pyplot.clabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
     function) so that they all have a form like `.labelAttribute`. The three attributes that are most likely to be used by end users, `.cl`, `.cl_xy` and `.cl_cvalues` have been maintained for the moment (in addition to their renamed versions), but they are deprecated and will eventually be removed.
    
*   Moved several functions in [`matplotlib.mlab`](https://matplotlib.org/stable/api/mlab_api.html#module-matplotlib.mlab "matplotlib.mlab")
     and [`matplotlib.cbook`](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "matplotlib.cbook")
     into a separate module `matplotlib.numerical_methods` because they were unrelated to the initial purpose of mlab or cbook and appeared more coherent elsewhere.