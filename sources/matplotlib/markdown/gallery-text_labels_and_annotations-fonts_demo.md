[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-fonts-demo-py)
 to download the full example code.

Fonts demo (object-oriented style)[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html#fonts-demo-object-oriented-style "Link to this heading")

=================================================================================================================================================================================

Set font properties using setters.

See [Fonts demo (keyword arguments)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html)
 to achieve the same effect using keyword arguments.

![fonts demo](https://matplotlib.org/stable/_images/sphx_glr_fonts_demo_001_2_00x.png)

import matplotlib.pyplot as plt

from matplotlib.font\_manager import [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
[yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2\]
[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='large')

\# Show family options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.1, 0.9, 'family', fontproperties\=[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[families](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([families](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=\[[family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\])
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.1, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show style options
[styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['normal', 'italic', 'oblique'\]
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.9, 'style', fontproperties\=[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='sans-serif', [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show variant options
[variants](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['normal', 'small-caps'\]
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, 0.9, 'variant', fontproperties\=[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([variants](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='serif', [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show weight options
[weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'\]
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.7, 0.9, 'weight', fontproperties\=[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.7, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show size options
[sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'\]
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.9, 0.9, 'size', fontproperties\=[heading\_font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.9, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show bold italic
[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='x-small')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.1, 'bold italic', fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='medium')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.2, 'bold italic', fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
([style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='x-large')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.3, 'bold italic', fontproperties\=[font](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: fonts_demo.ipynb`](https://matplotlib.org/stable/_downloads/7fceed023d9ab7f540f3ab5aa5f87514/fonts_demo.ipynb)

[`Download Python source code: fonts_demo.py`](https://matplotlib.org/stable/_downloads/a07ccc7ac96893982528857f66715b4d/fonts_demo.py)

[`Download zipped: fonts_demo.zip`](https://matplotlib.org/stable/_downloads/80797c847eb3eba50da6e6d7b2063d3e/fonts_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)