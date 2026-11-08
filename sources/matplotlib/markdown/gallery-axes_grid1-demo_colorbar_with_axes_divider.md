[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html#sphx-glr-download-gallery-axes-grid1-demo-colorbar-with-axes-divider-py)
 to download the full example code.

Colorbar with AxesDivider[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html#colorbar-with-axesdivider "Link to this heading")

=====================================================================================================================================================================

The [`axes_divider.make_axes_locatable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable")
 function takes an existing Axes, adds it to a new [`AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 and returns the [`AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
. The [`append_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
 method of the [`AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 can then be used to create a new Axes on a given side ("top", "right", "bottom", or "left") of the original Axes. This example uses [`append_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
 to add colorbars next to Axes.

Users should consider simply passing the main Axes to the _ax_ keyword argument of [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 instead of creating a locatable Axes manually like this. See [Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html#colorbar-placement)
.

![demo colorbar with axes divider](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_axes_divider_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1.axes\_divider import [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(wspace\=0.5)

[im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[1, 2\], \[3, 4\]\])
[ax1\_divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
\# Add an Axes to the right of the main Axes.
[cax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax1\_divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("right", size\="7%", pad\="2%")
[cb1](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, cax\=[cax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[im2](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[1, 2\], \[3, 4\]\])
[ax2\_divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
\# Add an Axes above the main Axes.
[cax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax2\_divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("top", size\="7%", pad\="2%")
[cb2](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im2](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, cax\=[cax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\="horizontal")
\# Change tick position to top (with the default tick position "bottom", ticks
\# overlap the image).
[cax2.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
("top")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_colorbar_with_axes_divider.ipynb`](https://matplotlib.org/stable/_downloads/330f1d6a11f1f4baddf7fdd10f1ba589/demo_colorbar_with_axes_divider.ipynb)

[`Download Python source code: demo_colorbar_with_axes_divider.py`](https://matplotlib.org/stable/_downloads/cec7ab65767ff5217c21ae213755cda8/demo_colorbar_with_axes_divider.py)

[`Download zipped: demo_colorbar_with_axes_divider.zip`](https://matplotlib.org/stable/_downloads/e555d3cb1914a100553ede0d417c37fc/demo_colorbar_with_axes_divider.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)