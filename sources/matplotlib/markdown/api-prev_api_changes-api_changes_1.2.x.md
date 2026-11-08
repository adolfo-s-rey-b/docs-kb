[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.2.x.html#main-content)

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
    

API Changes in 1.2.x[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.2.x.html#api-changes-in-1-2-x "Link to this heading")

===============================================================================================================================================

*   The `classic` option of the rc parameter `toolbar` is deprecated and will be removed in the next release.
    
*   The `matplotlib.cbook.isvector` method has been removed since it is no longer functional.
    
*   The `rasterization_zorder` property on [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     sets a zorder below which artists are rasterized. This has defaulted to -30000.0, but it now defaults to _None_, meaning no artists will be rasterized. In order to rasterize artists below a given zorder value, [`set_rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder")
     must be explicitly called.
    
*   In [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    , and [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
    , when specifying a marker using a tuple, the angle is now specified in degrees, not radians.
    
*   Using [`twinx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
     or [`twiny()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html#matplotlib.axes.Axes.twiny "matplotlib.axes.Axes.twiny")
     no longer overrides the current locaters and formatters on the axes.
    
*   In [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
    , the handling of the _extend_ kwarg has changed. Formerly, the extended ranges were mapped after to 0, 1 after being normed, so that they always corresponded to the extreme values of the colormap. Now they are mapped outside this range so that they correspond to the special colormap values determined by the [`set_under()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")
     and [`set_over()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "matplotlib.colors.Colormap.set_over")
     methods, which default to the colormap end points.
    
*   The new rc parameter `savefig.format` replaces `cairo.format` and `savefig.extension`, and sets the default file format used by [`matplotlib.figure.Figure.savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
    .
    
*   In [`pyplot.pie()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
     and [`axes.Axes.pie()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
    , one can now set the radius of the pie; setting the _radius_ to 'None' (the default value), will result in a pie with a radius of 1 as before.
    
*   Use of `matplotlib.projections.projection_factory` is now deprecated in favour of axes class identification using `matplotlib.projections.process_projection_requirements` followed by direct axes class invocation (at the time of writing, functions which do this are: [`add_axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
    , [`add_subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
     and [`gca()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca")
    ). Therefore:
    
    key \= figure.\_make\_key(\*args, \*\*kwargs)
    ispolar \= kwargs.pop('polar', False)
    projection \= kwargs.pop('projection', None)
    if ispolar:
        if projection is not None and projection != 'polar':
            raise ValueError('polar and projection args are inconsistent')
        projection \= 'polar'
    ax \= projection\_factory(projection, self, rect, \*\*kwargs)
    key \= self.\_make\_key(\*args, \*\*kwargs)
    
    \# is now
    
    projection\_class, kwargs, key \= \\
                       process\_projection\_requirements(self, \*args, \*\*kwargs)
    ax \= projection\_class(self, rect, \*\*kwargs)
    
    This change means that third party objects can expose themselves as Matplotlib axes by providing a `_as_mpl_axes` method. See [`matplotlib.projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
     for more detail.
    
*   A new keyword _extendfrac_ in [`colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
     and [`ColorbarBase`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.ColorbarBase "matplotlib.colorbar.ColorbarBase")
     allows one to control the size of the triangular minimum and maximum extensions on colorbars.
    
*   A new keyword _capthick_ in [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
     has been added as an intuitive alias to the _markeredgewidth_ and _mew_ keyword arguments, which indirectly controlled the thickness of the caps on the errorbars. For backwards compatibility, specifying either of the original keyword arguments will override any value provided by _capthick_.
    
*   Transform subclassing behaviour is now subtly changed. If your transform implements a non-affine transformation, then it should override the `transform_non_affine` method, rather than the generic `transform` method. Previously transforms would define `transform` and then copy the method into `transform_non_affine`:
    
    class MyTransform(mtrans.Transform):
        def transform(self, xy):
            ...
        transform\_non\_affine \= transform
    
    This approach will no longer function correctly and should be changed to:
    
    class MyTransform(mtrans.Transform):
        def transform\_non\_affine(self, xy):
            ...
    
*   Artists no longer have `x_isdata` or `y_isdata` attributes; instead any artist's transform can be interrogated with `artist_instance.get_transform().contains_branch(ax.transData)`
    
*   Lines added to an axes now take into account their transform when updating the data and view limits. This means transforms can now be used as a pre-transform. For instance:
    
    \>>> import matplotlib.pyplot as plt
    \>>> import matplotlib.transforms as mtrans
    \>>> ax \= plt.axes()
    \>>> ax.plot(range(10), transform\=mtrans.Affine2D().scale(10) + ax.transData)
    \>>> print(ax.viewLim)
    Bbox('array(\[\[  0.,   0.\],\\n       \[ 90.,  90.\]\])')
    
*   One can now easily get a transform which goes from one transform's coordinate system to another, in an optimized way, using the new subtract method on a transform. For instance, to go from data coordinates to axes coordinates:
    
    \>>> import matplotlib.pyplot as plt
    \>>> ax \= plt.axes()
    \>>> data2ax \= ax.transData \- ax.transAxes
    \>>> print(ax.transData.depth, ax.transAxes.depth)
    3, 1
    \>>> print(data2ax.depth)
    2
    
    for versions before 1.2 this could only be achieved in a sub-optimal way, using `ax.transData + ax.transAxes.inverted()` (depth is a new concept, but had it existed it would return 4 for this example).
    
*   `twinx` and `twiny` now returns an instance of SubplotBase if parent axes is an instance of SubplotBase.
    
*   All Qt3-based backends are now deprecated due to the lack of py3k bindings. Qt and QtAgg backends will continue to work in v1.2.x for py2.6 and py2.7. It is anticipated that the Qt3 support will be completely removed for the next release.
    
*   `matplotlib.colors.ColorConverter`, [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
     and [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     now subclasses `object`
    
*   ContourSet instances no longer have a `transform` attribute. Instead, access the transform with the `get_transform` method.