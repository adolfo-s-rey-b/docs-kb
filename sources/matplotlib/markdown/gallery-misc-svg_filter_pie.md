[Skip to main content](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html#sphx-glr-download-gallery-misc-svg-filter-pie-py)
 to download the full example code.

SVG filter pie[#](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html#svg-filter-pie "Link to this heading")

========================================================================================================================

Demonstrate SVG filtering effects which might be used with Matplotlib. The pie chart drawing code is borrowed from pie\_demo.py

Note that the filtering effects are only effective if your SVG renderer support it.

![svg filter pie](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_pie_001_2_00x.png)

Saving 'svg\_filter\_pie.svg'

  

import io
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt

from matplotlib.patches import [Shadow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")

\# make a square figure and Axes
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.1, 0.8, 0.8))

[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 'Frogs', 'Hogs', 'Dogs', 'Logs'
[fracs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[15, 30, 45, 10\]

[explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0, 0.05, 0, 0)

\# We want to draw the shadow for each pie, but we will not use "shadow"
\# option as it doesn't save the references to the shadow patches.
[pie](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([fracs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%1.1f%%')

for [w](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 in [pie.wedges](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
:
    \# set the id with the label.
    [w.set\_gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid")
([w.get\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_label.html#matplotlib.artist.Artist.get_label "matplotlib.artist.Artist.get_label")
())

    \# we don't want to draw the edge of the pie
    [w.set\_edgecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")
("none")

for [w](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 in [pie.wedges](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
:
    \# create shadow patch
    [s](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 \= [Shadow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
([w](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
, \-0.01, \-0.01)
    [s.set\_gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid")
([w.get\_gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_gid.html#matplotlib.artist.Artist.get_gid "matplotlib.artist.Artist.get_gid")
() + "\_shadow")
    [s.set\_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder")
([w.get\_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_zorder.html#matplotlib.artist.Artist.get_zorder "matplotlib.artist.Artist.get_zorder")
() \- 0.1)
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([s](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
)

\# save
f \= [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
[plt.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
(f, format\="svg")

\# Filter definition for shadow using a gaussian blur and lighting effect.
\# The lighting filter is copied from http://www.w3.org/TR/SVG/filters.html

\# I tested it with Inkscape and Firefox3. "Gaussian blur" is supported
\# in both, but the lighting effect only in Inkscape. Also note
\# that, Inkscape's exporting also may not support it.

[filter\_def](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='2'/>
    </filter>

    <filter id='MyFilter' filterUnits='objectBoundingBox'
            x='0' y='0' width='1' height='1'>
      <feGaussianBlur in='SourceAlpha' stdDeviation='4%' result='blur'/>
      <feOffset in='blur' dx='4%' dy='4%' result='offsetBlur'/>
      <feSpecularLighting in='blur' surfaceScale='5' specularConstant='.75'
           specularExponent='20' lighting-color='#bbbbbb' result='specOut'>
        <fePointLight x='-5000%' y='-10000%' z='20000%'/>
      </feSpecularLighting>
      <feComposite in='specOut' in2='SourceAlpha'
                   operator='in' result='specOut'/>
      <feComposite in='SourceGraphic' in2='specOut' operator='arithmetic'
    k1='0' k2='1' k3='1' k4='0'/>
    </filter>
  </defs>
"""

[tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
, [xmlid](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ET.XMLID](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLID "xml.etree.ElementTree.XMLID")
(f.getvalue())

\# insert the filter definition in the svg dom tree.
[tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
.insert(0, [ET.XML](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "xml.etree.ElementTree.XML")
([filter\_def](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [pie\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [pie](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
 \= [xmlid](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[pie\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]
    [pie](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
.set("filter", 'url(#MyFilter)')

    [shadow](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
 \= [xmlid](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[pie\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
 + "\_shadow"\]
    [shadow](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
.set("filter", 'url(#dropshadow)')

[fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= "svg\_filter\_pie.svg"
print(f"Saving '{[fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'")
[ET.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
([tree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
).write([fn](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[`Download Jupyter notebook: svg_filter_pie.ipynb`](https://matplotlib.org/stable/_downloads/ffce266ab187d41ab9a3afd68f7826bf/svg_filter_pie.ipynb)

[`Download Python source code: svg_filter_pie.py`](https://matplotlib.org/stable/_downloads/15ebd41aec6ebf084ad5797ba93359e4/svg_filter_pie.py)

[`Download zipped: svg_filter_pie.zip`](https://matplotlib.org/stable/_downloads/695240f0e4ef5c3f89a57755d65835b9/svg_filter_pie.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)