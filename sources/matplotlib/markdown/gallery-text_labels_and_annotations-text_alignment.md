[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html#sphx-glr-download-gallery-text-labels-and-annotations-text-alignment-py)
 to download the full example code.

Text alignment[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html#text-alignment "Link to this heading")

===============================================================================================================================================

Texts are aligned relative to their anchor point depending on the properties `horizontalalignment` (default: `left`) and `verticalalignment` (default: `baseline`.)

([`Source code`](https://matplotlib.org/stable/_downloads/34b57850619635be59d7cd6efce83636/text_alignment-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d1e6cc4abab17a9df4a4e155b6a13a3b/text_alignment-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9ace2c4b211a681cc795c4d18229934f/text_alignment-1.png)
)

[![](https://matplotlib.org/stable/_images/gallery-text_labels_and_annotations-text_alignment-1.2x.png)](https://matplotlib.org/stable/_images/gallery-text_labels_and_annotations-text_alignment-1.2x.png)

The following plot uses this to align text relative to a plotted rectangle.

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Build a rectangle in axes coords
[left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= .25, .5
[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= .25, .5
[right](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
[p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 \= [plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
), [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
, fill\=False)
[p.set\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform")
([ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)
[p.set\_clip\_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on")
(False)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'left top',
        horizontalalignment\='left',
        verticalalignment\='top',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'left bottom',
        horizontalalignment\='left',
        verticalalignment\='bottom',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([right](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'right bottom',
        horizontalalignment\='right',
        verticalalignment\='bottom',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([right](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'right top',
        horizontalalignment\='right',
        verticalalignment\='top',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([right](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'center top',
        horizontalalignment\='center',
        verticalalignment\='top',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5 \* ([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'right center',
        horizontalalignment\='right',
        verticalalignment\='center',
        rotation\='vertical',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5 \* ([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'left center',
        horizontalalignment\='left',
        verticalalignment\='center',
        rotation\='vertical',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5 \* ([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [right](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 0.5 \* ([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'middle',
        horizontalalignment\='center',
        verticalalignment\='center',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([right](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5 \* ([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'centered',
        horizontalalignment\='center',
        verticalalignment\='center',
        rotation\='vertical',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [top](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 'rotated\\nwith newlines',
        horizontalalignment\='center',
        verticalalignment\='center',
        rotation\=45,
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![text alignment](https://matplotlib.org/stable/_images/sphx_glr_text_alignment_001_2_00x.png)

[`Download Jupyter notebook: text_alignment.ipynb`](https://matplotlib.org/stable/_downloads/78978cde8f6f8ff3d132e70551f73977/text_alignment.ipynb)

[`Download Python source code: text_alignment.py`](https://matplotlib.org/stable/_downloads/5cab53f2f56674b26cb1a8e3c1eeb899/text_alignment.py)

[`Download zipped: text_alignment.zip`](https://matplotlib.org/stable/_downloads/3438cafcc0454d2246fd862faa196c71/text_alignment.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)