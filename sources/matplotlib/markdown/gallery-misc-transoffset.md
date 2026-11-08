[Skip to main content](https://matplotlib.org/stable/gallery/misc/transoffset.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/transoffset.html#sphx-glr-download-gallery-misc-transoffset-py)
 to download the full example code.

transforms.offset\_copy[#](https://matplotlib.org/stable/gallery/misc/transoffset.html#transforms-offset-copy "Link to this heading")

======================================================================================================================================

This illustrates the use of [`transforms.offset_copy`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
 to make a transform that positions a drawing element such as a text string at a specified offset in screen coordinates (dots or inches) relative to a location given in any coordinates.

Every Artist (Text, Line2D, etc.) has a transform that can be set when the Artist is created, such as by the corresponding pyplot function. By default, this is usually the Axes.transData transform, going from data units to screen pixels. We can use the [`offset_copy`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
 function to make a modified copy of this transform, where the modification consists of an offset.

![transoffset](https://matplotlib.org/stable/_images/sphx_glr_transoffset_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.transforms as mtransforms

[xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(7)
[ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 10))
ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 1)

\# If we want the same offset for each text instance,
\# we only need to make one transform.  To get the
\# transform argument to offset\_copy, we need to make the Axes
\# first; the subplot function above is one way to do this.
[trans\_offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [mtransforms.offset\_copy](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
,
                                       [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
\=0.05, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
\=0.10, units\='inches')

for [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 in zip([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, 'ro')
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, '%d, %d' % (int([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
), int([y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
)), transform\=[trans\_offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)

\# offset\_copy works for polar plots also.
ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 2, projection\='polar')

[trans\_offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [mtransforms.offset\_copy](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
,
                                       [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
\=6, units\='dots')

for [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 in zip([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [plt.polar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib.pyplot.polar "matplotlib.pyplot.polar")
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, 'ro')
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, '%d, %d' % (int([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
), int([y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
)),
             transform\=[trans\_offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
             horizontalalignment\='center',
             verticalalignment\='bottom')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.068 seconds)

[`Download Jupyter notebook: transoffset.ipynb`](https://matplotlib.org/stable/_downloads/d09a6ddd0daca599aeda62065ad57a06/transoffset.ipynb)

[`Download Python source code: transoffset.py`](https://matplotlib.org/stable/_downloads/51f71780b1f0e8c2b3d14e33ae33f05f/transoffset.py)

[`Download zipped: transoffset.zip`](https://matplotlib.org/stable/_downloads/09bcca24d6b48658cf008eab8fbb7344/transoffset.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)