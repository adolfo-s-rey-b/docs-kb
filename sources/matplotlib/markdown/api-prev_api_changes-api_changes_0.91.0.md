[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.91.0.html#main-content)

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
    

Changes for 0.91.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.91.0.html#changes-for-0-91-0 "Link to this heading")

============================================================================================================================================

*   Changed `cbook.is_file_like` to `cbook.is_writable_file_like` and corrected behavior.
    
*   Added _ax_ keyword argument to [`pyplot.colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
     and [`Figure.colorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     so that one can specify the axes object from which space for the colorbar is to be taken, if one does not want to make the colorbar axes manually.
    
*   Changed `cbook.reversed` so it yields a tuple rather than a (index, tuple). This agrees with the Python reversed builtin, and cbook only defines reversed if Python doesn't provide the builtin.
    
*   Made skiprows=1 the default on `csv2rec`
    
*   The gd and paint backends have been deleted.
    
*   The errorbar method and function now accept additional kwargs so that upper and lower limits can be indicated by capping the bar with a caret instead of a straight line segment.
    
*   The [`matplotlib.dviread`](https://matplotlib.org/stable/api/dviread.html#module-matplotlib.dviread "matplotlib.dviread")
     file now has a parser for files like psfonts.map and pdftex.map, to map TeX font names to external files.
    
*   The file `matplotlib.type1font` contains a new class for Type 1 fonts. Currently it simply reads pfa and pfb format files and stores the data in a way that is suitable for embedding in pdf files. In the future the class might actually parse the font to allow e.g., subsetting.
    
*   `matplotlib.ft2font` now supports `FT_Attach_File`. In practice this can be used to read an afm file in addition to a pfa/pfb file, to get metrics and kerning information for a Type 1 font.
    
*   The `AFM` class now supports querying CapHeight and stem widths. The get\_name\_char method now has an isord kwarg like get\_width\_char.
    
*   Changed [`pcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
     default to `shading='flat'`; but as noted now in the docstring, it is preferable to simply use the _edgecolor_ keyword argument.
    
*   The mathtext font commands (`\cal`, `\rm`, `\it`, `\tt`) now behave as TeX does: they are in effect until the next font change command or the end of the grouping. Therefore uses of `$\cal{R}$` should be changed to `${\cal R}$`. Alternatively, you may use the new LaTeX-style font commands (`\mathcal`, `\mathrm`, `\mathit`, `\mathtt`) which do affect the following group, e.g., `$\mathcal{R}$`.
    
*   Text creation commands have a new default linespacing and a new `linespacing` kwarg, which is a multiple of the maximum vertical extent of a line of ordinary text. The default is 1.2; `linespacing=2` would be like ordinary double spacing, for example.
    
*   Changed default kwarg in [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     to `clip=False`; clipping silently defeats the purpose of the special over, under, and bad values in the colormap, thereby leading to unexpected behavior. The new default should reduce such surprises.
    
*   Made the emit property of [`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
     and [`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
     `True` by default; removed the Axes custom callback handling into a 'callbacks' attribute which is a [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
     instance. This now supports the 'xlim\_changed' and 'ylim\_changed' Axes events.