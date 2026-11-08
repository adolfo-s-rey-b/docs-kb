[Skip to main content](https://matplotlib.org/stable/gallery/color/color_sequences.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/color_sequences.html#sphx-glr-download-gallery-color-color-sequences-py)
 to download the full example code.

Named color sequences[#](https://matplotlib.org/stable/gallery/color/color_sequences.html#named-color-sequences "Link to this heading")

========================================================================================================================================

Matplotlib's [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
 allows access to predefined lists of colors by name e.g. `colors = matplotlib.color_sequences['Set1']`. This example shows all of the built in color sequences.

User-defined sequences can be added via [`ColorSequenceRegistry.register`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.register "matplotlib.colors.ColorSequenceRegistry.register")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def plot\_color\_sequences(names, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    \# Display each named color sequence horizontally on the supplied axes.

    for n, name in enumerate(names):
        colors \= [mpl.color\_sequences](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
\[name\]
        n\_colors \= len(colors)
        x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_colors)
        y \= [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(x, n)

        [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(x, y, facecolor\=colors, edgecolor\='dimgray', s\=200, zorder\=2)

    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(range(len(names)), labels\=names)
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(visible\=True, axis\='y')
    [ax.yaxis.set\_inverted](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted")
(True)
    [ax.xaxis.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[:\].set\_visible(False)
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(left\=False)

[built\_in\_color\_sequences](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    'tab10', 'tab20', 'tab20b', 'tab20c', 'Pastel1', 'Pastel2', 'Paired',\
    'Accent', 'okabe\_ito', 'Dark2', 'Set1', 'Set2', 'Set3', 'petroff6',\
    'petroff8', 'petroff10'\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6.4, 9.6), layout\='constrained')

plot\_color\_sequences([built\_in\_color\_sequences](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Built In Color Sequences')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Built In Color Sequences](https://matplotlib.org/stable/_images/sphx_glr_color_sequences_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors.ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
    
*   [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

[`Download Jupyter notebook: color_sequences.ipynb`](https://matplotlib.org/stable/_downloads/8e0c9d0a9e51a5ef27dd8f57ce946e11/color_sequences.ipynb)

[`Download Python source code: color_sequences.py`](https://matplotlib.org/stable/_downloads/9e70d40e9d045adb66bdd483958508f2/color_sequences.py)

[`Download zipped: color_sequences.zip`](https://matplotlib.org/stable/_downloads/3a9f371660ae050f9b90d1304ac8f71e/color_sequences.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)