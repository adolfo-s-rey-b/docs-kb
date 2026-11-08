[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html#sphx-glr-download-gallery-text-labels-and-annotations-accented-text-py)
 to download the full example code.

Accented text[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html#accented-text "Link to this heading")

============================================================================================================================================

Matplotlib supports accented characters via TeX mathtext or Unicode.

Using mathtext, the following accents are provided: \\hat, \\breve, \\grave, \\bar, \\acute, \\tilde, \\vec, \\dot, \\ddot. All of them have the same syntax, e.g. \\bar{o} yields "o overbar", \\ddot{o} yields "o umlaut". Shortcuts such as \\"o \\'e \\\`e \\~n \\.x \\^y are also supported.

import matplotlib.pyplot as plt

\# Mathtext demo
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(r'$\\ddot{o}\\acute{e}\\grave{e}\\hat{O}'
             r'\\breve{i}\\bar{A}\\tilde{n}\\vec{q}$', fontsize\=20)

\# Shorthand is also supported and curly braces are optional
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
(r"""$\\"o\\ddot o \\'e\\\`e\\~n\\.x\\^y$""", fontsize\=20)
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(4, 0.5, r"$F=m\\ddot{x}$")
[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

![$\ddot{o}\acute{e}\grave{e}\hat{O}\breve{i}\bar{A}\tilde{n}\vec{q}$](https://matplotlib.org/stable/_images/sphx_glr_accented_text_001_2_00x.png)

You can also use Unicode characters directly in strings.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("LE COUP DE DÉ DE DE GAULLE")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('André was here!')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.2, 0.8, 'Institut für Festkörperphysik', rotation\=45)
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.4, 0.2, 'AVA (check kerning)')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![GISCARD CHAHUTÉ À L'ASSEMBLÉE](https://matplotlib.org/stable/_images/sphx_glr_accented_text_002_2_00x.png)

[`Download Jupyter notebook: accented_text.ipynb`](https://matplotlib.org/stable/_downloads/32692f6160c1c402e084acaba1e041dc/accented_text.ipynb)

[`Download Python source code: accented_text.py`](https://matplotlib.org/stable/_downloads/6fd60662b3bc1e803fc9f7e8e24a9025/accented_text.py)

[`Download zipped: accented_text.zip`](https://matplotlib.org/stable/_downloads/7d415d48fceae1de5bbb07ab8c1c9dc2/accented_text.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)