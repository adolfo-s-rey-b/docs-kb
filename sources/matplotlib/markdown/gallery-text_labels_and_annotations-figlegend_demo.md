[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/figlegend_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/figlegend_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-figlegend-demo-py)
 to download the full example code.

Figure legend demo[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/figlegend_demo.html#figure-legend-demo "Link to this heading")

=======================================================================================================================================================

Rather than plotting a legend on each axis, a legend for all the artists on all the sub-axes of a figure can be plotted instead.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained')

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 4\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.2)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), label\='Line 1')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2), marker\='o', label\='Line 2')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), color\='tab:green', label\='Line 3')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/4), color\='tab:red', marker\='^', label\='Line 4')

[fig.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
(loc\='outside right upper')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![figlegend demo](https://matplotlib.org/stable/_images/sphx_glr_figlegend_demo_001_2_00x.png)

The outside positioning is discussed in detail here: [https://matplotlib.org/stable/users/explain/axes/legend\_guide.html#figure-legends](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#figure-legends)

See also

The [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 contains an in depth discussion on the configuration options for legends.

**Total running time of the script:** (0 minutes 1.197 seconds)

[`Download Jupyter notebook: figlegend_demo.ipynb`](https://matplotlib.org/stable/_downloads/25e33319638f2e3971829d70fb305d42/figlegend_demo.ipynb)

[`Download Python source code: figlegend_demo.py`](https://matplotlib.org/stable/_downloads/5f2c35d6ffe75884c672ca725851c0f4/figlegend_demo.py)

[`Download zipped: figlegend_demo.zip`](https://matplotlib.org/stable/_downloads/7b289cf0b87b3296dac8425beec3e96f/figlegend_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)