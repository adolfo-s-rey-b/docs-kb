[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html#sphx-glr-download-gallery-specialty-plots-leftventricle-bullseye-py)
 to download the full example code.

Left ventricle bullseye[#](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html#left-ventricle-bullseye "Link to this heading")

=============================================================================================================================================================

This example demonstrates how to create the 17 segment model for the left ventricle recommended by the American Heart Association (AHA).

See also the [Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)
 example.

![Bulls Eye (AHA), Bulls Eye (AHA), Segments [3, 5, 6, 11, 12, 16] in bold](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def bullseye\_plot(ax, [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, seg\_bold\=None, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\="viridis", [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=None):
    """
    Bullseye representation for the left ventricle.

    Parameters
    ----------
    ax : Axes
    data : list\[float\]
        The intensity values for each of the 17 segments.
    seg\_bold : list\[int\], optional
        A list with the segments to highlight.
    cmap : colormap, default: "viridis"
        Colormap for the data.
    norm : Normalize or None, optional
        Normalizer for the data.

    Notes
    -----
    This function creates the 17 segment model for the left ventricle according
    to the American Heart Association (AHA) \[1\]\_

    References
    ----------
    .. \[1\] M. D. Cerqueira, N. J. Weissman, V. Dilsizian, A. K. Jacobs,
        S. Kaul, W. K. Laskey, D. J. Pennell, J. A. Rumberger, T. Ryan,
        and M. S. Verani, "Standardized myocardial segmentation and
        nomenclature for tomographic imaging of the heart",
        Circulation, vol. 105, no. 4, pp. 539-542, 2002.
    """

    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    if seg\_bold is None:
        seg\_bold \= \[\]
    if [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 is None:
        [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), vmax\=[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())

    r \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.2, 1, 4)

    ax.set(ylim\=(0, 1), xticklabels\=\[\], yticklabels\=\[\])
    ax.grid(False)  \# Remove grid

    \# Fill segments 1-6, 7-12, 13-16.
    for start, stop, r\_in, r\_out in \[\
            (0, 6, r\[2\], r\[3\]),\
            (6, 12, r\[1\], r\[2\]),\
            (12, 16, r\[0\], r\[1\]),\
            (16, 17, 0, r\[0\]),\
    \]:
        n \= stop \- start
        dtheta \= 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / n
        ax.bar([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n) \* dtheta + [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2, r\_out \- r\_in, dtheta, r\_in,
               color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[start:stop\])))

    \# Now, draw the segment borders.  In order for the outer bold borders not
    \# to be covered by inner segments, the borders are all drawn separately
    \# after the segments have all been filled.  We also disable clipping, which
    \# would otherwise affect the outermost segment edges.
    \# Draw edges of segments 1-6, 7-12, 13-16.
    for start, stop, r\_in, r\_out in \[\
            (0, 6, r\[2\], r\[3\]),\
            (6, 12, r\[1\], r\[2\]),\
            (12, 16, r\[0\], r\[1\]),\
    \]:
        n \= stop \- start
        dtheta \= 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / n
        ax.bar([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n) \* dtheta + [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2, r\_out \- r\_in, dtheta, r\_in,
               clip\_on\=False, color\="none", edgecolor\="k", linewidth\=\[\
                   4 if i + 1 in seg\_bold else 2 for i in range(start, stop)\])
    \# Draw edge of segment 17 -- here; the edge needs to be drawn differently,
    \# using plot().
    ax.plot([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(r\[0\], r\[0\]), "k",
            linewidth\=(4 if 17 in seg\_bold else 2))

\# Create the fake data
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(17) + 1

\# Make a figure and Axes with dimensions as desired.
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5), layout\="constrained")
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(wspace\=.1, w\_pad\=.2)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(1, 3, subplot\_kw\=dict(projection\='polar'))
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.canvas.manager.set\_window\_title('Left Ventricle Bulls Eyes (AHA)')

\# Set the colormap and norm to correspond to the data for which
\# the colorbar will be used.
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["viridis"\]
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=1, vmax\=17)
\# Create an empty ScalarMappable to set the colorbar's colormap and norm.
\# The following gives a basic continuous colorbar with ticks and labels.
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.cm.ScalarMappable](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "matplotlib.colorizer._ScalarMappable")
([cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
),
             cax\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].inset\_axes(\[0, \-.15, 1, .1\]),
             orientation\='horizontal', label\='Some units')

\# And again for the second colorbar.
[cmap2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["cool"\]
[norm2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=1, vmax\=17)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.cm.ScalarMappable](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "matplotlib.colorizer._ScalarMappable")
([cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
),
             cax\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].inset\_axes(\[0, \-.15, 1, .1\]),
             orientation\='horizontal', label\='Some other units')

\# The second example illustrates the use of a ListedColormap, a
\# BoundaryNorm, and extended ends to show the "over" and "under"
\# value colors.
[cmap3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\['r', 'g', 'b', 'c'\], over\='0.35', under\='0.75')
\# If a ListedColormap is used, the length of the bounds array must be
\# one greater than the length of the color list.  The bounds must be
\# monotonically increasing.
[bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[2, 3, 7, 9, 15\]
[norm3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [mpl.colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
([bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap3.N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.cm.ScalarMappable](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "matplotlib.colorizer._ScalarMappable")
([cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
),
             cax\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].inset\_axes(\[0, \-.15, 1, .1\]),
             extend\='both',
             ticks\=[bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,  \# optional
             spacing\='proportional',
             orientation\='horizontal',
             label\='Discrete intervals, some other units')

\# Create the 17 segment model
bullseye\_plot([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Bulls Eye (AHA)')

bullseye\_plot([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('Bulls Eye (AHA)')

bullseye\_plot([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, seg\_bold\=\[3, 5, 6, 11, 12, 16\],
              [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm3](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_title('Segments \[3, 5, 6, 11, 12, 16\] in bold')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 2.935 seconds)

[`Download Jupyter notebook: leftventricle_bullseye.ipynb`](https://matplotlib.org/stable/_downloads/239ab391690d0658217395e893d357e2/leftventricle_bullseye.ipynb)

[`Download Python source code: leftventricle_bullseye.py`](https://matplotlib.org/stable/_downloads/02544761e32038ab6461a08bc2b3e1fd/leftventricle_bullseye.py)

[`Download zipped: leftventricle_bullseye.zip`](https://matplotlib.org/stable/_downloads/acf6c6a7c41faf326629f5df46860ebc/leftventricle_bullseye.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)