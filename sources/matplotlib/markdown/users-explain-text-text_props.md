[Skip to main content](https://matplotlib.org/stable/users/explain/text/text_props.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/text/text_props.html#sphx-glr-download-users-explain-text-text-props-py)
 to download the full example code.

Text properties and layout[#](https://matplotlib.org/stable/users/explain/text/text_props.html#text-properties-and-layout "Link to this heading")

==================================================================================================================================================

Controlling properties of text and its layout with Matplotlib.

[`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instances have a variety of properties which can be configured via keyword arguments to [`set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
, [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
, [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
, etc.

| Property | Value Type |
| --- | --- |
| alpha | [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
| backgroundcolor | any matplotlib [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| bbox | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")<br> prop dict plus key `'pad'` which is a pad in points |
| clip\_box | a matplotlib.transform.Bbox instance |
| clip\_on | bool |
| clip\_path | a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> instance and a [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")<br> instance, a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch") |
| color | any matplotlib [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| family | \[ `'serif'` \| `'sans-serif'` \| `'cursive'` \| `'fantasy'` \| `'monospace'` \] |
| fontproperties | [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties") |
| horizontalalignment or ha | \[ `'center'` \| `'right'` \| `'left'` \] |
| label | any string |
| linespacing | [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
| multialignment | \[`'left'` \| `'right'` \| `'center'` \] |
| name or fontname | string e.g., \[`'Sans'` \| `'Courier'` \| `'Helvetica'` ...\] |
| picker | \[None\|float\|bool\|callable\] |
| position | (x, y) |
| rotation | \[ angle in degrees \| `'vertical'` \| `'horizontal'` \] |
| size or fontsize | \[ size in points \| relative size, e.g., `'small'`, `'x-large'` \] |
| style or fontstyle | \[ `'normal'` \| `'italic'` \| `'oblique'` \] |
| text | string or anything printable with '%s' conversion |
| transform | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")<br> subclass |
| variant | \[ `'normal'` \| `'small-caps'` \] |
| verticalalignment or va | \[ `'center'` \| `'top'` \| `'bottom'` \| `'baseline'` \] |
| visible | bool |
| weight or fontweight | \[ `'normal'` \| `'bold'` \| `'heavy'` \| `'light'` \| `'ultrabold'` \| `'ultralight'`\] |
| x   | [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
| y   | [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
| zorder | any number |

Text alignment[#](https://matplotlib.org/stable/users/explain/text/text_props.html#text-alignment "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

You can lay out text with the alignment arguments `horizontalalignment`, `verticalalignment`, and `multialignment`. `horizontalalignment` controls whether the x positional argument for the text indicates the left, center or right side of the text bounding box. `verticalalignment` controls whether the y positional argument for the text indicates the bottom, center or top side of the text bounding box. `multialignment`, for newline separated strings only, controls whether the different lines are left, center or right justified. Here is an example which uses the [`text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
 command to show the various alignment possibilities. The use of `transform=ax.transAxes` throughout the code indicates that the coordinates are given relative to the Axes bounding box, with (0, 0) being the lower left of the Axes and (1, 1) the upper right.

import matplotlib.pyplot as plt

import matplotlib.patches as patches

\# build a rectangle in axes coords
[left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25, 0.5
[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25, 0.5
[right](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [height](https://docs.python.org/3/library/functions.html#float "builtins.float")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))

\# axes coordinates: (0, 0) is bottom left and (1, 1) is upper right
[p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 \= [patches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(
    ([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
), [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
    fill\=False, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, clip\_on\=False
    )

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
, 0.5\*([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'right center',
        horizontalalignment\='right',
        verticalalignment\='center',
        rotation\='vertical',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5\*([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'left center',
        horizontalalignment\='left',
        verticalalignment\='center',
        rotation\='vertical',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5\*([left](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[right](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 0.5\*([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
), 'middle',
        horizontalalignment\='center',
        verticalalignment\='center',
        fontsize\=20, color\='red',
        transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([right](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.5\*([bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[top](https://docs.python.org/3/library/functions.html#float "builtins.float")
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

![text props](https://matplotlib.org/stable/_images/sphx_glr_text_props_001_2_00x.png)

Relative font sizes[#](https://matplotlib.org/stable/users/explain/text/text_props.html#relative-font-sizes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Font sizes can be specified in points, or as a string that indicates the size relative to the default font size. The following are valid values for relative font sizes:

| Relative font size | Scaling of default font size |
| --- | --- |
| xx-small | 0.579 |
| x-small | 0.694 |
| small | 0.833 |
| medium | 1.000 |
| large | 1.200 |
| x-large | 1.440 |
| xx-large | 1.728 |

Default Font[#](https://matplotlib.org/stable/users/explain/text/text_props.html#default-font "Link to this heading")

======================================================================================================================

The base default font is controlled by a set of rcParams. To set the font for mathematical expressions, use the rcParams beginning with `mathtext` (see [mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext-fonts)
).

| rcParam | usage |
| --- | --- |
| `'font.family'` | List of font families (installed on user's machine) and/or `{'cursive', 'fantasy', 'monospace', 'sans', 'sans serif', 'sans-serif', 'serif'}`. |
| `'font.style'` | The default style, ex `'normal'`, `'italic'`. |
| `'font.variant'` | Default variant, ex `'normal'`, `'small-caps'` (untested) |
| `'font.stretch'` | Default stretch, ex `'normal'`, `'condensed'` (incomplete) |
| `'font.weight'` | Default weight. Either string or integer |
| `'font.size'` | Default font size in points. Relative font sizes (`'large'`, `'x-small'`) are computed against this size. |

Matplotlib can use font families installed on the user's computer, i.e. Helvetica, Times, etc. Font families can also be specified with generic-family aliases like (`{'cursive', 'fantasy', 'monospace', 'sans', 'sans serif', 'sans-serif', 'serif'}`).

Note

To access the full list of available fonts:

matplotlib.font\_manager.get\_font\_names()

The mapping between the generic family aliases and actual font families (mentioned at [default rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
) is controlled by the following rcParams:

| CSS-based generic-family alias | rcParam with mappings |
| --- | --- |
| `'serif'` | `'font.serif'` |
| `'monospace'` | `'font.monospace'` |
| `'fantasy'` | `'font.fantasy'` |
| `'cursive'` | `'font.cursive'` |
| `{'sans', 'sans serif', 'sans-serif'}` | `'font.sans-serif'` |

If any of generic family names appear in `'font.family'`, we replace that entry by all the entries in the corresponding rcParam mapping. For example:

matplotlib.rcParams\['font.family'\] \= \['Family1', 'serif', 'Family2'\]
matplotlib.rcParams\['font.serif'\] \= \['SerifFamily1', 'SerifFamily2'\]

\# This is effectively translated to:
matplotlib.rcParams\['font.family'\] \= \['Family1', 'SerifFamily1', 'SerifFamily2', 'Family2'\]

Text with non-latin glyphs[#](https://matplotlib.org/stable/users/explain/text/text_props.html#text-with-non-latin-glyphs "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

As of v2.0 the [default font](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#default-changes-font)
, DejaVu, contains glyphs for many western alphabets, but not other scripts, such as Chinese, Korean, or Japanese.

To set the default font to be one that supports the code points you need, prepend the font name to `'font.family'` (recommended), or to the desired alias lists.

\# first method
matplotlib.rcParams\['font.family'\] \= \['Source Han Sans TW', 'sans-serif'\]

\# second method
matplotlib.rcParams\['font.family'\] \= \['sans-serif'\]
matplotlib.rcParams\['sans-serif'\] \= \['Source Han Sans TW', ...\]

The generic family alias lists contain fonts that are either shipped alongside Matplotlib (so they have 100% chance of being found), or fonts which have a very high probability of being present in most systems.

A good practice when setting custom font families is to append a generic-family to the font-family list as a last resort.

You can also set it in your `.matplotlibrc` file:

font.family: Source Han Sans TW, Arial, sans\-serif

To control the font used on per-artist basis use the _name_, _fontname_ or _fontproperties_ keyword arguments documented in [Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props)
.

On linux, [fc-list](https://linux.die.net/man/1/fc-list)
 can be a useful tool to discover the font name; for example

$ fc-list :lang=zh family
Noto to Sans Mono CJK TC,Noto Sans Mono CJK TC Bold
Noto Sans CJK TC,Noto Sans CJK TC Medium
Noto Sans CJK TC,Noto Sans CJK TC DemiLight
Noto Sans CJK KR,Noto Sans CJK KR Black
Noto Sans CJK TC,Noto Sans CJK TC Black
Noto Sans Mono CJK TC,Noto Sans Mono CJK TC Regular
Noto Sans CJK SC,Noto Sans CJK SC Light

lists all of the fonts that support Chinese.

[`Download Jupyter notebook: text_props.ipynb`](https://matplotlib.org/stable/_downloads/16a2563b6427496cdb53f676f2b9816a/text_props.ipynb)

[`Download Python source code: text_props.py`](https://matplotlib.org/stable/_downloads/24fe8dfa54a83044ce4a75c45641def2/text_props.py)

[`Download zipped: text_props.zip`](https://matplotlib.org/stable/_downloads/51266afeb4315431042f607257192e8a/text_props.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page