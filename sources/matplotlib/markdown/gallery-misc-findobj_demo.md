[Skip to main content](https://matplotlib.org/stable/gallery/misc/findobj_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/findobj_demo.html#sphx-glr-download-gallery-misc-findobj-demo-py)
 to download the full example code.

Findobj Demo[#](https://matplotlib.org/stable/gallery/misc/findobj_demo.html#findobj-demo "Link to this heading")

==================================================================================================================

Recursively find all objects that match some criteria

![Minimum Message Length](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.text as text

[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 3, .02)
[b](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 3, .02)
[c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[d](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::\-1\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k--', [a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [d](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k:', [a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [d](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k')
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(('Model length', 'Data length', 'Total message length'),
           loc\='upper center', shadow\=True)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[\-1, 20\])
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(False)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
('Model complexity --->')
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
('Message length --->')
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Minimum Message Length')

\# match on arbitrary function
def myfunc(x):
    return hasattr(x, 'set\_color') and not hasattr(x, 'set\_facecolor')

for [o](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in [fig.findobj](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.findobj.html#matplotlib.artist.Artist.findobj "matplotlib.artist.Artist.findobj")
(myfunc):
    [o.set\_color](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
('blue')

\# match on class instances
for [o](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in [fig.findobj](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.findobj.html#matplotlib.artist.Artist.findobj "matplotlib.artist.Artist.findobj")
([text.Text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
):
    [o.set\_fontstyle](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")
('italic')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: findobj_demo.ipynb`](https://matplotlib.org/stable/_downloads/707278e40febb1ee8abb05052b9ccd4a/findobj_demo.ipynb)

[`Download Python source code: findobj_demo.py`](https://matplotlib.org/stable/_downloads/4095e40bfdaeea40b5ebf921dca65a60/findobj_demo.py)

[`Download zipped: findobj_demo.zip`](https://matplotlib.org/stable/_downloads/635a6dd0aa49f8bed82883b742492b6c/findobj_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)