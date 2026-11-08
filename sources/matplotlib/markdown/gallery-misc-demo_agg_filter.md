[Skip to main content](https://matplotlib.org/stable/gallery/misc/demo_agg_filter.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/demo_agg_filter.html#sphx-glr-download-gallery-misc-demo-agg-filter-py)
 to download the full example code.

AGG filter[#](https://matplotlib.org/stable/gallery/misc/demo_agg_filter.html#agg-filter "Link to this heading")

=================================================================================================================

Most pixel-based backends in Matplotlib use [Anti-Grain Geometry (AGG)](http://agg.sourceforge.net/antigrain.com)
 for rendering. You can modify the rendering of Artists by applying a filter via [`Artist.set_agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter")
.

![demo agg filter](https://matplotlib.org/stable/_images/sphx_glr_demo_agg_filter_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.artist import [Artist](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
from matplotlib.colors import [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
import matplotlib.transforms as mtransforms

def smooth1d(x, window\_len):
    \# copied from https://scipy-cookbook.readthedocs.io/items/SignalSmooth.html
    s \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[2\*x\[0\] \- x\[window\_len:1:\-1\], x, 2\*x\[\-1\] \- x\[\-1:\-window\_len:\-1\]\]
    w \= [np.hanning](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy.hanning "numpy.hanning")
(window\_len)
    y \= [np.convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
(w/w.sum(), s, mode\='same')
    return y\[window\_len\-1:\-window\_len+1\]

def smooth2d(A, sigma\=3):
    window\_len \= max(int(sigma), 3) \* 2 + 1
    A \= [np.apply\_along\_axis](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis")
(smooth1d, 0, A, window\_len)
    A \= [np.apply\_along\_axis](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis")
(smooth1d, 1, A, window\_len)
    return A

class BaseFilter:

    def get\_pad(self, dpi):
        return 0

    def process\_image(self, padded\_src, dpi):
        raise NotImplementedError("Should be overridden by subclasses")

    def \_\_call\_\_(self, im, dpi):
        pad \= self.get\_pad(dpi)
        padded\_src \= [np.pad](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy.pad "numpy.pad")
(im, \[(pad, pad), (pad, pad), (0, 0)\], "constant")
        tgt\_image \= self.process\_image(padded\_src, dpi)
        return tgt\_image, \-pad, \-pad

class OffsetFilter(BaseFilter):

    def \_\_init\_\_(self, offsets\=(0, 0)):
        self.offsets \= offsets

    def get\_pad(self, dpi):
        return int(max(self.offsets) / 72 \* dpi)

    def process\_image(self, padded\_src, dpi):
        ox, oy \= self.offsets
        a1 \= [np.roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "numpy.roll")
(padded\_src, int(ox / 72 \* dpi), axis\=1)
        a2 \= [np.roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "numpy.roll")
(a1, \-int(oy / 72 \* dpi), axis\=0)
        return a2

class GaussianFilter(BaseFilter):
    """Simple Gaussian filter."""

    def \_\_init\_\_(self, sigma, alpha\=0.5, color\=(0, 0, 0)):
        self.sigma \= sigma
        self.alpha \= alpha
        self.color \= color

    def get\_pad(self, dpi):
        return int(self.sigma\*3 / 72 \* dpi)

    def process\_image(self, padded\_src, dpi):
        tgt\_image \= [np.empty\_like](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")
(padded\_src)
        tgt\_image\[:, :, :3\] \= self.color
        tgt\_image\[:, :, 3\] \= smooth2d(padded\_src\[:, :, 3\] \* self.alpha,
                                      self.sigma / 72 \* dpi)
        return tgt\_image

class DropShadowFilter(BaseFilter):

    def \_\_init\_\_(self, sigma, alpha\=0.3, color\=(0, 0, 0), offsets\=(0, 0)):
        self.gauss\_filter \= GaussianFilter(sigma, alpha, color)
        self.offset\_filter \= OffsetFilter(offsets)

    def get\_pad(self, dpi):
        return max(self.gauss\_filter.get\_pad(dpi),
                   self.offset\_filter.get\_pad(dpi))

    def process\_image(self, padded\_src, dpi):
        t1 \= self.gauss\_filter.process\_image(padded\_src, dpi)
        t2 \= self.offset\_filter.process\_image(t1, dpi)
        return t2

class LightFilter(BaseFilter):
    """Apply LightSource filter"""

    def \_\_init\_\_(self, sigma, fraction\=1):
        """
        Parameters
        ----------
        sigma : float
            sigma for gaussian filter
        fraction: number, default: 1
            Increases or decreases the contrast of the hillshade.
            See \`matplotlib.colors.LightSource\`

        """
        self.gauss\_filter \= GaussianFilter(sigma, alpha\=1)
        self.light\_source \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
()
        self.fraction \= fraction

    def get\_pad(self, dpi):
        return self.gauss\_filter.get\_pad(dpi)

    def process\_image(self, padded\_src, dpi):
        t1 \= self.gauss\_filter.process\_image(padded\_src, dpi)
        elevation \= t1\[:, :, 3\]
        rgb \= padded\_src\[:, :, :3\]
        alpha \= padded\_src\[:, :, 3:\]
        rgb2 \= self.light\_source.shade\_rgb(rgb, elevation,
                                           fraction\=self.fraction,
                                           blend\_mode\="overlay")
        return [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[rgb2, alpha\], \-1)

class GrowFilter(BaseFilter):
    """Enlarge the area."""

    def \_\_init\_\_(self, pixels, color\=(1, 1, 1)):
        self.pixels \= pixels
        self.color \= color

    def \_\_call\_\_(self, im, dpi):
        alpha \= [np.pad](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy.pad "numpy.pad")
(im\[..., 3\], self.pixels, "constant")
        alpha2 \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(smooth2d(alpha, self.pixels / 72 \* dpi) \* 5, 0, 1)
        new\_im \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
((\*alpha2.shape, 4))
        new\_im\[:, :, :3\] \= self.color
        new\_im\[:, :, 3\] \= alpha2
        offsetx, offsety \= \-self.pixels, \-self.pixels
        return new\_im, offsetx, offsety

class FilteredArtistList([Artist](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
):
    """A simple container to filter multiple artists at once."""

    def \_\_init\_\_(self, artist\_list, filter):
        super().\_\_init\_\_()
        self.\_artist\_list \= artist\_list
        self.\_filter \= filter

    def draw(self, renderer):
        renderer.start\_rasterizing()
        renderer.start\_filter()
        for a in self.\_artist\_list:
            a.draw(renderer)
        renderer.stop\_filter(self.\_filter)
        renderer.stop\_rasterizing()

def filtered\_text(ax):
    \# mostly copied from contour\_demo.py

    \# prepare image
    delta \= 0.025
    x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, delta)
    y \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2.0, 2.0, delta)
    X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(x, y)
    Z1 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-X\*\*2 \- Y\*\*2)
    Z2 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(X \- 1)\*\*2 \- (Y \- 1)\*\*2)
    Z \= (Z1 \- Z2) \* 2

    \# draw
    ax.imshow(Z, interpolation\='bilinear', origin\='lower',
              cmap\="gray", extent\=(\-3, 3, \-2, 2), aspect\='auto')
    levels \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-1.2, 1.6, 0.2)
    CS \= ax.contour(Z, levels,
                    origin\='lower',
                    linewidths\=2,
                    extent\=(\-3, 3, \-2, 2))

    \# contour label
    cl \= ax.clabel(CS, levels\[1::2\],  \# label every second level
                   fmt\='%1.1f',
                   fontsize\=11)

    \# change clabel color to black
    from matplotlib.patheffects import [Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")
    for t in cl:
        t.set\_color("k")
        \# to force TextPath (i.e., same font in all backends)
        t.set\_path\_effects(\[[Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")\
()\])

    \# Add white glows to improve visibility of labels.
    white\_glows \= [FilteredArtistList](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
(cl, GrowFilter(3))
    ax.add\_artist(white\_glows)
    white\_glows.set\_zorder(cl\[0\].get\_zorder() \- 0.1)

    ax.xaxis.set\_visible(False)
    ax.yaxis.set\_visible(False)

def drop\_shadow\_line(ax):
    \# copied from examples/misc/svg\_filter\_line.py

    \# draw lines
    l1, \= ax.plot(\[0.1, 0.5, 0.9\], \[0.1, 0.9, 0.5\], "bo-")
    l2, \= ax.plot(\[0.1, 0.5, 0.9\], \[0.5, 0.2, 0.7\], "ro-")

    gauss \= DropShadowFilter(4)

    for l in \[l1, l2\]:

        \# draw shadows with same lines with slight offset.
        xx \= l.get\_xdata()
        yy \= l.get\_ydata()
        shadow, \= ax.plot(xx, yy)
        shadow.update\_from(l)

        \# offset transform
        transform \= [mtransforms.offset\_copy](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
(l.get\_transform(), ax.figure,
                                            x\=4.0, y\=-6.0, units\='points')
        shadow.set\_transform(transform)

        \# adjust zorder of the shadow lines so that it is drawn below the
        \# original lines
        shadow.set\_zorder(l.get\_zorder() \- 0.5)
        shadow.set\_agg\_filter(gauss)
        shadow.set\_rasterized(True)  \# to support mixed-mode renderers

    ax.set\_xlim(0., 1.)
    ax.set\_ylim(0., 1.)

    ax.xaxis.set\_visible(False)
    ax.yaxis.set\_visible(False)

def drop\_shadow\_patches(ax):
    \# Copied from barchart\_demo.py
    N \= 5
    group1\_means \= \[20, 35, 30, 35, 27\]

    ind \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(N)  \# the x locations for the groups
    width \= 0.35  \# the width of the bars

    rects1 \= ax.bar(ind, group1\_means, width, color\='r', ec\="w", lw\=2)

    group2\_means \= \[25, 32, 34, 20, 25\]
    rects2 \= ax.bar(ind + width + 0.1, group2\_means, width,
                    color\='y', ec\="w", lw\=2)

    drop \= DropShadowFilter(5, offsets\=(1, 1))
    shadow \= [FilteredArtistList](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
(rects1 + rects2, drop)
    ax.add\_artist(shadow)
    shadow.set\_zorder(rects1\[0\].get\_zorder() \- 0.1)

    ax.set\_ylim(0, 40)

    ax.xaxis.set\_visible(False)
    ax.yaxis.set\_visible(False)

def light\_filter\_pie(ax):
    fracs \= \[15, 30, 45, 10\]
    explode \= (0.1, 0.2, 0.1, 0.1)
    pie \= ax.pie(fracs, explode\=explode)

    light\_filter \= LightFilter(9)
    for p in pie.wedges:
        p.set\_agg\_filter(light\_filter)
        p.set\_rasterized(True)  \# to support mixed-mode renderers
        p.set(ec\="none",
              lw\=2)

    gauss \= DropShadowFilter(9, offsets\=(3, \-4), alpha\=0.7)
    shadow \= [FilteredArtistList](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
(pie.wedges, gauss)
    ax.add\_artist(shadow)
    shadow.set\_zorder(pie.wedges\[0\].get\_zorder() \- 0.1)

if \_\_name\_\_ \== "\_\_main\_\_":

    [fix](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)

    filtered\_text([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\])
    drop\_shadow\_line([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\])
    drop\_shadow\_patches([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\])
    light\_filter\_pie([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\])
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_frame\_on(True)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.764 seconds)

[`Download Jupyter notebook: demo_agg_filter.ipynb`](https://matplotlib.org/stable/_downloads/749f62f8c73dbbf0d0835f1a8410a38a/demo_agg_filter.ipynb)

[`Download Python source code: demo_agg_filter.py`](https://matplotlib.org/stable/_downloads/5787bdd3c2fb5d84c40860c89508a642/demo_agg_filter.py)

[`Download zipped: demo_agg_filter.zip`](https://matplotlib.org/stable/_downloads/13d11f169f949f5d5b96d6ba37f708d6/demo_agg_filter.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)