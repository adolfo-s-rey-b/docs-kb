[Skip to main content](https://matplotlib.org/stable/api/pylab.html#main-content)

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
    

`pylab`[#](https://matplotlib.org/stable/api/pylab.html#module-pylab "Link to this heading")

=============================================================================================

[`pylab`](https://matplotlib.org/stable/api/pylab.html#module-pylab "pylab")
 is a historic interface and its use is strongly discouraged. The equivalent replacement is [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
. See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
 for a full overview of Matplotlib interfaces.

[`pylab`](https://matplotlib.org/stable/api/pylab.html#module-pylab "pylab")
 was designed to support a MATLAB-like way of working with all plotting related functions directly available in the global namespace. This was achieved through a wildcard import (`from pylab import *`).

Warning

The use of [`pylab`](https://matplotlib.org/stable/api/pylab.html#module-pylab "pylab")
 is discouraged for the following reasons:

`from pylab import *` imports all the functions from [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
, [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "(in NumPy v2.5)")
, [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "(in NumPy v2.5)")
, [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "(in NumPy v2.5)")
, and [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "(in NumPy v2.5)")
, and some additional functions into the global namespace.

Such a pattern is considered bad practice in modern python, as it clutters the global namespace. Even more severely, in the case of [`pylab`](https://matplotlib.org/stable/api/pylab.html#module-pylab "pylab")
, this will overwrite some builtin functions (e.g. the builtin [`sum`](https://docs.python.org/3/library/functions.html#sum "(in Python v3.14)")
 will be replaced by [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "(in NumPy v2.5)")
), which can lead to unexpected behavior.