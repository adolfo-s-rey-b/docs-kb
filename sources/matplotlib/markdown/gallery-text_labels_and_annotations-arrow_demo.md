[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/arrow_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/arrow_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-arrow-demo-py)
 to download the full example code.

Arrow Demo[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/arrow_demo.html#arrow-demo "Link to this heading")

===================================================================================================================================

Three ways of drawing arrows to encode arrow "strength" (e.g., transition probabilities in a Markov model) using arrow length, width, or alpha (opacity).

![flux encoded as arrow length, flux encoded as arrow width, flux encoded as arrow alpha](https://matplotlib.org/stable/_images/sphx_glr_arrow_demo_001_2_00x.png)

import itertools

import matplotlib.pyplot as plt
import numpy as np

def make\_arrow\_graph([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=4, [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='length', shape\='right',
                     max\_arrow\_width\=0.03, arrow\_sep\=0.02, alpha\=0.5,
                     normalize\_data\=False, ec\=None, labelcolor\=None,
                     \*\*kwargs):
    """
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The Axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max\_arrow\_width : float
        Maximum width of an arrow, in data coordinates.
    arrow\_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    \*\*kwargs
        \`.FancyArrow\` properties, e.g. \*linewidth\* or \*edgecolor\*.
    """

    [ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-0.25, 1.25), ylim\=(\-0.25, 1.25), xticks\=\[\], yticks\=\[\],
           title\=f'flux encoded as arrow {[display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}')
    max\_text\_size \= [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* 12
    min\_text\_size \= [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
    label\_text\_size \= [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* 4

    bases \= 'ATGC'
    coords \= {
        'A': [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1\]),
        'T': [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1, 1\]),
        'G': [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 0\]),
        'C': [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1, 0\]),
    }
    colors \= {'A': 'r', 'T': 'k', 'G': 'g', 'C': 'b'}

    for base in bases:
        fontsize \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(max\_text\_size \* [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[base\]\*\*(1/2),
                           min\_text\_size, max\_text\_size)
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\*coords\[base\], f'${base}\_3$',
                color\=colors\[base\], [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=fontsize,
                horizontalalignment\='center', verticalalignment\='center',
                weight\='bold')

    arrow\_h\_offset \= 0.25  \# data coordinates, empirically determined
    max\_arrow\_length \= 1 \- 2 \* arrow\_h\_offset
    max\_head\_width \= 2.5 \* max\_arrow\_width
    max\_head\_length \= 2 \* max\_arrow\_width
    sf \= 0.6  \# max arrow size represents this in data coords

    if normalize\_data:
        \# find maximum value for rates, i.e. where keys are 2 chars long
        max\_val \= max((v for k, v in [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items() if len(k) \== 2), default\=0)
        \# divide rates by max val, multiply by arrow scale factor
        for k, v in [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
            [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[k\] \= v / max\_val \* sf

    \# iterate over strings 'AT', 'TA', 'AG', 'GA', etc.
    for pair in map(''.join, [itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations "itertools.permutations")
(bases, 2)):
        \# set the length of the arrow
        if [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \== 'length':
            length \= (max\_head\_length
                      + [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[pair\] / sf \* (max\_arrow\_length \- max\_head\_length))
        else:
            length \= max\_arrow\_length
        \# set the transparency of the arrow
        if [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \== 'alpha':
            alpha \= min([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[pair\] / sf, alpha)
        \# set the width of the arrow
        if [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \== 'width':
            scale \= [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[pair\] / sf
            width \= max\_arrow\_width \* scale
            head\_width \= max\_head\_width \* scale
            head\_length \= max\_head\_length \* scale
        else:
            width \= max\_arrow\_width
            head\_width \= max\_head\_width
            head\_length \= max\_head\_length

        fc \= colors\[pair\[0\]\]

        cp0 \= coords\[pair\[0\]\]
        cp1 \= coords\[pair\[1\]\]
        \# unit vector in arrow direction
        delta \= cos, sin \= (cp1 \- cp0) / [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\*(cp1 \- cp0))
        x\_pos, y\_pos \= (
            (cp0 + cp1) / 2  \# midpoint
            \- delta \* length / 2  \# half the arrow length
            + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\-sin, cos\]) \* arrow\_sep  \# shift outwards by arrow\_sep
        )
        [ax.arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow "matplotlib.axes.Axes.arrow")
(
            x\_pos, y\_pos, cos \* length, sin \* length,
            fc\=fc, ec\=ec or fc, alpha\=alpha, width\=width,
            head\_width\=head\_width, head\_length\=head\_length, shape\=shape,
            length\_includes\_head\=True,
            \*\*kwargs
        )

        \# figure out coordinates for text:
        \# if drawing relative to base: x and y are same as for arrow
        \# dx and dy are one arrow width left and up
        orig\_positions \= {
            'base': \[3 \* max\_arrow\_width, 3 \* max\_arrow\_width\],
            'center': \[length / 2, 3 \* max\_arrow\_width\],
            'tip': \[length \- 3 \* max\_arrow\_width, 3 \* max\_arrow\_width\],
        }
        \# for diagonal arrows, put the label at the arrow base
        \# for vertical or horizontal arrows, center the label
        where \= 'base' if (cp0 != cp1).all() else 'center'
        \# rotate based on direction of arrow (cos, sin)
        M \= \[\[cos, \-sin\], \[sin, cos\]\]
        x, y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(M, orig\_positions\[where\]) + \[x\_pos, y\_pos\]
        label \= r'$r\_{\_{\\mathrm{%s}}}$' % (pair,)
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(x, y, label, [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=label\_text\_size, ha\='center', va\='center',
                color\=labelcolor or fc)

if \_\_name\_\_ \== '\_\_main\_\_':
    [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {  \# test data
        'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
        'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
        'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
        'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
        'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
    }

    [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 4
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(3 \* [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
), layout\="constrained")
    [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(\[\["length", "width", "alpha"\]\])

    for [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
        make\_arrow\_graph(
            [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[display](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, linewidth\=0.001, edgecolor\=None,
            normalize\_data\=True, [size](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[size](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.386 seconds)

[`Download Jupyter notebook: arrow_demo.ipynb`](https://matplotlib.org/stable/_downloads/cc4e36bfe238f043e60002b4c16370c6/arrow_demo.ipynb)

[`Download Python source code: arrow_demo.py`](https://matplotlib.org/stable/_downloads/2d636f361d6c4d193b00e03241a15176/arrow_demo.py)

[`Download zipped: arrow_demo.zip`](https://matplotlib.org/stable/_downloads/ac8a7b3d01629e0813f017e5f770fe8d/arrow_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)