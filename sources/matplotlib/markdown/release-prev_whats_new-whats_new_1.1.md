[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#main-content)

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
    

[What's new in Matplotlib 1.1 (Nov 02, 2011)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#what-s-new-in-matplotlib-1-1-nov-02-2011 "Link to this heading")

========================================================================================================================================================================================================================================================================

Note

matplotlib 1.1 supports Python 2.4 to 2.7

[Sankey Diagrams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#sankey-diagrams "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kevin Davies has extended Yannick Copin's original Sankey example into a module ([`sankey`](https://matplotlib.org/stable/api/sankey_api.html#module-matplotlib.sankey "matplotlib.sankey")
) and provided new examples ([The Sankey class](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html)
, [Long chain of connections using Sankey](https://matplotlib.org/stable/gallery/specialty_plots/sankey_links.html)
, [Rankine power cycle](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html)
).

[![../../_images/sphx_glr_sankey_rankine_001.png](https://matplotlib.org/stable/_images/sphx_glr_sankey_rankine_001.png)](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html)

[Animation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#animation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ryan May has written a backend-independent framework for creating animated figures. The [`animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
 module is intended to replace the backend-specific examples formerly in the [Examples](https://matplotlib.org/stable/gallery/index.html#examples-index)
 listings. Examples using the new framework are in [Animation](https://matplotlib.org/stable/gallery/animation/index.html#animation-examples-index)
; see the entrancing `double pendulum <gallery/animation/double_pendulum_sgskip.py>` which uses [`matplotlib.animation.Animation.save()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
 to create the movie below.

This should be considered as a beta release of the framework; please try it and provide feedback.

[Tight Layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#tight-layout "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A frequent issue raised by users of matplotlib is the lack of a layout engine to nicely space out elements of the plots. While matplotlib still adheres to the philosophy of giving users complete control over the placement of plot elements, Jae-Joon Lee created the `matplotlib.tight_layout` module and introduced a new command [`tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 to address the most common layout issues.

([`Source code`](https://matplotlib.org/stable/_downloads/a854a5b1f7c88078e914a3f8eeb3a48c/whats_new_1-1-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b87c57b2e0e7fe7bf7d8e783b38b38e5/whats_new_1-1-1_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/af0493fbd7ca6ab107098f064f80e980/whats_new_1-1-1_00_00.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-1-1_00_00.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-1-1_00_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/2da922e3ad2fe5e07eb0e92f1fcaad48/whats_new_1-1-1_01_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ab9d9bcc06ab7883361bfad404037deb/whats_new_1-1-1_01_00.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-1-1_01_00.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-1-1_01_00.2x.png)

The usage of this functionality can be as simple as

plt.tight\_layout()

and it will adjust the spacing between subplots so that the axis labels do not overlap with neighboring subplots. A [Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
 has been created to show how to use this new tool.

[PyQT4, PySide, and IPython](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#pyqt4-pyside-and-ipython "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gerald Storer made the Qt4 backend compatible with PySide as well as PyQT4. At present, however, PySide does not support the PyOS\_InputHook mechanism for handling gui events while waiting for text input, so it cannot be used with the new version 0.11 of [IPython](http://ipython.org/)
. Until this feature appears in PySide, IPython users should use the PyQT4 wrapper for QT4, which remains the matplotlib default.

An rcParam entry, "backend.qt4", has been added to allow users to select PyQt4, PyQt4v2, or PySide. The latter two use the Version 2 Qt API. In most cases, users can ignore this rcParam variable; it is available to aid in testing, and to provide control for users who are embedding matplotlib in a PyQt4 or PySide app.

[Legend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#legend "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Jae-Joon Lee has improved plot legends. First, legends for complex plots such as [`stem()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
 plots will now display correctly. Second, the 'best' placement of a legend has been improved in the presence of NANs.

See the [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for more detailed explanation and examples.

[![../../_images/sphx_glr_legend_demo_004.png](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_004.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

[mplot3d](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#mplot3d "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In continuing the efforts to make 3D plotting in matplotlib just as easy as 2D plotting, Ben Root has made several improvements to the [`mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 module.

*   [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
     has been improved to bring the class towards feature-parity with regular Axes objects
    
*   Documentation for [The mplot3d toolkit](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#mplot3d)
     was significantly expanded
    
*   Axis labels and orientation improved
    
*   Most 3D plotting functions now support empty inputs
    
*   Ticker offset display added:
    

[![../../_images/sphx_glr_offset_001.png](https://matplotlib.org/stable/_images/sphx_glr_offset_001.png)](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

*   [`contourf()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf")
     gains _zdir_ and _offset_ kwargs. You can now do this:
    

[![../../_images/sphx_glr_contourf3d_2_001.png](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_2_001.png)](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)

[Numerix support removed](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#numerix-support-removed "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After more than two years of deprecation warnings, Numerix support has now been completely removed from matplotlib.

[Markers](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#markers "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The list of available markers for [`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
 and [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
 has now been merged. While they were mostly similar, some markers existed for one function, but not the other. This merge did result in a conflict for the 'd' diamond marker. Now, 'd' will be interpreted to always mean "thin" diamond while 'D' will mean "regular" diamond.

Thanks to Michael Droettboom for this effort.

[Other improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.1.html#other-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Unit support for polar axes and [`arrow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow "matplotlib.axes.Axes.arrow")
    
*   [`PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
     gains getters and setters for "theta\_direction", and "theta\_offset" to allow for theta to go in either the clock-wise or counter-clockwise direction and to specify where zero degrees should be placed. [`set_theta_zero_location()`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_zero_location "matplotlib.projections.polar.PolarAxes.set_theta_zero_location")
     is an added convenience function.
    
*   Fixed error in argument handling for tri-functions such as [`tripcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tripcolor.html#matplotlib.pyplot.tripcolor "matplotlib.pyplot.tripcolor")
    
*   `axes.labelweight` parameter added to rcParams.
    
*   For [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    , _interpolation='nearest'_ will now always perform an interpolation. A "none" option has been added to indicate no interpolation at all.
    
*   An error in the Hammer projection has been fixed.
    
*   _clabel_ for [`contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
     now accepts a callable. Thanks to Daniel Hyams for the original patch.
    
*   Jae-Joon Lee added the [`HBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "mpl_toolkits.axes_grid1.axes_divider.HBoxDivider")
     and [`VBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
     classes.
    
*   Christoph Gohlke reduced memory usage in [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    .
    
*   [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
     now accepts empty inputs.
    
*   The behavior for 'symlog' scale has been fixed, but this may result in some minor changes to existing plots. This work was refined by ssyr.
    
*   Peter Butterworth added named figure support to [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
    .
    
*   Michiel de Hoon has modified the MacOSX backend to make its interactive behavior consistent with the other backends.
    
*   Pim Schellart added a new colormap called "cubehelix". Sameer Grover also added a colormap called "coolwarm". See it and all other colormaps [here](https://matplotlib.org/stable/users/explain/colors/colormaps.html#color-colormaps-reference)
    .
    
*   Many bug fixes and documentation improvements.
    

On this page