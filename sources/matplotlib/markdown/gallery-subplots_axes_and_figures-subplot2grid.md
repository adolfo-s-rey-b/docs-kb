[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html#sphx-glr-download-gallery-subplots-axes-and-figures-subplot2grid-py)
 to download the full example code.

subplot2grid[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html#subplot2grid "Link to this heading")

=======================================================================================================================================

This example demonstrates the use of [`pyplot.subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
 to generate subplots. Using [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, as demonstrated in [GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)
 is generally preferred.

![subplot2grid](https://matplotlib.org/stable/_images/sphx_glr_subplot2grid_001_2_00x.png)

import matplotlib.pyplot as plt

def annotate\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    for i, ax in enumerate([fig.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html#matplotlib.figure.Figure.axes "matplotlib.figure.Figure.axes")
):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va\="center", ha\="center")
        ax.tick\_params(labelbottom\=False, labelleft\=False)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (0, 0), colspan\=3)
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (1, 0), colspan\=2)
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (1, 2), rowspan\=2)
[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (2, 0))
[ax5](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (2, 1))

annotate\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: subplot2grid.ipynb`](https://matplotlib.org/stable/_downloads/9daec55e51d863af6763e40e0e313b4e/subplot2grid.ipynb)

[`Download Python source code: subplot2grid.py`](https://matplotlib.org/stable/_downloads/4be179670089e2aef92ee35952df0b04/subplot2grid.py)

[`Download zipped: subplot2grid.zip`](https://matplotlib.org/stable/_downloads/ad2eb38bbafcc5d4eab1c11038927e63/subplot2grid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)