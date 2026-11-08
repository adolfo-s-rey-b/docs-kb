[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#main-content)

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
    

[What's new in Matplotlib 3.8.0 (Sept 13, 2023)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#what-s-new-in-matplotlib-3-8-0-sept-13-2023 "Link to this heading")

==================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Type Hints](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#type-hints "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib now provides first-party PEP484 style type hints files for most public APIs.

While still considered provisional and subject to change (and sometimes we are not quite able to fully specify what we would like to), they should provide a reasonable basis to type check many common usage patterns, as well as integrating with many editors/IDEs.

[Plotting and Annotation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#plotting-and-annotation-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Support customizing antialiasing for text and annotation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#support-customizing-antialiasing-for-text-and-annotation "Link to this heading")

`matplotlib.pyplot.annotate()` and `matplotlib.pyplot.text()` now support parameter _antialiased_. When _antialiased_ is set to `True`, antialiasing will be applied to the text. When _antialiased_ is set to `False`, antialiasing will not be applied to the text. When _antialiased_ is not specified, antialiasing will be set by `[rcParams["text.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.antialiased#rcparam-text-antialiased) ` (default: `True`) at the creation time of `Text` and `Annotation` object. Examples:

mpl.text.Text(.5, .5, "foo\\nbar", antialiased\=True)
plt.text(0.5, 0.5, '6 inches x 2 inches', antialiased\=True)
ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5), antialiased\=False)

If the text contains math expression, _antialiased_ applies to the whole text. Examples:

\# no part will be antialiased for the text below
plt.text(0.5, 0.25, r"$I'm \\sqrt{x}$", antialiased\=False)

Also note that antialiasing for tick labels will be set with `[rcParams["text.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.antialiased#rcparam-text-antialiased) ` (default: `True`) when they are created (usually when a `Figure` is created) and cannot be changed afterwards.

Furthermore, with this new feature, you may want to make sure that you are creating and saving/showing the figure under the same context:

\# previously this was a no-op, now it is what works
with rccontext(text.antialiased\=False):
    fig, ax \= plt.subplots()
    ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5))
    fig.savefig('/tmp/test.png')

\# previously this had an effect, now this is a no-op
fig, ax \= plt.subplots()
ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5))
with rccontext(text.antialiased\=False):
    fig.savefig('/tmp/test.png')

### [rcParams for `AutoMinorLocator` divisions](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#rcparams-for-autominorlocator-divisions "Link to this heading")

The rcParams `[rcParams["xtick.minor.ndivs"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.minor.ndivs#rcparam-xtick-minor-ndivs) ` (default: `'auto'`) and `[rcParams["ytick.minor.ndivs"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.minor.ndivs#rcparam-ytick-minor-ndivs) ` (default: `'auto'`) have been added to enable setting the default number of divisions; if set to `auto`, the number of divisions will be chosen by the distance between major ticks.

### [Axline setters and getters](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#axline-setters-and-getters "Link to this heading")

The returned object from [`axes.Axes.axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
 now supports getter and setter methods for its _xy1_, _xy2_ and _slope_ attributes:

line1.get\_xy1()
line1.get\_slope()
line2.get\_xy2()

line1.set\_xy1(.2, .3)
line1.set\_slope(2.4)
line2.set\_xy2(.1, .6)

### [Clipping for contour plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#clipping-for-contour-plots "Link to this heading")

[`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 now accept the _clip\_path_ parameter.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x \= y \= np.arange(\-3.0, 3.01, 0.025)
X, Y \= np.meshgrid(x, y)
Z1 \= np.exp(\-X\*\*2 \- Y\*\*2)
Z2 \= np.exp(\-(X \- 1)\*\*2 \- (Y \- 1)\*\*2)
Z \= (Z1 \- Z2) \* 2

fig, ax \= plt.subplots()
patch \= mpatches.RegularPolygon((0, 0), 5, radius\=2,
                                transform\=ax.transData)
ax.contourf(X, Y, Z, clip\_path\=patch)

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/9056f0bddfeac233b1205150bb379063/whats_new_3-8-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/849602aa62d06c8a2fbbc9b9250831fb/whats_new_3-8-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/923f960330f4a6be97ef8f37c5c0e086/whats_new_3-8-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-1.2x.png)

