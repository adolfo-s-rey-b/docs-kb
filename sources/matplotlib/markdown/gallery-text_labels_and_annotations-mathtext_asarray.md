[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_asarray.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_asarray.html#sphx-glr-download-gallery-text-labels-and-annotations-mathtext-asarray-py)
 to download the full example code.

Convert texts to images[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_asarray.html#convert-texts-to-images "Link to this heading")

===================================================================================================================================================================

from io import [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
from matplotlib.transforms import [IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")

def text\_to\_rgba(s, \*, dpi, \*\*kwargs):
    \# To convert a text string to an image, we can:
    \# - draw it on an empty and transparent figure;
    \# - save the figure to a temporary buffer using \`\`bbox\_inches="tight",
    \#   pad\_inches=0\`\` which will pick the correct area to save;
    \# - load the buffer using \`\`PIL.Image.open\`\`.
    #
    \# (If desired, one can also directly save the image to the filesystem.)
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(facecolor\="none")
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0, 0, s, \*\*kwargs)
    with [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
() as buf:
        [fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
(buf, dpi\=dpi, format\="png", bbox\_inches\="tight",
                    pad\_inches\=0)
        buf.seek(0)
        rgba \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
(buf))
    return rgba

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[rgba1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= text\_to\_rgba(r"IQ: $\\sigma\_i=15$", color\="blue", fontsize\=20, dpi\=200)
[rgba2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= text\_to\_rgba(r"some other string", color\="red", fontsize\=20, dpi\=200)
\# One can then draw such text images to a Figure using \`.Figure.figimage\`.
[fig.figimage](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
([rgba1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 100, 50)
[fig.figimage](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
([rgba2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 100, 150)

\# One can also directly draw texts to a figure with positioning
\# in pixel coordinates by using \`.Figure.text\` together with
\# \`.transforms.IdentityTransform\`.
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(100, 250, r"IQ: $\\sigma\_i=15$", color\="blue", fontsize\=20,
         transform\=[IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(100, 350, r"some other string", color\="red", fontsize\=20,
         transform\=[IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![mathtext asarray](https://matplotlib.org/stable/_images/sphx_glr_mathtext_asarray_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.figure.Figure.figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
    
*   [`matplotlib.figure.Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
    
*   [`matplotlib.transforms.IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
    
*   [`matplotlib.image.imread`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "matplotlib.image.imread")
    

[`Download Jupyter notebook: mathtext_asarray.ipynb`](https://matplotlib.org/stable/_downloads/646ed6e33bfbf13d7f8129414dcebf05/mathtext_asarray.ipynb)

[`Download Python source code: mathtext_asarray.py`](https://matplotlib.org/stable/_downloads/fb498376a4f52d3e7e49f9367638b72d/mathtext_asarray.py)

[`Download zipped: mathtext_asarray.zip`](https://matplotlib.org/stable/_downloads/242e27b95d8f37478c527909ac05776d/mathtext_asarray.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)