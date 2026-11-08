[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html#sphx-glr-download-gallery-shapes-and-collections-hatch-style-reference-py)
 to download the full example code.

Hatch style reference[#](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html#hatch-style-reference "Link to this heading")

===============================================================================================================================================================

Hatches can be added to most polygons in Matplotlib, including [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
, [`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
, [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
, and children of [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
. They are currently supported in the PS, PDF, SVG, macosx, and Agg backends. The WX and Cairo backends do not currently support hatching.

See also [Contourf hatching](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)
 for an example using [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
, and [Hatch demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html)
 for more usage examples.

import matplotlib.pyplot as plt

from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 5, layout\='constrained', figsize\=(6.4, 3.2))

[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['/', '\\\\', '|', '-', '+', 'x', 'o', 'O', '.', '\*'\]

def hatches\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
):
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((0, 0), 2, 2, fill\=False, hatch\=[h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1, \-0.5, f"' {[h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
} '", size\=15, ha\="center")
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('equal')
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    hatches\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![hatch style reference](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_001_2_00x.png)

Hatching patterns can be repeated to increase the density.

Note

In regular (non-raw) Python strings, backslashes must be escaped: `'\\\\'` and `r'\\'` are both the two-character hatch `\\`. Forgetting this silently halves the density — `'\\\\\\'` is only a triple hatch and thus sparser than `'//////'`.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 5, layout\='constrained', figsize\=(6.4, 3.2))

[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['//', r'\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '\*\*'\]

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    hatches\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![hatch style reference](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_002_2_00x.png)

Hatching patterns can be combined to create additional patterns.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 5, layout\='constrained', figsize\=(6.4, 3.2))

[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['/o', r'\\|', '|\*', r'\\-', '+o', 'x\*', 'o-', 'O|', 'O.', '\*-'\]

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    hatches\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [h](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![hatch style reference](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    

Tags: [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 1.604 seconds)

[`Download Jupyter notebook: hatch_style_reference.ipynb`](https://matplotlib.org/stable/_downloads/00fb9b6278ae3996d0eda53a7198ae42/hatch_style_reference.ipynb)

[`Download Python source code: hatch_style_reference.py`](https://matplotlib.org/stable/_downloads/8001758ca7a6a0a62185dff602f25056/hatch_style_reference.py)

[`Download zipped: hatch_style_reference.zip`](https://matplotlib.org/stable/_downloads/e84542c87c556ca1759485c226faca56/hatch_style_reference.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)