### [`Axes.ecdf`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#axes-ecdf "Link to this heading")

A new Axes method, [`ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html#matplotlib.axes.Axes.ecdf "matplotlib.axes.Axes.ecdf")
, allows plotting empirical cumulative distribution functions without any binning.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots()
ax.ecdf(np.random.randn(100))

([`Source code`](https://matplotlib.org/stable/_downloads/2bdbe9fdb77784bd7129483eb33c47e6/whats_new_3-8-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/abed795d302f8c7015df1e8ba5d7929e/whats_new_3-8-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a1f12c9a152b3927fe432b9851112295/whats_new_3-8-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-2.2x.png)

### [`Figure.get_suptitle()`, `Figure.get_supxlabel()`, `Figure.get_supylabel()`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#figure-get-suptitle-figure-get-supxlabel-figure-get-supylabel "Link to this heading")

These methods return the strings set by `Figure.suptitle()`, `Figure.supxlabel()` and `Figure.supylabel()` respectively.

### [`Ellipse.get_vertices()`, `Ellipse.get_co_vertices()`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#ellipse-get-vertices-ellipse-get-co-vertices "Link to this heading")

These methods return the coordinates of ellipse vertices of major and minor axis. Additionally, an example gallery demo is added which shows how to add an arrow to an ellipse showing a clockwise or counter-clockwise rotation of the ellipse. To place the arrow exactly on the ellipse, the coordinates of the vertices are used.

### [Remove inner ticks in `label_outer()`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#remove-inner-ticks-in-label-outer "Link to this heading")

Up to now, `label_outer()` has only removed the ticklabels. The ticks lines were left visible. This is now configurable through a new parameter `label_outer(remove_inner_ticks=True)`.

import numpy as np
import matplotlib.pyplot as plt

x \= np.linspace(0, 2 \* np.pi, 100)

fig, axs \= plt.subplots(2, 2, sharex\=True, sharey\=True,
                        gridspec\_kw\=dict(hspace\=0, wspace\=0))

axs\[0, 0\].plot(x, np.sin(x))
axs\[0, 1\].plot(x, np.cos(x))
axs\[1, 0\].plot(x, \-np.cos(x))
axs\[1, 1\].plot(x, \-np.sin(x))

for ax in axs.flat:
    ax.grid(color\='0.9')
    ax.label\_outer(remove\_inner\_ticks\=True)

([`Source code`](https://matplotlib.org/stable/_downloads/bb4a48100095c36a5a584ce5309711f1/whats_new_3-8-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ebe7863549e655c4120eefde3c49ae1f/whats_new_3-8-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e59eb8b0b99f3907abe13ce0528fab8c/whats_new_3-8-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-3.2x.png)

### [Configurable legend shadows](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#configurable-legend-shadows "Link to this heading")

The _shadow_ parameter of legends now accepts dicts in addition to booleans. Dictionaries can contain any keywords for [`patches.Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
. For example, this allows one to set the color and/or the transparency of a legend shadow:

ax.legend(loc\='center left', shadow\={'color': 'red', 'alpha': 0.5})

and to control the shadow location:

ax.legend(loc\='center left', shadow\={"ox":20, "oy":\-20})

Configuration is currently not supported via `[rcParams["legend.shadow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.shadow#rcparam-legend-shadow) ` (default: `False`).

### [`offset` parameter for MultipleLocator](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#offset-parameter-for-multiplelocator "Link to this heading")

An _offset_ may now be specified to shift all the ticks by the given value.

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

\_, ax \= plt.subplots()
ax.plot(range(10))
locator \= mticker.MultipleLocator(base\=3, offset\=0.3)
ax.xaxis.set\_major\_locator(locator)

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/4b5d66b3f8cf6902e6ff327479da4cb1/whats_new_3-8-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/cde1b90687b5fb120e3afce21c699b55/whats_new_3-8-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/34de6fa6fd13ad2217c17dc18b7f2fab/whats_new_3-8-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-4.2x.png)

