[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html#sphx-glr-download-gallery-specialty-plots-sankey-basics-py)
 to download the full example code.

The Sankey class[#](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html#the-sankey-class "Link to this heading")

======================================================================================================================================

Demonstrate the Sankey class by producing three basic diagrams.

import matplotlib.pyplot as plt

from matplotlib.sankey import [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")

Example 1 -- Mostly defaults

This demonstrates how to create a simple diagram by implicitly calling the Sankey.add() method and by appending finish() to the call to the class.

[Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
([flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[0.25, 0.15, 0.60, \-0.20, \-0.15, \-0.05, \-0.50, \-0.10\],
       labels\=\['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'\],
       orientations\=\[\-1, 1, 0, 1, 1, 1, 0, \-1\]).finish()
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("The default settings produce a diagram like this.")

![The default settings produce a diagram like this.](https://matplotlib.org/stable/_images/sphx_glr_sankey_basics_001_2_00x.png)

Notice:

1.  Axes weren't provided when Sankey() was instantiated, so they were created automatically.
    
2.  The scale argument wasn't necessary since the data was already normalized.
    
3.  By default, the lengths of the paths are justified.
    

Example 2

This demonstrates:

1.  Setting one path longer than the others
    
2.  Placing a label in the middle of the diagram
    
3.  Using the scale argument to normalize the flows
    
4.  Implicitly passing keyword arguments to PathPatch()
    
5.  Changing the angle of the arrow heads
    
6.  Changing the offset between the tips of the paths and their labels
    
7.  Formatting the numbers in the path labels and the associated unit
    
8.  Changing the appearance of the patch and the labels after the figure is created
    

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 1, 1, xticks\=\[\], yticks\=\[\],
                     title\="Flow Diagram of a Widget")
[sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 \= [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, scale\=0.01, offset\=0.2, head\_angle\=180,
                format\='%.0f', unit\='%')
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
([flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[25, 0, 60, \-10, \-20, \-5, \-15, \-10, \-40\],
           labels\=\['', '', '', 'First', 'Second', 'Third', 'Fourth',\
                   'Fifth', 'Hurray!'\],
           orientations\=\[\-1, 1, 0, 1, 1, 1, \-1, \-1, 0\],
           pathlengths\=\[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,\
                        0.25\],
           patchlabel\="Widget\\nA")  \# Arguments to matplotlib.patches.PathPatch
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [sankey.finish](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
()
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].texts\[\-1\].set\_color('r')
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].text.set\_fontweight('bold')

![Flow Diagram of a Widget](https://matplotlib.org/stable/_images/sphx_glr_sankey_basics_002_2_00x.png)

Notice:

1.  Since the sum of the flows is nonzero, the width of the trunk isn't uniform. The matplotlib logging system logs this at the DEBUG level.
    
2.  The second flow doesn't appear because its value is zero. Again, this is logged at the DEBUG level.
    

Example 3

This demonstrates:

1.  Connecting two systems
    
2.  Turning off the labels of the quantities
    
3.  Adding a legend
    

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 1, 1, xticks\=\[\], yticks\=\[\], title\="Two Systems")
[flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.25, 0.15, 0.60, \-0.10, \-0.05, \-0.25, \-0.15, \-0.10, \-0.35\]
[sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 \= [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, unit\=None)
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
([flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\='one',
           orientations\=\[\-1, 1, 0, 1, 1, 1, \-1, \-1, 0\])
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
([flows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[\-0.25, 0.15, 0.1\], label\='two',
           orientations\=\[\-1, \-1, \-1\], prior\=0, connect\=(0, 0))
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [sankey.finish](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
()
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1\].patch.set\_hatch('/')
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()

![Two Systems](https://matplotlib.org/stable/_images/sphx_glr_sankey_basics_003_2_00x.png)

Notice that only one connection is specified, but the systems form a circuit since: (1) the lengths of the paths are justified and (2) the orientation and ordering of the flows is mirrored.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.sankey`](https://matplotlib.org/stable/api/sankey_api.html#module-matplotlib.sankey "matplotlib.sankey")
    
*   [`matplotlib.sankey.Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
    
*   [`matplotlib.sankey.Sankey.add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
    
*   [`matplotlib.sankey.Sankey.finish`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
    

**Total running time of the script:** (0 minutes 1.432 seconds)

[`Download Jupyter notebook: sankey_basics.ipynb`](https://matplotlib.org/stable/_downloads/15cb8e7f3f9a4cf5db016c0f7c09e9a4/sankey_basics.ipynb)

[`Download Python source code: sankey_basics.py`](https://matplotlib.org/stable/_downloads/e7ecb4f6799167cf0409edff13ddb823/sankey_basics.py)

[`Download zipped: sankey_basics.zip`](https://matplotlib.org/stable/_downloads/b942a2221f7bd1616ce97dd1f07a798c/sankey_basics.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)