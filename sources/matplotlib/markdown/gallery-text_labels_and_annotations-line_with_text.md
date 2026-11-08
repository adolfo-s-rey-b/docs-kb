[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html#sphx-glr-download-gallery-text-labels-and-annotations-line-with-text-py)
 to download the full example code.

Artist within an artist[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html#artist-within-an-artist "Link to this heading")

=================================================================================================================================================================

Override basic methods so an artist can contain another artist. In this case, the line contains a Text instance to label it.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as lines
import matplotlib.text as mtext
import matplotlib.transforms as mtransforms

class MyLine([lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
):
    def \_\_init\_\_(self, \*args, \*\*kwargs):
        \# we'll update the position when the line data is set
        self.text \= [mtext.Text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
(0, 0, '')
        super().\_\_init\_\_(\*args, \*\*kwargs)

        \# we can't access the label attr until \*after\* the line is
        \# initiated
        self.text.set\_text(self.get\_label())

    def set\_figure(self, figure):
        self.text.set\_figure(figure)
        super().set\_figure(figure)

    \# Override the Axes property setter to set Axes on our children as well.
    @lines.Line2D.axes.setter
    def axes(self, new\_axes):
        self.text.axes \= new\_axes
        [lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.axes.fset(self, new\_axes)  \# Call the superclass property setter.

    def set\_transform(self, transform):
        \# 2 pixel offset
        texttrans \= transform + [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(2, 2)
        self.text.set\_transform(texttrans)
        super().set\_transform(transform)

    def set\_data(self, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
        if len([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
            self.text.set\_position(([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\]))

        super().set\_data([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    def draw(self, renderer):
        \# draw my label at the end of the line with 2 pixel offset
        super().draw(renderer)
        self.text.draw(renderer)

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, 20)
line \= [MyLine](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, mfc\='red', ms\=12, label\='line label')
[line.text.set\_color](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
('red')
[line.text.set\_fontsize](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")
(16)

[ax.add\_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
(line)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![line with text](https://matplotlib.org/stable/_images/sphx_glr_line_with_text_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.lines`](https://matplotlib.org/stable/api/lines_api.html#module-matplotlib.lines "matplotlib.lines")
    
*   [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
    
*   [`matplotlib.lines.Line2D.set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
    
*   [`matplotlib.artist`](https://matplotlib.org/stable/api/artist_api.html#module-matplotlib.artist "matplotlib.artist")
    
*   [`matplotlib.artist.Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    
*   [`matplotlib.artist.Artist.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "matplotlib.artist.Artist.draw")
    
*   [`matplotlib.artist.Artist.set_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform")
    
*   [`matplotlib.text`](https://matplotlib.org/stable/api/text_api.html#module-matplotlib.text "matplotlib.text")
    
*   [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
    
*   [`matplotlib.text.Text.set_color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
    
*   [`matplotlib.text.Text.set_fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")
    
*   [`matplotlib.text.Text.set_position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position")
    
*   [`matplotlib.axes.Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
    
*   [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
    
*   [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    

[`Download Jupyter notebook: line_with_text.ipynb`](https://matplotlib.org/stable/_downloads/454d14286bc8bd693ac8001a86d96cf6/line_with_text.ipynb)

[`Download Python source code: line_with_text.py`](https://matplotlib.org/stable/_downloads/41b07a606d47877f7b24b3b5e4dcbca8/line_with_text.py)

[`Download zipped: line_with_text.zip`](https://matplotlib.org/stable/_downloads/55d431b31a8483e135181aa8866857d3/line_with_text.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)