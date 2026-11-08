[Skip to main content](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html#sphx-glr-download-gallery-showcase-mandelbrot-py)
 to download the full example code.

Shaded & power normalized rendering[#](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html#shaded-power-normalized-rendering "Link to this heading")

================================================================================================================================================================

The Mandelbrot set rendering can be improved by using a normalized recount associated with a power normalized colormap (gamma=0.3). Rendering can be further enhanced thanks to shading.

The `maxiter` gives the precision of the computation. `maxiter=200` should take a few seconds on most modern laptops.

![mandelbrot](https://matplotlib.org/stable/_images/sphx_glr_mandelbrot_001_2_00x.png)

import numpy as np

def mandelbrot\_set([xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xmax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [yn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [maxiter](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [horizon](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=2.0):
    X \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xmax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xn](https://docs.python.org/3/library/functions.html#int "builtins.int")
).astype([np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
)
    Y \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [yn](https://docs.python.org/3/library/functions.html#int "builtins.int")
).astype([np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
)
    C \= X + Y\[:, None\] \* 1j
    [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(C, dtype\=int)
    [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(C)
    for n in range([maxiter](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
        I \= abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) < [horizon](https://docs.python.org/3/library/functions.html#float "builtins.float")
        [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[I\] \= n
        [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[I\] \= [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[I\]\*\*2 + C\[I\]
    [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \== [maxiter](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\-1\] \= 0
    return [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

if \_\_name\_\_ \== '\_\_main\_\_':
    import time

    import matplotlib.pyplot as plt

    import matplotlib
    from matplotlib import colors

    [xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xmax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-2.25, +0.75, 3000 // 2
    [ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [yn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-1.25, +1.25, 2500 // 2
    [maxiter](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
    [horizon](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 2.0 \*\* 40
    [log\_horizon](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.log2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.log](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([horizon](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= mandelbrot\_set([xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xmax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ymax](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [xn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [yn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [maxiter](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [horizon](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

    \# Normalized recount as explained in:
    \# https://linas.org/art-gallery/escape/smooth.html
    \# https://web.archive.org/web/20160331171238/https://www.ibm.com/developerworks/community/blogs/jfp/entry/My\_Christmas\_Gift?lang=en

    \# This line will generate warnings for null values, but it is faster to
    \# process them afterwards using the nan\_to\_num
    with [np.errstate](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
(invalid\='ignore'):
        [M](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.nan\_to\_num](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#numpy.nan_to_num "numpy.nan_to_num")
([N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 1 \- [np.log2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.log](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))) + [log\_horizon](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)

    [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 72
    [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
    [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 10\*[yn](https://docs.python.org/3/library/functions.html#int "builtins.int")
/[xn](https://docs.python.org/3/library/functions.html#int "builtins.int")
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=([width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
), [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1), frameon\=False, aspect\=1)

    \# Shaded rendering
    [light](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
 \= [colors.LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(azdeg\=315, altdeg\=10)
    [M](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [light.shade](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "matplotlib.colors.LightSource.shade")
([M](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\=[plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["hot"\], vert\_exag\=1.5,
                    norm\=[colors.PowerNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
(0.3), blend\_mode\='hsv')
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([M](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, extent\=\[[xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [xmax](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [ymax](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], interpolation\="bicubic")
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[\])
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])

    \# Some advertisement for matplotlib
    [year](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [time.strftime](https://docs.python.org/3/library/time.html#time.strftime "time.strftime")
("%Y")
    [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= ("The Mandelbrot fractal set\\n"
            "Rendered with matplotlib %s, %s - https://matplotlib.org"
            % ([matplotlib.\_\_version\_\_](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [year](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([xmin](https://docs.python.org/3/library/functions.html#float "builtins.float")
+.025, [ymin](https://docs.python.org/3/library/functions.html#float "builtins.float")
+.025, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, color\="white", fontsize\=12, alpha\=0.5)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 6.029 seconds)

[`Download Jupyter notebook: mandelbrot.ipynb`](https://matplotlib.org/stable/_downloads/03a4ae19b81e22290c46a94bdf82cb9a/mandelbrot.ipynb)

[`Download Python source code: mandelbrot.py`](https://matplotlib.org/stable/_downloads/201501ef1714f6f71b3f2fe0dd7ddeae/mandelbrot.py)

[`Download zipped: mandelbrot.zip`](https://matplotlib.org/stable/_downloads/233613fce9ebb121ac42ee7597391103/mandelbrot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)