[Skip to main content](https://matplotlib.org/stable/users/explain/colors/colors.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/colors/colors.html#sphx-glr-download-users-explain-colors-colors-py)
 to download the full example code.

Specifying colors[#](https://matplotlib.org/stable/users/explain/colors/colors.html#specifying-colors "Link to this heading")

==============================================================================================================================

Color formats[#](https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Matplotlib recognizes the following formats to specify a color.

| Format | Example |
| --- | --- |
| RGB or RGBA (red, green, blue, alpha) tuple of float values in a closed interval \[0, 1\]. | *   `(0.1, 0.2, 0.5)`<br>    <br>*   `(0.1, 0.2, 0.5, 0.3)` |
| Case-insensitive hex RGB or RGBA string. | *   `'#0f0f0f'`<br>    <br>*   `'#0f0f0f80'` |
| Case-insensitive RGB or RGBA string equivalent hex shorthand of duplicated characters. | *   `'#abc'` as `'#aabbcc'`<br>    <br>*   `'#fb1'` as `'#ffbb11'` |
| String representation of float value in closed interval `[0, 1]` for grayscale values. | *   `'0'` as black<br>    <br>*   `'1'` as white<br>    <br>*   `'0.8'` as light gray |
| Single character shorthand notation for some basic colors.<br><br>Note<br><br>The colors green, cyan, magenta, and yellow do not coincide with X11/CSS4 colors. Their particular shades were chosen for better visibility of colored lines against typical backgrounds. | *   `'b'` as blue<br>    <br>*   `'g'` as green<br>    <br>*   `'r'` as red<br>    <br>*   `'c'` as cyan<br>    <br>*   `'m'` as magenta<br>    <br>*   `'y'` as yellow<br>    <br>*   `'k'` as black<br>    <br>*   `'w'` as white |
| Case-insensitive X11/CSS4 color name with no spaces. | *   `'aquamarine'`<br>    <br>*   `'mediumseagreen'` |
| Case-insensitive color name from [xkcd color survey](https://xkcd.com/color/rgb/)<br> with `'xkcd:'` prefix. | *   `'xkcd:sky blue'`<br>    <br>*   `'xkcd:eggshell'` |
| Case-insensitive Tableau Colors from 'T10' categorical palette.<br><br>Note<br><br>This is the default color cycle. | *   `'tab:blue'`<br>    <br>*   `'tab:orange'`<br>    <br>*   `'tab:green'`<br>    <br>*   `'tab:red'`<br>    <br>*   `'tab:purple'`<br>    <br>*   `'tab:brown'`<br>    <br>*   `'tab:pink'`<br>    <br>*   `'tab:gray'`<br>    <br>*   `'tab:olive'`<br>    <br>*   `'tab:cyan'` |
| "CN" color spec where `'C'` precedes a number acting as an index into the default property cycle.<br><br>Note<br><br>The cycle comes from the global `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`), not an Axes-local cycle set by [`set_prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle")<br>. Matplotlib indexes color at draw time and defaults to black if cycle does not include color. | *   `'C0'`<br>    <br>*   `'C1'` |
| Tuple of one of the above color formats and an alpha float.<br><br>Added in version 3.8. | *   `('green', 0.3)`<br>    <br>*   `('#f00', 0.9)` |
| The special value "none" is fully transparent, i.e. equivalent to a RGBA value `(0.0, 0.0, 0.0, 0.0)` | *   `'none'` |

See also

The following links provide more information on colors in Matplotlib.

*   [Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)
     Example
    
*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
     API
    
*   [List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
     Example
    

"Red", "Green", and "Blue" are the intensities of those colors. In combination, they represent the colorspace.

Transparency[#](https://matplotlib.org/stable/users/explain/colors/colors.html#transparency "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

The _alpha_ value of a color specifies its transparency, where 0 is fully transparent and 1 is fully opaque. When a color is semi-transparent, the background color will show through.

The _alpha_ value determines the resulting color by blending the foreground color with the background color according to the formula

\\\[RGB\_{result} = RGB\_{background} \* (1 - \\alpha) + RGB\_{foreground} \* \\alpha\\\]

The following plot illustrates the effect of transparency.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6.5, 1.65), layout\='constrained')
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((\-0.2, \-0.35), 11.2, 0.7, color\='C1', [alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=0.8))
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 in enumerate([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 11)):
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 0.05), 0.8, 0.6, [alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, zorder\=0))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
+0.4, 0.85, f"{[alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
:.1f}", ha\='center')
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, \-0.05), 0.8, \-0.6, [alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[alpha](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, zorder\=2))
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-0.2, 13)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 1)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('alpha values')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(11.3, 0.6, 'zorder=1', va\='center', color\='C0')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(11.3, 0, 'zorder=2\\nalpha=0.8', va\='center', color\='C1')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(11.3, \-0.6, 'zorder=3', va\='center', color\='C0')
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')

![alpha values](https://matplotlib.org/stable/_images/sphx_glr_colors_001_2_00x.png)

The orange rectangle is semi-transparent with _alpha_ = 0.8. The top row of blue squares is drawn below and the bottom row of blue squares is drawn on top of the orange rectangle.

See also [Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)
 to learn more on the drawing order.

"CN" color selection[#](https://matplotlib.org/stable/users/explain/colors/colors.html#cn-color-selection "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Matplotlib converts "CN" colors to RGBA when drawing Artists. The [Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#color-cycle)
 section contains additional information about controlling colors and style properties.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

[th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 128)

def demo(sty):
    [mpl.style.use](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")
(sty)
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))

    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'style: {sty!r}', color\='C0')

    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 'C1', label\='C1')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 'C2', label\='C2')
    [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

demo('default')
demo('seaborn-v0\_8')

*   ![style: 'default'](https://matplotlib.org/stable/_images/sphx_glr_colors_002_2_00x.png)
*   ![style: 'seaborn-v0_8'](https://matplotlib.org/stable/_images/sphx_glr_colors_003_2_00x.png)

The first color `'C0'` is the title. Each plot uses the second and third colors of each style's `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`). They are `'C1'` and `'C2'`, respectively.

Comparison between X11/CSS4 and xkcd colors[#](https://matplotlib.org/stable/users/explain/colors/colors.html#comparison-between-x11-css4-and-xkcd-colors "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The xkcd colors come from a [user survey conducted by the webcomic xkcd](https://blog.xkcd.com/2010/05/03/color-survey-results/)
.

95 out of the 148 X11/CSS4 color names also appear in the xkcd color survey. Almost all of them map to different color values in the X11/CSS4 and in the xkcd palette. Only 'black', 'white' and 'cyan' are identical.

For example, `'blue'` maps to `'#0000FF'` whereas `'xkcd:blue'` maps to `'#0343DF'`. Due to these name collisions, all xkcd colors have the `'xkcd:'` prefix.

The visual below shows name collisions. Color names where color values agree are in bold.

import matplotlib.colors as mcolors
import matplotlib.patches as mpatch

[overlap](https://docs.python.org/3/library/stdtypes.html#set "builtins.set")
 \= {name for name in [mcolors.CSS4\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
           if f'xkcd:{name}' in [mcolors.XKCD\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=\[9, 5\])
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))

[n\_groups](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 3
[n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([overlap](https://docs.python.org/3/library/stdtypes.html#set "builtins.set")
) // [n\_groups](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1

for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate(sorted([overlap](https://docs.python.org/3/library/stdtypes.html#set "builtins.set")
)):
    [css4](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [mcolors.CSS4\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]
    [xkcd](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [mcolors.XKCD\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[f'xkcd:{[color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
}'\].upper()

    \# Pick text colour based on perceived luminance.
    [rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [mcolors.to\_rgba\_array](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")
(\[[css4](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
, [xkcd](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\])
    [luma](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.299 \* [rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\] + 0.587 \* [rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\] + 0.114 \* [rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\]
    [css4\_text\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'k' if [luma](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\] \> 0.5 else 'w'
    [xkcd\_text\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'k' if [luma](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\] \> 0.5 else 'w'

    [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= ([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // [n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
) \* 3
    [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 % [n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
    [text\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(fontsize\=10, weight\='bold' if [css4](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \== [xkcd](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 else None)
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([mpatch.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((0 + [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
), 1, 1, color\=[css4](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([mpatch.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((1 + [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
), 1, 1, color\=[xkcd](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5 + [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + .7, [css4](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
            color\=[css4\_text\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, ha\='center', \*\*[text\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1.5 + [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + .7, [xkcd](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
            color\=[xkcd\_text\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, ha\='center', \*\*[text\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(2 + [col\_shift](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y\_pos](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + .7, f'  {[color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}', \*\*[text\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

for [g](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([n\_groups](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [ax.hlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines "matplotlib.axes.Axes.hlines")
(range([n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
), 3\*[g](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 3\*[g](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 2.8, color\='0.7', linewidth\=1)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5 + 3\*[g](https://docs.python.org/3/library/functions.html#int "builtins.int")
, \-0.3, 'X11/CSS4', ha\='center')
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1.5 + 3\*[g](https://docs.python.org/3/library/functions.html#int "builtins.int")
, \-0.3, 'xkcd', ha\='center')

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 3 \* [n\_groups](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
([n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
, \-1)
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![colors](https://matplotlib.org/stable/_images/sphx_glr_colors_004_2_00x.png)

**Total running time of the script:** (0 minutes 2.938 seconds)

[`Download Jupyter notebook: colors.ipynb`](https://matplotlib.org/stable/_downloads/3761761bc2c3918b60021a855b3e3d0b/colors.ipynb)

[`Download Python source code: colors.py`](https://matplotlib.org/stable/_downloads/c72ce5570d6edb7c95b72e06f668bdce/colors.py)

[`Download zipped: colors.zip`](https://matplotlib.org/stable/_downloads/55b0bbea1048cf55165a696493894f3d/colors.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page