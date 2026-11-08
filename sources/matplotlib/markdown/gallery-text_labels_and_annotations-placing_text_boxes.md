[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html#sphx-glr-download-gallery-text-labels-and-annotations-placing-text-boxes-py)
 to download the full example code.

Placing text boxes[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html#placing-text-boxes "Link to this heading")

===========================================================================================================================================================

When decorating Axes with text boxes, two useful tricks are to place the text in axes coordinates (see [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
), so the text doesn't move around with changes in x or y limits. You can also use the `bbox` property of text to surround the text with a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 instance -- the `bbox` keyword argument takes a dictionary with keys that are Patch properties.

![placing text boxes](https://matplotlib.org/stable/_images/sphx_glr_placing_text_boxes_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 30\*[np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(10000)
[mu](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.mean()
[median](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.median](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[sigma](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.std()
[textstr](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '\\n'.join((
    r'$\\mu=%.2f$' % ([mu](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, ),
    r'$\\mathrm{median}\=%.2f$' % ([median](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, ),
    r'$\\sigma=%.2f$' % ([sigma](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, )))

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 50)
\# these are matplotlib.patch.Patch properties
[props](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(boxstyle\='round', facecolor\='wheat', alpha\=0.5)

\# place a text box in upper left in axes coords
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.05, 0.95, [textstr](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, fontsize\=14,
        verticalalignment\='top', bbox\=[props](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: placing_text_boxes.ipynb`](https://matplotlib.org/stable/_downloads/945a3cb57e8cb36e61dffbdec85bebfb/placing_text_boxes.ipynb)

[`Download Python source code: placing_text_boxes.py`](https://matplotlib.org/stable/_downloads/5791f26b231e858c2348b402b3931922/placing_text_boxes.py)

[`Download zipped: placing_text_boxes.zip`](https://matplotlib.org/stable/_downloads/524c7e814b0d5173365a0866b3586b3e/placing_text_boxes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)