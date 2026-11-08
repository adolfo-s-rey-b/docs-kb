[Skip to main content](https://matplotlib.org/stable/gallery/misc/set_and_get.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/set_and_get.html#sphx-glr-download-gallery-misc-set-and-get-py)
 to download the full example code.

Set and get properties[#](https://matplotlib.org/stable/gallery/misc/set_and_get.html#set-and-get-properties "Link to this heading")

=====================================================================================================================================

The pyplot interface allows you to use `setp` and `getp` to set and get object properties respectively, as well as to do introspection on the object.

Setting with `setp`[#](https://matplotlib.org/stable/gallery/misc/set_and_get.html#setting-with-setp "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

To set the linestyle of a line to be dashed, you use `setp`:

\>>> line, \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[1, 2, 3\])
\>>> [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(line, linestyle\='--')

If you want to know the valid types of arguments, you can provide the name of the property you want to set without a value:

\>>> [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(line, 'linestyle')
    linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

If you want to see all the properties that can be set, and their possible values, you can do:

\>>> [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(line)

`setp` operates on a single instance or a list of instances. If you are in query mode introspecting the possible values, only the first instance in the sequence is used. When actually setting values, all the instances will be set. For example, suppose you have a list of two lines, the following will make both lines thicker and red:

\>>> [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.01)
\>>> [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\>>> [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\>>> [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\>>> [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, linewidth\=2, color\='r')

Getting with `getp`[#](https://matplotlib.org/stable/gallery/misc/set_and_get.html#getting-with-getp "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

`getp` returns the value of a given attribute. You can use it to query the value of a single attribute:

\>>> [plt.getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")
(line, 'linewidth')
    0.5

or all the attribute/value pairs:

\>>> [plt.getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")
(line)
    aa = True
    alpha = 1.0
    antialiased = True
    c = b
    clip\_on = True
    color = b
    ... long listing skipped ...

Aliases[#](https://matplotlib.org/stable/gallery/misc/set_and_get.html#aliases "Link to this heading")

-------------------------------------------------------------------------------------------------------

To reduce keystrokes in interactive mode, a number of properties have short aliases, e.g., 'lw' for 'linewidth' and 'mec' for 'markeredgecolor'. When calling set or get in introspection mode, these properties will be listed as 'fullname' or 'aliasname'.

![Hi mom](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_001_2_00x.png)

Line setters
  agg\_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image
  alpha: float or None
  animated: bool
  antialiased or aa: bool
  clip\_box: \`~matplotlib.transforms.BboxBase\` or None
  clip\_on: bool
  clip\_path: Patch or (Path, Transform) or None
  color or c: :mpltype:\`color\`
  dash\_capstyle: \`.CapStyle\` or {'butt', 'projecting', 'round'}
  dash\_joinstyle: \`.JoinStyle\` or {'miter', 'round', 'bevel'}
  dashes: sequence of floats (on/off ink in points) or (None, None)
  data: (2, N) array or two 1D arrays
  drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
  figure: \`~matplotlib.figure.Figure\` or \`~matplotlib.figure.SubFigure\`
  fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
  gapcolor: :mpltype:\`color\` or None
  gid: str
  in\_layout: bool
  label: object
  linestyle or ls: {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)
  linewidth or lw: float
  marker: marker style string, \`~.path.Path\` or \`~.markers.MarkerStyle\`
  markeredgecolor or mec: :mpltype:\`color\`
  markeredgewidth or mew: float
  markerfacecolor or mfc: :mpltype:\`color\`
  markerfacecoloralt or mfcalt: :mpltype:\`color\`
  markersize or ms: float
  markevery: None or int or (int, int) or slice or list\[int\] or float or (float, float) or list\[bool\]
  mouseover: bool
  path\_effects: list of \`.AbstractPathEffect\`
  picker: float or callable\[\[Artist, Event\], tuple\[bool, dict\]\]
  pickradius: float
  rasterized: bool
  sketch\_params: (scale: float, length: float, randomness: float)
  snap: bool or None
  solid\_capstyle: \`.CapStyle\` or {'butt', 'projecting', 'round'}
  solid\_joinstyle: \`.JoinStyle\` or {'miter', 'round', 'bevel'}
  transform: \`~matplotlib.transforms.Transform\`
  url: str
  visible: bool
  xdata: 1D array
  ydata: 1D array
  zorder: float
Line getters
    agg\_filter = None
    alpha = None
    animated = False
    antialiased or aa = True
    bbox = Bbox(x0=0.0, y0=-1.0, x1=0.99, y1=1.0)
    children = \[\]
    clip\_box = TransformedBbox(     Bbox(x0=0.0, y0=0.0, x1=1.0, ...
    clip\_on = True
    clip\_path = None
    color or c = r
    dash\_capstyle = butt
    dash\_joinstyle = round
    data = (array(\[0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, ...\
    drawstyle or ds = default\
    figure = Figure(640x480)\
    fillstyle = full\
    gapcolor = None\
    gid = None\
    in\_layout = True\
    label = \_child0\
    linestyle or ls = --\
    linewidth or lw = 2.0\
    marker = None\
    markeredgecolor or mec = r\
    markeredgewidth or mew = 1.0\
    markerfacecolor or mfc = r\
    markerfacecoloralt or mfcalt = none\
    markersize or ms = 6.0\
    markevery = None\
    mouseover = False\
    path = Path(array(\[\[ 0.00000000e+00,  0.00000000e+00\],   ...\
    path\_effects = \[\]\
    picker = None\
    pickradius = 5\
    rasterized = False\
    sketch\_params = None\
    snap = None\
    solid\_capstyle = projecting\
    solid\_joinstyle = round\
    tightbbox = Bbox(x0=80.0, y0=52.8, x1=571.04, y1=422.4)\
    transform = CompositeGenericTransform(     TransformWrapper(  ...\
    transformed\_clip\_path\_and\_affine = (None, None)\
    url = None\
    visible = True\
    window\_extent = Bbox(x0=80.0, y0=-316.79999999999995, x1=571.04, y...\
    xdata = \[0.   0.01 0.02 0.03 0.04 0.05\]...\
    xydata = \[\[0.         0.        \]  \[0.01       0.06279052\] ...\
    ydata = \[0.         0.06279052 0.12533323 0.18738131 0.248...\
    zorder = 2\
Rectangle setters\
  agg\_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image\
  alpha: float or None\
  angle: unknown\
  animated: bool\
  antialiased or aa: bool or None\
  bounds: (left, bottom, width, height)\
  capstyle: \`.CapStyle\` or {'butt', 'projecting', 'round'}\
  clip\_box: \`~matplotlib.transforms.BboxBase\` or None\
  clip\_on: bool\
  clip\_path: Patch or (Path, Transform) or None\
  color: :mpltype:\`color\`\
  edgecolor or ec: :mpltype:\`color\` or None\
  edgegapcolor: :mpltype:\`color\` or None\
  facecolor or fc: :mpltype:\`color\` or None\
  figure: \`~matplotlib.figure.Figure\` or \`~matplotlib.figure.SubFigure\`\
  fill: bool\
  gid: str\
  hatch: {'/', '\\\\', '|', '-', '+', 'x', 'o', 'O', '.', '\*'}\
  hatch\_linewidth: unknown\
  hatchcolor: :mpltype:\`color\` or 'edge' or None\
  height: unknown\
  in\_layout: bool\
  joinstyle: \`.JoinStyle\` or {'miter', 'round', 'bevel'}\
  label: object\
  linestyle or ls: {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)\
  linewidth or lw: float or None\
  mouseover: bool\
  path\_effects: list of \`.AbstractPathEffect\`\
  picker: None or bool or float or callable\
  rasterized: bool\
  sketch\_params: (scale: float, length: float, randomness: float)\
  snap: bool or None\
  transform: \`~matplotlib.transforms.Transform\`\
  url: str\
  visible: bool\
  width: unknown\
  x: unknown\
  xy: (float, float)\
  y: unknown\
  zorder: float\
Rectangle getters\
    agg\_filter = None\
    alpha = None\
    angle = 0.0\
    animated = False\
    antialiased or aa = True\
    bbox = Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0)\
    capstyle = butt\
    center = \[0.5 0.5\]\
    children = \[\]\
    clip\_box = None\
    clip\_on = True\
    clip\_path = None\
    corners = \[\[0. 0.\]  \[1. 0.\]  \[1. 1.\]  \[0. 1.\]\]\
    data\_transform = BboxTransformTo(     TransformedBbox(         Bbox...\
    edgecolor or ec = (0.0, 0.0, 0.0, 0.0)\
    edgegapcolor = None\
    extents = Bbox(x0=80.0, y0=52.8, x1=576.0, y1=422.4)\
    facecolor or fc = (1.0, 1.0, 1.0, 1.0)\
    figure = Figure(640x480)\
    fill = True\
    gid = None\
    hatch = None\
    hatch\_linewidth = 1.0\
    hatchcolor = (0.0, 0.0, 0.0, 1.0)\
    height = 1.0\
    in\_layout = True\
    joinstyle = miter\
    label =\
    linestyle or ls = solid\
    linewidth or lw = 0.0\
    mouseover = False\
    patch\_transform = CompositeGenericTransform(     BboxTransformTo(   ...\
    path = Path(array(\[\[0., 0.\],        \[1., 0.\],        \[1.,...\
    path\_effects = \[\]\
    picker = None\
    rasterized = False\
    sketch\_params = None\
    snap = None\
    tightbbox = Bbox(x0=80.0, y0=52.8, x1=576.0, y1=422.4)\
    transform = CompositeGenericTransform(     CompositeGenericTra...\
    transformed\_clip\_path\_and\_affine = (None, None)\
    url = None\
    verts = \[\[ 80.   52.8\]  \[576.   52.8\]  \[576.  422.4\]  \[ 80...\
    visible = True\
    width = 1.0\
    window\_extent = Bbox(x0=80.0, y0=52.8, x1=576.0, y1=422.4)\
    x = 0.0\
    xy = (0.0, 0.0)\
    y = 0.0\
    zorder = 1\
Text setters\
  agg\_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image\
  alpha: float or None\
  animated: bool\
  antialiased: bool\
  backgroundcolor: :mpltype:\`color\`\
  bbox: dict with properties for \`.FancyBboxPatch\` or None\
  clip\_box: \`~matplotlib.transforms.BboxBase\` or None\
  clip\_on: bool\
  clip\_path: Patch or (Path, Transform) or None\
  color or c: :mpltype:\`color\`\
  figure: \`~matplotlib.figure.Figure\` or \`~matplotlib.figure.SubFigure\`\
  fontfamily or family or fontname: {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}\
  fontfeatures: list of str, or tuple of str, or None\
  fontproperties or font or font\_properties: \`.font\_manager.FontProperties\` or \`str\` or \`pathlib.Path\`\
  fontsize or size: float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}\
  fontstretch or stretch: {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}\
  fontstyle or style: {'normal', 'italic', 'oblique'}\
  fontvariant or variant: {'normal', 'small-caps'}\
  fontweight or weight: {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}\
  gid: str\
  horizontalalignment or ha: {'left', 'center', 'right'}\
  in\_layout: bool\
  label: object\
  language: str or None\
  linespacing: 'normal' or float, default: 'normal'\
  math\_fontfamily: str\
  mouseover: bool\
  multialignment or ma: {'left', 'right', 'center'}\
  parse\_math: bool\
  path\_effects: list of \`.AbstractPathEffect\`\
  picker: None or bool or float or callable\
  position: (float, float)\
  rasterized: bool\
  rotation: float or {'vertical', 'horizontal'}\
  rotation\_mode: {None, 'default', 'anchor', 'xtick', 'ytick'}\
  sketch\_params: (scale: float, length: float, randomness: float)\
  snap: bool or None\
  text: object\
  transform: \`~matplotlib.transforms.Transform\`\
  transform\_rotates\_text: bool\
  url: str\
  usetex: bool, default: :rc:\`text.usetex\`\
  verticalalignment or va: {'baseline', 'bottom', 'center', 'center\_baseline', 'top'}\
  visible: bool\
  wrap: bool\
  x: float\
  y: float\
  zorder: float\
Text getters\
    agg\_filter = None\
    alpha = None\
    animated = False\
    antialiased = True\
    bbox\_patch = None\
    children = \[\]\
    clip\_box = None\
    clip\_on = True\
    clip\_path = None\
    color or c = black\
    figure = Figure(640x480)\
    fontfamily or family or fontname = \['sans-serif'\]\
    fontfeatures = None\
    fontname or name = DejaVu Sans\
    fontproperties or font or font\_properties = sans\\-serif:style=normal:variant=normal:weight=nor...\
    fontsize or size = 12.0\
    fontstyle or style = normal\
    fontvariant or variant = normal\
    fontweight or weight = normal\
    gid = None\
    horizontalalignment or ha = center\
    in\_layout = True\
    label =\
    language = None\
    linespacing = normal\
    math\_fontfamily = dejavusans\
    mouseover = False\
    parse\_math = True\
    path\_effects = \[\]\
    picker = None\
    position = (0.5, 1.0)\
    rasterized = False\
    rotation = 0.0\
    rotation\_mode = default\
    sketch\_params = None\
    snap = None\
    stretch = normal\
    text = Hi mom\
    tightbbox = Bbox(x0=294.5, y0=426.7294270833333, x1=361.5, y1=...\
    transform = CompositeGenericTransform(     BboxTransformTo(   ...\
    transform\_rotates\_text = False\
    transformed\_clip\_path\_and\_affine = (None, None)\
    unitless\_position = (0.5, 1.0)\
    url = None\
    usetex = False\
    verticalalignment or va = baseline\
    visible = True\
    window\_extent = Bbox(x0=294.5, y0=426.7294270833333, x1=361.5, y1=...\
    wrap = False\
    zorder = 3\
\
  \
\
import matplotlib.pyplot as plt\
import numpy as np\
\
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(0, 1.0, 0.01)\
[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
)\
[y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(4\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
)\
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
 \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
)\
[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
 \= [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, linestyle\='--')       \# set both to dashed\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, linewidth\=2, color\='r')  \# line1 is thick and red\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, linewidth\=1, color\='g')  \# line2 is thinner and green\
\
print('Line setters')\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
)\
print('Line getters')\
[plt.getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")\
([l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
)\
\
print('Rectangle setters')\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")\
().patch)\
print('Rectangle getters')\
[plt.getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")\
([plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")\
().patch)\
\
[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
('Hi mom')\
print('Text setters')\
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")\
([t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
)\
print('Text getters')\
[plt.getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")\
([t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
)\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
[`Download Jupyter notebook: set_and_get.ipynb`](https://matplotlib.org/stable/_downloads/37e4a04cefe1e372ce19afe76d517baa/set_and_get.ipynb)\
\
[`Download Python source code: set_and_get.py`](https://matplotlib.org/stable/_downloads/1164b1c779f1bc16a7184125264f2b1a/set_and_get.py)\
\
[`Download zipped: set_and_get.zip`](https://matplotlib.org/stable/_downloads/0e63a282897fe57d2bbbe954a05b37d2/set_and_get.zip)\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page