### [Add a new valid color format `(matplotlib_color, alpha)`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#add-a-new-valid-color-format-matplotlib-color-alpha "Link to this heading")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax \= plt.subplots()

rectangle \= Rectangle((.2, .2), .6, .6,
                      facecolor\=('blue', 0.2),
                      edgecolor\=('green', 0.5))
ax.add\_patch(rectangle)

([`Source code`](https://matplotlib.org/stable/_downloads/9c1f60bd79b51f6eda420d908c5aeacf/whats_new_3-8-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b3a420e69c4822c87836ea6e5823ac57/whats_new_3-8-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6d558efd7a432a93ca461c20cdf6a8b2/whats_new_3-8-0-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-5.2x.png)

Users can define a color using the new color specification, _(matplotlib\_color, alpha)_. Note that an explicit alpha keyword argument will override an alpha value from _(matplotlib\_color, alpha)_.

### [The pie chart shadow can be controlled](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#the-pie-chart-shadow-can-be-controlled "Link to this heading")

The _shadow_ argument to [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 can now be a dict, allowing more control of the [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
\-patch used.

### [`PolyQuadMesh` is a new class for drawing quadrilateral meshes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#polyquadmesh-is-a-new-class-for-drawing-quadrilateral-meshes "Link to this heading")

[`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 previously returned a flattened [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 with only the valid polygons (unmasked) contained within it. Now, we return a [`PolyQuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyQuadMesh "matplotlib.collections.PolyQuadMesh")
, which is a mixin incorporating the usefulness of 2D array and mesh coordinates handling, but still inheriting the draw methods of [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
, which enables more control over the rendering properties than a normal [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 that is returned from [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
. The new class subclasses [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 and thus should still behave the same as before. This new class keeps track of the mask for the user and updates the Polygons that are sent to the renderer appropriately.

([`Source code`](https://matplotlib.org/stable/_downloads/d9b98d2c3c4288cdce4792bc95b7c663/whats_new_3-8-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/658753cb57e4203a37690e29609a460d/whats_new_3-8-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/065bac82ccb7bd185fc2e62db14ca332/whats_new_3-8-0-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-6.2x.png)

### [Shadow shade can be controlled](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#shadow-shade-can-be-controlled "Link to this heading")

The [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 patch now has a _shade_ argument to control the shadow darkness. If 1, the shadow is black, if 0, the shadow has the same color as the patch that is shadowed. The default value, which earlier was fixed, is 0.7.

### [`SpinesProxy` now supports calling the `set()` method](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#spinesproxy-now-supports-calling-the-set-method "Link to this heading")

One can now call e.g. `ax.spines[:].set(visible=False)`.

### [Allow setting the tick label fonts with a keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#allow-setting-the-tick-label-fonts-with-a-keyword-argument "Link to this heading")

`Axes.tick_params` now accepts a _labelfontfamily_ keyword that changes the tick label font separately from the rest of the text objects:

Axis.tick\_params(labelfontfamily\='monospace')

[Figure, Axes, and Legend Layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#figure-axes-and-legend-layout "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [pad\_inches="layout" for savefig](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#pad-inches-layout-for-savefig "Link to this heading")

When using constrained or compressed layout,

savefig(filename, bbox\_inches\="tight", pad\_inches\="layout")

will now use the padding sizes defined on the layout engine.

### [Add a public method to modify the location of `Legend`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#add-a-public-method-to-modify-the-location-of-legend "Link to this heading")

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 locations now can be tweaked after they've been defined.

from matplotlib import pyplot as plt

fig \= plt.figure()
ax \= fig.add\_subplot(1, 1, 1)

x \= list(range(\-100, 101))
y \= \[i\*\*2 for i in x\]

ax.plot(x, y, label\="f(x)")
ax.legend()
ax.get\_legend().set\_loc("right")
\# Or
\# ax.get\_legend().set(loc="right")

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/3c11c6ec3ef28a582bb43129826f1e3f/whats_new_3-8-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a38aa5ad0607674b0c318a56daafc069/whats_new_3-8-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d29b48ac05954041057f395abbd8b218/whats_new_3-8-0-7.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-7.2x.png)

### [`rcParams['legend.loc']` now accepts float-tuple inputs](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#rcparams-legend-loc-now-accepts-float-tuple-inputs "Link to this heading")

The `[rcParams["legend.loc"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.loc#rcparam-legend-loc) ` (default: `'best'`) rcParams now accepts float-tuple inputs, same as the _loc_ keyword argument to [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
. This allows users to set the location of the legend in a more flexible and consistent way.

[Mathtext improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Improvements are to Mathtext, Matplotlib's native TeX-like mathematics parser (see [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
, not to be confused with Matplotlib using LaTeX directly: [Text rendering with LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html#usetex)
).

### [Boldsymbol mathtext command `\boldsymbol`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#boldsymbol-mathtext-command-boldsymbol "Link to this heading")

Supports using the `\boldsymbol{}` command in mathtext:

To change symbols to bold enclose the text in a font command as shown:

r'$\\boldsymbol{a+2+\\alpha}$'

\\\[\\boldsymbol{a+2+\\alpha}\\\]

### [`mathtext` has more sizable delimiters](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-has-more-sizable-delimiters "Link to this heading")

The `\lgroup` and `\rgroup` sizable delimiters have been added.

The following delimiter names have been supported earlier, but can now be sized with `\left` and `\right`:

*   `\lbrace`, `\rbrace`, `\leftbrace`, and `\rightbrace`
    
*   `\lbrack` and `\rbrack`
    
*   `\leftparen` and `\rightparen`
    

There are really no obvious advantages in using these. Instead, they are added for completeness.

### [`mathtext` documentation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-documentation-improvements "Link to this heading")

The documentation is updated to take information directly from the parser. This means that (almost) all supported symbols, operators etc are shown at [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
.

### [`mathtext` now supports `\substack`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-now-supports-substack "Link to this heading")

`\substack` can be used to create multi-line subscripts or superscripts within an equation.

To use it to enclose the math in a substack command as shown:

r'$\\sum\_{\\substack{1\\leq i\\leq 3\\\\ 1\\leq j\\leq 5}}$'

![](https://matplotlib.org/stable/_images/mathmpl/math-7a015d497c-2x.png)

### [`mathtext` now supports `\middle` delimiter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-now-supports-middle-delimiter "Link to this heading")

The `\middle` delimiter has been added, and can now be used with the `\left` and `\right` delimiters:

To use the middle command enclose it in between the `\left` and `\right` delimiter command as shown:

r'$\\left( \\frac{a}{b} \\middle| q \\right)$'

![](https://matplotlib.org/stable/_images/mathmpl/math-2ad91a2086-2x.png)

### [`mathtext` operators](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-operators "Link to this heading")

There has been a number of operators added and corrected when a Unicode font is used. In addition, correct spacing has been added to a number of the previous operators. Especially, the characters used for `\gnapprox`, `\lnapprox`, `\leftangle`, and `\rightangle` have been corrected.

### [`mathtext` spacing corrections](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id31)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-spacing-corrections "Link to this heading")

As consequence of the updated documentation, the spacing on a number of relational and operator symbols were classified like that and therefore will be spaced properly.

### [`mathtext` now supports `\text`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id32)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#mathtext-now-supports-text "Link to this heading")

`\text` can be used to obtain upright text within an equation and to get a plain dash (-).

import matplotlib.pyplot as plt
plt.text(0.1, 0.5, r"$a = \\sin(\\phi) \\text{ such that } \\phi = \\frac{x}{y}$")
plt.text(0.1, 0.3, r"$\\text{dashes (-) are retained}$")

([`Source code`](https://matplotlib.org/stable/_downloads/51f3da82946d526c11a46e8b5358f564/whats_new_3-8-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/18c7db100cc962ffdb8828d85737256b/whats_new_3-8-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/29de7fccba59a1b0fa2d1ac72768ce56/whats_new_3-8-0-8.png)
)

[![Illustration of the newly added \text command, showing that it renders as normal text, including spaces, despite being part of an equation. Also show that a dash is not rendered as a minus when part of a \text command.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-8.2x.png)

### [Bold-italic mathtext command `\mathbfit`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id33)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#bold-italic-mathtext-command-mathbfit "Link to this heading")

Supports use of bold-italic font style in mathtext using the `\mathbfit{}` command:

To change font to bold and italic enclose the text in a font command as shown:

r'$\\mathbfit{\\eta \\leq C(\\delta(\\eta))}$

\\\[\\mathbfit{\\eta \\leq C(\\delta(\\eta))}\\\]

[3D plotting improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id34)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#d-plotting-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Specify ticks and axis label positions for 3D plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id35)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#specify-ticks-and-axis-label-positions-for-3d-plots "Link to this heading")

You can now specify the positions of ticks and axis labels for 3D plots.

import matplotlib.pyplot as plt

positions \= \['lower', 'upper', 'default', 'both', 'none'\]
fig, axs \= plt.subplots(2, 3, figsize\=(12, 8),
                        subplot\_kw\={'projection': '3d'})
for ax, pos in zip(axs.flatten(), positions):
    for axis in ax.xaxis, ax.yaxis, ax.zaxis:
        axis.set\_label\_position(pos)
        axis.set\_ticks\_position(pos)
    title \= f'position="{pos}"'
    ax.set(xlabel\='x', ylabel\='y', zlabel\='z', title\=title)
axs\[1, 2\].axis('off')

([`Source code`](https://matplotlib.org/stable/_downloads/32f010baa7fea8e0993998ca8a0d0772/whats_new_3-8-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1e291c758ca8c363199dfeaf52a42619/whats_new_3-8-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/69ff719e41050d98fd5757126356782c/whats_new_3-8-0-9.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-8-0-9.2x.png)

### [3D hover coordinates](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id36)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#d-hover-coordinates "Link to this heading")

The x, y, z coordinates displayed in 3D plots were previously showing nonsensical values. This has been fixed to report the coordinate on the view pane directly beneath the mouse cursor. This is likely to be most useful when viewing 3D plots along a primary axis direction when using an orthographic projection, or when a 2D plot has been projected onto one of the 3D axis panes. Note that there is still no way to directly display the coordinates of plotted data points.

### [3D plots can share view angles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id37)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#d-plots-can-share-view-angles "Link to this heading")

3D plots can now share the same view angles, so that when you rotate one plot the other plots also rotate. This can be done with the _shareview_ keyword argument when adding an axes, or by using the _ax1.shareview(ax2)_ method of existing 3D axes.

[Other improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id38)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#other-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [macosx: New figures can be opened in either windows or tabs](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id39)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#macosx-new-figures-can-be-opened-in-either-windows-or-tabs "Link to this heading")

There is a new `[rcParams["macosx.window_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=macosx.window_mode#rcparam-macosx-window-mode) ` (default: `'system'`) rcParam to control how new figures are opened with the macosx backend. The default is **system** which uses the system settings, or one can specify either **tab** or **window** to explicitly choose the mode used to open new figures.

### [`matplotlib.mpl_toolkits` is now an implicit namespace package](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id40)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#matplotlib-mpl-toolkits-is-now-an-implicit-namespace-package "Link to this heading")

Following the deprecation of `pkg_resources.declare_namespace` in `setuptools` 67.3.0, `matplotlib.mpl_toolkits` is now implemented as an implicit namespace, following [PEP 420](https://peps.python.org/pep-0420/)
.

### [Plot Directive now can make responsive images with "srcset"](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#id41)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.8.0.html#plot-directive-now-can-make-responsive-images-with-srcset "Link to this heading")

The plot sphinx directive (`matplotlib.sphinxext.plot_directive`, invoked in rst as `.. plot::`) can be configured to automatically make higher res figures and add these to the built html docs. In `conf.py`:

extensions \= \[\
...\
    'matplotlib.sphinxext.plot\_directive',\
    'matplotlib.sphinxext.figmpl\_directive',\
...\]

plot\_srcset \= \['2x'\]

will make png files with double the resolution for hiDPI displays. Resulting html files will have image entries like:

<img src\="../\_images/nestedpage-index-2.png" style\="" srcset\="../\_images/nestedpage-index-2.png, ../\_images/nestedpage-index-2.2x.png 2.00x" alt\="" class\="plot-directive "/>

On this page