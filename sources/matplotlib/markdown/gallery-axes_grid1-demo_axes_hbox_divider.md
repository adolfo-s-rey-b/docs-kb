[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html#sphx-glr-download-gallery-axes-grid1-demo-axes-hbox-divider-py)
 to download the full example code.

HBoxDivider and VBoxDivider demo[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html#hboxdivider-and-vboxdivider-demo "Link to this heading")

==========================================================================================================================================================================

Using an [`HBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "mpl_toolkits.axes_grid1.axes_divider.HBoxDivider")
 to arrange subplots.

Note that both Axes' location are adjusted so that they have equal heights while maintaining their aspect ratios.

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.axes\_grid1.axes\_divider import [HBoxDivider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "mpl_toolkits.axes_grid1.axes_divider.HBoxDivider")
, [VBoxDivider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
import mpl\_toolkits.axes\_grid1.axes\_size as Size

[arr1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(20).reshape((4, 5))
[arr2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(20).reshape((5, 4))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
[ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[pad](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.5  \# pad in inches
[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
 \= [HBoxDivider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "mpl_toolkits.axes_grid1.axes_divider.HBoxDivider")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 111,
    horizontal\=\[[Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
([pad](https://docs.python.org/3/library/functions.html#float "builtins.float")\
), [Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
)\],
    vertical\=\[[Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1), [Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
)\])
[ax1.set\_axes\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator")
([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator")
(0))
[ax2.set\_axes\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator")
([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator")
(2))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo axes hbox divider](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_001_2_00x.png)

Using a [`VBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
 to arrange subplots.

Note that both Axes' location are adjusted so that they have equal widths while maintaining their aspect ratios.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1)
[ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
 \= [VBoxDivider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 111,
    horizontal\=\[[Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1), [Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
)\],
    vertical\=\[[Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
([pad](https://docs.python.org/3/library/functions.html#float "builtins.float")\
), [Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
)\])

[ax1.set\_axes\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator")
([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator")
(0))
[ax2.set\_axes\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator")
([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator")
(2))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo axes hbox divider](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_002_2_00x.png)

[`Download Jupyter notebook: demo_axes_hbox_divider.ipynb`](https://matplotlib.org/stable/_downloads/d43f7abc86ae3d0af10ddabd4317f06b/demo_axes_hbox_divider.ipynb)

[`Download Python source code: demo_axes_hbox_divider.py`](https://matplotlib.org/stable/_downloads/d068f88cea39314c1b79c61e63f18720/demo_axes_hbox_divider.py)

[`Download zipped: demo_axes_hbox_divider.zip`](https://matplotlib.org/stable/_downloads/9739909e095a30b43ae23ebb62aef816/demo_axes_hbox_divider.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)