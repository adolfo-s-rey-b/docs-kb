[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/svg_tooltip_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/svg_tooltip_sgskip.html#sphx-glr-download-gallery-user-interfaces-svg-tooltip-sgskip-py)
 to download the full example code.

SVG Tooltip[#](https://matplotlib.org/stable/gallery/user_interfaces/svg_tooltip_sgskip.html#svg-tooltip "Link to this heading")

=================================================================================================================================

This example shows how to create a tooltip that will show up when hovering over a matplotlib patch.

Although it is possible to create the tooltip from CSS or javascript, here we create it in matplotlib and simply toggle its visibility on when hovering over the patch. This approach provides total control over the tooltip placement and appearance, at the expense of more code up front.

The alternative approach would be to put the tooltip content in `title` attributes of SVG objects. Then, using an existing js/CSS library, it would be relatively straightforward to create the tooltip in the browser. The content would be dictated by the `title` attribute, and the appearance by the CSS.

author:

David Huard

from io import [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt

[ET.register\_namespace](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace "xml.etree.ElementTree.register_namespace")
("", "http://www.w3.org/2000/svg")

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Create patches to which tooltips will be assigned.
rect1 \= plt.Rectangle((10, \-20), 10, 5, fc\='blue')
rect2 \= plt.Rectangle((\-20, 15), 10, 5, fc\='green')

shapes \= \[rect1, rect2\]
labels \= \['This is a blue rectangle.', 'This is a green rectangle'\]

for i, (item, label) in enumerate(zip(shapes, labels)):
    patch \= ax.add\_patch(item)
    annotate \= ax.annotate(labels\[i\], xy\=item.get\_xy(), xytext\=(0, 0),
                           textcoords\='offset points', color\='w', ha\='center',
                           fontsize\=8, bbox\=dict(boxstyle\='round, pad=.5',
                                                 fc\=(.1, .1, .1, .92),
                                                 ec\=(1., 1., 1.), lw\=1,
                                                 zorder\=1))

    ax.add\_patch(patch)
    patch.set\_gid(f'mypatch\_{i:03d}')
    annotate.set\_gid(f'mytooltip\_{i:03d}')

\# Save the figure in a fake file object
ax.set\_xlim(\-30, 30)
ax.set\_ylim(\-30, 30)
ax.set\_aspect('equal')

f \= [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
[plt.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
(f, format\="svg")

\# --- Add interactivity ---

\# Create XML tree from the SVG file.
tree, xmlid \= [ET.XMLID](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLID "xml.etree.ElementTree.XMLID")
(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    \# Get the index of the shape
    index \= shapes.index(i)
    \# Hide the tooltips
    tooltip \= xmlid\[f'mytooltip\_{index:03d}'\]
    tooltip.set('visibility', 'hidden')
    \# Assign onmouseover and onmouseout callbacks to patches.
    mypatch \= xmlid\[f'mypatch\_{index:03d}'\]
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

\# This is the script defining the ShowTooltip and HideTooltip functions.
script \= """
    <script type="text/ecmascript">
    <!\[CDATA\[\
\
    function init(event) {\
        if ( window.svgDocument == null ) {\
            svgDocument = event.target.ownerDocument;\
            }\
        }\
\
    function ShowTooltip(obj) {\
        var cur = obj.id.split("\_")\[1\];\
        var tip = svgDocument.getElementById('mytooltip\_' + cur);\
        tip.setAttribute('visibility', "visible")\
        }\
\
    function HideTooltip(obj) {\
        var cur = obj.id.split("\_")\[1\];\
        var tip = svgDocument.getElementById('mytooltip\_' + cur);\
        tip.setAttribute('visibility', "hidden")\
        }\
\
    \]\]>
    </script>
    """

\# Insert the script at the top of the file and save it.
tree.insert(0, [ET.XML](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "xml.etree.ElementTree.XML")
(script))
[ET.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
(tree).write('svg\_tooltip.svg')

[`Download Jupyter notebook: svg_tooltip_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/bd174ce75b292e7e21e43d7719eecd67/svg_tooltip_sgskip.ipynb)

[`Download Python source code: svg_tooltip_sgskip.py`](https://matplotlib.org/stable/_downloads/b1d72b68be293db9dab6f77187a06e16/svg_tooltip_sgskip.py)

[`Download zipped: svg_tooltip_sgskip.zip`](https://matplotlib.org/stable/_downloads/e761120577534aec4c9c7339b605106d/svg_tooltip_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)