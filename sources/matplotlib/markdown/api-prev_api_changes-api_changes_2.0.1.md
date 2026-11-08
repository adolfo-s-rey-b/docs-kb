[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#main-content)

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
    

API Changes in 2.0.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#api-changes-in-2-0-1 "Link to this heading")

===============================================================================================================================================

Extensions to [`matplotlib.backend_bases.GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#extensions-to-matplotlib-backend-bases-graphicscontextbase "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To better support controlling the color of hatches, the method [`matplotlib.backend_bases.GraphicsContextBase.set_hatch_color`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_hatch_color "matplotlib.backend_bases.GraphicsContextBase.set_hatch_color")
 was added to the expected API of `GraphicsContext` classes. Calls to this method are currently wrapped with a `try:...except Attribute:` block to preserve back-compatibility with any third-party backends which do not extend [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
.

This value can be accessed in the backends via [`matplotlib.backend_bases.GraphicsContextBase.get_hatch_color`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch_color "matplotlib.backend_bases.GraphicsContextBase.get_hatch_color")
 (which was added in 2.0 see [Extension to matplotlib.backend\_bases.GraphicsContextBase](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#gc-get-hatch-color-wn)
) and should be used to color the hatches.

In the future there may also be `hatch_linewidth` and `hatch_density` related methods added. It is encouraged, but not required that third-party backends extend [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 to make adapting to these changes easier.

`afm.get_fontconfig_fonts` returns a list of paths and does not check for existence[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#afm-get-fontconfig-fonts-returns-a-list-of-paths-and-does-not-check-for-existence "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`afm.get_fontconfig_fonts` used to return a set of paths encoded as a `{key: 1, ...}` dict, and checked for the existence of the paths. It now returns a list and dropped the existence check, as the same check is performed by the caller (`afm.findSystemFonts`) as well.

`bar` now returns rectangles of negative height or width if the corresponding input is negative[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#bar-now-returns-rectangles-of-negative-height-or-width-if-the-corresponding-input-is-negative "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
 used to normalize the coordinates of the rectangles that it created, to keep their height and width positives, even if the corresponding input was negative. This normalization has been removed to permit a simpler computation of the correct [`Artist.sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")
 to use.

Do not clip line width when scaling dashes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#do-not-clip-line-width-when-scaling-dashes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The algorithm to scale dashes was changed to no longer clip the scaling factor: the dash patterns now continue to shrink at thin line widths. If the line width is smaller than the effective pixel size, this may result in dashed lines turning into solid gray-ish lines. This also required slightly tweaking the default patterns for '--', ':', and '.-' so that with the default line width the final patterns would not change.

There is no way to restore the old behavior.

Deprecate 'Vega' colormaps[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.1.html#deprecate-vega-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

The "Vega" colormaps are deprecated in Matplotlib 2.0.1 and will be removed in Matplotlib 2.2. Use the "tab" colormaps instead: "tab10", "tab20", "tab20b", "tab20c".

On this page