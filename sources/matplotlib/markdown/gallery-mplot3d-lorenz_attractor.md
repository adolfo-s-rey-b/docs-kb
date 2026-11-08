[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html#sphx-glr-download-gallery-mplot3d-lorenz-attractor-py)
 to download the full example code.

Lorenz attractor[#](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html#lorenz-attractor "Link to this heading")

=================================================================================================================================

This is an example of plotting Edward Lorenz's 1963 ["Deterministic Nonperiodic Flow"](https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml)
 in a 3-dimensional space using mplot3d.

Note

Because this is a simple non-linear ODE, it would be more easily done using SciPy's ODE solver, but this approach depends only upon NumPy.

import matplotlib.pyplot as plt
import numpy as np

def lorenz(xyz, \*, s\=10, r\=28, b\=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz\_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at \*xyz\*.
    """
    x, y, z \= xyz
    x\_dot \= s\*(y \- x)
    y\_dot \= r\*x \- y \- x\*z
    z\_dot \= x\*y \- b\*z
    return [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[x\_dot, y\_dot, z\_dot\])

[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.01
[num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10000

[xyzs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
(([num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1, 3))  \# Need one more for the initial values
[xyzs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\] \= (0., 1., 1.05)  \# Set initial values
\# Step through "time", calculating the partial derivatives at the current point
\# and using them to estimate the next point
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [xyzs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1\] \= [xyzs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] + lorenz([xyzs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]) \* [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")

\# Plot
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
(\*[xyzs.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=0.5)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("X Axis")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Y Axis")
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
("Z Axis")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.Axes3D.set_title")
("Lorenz Attractor")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Lorenz Attractor](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: lorenz_attractor.ipynb`](https://matplotlib.org/stable/_downloads/ec9373c2ddb27f908f3127e7805f9df0/lorenz_attractor.ipynb)

[`Download Python source code: lorenz_attractor.py`](https://matplotlib.org/stable/_downloads/7bcb50501dff2222c41e6dd71664c10f/lorenz_attractor.py)

[`Download zipped: lorenz_attractor.zip`](https://matplotlib.org/stable/_downloads/0537d9f845183123d518743d72366701/lorenz_attractor.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)