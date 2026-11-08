[Skip to main content](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html#sphx-glr-download-gallery-misc-patheffect-demo-py)
 to download the full example code.

Patheffect Demo[#](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html#patheffect-demo "Link to this heading")

===========================================================================================================================

![patheffect demo](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(8, 3))
[ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[1, 2\], \[2, 3\]\])
[txt](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
("test", (1., 1.), (0., 0),
                   arrowprops\=dict(arrowstyle\="->",
                                   connectionstyle\="angle3", lw\=2),
                   size\=20, ha\="center",
                   path\_effects\=\[[patheffects.withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=3,\
                                                        foreground\="w")\])
[txt.arrow\_patch.set\_path\_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
(\[\
    [patheffects.Stroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")\
(linewidth\=5, foreground\="w"),\
    [patheffects.Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")\
()\])

[pe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[patheffects.withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=3,\
                             foreground\="w")\]
[ax1.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True, linestyle\="-", path\_effects\=[pe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(25).reshape((5, 5))
[ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[cntr](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax2.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, colors\="k")

[cntr.set](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet.set "matplotlib.contour.QuadContourSet.set")
(path\_effects\=\[[patheffects.withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=3, foreground\="w")\])

[clbls](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "matplotlib.cbook.silent_list")
 \= [ax2.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
([cntr](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, fmt\="%2.0f", use\_clabeltext\=True)
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([clbls](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "matplotlib.cbook.silent_list")
, path\_effects\=\[\
    [patheffects.withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=3, foreground\="w")\])

\# shadow as a path effect
[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax3.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1\], \[0, 1\])
[leg](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax3.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\], \["Line 1"\], fancybox\=True, loc\='upper left')
[leg.legendPatch.set\_path\_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
(\[[patheffects.withSimplePatchShadow](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withSimplePatchShadow "matplotlib.patheffects.withSimplePatchShadow")\
()\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: patheffect_demo.ipynb`](https://matplotlib.org/stable/_downloads/b520ac20c5a4ad1dba010866a0aaa89b/patheffect_demo.ipynb)

[`Download Python source code: patheffect_demo.py`](https://matplotlib.org/stable/_downloads/1403c9176f441d71ec67e54e239b695e/patheffect_demo.py)

[`Download zipped: patheffect_demo.zip`](https://matplotlib.org/stable/_downloads/e5d1ea037052d83d998ca8fcfc78c7f0/patheffect_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)