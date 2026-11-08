[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html#sphx-glr-download-gallery-subplots-axes-and-figures-gridspec-nested-py)
 to download the full example code.

Nested Gridspecs[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html#nested-gridspecs "Link to this heading")

==================================================================================================================================================

GridSpecs can be nested, so that a subplot from a parent GridSpec can set the position for a nested grid of subplots.

Note that the same functionality can be achieved more directly with [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
; see [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
.

import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec

def format\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    for i, ax in enumerate([fig.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html#matplotlib.figure.Figure.axes "matplotlib.figure.Figure.axes")
):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va\="center", ha\="center")
        ax.tick\_params(labelbottom\=False, labelleft\=False)

\# gridspec inside gridspec
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(1, 2, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

[gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gridspec.GridSpecFromSubplotSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
(3, 3, subplot\_spec\=[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\])

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[:\-1, :\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[\-1, :\-1\])
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[\-1, \-1\])

\# the following syntax does the same as the GridSpecFromSubplotSpec call above:
[gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\].subgridspec(3, 3)

[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[:, :\-1\])
[ax5](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[:\-1, \-1\])
[ax6](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[\-1, \-1\])

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("GridSpec Inside GridSpec")
format\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![GridSpec Inside GridSpec](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_001_2_00x.png)

Tags: [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: gridspec_nested.ipynb`](https://matplotlib.org/stable/_downloads/dc5ba078aebe8d7561daefb7dda542a8/gridspec_nested.ipynb)

[`Download Python source code: gridspec_nested.py`](https://matplotlib.org/stable/_downloads/6f740ff878eb7af08d204edefcd427ba/gridspec_nested.py)

[`Download zipped: gridspec_nested.zip`](https://matplotlib.org/stable/_downloads/d910e063c1a9ba6d5c5653a4cb7937f9/gridspec_nested.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)