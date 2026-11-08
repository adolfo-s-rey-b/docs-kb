[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html#sphx-glr-download-gallery-event-handling-ginput-manual-clabel-sgskip-py)
 to download the full example code.

Interactive functions[#](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html#interactive-functions "Link to this heading")

=============================================================================================================================================================

This provides examples of uses of interactive functions, such as ginput, waitforbuttonpress and manual clabel placement.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

import time

import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(s, fontsize\=16)
    [plt.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw "matplotlib.pyplot.draw")
()

Define a triangle by clicking three points

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 1)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(0, 1)

tellme('You will define a triangle, click to begin')

[plt.waitforbuttonpress](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress "matplotlib.pyplot.waitforbuttonpress")
()

while True:
    pts \= \[\]
    while len(pts) < 3:
        tellme('Select 3 corners with mouse')
        pts \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([plt.ginput](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput "matplotlib.pyplot.ginput")
(3, timeout\=-1))
        if len(pts) < 3:
            tellme('Too few points, starting over')
            [time.sleep](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
(1)  \# Wait a second

    ph \= [plt.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill "matplotlib.pyplot.fill")
(pts\[:, 0\], pts\[:, 1\], 'r', lw\=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if [plt.waitforbuttonpress](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress "matplotlib.pyplot.waitforbuttonpress")
():
        break

    \# Get rid of fill
    for p in ph:
        p.remove()

Now contour according to distance from triangle corners - just an example

\# Define a nice function of distance from individual pts
def f(x, y, pts):
    z \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(x)
    for p in pts:
        z \= z + 1/([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
((x \- p\[0\])\*\*2 + (y \- p\[1\])\*\*2))
    return 1/z

X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, 51), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, 51))
Z \= f(X, Y, pts)

CS \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(X, Y, Z, 20)

tellme('Use mouse to select contour label locations, middle button to finish')
CL \= [plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(CS, manual\=True)

Now do a zoom

tellme('Now do a nested zoom, click to begin')
[plt.waitforbuttonpress](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress "matplotlib.pyplot.waitforbuttonpress")
()

while True:
    tellme('Select two corners of zoom, middle mouse button to finish')
    pts \= [plt.ginput](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput "matplotlib.pyplot.ginput")
(2, timeout\=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) \= pts
    xmin, xmax \= sorted(\[x0, x1\])
    ymin, ymax \= sorted(\[y0, y1\])
    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(xmin, xmax)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(ymin, ymax)

tellme('All Done!')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: ginput_manual_clabel_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/56e05f68b79dabcbe43a0ff2f68e69c5/ginput_manual_clabel_sgskip.ipynb)

[`Download Python source code: ginput_manual_clabel_sgskip.py`](https://matplotlib.org/stable/_downloads/784e624667ea437932f1b7daca5c5e2f/ginput_manual_clabel_sgskip.py)

[`Download zipped: ginput_manual_clabel_sgskip.zip`](https://matplotlib.org/stable/_downloads/161b6c78de77756d03e8ff78af767e17/ginput_manual_clabel_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)