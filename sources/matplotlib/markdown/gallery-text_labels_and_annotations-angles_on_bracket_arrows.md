[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html#sphx-glr-download-gallery-text-labels-and-annotations-angles-on-bracket-arrows-py)
 to download the full example code.

Angle annotations on bracket arrows[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html#angle-annotations-on-bracket-arrows "Link to this heading")

===================================================================================================================================================================================================

This example shows how to add angle annotations to bracket arrow styles created using [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
. _angleA_ and _angleB_ are measured from a vertical line as positive (to the left) or negative (to the right). Blue [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
 arrows indicate the directions of _angleA_ and _angleB_ from the vertical and axes text annotate the angle sizes.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")

def get\_point\_of\_rotated\_vertical(origin, line\_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad \= [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-degrees)
    return \[origin\[0\] + line\_length \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(rad),\
            origin\[1\] + line\_length \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(rad)\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 6), ylim\=(\-1, 5))
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Orientation of the bracket arrows relative to angleA and angleB")

[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '\]-\['\
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in enumerate(\[\-40, 0, 60\]):\
    [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \= 2\*[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
    [arrow\_centers](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 \= ((1, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
), (5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
))\
    [vlines](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 \= ((1, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 0.5), (5, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 0.5))\
    [anglesAB](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 \= ([angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, \-[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\
    [bracketstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
 \= f"{[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
}, angleA={[anglesAB](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\[0\]}, angleB={[anglesAB](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\[1\]}"\
    [bracket](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
 \= [FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
(\*[arrow\_centers](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [arrowstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\=[bracketstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
,\
                              mutation\_scale\=42)\
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")\
([bracket](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
)\
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
(3, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 0.05, [bracketstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
, ha\="center", va\="bottom", fontsize\=14)\
    [ax.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")\
(\[line\[0\] for line in [vlines](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\], \[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], \[line\[1\] for line in [vlines](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\],\
              linestyles\="--", color\="C0")\
    \# Get the top coordinates for the drawn patches at A and B\
    [patch\_tops](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
 \= \[get\_point\_of\_rotated\_vertical(center, 0.5, [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\
                  for center, [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in zip([arrow\_centers](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [anglesAB](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
)\]\
    \# Define the connection directions for the annotation arrows\
    [connection\_dirs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 \= (1, \-1) if [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \> 0 else (\-1, 1)\
    \# Add arrows and annotation text\
    [arrowstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
 \= "Simple, tail\_width=0.5, head\_width=4, head\_length=8"\
    for [vline](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, dir, [patch\_top](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in zip([vlines](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [connection\_dirs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
,\
                                            [patch\_tops](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [anglesAB](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
):\
        [kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")\
 \= dict(connectionstyle\=f"arc3,rad={dir \* 0.5}",\
                  [arrowstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\=[arrowstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
, color\="C0")\
        [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")\
([FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
([vline](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [patch\_top](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")\
))\
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
([vline](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\[0\] \- dir \* 0.15, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 0.7, f'{[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}°', ha\="center",\
                va\="center")\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
![Orientation of the bracket arrows relative to angleA and angleB](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_001_2_00x.png)\
\
References\
\
The use of the following functions, methods, classes and modules is shown in this example:\
\
*   [`matplotlib.patches.ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")\
    \
\
[`Download Jupyter notebook: angles_on_bracket_arrows.ipynb`](https://matplotlib.org/stable/_downloads/cbc861114d23f7b90a621d96ab81f4b4/angles_on_bracket_arrows.ipynb)\
\
[`Download Python source code: angles_on_bracket_arrows.py`](https://matplotlib.org/stable/_downloads/4af2c72e985d6771b93719ce29b0b6ac/angles_on_bracket_arrows.py)\
\
[`Download zipped: angles_on_bracket_arrows.zip`](https://matplotlib.org/stable/_downloads/00c5504fb7c2dac95f97dfc7fb5df3a0/angles_on_bracket_arrows.zip)\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)