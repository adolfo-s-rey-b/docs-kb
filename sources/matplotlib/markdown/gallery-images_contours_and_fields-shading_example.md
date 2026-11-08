[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html#sphx-glr-download-gallery-images-contours-and-fields-shading-example-py)
 to download the full example code.

Shading example[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html#shading-example "Link to this heading")

=================================================================================================================================================

Example showing how to make shaded relief plots like [Mathematica](http://reference.wolfram.com/mathematica/ref/ReliefPlot.html)
 or [Generic Mapping Tools](https://www.generic-mapping-tools.org/)
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from matplotlib.colors import [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")

def main():
    \# Test data
    x, y \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-5:5:0.05, \-5:5:0.05\]
    z \= 5 \* ([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2 + y\*\*2) + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x\*\*2 + y\*\*2))

    dem \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('jacksboro\_fault\_dem.npz')
    elev \= dem\['elevation'\]

    fig \= compare(z, [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["copper"\])
    fig.suptitle('HSV Blending Looks Best with Smooth Surfaces', y\=0.95)

    fig \= compare(elev, [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["gist\_earth"\], ve\=0.05)
    fig.suptitle('Overlay Blending Looks Best with Rough Surfaces', y\=0.95)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

def compare(z, cmap, ve\=1):
    \# Create subplots and hide ticks
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, nrows\=2)
    for ax in axs.flat:
        ax.set(xticks\=\[\], yticks\=\[\])

    \# Illuminate the scene from the northwest
    ls \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(azdeg\=315, altdeg\=45)

    axs\[0, 0\].imshow(z, cmap\=cmap)
    axs\[0, 0\].set(xlabel\='Colormapped Data')

    axs\[0, 1\].imshow(ls.hillshade(z, vert\_exag\=ve), cmap\='gray')
    axs\[0, 1\].set(xlabel\='Illumination Intensity')

    rgb \= ls.shade(z, cmap\=cmap, vert\_exag\=ve, blend\_mode\='hsv')
    axs\[1, 0\].imshow(rgb)
    axs\[1, 0\].set(xlabel\='Blend Mode: "hsv" (default)')

    rgb \= ls.shade(z, cmap\=cmap, vert\_exag\=ve, blend\_mode\='overlay')
    axs\[1, 1\].imshow(rgb)
    axs\[1, 1\].set(xlabel\='Blend Mode: "overlay"')

    return fig

if \_\_name\_\_ \== '\_\_main\_\_':
    main()

*   ![HSV Blending Looks Best with Smooth Surfaces](https://matplotlib.org/stable/_images/sphx_glr_shading_example_001_2_00x.png)
*   ![Overlay Blending Looks Best with Rough Surfaces](https://matplotlib.org/stable/_images/sphx_glr_shading_example_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors.LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
    
*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    

**Total running time of the script:** (0 minutes 1.982 seconds)

[`Download Jupyter notebook: shading_example.ipynb`](https://matplotlib.org/stable/_downloads/9a566359e1ce3cd72d2f794ca1ad785a/shading_example.ipynb)

[`Download Python source code: shading_example.py`](https://matplotlib.org/stable/_downloads/51f72ac52a09ab1afd7282dc56b96fb3/shading_example.py)

[`Download zipped: shading_example.zip`](https://matplotlib.org/stable/_downloads/5874da281e15ac8fd62c91dd22af6fa5/shading_example.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)