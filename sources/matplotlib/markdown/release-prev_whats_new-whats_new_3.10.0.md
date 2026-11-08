[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#main-content)

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
    

[What's new in Matplotlib 3.10.0 (December 13, 2024)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#what-s-new-in-matplotlib-3-10-0-december-13-2024 "Link to this heading")

==============================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.10.0 (Dec 14, 2024)](https://matplotlib.org/stable/release/prev_whats_new/github_stats_3.10.0.html#github-stats-3-10-0)
.

[Accessible Colors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#accessible-colors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [New more-accessible color cycle](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#new-more-accessible-color-cycle "Link to this heading")

A new color cycle named 'petroff10' was added. This cycle was constructed using a combination of algorithmically-enforced accessibility constraints, including color-vision-deficiency modeling, and a machine-learning-based aesthetics model developed from a crowdsourced color-preference survey. It aims to be both generally pleasing aesthetically and colorblind accessible such that it could serve as a default in the aim of universal design. For more details see [Petroff, M. A.: "Accessible Color Sequences for Data Visualization"](https://arxiv.org/abs/2107.02270)
 and related [SciPy talk](https://www.youtube.com/watch?v=Gapv8wR5DYU)
. A demonstration is included in the style sheets [reference](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html)
. To load this color cycle in place of the default:

import matplotlib.pyplot as plt
plt.style.use('petroff10')

### [Dark-mode diverging colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#dark-mode-diverging-colormaps "Link to this heading")

Three diverging colormaps have been added: "berlin", "managua", and "vanimo". They are dark-mode diverging colormaps, with minimum lightness at the center, and maximum at the extremes. These are taken from F. Crameri's Scientific colour maps version 8.0.1 (DOI: [https://doi.org/10.5281/zenodo.1243862](https://doi.org/10.5281/zenodo.1243862)
).

import numpy as np
import matplotlib.pyplot as plt

vals \= np.linspace(\-5, 5, 100)
x, y \= np.meshgrid(vals, vals)
img \= np.sin(x\*y)

\_, ax \= plt.subplots(1, 3)
ax\[0\].imshow(img, cmap\="berlin")
ax\[1\].imshow(img, cmap\="managua")
ax\[2\].imshow(img, cmap\="vanimo")

([`Source code`](https://matplotlib.org/stable/_downloads/7b15318b8b2efbf3dbd5de716b6c7c3b/whats_new_3-10-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/029e60bb87615f8840693d496c8b2504/whats_new_3-10-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5f7c7811293558897d0551d07258d6e1/whats_new_3-10-0-1.png)
)

[![Example figures using "imshow" with dark-mode diverging colormaps on positive and negative data. First panel: "berlin" (blue to red with a black center); second panel: "managua" (orange to cyan with a dark purple center); third panel: "vanimo" (pink to green with a black center).](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-1.2x.png)

[Plotting and Annotation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#plotting-and-annotation-improvements "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Specifying a single color in `contour` and `contourf`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#specifying-a-single-color-in-contour-and-contourf "Link to this heading")

[`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 previously accepted a single color provided it was expressed as a string. This restriction has now been removed and a single color in any format described in the [Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 tutorial may be passed.

import matplotlib.pyplot as plt

fig, (ax1, ax2) \= plt.subplots(ncols\=2, figsize\=(6, 3))
z \= \[\[0, 1\], \[1, 2\]\]

ax1.contour(z, colors\=('r', 0.4))
ax2.contour(z, colors\=(0.1, 0.2, 0.5))

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/13abed3dfe8afafab4035f930216fefe/whats_new_3-10-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/44ade32bb6d1cdbaf295f318762b05ba/whats_new_3-10-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/14d9122bc61fa57c467ae2f8e69bf468/whats_new_3-10-0-2.png)
)

[![Two-panel example contour plots.  The left panel has all transparent red contours.  The right panel has all dark blue contours.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-2.2x.png)

### [Vectorized `hist` style parameters](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#vectorized-hist-style-parameters "Link to this heading")

The parameters _hatch_, _edgecolor_, _facecolor_, _linewidth_ and _linestyle_ of the [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 method are now vectorized. This means that you can pass in individual parameters for each histogram when the input _x_ has multiple datasets.

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(19680801)

fig, ((ax1, ax2), (ax3, ax4)) \= plt.subplots(2, 2, figsize\=(9, 9))

data1 \= np.random.poisson(5, 1000)
data2 \= np.random.poisson(7, 1000)
data3 \= np.random.poisson(10, 1000)

labels \= \["Data 1", "Data 2", "Data 3"\]

ax1.hist(\[data1, data2, data3\], bins\=range(17), histtype\="step", stacked\=True,
         edgecolor\=\["red", "green", "blue"\], linewidth\=\[1, 2, 3\])
ax1.set\_title("Different linewidths")
ax1.legend(labels)

ax2.hist(\[data1, data2, data3\], bins\=range(17), histtype\="barstacked",
         hatch\=\["/", ".", "\*"\])
ax2.set\_title("Different hatch patterns")
ax2.legend(labels)

ax3.hist(\[data1, data2, data3\], bins\=range(17), histtype\="bar", fill\=False,
         edgecolor\=\["red", "green", "blue"\], linestyle\=\["--", "-.", ":"\])
ax3.set\_title("Different linestyles")
ax3.legend(labels)

ax4.hist(\[data1, data2, data3\], bins\=range(17), histtype\="barstacked",
         facecolor\=\["red", "green", "blue"\])
ax4.set\_title("Different facecolors")
ax4.legend(labels)

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/2ac4c662443f4d70bcb8b15093b64266/whats_new_3-10-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/75e0d13e41ac446850d7c0628a479107/whats_new_3-10-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/70282fa0ab9729378312fde29e5590e8/whats_new_3-10-0-3.png)
)

[![Four charts, each displaying stacked histograms of three Poisson distributions. Each chart differentiates the histograms using various parameters: top left uses different linewidths, top right uses different hatches, bottom left uses different edgecolors, and bottom right uses different facecolors. Each histogram on the left side also has a different edgecolor.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-3.2x.png)

### [`InsetIndicator` artist](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#insetindicator-artist "Link to this heading")

[`indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")
 and [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
 now return an instance of [`InsetIndicator`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator "matplotlib.inset.InsetIndicator")
 which contains the rectangle and connector patches. These patches now update automatically so that

ax.indicate\_inset\_zoom(ax\_inset)
ax\_inset.set\_xlim(new\_lim)

now gives the same result as

ax\_inset.set\_xlim(new\_lim)
ax.indicate\_inset\_zoom(ax\_inset)

### [`matplotlib.ticker.EngFormatter` can computes offsets now](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#matplotlib-ticker-engformatter-can-computes-offsets-now "Link to this heading")

[`matplotlib.ticker.EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 has gained the ability to show an offset text near the axis. Using logic shared with [`matplotlib.ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
, it is capable of deciding whether the data qualifies having an offset and show it with an appropriate SI quantity prefix, and with the supplied `unit`.

To enable this new behavior, simply pass `useOffset=True` when you instantiate [`matplotlib.ticker.EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
. See example [SI prefixed offsets and natural order of magnitudes](https://matplotlib.org/stable/gallery/ticks/engformatter_offset.html)
.

([`Source code`](https://matplotlib.org/stable/_downloads/9c8aafb41010700c1034f328f50fb3d6/engformatter_offset.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1326c624446384312705f44a03a85467/engformatter_offset.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/bf8538a1148949f5083b6931523e3e39/engformatter_offset.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-engformatter_offset.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-engformatter_offset.2x.png)

### [Fix padding of single colorbar for `ImageGrid`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#fix-padding-of-single-colorbar-for-imagegrid "Link to this heading")

`ImageGrid` with `cbar_mode="single"` no longer adds the `axes_pad` between the axes and the colorbar for `cbar_location` "left" and "bottom". If desired, add additional spacing using `cbar_pad`.

### [`ax.table` will accept a pandas DataFrame](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#ax-table-will-accept-a-pandas-dataframe "Link to this heading")

The [`table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.table.html#matplotlib.axes.Axes.table "matplotlib.axes.Axes.table")
 method can now accept a Pandas DataFrame for the `cellText` argument.

import matplotlib.pyplot as plt
import pandas as pd

data \= {
    'Letter': \['A', 'B', 'C'\],
    'Number': \[100, 200, 300\]
}

df \= pd.DataFrame(data)
fig, ax \= plt.subplots()
table \= ax.table(df, loc\='center')  \# or table = ax.table(cellText=df, loc='center')
ax.axis('off')
plt.show()

### [Subfigures are now added in row-major order](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#subfigures-are-now-added-in-row-major-order "Link to this heading")

`Figure.subfigures` are now added in row-major order for API consistency.

import matplotlib.pyplot as plt

fig \= plt.figure()
subfigs \= fig.subfigures(3, 3)
x \= np.linspace(0, 10, 100)

for i, sf in enumerate(fig.subfigs):
    ax \= sf.subplots()
    ax.plot(x, np.sin(x + i), label\=f'Subfigure {i+1}')
    sf.suptitle(f'Subfigure {i+1}')
    ax.set\_xticks(\[\])
    ax.set\_yticks(\[\])
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/be0cfab2313e59ae59627310dfe9ab11/whats_new_3-10-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/585473a15b3e836e55501c6fb1866c89/whats_new_3-10-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/09ef58c69b1b513c3cd0d2af3c428073/whats_new_3-10-0-4.png)
)

[![Example of creating 3 by 3 subfigures.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-4.2x.png)

### [`boxplot` and `bxp` orientation parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#boxplot-and-bxp-orientation-parameter "Link to this heading")

Boxplots have a new parameter _orientation: {"vertical", "horizontal"}_ to change the orientation of the plot. This replaces the deprecated _vert: bool_ parameter.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots()
np.random.seed(19680801)
all\_data \= \[np.random.normal(0, std, 100) for std in range(6, 10)\]

ax.boxplot(all\_data, orientation\='horizontal')
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/6cc3b84bd1dc9fcd225111127e9dad5c/whats_new_3-10-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/cca33ada99d0584ea8e7b27d2b5bb7bc/whats_new_3-10-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/57b30335248a6e5170375334391b91a0/whats_new_3-10-0-5.png)
)

[![Example of creating 4 horizontal boxplots.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-5.2x.png)

### [`violinplot` and `violin` orientation parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#violinplot-and-violin-orientation-parameter "Link to this heading")

Violinplots have a new parameter _orientation: {"vertical", "horizontal"}_ to change the orientation of the plot. This will replace the deprecated _vert: bool_ parameter.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots()
np.random.seed(19680801)
all\_data \= \[np.random.normal(0, std, 100) for std in range(6, 10)\]

ax.violinplot(all\_data, orientation\='horizontal')
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/9667b2ec25a6a933056aa8abcb35289f/whats_new_3-10-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c1a7d2b307855b409856a3da703d73ce/whats_new_3-10-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/aaf06287e4dd2707b4c8462fd1941c72/whats_new_3-10-0-6.png)
)

[![Example of creating 4 horizontal violinplots.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-6.2x.png)

### [`FillBetweenPolyCollection`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#fillbetweenpolycollection "Link to this heading")

The new class [`matplotlib.collections.FillBetweenPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection "matplotlib.collections.FillBetweenPolyCollection")
 provides the `set_data` method, enabling e.g. resampling (`galleries/event_handling/resample.html`). [`matplotlib.axes.Axes.fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 and [`matplotlib.axes.Axes.fill_betweenx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
 now return this new class.

import numpy as np
from matplotlib import pyplot as plt

t \= np.linspace(0, 1)

fig, ax \= plt.subplots()
coll \= ax.fill\_between(t, \-t\*\*2, t\*\*2)
fig.savefig("before.png")

coll.set\_data(t, \-t\*\*4, t\*\*4)
fig.savefig("after.png")

### [`matplotlib.colorizer.Colorizer` as container for `norm` and `cmap`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#matplotlib-colorizer-colorizer-as-container-for-norm-and-cmap "Link to this heading")

> [`matplotlib.colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
>  encapsulates the data-to-color pipeline. It makes reuse of colormapping easier, e.g. across multiple images. Plotting methods that support _norm_ and _cmap_ keyword arguments now also accept a _colorizer_ keyword argument.

In the following example the norm and cmap are changed on multiple plots simultaneously:

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x \= np.linspace(\-2, 2, 50)\[np.newaxis, :\]
y \= np.linspace(\-2, 2, 50)\[:, np.newaxis\]
im\_0 \= 1 \* np.exp( \- (x\*\*2 + y\*\*2 \- x \* y))
im\_1 \= 2 \* np.exp( \- (x\*\*2 + y\*\*2 + x \* y))

colorizer \= mpl.colorizer.Colorizer()
fig, axes \= plt.subplots(1, 2, figsize\=(6, 2))
cim\_0 \= axes\[0\].imshow(im\_0, colorizer\=colorizer)
fig.colorbar(cim\_0)
cim\_1 \= axes\[1\].imshow(im\_1, colorizer\=colorizer)
fig.colorbar(cim\_1)

colorizer.vmin \= 0.5
colorizer.vmax \= 2
colorizer.cmap \= 'RdBu'

([`Source code`](https://matplotlib.org/stable/_downloads/316a18481b56bee31824634c5ce3e451/whats_new_3-10-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/09b2078b2fbe26dd3e51219b4ad917a8/whats_new_3-10-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b5afc621af7df415892cc0dd430a81f6/whats_new_3-10-0-7.png)
)

[![Example use of a matplotlib.colorizer.Colorizer object](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-7.2x.png)

All plotting methods that use a data-to-color pipeline now create a colorizer object if one is not provided. This can be reused by subsequent artists such that they will share a single data-to-color pipeline:

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x \= np.linspace(\-2, 2, 50)\[np.newaxis, :\]
y \= np.linspace(\-2, 2, 50)\[:, np.newaxis\]
im\_0 \= 1 \* np.exp( \- (x\*\*2 + y\*\*2 \- x \* y))
im\_1 \= 2 \* np.exp( \- (x\*\*2 + y\*\*2 + x \* y))

fig, axes \= plt.subplots(1, 2, figsize\=(6, 2))

cim\_0 \= axes\[0\].imshow(im\_0, cmap\='RdBu', vmin\=0.5, vmax\=2)
fig.colorbar(cim\_0)
cim\_1 \= axes\[1\].imshow(im\_1, colorizer\=cim\_0.colorizer)
fig.colorbar(cim\_1)

cim\_1.cmap \= 'rainbow'

([`Source code`](https://matplotlib.org/stable/_downloads/ffaae24151eebd98e11fa47ee9a8b79d/whats_new_3-10-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b0f12cda067b6ece723f74067bf4c32e/whats_new_3-10-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/fb1feafbc4d6622e34a8147633c45020/whats_new_3-10-0-8.png)
)

[![Example of how artists that share a ``colorizer`` have coupled colormaps](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-8.2x.png)

[3D plotting improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#d-plotting-improvements "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Fill between 3D lines](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#fill-between-3d-lines "Link to this heading")

The new method [`Axes3D.fill_between`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between "mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between")
 allows to fill the surface between two 3D lines with polygons.

N \= 50
theta \= np.linspace(0, 2\*np.pi, N)

x1 \= np.cos(theta)
y1 \= np.sin(theta)
z1 \= 0.1 \* np.sin(6 \* theta)

x2 \= 0.6 \* np.cos(theta)
y2 \= 0.6 \* np.sin(theta)
z2 \= 2  \# Note that scalar values work in addition to length N arrays

fig \= plt.figure()
ax \= fig.add\_subplot(projection\='3d')
ax.fill\_between(x1, y1, z1, x2, y2, z2,
                alpha\=0.5, edgecolor\='k')

([`Source code`](https://matplotlib.org/stable/_downloads/3abe777e7d9806ceaeb2138495e25b49/whats_new_3-10-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/cc774722074c9ff8f96912eeb1b99119/whats_new_3-10-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f35be520aea5a04d8581bc379ed9b1c5/whats_new_3-10-0-9.png)
)

[![Example of 3D fill_between](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-9.2x.png)

### [Rotating 3d plots with the mouse](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#rotating-3d-plots-with-the-mouse "Link to this heading")

Rotating three-dimensional plots with the mouse has been made more intuitive. The plot now reacts the same way to mouse movement, independent of the particular orientation at hand; and it is possible to control all 3 rotational degrees of freedom (azimuth, elevation, and roll). By default, it uses a variation on Ken Shoemake's ARCBALL [\[1\]](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id2)
. The particular style of mouse rotation can be set via `[rcParams["axes3d.mouserotationstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.mouserotationstyle#rcparam-axes3d-mouserotationstyle) ` (default: `'arcball'`). See also [Rotation with mouse](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#toolkit-mouse-rotation)
.

To revert to the original mouse rotation style, create a file `matplotlibrc` with contents:

axes3d.mouserotationstyle: azel

To try out one of the various mouse rotation styles:

import matplotlib as mpl
mpl.rcParams\['axes3d.mouserotationstyle'\] \= 'trackball'  \# 'azel', 'trackball', 'sphere', or 'arcball'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

ax \= plt.figure().add\_subplot(projection\='3d')

X \= np.arange(\-5, 5, 0.25)
Y \= np.arange(\-5, 5, 0.25)
X, Y \= np.meshgrid(X, Y)
R \= np.sqrt(X\*\*2 + Y\*\*2)
Z \= np.sin(R)

surf \= ax.plot\_surface(X, Y, Z, cmap\=cm.coolwarm,
                       linewidth\=0, antialiased\=False)

plt.show()

### [Data in 3D plots can now be dynamically clipped to the axes view limits](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#data-in-3d-plots-can-now-be-dynamically-clipped-to-the-axes-view-limits "Link to this heading")

All 3D plotting functions now support the _axlim\_clip_ keyword argument, which will clip the data to the axes view limits, hiding all data outside those bounds. This clipping will be dynamically applied in real time while panning and zooming.

Please note that if one vertex of a line segment or 3D patch is clipped, then the entire segment or patch will be hidden. Not being able to show partial lines or patches such that they are "smoothly" cut off at the boundaries of the view box is a limitation of the current renderer.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots(subplot\_kw\={"projection": "3d"})
x \= np.arange(\-5, 5, 0.5)
y \= np.arange(\-5, 5, 0.5)
X, Y \= np.meshgrid(x, y)
R \= np.sqrt(X\*\*2 + Y\*\*2)
Z \= np.sin(R)

\# Note that when a line has one vertex outside the view limits, the entire
\# line is hidden. The same is true for 3D patches (not shown).
\# In this example, data where x < 0 or z > 0.5 is clipped.
ax.plot\_wireframe(X, Y, Z, color\='C0')
ax.plot\_wireframe(X, Y, Z, color\='C1', axlim\_clip\=True)
ax.set(xlim\=(0, 10), ylim\=(\-5, 5), zlim\=(\-1, 0.5))
ax.legend(\['axlim\_clip=False (default)', 'axlim\_clip=True'\])

([`Source code`](https://matplotlib.org/stable/_downloads/d6d68f3be367971b519a550ef8afa5a1/whats_new_3-10-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/84a2bccf691e2fcd80c544ef8d85ddd3/whats_new_3-10-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f145df8cd62a5f8a32ec51abc770ab01/whats_new_3-10-0-10.png)
)

[![Example of default behavior (blue) and axlim_clip=True (orange)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-10-0-10.2x.png)

[Preliminary support for free-threaded CPython 3.13](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#preliminary-support-for-free-threaded-cpython-3-13 "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib 3.10 has preliminary support for the free-threaded build of CPython 3.13. See [https://py-free-threading.github.io](https://py-free-threading.github.io/)
, [PEP 703](https://peps.python.org/pep-0703/)
 and the [CPython 3.13 release notes](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython)
 for more detail about free-threaded Python.

Support for free-threaded Python does not mean that Matplotlib is wholly thread safe. We expect that use of a Figure within a single thread will work, and though input data is usually copied, modification of data objects used for a plot from another thread may cause inconsistencies in cases where it is not. Use of any global state (such as the `pyplot` module) is highly discouraged and unlikely to work consistently. Also note that most GUI toolkits expect to run on the main thread, so interactive usage may be limited or unsupported from other threads.

If you are interested in free-threaded Python, for example because you have a multiprocessing-based workflow that you are interested in running with Python threads, we encourage testing and experimentation. If you run into problems that you suspect are because of Matplotlib, please open an issue, checking first if the bug also occurs in the “regular” non-free-threaded CPython 3.13 build.

[Other Improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#other-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`svg.id` rcParam](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#svg-id-rcparam "Link to this heading")

`[rcParams["svg.id"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=svg.id#rcparam-svg-id) ` (default: `None`) lets you insert an `id` attribute into the top-level `<svg>` tag.

e.g. `rcParams["svg.id"] = "svg1"` results in

<svg
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="50pt" height="50pt"
    viewBox="0 0 50 50"
    xmlns="http://www.w3.org/2000/svg"
    version="1.1"
    id="svg1"
\></svg>

This is useful if you would like to link the entire matplotlib SVG file within another SVG file with the `<use>` tag.

<svg>
<use
    width="50" height="50"
    xlink:href="mpl.svg#svg1" id="use1"
    x="0" y="0"
/></svg>

Where the `#svg1` indicator will now refer to the top level `<svg>` tag, and will hence result in the inclusion of the entire file.

By default, no `id` tag is included.

### [Exception handling control](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#exception-handling-control "Link to this heading")

The exception raised when an invalid keyword parameter is passed now includes that parameter name as the exception's `name` property. This provides more control for exception handling:

import matplotlib.pyplot as plt

def wobbly\_plot(args, \*\*kwargs):
    w \= kwargs.pop('wobble\_factor', None)

    try:
        plt.plot(args, \*\*kwargs)
    except AttributeError as e:
        raise AttributeError(f'wobbly\_plot does not take parameter {e.name}') from e

wobbly\_plot(\[0, 1\], wibble\_factor\=5)

AttributeError: wobbly\_plot does not take parameter wibble\_factor

### [Increased Figure limits with Agg renderer](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#increased-figure-limits-with-agg-renderer "Link to this heading")

Figures using the Agg renderer are now limited to 2\*\*23 pixels in each direction, instead of 2\*\*16. Additionally, bugs that caused artists to not render past 2\*\*15 pixels horizontally have been fixed.

Note that if you are using a GUI backend, it may have its own smaller limits (which may themselves depend on screen size.)

### [Miscellaneous Changes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#miscellaneous-changes "Link to this heading")

*   The [`matplotlib.ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
     class has gained a new instantiating parameter `usetex`.
    
*   Creating an Axes is now 20-25% faster due to internal optimizations.
    
*   The API on [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
     and [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
     are now considered stable.
    

On this page