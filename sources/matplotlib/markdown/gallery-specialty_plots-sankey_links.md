[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/sankey_links.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/sankey_links.html#sphx-glr-download-gallery-specialty-plots-sankey-links-py)
 to download the full example code.

Long chain of connections using Sankey[#](https://matplotlib.org/stable/gallery/specialty_plots/sankey_links.html#long-chain-of-connections-using-sankey "Link to this heading")

=================================================================================================================================================================================

Demonstrate/test the Sankey class by producing a long chain of connections.

import matplotlib.pyplot as plt

from matplotlib.sankey import [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")

[links\_per\_side](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 6

def side([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
, n\=1):
    """Generate a side chain."""
    prior \= len([sankey.diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    for i in range(0, 2\*n, 2):
        [sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(flows\=\[1, \-1\], orientations\=\[\-1, \-1\],
                   patchlabel\=str(prior + i),
                   prior\=prior + i \- 1, connect\=(1, 0), alpha\=0.5)
        [sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(flows\=\[1, \-1\], orientations\=\[1, 1\],
                   patchlabel\=str(prior + i + 1),
                   prior\=prior + i, connect\=(1, 0), alpha\=0.5)

def corner([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
):
    """Generate a corner link."""
    prior \= len([sankey.diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    [sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(flows\=\[1, \-1\], orientations\=\[0, 1\],
               patchlabel\=str(prior), facecolor\='k',
               prior\=prior \- 1, connect\=(1, 0), alpha\=0.5)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 1, 1, xticks\=\[\], yticks\=\[\],
                     title\="Why would you want to do this?\\n(But you could.)")
[sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 \= [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, unit\=None)
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(flows\=\[1, \-1\], orientations\=\[0, 1\],
           patchlabel\="0", facecolor\='k',
           rotation\=45)
side([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
, n\=[links\_per\_side](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
corner([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
)
side([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
, n\=[links\_per\_side](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
corner([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
)
side([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
, n\=[links\_per\_side](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
corner([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
)
side([sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
, n\=[links\_per\_side](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[sankey.finish](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
()
\# Notice:
\# 1. The alignment doesn't drift significantly (if at all; with 16007
\#    subdiagrams there is still closure).
\# 2. The first diagram is rotated 45 deg, so all other diagrams are rotated
\#    accordingly.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Why would you want to do this? (But you could.)](https://matplotlib.org/stable/_images/sphx_glr_sankey_links_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.sankey`](https://matplotlib.org/stable/api/sankey_api.html#module-matplotlib.sankey "matplotlib.sankey")
    
*   [`matplotlib.sankey.Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
    
*   [`matplotlib.sankey.Sankey.add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
    
*   [`matplotlib.sankey.Sankey.finish`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
    

**Total running time of the script:** (0 minutes 1.096 seconds)

[`Download Jupyter notebook: sankey_links.ipynb`](https://matplotlib.org/stable/_downloads/611003c013aae53e504fe12335dbbd54/sankey_links.ipynb)

[`Download Python source code: sankey_links.py`](https://matplotlib.org/stable/_downloads/a373108b373a2ec7450403e183dc3c5d/sankey_links.py)

[`Download zipped: sankey_links.zip`](https://matplotlib.org/stable/_downloads/0b4703f05e7035d4b75d68b0503dea2a/sankey_links.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)