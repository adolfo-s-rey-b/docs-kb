[Skip to main content](https://matplotlib.org/stable/api/index.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html#)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

API Reference[#](https://matplotlib.org/stable/api/index.html#api-reference "Link to this heading")

====================================================================================================

Matplotlib interfaces[#](https://matplotlib.org/stable/api/index.html#matplotlib-interfaces "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Matplotlib has two interfaces. See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
 for a more detailed description of both and their recommended use cases.

**Axes interface** (object-based, explicit)

create a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 and one or more [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects, then _explicitly_ use methods on these objects to add data, configure limits, set labels etc.

API:

*   [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    : create Figure and Axes
    
*   [`axes`](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes "matplotlib.axes")
    : add data, limits, labels etc.
    
*   [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    : for figure-level methods
    

Example:

fig, ax \= plt.subplots()
ax.plot(x, y)
ax.set\_title("Sample plot")
plt.show()

**pyplot interface** (function-based, implicit)

consists of functions in the [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module. Figure and Axes are manipulated through these functions and are only _implicitly_ present in the background.

API:

*   [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
    

Example:

plt.plot(x, y)
plt.title("Sample plot")
plt.show()

Modules[#](https://matplotlib.org/stable/api/index.html#modules "Link to this heading")

----------------------------------------------------------------------------------------

Alphabetical list of modules:

*   [`matplotlib`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html)
    
*   [`matplotlib.animation`](https://matplotlib.org/stable/api/animation_api.html)
    
*   [`matplotlib.artist`](https://matplotlib.org/stable/api/artist_api.html)
    
*   [`matplotlib.axes`](https://matplotlib.org/stable/api/axes_api.html)
    
*   [`matplotlib.axis`](https://matplotlib.org/stable/api/axis_api.html)
    
*   [`matplotlib.backend_bases`](https://matplotlib.org/stable/api/backend_bases_api.html)
    
*   [`matplotlib.backend_managers`](https://matplotlib.org/stable/api/backend_managers_api.html)
    
*   [`matplotlib.backend_tools`](https://matplotlib.org/stable/api/backend_tools_api.html)
    
*   [`matplotlib.backends`](https://matplotlib.org/stable/api/index_backend_api.html)
    
*   [`matplotlib.bezier`](https://matplotlib.org/stable/api/bezier_api.html)
    
*   [`matplotlib.category`](https://matplotlib.org/stable/api/category_api.html)
    
*   [`matplotlib.cbook`](https://matplotlib.org/stable/api/cbook_api.html)
    
*   [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html)
    
*   [`matplotlib.collections`](https://matplotlib.org/stable/api/collections_api.html)
    
*   [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html)
    
*   [`matplotlib.colorizer`](https://matplotlib.org/stable/api/colorizer_api.html)
    
*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html)
    
*   [`matplotlib.container`](https://matplotlib.org/stable/api/container_api.html)
    
*   [`matplotlib.contour`](https://matplotlib.org/stable/api/contour_api.html)
    
*   [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html)
    
*   [`matplotlib.dviread`](https://matplotlib.org/stable/api/dviread.html)
    
*   [`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html)
    
*   [`matplotlib.font_manager`](https://matplotlib.org/stable/api/font_manager_api.html)
    
*   [`matplotlib.ft2font`](https://matplotlib.org/stable/api/ft2font.html)
    
*   [`matplotlib.gridspec`](https://matplotlib.org/stable/api/gridspec_api.html)
    
*   [`matplotlib.hatch`](https://matplotlib.org/stable/api/hatch_api.html)
    
*   [`matplotlib.image`](https://matplotlib.org/stable/api/image_api.html)
    
*   [`matplotlib.inset`](https://matplotlib.org/stable/api/inset_api.html)
    
*   [`matplotlib.layout_engine`](https://matplotlib.org/stable/api/layout_engine_api.html)
    
*   [`matplotlib.legend`](https://matplotlib.org/stable/api/legend_api.html)
    
*   [`matplotlib.legend_handler`](https://matplotlib.org/stable/api/legend_handler_api.html)
    
*   [`matplotlib.lines`](https://matplotlib.org/stable/api/lines_api.html)
    
*   [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html)
    
*   [`matplotlib.mathtext`](https://matplotlib.org/stable/api/mathtext_api.html)
    
*   [`matplotlib.mlab`](https://matplotlib.org/stable/api/mlab_api.html)
    
*   [`matplotlib.offsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html)
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html)
    
*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html)
    
*   [`matplotlib.patheffects`](https://matplotlib.org/stable/api/patheffects_api.html)
    
*   [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html)
    
*   [`matplotlib.projections`](https://matplotlib.org/stable/api/projections_api.html)
    
*   [`matplotlib.quiver`](https://matplotlib.org/stable/api/quiver_api.html)
    
*   [`matplotlib.rcsetup`](https://matplotlib.org/stable/api/rcsetup_api.html)
    
*   [`matplotlib.sankey`](https://matplotlib.org/stable/api/sankey_api.html)
    
*   [`matplotlib.scale`](https://matplotlib.org/stable/api/scale_api.html)
    
*   [`matplotlib.sphinxext.mathmpl`](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html)
    
*   [`matplotlib.sphinxext.plot_directive`](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html)
    
*   [`matplotlib.sphinxext.figmpl_directive`](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html)
    
*   [`matplotlib.sphinxext.roles`](https://matplotlib.org/stable/api/sphinxext_roles.html)
    
*   [`matplotlib.spines`](https://matplotlib.org/stable/api/spines_api.html)
    
*   [`matplotlib.style`](https://matplotlib.org/stable/api/style_api.html)
    
*   [`matplotlib.table`](https://matplotlib.org/stable/api/table_api.html)
    
*   [`matplotlib.testing`](https://matplotlib.org/stable/api/testing_api.html)
    
*   [`matplotlib.text`](https://matplotlib.org/stable/api/text_api.html)
    
*   [`matplotlib.texmanager`](https://matplotlib.org/stable/api/texmanager_api.html)
    
*   [`matplotlib.ticker`](https://matplotlib.org/stable/api/ticker_api.html)
    
*   [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html)
    
*   [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html)
    
*   [`matplotlib.typing`](https://matplotlib.org/stable/api/typing_api.html)
    
*   [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html)
    
*   [`matplotlib.widgets`](https://matplotlib.org/stable/api/widgets_api.html)
    
*   [`matplotlib._afm`](https://matplotlib.org/stable/api/_afm_api.html)
    
*   [`matplotlib._api`](https://matplotlib.org/stable/api/_api_api.html)
    
*   [`matplotlib._docstring`](https://matplotlib.org/stable/api/_docstring_api.html)
    
*   [`matplotlib._enums`](https://matplotlib.org/stable/api/_enums_api.html)
    
*   [`matplotlib._type1font`](https://matplotlib.org/stable/api/_type1font.html)
    
*   [`matplotlib._tight_bbox`](https://matplotlib.org/stable/api/_tight_bbox_api.html)
    
*   [`matplotlib._tight_layout`](https://matplotlib.org/stable/api/_tight_layout_api.html)
    
*   [`mpl_toolkits.mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html)
    
*   [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html)
    
*   [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html)
    
*   [`pylab`](https://matplotlib.org/stable/api/pylab.html)
    

On this page