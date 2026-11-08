[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#sphx-glr-download-gallery-lines-bars-and-markers-marker-reference-py)
 to download the full example code.

Marker reference[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#marker-reference "Link to this heading")

================================================================================================================================================

Matplotlib supports multiple categories of markers which are selected using the `marker` parameter of plot commands:

*   [Unfilled markers](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#unfilled-markers)
    
*   [Filled markers](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#filled-markers)
    
*   [Markers created from TeX symbols](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-tex-symbols)
    
*   [Markers created from Paths](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-paths)
    

For a list of all markers see also the [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
 documentation.

For example usages see [Marker examples](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html)
.

import matplotlib.pyplot as plt

from matplotlib.lines import Line2D
from matplotlib.markers import [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(horizontalalignment\='right', verticalalignment\='center',
                  fontsize\=12, fontfamily\='monospace')
[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(linestyle\=':', color\='0.8', markersize\=10,
                    markerfacecolor\="tab:blue", markeredgecolor\="tab:blue")

def format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    [ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.2)
    [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
    [ax.invert\_yaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
()

def split\_list(a\_list):
    i\_half \= len(a\_list) // 2
    return a\_list\[:i\_half\], a\_list\[i\_half:\]

Unfilled markers[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#unfilled-markers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Unfilled markers are single-colored.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Un-filled markers', fontsize\=14)

\# Filter out filled markers and marker settings that do nothing.
[unfilled\_markers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")\
 for [m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")\
, func in Line2D.[markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")\
.items()\
                    if func != 'nothing' and [m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")\
 not in [Line2D.filled\_markers](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\]

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, split\_list([unfilled\_markers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)):
    for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 in enumerate([markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
):
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, repr([marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
), \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
        [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \* 3, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, \*\*[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Un-filled markers](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_001_2_00x.png)

Filled markers[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#filled-markers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Filled markers', fontsize\=14)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, split\_list([Line2D.filled\_markers](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)):
    for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 in enumerate([markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
):
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, repr([marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
), \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
        [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \* 3, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, \*\*[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Filled markers](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_002_2_00x.png)

### Marker fill styles[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#marker-fill-styles "Link to this heading")

The edge color and fill color of filled markers can be specified separately. Additionally, the `fillstyle` can be configured to be unfilled, fully filled, or half-filled in various directions. The half-filled styles use `markerfacecoloralt` as secondary fill color.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Marker fillstyle', fontsize\=14)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.4)

[filled\_marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict([marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\='o', linestyle\=':', markersize\=15,
                           color\='darkgrey',
                           markerfacecolor\='tab:blue',
                           markerfacecoloralt\='lightsteelblue',
                           markeredgecolor\='brown')

for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [fill\_style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([Line2D.fillStyles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, repr([fill\_style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
), \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \* 3, fillstyle\=[fill\_style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[filled\_marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Marker fillstyle](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_003_2_00x.png)

Markers created from TeX symbols[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-tex-symbols "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use [MathText](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
, to use custom marker symbols, like e.g. `"$\u266B$"`. For an overview over the STIX font symbols refer to the [STIX font table](http://www.stixfonts.org/allGlyphs.html)
. Also see the [STIX Fonts](https://matplotlib.org/stable/gallery/text_labels_and_annotations/stix_fonts_demo.html)
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Mathtext markers', fontsize\=14)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.4)

[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.update(markeredgecolor\="none", markersize\=15)
[markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= \["$1$", r"$\\frac{1}{2}$", "$f$", "$\\u266B$", r"$\\mathcal{A}$"\]

for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 in enumerate([markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
):
    \# Escape dollars so that the text is written "as is", not as mathtext.
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, repr([marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
).replace("$", r"\\$"), \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \* 3, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, \*\*[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Mathtext markers](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_004_2_00x.png)

Markers created from Paths[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-paths "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Any [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 can be used as a marker. The following example shows two simple paths _star_ and _circle_, and a more elaborate path of a circle with a cut-out star.

import numpy as np

import matplotlib.path as mpath

[star](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path.unit\_regular\_star](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_regular_star "matplotlib.path.Path.unit_regular_star")
(6)
[circle](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path.unit\_circle](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_circle "matplotlib.path.Path.unit_circle")
()
\# concatenate the circle with an internal cutout of the star
[cut\_star](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(
    vertices\=[np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[circle.vertices](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.vertices "matplotlib.path.Path.vertices")\
, [star.vertices](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.vertices "matplotlib.path.Path.vertices")\
\[::\-1, ...\]\]),
    codes\=[np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[circle.codes](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.codes "matplotlib.path.Path.codes")\
, [star.codes](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.codes "matplotlib.path.Path.codes")\
\]))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Path markers', fontsize\=14)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.4)

[markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'star': [star](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, 'circle': [circle](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, 'cut\_star': [cut\_star](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
}

for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
) in enumerate([markers](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \* 3, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, \*\*[marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Path markers](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_005_2_00x.png)

Advanced marker modifications with transform[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#advanced-marker-modifications-with-transform "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Markers can be modified by passing a transform to the MarkerStyle constructor. Following example shows how a supplied rotation is applied to several marker shapes.

[common\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {k: v for k, v in [filled\_marker\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items() if k != 'marker'}
[angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 10, 20, 30, 45, 60, 90\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Rotated markers', fontsize\=14)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, 0, 'Filled marker', \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 0, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
('o', 'left', [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
), \*\*[common\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, 1, 'Un-filled marker', \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 1, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
('1', 'left', [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
), \*\*[common\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, 2, 'Equation marker', \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [eq](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= r'$\\frac{1}{x}$'
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
([eq](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, 'left', [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
), \*\*[common\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2.5, f"{[theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
}°", horizontalalignment\="center")
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

![Rotated markers](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_006_2_00x.png)

Setting marker cap style and join style[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#setting-marker-cap-style-and-join-style "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Markers have default cap and join styles, but these can be customized when creating a MarkerStyle.

from matplotlib.markers import [CapStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
, [JoinStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")

[marker\_inner](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(markersize\=35,
                    markerfacecolor\='tab:blue',
                    markerfacecoloralt\='lightsteelblue',
                    markeredgecolor\='brown',
                    markeredgewidth\=8,
                    )

[marker\_outer](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(markersize\=35,
                    markerfacecolor\='tab:blue',
                    markerfacecoloralt\='lightsteelblue',
                    markeredgecolor\='white',
                    markeredgewidth\=1,
                    )

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Marker CapStyle', fontsize\=14)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.1)

for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [cap\_style](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 in enumerate([CapStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [cap\_style.name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
        [m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 \= [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
('1', transform\=[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
, capstyle\=[cap\_style](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
)
        [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
, \*\*[marker\_inner](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
        [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
, \*\*[marker\_outer](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, len([CapStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
) \- .5, f'{[theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
}°', ha\='center')
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Marker CapStyle](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_007_2_00x.png)

Modifying the join style:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Marker JoinStyle', fontsize\=14)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.05)

for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [join\_style](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 in enumerate([JoinStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [join\_style.name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[text\_style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([angles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
        [m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 \= [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
('\*', transform\=[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
, joinstyle\=[join\_style](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
)
        [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [marker](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
\=[m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
, \*\*[marker\_inner](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, len([JoinStyle](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
) \- .5, f'{[theta](https://docs.python.org/3/library/functions.html#int "builtins.int")
}°', ha\='center')
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Marker JoinStyle](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_008_2_00x.png)

Tags: [component: marker](https://matplotlib.org/stable/_tags/component-marker.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 3.322 seconds)

[`Download Jupyter notebook: marker_reference.ipynb`](https://matplotlib.org/stable/_downloads/06e654e0fb4f1e562a0a57e38cbc660c/marker_reference.ipynb)

[`Download Python source code: marker_reference.py`](https://matplotlib.org/stable/_downloads/af914017c64db37d6e814a5e9cdfb4a2/marker_reference.py)

[`Download zipped: marker_reference.zip`](https://matplotlib.org/stable/_downloads/8d1051f3bef6613d8ac2f3ebce7b5314/marker_reference.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page