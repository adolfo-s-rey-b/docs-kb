[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#main-content)

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
    

[What's new in Matplotlib 1.3 (Aug 01, 2013)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#what-s-new-in-matplotlib-1-3-aug-01-2013 "Link to this heading")

========================================================================================================================================================================================================================================================================

Note

matplotlib 1.3 supports Python 2.6, 2.7, 3.2, and 3.3

[New in 1.3.1](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#new-in-1-3-1 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.3.1 is a micro release, primarily dealing with improved setup and handling of dependencies, and correcting and enhancing the documentation.

The following changes were made in 1.3.1 since 1.3.0.

### Enhancements[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#enhancements "Link to this heading")

*   Added a context manager for creating multi-page pdfs (see [`matplotlib.backends.backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
    ).
    
*   The WebAgg backend should now have lower latency over heterogeneous Internet connections.
    

### Bug fixes[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#bug-fixes "Link to this heading")

*   Histogram plots now contain the endline.
    
*   Fixes to the Molleweide projection.
    
*   Handling recent fonts from Microsoft and Macintosh-style fonts with non-ascii metadata is improved.
    
*   Hatching of fill between plots now works correctly in the PDF backend.
    
*   Tight bounding box support now works in the PGF backend.
    
*   Transparent figures now display correctly in the Qt4Agg backend.
    
*   Drawing lines from one subplot to another now works.
    
*   Unit handling on masked arrays has been improved.
    

### Setup and dependencies[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#setup-and-dependencies "Link to this heading")

*   Now works with any version of pyparsing 1.5.6 or later, without displaying hundreds of warnings.
    
*   Now works with 64-bit versions of Ghostscript on MS-Windows.
    
*   When installing from source into an environment without Numpy, Numpy will first be downloaded and built and then used to build matplotlib.
    
*   Externally installed backends are now always imported using a fully-qualified path to the module.
    
*   Works with newer version of wxPython.
    
*   Can now build with a PyCXX installed globally on the system from source.
    
*   Better detection of Gtk3 dependencies.
    

### Testing[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#testing "Link to this heading")

*   Tests should now work in non-English locales.
    
*   PEP8 conformance tests now report on locations of issues.
    

[New plotting features](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#new-plotting-features "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`xkcd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "matplotlib.pyplot.xkcd")
\-style sketch plotting[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#xkcd-style-sketch-plotting "Link to this heading")

To give your plots a sense of authority that they may be missing, Michael Droettboom (inspired by the work of many others in [PR #1329](https://github.com/matplotlib/matplotlib/pull/1329/)
) has added an [xkcd-style](https://xkcd.com/)
 sketch plotting mode. To use it, simply call [`matplotlib.pyplot.xkcd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "matplotlib.pyplot.xkcd")
 before creating your plot. For really fine control, it is also possible to modify each artist's sketch parameters individually with [`matplotlib.artist.Artist.set_sketch_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params")
.

[![../../_images/sphx_glr_xkcd_001.png](https://matplotlib.org/stable/_images/sphx_glr_xkcd_001.png)](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

[Updated Axes3D.contour methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#updated-axes3d-contour-methods "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Damon McDougall updated the [`tricontour()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour "mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour")
 and [`tricontourf()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf "mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf")
 methods to allow 3D contour plots on arbitrary unstructured user-specified triangulations.

[![../../_images/sphx_glr_tricontour3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_001.png)](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html)

### New eventplot plot type[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#new-eventplot-plot-type "Link to this heading")

Todd Jennings added a [`eventplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html#matplotlib.pyplot.eventplot "matplotlib.pyplot.eventplot")
 function to create multiple rows or columns of identical line segments

[![../../_images/sphx_glr_eventplot_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_eventplot_demo_001.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html)

As part of this feature, there is a new [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 class that allows for plotting and manipulating rows or columns of identical line segments.

### Triangular grid interpolation[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#triangular-grid-interpolation "Link to this heading")

Geoffroy Billotey and Ian Thomas added classes to perform interpolation within triangular grids: ([`LinearTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
 and [`CubicTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
) and a utility class to find the triangles in which points lie ([`TrapezoidMapTriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TrapezoidMapTriFinder "matplotlib.tri.TrapezoidMapTriFinder")
). A helper class to perform mesh refinement and smooth contouring was also added ([`UniformTriRefiner`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
). Finally, a class implementing some basic tools for triangular mesh improvement was added ([`TriAnalyzer`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
).

[![../../_images/sphx_glr_tricontour_smooth_user_001.png](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_user_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_user.html)

### Baselines for stackplot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#baselines-for-stackplot "Link to this heading")

Till Stensitzki added non-zero baselines to [`stackplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib.pyplot.stackplot "matplotlib.pyplot.stackplot")
. They may be symmetric or weighted.

[![../../_images/sphx_glr_stackplot_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_stackplot_demo_001.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html)

### Rectangular colorbar extensions[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#rectangular-colorbar-extensions "Link to this heading")

Andrew Dawson added a new keyword argument _extendrect_ to [`colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 to optionally make colorbar extensions rectangular instead of triangular.

### More robust boxplots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#more-robust-boxplots "Link to this heading")

Paul Hobson provided a fix to the [`boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
 method that prevent whiskers from being drawn inside the box for oddly distributed data sets.

### Calling subplot() without arguments[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#calling-subplot-without-arguments "Link to this heading")

A call to [`subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 without any arguments now acts the same as `subplot(111)` or `subplot(1, 1, 1)` -- it creates one axes for the whole figure. This was already the behavior for both [`axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
 and [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, and now this consistency is shared with [`subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
.

[Drawing](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#drawing "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Independent alpha values for face and edge colors[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#independent-alpha-values-for-face-and-edge-colors "Link to this heading")

Wes Campaigne modified how [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 objects are drawn such that (for backends supporting transparency) you can set different alpha values for faces and edges, by specifying their colors in RGBA format. Note that if you set the alpha attribute for the patch object (e.g. using [`set_alpha()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_alpha "matplotlib.patches.Patch.set_alpha")
 or the `alpha` keyword argument), that value will override the alpha components set in both the face and edge colors.

### Path effects on lines[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#path-effects-on-lines "Link to this heading")

Thanks to Jae-Joon Lee, path effects now also work on plot lines.

[![../../_images/sphx_glr_patheffect_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_001.png)](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

### Easier creation of colormap and normalizer for levels with colors[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#easier-creation-of-colormap-and-normalizer-for-levels-with-colors "Link to this heading")

Phil Elson added the [`matplotlib.colors.from_levels_and_colors()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.from_levels_and_colors.html#matplotlib.colors.from_levels_and_colors "matplotlib.colors.from_levels_and_colors")
 function to easily create a colormap and normalizer for representation of discrete colors for plot types such as [`matplotlib.pyplot.pcolormesh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "matplotlib.pyplot.pcolormesh")
, with a similar interface to that of [`matplotlib.pyplot.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
.

### Full control of the background color[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#full-control-of-the-background-color "Link to this heading")

Wes Campaigne and Phil Elson fixed the Agg backend such that PNGs are now saved with the correct background color when `fig.patch.get_alpha()` is not 1.

### Improved `bbox_inches="tight"` functionality[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#improved-bbox-inches-tight-functionality "Link to this heading")

Passing `bbox_inches="tight"` through to [`pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 now takes into account _all_ artists on a figure - this was previously not the case and led to several corner cases which did not function as expected.

### Initialize a rotated rectangle[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#initialize-a-rotated-rectangle "Link to this heading")

Damon McDougall extended the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 constructor to accept an _angle_ kwarg, specifying the rotation of a rectangle in degrees.

[Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#text "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Anchored text support[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#anchored-text-support "Link to this heading")

The SVG and pgf backends are now able to save text alignment information to their output formats. This allows to edit text elements in saved figures, using Inkscape for example, while preserving their intended position. For SVG please note that you'll have to disable the default text-to-path conversion (`mpl.rc('svg', fonttype='none')`).

### Better vertical text alignment and multi-line text[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#better-vertical-text-alignment-and-multi-line-text "Link to this heading")

The vertical alignment of text is now consistent across backends. You may see small differences in text placement, particularly with rotated text.

If you are using a custom backend, note that the [`draw_text`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_text "matplotlib.backend_bases.RendererBase.draw_text")
 renderer method is now passed the location of the baseline, not the location of the bottom of the text bounding box.

Multi-line text will now leave enough room for the height of very tall or very low text, such as superscripts and subscripts.

### Left and right side axes titles[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#left-and-right-side-axes-titles "Link to this heading")

Andrew Dawson added the ability to add axes titles flush with the left and right sides of the top of the axes using a new keyword argument _loc_ to [`title()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
.

### Improved manual contour plot label positioning[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#improved-manual-contour-plot-label-positioning "Link to this heading")

Brian Mattern modified the manual contour plot label positioning code to interpolate along line segments and find the actual closest point on a contour to the requested position. Previously, the closest path vertex was used, which, in the case of straight contours was sometimes quite distant from the requested location. Much more precise label positioning is now possible.

[Configuration (rcParams)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#configuration-rcparams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Quickly find rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#quickly-find-rcparams "Link to this heading")

Phil Elson made it easier to search for rcParameters by passing a valid regular expression to [`matplotlib.RcParams.find_all()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams.find_all "matplotlib.RcParams.find_all")
. [`matplotlib.RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 now also has a pretty repr and str representation so that search results are printed prettily:

\>>> import matplotlib
\>>> print(matplotlib.rcParams.find\_all('\\.size'))
RcParams({'font.size': 12,
          'xtick.major.size': 4,
          'xtick.minor.size': 2,
          'ytick.major.size': 4,
          'ytick.minor.size': 2})

### `axes.xmargin` and `axes.ymargin` added to rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#axes-xmargin-and-axes-ymargin-added-to-rcparams "Link to this heading")

`[rcParams["axes.xmargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.xmargin#rcparam-axes-xmargin) ` (default: `0.05`) and `[rcParams["axes.ymargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.ymargin#rcparam-axes-ymargin) ` (default: `0.05`) were added to configure the default margins used. Previously they were hard-coded to default to 0, default value of both rcParam values is 0.

### Changes to font rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#changes-to-font-rcparams "Link to this heading")

The `font.*` rcParams now affect only text objects created after the rcParam has been set, and will not retroactively affect already existing text objects. This brings their behavior in line with most other rcParams.

### Added `savefig.jpeg_quality` rcParam[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#added-savefig-jpeg-quality-rcparam "Link to this heading")

The `savefig.jpeg_quality` rcParam was added so that the user can configure the default quality used when a figure is written as a JPEG. The default quality is 95; previously, the default quality was 75. This change minimizes the artifacting inherent in JPEG images, particularly with images that have sharp changes in color as plots often do.

[Backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#backends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### WebAgg backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#webagg-backend "Link to this heading")

Michael Droettboom, Phil Elson and others have developed a new backend, WebAgg, to display figures in a web browser. It works with animations as well as being fully interactive.

![../../_images/webagg_screenshot.png](https://matplotlib.org/stable/_images/webagg_screenshot.png)

Future versions of matplotlib will integrate this backend with the IPython notebook for a fully web browser based plotting frontend.

### Remember save directory[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#remember-save-directory "Link to this heading")

Martin Spacek made the save figure dialog remember the last directory saved to. The default is configurable with the new `[rcParams["savefig.directory"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.directory#rcparam-savefig-directory) ` (default: `'~'`) rcParam in `matplotlibrc`.

[Documentation and examples](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#documentation-and-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Numpydoc docstrings[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#numpydoc-docstrings "Link to this heading")

Nelle Varoquaux has started an ongoing project to convert matplotlib's docstrings to numpydoc format. See [MEP10](https://github.com/matplotlib/matplotlib/wiki/Mep10)
 for more information.

### Example reorganization[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#example-reorganization "Link to this heading")

Tony Yu has begun work reorganizing the examples into more meaningful categories. The new gallery page is the fruit of this ongoing work. See [MEP12](https://github.com/matplotlib/matplotlib/wiki/MEP12)
 for more information.

### Examples now use subplots()[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#examples-now-use-subplots "Link to this heading")

For the sake of brevity and clarity, most of the [examples](https://matplotlib.org/stable/gallery/index.html#examples-index)
 now use the newer [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, which creates a figure and one (or multiple) axes object(s) in one call. The old way involved a call to [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, followed by one (or multiple) [`subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 calls.

[Infrastructure](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#infrastructure "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Housecleaning[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#housecleaning "Link to this heading")

A number of features that were deprecated in 1.2 or earlier, or have not been in a working state for a long time have been removed. Highlights include removing the Qt version 3 backends, and the FltkAgg and Emf backends. See [API Changes in 1.3.x](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.3.x.html#changes-in-1-3)
 for a complete list.

### New setup script[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#new-setup-script "Link to this heading")

matplotlib 1.3 includes an entirely rewritten setup script. We now ship fewer dependencies with the tarballs and installers themselves. Notably, [pytz](https://pypi.org/project/pytz/)
, [dateutil](https://pypi.org/project/python-dateutil/)
, [pyparsing](https://pypi.org/project/pyparsing/)
 and [six](https://pypi.org/project/six/)
 are no longer included with matplotlib. You can either install them manually first, or let [pip](https://pypi.org/project/pip/)
 install them as dependencies along with matplotlib. It is now possible to not include certain subcomponents, such as the unit test data, in the install. See `setup.cfg.template` for more information.

### XDG base directory support[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#xdg-base-directory-support "Link to this heading")

On Linux, matplotlib now uses the [XDG base directory specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
 to find the `matplotlibrc` configuration file. `matplotlibrc` should now be kept in `~/.config/matplotlib`, rather than `~/.matplotlib`. If your configuration is found in the old location, it will still be used, but a warning will be displayed.

### Catch opening too many figures using pyplot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.3.html#catch-opening-too-many-figures-using-pyplot "Link to this heading")

Figures created through [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 are retained until they are explicitly closed. It is therefore common for new users of matplotlib to run out of memory when creating a large series of figures in a loop without closing them.

matplotlib will now display a [`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "(in Python v3.14)")
 when too many figures have been opened at once. By default, this is displayed for 20 or more figures, but the exact number may be controlled using the `figure.max_open_warning` rcParam.

On this page