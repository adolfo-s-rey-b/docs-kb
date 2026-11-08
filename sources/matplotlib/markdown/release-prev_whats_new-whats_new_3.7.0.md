[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#main-content)

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
    

[What's new in Matplotlib 3.7.0 (Feb 13, 2023)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#what-s-new-in-matplotlib-3-7-0-feb-13-2023 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Plotting and Annotation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#plotting-and-annotation-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`hatch` parameter for pie](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#hatch-parameter-for-pie "Link to this heading")

[`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 now accepts a _hatch_ keyword that takes as input a hatch or list of hatches:

fig, (ax1, ax2) \= plt.subplots(ncols\=2)
x \= \[10, 30, 60\]

ax1.pie(x, hatch\=\['.', 'o', 'O'\])
ax2.pie(x, hatch\='.O')

ax1.set\_title("hatch=\['.', 'o', 'O'\]")
ax2.set\_title("hatch='.O'")

([`Source code`](https://matplotlib.org/stable/_downloads/d7688ea416134eb83cef2cf25889457f/whats_new_3-7-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/33a5159019e4826588d43ebae289f4a1/whats_new_3-7-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9ce5ebece38ecf570653cf406c2be034/whats_new_3-7-0-1.png)
)

[![Two pie charts, identified as ax1 and ax2, both have a small blue slice, a medium orange slice, and a large green slice. ax1 has a dot hatching on the small slice, a small open circle hatching on the medium slice, and a large open circle hatching on the large slice. ax2 has the same large open circle with a dot hatch on every slice.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-1.2x.png)

### [Polar plot errors drawn in polar coordinates](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#polar-plot-errors-drawn-in-polar-coordinates "Link to this heading")

Caps and error lines are now drawn with respect to polar coordinates, when plotting errorbars on polar plots.

[![../../_images/sphx_glr_polar_error_caps_001.png](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_001.png)](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html)

### [Additional format string options in](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id5)
 [`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#additional-format-string-options-in-bar-label "Link to this heading")

The `fmt` argument of [`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
 now accepts {}-style format strings:

import matplotlib.pyplot as plt

fruit\_names \= \['Coffee', 'Salted Caramel', 'Pistachio'\]
fruit\_counts \= \[4000, 2000, 7000\]

fig, ax \= plt.subplots()
bar\_container \= ax.bar(fruit\_names, fruit\_counts)
ax.set(ylabel\='pints sold', title\='Gelato sales by flavor', ylim\=(0, 8000))
ax.bar\_label(bar\_container, fmt\='{:,.0f}')

([`Source code`](https://matplotlib.org/stable/_downloads/9c6132f698c274150fb38b5fd8774ad3/whats_new_3-7-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/928af5d119a0514870b85b9fe0a7aa69/whats_new_3-7-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/0fa61a70b0d2aecd4fb81bde79c6ff82/whats_new_3-7-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-2.2x.png)

It also accepts callables:

animal\_names \= \['Lion', 'Gazelle', 'Cheetah'\]
mph\_speed \= \[50, 60, 75\]

fig, ax \= plt.subplots()
bar\_container \= ax.bar(animal\_names, mph\_speed)
ax.set(ylabel\='speed in MPH', title\='Running speeds', ylim\=(0, 80))
ax.bar\_label(
    bar\_container, fmt\=lambda x: '{:.1f} km/h'.format(x \* 1.61)
)

([`Source code`](https://matplotlib.org/stable/_downloads/bed82763e8cf567516da85b4a391199e/whats_new_3-7-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9b64c6755f998532b148dc143c41a679/whats_new_3-7-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2f66429cc8b5fadeb54889dac0277b97/whats_new_3-7-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-3.2x.png)

### [`ellipse` boxstyle option for annotations](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#ellipse-boxstyle-option-for-annotations "Link to this heading")

The `'ellipse'` option for boxstyle can now be used to create annotations with an elliptical outline. It can be used as a closed curve shape for longer texts instead of the `'circle'` boxstyle which can get quite big.

import matplotlib.pyplot as plt
fig, ax \= plt.subplots(figsize\=(5, 5))
t \= ax.text(0.5, 0.5, "elliptical box",
        ha\="center", size\=15,
        bbox\=dict(boxstyle\="ellipse,pad=0.3"))

([`Source code`](https://matplotlib.org/stable/_downloads/98a5d17682d486fe8026444410ff07f5/whats_new_3-7-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/7cf52eb85809032726d904475a02fc6b/whats_new_3-7-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7de78205e5b49e098ce4864e23fa141b/whats_new_3-7-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-4.2x.png)

### [The _extent_ of `imshow` can now be expressed with units](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#the-extent-of-imshow-can-now-be-expressed-with-units "Link to this heading")

The _extent_ parameter of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 and [`set_extent`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set_extent "matplotlib.image.AxesImage.set_extent")
 can now be expressed with units.

import matplotlib.pyplot as plt
import numpy as np

fig, ax \= plt.subplots(layout\='constrained')
date\_first \= np.datetime64('2020-01-01', 'D')
date\_last \= np.datetime64('2020-01-11', 'D')

arr \= \[\[i+j for i in range(10)\] for j in range(10)\]

ax.imshow(arr, origin\='lower', extent\=\[0, 10, date\_first, date\_last\])

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/2c5f0260cceabfc0d5307ed4544c95a4/whats_new_3-7-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/70800779ddcc248f799d1e0117b9d447/whats_new_3-7-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e21052727ac90d9c3e7e2b41815dd2ab/whats_new_3-7-0-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-5.2x.png)

### [Reversed order of legend entries](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#reversed-order-of-legend-entries "Link to this heading")

The order of legend entries can now be reversed by passing `reverse=True` to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
.

### [`pcolormesh` accepts RGB(A) colors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#pcolormesh-accepts-rgb-a-colors "Link to this heading")

The [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 method can now handle explicit colors specified with RGB(A) values. To specify colors, the array must be 3D with a shape of `(M, N, [3, 4])`.

import matplotlib.pyplot as plt
import numpy as np

colors \= np.linspace(0, 1, 90).reshape((5, 6, 3))
plt.pcolormesh(colors)
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/66bdb0c632afc49b6278d4eef7ebccbd/whats_new_3-7-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a6ac26e145bbb8affecf97de67cf7101/whats_new_3-7-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a71f052ef5b4bedab35a960232b8cf92/whats_new_3-7-0-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-6.2x.png)

### [View current appearance settings for ticks, tick labels, and gridlines](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#view-current-appearance-settings-for-ticks-tick-labels-and-gridlines "Link to this heading")

The new [`get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params")
 method can be used to retrieve the appearance settings that will be applied to any additional ticks, tick labels, and gridlines added to the plot:

\>>> import matplotlib.pyplot as plt

\>>> fig, ax \= plt.subplots()
\>>> ax.yaxis.set\_tick\_params(labelsize\=30, labelcolor\='red',
...                          direction\='out', which\='major')
\>>> ax.yaxis.get\_tick\_params(which\='major')
{'direction': 'out',
'left': True,
'right': False,
'labelleft': True,
'labelright': False,
'gridOn': False,
'labelsize': 30,
'labelcolor': 'red'}
\>>> ax.yaxis.get\_tick\_params(which\='minor')
{'left': True,
'right': False,
'labelleft': True,
'labelright': False,
'gridOn': False}

### [Style files can be imported from third-party packages](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#style-files-can-be-imported-from-third-party-packages "Link to this heading")

Third-party packages can now distribute style files that are globally available as follows. Assume that a package is importable as `import mypackage`, with a `mypackage/__init__.py` module. Then a `mypackage/presentation.mplstyle` style sheet can be used as `plt.style.use("mypackage.presentation")`.

The implementation does not actually import `mypackage`, making this process safe against possible import-time side effects. Subpackages (e.g. `dotted.package.name`) are also supported.

[Improvements to 3D Plotting](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#improvements-to-3d-plotting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [3D plot pan and zoom buttons](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#d-plot-pan-and-zoom-buttons "Link to this heading")

The pan and zoom buttons in the toolbar of 3D plots are now enabled. Unselect both to rotate the plot. When the zoom button is pressed, zoom in by using the left mouse button to draw a bounding box, and out by using the right mouse button to draw the box. When zooming a 3D plot, the current view aspect ratios are kept fixed.

### [_adjustable_ keyword argument for setting equal aspect ratios in 3D](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#adjustable-keyword-argument-for-setting-equal-aspect-ratios-in-3d "Link to this heading")

While setting equal aspect ratios for 3D plots, users can choose to modify either the data limits or the bounding box in parity with 2D Axes.

import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations, product

aspects \= ('auto', 'equal', 'equalxy', 'equalyz', 'equalxz')
fig, axs \= plt.subplots(1, len(aspects), subplot\_kw\={'projection': '3d'},
                        figsize\=(12, 6))

\# Draw rectangular cuboid with side lengths \[4, 3, 5\]
r \= \[0, 1\]
scale \= np.array(\[4, 3, 5\])
pts \= combinations(np.array(list(product(r, r, r))), 2)
for start, end in pts:
    if np.sum(np.abs(start \- end)) \== r\[1\] \- r\[0\]:
        for ax in axs:
            ax.plot3D(\*zip(start\*scale, end\*scale), color\='C0')

\# Set the aspect ratios
for i, ax in enumerate(axs):
    ax.set\_aspect(aspects\[i\], adjustable\='datalim')
    \# Alternatively: ax.set\_aspect(aspects\[i\], adjustable='box')
    \# which will change the box aspect ratio instead of axis data limits.
    ax.set\_title(f"set\_aspect('{aspects\[i\]}')")

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/610c7d0ef71e1912ebe9b9bcf078dca5/whats_new_3-7-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1a76b866482852808a5f544abbbe4989/whats_new_3-7-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ba95419ea11bf609c9b70b3d19b051f0/whats_new_3-7-0-7.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-7.2x.png)

### [`Poly3DCollection` supports shading](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#poly3dcollection-supports-shading "Link to this heading")

It is now possible to shade a [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
. This is useful if the polygons are obtained from e.g. a 3D model.

import numpy as np
import matplotlib.pyplot as plt
from mpl\_toolkits.mplot3d.art3d import Poly3DCollection

\# Define 3D shape
block \= np.array(\[\
    \[\[1, 1, 0\],\
     \[1, 0, 0\],\
     \[0, 1, 0\]\],\
    \[\[1, 1, 0\],\
     \[1, 1, 1\],\
     \[1, 0, 0\]\],\
    \[\[1, 1, 0\],\
     \[1, 1, 1\],\
     \[0, 1, 0\]\],\
    \[\[1, 0, 0\],\
     \[1, 1, 1\],\
     \[0, 1, 0\]\]\
\])

ax \= plt.subplot(projection\='3d')
pc \= Poly3DCollection(block, facecolors\='b', shade\=True)
ax.add\_collection(pc)
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/2420cb78e95e754c66cf8c0d6ccbf289/whats_new_3-7-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f426cdc5344469ef7510e3a76944e926/whats_new_3-7-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a3fdc2114b0f5f1bd4e151a3e3eb7dd5/whats_new_3-7-0-8.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-8.2x.png)

### [rcParam for 3D pane color](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#rcparam-for-3d-pane-color "Link to this heading")

The rcParams `[rcParams["axes3d.xaxis.panecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.xaxis.panecolor#rcparam-axes3d-xaxis-panecolor) ` (default: `(0.95, 0.95, 0.95, 0.5)`), `[rcParams["axes3d.yaxis.panecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.yaxis.panecolor#rcparam-axes3d-yaxis-panecolor) ` (default: `(0.9, 0.9, 0.9, 0.5)`), `[rcParams["axes3d.zaxis.panecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.zaxis.panecolor#rcparam-axes3d-zaxis-panecolor) ` (default: `(0.925, 0.925, 0.925, 0.5)`) can be used to change the color of the background panes in 3D plots. Note that it is often beneficial to give them slightly different shades to obtain a "3D effect" and to make them slightly transparent (alpha < 1).

import matplotlib.pyplot as plt
with plt.rc\_context({'axes3d.xaxis.panecolor': (0.9, 0.0, 0.0, 0.5),
                     'axes3d.yaxis.panecolor': (0.7, 0.0, 0.0, 0.5),
                     'axes3d.zaxis.panecolor': (0.8, 0.0, 0.0, 0.5)}):
    fig \= plt.figure()
    fig.add\_subplot(projection\='3d')

([`Source code`](https://matplotlib.org/stable/_downloads/b7769f8adb7fed234982bd35b73ad93f/whats_new_3-7-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b5035e767d3c97174d27a9cc630b685c/whats_new_3-7-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b8e971488aec15028a9f23018bd4ed98/whats_new_3-7-0-9.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-9.2x.png)

[Figure and Axes Layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#figure-and-axes-layout "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`colorbar` now has a _location_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#colorbar-now-has-a-location-keyword-argument "Link to this heading")

The `colorbar` method now supports a _location_ keyword argument to more easily position the color bar. This is useful when providing your own inset axes using the _cax_ keyword argument and behaves similar to the case where axes are not provided (where the _location_ keyword is passed through). _orientation_ and _ticklocation_ are no longer required as they are determined by _location_. _ticklocation_ can still be provided if the automatic setting is not preferred. (_orientation_ can also be provided but must be compatible with the _location_.)

An example is:

import matplotlib.pyplot as plt
import numpy as np
rng \= np.random.default\_rng(19680801)
imdata \= rng.random((10, 10))
fig, ax \= plt.subplots(layout\='constrained')
im \= ax.imshow(imdata)
fig.colorbar(im, cax\=ax.inset\_axes(\[0, 1.05, 1, 0.05\]),
             location\='top')

([`Source code`](https://matplotlib.org/stable/_downloads/880bc41213432adc4cee938be3f9182f/whats_new_3-7-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/acdaae5cf600a37d8a7b6ca155dd6d47/whats_new_3-7-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b24ee575b5e0ca9975a50191a63005a8/whats_new_3-7-0-10.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-10.2x.png)

### [Figure legends can be placed outside figures using constrained\_layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#figure-legends-can-be-placed-outside-figures-using-constrained-layout "Link to this heading")

Constrained layout will make space for Figure legends if they are specified by a _loc_ keyword argument that starts with the string "outside". The codes are unique from axes codes, in that "outside upper right" will make room at the top of the figure for the legend, whereas "outside right upper" will make room on the right-hand side of the figure. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for details.

### [Per-subplot keyword arguments in `subplot_mosaic`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#per-subplot-keyword-arguments-in-subplot-mosaic "Link to this heading")

It is now possible to pass keyword arguments through to Axes creation in each specific call to `add_subplot` in [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 :

fig, axd \= plt.subplot\_mosaic(
    "AB;CD",
    per\_subplot\_kw\={
        "A": {"projection": "polar"},
        ("C", "D"): {"xscale": "log"},
        "B": {"projection": "3d"},
    },
)

([`Source code`](https://matplotlib.org/stable/_downloads/144fcc245c0b050882d0f5c2274dd504/whats_new_3-7-0-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a5380b9a52217e1b1089bb00a8e219ad/whats_new_3-7-0-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/186faea3c1eb7eae0608d23cb7e50336/whats_new_3-7-0-11.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-11.2x.png)

This is particularly useful for creating mosaics with mixed projections, but any keyword arguments can be passed through.

### [`subplot_mosaic` no longer provisional](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#subplot-mosaic-no-longer-provisional "Link to this heading")

The API on [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 are now considered stable and will change under Matplotlib's normal deprecation process.

[Widget Improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#widget-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Custom styling of button widgets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#custom-styling-of-button-widgets "Link to this heading")

Additional custom styling of button widgets may be achieved via the _label\_props_ and _radio\_props_ arguments to [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
; and the _label\_props_, _frame\_props_, and _check\_props_ arguments to [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
.

from matplotlib.widgets import CheckButtons, RadioButtons

fig, ax \= plt.subplots(nrows\=2, ncols\=2, figsize\=(5, 2), width\_ratios\=\[1, 2\])
default\_rb \= RadioButtons(ax\[0, 0\], \['Apples', 'Oranges'\])
styled\_rb \= RadioButtons(ax\[0, 1\], \['Apples', 'Oranges'\],
                         label\_props\={'color': \['red', 'orange'\],
                                      'fontsize': \[16, 20\]},
                         radio\_props\={'edgecolor': \['red', 'orange'\],
                                      'facecolor': \['mistyrose', 'peachpuff'\]})

default\_cb \= CheckButtons(ax\[1, 0\], \['Apples', 'Oranges'\],
                          actives\=\[True, True\])
styled\_cb \= CheckButtons(ax\[1, 1\], \['Apples', 'Oranges'\],
                         actives\=\[True, True\],
                         label\_props\={'color': \['red', 'orange'\],
                                      'fontsize': \[16, 20\]},
                         frame\_props\={'edgecolor': \['red', 'orange'\],
                                      'facecolor': \['mistyrose', 'peachpuff'\]},
                         check\_props\={'color': \['darkred', 'darkorange'\]})

ax\[0, 0\].set\_title('Default')
ax\[0, 1\].set\_title('Stylized')

([`Source code`](https://matplotlib.org/stable/_downloads/31ad00db9a012c2c15ac0a1f9447655f/whats_new_3-7-0-12.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/71e71ca44988e12216b76a67d251ee26/whats_new_3-7-0-12.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f92fa1305ff4b0ac0dee2ecd30b16d2b/whats_new_3-7-0-12.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-7-0-12.2x.png)

### [Blitting in Button widgets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#blitting-in-button-widgets "Link to this heading")

The [`Button`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
, [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
, and [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 widgets now support blitting for faster rendering, on backends that support it, by passing `useblit=True` to the constructor. Blitting is enabled by default on supported backends.

[Other Improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#other-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Source links can be shown or hidden for each Sphinx plot directive](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#source-links-can-be-shown-or-hidden-for-each-sphinx-plot-directive "Link to this heading")

The [Sphinx plot directive](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html)
 (`.. plot::`) now supports a `:show-source-link:` option to show or hide the link to the source code for each plot. The default is set using the `plot_html_show_source_link` variable in `conf.py` (which defaults to True).

### [Figure hooks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#figure-hooks "Link to this heading")

The new `[rcParams["figure.hooks"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.hooks#rcparam-figure-hooks) ` (default: `[]`) provides a mechanism to register arbitrary customizations on pyplot figures; it is a list of "dotted.module.name:dotted.callable.name" strings specifying functions that are called on each figure created by [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
; these functions can e.g. attach callbacks or modify the toolbar. See [mplcvd -- an example of figure hook](https://matplotlib.org/stable/gallery/user_interfaces/mplcvd.html)
 for an example of toolbar customization.

[New & Improved Narrative Documentation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.7.0.html#new-improved-narrative-documentation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Brand new [Animations](https://matplotlib.org/stable/users/explain/animations/animations.html#animations)
     tutorial.
    
*   New grouped and stacked [bar chart](https://matplotlib.org/stable/gallery/index.html#lines_bars_and_markers)
     examples.
    
*   New section for new contributors and reorganized git instructions in the [contributing guide](https://matplotlib.org/stable/devel/contribute.html#contributing)
    .
    
*   Restructured [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
     tutorial.
    

On this page