[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html#sphx-glr-download-gallery-specialty-plots-sankey-rankine-py)
 to download the full example code.

Rankine power cycle[#](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html#rankine-power-cycle "Link to this heading")

=============================================================================================================================================

Demonstrate the Sankey class with a practical example of a Rankine power cycle.

import matplotlib.pyplot as plt

from matplotlib.sankey import [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 9))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 1, 1, xticks\=\[\], yticks\=\[\],
                     title\="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\\n\\x22Fundamentals of Engineering Thermodynamics "
                     "\\x22, 6th ed., 2008")
[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[260.431, 35.078, 180.794, 221.115, 22.700,\
        142.361, 10.193, 10.210, 43.670, 44.312,\
        68.631, 10.758, 10.758, 0.017, 0.642,\
        232.121, 44.559, 100.613, 132.168\]  \# MW
[sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 \= [Sankey](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, format\='%.3G', unit\=' MW', gap\=0.5, scale\=1.0/[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\])
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='\\n\\nPump 1', rotation\=90, facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[13\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[6\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[7\]\],
           labels\=\['Shaft power', '', None\],
           pathlengths\=\[0.4, 0.883, 0.25\],
           orientations\=\[1, \-1, 0\])
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='\\n\\nOpen\\nheater', facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[11\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[7\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[4\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[8\]\],
           labels\=\[None, '', None, None\],
           pathlengths\=\[0.25, 0.25, 1.93, 0.25\],
           orientations\=\[1, 0, \-1, 0\], prior\=0, connect\=(2, 1))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='\\n\\nPump 2', facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[14\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[8\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[9\]\],
           labels\=\['Shaft power', '', None\],
           pathlengths\=\[0.4, 0.25, 0.25\],
           orientations\=\[1, 0, 0\], prior\=1, connect\=(3, 1))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='Closed\\nheater', trunklength\=2.914, fc\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[9\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[1\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[11\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[10\]\],
           pathlengths\=\[0.25, 1.543, 0.25, 0.25\],
           labels\=\['', '', None, None\],
           orientations\=\[0, \-1, 1, \-1\], prior\=2, connect\=(2, 0))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='Trap', facecolor\='#37c959', trunklength\=5.102,
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[11\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[12\]\],
           labels\=\['\\n', None\],
           pathlengths\=\[1.0, 1.01\],
           orientations\=\[1, 1\], prior\=3, connect\=(2, 0))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='Steam\\ngenerator', facecolor\='#ff5555',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[15\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[10\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[2\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[3\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[0\]\],
           labels\=\['Heat rate', '', '', None, None\],
           pathlengths\=0.25,
           orientations\=\[1, 0, \-1, \-1, \-1\], prior\=3, connect\=(3, 1))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='\\n\\n\\nTurbine 1', facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[0\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[16\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[1\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[2\]\],
           labels\=\['', None, None, None\],
           pathlengths\=\[0.25, 0.153, 1.543, 0.25\],
           orientations\=\[0, 1, \-1, \-1\], prior\=5, connect\=(4, 0))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='\\n\\n\\nReheat', facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[2\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[2\]\],
           labels\=\[None, None\],
           pathlengths\=\[0.725, 0.25\],
           orientations\=\[\-1, 0\], prior\=6, connect\=(3, 0))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='Turbine 2', trunklength\=3.212, facecolor\='#37c959',
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[3\], [Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[16\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[5\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[4\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[17\]\],
           labels\=\[None, 'Shaft power', None, '', 'Shaft power'\],
           pathlengths\=\[0.751, 0.15, 0.25, 1.93, 0.25\],
           orientations\=\[0, \-1, 0, \-1, 1\], prior\=6, connect\=(1, 1))
[sankey.add](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
(patchlabel\='Condenser', facecolor\='#58b1fa', trunklength\=1.764,
           flows\=\[[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[5\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[18\], \-[Hdot](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[6\]\],
           labels\=\['', 'Heat rate', None\],
           pathlengths\=\[0.45, 0.25, 0.883\],
           orientations\=\[\-1, 1, 0\], prior\=8, connect\=(2, 0))
[diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [sankey.finish](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
()
for [diagram](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace")
 in [diagrams](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [diagram.text.set\_fontweight](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")
('bold')
    [diagram.text.set\_fontsize](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")
('10')
    for [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in [diagram.texts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
        [text.set\_fontsize](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")
('10')
\# Notice that the explicit connections are handled automatically, but the
\# implicit ones currently are not.  The lengths of the paths and the trunks
\# must be adjusted manually, and that is a bit tricky.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Rankine Power Cycle: Example 8.6 from Moran and Shapiro ](https://matplotlib.org/stable/_images/sphx_glr_sankey_rankine_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.sankey`](https://matplotlib.org/stable/api/sankey_api.html#module-matplotlib.sankey "matplotlib.sankey")
    
*   [`matplotlib.sankey.Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
    
*   [`matplotlib.sankey.Sankey.add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
    
*   [`matplotlib.sankey.Sankey.finish`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")
    

**Total running time of the script:** (0 minutes 1.443 seconds)

[`Download Jupyter notebook: sankey_rankine.ipynb`](https://matplotlib.org/stable/_downloads/ec177c0ffe33a3b8c03401dda4e0cf8c/sankey_rankine.ipynb)

[`Download Python source code: sankey_rankine.py`](https://matplotlib.org/stable/_downloads/2e9a7fa3acabe04307104bb0222f2f30/sankey_rankine.py)

[`Download zipped: sankey_rankine.zip`](https://matplotlib.org/stable/_downloads/529cb146764a5cb69a79615670bcbadd/sankey_rankine.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)