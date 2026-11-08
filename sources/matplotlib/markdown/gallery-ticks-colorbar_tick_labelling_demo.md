[Skip to main content](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html#sphx-glr-download-gallery-ticks-colorbar-tick-labelling-demo-py)
 to download the full example code.

Colorbar Tick labelling[#](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html#colorbar-tick-labelling "Link to this heading")

=========================================================================================================================================================

Vertical colorbars have ticks, tick labels, and labels visible on the _y_ axis, horizontal colorbars on the _x_ axis. The `ticks` parameter can be used to set the ticks and the `format` parameter can be used to format the tick labels of the visible colorbar Axes. For further adjustments, the `yaxis` or `xaxis` Axes of the colorbar can be retrieved using its `ax` property.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as mticker

\# Fixing random state for reproducibility
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(seed\=19680801)

Make plot with vertical (default) colorbar

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
((250, 250))

[cax](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1, cmap\='coolwarm')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Gaussian noise with vertical colorbar')

\# Add colorbar, make sure to specify tick locations to match desired ticklabels
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cax](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
,
                    ticks\=\[\-1, 0, 1\],
                    format\=[mticker.FixedFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
(\['< -1', '0', '> 1'\]),
                    extend\='both'
                    )
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [cbar.ax.get\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels")
()
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].set\_verticalalignment('top')
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1\].set\_verticalalignment('bottom')

![Gaussian noise with vertical colorbar](https://matplotlib.org/stable/_images/sphx_glr_colorbar_tick_labelling_demo_001_2_00x.png)

Make plot with horizontal colorbar

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \-1, 1)

[cax](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='afmhot')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Gaussian noise with horizontal colorbar')

\# Add colorbar and adjust ticks afterwards
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cax](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, orientation\='horizontal')
[cbar.set\_ticks](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
(ticks\=\[\-1, 0, 1\], [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\['Low', 'Medium', 'High'\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Gaussian noise with horizontal colorbar](https://matplotlib.org/stable/_images/sphx_glr_colorbar_tick_labelling_demo_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colorbar.Colorbar.set_ticks`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    

**Total running time of the script:** (0 minutes 1.353 seconds)

[`Download Jupyter notebook: colorbar_tick_labelling_demo.ipynb`](https://matplotlib.org/stable/_downloads/baca3c3513a3e3102673c4c4bf6dfd44/colorbar_tick_labelling_demo.ipynb)

[`Download Python source code: colorbar_tick_labelling_demo.py`](https://matplotlib.org/stable/_downloads/7c1c0355d383ada156a40adab206a88a/colorbar_tick_labelling_demo.py)

[`Download zipped: colorbar_tick_labelling_demo.zip`](https://matplotlib.org/stable/_downloads/93d5c05c8ca908eaf7ce9b1d09f37fb4/colorbar_tick_labelling_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)