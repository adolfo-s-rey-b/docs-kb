[Skip to main content](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#sphx-glr-download-gallery-scales-symlog-demo-py)
 to download the full example code.

Symlog scale[#](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#symlog-scale "Link to this heading")

===================================================================================================================

The symmetric logarithmic scale is an extension of the logarithmic scale that also covers negative values. As with the logarithmic scale, it is particularly useful for numerical data that spans a broad range of values, especially when there are significant differences between the magnitudes of the numbers involved.

Example use of symlog (symmetric log) axis scaling.

import matplotlib.pyplot as plt
import numpy as np

[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.01
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-50.0, 50.0, [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 100.0, [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3)

[ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax0.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog')
[ax0.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('symlogx')
[ax0.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ax0.xaxis.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid")
(which\='minor')  \# minor grid on too

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('symlog')
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('symlogy')

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 3.0))
[ax2.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog')
[ax2.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('symlog', linthresh\=0.015)
[ax2.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ax2.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('symlog both')

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![symlog demo](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_001_2_00x.png)

Linear threshold[#](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#linear-threshold "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Since each decade on a logarithmic scale covers the same amount of visual space and there are infinitely many decades between a given number and zero, the symlog scale must deviate from logarithmic mapping in a small range _(-linthresh, linthresh)_, so that the range is mapped to a finite visual space.

def format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\=None):
    """A helper function to better visualize properties of the symlog scale."""
    [ax.xaxis.get\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_locator.html#matplotlib.axis.Axis.get_minor_locator "matplotlib.axis.Axis.get_minor_locator")
().set\_params(subs\=\[2, 3, 4, 5, 6, 7, 8, 9\])
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
    [ax.xaxis.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid")
(which\='minor')  \# minor grid on too
    linthresh \= [ax.xaxis.get\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_transform.html#matplotlib.artist.Artist.get_transform "matplotlib.artist.Artist.get_transform")
().linthresh
    linscale \= [ax.xaxis.get\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_transform.html#matplotlib.artist.Artist.get_transform "matplotlib.artist.Artist.get_transform")
().linscale
    [ax.axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
(\-linthresh, linthresh, color\='0.9')
    if title:
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(title.format(linthresh\=linthresh, linscale\=linscale))

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-60, 60, 201)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 100.0, 201)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, layout\="constrained")

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog', linthresh\=1)
format\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\='Linear region: linthresh={linthresh}')

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog', linthresh\=5)
format\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\='Linear region: linthresh={linthresh}')

![Linear region: linthresh=1, Linear region: linthresh=5](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_002_2_00x.png)

Generally, _linthresh_ should be chosen so that no or only a few data points are in the linear region. As a rule of thumb, \\(linthresh \\approx \\mathrm{min} |x|\\).

Linear scale[#](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#linear-scale "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

Additionally, the _linscale_ parameter determines how much visual space should be used for the linear range. More precisely, it defines the ratio of visual space of the region (0, linthresh) relative to one decade.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, layout\="constrained")

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog', linthresh\=1)
format\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\='Linear region: linthresh={linthresh}, linscale={linscale}')

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog', linthresh\=1, linscale\=0.1)
format\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\='Linear region: linthresh={linthresh}, linscale={linscale}')

![Linear region: linthresh=1, linscale=1, Linear region: linthresh=1, linscale=0.1](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_003_2_00x.png)

The suitable value for linscale depends on the dynamic range of data. As most data will be outside the linear region, you typically the linear region only to cover a small fraction of the visual area.

Limitations and alternatives[#](https://matplotlib.org/stable/gallery/scales/symlog_demo.html#limitations-and-alternatives "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The coordinate transform used by `symlog` has a discontinuous gradient at the transition between its linear and logarithmic regions. Depending on data and scaling, this will be more or less obvious in the plot.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('symlog', linscale\=0.05)
format\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\="Discontinuous gradient at linear/log transition")

![Discontinuous gradient at linear/log transition](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_004_2_00x.png)

The `asinh` axis scale is an alternative transformation that supports a wide dynamic range with a smooth gradient and thus may avoid such visual artifacts. See [Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)
.

References

*   [`matplotlib.scale.SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
    
*   [`matplotlib.ticker.SymmetricalLogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator "matplotlib.ticker.SymmetricalLogLocator")
    
*   [`matplotlib.scale.AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
    

**Total running time of the script:** (0 minutes 5.000 seconds)

[`Download Jupyter notebook: symlog_demo.ipynb`](https://matplotlib.org/stable/_downloads/12a15d8f9ee7d7373e974c6b749bada7/symlog_demo.ipynb)

[`Download Python source code: symlog_demo.py`](https://matplotlib.org/stable/_downloads/525d48a4fd42b3666f5ef61d8acd742e/symlog_demo.py)

[`Download zipped: symlog_demo.zip`](https://matplotlib.org/stable/_downloads/55dee1cc72c5b44461bf987aa37b3465/symlog_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page