[Skip to main content](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html#sphx-glr-download-gallery-misc-svg-filter-line-py)
 to download the full example code.

Apply SVG filter to a line[#](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html#apply-svg-filter-to-a-line "Link to this heading")

=================================================================================================================================================

Demonstrate SVG filtering effects which might be used with Matplotlib.

Note that the filtering effects are only effective if your SVG renderer support it.

![svg filter line](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_001_2_00x.png)

Saving 'svg\_filter\_line.svg'

  

import io
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt

import matplotlib.transforms as mtransforms

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig1.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.1, 0.8, 0.8))

\# draw lines
[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0.1, 0.5, 0.9\], \[0.1, 0.9, 0.5\], "bo-",
              mec\="b", lw\=5, ms\=10, label\="Line 1")
[l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0.1, 0.5, 0.9\], \[0.5, 0.2, 0.7\], "rs-",
              mec\="r", lw\=5, ms\=10, label\="Line 2")

for [l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 in \[[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\]:

    \# draw shadows with same lines with slight offset and gray colors.

    [xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [l.get\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "matplotlib.lines.Line2D.get_xdata")
()
    [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [l.get\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ydata "matplotlib.lines.Line2D.get_ydata")
()
    [shadow](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [shadow.update\_from](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
([l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)

    \# adjust color
    [shadow.set\_color](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
("0.2")
    \# adjust zorder of the shadow lines so that it is drawn below the
    \# original lines
    [shadow.set\_zorder](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
([l.get\_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_zorder.html#matplotlib.artist.Artist.get_zorder "matplotlib.artist.Artist.get_zorder")
() \- 0.5)

    \# offset transform
    [transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [mtransforms.offset\_copy](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
([l.get\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_transform.html#matplotlib.artist.Artist.get_transform "matplotlib.artist.Artist.get_transform")
(), [fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
,
                                        x\=4.0, y\=-6.0, units\='points')
    [shadow.set\_transform](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
([transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)

    \# set the id for a later use
    [shadow.set\_gid](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
([l.get\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_label.html#matplotlib.artist.Artist.get_label "matplotlib.artist.Artist.get_label")
() + "\_shadow")

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0., 1.)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0., 1.)

\# save the figure as a bytes string in the svg format.
f \= [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
[plt.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
(f, format\="svg")

\# filter definition for a gaussian blur
[filter\_def](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""

\# read in the saved svg
[tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
, [xmlid](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ET.XMLID](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLID "xml.etree.ElementTree.XMLID")
(f.getvalue())

\# insert the filter definition in the svg dom tree.
[tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
.insert(0, [ET.XML](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "xml.etree.ElementTree.XML")
([filter\_def](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))

for [l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 in \[[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\]:
    \# pick up the svg element with given id
    [shadow](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
 \= [xmlid](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[l.get\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_label.html#matplotlib.artist.Artist.get_label "matplotlib.artist.Artist.get_label")\
() + "\_shadow"\]
    \# apply shadow filter
    [shadow](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
.set("filter", 'url(#dropshadow)')

[fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= "svg\_filter\_line.svg"
print(f"Saving '{[fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'")
[ET.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
([tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
).write([fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[`Download Jupyter notebook: svg_filter_line.ipynb`](https://matplotlib.org/stable/_downloads/9787ab1f9cf2a45d97792ee8188212ac/svg_filter_line.ipynb)

[`Download Python source code: svg_filter_line.py`](https://matplotlib.org/stable/_downloads/9f8aa7731c3c1bf0306b6dce55bacda0/svg_filter_line.py)

[`Download zipped: svg_filter_line.zip`](https://matplotlib.org/stable/_downloads/f25f849b9b735a808745b806dc92f848/svg_filter_line.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)