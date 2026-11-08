[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#sphx-glr-download-gallery-subplots-axes-and-figures-figure-size-units-py)
 to download the full example code.

Figure size in different units[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#figure-size-in-different-units "Link to this heading")

================================================================================================================================================================================

The native figure size unit in Matplotlib is inches, deriving from print industry standards. However, users may need to specify their figures in other units like centimeters or pixels. This example illustrates how to do this efficiently.

import matplotlib.pyplot as plt

[text\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(ha\='center', va\='center', fontsize\=28, color\='C1')

Figure size in inches (default)[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#figure-size-in-inches-default "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 2))
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.5, 0.5, '6 inches x 2 inches', \*\*[text\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![figure size units](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_001_2_00x.png)

Figure size in centimeter[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#figure-size-in-centimeter "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Multiplying centimeter-based numbers with a conversion factor from cm to inches, gives the right numbers. Naming the conversion factor `cm` makes the conversion almost look like appending a unit to the number, which is nicely readable.

[cm](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1/2.54  \# centimeters in inches
[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(15\*[cm](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 5\*[cm](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.5, 0.5, '15cm x 5cm', \*\*[text\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![figure size units](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_002_2_00x.png)

Figure size in pixel[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#figure-size-in-pixel "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Similarly, one can use a conversion from pixels.

Note that you could break this if you use [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 with a different explicit dpi value.

[px](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1/[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.dpi'\]  \# pixel in inches
[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(600\*[px](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 200\*[px](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.5, 0.5, '600px x 200px', \*\*[text\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![figure size units](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_003_2_00x.png)

Quick interactive work is usually rendered to the screen, making pixels a good size of unit. But defining the conversion factor may feel a little tedious for quick iterations.

Because of the default `rcParams['figure.dpi'] = 100`, one can mentally divide the needed pixel value by 100 [\[1\]](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#id2)
:

[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 2))
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.5, 0.5, '600px x 200px', \*\*[text\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![figure size units](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_004_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
    
*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    
*   [`matplotlib.pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
    

Tags: [component: figure](https://matplotlib.org/stable/_tags/component-figure.html)
 [styling: size](https://matplotlib.org/stable/_tags/styling-size.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: figure_size_units.ipynb`](https://matplotlib.org/stable/_downloads/2b8a8458d23f0c7e2ab390a23d1a02d7/figure_size_units.ipynb)

[`Download Python source code: figure_size_units.py`](https://matplotlib.org/stable/_downloads/69acc8b9ce1af724427c3422182b1194/figure_size_units.py)

[`Download zipped: figure_size_units.zip`](https://matplotlib.org/stable/_downloads/d6d30208a962b9d6a65b82db0653cca6/figure_size_units.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page