[Skip to main content](https://matplotlib.org/stable/gallery/scales/logit_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/scales/logit_demo.html#sphx-glr-download-gallery-scales-logit-demo-py)
 to download the full example code.

Logit scale[#](https://matplotlib.org/stable/gallery/scales/logit_demo.html#logit-scale "Link to this heading")

================================================================================================================

Examples of plots with logit axes.

This example visualises how `set_yscale("logit")` works on probability plots by generating three distributions: normal, laplacian, and cauchy in one plot.

The advantage of logit scale is that it effectively spreads out values close to 0 and 1.

In a linear scale plot, probability values near 0 and 1 appear compressed, making it difficult to see differences in those regions.

In a logit scale plot, the transformation expands these regions, making the graph cleaner and easier to compare across different probability values.

This makes the logit scale especially useful when visalising probabilities in logistic regression, classification models, and cumulative distribution functions.

![logit scale, logit scale, logit scale, logit scale, linear scale, linear scale](https://matplotlib.org/stable/_images/sphx_glr_logit_demo_001_2_00x.png)

import math

import matplotlib.pyplot as plt
import numpy as np

[xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-[xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 10000)
[cdf\_norm](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[math.erf](https://docs.python.org/3/library/math.html#math.erf "math.erf")\
(w / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(2)) / 2 + 1 / 2 for w in [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]
[cdf\_laplacian](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 < 0, 1 / 2 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 1 \- 1 / 2 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[cdf\_cauchy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + 1 / 2

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, ncols\=2, figsize\=(6.4, 8.5))

\# Common part, for the example, we will do the same plots on all graphs
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(3):
    for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cdf\_norm](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=r"$\\mathcal{N}$")
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cdf\_laplacian](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\=r"$\\mathcal{L}$")
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cdf\_cauchy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="Cauchy")
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].legend()
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].grid()

\# First line, logitscale, with standard notation
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set(title\="logit scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_yscale("logit")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_ylim(1e-5, 1 \- 1e-5)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set(title\="logit scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_yscale("logit")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_xlim(0, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_ylim(0.8, 1 \- 5e-3)

\# Second line, logitscale, with survival notation (with \`use\_overline\`), and
\# other format display 1/2
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set(title\="logit scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_yscale("logit", one\_half\="1/2", use\_overline\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_ylim(1e-5, 1 \- 1e-5)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set(title\="logit scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_yscale("logit", one\_half\="1/2", use\_overline\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_xlim(0, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_ylim(0.8, 1 \- 5e-3)

\# Third line, linear scale
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 0\].set(title\="linear scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 0\].set\_ylim(0, 1)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 1\].set(title\="linear scale")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 1\].set\_xlim(0, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 1\].set\_ylim(0.8, 1)

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 3.310 seconds)

[`Download Jupyter notebook: logit_demo.ipynb`](https://matplotlib.org/stable/_downloads/1995eb90ca3090322cbb5cb8ba054d0a/logit_demo.ipynb)

[`Download Python source code: logit_demo.py`](https://matplotlib.org/stable/_downloads/c45fd17e10ff2324af973d556a378f18/logit_demo.py)

[`Download zipped: logit_demo.zip`](https://matplotlib.org/stable/_downloads/07a3faa9a5512fe2e19e5e196df1aac0/logit_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)