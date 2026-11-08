[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/view_planes_3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/view_planes_3d.html#sphx-glr-download-gallery-mplot3d-view-planes-3d-py)
 to download the full example code.

Primary 3D view planes[#](https://matplotlib.org/stable/gallery/mplot3d/view_planes_3d.html#primary-3d-view-planes "Link to this heading")

===========================================================================================================================================

This example generates an "unfolded" 3D plot that shows each of the primary 3D view planes. The elevation, azimuth, and roll angles required for each view are labeled. You could print out this image and fold it into a box where each plane forms a side of the box.

import matplotlib.pyplot as plt

def annotate\_axes(ax, text, fontsize\=18):
    ax.text(x\=0.5, y\=0.5, z\=0.5, s\=text,
            va\="center", ha\="center", fontsize\=fontsize, color\="black")

\# (plane, (elev, azim, roll))
[views](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[('XY',   (90, \-90, 0)),\
         ('XZ',    (0, \-90, 0)),\
         ('YZ',    (0,   0, 0)),\
         ('-XY', (\-90,  90, 0)),\
         ('-XZ',   (0,  90, 0)),\
         ('-YZ',   (0, 180, 0))\]

[layout](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\['XY',  '.',   'L',   '.'\],\
          \['XZ', 'YZ', '-XZ', '-YZ'\],\
          \['.',   '.', '-XY',   '.'\]\]
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
([layout](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, subplot\_kw\={'projection': '3d'},
                              figsize\=(12, 8.5))
for [plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [angles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in [views](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_xlabel('x')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_ylabel('y')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_zlabel('z')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_proj\_type('ortho')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].view\_init(elev\=[angles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], azim\=[angles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], roll\=[angles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[2\])
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_box\_aspect(None, zoom\=1.25)

    [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f'{[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}\\n{[angles](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
}'
    annotate\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\], [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\=14)

for [plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('XY', '-XY'):
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_zticklabels(\[\])
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_zlabel('')
for [plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('XZ', '-XZ'):
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_yticklabels(\[\])
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_ylabel('')
for [plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('YZ', '-YZ'):
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_xticklabels(\[\])
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[plane](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_xlabel('')

[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'mplot3d primary view planes\\n' + 'ax.view\_init(elev, azim, roll)'
annotate\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['L'\], [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\=18)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['L'\].set\_axis\_off()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![view planes 3d](https://matplotlib.org/stable/_images/sphx_glr_view_planes_3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.394 seconds)

[`Download Jupyter notebook: view_planes_3d.ipynb`](https://matplotlib.org/stable/_downloads/0f14cc81759ad6dd9752fa40522abf1b/view_planes_3d.ipynb)

[`Download Python source code: view_planes_3d.py`](https://matplotlib.org/stable/_downloads/9184f11a80de896a620b8b82acb59c17/view_planes_3d.py)

[`Download zipped: view_planes_3d.zip`](https://matplotlib.org/stable/_downloads/09bb0322b8be50f2865dd76fc1ad69d8/view_planes_3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)