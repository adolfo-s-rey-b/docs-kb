[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html#sphx-glr-download-gallery-subplots-axes-and-figures-gridspec-and-subplots-py)
 to download the full example code.

Combine two subplots using subplots and GridSpec[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html#combine-two-subplots-using-subplots-and-gridspec "Link to this heading")

========================================================================================================================================================================================================================

Sometimes we want to combine two subplots in an Axes layout created with [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
. We can get the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 from the Axes and then remove the covered Axes and fill the gap with a new bigger Axes. Here we create a layout with the bottom two Axes in the last column combined.

To start with this layout (rather than removing the overlapping Axes) use [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
.

See also [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes)
.

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, nrows\=3)
[gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].get\_gridspec()
\# remove the underlying Axes
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, \-1\]:
    [ax.remove](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#matplotlib.axes.Axes.remove "matplotlib.axes.Axes.remove")
()
[axbig](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1:, \-1\])
[axbig.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('Big Axes \\nGridSpec\[1:, -1\]', (0.1, 0.5),
               xycoords\='axes fraction', va\='center')

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![gridspec and subplots](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_001_2_00x.png)

Tags: [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.322 seconds)

[`Download Jupyter notebook: gridspec_and_subplots.ipynb`](https://matplotlib.org/stable/_downloads/24f9ea6e6c86518bcdc77699fffc02bd/gridspec_and_subplots.ipynb)

[`Download Python source code: gridspec_and_subplots.py`](https://matplotlib.org/stable/_downloads/1e01451841b499da6640677973bcab50/gridspec_and_subplots.py)

[`Download zipped: gridspec_and_subplots.zip`](https://matplotlib.org/stable/_downloads/9832d8c1e9ff1e62ced355c5a844550d/gridspec_and_subplots.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)