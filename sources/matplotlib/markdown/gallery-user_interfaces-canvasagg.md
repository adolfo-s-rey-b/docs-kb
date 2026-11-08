[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html#sphx-glr-download-gallery-user-interfaces-canvasagg-py)
 to download the full example code.

CanvasAgg demo[#](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html#canvasagg-demo "Link to this heading")

==============================================================================================================================

This example shows how to use the agg backend directly to create images, which may be of use to web application developers who want full control over their code without using the pyplot interface to manage figures, figure closing etc.

Note

It is not necessary to avoid using the pyplot interface in order to create figures without a graphical front-end - simply setting the backend to "Agg" would be sufficient.

In this example, we show how to save the contents of the agg canvas to a file, and how to extract them to a numpy array, which can in turn be passed off to [Pillow](https://pillow.readthedocs.io/)
. The latter functionality allows e.g. to use Matplotlib inside a cgi-script _without_ needing to write a figure to disk, and to write images in any format supported by Pillow.

from PIL import Image

import numpy as np

from matplotlib.backends.backend\_agg import [FigureCanvasAgg](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(5, 4), dpi\=100)

\# Do some plotting.
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\])

\# Option 1: Save the figure to a file; can also be a file-like object (BytesIO,
\# etc.).
[fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
("test.png")

\# Option 2 (low-level approach to directly save to a numpy array): Manually
\# attach a canvas to the figure (pyplot or savefig would automatically do
\# it), by instantiating the canvas with the figure as argument; then draw the
\# figure, retrieve a memoryview on the renderer buffer, and convert it to a
\# numpy array.
[canvas](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
 \= [FigureCanvasAgg](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
[canvas.draw](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.draw "matplotlib.backends.backend_agg.FigureCanvasAgg.draw")
()
[rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([canvas.buffer\_rgba](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.buffer_rgba "matplotlib.backends.backend_agg.FigureCanvasAgg.buffer_rgba")
())
\# ... and pass it to PIL.
[im](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image "PIL.Image.Image")
 \= [Image.fromarray](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.fromarray "PIL.Image.fromarray")
([rgba](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\# This image can then be saved to any format supported by Pillow, e.g.:
[im.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "PIL.Image.Image.save")
("test.bmp")

\# Uncomment this line to display the image using ImageMagick's \`display\` tool.
\# im.show()

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.backends.backend_agg.FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
    
*   [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    
*   [`matplotlib.figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
    
*   [`matplotlib.figure.Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
     / [`matplotlib.pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
    
*   [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     / [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
    

[`Download Jupyter notebook: canvasagg.ipynb`](https://matplotlib.org/stable/_downloads/2e7ac2468f5855121108bc279b6a5b2e/canvasagg.ipynb)

[`Download Python source code: canvasagg.py`](https://matplotlib.org/stable/_downloads/bea141aa211880f8734553ebfce669da/canvasagg.py)

[`Download zipped: canvasagg.zip`](https://matplotlib.org/stable/_downloads/60fbe277c61887bee58bd90cc2ef873b/canvasagg.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)