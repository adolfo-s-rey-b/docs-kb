[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#main-content)

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
    

[What's new in Matplotlib 1.0 (Jul 06, 2010)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#what-s-new-in-matplotlib-1-0-jul-06-2010 "Link to this heading")

========================================================================================================================================================================================================================================================================

[HTML5/Canvas backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#html5-canvas-backend "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Simon Ratcliffe and Ludwig Schwardt have released an [HTML5/Canvas](https://code.google.com/archive/p/mplh5canvas)
 backend for matplotlib. The backend is almost feature complete, and they have done a lot of work comparing their html5 rendered images with our core renderer Agg. The backend features client/server interactive navigation of matplotlib figures in an html5 compliant browser.

[Sophisticated subplot grid layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#sophisticated-subplot-grid-layout "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Jae-Joon Lee has written [`gridspec`](https://matplotlib.org/stable/api/gridspec_api.html#module-matplotlib.gridspec "matplotlib.gridspec")
, a new module for doing complex subplot layouts, featuring row and column spans and more. See [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes)
 for a tutorial overview.

[![../../_images/sphx_glr_subplot2grid_001.png](https://matplotlib.org/stable/_images/sphx_glr_subplot2grid_001.png)](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html)

[Easy pythonic subplots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#easy-pythonic-subplots "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fernando Perez got tired of all the boilerplate code needed to create a figure and multiple subplots when using the matplotlib API, and wrote a [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 helper function. Basic usage allows you to create the figure and an array of subplots with numpy indexing (starts with 0). e.g.:

fig, axarr \= plt.subplots(2, 2)
axarr\[0,0\].plot(\[1,2,3\])   \# upper, left

See [Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)
 for several code examples.

[Contour fixes and triplot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#contour-fixes-and-triplot "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ian Thomas has fixed a long-standing bug that has vexed our most talented developers for years. [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
 now handles interior masked regions, and the boundaries of line and filled contours coincide.

Additionally, he has contributed a new module [`tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
 and helper function [`triplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
 for creating and plotting unstructured triangular grids.

[![../../_images/sphx_glr_triplot_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html)

[multiple calls to show supported](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#multiple-calls-to-show-supported "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A long standing request is to support multiple calls to [`show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
. This has been difficult because it is hard to get consistent behavior across operating systems, user interface toolkits and versions. Eric Firing has done a lot of work on rationalizing show across backends, with the desired behavior to make show raise all newly created figures and block execution until they are closed. Repeated calls to show should raise newly created figures since the last call. Eric has done a lot of testing on the user interface toolkits and versions and platforms he has access to, but it is not possible to test them all, so please report problems to the [mailing list](https://mail.python.org/mailman/listinfo/matplotlib-users)
 and [bug tracker](https://github.com/matplotlib/matplotlib/issues)
.

[mplot3d graphs can be embedded in arbitrary axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#mplot3d-graphs-can-be-embedded-in-arbitrary-axes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can now place an mplot3d graph into an arbitrary axes location, supporting mixing of 2D and 3D graphs in the same figure, and/or multiple 3D graphs in a single figure, using the "projection" keyword argument to add\_axes or add\_subplot. Thanks Ben Root.

([`Source code`](https://matplotlib.org/stable/_downloads/7747488f8536414a5b41daa611d4ed74/whats_new_1-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a889a14fe6ecbbbaab0626a47897c69c/whats_new_1-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/429790700287dfc3b146e661d6ee6ccf/whats_new_1-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-0-1.2x.png)

[tick\_params](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#tick-params "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Eric Firing wrote tick\_params, a convenience method for changing the appearance of ticks and tick labels. See pyplot function [`tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")
 and associated Axes method [`tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

[Lots of performance and feature enhancements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#lots-of-performance-and-feature-enhancements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Faster magnification of large images, and the ability to zoom in to a single pixel
    
*   Local installs of documentation work better
    
*   Improved "widgets" -- mouse grabbing is supported
    
*   More accurate snapping of lines to pixel boundaries
    
*   More consistent handling of color, particularly the alpha channel, throughout the API
    

[Much improved software carpentry](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#much-improved-software-carpentry "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The matplotlib trunk is probably in as good a shape as it has ever been, thanks to improved [software carpentry](https://software-carpentry.org/)
. We now have a [buildbot](https://buildbot.net/)
 which runs a suite of [nose](http://code.google.com/p/python-nose/)
 regression tests on every svn commit, auto-generating a set of images and comparing them against a set of known-goods, sending emails to developers on failures with a pixel-by-pixel image comparison. Releases and release bugfixes happen in branches, allowing active new feature development to happen in the trunk while keeping the release branches stable. Thanks to Andrew Straw, Michael Droettboom and other matplotlib developers for the heavy lifting.

[Bugfix marathon](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.0.html#bugfix-marathon "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Eric Firing went on a bug fixing and closing marathon, closing over 100 bugs on the (now-closed) SourceForge bug tracker with help from Jae-Joon Lee, Michael Droettboom, Christoph Gohlke and Michiel de Hoon.

On this page