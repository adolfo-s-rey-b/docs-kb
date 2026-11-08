[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html#sphx-glr-download-gallery-lines-bars-and-markers-scatter-star-poly-py)
 to download the full example code.

Marker examples[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html#marker-examples "Link to this heading")

===============================================================================================================================================

Demonstrates several ways to specify markers in scatter plots, including built-in marker styles and custom marker paths.

See also the [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
 documentation for a list of all markers and [Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)
 for more information on configuring markers.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10)
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, sharex\=True, sharey\=True, layout\="constrained")

\# Matplotlib marker symbol
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=">")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title("marker='>'")

\# marker from TeX: passing a TeX symbol name enclosed in $-signs
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=r"$\\clubsuit$")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title(r"marker=r'\\$\\clubsuit\\$'")

\# marker from path: passing a custom path of N vertices as a (N, 2) array-like
[verts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\-1, \-1\], \[1, \-1\], \[1, 1\], \[\-1, \-1\]\]
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=[verts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title("marker=verts")

\# regular pentagon marker
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=(5, 0))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title("marker=(5, 0)")

\# regular 5-pointed star marker
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=(5, 1))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title("marker=(5, 1)")

\# regular 5-pointed asterisk marker
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=80, c\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=(5, 2))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].set\_title("marker=(5, 2)")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![marker='>', marker=r'\$\clubsuit\$', marker=verts, marker=(5, 0), marker=(5, 1), marker=(5, 2)](https://matplotlib.org/stable/_images/sphx_glr_scatter_star_poly_001_2_00x.png)

Tags: [component: marker](https://matplotlib.org/stable/_tags/component-marker.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 2.028 seconds)

[`Download Jupyter notebook: scatter_star_poly.ipynb`](https://matplotlib.org/stable/_downloads/504fdb7ac271d99d328d1d1d75d77e78/scatter_star_poly.ipynb)

[`Download Python source code: scatter_star_poly.py`](https://matplotlib.org/stable/_downloads/bec52923c4e8bde35b6455fdff6def07/scatter_star_poly.py)

[`Download zipped: scatter_star_poly.zip`](https://matplotlib.org/stable/_downloads/49db9d1769c7dcdae7bf39fa8cf1cefe/scatter_star_poly.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)