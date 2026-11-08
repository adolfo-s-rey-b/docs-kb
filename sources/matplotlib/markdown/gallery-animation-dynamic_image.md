[Skip to main content](https://matplotlib.org/stable/gallery/animation/dynamic_image.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/dynamic_image.html#sphx-glr-download-gallery-animation-dynamic-image-py)
 to download the full example code.

Animated image using a precomputed list of images[#](https://matplotlib.org/stable/gallery/animation/dynamic_image.html#animated-image-using-a-precomputed-list-of-images "Link to this heading")

==================================================================================================================================================================================================

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

def f([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    return [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 120)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 100).reshape(\-1, 1)

\# ims is a list of lists, each row is a list of artists to draw in the
\# current frame; here we are just animating one artist, the image, in
\# each frame
[ims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(60):
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 15
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 30
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(f([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), animated\=True)
    if [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 0:
        [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(f([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))  \# show an initial one first
    [ims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append(\[[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")\
\])

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 \= [animation.ArtistAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, interval\=50, blit\=True,
                                repeat\_delay\=1000)

\# To save the animation, use e.g.
#
\# ani.save("movie.mp4")
#
\# or
#
\# writer = animation.FFMpegWriter(
\#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
\# ani.save("movie.mp4", writer=writer)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)

**Total running time of the script:** (0 minutes 17.026 seconds)

[`Download Jupyter notebook: dynamic_image.ipynb`](https://matplotlib.org/stable/_downloads/85eea2a9b9c6a3a221733494325998c8/dynamic_image.ipynb)

[`Download Python source code: dynamic_image.py`](https://matplotlib.org/stable/_downloads/c71a756999a5cacfd767880b3f5f5a19/dynamic_image.py)

[`Download zipped: dynamic_image.zip`](https://matplotlib.org/stable/_downloads/b93088c34d52404e4014467b356fb4f1/dynamic_image.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)