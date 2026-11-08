[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html#sphx-glr-download-gallery-text-labels-and-annotations-fonts-demo-kw-py)
 to download the full example code.

Fonts demo (keyword arguments)[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html#fonts-demo-keyword-arguments "Link to this heading")

============================================================================================================================================================================

Set font properties using keyword arguments.

See [Fonts demo (object-oriented style)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html)
 to achieve the same effect using setters.

![fonts demo kw](https://matplotlib.org/stable/_images/sphx_glr_fonts_demo_kw_001_2_00x.png)

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
[yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2\]

\# Show family options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.1, 0.9, 'family', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='large', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[families](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([families](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.1, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show style options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.9, 'style', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['normal', 'italic', 'oblique'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='sans-serif', [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show variant options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, 0.9, 'variant', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[variants](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['normal', 'small-caps'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([variants](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [family](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='serif', [variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[variant](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show weight options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.7, 0.9, 'weight', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.7, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show size options
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.9, 0.9, 'size', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'\]
for [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.9, [yp](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Show bold italic
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.1, 'bold italic',
         [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='x-small', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.2, 'bold italic',
         [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='medium', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.3, 0.3, 'bold italic',
         [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='italic', [weight](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='bold', [size](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='x-large', \*\*[alignment](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: fonts_demo_kw.ipynb`](https://matplotlib.org/stable/_downloads/329693a7abd578dec6c6a6e45787d7dc/fonts_demo_kw.ipynb)

[`Download Python source code: fonts_demo_kw.py`](https://matplotlib.org/stable/_downloads/9c5f5b75a1364025604ffb07f11a7118/fonts_demo_kw.py)

[`Download zipped: fonts_demo_kw.zip`](https://matplotlib.org/stable/_downloads/60dd72cbc9a57a0dcd5154c729859af1/fonts_demo_kw.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)