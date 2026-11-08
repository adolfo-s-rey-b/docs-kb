[Skip to main content](https://matplotlib.org/stable/gallery/misc/logos2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/logos2.html#sphx-glr-download-gallery-misc-logos2-py)
 to download the full example code.

Matplotlib logo[#](https://matplotlib.org/stable/gallery/misc/logos2.html#matplotlib-logo "Link to this heading")

==================================================================================================================

This example generates the current matplotlib logo.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm
import matplotlib.font\_manager
from matplotlib.patches import [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
, [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
from matplotlib.text import [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
import matplotlib.transforms as mtrans

[MPL\_BLUE](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '#11557c'

def get\_font\_properties():
    \# The original font is Calibri, if that is not installed, we fall back
    \# to Carlito, which is metrically equivalent.
    if 'calibri' in [matplotlib.font\_manager.findfont](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
('Calibri:bold').lower():
        return [matplotlib.font\_manager.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(family\='Calibri',
                                                      weight\='bold')
    \# Our website documentation uses Carlito because Calibri is proprietary.
    if 'carlito' in [matplotlib.font\_manager.findfont](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
('Carlito:bold').lower():
        print('Original font not found. Falling back to Carlito. '
              'The logo text will not be in the correct font.')
        return [matplotlib.font\_manager.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(family\='Carlito',
                                                      weight\='bold')
    print('Original font not found. '
          'The logo text will not be in the correct font.')
    return None

def create\_icon\_axes(fig, ax\_position, lw\_bars, lw\_grid, lw\_border, rgrid):
    """
    Create a polar Axes containing the matplotlib radar plot.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to draw into.
    ax\_position : (float, float, float, float)
        The position of the created Axes in figure coordinates as
        (x, y, width, height).
    lw\_bars : float
        The linewidth of the bars.
    lw\_grid : float
        The linewidth of the grid.
    lw\_border : float
        The linewidth of the Axes border.
    rgrid : array-like
        Positions of the radial grid.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The created Axes.
    """
    with [plt.rc\_context](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib.pyplot.rc_context "matplotlib.pyplot.rc_context")
({'axes.edgecolor': [MPL\_BLUE](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
                         'axes.linewidth': lw\_border}):
        ax \= fig.add\_axes(ax\_position, projection\='polar')
        ax.set\_axisbelow(True)

        N \= 7
        arc \= 2. \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
        theta \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, arc, arc / N)
        radii \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[2, 6, 8, 7, 4, 5, 8\])
        width \= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 4 \* [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3\])
        bars \= ax.bar(theta, radii, width\=width, bottom\=0.0, align\='edge',
                      edgecolor\='0.3', lw\=lw\_bars)
        for r, bar in zip(radii, bars):
            color \= \*[cm.jet](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
(r / 10.)\[:3\], 0.6  \# color from jet with alpha=0.6
            bar.set\_facecolor(color)

        ax.tick\_params(labelbottom\=False, labeltop\=False,
                       labelleft\=False, labelright\=False)

        ax.grid(lw\=lw\_grid, color\='0.9')
        ax.set\_rmax(9)
        ax.set\_yticks(rgrid)

        \# the actual visible background - extends a bit beyond the axis
        ax.add\_patch([Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((0, 0), arc, 9.58,
                               facecolor\='white', zorder\=0,
                               clip\_on\=False, in\_layout\=False))
        return ax

def create\_text\_axes(fig, height\_px):
    """Create an Axes in \*fig\* that contains 'matplotlib' as Text."""
    ax \= fig.add\_axes((0, 0, 1, 1))
    ax.set\_aspect("equal")
    ax.set\_axis\_off()

    path \= [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
((0, 0), "matplotlib", size\=height\_px \* 0.8,
                    prop\=get\_font\_properties())

    angle \= 4.25  \# degrees
    trans \= [mtrans.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().skew\_deg(angle, 0)

    patch \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(path, transform\=trans + ax.transData, color\=[MPL\_BLUE](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
                      lw\=0)
    ax.add\_patch(patch)
    ax.autoscale()

def make\_logo(height\_px, lw\_bars, lw\_grid, lw\_border, rgrid, with\_text\=False):
    """
    Create a full figure with the Matplotlib logo.

    Parameters
    ----------
    height\_px : int
        Height of the figure in pixel.
    lw\_bars : float
        The linewidth of the bar border.
    lw\_grid : float
        The linewidth of the grid.
    lw\_border : float
        The linewidth of icon border.
    rgrid : sequence of float
        The radial grid positions.
    with\_text : bool
        Whether to draw only the icon or to include 'matplotlib' as text.
    """
    dpi \= 100
    height \= height\_px / dpi
    figsize \= (5 \* height, height) if with\_text else (height, height)
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=figsize, dpi\=dpi)
    fig.patch.set\_alpha(0)

    if with\_text:
        create\_text\_axes(fig, height\_px)
    ax\_pos \= (0.535, 0.12, .17, 0.75) if with\_text else (0.03, 0.03, .94, .94)
    ax \= create\_icon\_axes(fig, ax\_pos, lw\_bars, lw\_grid, lw\_border, rgrid)

    return fig, ax

A large logo:

make\_logo(height\_px\=110, lw\_bars\=0.7, lw\_grid\=0.5, lw\_border\=1,
          rgrid\=\[1, 3, 5, 7\])

![logos2](https://matplotlib.org/stable/_images/sphx_glr_logos2_001_2_00x.png)

A small 32px logo:

make\_logo(height\_px\=32, lw\_bars\=0.3, lw\_grid\=0.3, lw\_border\=0.3, rgrid\=\[5\])

![logos2](https://matplotlib.org/stable/_images/sphx_glr_logos2_002_2_00x.png)

A large logo including text, as used on the matplotlib website.

make\_logo(height\_px\=110, lw\_bars\=0.7, lw\_grid\=0.5, lw\_border\=1,
          rgrid\=\[1, 3, 5, 7\], with\_text\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![logos2](https://matplotlib.org/stable/_images/sphx_glr_logos2_003_2_00x.png)

findfont: Font family \['Calibri'\] not found. Falling back to DejaVu Sans.
Original font not found. Falling back to Carlito. The logo text will not be in the correct font.

[`Download Jupyter notebook: logos2.ipynb`](https://matplotlib.org/stable/_downloads/c2174e10ada6a495467cc486f074bac5/logos2.ipynb)

[`Download Python source code: logos2.py`](https://matplotlib.org/stable/_downloads/0846c3e5d114c457e124451aea9e558a/logos2.py)

[`Download zipped: logos2.zip`](https://matplotlib.org/stable/_downloads/34c6f9eecfc096024b40cae4580bcee9/logos2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)