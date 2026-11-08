[Skip to main content](https://matplotlib.org/stable/gallery/scales/asinh_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/scales/asinh_demo.html#sphx-glr-download-gallery-scales-asinh-demo-py)
 to download the full example code.

Asinh scale[#](https://matplotlib.org/stable/gallery/scales/asinh_demo.html#asinh-scale "Link to this heading")

================================================================================================================

Illustration of the [`asinh`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
 axis scaling, which uses the transformation

\\\[a \\rightarrow a\_0 \\sinh^{-1} (a / a\_0)\\\]

For coordinate values close to zero (i.e. much smaller than the "linear width" \\(a\_0\\)), this leaves values essentially unchanged:

\\\[a \\rightarrow a + \\mathcal{O}(a^3)\\\]

but for larger values (i.e. \\(|a| \\gg a\_0\\), this is asymptotically

\\\[a \\rightarrow a\_0 \\, \\mathrm{sgn}(a) \\ln |a| + \\mathcal{O}(1)\\\]

As with the [`symlog`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
 scaling, this allows one to plot quantities that cover a very wide dynamic range that includes both positive and negative values. However, `symlog` involves a transformation that has discontinuities in its gradient because it is built from _separate_ linear and logarithmic transformations. The `asinh` scaling uses a transformation that is smooth for all (finite) values, which is both mathematically cleaner and reduces visual artifacts associated with an abrupt transition between linear and logarithmic regions of the plot.

Note

[`scale.AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
 is experimental, and the API may change.

See [`AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
, [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
.

import matplotlib.pyplot as plt
import numpy as np

\# Prepare sample values for variations on y=x graph:
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 6, 500)

Compare "symlog" and "asinh" behaviour on sample y=x graph, where there is a discontinuous gradient in "symlog" near y=2:

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig1.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(1, 2, sharex\=True)

[ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax0.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('symlog')
[ax0.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ax0.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('symlog')

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('asinh')
[ax1.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('asinh')

![symlog, asinh](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_001_2_00x.png)

Compare "asinh" graphs with different scale parameter "linear\_width":

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig2.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(1, 3, sharex\=True)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([a0](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [base](https://docs.python.org/3/library/functions.html#int "builtins.int")
) in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ((0.2, 2), (1.0, 0), (5.0, 10))):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'linear\_width={[a0](https://docs.python.org/3/library/functions.html#float "builtins.float")
:.3g}')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='y=x')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 10\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='y=10x')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 100\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='y=100x')
    [ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('asinh', linear\_width\=[a0](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [base](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[base](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
    [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\='best', fontsize\='small')

![linear_width=0.2, linear_width=1, linear_width=5](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_002_2_00x.png)

Compare "symlog" and "asinh" scalings on 2D Cauchy-distributed random numbers, where one may be able to see more subtle artifacts near y=2 due to the gradient-discontinuity in "symlog":

[fig3](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig3.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(1, 1)
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 3 \* [np.tan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2.02, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2.02,
                                 size\=(5000,)))
[th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, size\=[r.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), s\=4, alpha\=0.5)
[ax.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('asinh')
[ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('symlog')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('asinh')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('symlog')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('2D Cauchy random deviates')
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-50, 50)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-50, 50)
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![2D Cauchy random deviates](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_003_2_00x.png)

References

*   [`matplotlib.scale.AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
    
*   [`matplotlib.ticker.AsinhLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator "matplotlib.ticker.AsinhLocator")
    
*   [`matplotlib.scale.SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
    

**Total running time of the script:** (0 minutes 3.855 seconds)

[`Download Jupyter notebook: asinh_demo.ipynb`](https://matplotlib.org/stable/_downloads/ac303b345a2a9a3062ea4c4527786c6c/asinh_demo.ipynb)

[`Download Python source code: asinh_demo.py`](https://matplotlib.org/stable/_downloads/c3e8c851c8fd86187bdf100a54e5afc4/asinh_demo.py)

[`Download zipped: asinh_demo.zip`](https://matplotlib.org/stable/_downloads/e48a71235a2bb0b4039c81aede1d98dc/asinh_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)