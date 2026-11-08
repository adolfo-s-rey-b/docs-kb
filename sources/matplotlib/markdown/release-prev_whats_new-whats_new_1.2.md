[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#main-content)

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
    

[What's new in Matplotlib 1.2 (Nov 9, 2012)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#what-s-new-in-matplotlib-1-2-nov-9-2012 "Link to this heading")

======================================================================================================================================================================================================================================================================

Note

matplotlib 1.2 supports Python 2.6, 2.7, and 3.1

[Python 3.x support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#python-3-x-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib 1.2 is the first version to support Python 3.x, specifically Python 3.1 and 3.2. To make this happen in a reasonable way, we also had to drop support for Python versions earlier than 2.6.

This work was done by Michael Droettboom, the Cape Town Python Users' Group, many others and supported financially in part by the SAGE project.

The following GUI backends work under Python 3.x: Gtk3Cairo, Qt4Agg, TkAgg and MacOSX. The other GUI backends do not yet have adequate bindings for Python 3.x, but continue to work on Python 2.6 and 2.7, particularly the Qt and QtAgg backends (which have been deprecated). The non-GUI backends, such as PDF, PS and SVG, work on both Python 2.x and 3.x.

Features that depend on the Python Imaging Library, such as JPEG handling, do not work, since the version of PIL for Python 3.x is not sufficiently mature.

[PGF/TikZ backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#pgf-tikz-backend "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Peter Würtz wrote a backend that allows matplotlib to export figures as drawing commands for LaTeX. These can be processed by PdfLaTeX, XeLaTeX or LuaLaTeX using the PGF/TikZ package. Usage examples and documentation are found in [Text rendering with XeLaTeX/LuaLaTeX via the pgf backend](https://matplotlib.org/stable/users/explain/text/pgf.html#pgf)
.

![../../_images/pgf_preamble.png](https://matplotlib.org/stable/_images/pgf_preamble.png)

[Locator interface](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#locator-interface "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Philip Elson exposed the intelligence behind the tick Locator classes with a simple interface. For instance, to get no more than 5 sensible steps which span the values 10 and 19.5:

\>>> import matplotlib.ticker as mticker
\>>> locator \= mticker.MaxNLocator(nbins\=5)
\>>> print(locator.tick\_values(10, 19.5))
\[ 10.  12.  14.  16.  18.  20.\]

[Tri-Surface Plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#tri-surface-plots "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Damon McDougall added a new plotting method for the [`mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 toolkit called [`plot_trisurf()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
.

[![../../_images/sphx_glr_trisurf3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_001.png)](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html)

[Control the lengths of colorbar extensions](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#control-the-lengths-of-colorbar-extensions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Andrew Dawson added a new keyword argument _extendfrac_ to [`colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 to control the length of minimum and maximum colorbar extensions.

([`Source code`](https://matplotlib.org/stable/_downloads/c6faa4ac8d059d728b92adee9185065b/whats_new_1-2-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5814695ce35cffa6294f558ddedfc624/whats_new_1-2-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5436e31032a2b4e2ed7278b496c9ea40/whats_new_1-2-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-2-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-2-1.2x.png)

[Figures are picklable](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#figures-are-picklable "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Philip Elson added an experimental feature to make figures picklable for quick and easy short-term storage of plots. Pickle files are not designed for long term storage, are unsupported when restoring a pickle saved in another matplotlib version and are insecure when restoring a pickle from an untrusted source. Having said this, they are useful for short term storage for later modification inside matplotlib.

[Set default bounding box in matplotlibrc](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#set-default-bounding-box-in-matplotlibrc "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Two new defaults are available in the matplotlibrc configuration file: `savefig.bbox`, which can be set to 'standard' or 'tight', and `savefig.pad_inches`, which controls the bounding box padding.

[New Boxplot Functionality](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#new-boxplot-functionality "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Users can now incorporate their own methods for computing the median and its confidence intervals into the [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 method. For every column of data passed to boxplot, the user can specify an accompanying median and confidence interval.

[![../../_images/sphx_glr_boxplot_demo_003.png](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_003.png)](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

[New RC parameter functionality](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#new-rc-parameter-functionality "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matthew Emmett added a function and a context manager to help manage RC parameters: [`rc_file()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file "matplotlib.rc_file")
 and [`rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
. To load RC parameters from a file:

\>>> mpl.rc\_file('mpl.rc')

To temporarily use RC parameters:

\>>> with mpl.rc\_context(fname\='mpl.rc', rc\={'text.usetex': True}):
\>>>     ...

[Streamplot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#streamplot "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tom Flannaghan and Tony Yu have added a new [`streamplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot "matplotlib.pyplot.streamplot")
 function to plot the streamlines of a vector field. This has been a long-requested feature and complements the existing [`quiver()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
 function for plotting vector fields. In addition to simply plotting the streamlines of the vector field, [`streamplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot "matplotlib.pyplot.streamplot")
 allows users to map the colors and/or line widths of the streamlines to a separate parameter, such as the speed or local intensity of the vector field.

[![../../_images/sphx_glr_plot_streamplot_001.png](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

[New hist functionality](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#new-hist-functionality "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Nic Eggert added a new _stacked_ kwarg to [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
 that allows creation of stacked histograms using any of the histogram types. Previously, this functionality was only available by using the "barstacked" histogram type. Now, when `stacked=True` is passed to the function, any of the histogram types can be stacked. The "barstacked" histogram type retains its previous functionality for backwards compatibility.

[Updated shipped dependencies](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#updated-shipped-dependencies "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following dependencies that ship with matplotlib and are optionally installed alongside it have been updated:

*   [pytz](http://pytz.sourceforge.net/)
     2012d
    
*   [dateutil](http://labix.org/python-dateutil)
     1.5 on Python 2.x,
    
    and 2.1 on Python 3.x
    

[Face-centred colors in tripcolor plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#face-centred-colors-in-tripcolor-plots "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ian Thomas extended [`tripcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tripcolor.html#matplotlib.pyplot.tripcolor "matplotlib.pyplot.tripcolor")
 to allow one color value to be specified for each triangular face rather than for each point in a triangulation.

[![../../_images/sphx_glr_tripcolor_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_demo_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/tripcolor_demo.html)

[Hatching patterns in filled contour plots, with legends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#hatching-patterns-in-filled-contour-plots-with-legends "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Phil Elson added support for hatching to [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
, together with the ability to use a legend to identify contoured ranges.

[![../../_images/sphx_glr_contourf_hatching_001.png](https://matplotlib.org/stable/_images/sphx_glr_contourf_hatching_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)

[Known issues in the matplotlib 1.2 release](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.2.html#known-issues-in-the-matplotlib-1-2-release "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   When using the Qt4Agg backend with IPython 0.11 or later, the save dialog will not display. This should be fixed in a future version of IPython.
    

On this page