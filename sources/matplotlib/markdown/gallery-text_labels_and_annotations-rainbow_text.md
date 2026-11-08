[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/rainbow_text.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/rainbow_text.html#sphx-glr-download-gallery-text-labels-and-annotations-rainbow-text-py)
 to download the full example code.

Concatenate text objects with different properties[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/rainbow_text.html#concatenate-text-objects-with-different-properties "Link to this heading")

=====================================================================================================================================================================================================================

The example strings together several Text objects with different properties (e.g., color or font), positioning each one after the other. The first Text is created directly using [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
; all subsequent ones are created with [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
, which allows positioning the Text's lower left corner at the lower right corner (`xy=(1, 0)`) of the previous one (`xycoords=text`).

![rainbow text](https://matplotlib.org/stable/_images/sphx_glr_rainbow_text_001_2_00x.png)

import matplotlib.pyplot as plt

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.size"\] \= 20
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(xticks\=\[\], yticks\=\[\])

\# The first word, created with text().
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.1, .5, "Matplotlib", color\="red")
\# Subsequent words, positioned with annotate(), relative to the preceding one.
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    " says,", xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
, xy\=(1, 0), verticalalignment\="bottom",
    color\="gold", weight\="bold")  \# custom properties
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    " hello", xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
, xy\=(1, 0), verticalalignment\="bottom",
    color\="green", style\="italic")  \# custom properties
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    " world!", xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
, xy\=(1, 0), verticalalignment\="bottom",
    color\="blue", family\="serif")  \# custom properties

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: rainbow_text.ipynb`](https://matplotlib.org/stable/_downloads/088ca86d579a97933334b09cf8f9f03f/rainbow_text.ipynb)

[`Download Python source code: rainbow_text.py`](https://matplotlib.org/stable/_downloads/a5b6cfad5a914962a881f60a919c0ca7/rainbow_text.py)

[`Download zipped: rainbow_text.zip`](https://matplotlib.org/stable/_downloads/740c51cb6f3028eab042fed5164bfdbf/rainbow_text.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)