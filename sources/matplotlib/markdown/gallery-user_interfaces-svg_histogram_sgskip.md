[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html#sphx-glr-download-gallery-user-interfaces-svg-histogram-sgskip-py)
 to download the full example code.

SVG Histogram[#](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html#svg-histogram "Link to this heading")

=======================================================================================================================================

Demonstrate how to create an interactive histogram, in which bars are hidden or shown by clicking on legend markers.

The interactivity is encoded in ecmascript (javascript) and inserted in the SVG code in a post-processing step. To render the image, open it in a web browser. SVG is supported in most web browsers used by Linux and macOS users. Windows IE9 supports SVG, but earlier versions do not.

Notes[#](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html#notes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

The matplotlib backend lets us assign ids to each object. This is the mechanism used here to relate matplotlib objects created in python and the corresponding SVG constructs that are parsed in the second step. While flexible, ids are cumbersome to use for large collection of objects. Two mechanisms could be used to simplify things:

*   systematic grouping of objects into SVG <g> tags,
    
*   assigning classes to each SVG object according to its origin.
    

For example, instead of modifying the properties of each individual bar, the bars from the [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
 function could either be grouped in a PatchCollection, or be assigned a class="hist\_##" attribute.

CSS could also be used more extensively to replace repetitive markup throughout the generated SVG.

Author: [david.huard@gmail.com](mailto:david.huard%40gmail.com)

from io import [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
import json
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
\['svg.fonttype'\] \= 'none'

\# Apparently, this \`register\_namespace\` method is necessary to avoid garbling
\# the XML namespace with ns0.
[ET.register\_namespace](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace "xml.etree.ElementTree.register_namespace")
("", "http://www.w3.org/2000/svg")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# --- Create histogram, legend and title ---
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
r \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(100)
r1 \= r + 1
labels \= \['Rabbits', 'Frogs'\]
H \= [plt.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
(\[r, r1\], label\=labels)
containers \= H\[\-1\]
leg \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(frameon\=False)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("From a web browser, click on the legend\\n"
          "marker to toggle the corresponding histogram.")

\# --- Add ids to the svg objects we'll modify

hist\_patches \= {}
for ic, c in enumerate(containers):
    hist\_patches\[f'hist\_{ic}'\] \= \[\]
    for il, element in enumerate(c):
        element.set\_gid(f'hist\_{ic}\_patch\_{il}')
        hist\_patches\[f'hist\_{ic}'\].append(f'hist\_{ic}\_patch\_{il}')

\# Set ids for the legend patches
for i, t in enumerate(leg.get\_patches()):
    t.set\_gid(f'leg\_patch\_{i}')

\# Set ids for the text patches
for i, t in enumerate(leg.get\_texts()):
    t.set\_gid(f'leg\_text\_{i}')

\# Save SVG in a fake file object.
f \= [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
[plt.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
(f, format\="svg")

\# Create XML tree from the SVG file.
tree, xmlid \= [ET.XMLID](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLID "xml.etree.ElementTree.XMLID")
(f.getvalue())

\# --- Add interactivity ---

\# Add attributes to the patch objects.
for i, t in enumerate(leg.get\_patches()):
    el \= xmlid\[f'leg\_patch\_{i}'\]
    el.set('cursor', 'pointer')
    el.set('onclick', "toggle\_hist(this)")

\# Add attributes to the text objects.
for i, t in enumerate(leg.get\_texts()):
    el \= xmlid\[f'leg\_text\_{i}'\]
    el.set('cursor', 'pointer')
    el.set('onclick', "toggle\_hist(this)")

\# Create script defining the function \`toggle\_hist\`.
\# We create a global variable \`container\` that stores the patches id
\# belonging to each histogram. Then a function "toggle\_element" sets the
\# visibility attribute of all patches of each histogram and the opacity
\# of the marker itself.

script \= """
<script type="text/ecmascript">
<!\[CDATA\[\
var container = %s\
\
function toggle(oid, attribute, values) {\
    /\* Toggle the style attribute of an object between two values.\
\
    Parameters\
    ----------\
    oid : str\
      Object identifier.\
    attribute : str\
      Name of style attribute.\
    values : \[on state, off state\]\
      The two values that are switched between.\
    \*/\
    var obj = document.getElementById(oid);\
    var a = obj.style\[attribute\];\
\
    a = (a == values\[0\] || a == "") ? values\[1\] : values\[0\];\
    obj.style\[attribute\] = a;\
    }\
\
function toggle\_hist(obj) {\
\
    var num = obj.id.slice(-1);\
\
    toggle('leg\_patch\_' + num, 'opacity', \[1, 0.3\]);\
    toggle('leg\_text\_' + num, 'opacity', \[1, 0.5\]);\
\
    var names = container\['hist\_'+num\]\
\
    for (var i=0; i < names.length; i++) {\
        toggle(names\[i\], 'opacity', \[1, 0\])\
    };\
    }\
\]\]>
</script>
""" % [json.dumps](https://docs.python.org/3/library/json.html#json.dumps "json.dumps")
(hist\_patches)

\# Add a transition effect
css \= tree.find('.//{http://www.w3.org/2000/svg}style')
css.text \= css.text + "g {-webkit-transition:opacity 0.4s ease-out;" + \\
    "-moz-transition:opacity 0.4s ease-out;}"

\# Insert the script and save to file.
tree.insert(0, [ET.XML](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "xml.etree.ElementTree.XML")
(script))

[ET.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
(tree).write("svg\_histogram.svg")

[`Download Jupyter notebook: svg_histogram_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/ebe686565d37c82ce4be61ed77e181e8/svg_histogram_sgskip.ipynb)

[`Download Python source code: svg_histogram_sgskip.py`](https://matplotlib.org/stable/_downloads/dbbfc471cc5f69a894fff87dbd2bbf19/svg_histogram_sgskip.py)

[`Download zipped: svg_histogram_sgskip.zip`](https://matplotlib.org/stable/_downloads/a093a8cbc50e27bbe8c54a52cf8f91db/svg_histogram_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page