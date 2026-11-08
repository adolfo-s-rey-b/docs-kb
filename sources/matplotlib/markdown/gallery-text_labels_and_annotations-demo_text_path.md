[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html#sphx-glr-download-gallery-text-labels-and-annotations-demo-text-path-py)
 to download the full example code.

Using a text as a Path[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html#using-a-text-as-a-path "Link to this heading")

===============================================================================================================================================================

[`TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.text.TextPath")
 creates a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 that is the outline of the characters of a text. The resulting path can be employed e.g. as a clip path for an image.

![demo text path](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_001_2_00x.png)

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
from matplotlib.image import [BboxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
from matplotlib.offsetbox import [AnchoredOffsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
, [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
, [AuxTransformBox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
from matplotlib.patches import [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
, [Shadow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
from matplotlib.text import [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.transforms import [IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")

class PathClippedImagePatch([PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
):
    """
    The given image is used to draw the face of the patch. Internally,
    it uses BboxImage whose clippath set to the path of the patch.

    FIXME : The result is currently dpi dependent.
    """

    def \_\_init\_\_(self, path, bbox\_image, \*\*kwargs):
        super().\_\_init\_\_(path, \*\*kwargs)
        self.bbox\_image \= [BboxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
(
            self.get\_window\_extent, norm\=None, origin\=None)
        self.bbox\_image.set\_data(bbox\_image)

    def set\_facecolor(self, color):
        """Simply ignore facecolor."""
        super().set\_facecolor("none")

    def draw(self, renderer\=None):
        \# the clip path must be updated every draw. any solution? -JJ
        self.bbox\_image.set\_clip\_path(self.\_path, self.get\_transform())
        self.bbox\_image.draw(renderer)
        super().draw(renderer)

if \_\_name\_\_ \== "\_\_main\_\_":

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2)

    \# EXAMPLE 1

    [arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
([get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("grace\_hopper.jpg"))

    text\_path \= [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
((0, 0), "!?", size\=150)
    p \= [PathClippedImagePatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(text\_path, [arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ec\="k")

    \# make offset box
    [offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
 \= [AuxTransformBox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
([IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
    [offsetbox.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
(p)

    \# make anchored offset box
    [ao](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
 \= [AnchoredOffsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
(loc\='upper left', child\=[offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
, frameon\=True,
                           borderpad\=0.2)
    [ax1.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ao](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
)

    \# another text
    for [usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
, [ypos](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [string](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \[\
            (False, 0.25, r"textpath supports mathtext"),\
            (True, 0.05, r"textpath supports \\TeX"),\
    \]:
        text\_path \= [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
((0, 0), [string](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, size\=20, [usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
\=[usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
)

        [p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(text\_path, ec\="w", lw\=3, fc\="w", alpha\=0.9)
        [p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(text\_path, ec\="none", fc\="k")

        [offsetbox2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
 \= [AuxTransformBox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
([IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
        [offsetbox2.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
([p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
        [offsetbox2.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
([p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)

        [ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([offsetbox2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
, (0.95, [ypos](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                            xycoords\='axes fraction',
                            boxcoords\="offset points",
                            box\_alignment\=(1., 0.),
                            frameon\=False,
                            )
        [ax1.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

    [ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[0, 1, 2\], \[1, 2, 3\]\], cmap\="gist\_gray\_r",
               interpolation\="bilinear", aspect\="auto")

    \# EXAMPLE 2

    [arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(256).reshape(1, 256)

    for [usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
, [xpos](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [string](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \[\
            (False, 0.25,\
             r"$\\left\[\\sum\_{n=1}^\\infty\\frac{-e^{i\\pi}}{2^n}\\right\]$!"),\
            (True, 0.75,\
             r"$\\displaystyle\\left\[\\sum\_{n=1}^\\infty"\
             r"\\frac{-e^{i\\pi}}{2^n}\\right\]$!"),\
    \]:
        text\_path \= [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
((0, 0), [string](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, size\=40, [usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
\=[usetex](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
)
        text\_patch \= [PathClippedImagePatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(text\_path, [arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ec\="none")
        [shadow1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 \= [Shadow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
(text\_patch, 1, \-1, fc\="none", ec\="0.6", lw\=3)
        [shadow2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 \= [Shadow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
(text\_patch, 1, \-1, fc\="0.3", ec\="none")

        \# make offset box
        [offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
 \= [AuxTransformBox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
([IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
        [offsetbox.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
([shadow1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
)
        [offsetbox.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
([shadow2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
)
        [offsetbox.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "matplotlib.offsetbox.AuxTransformBox.add_artist")
(text\_patch)

        \# place the anchored offset box using AnnotationBbox
        [ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
([offsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
, ([xpos](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5), box\_alignment\=(0.5, 0.5))

        [ax2.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ab](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
)

    [ax2.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 1)
    [ax2.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 1)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.905 seconds)

[`Download Jupyter notebook: demo_text_path.ipynb`](https://matplotlib.org/stable/_downloads/05551433a67337134e29a429c24d6769/demo_text_path.ipynb)

[`Download Python source code: demo_text_path.py`](https://matplotlib.org/stable/_downloads/986997c8a8bb17b365f417251e167454/demo_text_path.py)

[`Download zipped: demo_text_path.zip`](https://matplotlib.org/stable/_downloads/418371c6032d86e47b1e0874fbf5c889/demo_text_path.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)