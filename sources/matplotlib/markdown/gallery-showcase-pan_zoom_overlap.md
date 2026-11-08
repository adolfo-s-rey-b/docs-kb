[Skip to main content](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html#sphx-glr-download-gallery-showcase-pan-zoom-overlap-py)
 to download the full example code.

Pan/zoom events of overlapping axes[#](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html#pan-zoom-events-of-overlapping-axes "Link to this heading")

========================================================================================================================================================================

Example to illustrate how pan/zoom events of overlapping axes are treated.

The default is the following:

*   Axes with a visible patch capture pan/zoom events
    
*   Axes with an invisible patch forward pan/zoom events to axes below
    
*   Shared axes always trigger with their parent axes (irrespective of the patch visibility)
    

Note: The visibility of the patch hereby refers to the value of `ax.patch.get_visible()`. The color and transparency of a patch have no effect on the treatment of pan/zoom events!

`ax.set_forward_navigation_events(val)` can be used to override the default behaviour:

*   `True`: Forward navigation events to axes below.
    
*   `False`: Execute navigation events only on this axes.
    
*   `"auto"`: Use the default behaviour.
    

To disable pan/zoom events completely, use `ax.set_navigate(False)`

![Showcase for pan/zoom events on overlapping axes.](https://matplotlib.org/stable/_images/sphx_glr_pan_zoom_overlap_001_2_00x.png)

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(11, 6))
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Showcase for pan/zoom events on overlapping axes.")

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((.05, .05, .9, .9))
[ax.patch.set\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color")
(".75")
[ax\_twin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(221)
[ax1\_twin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax1.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()
[ax1.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.5, .5,
         "Visible patch\\n\\n"
         "Pan/zoom events are NOT\\n"
         "forwarded to axes below",
         ha\="center", va\="center", transform\=[ax1.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax11](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(223, sharex\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, sharey\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax11.set\_forward\_navigation\_events](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events")
(True)
[ax11.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.5, .5,
          "Visible patch\\n\\n"
          "Override capture behavior:\\n\\n"
          "ax.set\_forward\_navigation\_events(True)",
          ha\="center", va\="center", transform\=[ax11.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(222)
[ax2\_twin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax2.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()
[ax2.patch.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[ax2.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.5, .5,
         "Invisible patch\\n\\n"
         "Pan/zoom events are\\n"
         "forwarded to axes below",
         ha\="center", va\="center", transform\=[ax2.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax22](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(224, sharex\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, sharey\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax22.patch.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[ax22.set\_forward\_navigation\_events](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events")
(False)
[ax22.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.5, .5,
          "Invisible patch\\n\\n"
          "Override capture behavior:\\n\\n"
          "ax.set\_forward\_navigation\_events(False)",
          ha\="center", va\="center", transform\=[ax22.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

**Total running time of the script:** (0 minutes 1.931 seconds)

[`Download Jupyter notebook: pan_zoom_overlap.ipynb`](https://matplotlib.org/stable/_downloads/89ce01ed80f9aef22de2014e415f7336/pan_zoom_overlap.ipynb)

[`Download Python source code: pan_zoom_overlap.py`](https://matplotlib.org/stable/_downloads/6400d2a702519ce3002085a3680be369/pan_zoom_overlap.py)

[`Download zipped: pan_zoom_overlap.zip`](https://matplotlib.org/stable/_downloads/d8f2b50d521368be992da58b3749aa77/pan_zoom_overlap.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)