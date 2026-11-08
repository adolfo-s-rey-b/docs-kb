[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html#sphx-glr-download-gallery-axes-grid1-parasite-simple2-py)
 to download the full example code.

Parasite Simple2[#](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html#parasite-simple2 "Link to this heading")

====================================================================================================================================

![parasite simple2](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple2_001_2_00x.png)

import matplotlib.pyplot as plt

import matplotlib.transforms as mtransforms
from mpl\_toolkits.axes\_grid1.parasite\_axes import [HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")

[obs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\["01\_S1", 3.88, 0.14, 1970, 63\],\
       \["01\_S4", 5.6, 0.82, 1622, 150\],\
       \["02\_S1", 2.4, 0.54, 1570, 40\],\
       \["03\_S1", 4.1, 0.62, 2380, 170\]\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

ax\_kms \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(axes\_class\=[HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
, aspect\=1)

\# angular proper motion("/yr) to linear velocity(km/s) at distance=2.3kpc
[pm\_to\_kms](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1./206265.\*2300\*3.085e18/3.15e7/1.e5

[aux\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([pm\_to\_kms](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 1.)
ax\_pm \= [ax\_kms.twin](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twin "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twin")
([aux\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)

for [n](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ds](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dse](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [we](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in [obs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [time](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= ((2007 + (10. + 4/30.)/12) \- 1988.5)
    [v](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [ds](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [time](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [pm\_to\_kms](https://docs.python.org/3/library/functions.html#float "builtins.float")
    [ve](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [dse](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [time](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [pm\_to\_kms](https://docs.python.org/3/library/functions.html#float "builtins.float")
    [ax\_kms.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
(\[[v](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], \[[w](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], xerr\=\[[ve](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], yerr\=\[[we](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], color\="k")

[ax\_kms.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.axis "mpl_toolkits.axes_grid1.mpl_axes.Axes.axis")
\["bottom"\].set\_label("Linear velocity at 2.3 kpc \[km/s\]")
[ax\_kms.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.axis "mpl_toolkits.axes_grid1.mpl_axes.Axes.axis")
\["left"\].set\_label("FWHM \[km/s\]")
[ax\_pm.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.axis "mpl_toolkits.axes_grid1.mpl_axes.Axes.axis")
\["top"\].set\_label(r"Proper Motion \[$''$/yr\]")
[ax\_pm.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.axis "mpl_toolkits.axes_grid1.mpl_axes.Axes.axis")
\["top"\].label.set\_visible(True)
[ax\_pm.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.axis "mpl_toolkits.axes_grid1.mpl_axes.Axes.axis")
\["right"\].major\_ticklabels.set\_visible(False)

[ax\_kms.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(950, 3700)
[ax\_kms.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(950, 3100)
\# xlim and ylim of ax\_pms will be automatically adjusted.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: parasite_simple2.ipynb`](https://matplotlib.org/stable/_downloads/266c634177141fb6b6bf2761e0e9c9b7/parasite_simple2.ipynb)

[`Download Python source code: parasite_simple2.py`](https://matplotlib.org/stable/_downloads/7cde5ea64c654f0494cddafd39449630/parasite_simple2.py)

[`Download zipped: parasite_simple2.zip`](https://matplotlib.org/stable/_downloads/35158d6bd322e45227a0fbbb043e7ae6/parasite_simple2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)