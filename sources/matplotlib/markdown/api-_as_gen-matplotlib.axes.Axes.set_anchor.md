[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#main-content)

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
    

matplotlib.axes.Axes.set\_anchor[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib-axes-axes-set-anchor "Link to this heading")

===========================================================================================================================================================================

Axes.set\_anchor(_anchor_, _share\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1922-L1966)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "Link to this definition")

Define the anchor location.

The actual drawing area (active position) of the Axes may be smaller than the Bbox (original position) when a fixed aspect is required. The anchor defines where the drawing area will be located within the available space.

Parameters:

**anchor**(float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...}

Either an (_x_, _y_) pair of relative coordinates (0 is left or bottom, 1 is right or top), 'C' (center), or a cardinal direction ('SW', southwest, is bottom left, etc.). str inputs are shorthands for (_x_, _y_) coordinates, as shown in the following diagram:

┌─────────────────┬─────────────────┬─────────────────┐
│ 'NW' (0.0, 1.0) │ 'N' (0.5, 1.0)  │ 'NE' (1.0, 1.0) │
├─────────────────┼─────────────────┼─────────────────┤
│ 'W'  (0.0, 0.5) │ 'C' (0.5, 0.5)  │ 'E'  (1.0, 0.5) │
├─────────────────┼─────────────────┼─────────────────┤
│ 'SW' (0.0, 0.0) │ 'S' (0.5, 0.0)  │ 'SE' (1.0, 0.0) │
└─────────────────┴─────────────────┴─────────────────┘

**share**bool, default: False

If `True`, apply the settings to all shared Axes.

See also

[`matplotlib.axes.Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")

for a description of aspect handling.

On this page