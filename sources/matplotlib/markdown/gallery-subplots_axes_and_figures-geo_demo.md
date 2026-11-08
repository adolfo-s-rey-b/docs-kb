[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#sphx-glr-download-gallery-subplots-axes-and-figures-geo-demo-py)
 to download the full example code.

Geographic Projections[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#geographic-projections "Link to this heading")

=======================================================================================================================================================

This shows 4 possible geographic projections. [Cartopy](https://cartopy.readthedocs.io/)
 supports more projections.

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(projection\="aitoff")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Aitoff")
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

![Aitoff](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_001_2_00x.png)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(projection\="hammer")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Hammer")
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

![Hammer](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_002_2_00x.png)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(projection\="lambert")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Lambert")
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

![Lambert](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_003_2_00x.png)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(projection\="mollweide")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Mollweide")
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Mollweide](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_004_2_00x.png)

Tags: [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [component: projection](https://matplotlib.org/stable/_tags/component-projection.html)
 [domain: cartography](https://matplotlib.org/stable/_tags/domain-cartography.html)

**Total running time of the script:** (0 minutes 1.537 seconds)

[`Download Jupyter notebook: geo_demo.ipynb`](https://matplotlib.org/stable/_downloads/333307aae380f8ba98a2136aa2d0aa2a/geo_demo.ipynb)

[`Download Python source code: geo_demo.py`](https://matplotlib.org/stable/_downloads/4fc64c4adf40fca6c0f00c65a4d84e3f/geo_demo.py)

[`Download zipped: geo_demo.zip`](https://matplotlib.org/stable/_downloads/25bb1071d00c5b8eb82dc50a01da07d7/geo_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)