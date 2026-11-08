[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/text3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/text3d.html#sphx-glr-download-gallery-mplot3d-text3d-py)
 to download the full example code.

Text annotations in 3D[#](https://matplotlib.org/stable/gallery/mplot3d/text3d.html#text-annotations-in-3d "Link to this heading")

===================================================================================================================================

Demonstrates the placement of text annotations on a 3D plot.

Functionality shown:

*   Using the [`text`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.axes3d.Axes3D.text")
     function with three types of _zdir_ values: None, an axis name (ex. 'x'), or a direction tuple (ex. (1, 1, 0)).
    
*   Using the [`text`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.axes3d.Axes3D.text")
     function with the color keyword.
    
*   Using the [`text2D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text2D "mpl_toolkits.mplot3d.axes3d.Axes3D.text2D")
     function to place text on a fixed position on the ax object.
    

import matplotlib.pyplot as plt

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

\# Demo 1: zdir
[zdirs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
[xs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (1, 4, 4, 9, 4, 1)
[ys](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (2, 5, 8, 10, 1, 2)
[zs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (10, 3, 8, 9, 1, 8)

for [zdir](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [z](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in zip([zdirs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [xs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ys](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [zs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '(%d, %d, %d), dir=%s' % ([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [z](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [zdir](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.Axes3D.text")
([x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [z](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [zdir](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

\# Demo 2: color
[ax.text](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.Axes3D.text")
(9, 0, 0, "red", color\='red')

\# Demo 3: text2D
\# Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
[ax.text2D](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text2D "mpl_toolkits.mplot3d.Axes3D.text2D")
(0.05, 0.95, "2D Text", transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

\# Tweaking display region and labels
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.Axes3D.set_xlim")
(0, 10)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.Axes3D.set_ylim")
(0, 10)
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(0, 10)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X axis')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Y axis')
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
('Z axis')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![text3d](https://matplotlib.org/stable/_images/sphx_glr_text3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: text3d.ipynb`](https://matplotlib.org/stable/_downloads/2ff24e32e325e455d65a638a75d1a2ab/text3d.ipynb)

[`Download Python source code: text3d.py`](https://matplotlib.org/stable/_downloads/562145a7614d88838c0b771963e376b3/text3d.py)

[`Download zipped: text3d.zip`](https://matplotlib.org/stable/_downloads/140b9ee6e9bd774edba93c6173fc6aa6/text3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)