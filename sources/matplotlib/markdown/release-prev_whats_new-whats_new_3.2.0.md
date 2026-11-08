[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#main-content)

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
    

[What's new in Matplotlib 3.2 (Mar 04, 2020)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#what-s-new-in-matplotlib-3-2-mar-04-2020 "Link to this heading")

============================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Unit converters recognize subclasses](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#unit-converters-recognize-subclasses "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit converters now also handle instances of subclasses of the class they have been registered for.

[](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id3)
[`imsave`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave "matplotlib.pyplot.imsave")
 accepts metadata and PIL options[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#imsave-accepts-metadata-and-pil-options "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`imsave`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave "matplotlib.pyplot.imsave")
 has gained support for the `metadata` and `pil_kwargs` parameters. These parameters behave similarly as for the [`Figure.savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 method.

[](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id4)
[`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#cbook-normalize-kwargs "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
 now presents a convenient interface to normalize artist properties (e.g., from "lw" to "linewidth"):

\>>> cbook.normalize\_kwargs({"lw": 1}, Line2D)
{"linewidth": 1}

The first argument is the mapping to be normalized, and the second argument can be an artist class or an artist instance (it can also be a mapping in a specific format; see the function's docstring for details).

[](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id5)
[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 accepts [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#fontproperties-accepts-os-pathlike "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The _fname_ argument to [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 can now be an [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
, e.g.

\>>> FontProperties(fname\=pathlib.Path("/path/to/font.ttf"))

[Gouraud-shading alpha channel in PDF backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#gouraud-shading-alpha-channel-in-pdf-backend "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The pdf backend now supports an alpha channel in Gouraud-shaded triangle meshes.

[Kerning adjustments now use correct values](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#kerning-adjustments-now-use-correct-values "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Due to an error in how kerning adjustments were applied, previous versions of Matplotlib would under-correct kerning. This version will now correctly apply kerning (for fonts supported by FreeType). To restore the old behavior (e.g., for test images), you may set the `text.kerning_factor` rcParam to 6 (instead of 0). Other values have undefined behavior.

With corrected kerning (below), slanted characters (e.g., AV or VA) will be spaced closer together, as well as various other character pairs, depending on font support (e.g., T and e, or the period after the W).

([`Source code`](https://matplotlib.org/stable/_downloads/b0d393ef77e7812abe0aedc4401abe13/whats_new_3-2-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/89e857581b8a69cc563b30bcfccf7861/whats_new_3-2-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/1d294dd8958b0ad3e44a21dbf4e1236b/whats_new_3-2-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-2-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-2-0-1.2x.png)

[bar3d lightsource shading](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#bar3d-lightsource-shading "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`bar3d()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d")
 now supports lighting from different angles when the _shade_ parameter is `True`, which can be configured using the `lightsource` parameter.

[Shifting errorbars](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#shifting-errorbars "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 accepted a keyword argument _errorevery_ such that the command `plt.errorbar(x, y, yerr, errorevery=6)` would add error bars to datapoints `x[::6], y[::6]`.

[`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 now also accepts a tuple for _errorevery_ such that `plt.errorbar(x, y, yerr, errorevery=(start, N))` adds error bars to points `x[start::N], y[start::N]`.

[Improvements in Logit scale ticker and formatter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#improvements-in-logit-scale-ticker-and-formatter "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Introduced in version 1.5, the logit scale didn't have an appropriate ticker and formatter. Previously, the location of ticks was not zoom dependent, too many labels were displayed causing overlapping which broke readability, and label formatting did not adapt to precision.

Starting from this version, the logit locator has nearly the same behavior as the locator for the log scale or the linear scale, depending on used zoom. The number of ticks is controlled. Some minor labels are displayed adaptively as sublabels in log scale. Formatting is adapted for probabilities and the precision adapts to the scale.

[rcParams for axes title location and color](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#rcparams-for-axes-title-location-and-color "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Two new rcParams have been added: `[rcParams["axes.titlelocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlelocation#rcparam-axes-titlelocation) ` (default: `'center'`) denotes the default axes title alignment, and `[rcParams["axes.titlecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlecolor#rcparam-axes-titlecolor) ` (default: `'auto'`) the default axes title color.

Valid values for `axes.titlelocation` are: left, center, and right. Valid values for `axes.titlecolor` are: auto or a color. Setting it to auto will fall back to previous behaviour, which is using the color in `text.color`.

[3-digit and 4-digit hex colors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#digit-and-4-digit-hex-colors "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Colors can now be specified using 3-digit or 4-digit hex colors, shorthand for the colors obtained by duplicating each character, e.g. `#123` is equivalent to `#112233` and `#123a` is equivalent to `#112233aa`.

[Added support for RGB(A) images in pcolorfast](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#added-support-for-rgb-a-images-in-pcolorfast "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Axes.pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast")
 now accepts 3D images (RGB or RGBA) arrays.

On this page