[Skip to main content](https://matplotlib.org/stable/gallery/color/colormap_reference.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-download-gallery-color-colormap-reference-py)
 to download the full example code.

Colormap reference[#](https://matplotlib.org/stable/gallery/color/colormap_reference.html#colormap-reference "Link to this heading")

=====================================================================================================================================

Reference for colormaps included with Matplotlib.

A reversed version of each of these colormaps is available by appending `_r` to the name, as shown in [Reversed colormaps](https://matplotlib.org/stable/gallery/color/colormap_reference.html#reverse-cmap)
.

See [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
 for an in-depth discussion about colormaps, including colorblind-friendliness, and [Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
 for a guide to creating colormaps.

import matplotlib.pyplot as plt
import numpy as np

[cmaps](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[('Perceptually Uniform Sequential', \[\
            'viridis', 'plasma', 'inferno', 'magma', 'cividis'\]),\
         ('Sequential', \[\
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',\
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',\
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'\]),\
         ('Sequential (2)', \[\
            'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter',\
            'cool', 'Wistia', 'hot', 'afmhot', 'gist\_heat', 'copper'\]),\
         ('Diverging', \[\
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',\
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',\
            'berlin', 'managua', 'vanimo'\]),\
         ('Cyclic', \['twilight', 'twilight\_shifted', 'hsv'\]),\
         ('Qualitative', \[\
            'Pastel1', 'Pastel2', 'Paired', 'Accent', 'okabe\_ito',\
            'Dark2', 'Set1', 'Set2', 'Set3',\
            'tab10', 'tab20', 'tab20b', 'tab20c'\]),\
         ('Miscellaneous', \[\
            'flag', 'prism', 'ocean', 'gist\_earth', 'terrain', 'gist\_stern',\
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',\
            'gist\_rainbow', 'rainbow', 'jet', 'turbo', 'nipy\_spectral',\
            'gist\_ncar'\])\]

[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 256)
[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

def plot\_color\_gradients([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    \# Create figure and adjust figure height to number of colormaps
    nrows \= len([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    figh \= 0.35 + 0.15 + (nrows + (nrows\-1)\*0.1)\*0.22
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=nrows, figsize\=(6.4, figh))
    fig.subplots\_adjust(top\=1\-.35/figh, bottom\=.15/figh, left\=0.2, right\=0.99)

    axs\[0\].set\_title(f"{[cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
} colormaps", fontsize\=14)

    for ax, cmap\_name in zip(axs, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        ax.imshow([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, aspect\='auto', cmap\=cmap\_name)
        ax.text(\-.01, .5, cmap\_name, va\='center', ha\='right', fontsize\=10,
                transform\=ax.transAxes)

    \# Turn off \*all\* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set\_axis\_off()

for [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 in [cmaps](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    plot\_color\_gradients([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

*   ![Perceptually Uniform Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_001_2_00x.png)
*   ![Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_002_2_00x.png)
*   ![Sequential (2) colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_003_2_00x.png)
*   ![Diverging colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_004_2_00x.png)
*   ![Cyclic colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_005_2_00x.png)
*   ![Qualitative colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_006_2_00x.png)
*   ![Miscellaneous colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_007_2_00x.png)

Discouraged

For backward compatibility we additionally support the following colormap names, which are identical to other builtin colormaps. Their use is discouraged. Use the suggested replacement instead.

| Colormap | Use identical replacement instead |
| --- | --- |
| gist\_gray | gray |
| gist\_yarg | gray\_r |
| binary | gray\_r |

Reversed colormaps[#](https://matplotlib.org/stable/gallery/color/colormap_reference.html#reversed-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Append `_r` to the name of any built-in colormap to get the reversed version:

plot\_color\_gradients("Original and reversed ", \['viridis', 'viridis\_r'\])

![Original and reversed  colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_008_2_00x.png)

The built-in reversed colormaps are generated using [`Colormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.reversed "matplotlib.colors.Colormap.reversed")
. For an example, see [Reversing a colormap](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#reversing-colormap)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
    
*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
    
*   [`matplotlib.figure.Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
    
*   [`matplotlib.axes.Axes.set_axis_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
    

Tags: [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 4.412 seconds)

[`Download Jupyter notebook: colormap_reference.ipynb`](https://matplotlib.org/stable/_downloads/ae2ae6268ccd7744803f2b64513ddf74/colormap_reference.ipynb)

[`Download Python source code: colormap_reference.py`](https://matplotlib.org/stable/_downloads/dd314a83577f446493e34d27a1ed8451/colormap_reference.py)

[`Download zipped: colormap_reference.zip`](https://matplotlib.org/stable/_downloads/e0a5a2285bdbf495ed4237f955e4e825/colormap_reference.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page