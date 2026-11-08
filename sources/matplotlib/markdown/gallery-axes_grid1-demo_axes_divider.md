[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_divider.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_divider.html#sphx-glr-download-gallery-axes-grid1-demo-axes-divider-py)
 to download the full example code.

Axes divider[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_divider.html#axes-divider "Link to this heading")

=============================================================================================================================

Axes divider to calculate location of Axes and create a divider for them using existing Axes instances.

![demo axes divider](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_divider_001_2_00x.png)

import matplotlib.pyplot as plt

from matplotlib import cbook

def get\_demo\_image():
    z \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")  \# 15x15 array
    return z, (\-3, 4, \-4, 3)

def demo\_simple\_image(ax):
    Z, extent \= get\_demo\_image()

    im \= ax.imshow(Z, extent\=extent)
    cb \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(im)
    cb.ax.yaxis.set\_tick\_params(labelright\=False)

def demo\_locatable\_axes\_hard(fig):
    from mpl\_toolkits.axes\_grid1 import Size, SubplotDivider

    divider \= SubplotDivider(fig, 2, 2, 2, aspect\=True)

    \# Axes for image
    ax \= fig.add\_subplot(axes\_locator\=divider.new\_locator(nx\=0, ny\=0))
    \# Axes for colorbar
    ax\_cb \= fig.add\_subplot(axes\_locator\=divider.new\_locator(nx\=2, ny\=0))

    divider.set\_horizontal(\[\
        Size.AxesX(ax),  \# main Axes\
        Size.Fixed(0.05),  \# padding, 0.1 inch\
        Size.Fixed(0.2),  \# colorbar, 0.3 inch\
    \])
    divider.set\_vertical(\[Size.AxesY(ax)\])

    Z, extent \= get\_demo\_image()

    im \= ax.imshow(Z, extent\=extent)
    [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(im, cax\=ax\_cb)
    ax\_cb.yaxis.set\_tick\_params(labelright\=False)

def demo\_locatable\_axes\_easy(ax):
    from mpl\_toolkits.axes\_grid1 import [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")

    divider \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
(ax)

    ax\_cb \= divider.append\_axes("right", size\="5%", pad\=0.05)
    fig \= ax.get\_figure()
    fig.add\_axes(ax\_cb)

    Z, extent \= get\_demo\_image()
    im \= ax.imshow(Z, extent\=extent)

    [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(im, cax\=ax\_cb)
    ax\_cb.yaxis.tick\_right()
    ax\_cb.yaxis.set\_tick\_params(labelright\=False)

def demo\_images\_side\_by\_side(ax):
    from mpl\_toolkits.axes\_grid1 import [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")

    divider \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
(ax)

    Z, extent \= get\_demo\_image()
    ax2 \= divider.append\_axes("right", size\="100%", pad\=0.05)
    fig1 \= ax.get\_figure()
    fig1.add\_axes(ax2)

    ax.imshow(Z, extent\=extent)
    ax2.imshow(Z, extent\=extent)
    ax2.yaxis.set\_tick\_params(labelleft\=False)

def demo():
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))

    \# PLOT 1
    \# simple image & colorbar
    ax \= fig.add\_subplot(2, 2, 1)
    demo\_simple\_image(ax)

    \# PLOT 2
    \# image and colorbar with draw-time positioning -- a hard way
    demo\_locatable\_axes\_hard(fig)

    \# PLOT 3
    \# image and colorbar with draw-time positioning -- an easy way
    ax \= fig.add\_subplot(2, 2, 3)
    demo\_locatable\_axes\_easy(ax)

    \# PLOT 4
    \# two images side by side with fixed padding.
    ax \= fig.add\_subplot(2, 2, 4)
    demo\_images\_side\_by\_side(ax)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

demo()

[`Download Jupyter notebook: demo_axes_divider.ipynb`](https://matplotlib.org/stable/_downloads/28d949c0d06f2ed62eb1d10112c36bc5/demo_axes_divider.ipynb)

[`Download Python source code: demo_axes_divider.py`](https://matplotlib.org/stable/_downloads/52e9d9c67d12b0707ec2ebfda10937f5/demo_axes_divider.py)

[`Download zipped: demo_axes_divider.zip`](https://matplotlib.org/stable/_downloads/5e2cd26138680564e2aac4c749270532/demo_axes_divider.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)