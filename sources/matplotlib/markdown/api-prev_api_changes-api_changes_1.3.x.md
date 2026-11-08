[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#main-content)

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
    

API Changes in 1.3.x[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#api-changes-in-1-3-x "Link to this heading")

===============================================================================================================================================

Changes in 1.3.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#changes-in-1-3-1 "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

It is rare that we make an API change in a micro release, however, for 1.3.1 since 1.3.0 the following change was made:

*   `text.Text.cached` (used to cache font objects) has been made into a private variable. Among the obvious encapsulation benefit, this removes this confusing-looking member from the documentation.
    
*   The method [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     now always returns bin occupancies as an array of type [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
    . Previously, it was sometimes an array of type [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    , depending on the call.
    

Code removal[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#code-removal "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   The following items that were deprecated in version 1.2 or earlier have now been removed completely.
    
    *   The Qt 3.x backends (`qt` and `qtagg`) have been removed in favor of the Qt 4.x backends (`qt4` and `qt4agg`).
        
    *   The FltkAgg and Emf backends have been removed.
        
    *   The `matplotlib.nxutils` module has been removed. Use the functionality on [`matplotlib.path.Path.contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
         and friends instead.
        
    *   Instead of `axes.Axes.get_frame`, use `axes.Axes.patch`.
        
    *   The following keyword arguments to the [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
         function have been renamed:
        
        *   _pad_ -> _borderpad_
            
        *   _labelsep_ -> _labelspacing_
            
        *   _handlelen_ -> _handlelength_
            
        *   _handletextsep_ -> _handletextpad_
            
        *   _axespad_ -> _borderaxespad_
            
        
        Related to this, the following rcParams have been removed:
        
        *   `legend.pad`,
            
        *   `legend.labelsep`,
            
        *   `legend.handlelen`,
            
        *   `legend.handletextsep` and
            
        *   `legend.axespad`
            
    *   For the [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
         function, instead of _width_, use _rwidth_ (relative width).
        
    *   On [`patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
        , the _resolution_ keyword argument has been removed. For a circle made up of line segments, use [`patches.CirclePolygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.CirclePolygon.html#matplotlib.patches.CirclePolygon "matplotlib.patches.CirclePolygon")
        .
        
    *   The printing functions in the Wx backend have been removed due to the burden of keeping them up-to-date.
        
    *   `mlab.liaupunov` has been removed.
        
    *   `mlab.save`, `mlab.load`, `pylab.save` and `pylab.load` have been removed. We recommend using [`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "(in NumPy v2.5)")
         and [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "(in NumPy v2.5)")
         instead.
        
    *   `widgets.HorizontalSpanSelector` has been removed. Use [`widgets.SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")
         instead.
        

Code deprecation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#code-deprecation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

*   The CocoaAgg backend has been deprecated, with the possibility for deletion or resurrection in a future release.
    
*   The top-level functions in [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
     that are implemented in C++ were never meant to be public. Instead, users should use the Pythonic wrappers for them in the [`path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
     and [`collections.Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
     classes. Use the following mapping to update your code:
    
    *   `point_in_path` -> [`path.Path.contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
        
    *   `get_path_extents` -> [`path.Path.get_extents`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.get_extents "matplotlib.path.Path.get_extents")
        
    *   `point_in_path_collection` -> [`collections.Collection.contains`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.contains "matplotlib.collections.Collection.contains")
        
    *   `path_in_path` -> [`path.Path.contains_path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_path "matplotlib.path.Path.contains_path")
        
    *   `path_intersects_path` -> [`path.Path.intersects_path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_path "matplotlib.path.Path.intersects_path")
        
    *   `convert_path_to_polygons` -> [`path.Path.to_polygons`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.to_polygons "matplotlib.path.Path.to_polygons")
        
    *   `cleanup_path` -> [`path.Path.cleaned`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "matplotlib.path.Path.cleaned")
        
    *   `points_in_path` -> [`path.Path.contains_points`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_points "matplotlib.path.Path.contains_points")
        
    *   `clip_path_to_rect` -> [`path.Path.clip_to_bbox`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.clip_to_bbox "matplotlib.path.Path.clip_to_bbox")
        
*   `matplotlib.colors.normalize` and `matplotlib.colors.no_norm` have been deprecated in favour of [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     and [`matplotlib.colors.NoNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.NoNorm.html#matplotlib.colors.NoNorm "matplotlib.colors.NoNorm")
     respectively.
    
*   The [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
     class' `set_colorbar` method is now deprecated. Instead, the [`matplotlib.cm.ScalarMappable.colorbar`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.colorbar "matplotlib.cm.ScalarMappable.colorbar")
     attribute should be used. In previous Matplotlib versions this attribute was an undocumented tuple of `(colorbar_instance, colorbar_axes)` but is now just `colorbar_instance`. To get the colorbar axes it is possible to just use the `matplotlib.colorbar.ColorbarBase.ax` attribute on a colorbar instance.
    
*   The `matplotlib.mpl` module is now deprecated. Those who relied on this module should transition to simply using `import matplotlib as mpl`.
    

Code changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#code-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
     now fully supports using RGBA values for its `facecolor` and `edgecolor` attributes, which enables faces and edges to have different alpha values. If the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
     object's `alpha` attribute is set to anything other than `None`, that value will override any alpha-channel value in both the face and edge colors. Previously, if [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
     had `alpha=None`, the alpha component of `edgecolor` would be applied to both the edge and face.
    
*   The optional `isRGB` argument to [`set_foreground()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_foreground "matplotlib.backend_bases.GraphicsContextBase.set_foreground")
     (and the other GraphicsContext classes that descend from it) has been renamed to `isRGBA`, and should now only be set to `True` if the `fg` color argument is known to be an RGBA tuple.
    
*   For [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
    , the `capstyle` used is now `butt`, to be consistent with the default for most other objects, and to avoid problems with non-solid `linestyle` appearing solid when using a large `linewidth`. Previously, [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
     used `capstyle='projecting'`.
    
*   [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
     objects can now be marked as _readonly_ by passing `readonly=True` to its constructor. The built-in path singletons, obtained through `Path.unit*` class methods return readonly paths. If you have code that modified these, you will need to make a deepcopy first, using either:
    
    import copy
    path \= copy.deepcopy(Path.unit\_circle())
    
    \# or
    
    path \= Path.unit\_circle().deepcopy()
    
    Deep copying a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
     always creates an editable (i.e. non-readonly) [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    .
    
*   The list at `Path.NUM_VERTICES` was replaced by a dictionary mapping Path codes to the number of expected vertices at [`NUM_VERTICES_FOR_CODE`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.NUM_VERTICES_FOR_CODE "matplotlib.path.Path.NUM_VERTICES_FOR_CODE")
    .
    
*   To support XKCD style plots, the `matplotlib.path.cleanup_path` method's signature was updated to require a sketch argument. Users of `matplotlib.path.cleanup_path` are encouraged to use the new [`cleaned()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "matplotlib.path.Path.cleaned")
     Path method.
    
*   Data limits on a plot now start from a state of having "null" limits, rather than limits in the range (0, 1). This has an effect on artists that only control limits in one direction, such as [`axes.Axes.axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
     and [`axes.Axes.axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
    , since their limits will no longer also include the range (0, 1). This fixes some problems where the computed limits would be dependent on the order in which artists were added to the axes.
    
*   Fixed a bug in setting the position for the right/top spine with data position type. Previously, it would draw the right or top spine at +1 data offset.
    
*   In [`FancyArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
    , the default arrow head width, `head_width`, has been made larger to produce a visible arrow head. The new value of this kwarg is `head_width = 20 * width`.
    
*   It is now possible to provide `number of levels + 1` colors in the case of `extend='both'` for contourf (or just `number of levels` colors for an extend value `min` or `max`) such that the resulting colormap's `set_under` and `set_over` are defined appropriately. Any other number of colors will continue to behave as before (if more colors are provided than levels, the colors will be unused). A similar change has been applied to contour, where `extend='both'` would expect `number of levels + 2` colors.
    
*   A new keyword _extendrect_ in [`colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
     and [`ColorbarBase`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.ColorbarBase "matplotlib.colorbar.ColorbarBase")
     allows one to control the shape of colorbar extensions.
    
*   The extension of [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor")
     to both vertical (default) and/or horizontal cursor implied that `self.line` is replaced by `self.vline` for vertical cursors lines and `self.hline` is added for the horizontal cursors lines.
    
*   On POSIX platforms, the `matplotlib.cbook.report_memory` function raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(in Python v3.14)")
     instead of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.14)")
     if the **ps** command cannot be run.
    
*   The `matplotlib.cbook.check_output` function has been moved to `matplotlib.compat.subprocess`.
    

Configuration and rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#configuration-and-rcparams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

*   On Linux, the user-specific `matplotlibrc` configuration file is now located in `~/.config/matplotlib/matplotlibrc` to conform to the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
    .
    
*   The `font.*` rcParams now affect only text objects created after the rcParam has been set, and will not retroactively affect already existing text objects. This brings their behavior in line with most other rcParams.
    
*   Removed call of [`grid()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
     in `matplotlib.pyplot.plotfile`. To draw the axes grid, set the `axes.grid` rcParam to _True_, or explicitly call [`grid()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
    .
    

On this page