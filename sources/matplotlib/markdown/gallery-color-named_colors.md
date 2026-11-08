[Skip to main content](https://matplotlib.org/stable/gallery/color/named_colors.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-download-gallery-color-named-colors-py)
 to download the full example code.

List of named colors[#](https://matplotlib.org/stable/gallery/color/named_colors.html#list-of-named-colors "Link to this heading")

===================================================================================================================================

This plots a list of the named colors supported by Matplotlib. For more information on colors in matplotlib see

*   the [Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
     tutorial;
    
*   the [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
     API;
    
*   the [Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)
    .
    

Helper Function for Plotting[#](https://matplotlib.org/stable/gallery/color/named_colors.html#helper-function-for-plotting "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

First we define a helper function for making a table of colors, then we use it on some common color categories.

import math

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

def plot\_colortable(colors, \*, ncols\=4, sort\_colors\=True):

    cell\_width \= 212
    cell\_height \= 22
    swatch\_width \= 48
    margin \= 12

    \# Sort colors by hue, saturation, value and name.
    if sort\_colors is True:
        names \= sorted(
            colors, key\=lambda c: tuple([mcolors.rgb\_to\_hsv](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.rgb_to_hsv.html#matplotlib.colors.rgb_to_hsv "matplotlib.colors.rgb_to_hsv")
([mcolors.to\_rgb](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgb.html#matplotlib.colors.to_rgb "matplotlib.colors.to_rgb")
(c))))
    else:
        names \= list(colors)

    n \= len(names)
    nrows \= [math.ceil](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
(n / ncols)

    width \= cell\_width \* ncols + 2 \* margin
    height \= cell\_height \* nrows + 2 \* margin
    dpi \= 72

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(width / dpi, height / dpi), dpi\=dpi)
    fig.subplots\_adjust(margin/width, margin/height,
                        (width\-margin)/width, (height\-margin)/height)
    ax.set\_xlim(0, cell\_width \* ncols)
    ax.set\_ylim(cell\_height \* (nrows\-0.5), \-cell\_height/2.)
    ax.yaxis.set\_visible(False)
    ax.xaxis.set\_visible(False)
    ax.set\_axis\_off()

    for i, name in enumerate(names):
        row \= i % nrows
        col \= i // nrows
        y \= row \* cell\_height

        swatch\_start\_x \= cell\_width \* col
        text\_pos\_x \= cell\_width \* col + swatch\_width + 7

        ax.text(text\_pos\_x, y, name, fontsize\=14,
                horizontalalignment\='left',
                verticalalignment\='center')

        ax.add\_patch(
            [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(xy\=(swatch\_start\_x, y\-9), width\=swatch\_width,
                      height\=18, facecolor\=colors\[name\], edgecolor\='0.7')
        )

    return fig

Base colors[#](https://matplotlib.org/stable/gallery/color/named_colors.html#base-colors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

plot\_colortable([mcolors.BASE\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, ncols\=3, sort\_colors\=False)

![named colors](https://matplotlib.org/stable/_images/sphx_glr_named_colors_001_2_00x.png)

Tableau Palette[#](https://matplotlib.org/stable/gallery/color/named_colors.html#tableau-palette "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

plot\_colortable([mcolors.TABLEAU\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, ncols\=2, sort\_colors\=False)

![named colors](https://matplotlib.org/stable/_images/sphx_glr_named_colors_002_2_00x.png)

CSS Colors[#](https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors "Link to this heading")

---------------------------------------------------------------------------------------------------------------

plot\_colortable([mcolors.CSS4\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![named colors](https://matplotlib.org/stable/_images/sphx_glr_named_colors_003_2_00x.png)

XKCD Colors[#](https://matplotlib.org/stable/gallery/color/named_colors.html#xkcd-colors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Matplotlib supports colors from the [xkcd color survey](https://xkcd.com/color/rgb/)
, e.g. `"xkcd:sky blue"`. Since this contains almost 1000 colors, a figure of this would be very large and is thus omitted here. You can use the following code to generate the overview yourself

xkcd\_fig \= plot\_colortable(mcolors.XKCD\_COLORS)
xkcd\_fig.savefig("XKCD\_Colors.png")

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
    
*   [`matplotlib.colors.rgb_to_hsv`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.rgb_to_hsv.html#matplotlib.colors.rgb_to_hsv "matplotlib.colors.rgb_to_hsv")
    
*   [`matplotlib.colors.to_rgba`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib.colors.to_rgba "matplotlib.colors.to_rgba")
    
*   [`matplotlib.figure.Figure.get_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_size_inches.html#matplotlib.figure.Figure.get_size_inches "matplotlib.figure.Figure.get_size_inches")
    
*   [`matplotlib.figure.Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    
*   [`matplotlib.patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
    

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 2.808 seconds)

[`Download Jupyter notebook: named_colors.ipynb`](https://matplotlib.org/stable/_downloads/bad4569afffc59fab7369853eda950d9/named_colors.ipynb)

[`Download Python source code: named_colors.py`](https://matplotlib.org/stable/_downloads/861cf0b07b083f3c44ddd625a0e99000/named_colors.py)

[`Download zipped: named_colors.zip`](https://matplotlib.org/stable/_downloads/93afd368b21efcbac3b47023e40fffc9/named_colors.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page