[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html#sphx-glr-download-gallery-subplots-axes-and-figures-axes-zoom-effect-py)
 to download the full example code.

Axes zoom effect[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html#axes-zoom-effect "Link to this heading")

===================================================================================================================================================

import matplotlib.pyplot as plt

from matplotlib.transforms import Bbox, [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
, [blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
from mpl\_toolkits.axes\_grid1.inset\_locator import ([BboxConnector](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnector.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnector "mpl_toolkits.axes_grid1.inset_locator.BboxConnector")
, [BboxConnectorPatch](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch "mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch")
,
                                                   [BboxPatch](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxPatch "mpl_toolkits.axes_grid1.inset_locator.BboxPatch")
)

def connect\_bbox(bbox1, bbox2,
                 loc1a, loc2a, loc1b, loc2b,
                 prop\_lines, prop\_patches\=None):
    if prop\_patches is None:
        prop\_patches \= {
            \*\*prop\_lines,
            "alpha": prop\_lines.get("alpha", 1) \* 0.2,
            "clip\_on": False,
        }

    c1 \= [BboxConnector](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnector.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnector "mpl_toolkits.axes_grid1.inset_locator.BboxConnector")
(
        bbox1, bbox2, loc1\=loc1a, loc2\=loc2a, clip\_on\=False, \*\*prop\_lines)
    c2 \= [BboxConnector](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnector.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnector "mpl_toolkits.axes_grid1.inset_locator.BboxConnector")
(
        bbox1, bbox2, loc1\=loc1b, loc2\=loc2b, clip\_on\=False, \*\*prop\_lines)

    bbox\_patch1 \= [BboxPatch](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxPatch "mpl_toolkits.axes_grid1.inset_locator.BboxPatch")
(bbox1, \*\*prop\_patches)
    bbox\_patch2 \= [BboxPatch](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxPatch "mpl_toolkits.axes_grid1.inset_locator.BboxPatch")
(bbox2, \*\*prop\_patches)

    p \= [BboxConnectorPatch](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch "mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch")
(bbox1, bbox2,
                           loc1a\=loc1a, loc2a\=loc2a, loc1b\=loc1b, loc2b\=loc2b,
                           clip\_on\=False,
                           \*\*prop\_patches)

    return c1, c2, bbox\_patch1, bbox\_patch2, p

def zoom\_effect01(ax1, ax2, xmin, xmax, \*\*kwargs):
    """
    Connect \*ax1\* and \*ax2\*. The \*xmin\*-to-\*xmax\* range in both Axes will
    be marked.

    Parameters
    ----------
    ax1
        The main Axes.
    ax2
        The zoomed Axes.
    xmin, xmax
        The limits of the colored area in both plot Axes.
    \*\*kwargs
        Arguments passed to the patch constructor.
    """

    bbox \= [Bbox.from\_extents](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_extents "matplotlib.transforms.Bbox.from_extents")
(xmin, 0, xmax, 1)

    mybbox1 \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
(bbox, ax1.get\_xaxis\_transform())
    mybbox2 \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
(bbox, ax2.get\_xaxis\_transform())

    prop\_patches \= {\*\*kwargs, "ec": "none", "alpha": 0.2}

    c1, c2, bbox\_patch1, bbox\_patch2, p \= connect\_bbox(
        mybbox1, mybbox2,
        loc1a\=3, loc2a\=2, loc1b\=4, loc2b\=1,
        prop\_lines\=kwargs, prop\_patches\=prop\_patches)

    ax1.add\_patch(bbox\_patch1)
    ax2.add\_patch(bbox\_patch2)
    ax2.add\_patch(c1)
    ax2.add\_patch(c2)
    ax2.add\_patch(p)

    return c1, c2, bbox\_patch1, bbox\_patch2, p

def zoom\_effect02(ax1, ax2, \*\*kwargs):
    """
    ax1 : the main Axes
    ax1 : the zoomed Axes

    Similar to zoom\_effect01.  The xmin & xmax will be taken from the
    ax1.viewLim.
    """

    tt \= ax1.transScale + (ax1.transLimits + ax2.transAxes)
    trans \= [blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
(ax2.transData, tt)

    mybbox1 \= ax1.bbox
    mybbox2 \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
(ax1.viewLim, trans)

    prop\_patches \= {\*\*kwargs, "ec": "none", "alpha": 0.2}

    c1, c2, bbox\_patch1, bbox\_patch2, p \= connect\_bbox(
        mybbox1, mybbox2,
        loc1a\=3, loc2a\=2, loc1b\=4, loc2b\=1,
        prop\_lines\=kwargs, prop\_patches\=prop\_patches)

    ax1.add\_patch(bbox\_patch1)
    ax2.add\_patch(bbox\_patch2)
    ax2.add\_patch(c1)
    ax2.add\_patch(c2)
    ax2.add\_patch(p)

    return c1, c2, bbox\_patch1, bbox\_patch2, p

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().subplot\_mosaic(\[\
    \["zoom1", "zoom2"\],\
    \["main", "main"\],\
\])

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["main"\].set(xlim\=(0, 5))
zoom\_effect01([axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["zoom1"\], [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["main"\], 0.2, 0.8)
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["zoom2"\].set(xlim\=(2, 3))
zoom\_effect02([axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["zoom2"\], [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["main"\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes zoom effect](https://matplotlib.org/stable/_images/sphx_glr_axes_zoom_effect_001_2_00x.png)

Tags: [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [component: transform](https://matplotlib.org/stable/_tags/component-transform.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

[`Download Jupyter notebook: axes_zoom_effect.ipynb`](https://matplotlib.org/stable/_downloads/54ca8f70991224d0d2325d48314a3ce5/axes_zoom_effect.ipynb)

[`Download Python source code: axes_zoom_effect.py`](https://matplotlib.org/stable/_downloads/9d8894d6769fb413514179203a72d47d/axes_zoom_effect.py)

[`Download zipped: axes_zoom_effect.zip`](https://matplotlib.org/stable/_downloads/08b42a743e5745300138fd7347d07d8b/axes_zoom_effect.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)