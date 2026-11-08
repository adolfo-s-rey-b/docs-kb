[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.4.x.html#main-content)

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
    

API Changes in 1.4.x[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.4.x.html#api-changes-in-1-4-x "Link to this heading")

===============================================================================================================================================

Code changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.4.x.html#code-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   A major refactoring of the axes module was made. The axes module has been split into smaller modules:
    
    *   the `_base` module, which contains a new private `_AxesBase` class. This class contains all methods except plotting and labelling methods.
        
    *   the [`axes`](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes "matplotlib.axes")
         module, which contains the [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
         class. This class inherits from `_AxesBase`, and contains all plotting and labelling methods.
        
    *   the `_subplot` module, with all the classes concerning subplotting.
        
    
    There are a couple of things that do not exists in the [`axes`](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes "matplotlib.axes")
     module's namespace anymore. If you use them, you need to import them from their original location:
    
    *   `math` -> `import math`
        
    *   `ma` -> `from numpy import ma`
        
    *   `cbook` -> `from matplotlib import cbook`
        
    *   `docstring` -> `from matplotlib import docstring`
        
    *   `is_sequence_of_strings` -> `from matplotlib.cbook import is_sequence_of_strings`
        
    *   `is_string_like` -> `from matplotlib.cbook import is_string_like`
        
    *   `iterable` -> `from matplotlib.cbook import iterable`
        
    *   `itertools` -> `import itertools`
        
    *   `martist` -> `from matplotlib import artist as martist`
        
    *   `matplotlib` -> `import matplotlib`
        
    *   `mcoll` -> `from matplotlib import collections as mcoll`
        
    *   `mcolors` -> `from matplotlib import colors as mcolors`
        
    *   `mcontour` -> `from matplotlib import contour as mcontour`
        
    *   `mpatches` -> `from matplotlib import patches as mpatches`
        
    *   `mpath` -> `from matplotlib import path as mpath`
        
    *   `mquiver` -> `from matplotlib import quiver as mquiver`
        
    *   `mstack` -> `from matplotlib import stack as mstack`
        
    *   `mstream` -> `from matplotlib import stream as mstream`
        
    *   `mtable` -> `from matplotlib import table as mtable`
        
*   As part of the refactoring to enable Qt5 support, the module `matplotlib.backends.qt4_compat` was renamed to `matplotlib.backends.qt_compat`. `qt4_compat` is deprecated in 1.4 and will be removed in 1.5.
    
*   The [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
     method has been changed such that the upper and lower limits (_lolims_, _uplims_, _xlolims_, _xuplims_) now point in the correct direction.
    
*   The _fmt_ kwarg for [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
     now supports the string 'none' to suppress drawing of a line and markers; use of the _None_ object for this is deprecated. The default _fmt_ value is changed to the empty string (''), so the line and markers are governed by the [`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
     defaults.
    
*   A bug has been fixed in the path effects rendering of fonts, which now means that the font size is consistent with non-path effect fonts. See [matplotlib/matplotlib#2889](https://github.com/matplotlib/matplotlib/issues/2889)
     for more detail.
    
*   The Sphinx extensions `ipython_directive` and `ipython_console_highlighting` have been moved to the IPython project itself. While they remain in Matplotlib for this release, they have been deprecated. Update your extensions in `conf.py` to point to `IPython.sphinxext.ipython_directive` instead of `matplotlib.sphinxext.ipython_directive`.
    
*   In `matplotlib.finance`, almost all functions have been deprecated and replaced with a pair of functions name `*_ochl` and `*_ohlc`. The former is the 'open-close-high-low' order of quotes used previously in this module, and the latter is the 'open-high-low-close' order that is standard in finance.
    
*   For consistency the `face_alpha` keyword to [`matplotlib.patheffects.SimplePatchShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "matplotlib.patheffects.SimplePatchShadow")
     has been deprecated in favour of the `alpha` keyword. Similarly, the keyword `offset_xy` is now named `offset` across all [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")
    s. `matplotlib.patheffects._Base` has been renamed to [`matplotlib.patheffects.AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")
    . `matplotlib.patheffect.ProxyRenderer` has been renamed to [`matplotlib.patheffects.PathEffectRenderer`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer "matplotlib.patheffects.PathEffectRenderer")
     and is now a full RendererBase subclass.
    
*   The artist used to draw the outline of a [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     has been changed from a [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
     to [`matplotlib.patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
    , thus `colorbar.ColorbarBase.outline` is now a [`matplotlib.patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
     object.
    
*   The legend handler interface has changed from a callable, to any object which implements the `legend_artists` method (a deprecation phase will see this interface be maintained for v1.4). See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
     for further details. Further legend changes include:
    
    *   `matplotlib.axes.Axes._get_legend_handles` now returns a generator of handles, rather than a list.
        
    *   The [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
         function's _loc_ positional argument has been deprecated. Use the _loc_ keyword argument instead.
        
*   The `[rcParams["savefig.transparent"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.transparent#rcparam-savefig-transparent) ` (default: `False`) has been added to control default transparency when saving figures.
    
*   Slightly refactored the [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
     family. The text location in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
     is now entirely handled by the underlying [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
     object so `.set_position` works as expected. The attributes _xytext_ and _textcoords_ have been deprecated in favor of _xyann_ and _anncoords_ so that [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
     and [`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
     can share a common sensibly named api for getting/setting the location of the text or box.
    
    *   _xyann_ -> set the location of the annotation
        
    *   _xy_ -> set where the arrow points to
        
    *   _anncoords_ -> set the units of the annotation location
        
    *   _xycoords_ -> set the units of the point location
        
    *   `set_position()` -> [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
         only set location of annotation
        
*   [`matplotlib.mlab.specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")
    , [`matplotlib.mlab.psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")
    , [`matplotlib.mlab.csd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")
    , [`matplotlib.mlab.cohere`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.cohere "matplotlib.mlab.cohere")
    , `matplotlib.mlab.cohere_pairs`, [`matplotlib.pyplot.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram")
    , [`matplotlib.pyplot.psd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd "matplotlib.pyplot.psd")
    , [`matplotlib.pyplot.csd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.csd.html#matplotlib.pyplot.csd "matplotlib.pyplot.csd")
    , and [`matplotlib.pyplot.cohere`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cohere.html#matplotlib.pyplot.cohere "matplotlib.pyplot.cohere")
     now raise ValueError where they previously raised AssertionError.
    
*   For [`matplotlib.mlab.psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")
    , [`matplotlib.mlab.csd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")
    , [`matplotlib.mlab.cohere`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.cohere "matplotlib.mlab.cohere")
    , `matplotlib.mlab.cohere_pairs`, [`matplotlib.pyplot.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram")
    , [`matplotlib.pyplot.psd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd "matplotlib.pyplot.psd")
    , [`matplotlib.pyplot.csd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.csd.html#matplotlib.pyplot.csd "matplotlib.pyplot.csd")
    , and [`matplotlib.pyplot.cohere`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cohere.html#matplotlib.pyplot.cohere "matplotlib.pyplot.cohere")
    , in cases where a shape (n, 1) array is returned, this is now converted to a (n, ) array. Previously, (n, m) arrays were averaged to an (n, ) array, but (n, 1) arrays were returned unchanged. This change makes the dimensions consistent in both cases.
    
*   Added the `[rcParams["axes.formatter.useoffset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.useoffset#rcparam-axes-formatter-useoffset) ` (default: `True`) to control the default value of _useOffset_ in [`ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
    
*   Added [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
     sub-class [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
     which does the exact same thing as [`FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
    , but for new-style formatting strings.
    
*   Deprecated `matplotlib.testing.image_util` and the only function within, `matplotlib.testing.image_util.autocontrast`. These will be removed completely in v1.5.0.
    
*   The `fmt` argument of `Axes.plot_date` has been changed from `bo` to just `o`, so color cycling can happen by default.
    
*   Removed the class `FigureManagerQTAgg` and deprecated `NavigationToolbar2QTAgg` which will be removed in 1.5.
    
*   Removed formerly public (non-prefixed) attributes `rect` and `drawRect` from `FigureCanvasQTAgg`; they were always an implementation detail of the (preserved) `drawRectangle()` function.
    
*   The function signatures of `matplotlib.tight_bbox.adjust_bbox` and `matplotlib.tight_bbox.process_figure_for_rasterizing` have been changed. A new _fixed\_dpi_ parameter allows for overriding the `figure.dpi` setting instead of trying to deduce the intended behaviour from the file format.
    
*   Added support for horizontal/vertical axes padding to [`mpl_toolkits.axes_grid1.axes_grid.ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
     --- argument _axes\_pad_ can now be tuple-like if separate axis padding is required. The original behavior is preserved.
    
*   Added support for skewed transforms to [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    , which can be created using the [`skew`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew "matplotlib.transforms.Affine2D.skew")
     and [`skew_deg`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew_deg "matplotlib.transforms.Affine2D.skew_deg")
     methods.
    
*   Added clockwise parameter to control sectors direction in [`axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
    
*   In [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
     the _markevery_ functionality has been extended. Previously an integer start-index and stride-length could be specified using either a two-element-list or a two-element-tuple. Now this can only be done using a two-element-tuple. If a two-element-list is used then it will be treated as NumPy fancy indexing and only the two markers corresponding to the given indexes will be shown.
    
*   Removed _prop_ keyword argument from [`mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
     call. It was passed through to the base-class `__init__` and is only used for setting padding. Now _fontproperties_ (which is what is really used to set the font properties of [`AnchoredSizeBar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
    ) is passed through in place of _prop_. If _fontproperties_ is not passed in, but _prop_ is, then _prop_ is used in place of _fontproperties_. If both are passed in, _prop_ is silently ignored.
    
*   The use of the index 0 in [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
     and related commands is deprecated. Due to a lack of validation, calling `plt.subplots(2, 2, 0)` does not raise an exception, but puts an axes in the \_last\_ position. This is due to the indexing in subplot being 1-based (to mirror MATLAB) so before indexing into the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
     object used to determine where the axes should go, 1 is subtracted off. Passing in 0 results in passing -1 to [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
     which results in getting the last position back. Even though this behavior is clearly wrong and not intended, we are going through a deprecation cycle in an abundance of caution that any users are exploiting this 'feature'. The use of 0 as an index will raise a warning in 1.4 and an exception in 1.5.
    
*   Clipping is now off by default on offset boxes.
    
*   Matplotlib now uses a less-aggressive call to `gc.collect(1)` when closing figures to avoid major delays with large numbers of user objects in memory.
    
*   The default clip value of _all_ pie artists now defaults to `False`.
    

Code removal[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.4.x.html#code-removal "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   Removed `mlab.levypdf`. The code raised a NumPy error (and has for a long time) and was not the standard form of the Levy distribution. `scipy.stats.levy` should be used instead
    

On this page