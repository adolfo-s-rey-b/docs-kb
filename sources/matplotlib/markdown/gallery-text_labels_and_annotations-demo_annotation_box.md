[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#sphx-glr-download-gallery-text-labels-and-annotations-demo-annotation-box-py)
 to download the full example code.

Artists as annotations[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#artists-as-annotations "Link to this heading")

====================================================================================================================================================================

[`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 facilitates using arbitrary artists as annotations, i.e. data at position _xy_ is annotated by a box containing an artist at position _xybox_. The coordinate systems for these points are set via the _xycoords_ and _boxcoords_ parameters, respectively; see the _xycoords_ and _textcoords_ parameters of [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 for a full listing of supported coordinate systems. The box containing the artist is a subclass of [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
, which is a container artist for positioning an artist relative to a parent artist.

from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")

import PIL

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import [get\_data\_path](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
from matplotlib.offsetbox import [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
, [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
, [OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
, [TextArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
from matplotlib.patches import [Annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")
, [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
, [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")

Text[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#text "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

[`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 supports positioning annotations relative to data, Artists, and callables, as described in [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
. The [`TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
 is used to create a textbox that is not explicitly attached to an axes, which allows it to be used for annotating figure objects. When annotating an axes element (such as a plot) with text, use [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 because it will create the text artist for you.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['t1', '.', 't2'\]\], layout\='compressed')

\# Define a 1st position to annotate (display it with a marker)
[xy1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (.25, .75)
[xy2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (.75, .25)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t1'\].plot(\*[xy1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, ".r")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t2'\].plot(\*[xy2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, ".r")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t1'\].set(xlim\=(0, 1), ylim\=(0, 1), aspect\='equal')
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t2'\].set(xlim\=(0, 1), ylim\=(0, 1), aspect\='equal')

\# Draw a connection patch arrow between the points
[c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 \= [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
(xyA\=[xy1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, xyB\=[xy2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
                    coordsA\=[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t1'\].transData, coordsB\=[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['t2'\].transData,
                    arrowstyle\='->')
[fig.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
([c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
)

\# Annotate the ConnectionPatch position ('Test 1')
[offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
 \= [TextArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
("Test 1")

\# place the annotation above the midpoint of c
[ab1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
,
                     [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=(.5, .5),
                     xybox\=(0, 30),
                     xycoords\=[c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
,
                     boxcoords\="offset points",
                     arrowprops\=dict(arrowstyle\="->"),
                     bboxprops\=dict(boxstyle\="sawtooth"))
[fig.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
([ab1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

![demo annotation box](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_001_2_00x.png)

Images[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#images "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

The [`OffsetImage`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
 container facilitates using images as annotations

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
\# Define a position to annotate
[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.3, 0.55)
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(\*[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, s\=200, marker\='X')

\# Annotate a position with an image generated from an array of pixels
[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))
[im](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
 \= [OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zoom\=2, cmap\='viridis')
[im.image.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.axes.html#matplotlib.artist.Artist.axes "matplotlib.artist.Artist.axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

\# place the image NW of xy
[ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([im](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
                    xybox\=(\-50., 50.),
                    xycoords\='data',
                    boxcoords\="offset points",
                    pad\=0.3,
                    arrowprops\=dict(arrowstyle\="->"))
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

\# Annotate the position with an image from file (a Grace Hopper portrait)
[img\_fp](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "pathlib.PosixPath")
 \= [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
([get\_data\_path](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
(), "sample\_data", "grace\_hopper.jpg")
with [PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
([img\_fp](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "pathlib.PosixPath")
) as [arr\_img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
:
    [imagebox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
 \= [OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
([arr\_img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
, zoom\=0.2)

[imagebox.image.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.axes.html#matplotlib.artist.Artist.axes "matplotlib.artist.Artist.axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

\# place the image SE of xy
[ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([imagebox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
                    xybox\=(120., \-80.),
                    xycoords\='data',
                    boxcoords\="offset points",
                    pad\=0.5,
                    arrowprops\=dict(
                        arrowstyle\="->",
                        connectionstyle\="angle,angleA=0,angleB=90,rad=3")
                    )

[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

\# Fix the display limits to see everything
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo annotation box](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_002_2_00x.png)

Arbitrary Artists[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html#arbitrary-artists "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Multiple and arbitrary artists can be placed inside a [`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
.

\# make this the thumbnail image
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Define a position to annotate
[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.05, 0.5)
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(\*[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, s\=500, marker\='X')

\# Annotate the position with a circle and annulus
[da](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
 \= [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
(120, 120)
[p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((30, 30), 25, color\='C0')
[da.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")
([p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[q](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")
 \= [Annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")
((65, 65), 50, 5, color\='C1')
[da.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")
([q](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")
)

\# Use the drawing area as an annotation
[ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([da](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
                    xybox\=(.55, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]),
                    xycoords\='data',
                    boxcoords\=("axes fraction", "data"),
                    box\_alignment\=(0, 0.5),
                    arrowprops\=dict(arrowstyle\="->"),
                    bboxprops\=dict(alpha\=0.5))

[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

\# Fix the display limits to see everything
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo annotation box](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.offsetbox.TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
    
*   [`matplotlib.offsetbox.DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
    
*   [`matplotlib.offsetbox.OffsetImage`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
    
*   [`matplotlib.offsetbox.AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
    

Tags: [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)

**Total running time of the script:** (0 minutes 1.503 seconds)

[`Download Jupyter notebook: demo_annotation_box.ipynb`](https://matplotlib.org/stable/_downloads/5f28215dd6e4e385c7b317d1a113df72/demo_annotation_box.ipynb)

[`Download Python source code: demo_annotation_box.py`](https://matplotlib.org/stable/_downloads/8f8964e173a4b95160a8595de75794d4/demo_annotation_box.py)

[`Download zipped: demo_annotation_box.zip`](https://matplotlib.org/stable/_downloads/84b07ef1e7f52a055e1b67c2901dc6bc/demo_annotation_box.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page