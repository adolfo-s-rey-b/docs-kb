[Skip to main content](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#sphx-glr-download-users-explain-artists-imshow-extent-py)
 to download the full example code.

Positioning and orientation of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 images[#](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#positioning-and-orientation-of-imshow-images "Link to this heading")

=======================================================================================================================================================================================================================================================================================================================================

[`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 allows you to render an image (either a 2D array which will be color-mapped (based on _norm_ and _cmap_) or a 3D RGB(A) array which will be used as-is) to a rectangular region in data space. The orientation of the image in the final rendering is controlled by the _origin_ and _extent_ keyword arguments (and attributes on the resulting [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 instance) and the data limits of the Axes.

The _extent_ keyword arguments controls the bounding box in data coordinates that the image will fill specified as `(left, right, bottom, top)` in **data coordinates**, the _origin_ keyword argument controls how the image fills that bounding box, and the orientation in the final rendered image is also affected by the axes limits.

Hint

Most of the code below is used for adding labels and informative text to the plots. The described effects of _origin_ and _extent_ can be seen in the plots without the need to follow all code details.

For a quick understanding, you may want to skip the code details below and directly continue with the discussion of the results.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

def index\_to\_coordinate(index, extent, origin):
    """Return the pixel center of an index."""
    left, right, bottom, top \= extent

    hshift \= 0.5 \* [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(right \- left)
    left, right \= left + hshift, right \- hshift
    vshift \= 0.5 \* [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(top \- bottom)
    bottom, top \= bottom + vshift, top \- vshift

    if origin \== 'upper':
        bottom, top \= top, bottom

    return {
        "\[0, 0\]": (left, bottom),
        "\[M', 0\]": (left, top),
        "\[0, N'\]": (right, bottom),
        "\[M', N'\]": (right, top),
    }\[index\]

def get\_index\_label\_pos(index, extent, origin, inverted\_xindex):
    """
    Return the desired position and horizontal alignment of an index label.
    """
    if extent is None:
        extent \= lookup\_extent(origin)
    left, right, bottom, top \= extent
    x, y \= index\_to\_coordinate(index, extent, origin)

    is\_x0 \= index\[\-2:\] \== "0\]"
    halign \= 'left' if is\_x0 ^ inverted\_xindex else 'right'
    hshift \= 0.5 \* [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(left \- right)
    x += hshift \* (1 if is\_x0 else \-1)
    return x, y, halign

def get\_color(index, data, cmap):
    """Return the data color of an index."""
    val \= {
        "\[0, 0\]": data\[0, 0\],
        "\[0, N'\]": data\[0, \-1\],
        "\[M', 0\]": data\[\-1, 0\],
        "\[M', N'\]": data\[\-1, \-1\],
    }\[index\]
    return cmap(val / data.max())

def lookup\_extent(origin):
    """Return extent for label positioning when not given explicitly."""
    if origin \== 'lower':
        return (\-0.5, 6.5, \-0.5, 5.5)
    else:
        return (\-0.5, 6.5, 5.5, \-0.5)

def set\_extent\_None\_text(ax):
    ax.text(3, 2.5, 'equals\\nextent=None', size\='large',
            ha\='center', va\='center', color\='w')

def plot\_imshow\_with\_labels(ax, data, extent, origin, xlim, ylim):
    """Actually run \`\`imshow()\`\` and add extent and index labels."""
    im \= ax.imshow(data, origin\=origin, extent\=extent)

    \# extent labels (left, right, bottom, top)
    left, right, bottom, top \= im.get\_extent()
    if xlim is None or top \> bottom:
        upper\_string, lower\_string \= 'top', 'bottom'
    else:
        upper\_string, lower\_string \= 'bottom', 'top'
    if ylim is None or left < right:
        port\_string, starboard\_string \= 'left', 'right'
        inverted\_xindex \= False
    else:
        port\_string, starboard\_string \= 'right', 'left'
        inverted\_xindex \= True
    bbox\_kwargs \= {'fc': 'w', 'alpha': .75, 'boxstyle': "round4"}
    ann\_kwargs \= {'xycoords': 'axes fraction',
                  'textcoords': 'offset points',
                  'bbox': bbox\_kwargs}
    ax.annotate(upper\_string, xy\=(.5, 1), xytext\=(0, \-1),
                ha\='center', va\='top', \*\*ann\_kwargs)
    ax.annotate(lower\_string, xy\=(.5, 0), xytext\=(0, 1),
                ha\='center', va\='bottom', \*\*ann\_kwargs)
    ax.annotate(port\_string, xy\=(0, .5), xytext\=(1, 0),
                ha\='left', va\='center', rotation\=90,
                \*\*ann\_kwargs)
    ax.annotate(starboard\_string, xy\=(1, .5), xytext\=(\-1, 0),
                ha\='right', va\='center', rotation\=-90,
                \*\*ann\_kwargs)
    ax.set\_title(f'origin: {origin}')

    \# index labels
    for index in \["\[0, 0\]", "\[0, N'\]", "\[M', 0\]", "\[M', N'\]"\]:
        tx, ty, halign \= get\_index\_label\_pos(index, extent, origin,
                                             inverted\_xindex)
        facecolor \= get\_color(index, data, im.get\_cmap())
        ax.text(tx, ty, index, color\='white', ha\=halign, va\='center',
                bbox\={'boxstyle': 'square', 'facecolor': facecolor})
    if xlim:
        ax.set\_xlim(\*xlim)
    if ylim:
        ax.set\_ylim(\*ylim)

def generate\_imshow\_demo\_grid([extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, xlim\=None, ylim\=None):
    N \= len([extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(tight\_layout\=True)
    fig.set\_size\_inches(6, N \* (11.25) / 5)
    gs \= [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(N, 5, figure\=fig)

    [columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'label': \[fig.add\_subplot(gs\[j, 0\]) for j in range(N)\],
               'upper': \[fig.add\_subplot(gs\[j, 1:3\]) for j in range(N)\],
               'lower': \[fig.add\_subplot(gs\[j, 3:5\]) for j in range(N)\]}
    x, y \= [np.ogrid](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
\[0:6, 0:7\]
    data \= x + y

    for origin in \['upper', 'lower'\]:
        for ax, extent in zip([columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[origin\], [extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
            plot\_imshow\_with\_labels(ax, data, extent, origin, xlim, ylim)

    [columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['label'\]\[0\].set\_title('extent=')
    for ax, extent in zip([columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['label'\], [extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        if extent is None:
            text \= 'None'
        else:
            left, right, bottom, top \= extent
            text \= (f'left: {left:0.1f}\\nright: {right:0.1f}\\n'
                    f'bottom: {bottom:0.1f}\\ntop: {top:0.1f}\\n')
        ax.text(1., .5, text, transform\=ax.transAxes, ha\='right', va\='center')
        ax.axis('off')
    return [columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")

Default extent[#](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#default-extent "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

First, let's have a look at the default `extent=None`

generate\_imshow\_demo\_grid([extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[None\])

![extent=, origin: upper, origin: lower](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_001_2_00x.png)

Generally, for an array of shape (M, N), the first index runs along the vertical, the second index runs along the horizontal. The pixel centers are at integer positions ranging from 0 to `N' = N - 1` horizontally and from 0 to `M' = M - 1` vertically. _origin_ determines how the data is filled in the bounding box.

For `origin='lower'`:

*   \[0, 0\] is at (left, bottom)
    
*   \[M', 0\] is at (left, top)
    
*   \[0, N'\] is at (right, bottom)
    
*   \[M', N'\] is at (right, top)
    

`origin='upper'` reverses the vertical axes direction and filling:

*   \[0, 0\] is at (left, top)
    
*   \[M', 0\] is at (left, bottom)
    
*   \[0, N'\] is at (right, top)
    
*   \[M', N'\] is at (right, bottom)
    

In summary, the position of the \[0, 0\] index as well as the extent are influenced by _origin_:

| origin | \[0, 0\] position | extent |
| --- | --- | --- |
| upper | top left | `(-0.5, numcols-0.5, numrows-0.5, -0.5)` |
| lower | bottom left | `(-0.5, numcols-0.5, -0.5, numrows-0.5)` |

The default value of _origin_ is set by `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`) which defaults to `'upper'` to match the matrix indexing conventions in math and computer graphics image indexing conventions.

Explicit extent[#](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#explicit-extent "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

By setting _extent_ we define the coordinates of the image area. The underlying image data is interpolated/resampled to fill that area.

If the Axes is set to autoscale, then the view limits of the Axes are set to match the _extent_ which ensures that the coordinate set by `(left, bottom)` is at the bottom left of the Axes! However, this may invert the axis so they do not increase in the 'natural' direction.

[extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(\-0.5, 6.5, \-0.5, 5.5),\
           (\-0.5, 6.5, 5.5, \-0.5),\
           (6.5, \-0.5, \-0.5, 5.5),\
           (6.5, \-0.5, 5.5, \-0.5)\]

[columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= generate\_imshow\_demo\_grid([extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
set\_extent\_None\_text([columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['upper'\]\[1\])
set\_extent\_None\_text([columns](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['lower'\]\[0\])

![extent=, origin: upper, origin: upper, origin: upper, origin: upper, origin: lower, origin: lower, origin: lower, origin: lower](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_002_2_00x.png)

Explicit extent and axes limits[#](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#explicit-extent-and-axes-limits "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

If we fix the axes limits by explicitly setting [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 / [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
, we force a certain size and orientation of the Axes. This can decouple the 'left-right' and 'top-bottom' sense of the image from the orientation on the screen.

In the example below we have chosen the limits slightly larger than the extent (note the white areas within the Axes).

While we keep the extents as in the examples before, the coordinate (0, 0) is now explicitly put at the bottom left and values increase to up and to the right (from the viewer's point of view). We can see that:

*   The coordinate `(left, bottom)` anchors the image which then fills the box going towards the `(right, top)` point in data space.
    
*   The first column is always closest to the 'left'.
    
*   _origin_ controls if the first row is closest to 'top' or 'bottom'.
    
*   The image may be inverted along either direction.
    
*   The 'left-right' and 'top-bottom' sense of the image may be uncoupled from the orientation on the screen.
    

generate\_imshow\_demo\_grid([extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[None\] + [extents](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                          xlim\=(\-2, 8), ylim\=(\-1, 6))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![extent=, origin: upper, origin: upper, origin: upper, origin: upper, origin: upper, origin: lower, origin: lower, origin: lower, origin: lower, origin: lower](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_003_2_00x.png)

**Total running time of the script:** (0 minutes 7.539 seconds)

[`Download Jupyter notebook: imshow_extent.ipynb`](https://matplotlib.org/stable/_downloads/ea3ff0e893d2ed62fab9c394e239acae/imshow_extent.ipynb)

[`Download Python source code: imshow_extent.py`](https://matplotlib.org/stable/_downloads/43950b7f379de8f06a65b585ed9a472e/imshow_extent.py)

[`Download zipped: imshow_extent.zip`](https://matplotlib.org/stable/_downloads/f3831234a7995f9841f0ed9b21e47b9e/imshow_extent.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page