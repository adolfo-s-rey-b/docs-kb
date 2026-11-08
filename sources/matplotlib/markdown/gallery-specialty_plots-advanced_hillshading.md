[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html#sphx-glr-download-gallery-specialty-plots-advanced-hillshading-py)
 to download the full example code.

Hillshading[#](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html#hillshading "Link to this heading")

===================================================================================================================================

Demonstrates a few common tricks with shaded plots.

*   ![Using a colorbar with a shaded plot](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_001_2_00x.png)
*   ![Avoiding Outliers in Shaded Plots, Full range of data, Manually set range](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_002_2_00x.png)
*   ![Shade by one variable, color by another](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_003_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

def display\_colorbar():
    """Display a correct numeric colorbar for a shaded plot."""
    y, x \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-4:2:200j, \-4:2:200j\]
    z \= 10 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2 + y\*\*2)

    cmap \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["copper"\]
    ls \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(315, 45)
    rgb \= ls.shade(z, cmap)

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    ax.imshow(rgb, interpolation\='bilinear')

    \# Use a proxy artist for the colorbar...
    im \= ax.imshow(z, cmap\=cmap)
    im.remove()
    fig.colorbar(im, ax\=ax)

    ax.set\_title('Using a colorbar with a shaded plot', size\='x-large')

def avoid\_outliers():
    """Use a custom norm to control the displayed z-range of a shaded plot."""
    y, x \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-4:2:200j, \-4:2:200j\]
    z \= 10 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2 + y\*\*2)

    \# Add some outliers...
    z\[100, 105\] \= 2000
    z\[120, 110\] \= \-9000

    ls \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(315, 45)
    fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(8, 4.5))

    rgb \= ls.shade(z, [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["copper"\])
    ax1.imshow(rgb, interpolation\='bilinear')
    ax1.set\_title('Full range of data')

    rgb \= ls.shade(z, [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["copper"\], vmin\=-10, vmax\=10)
    ax2.imshow(rgb, interpolation\='bilinear')
    ax2.set\_title('Manually set range')

    fig.suptitle('Avoiding Outliers in Shaded Plots', size\='x-large')

def shade\_other\_data():
    """Demonstrates displaying different variables through shade and color."""
    y, x \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-4:2:200j, \-4:2:200j\]
    z1 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2)  \# Data to hillshade
    z2 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2 + y\*\*2)  \# Data to color

    norm \= [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(z2.min(), z2.max())
    cmap \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["RdBu"\]

    ls \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(315, 45)
    rgb \= ls.shade\_rgb(cmap(norm(z2)), z1)

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    ax.imshow(rgb, interpolation\='bilinear')
    ax.set\_title('Shade by one variable, color by another', size\='x-large')

display\_colorbar()
avoid\_outliers()
shade\_other\_data()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 3.457 seconds)

[`Download Jupyter notebook: advanced_hillshading.ipynb`](https://matplotlib.org/stable/_downloads/e10d91c58039c201a3fcf218a3658b87/advanced_hillshading.ipynb)

[`Download Python source code: advanced_hillshading.py`](https://matplotlib.org/stable/_downloads/68782730e51de44d2fae945e9e89a387/advanced_hillshading.py)

[`Download zipped: advanced_hillshading.zip`](https://matplotlib.org/stable/_downloads/87297c03952df18dd30ab11829bb556b/advanced_hillshading.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)