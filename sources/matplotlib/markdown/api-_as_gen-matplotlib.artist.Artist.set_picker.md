[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#main-content)

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
    

matplotlib.artist.Artist.set\_picker[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib-artist-artist-set-picker "Link to this heading")

=======================================================================================================================================================================================

Artist.set\_picker(_picker_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L576-L609)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "Link to this definition")

Define the picking behavior of the artist.

Parameters:

**picker**None or bool or float or callable

This can be one of the following:

*   _None_: Picking is disabled for this artist (default).
    
*   A boolean: If _True_ then picking will be enabled and the artist will fire a pick event if the mouse event is over the artist.
    
*   A float: If picker is a number it is interpreted as an epsilon tolerance in points and the artist will fire off an event if its data is within epsilon of the mouse event. For some artists like lines and patch collections, the artist may provide additional data to the pick event that is generated, e.g., the indices of the data within epsilon of the pick event
    
*   A function: If picker is callable, it is a user supplied function which determines whether the artist is hit by the mouse event:
    
    hit, props \= picker(artist, mouseevent)
    
    to determine the hit test. if the mouse event is over the artist, return _hit=True_ and props is a dictionary of properties you want added to the PickEvent attributes.
    

Examples using `matplotlib.artist.Artist.set_picker`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#examples-using-matplotlib-artist-artist-set-picker "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_legend_picking_thumb.png)

[Legend picking](https://matplotlib.org/stable/gallery/event_handling/legend_picking.html)

Legend picking

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

On this page