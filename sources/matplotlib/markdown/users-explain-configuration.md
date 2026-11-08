[Skip to main content](https://matplotlib.org/stable/users/explain/configuration.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/configuration.html#sphx-glr-download-users-explain-configuration-py)
 to download the full example code.

Matplotlib configuration - rcParams[#](https://matplotlib.org/stable/users/explain/configuration.html#matplotlib-configuration-rcparams "Link to this heading")

================================================================================================================================================================

Matplotlib's configuration parameters (rcParams) control the behavior and appearance of plots. These parameters are stored in a dict-like variable called [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 (also accessible via `plt.rcParams`).

The following is a comprehensive reference of all available rcParams and their default values.

Backends[#](https://matplotlib.org/stable/users/explain/configuration.html#backends "Link to this heading")

------------------------------------------------------------------------------------------------------------

webagg.port: `8988`

The port to use for the web server in the WebAgg backend.

webagg.address: `'127.0.0.1'`

The address on which the WebAgg web server should be reachable.

webagg.port\_retries: `50`

If webagg.port is unavailable, a number of other random ports will be tried until one that is available is found.

webagg.open\_in\_browser: `True`

When True, open the web browser to the plot that is shown

backend\_fallback: `True`

If you are running pyplot inside a GUI and your backend choice conflicts, we will automatically try to find a compatible one for you if backend\_fallback is True

interactive: `False`

_no description_

figure.hooks: `[]`

list of dotted.module.name:dotted.callable.name

toolbar: `'toolbar2'`

{None, toolbar2, toolmanager}

timezone: `'UTC'`

a pytz timezone string, e.g., US/Central or Europe/Paris

Lines[#](https://matplotlib.org/stable/users/explain/configuration.html#lines "Link to this heading")

------------------------------------------------------------------------------------------------------

Default properties for line objects, such as those returned by plot().

lines.linewidth: `1.5`

line width in points

lines.linestyle: `'-'`

solid line

lines.color: `'C0'`

has no affect on plot(); see axes.prop\_cycle

lines.marker: `'None'`

the default marker

lines.markerfacecolor: `'auto'`

the default marker face color

lines.markeredgecolor: `'auto'`

the default marker edge color

lines.markeredgewidth: `1.0`

the line width around the marker symbol

lines.markersize: `6.0`

marker size, in points

lines.dash\_joinstyle: `'round'`

{miter, round, bevel}

lines.dash\_capstyle: `'butt'`

{butt, round, projecting}

lines.solid\_joinstyle: `'round'`

{miter, round, bevel}

lines.solid\_capstyle: `'projecting'`

{butt, round, projecting}

lines.antialiased: `True`

render lines in antialiased (no jaggies)

lines.dashed\_pattern: `[3.7, 1.6]`

The dash pattern for linestyle 'dashed'

lines.dashdot\_pattern: `[6.4, 1.6, 1.0, 1.6]`

The dash pattern for linestyle 'dashdot'

lines.dotted\_pattern: `[1.0, 1.65]`

The dash pattern for linestyle 'dotted'

lines.scale\_dashes: `True`

_no description_

markers.fillstyle: `'full'`

{full, left, right, bottom, top, none}

pcolor.shading: `'auto'`

_no description_

pcolormesh.snap: `True`

Whether to snap the mesh to pixel boundaries. This is provided solely to allow old test images to remain unchanged. Set to False to obtain the previous behavior.

Patches[#](https://matplotlib.org/stable/users/explain/configuration.html#patches "Link to this heading")

----------------------------------------------------------------------------------------------------------

patch.linewidth: `1.0`

edge width in points.

patch.facecolor: `'C0'`

_no description_

patch.edgecolor: `'black'`

By default, Patches and Collections do not draw edges. This value is only used if facecolor is "none" (an Artist without facecolor and edgecolor would be invisible) or if patch.force\_edgecolor is True.

patch.force\_edgecolor: `False`

By default, Patches and Collections do not draw edges. Set this to True to draw edges with patch.edgedcolor as the default edgecolor. This is mainly relevant for styles.

patch.antialiased: `True`

render patches in antialiased (no jaggies)

Hatches[#](https://matplotlib.org/stable/users/explain/configuration.html#hatches "Link to this heading")

----------------------------------------------------------------------------------------------------------

hatch.color: `'edge'`

_no description_

hatch.linewidth: `1.0`

_no description_

Boxplot[#](https://matplotlib.org/stable/users/explain/configuration.html#boxplot "Link to this heading")

----------------------------------------------------------------------------------------------------------

boxplot.notch: `False`

_no description_

boxplot.vertical: `True`

_no description_

boxplot.whiskers: `1.5`

_no description_

boxplot.bootstrap: `None`

_no description_

boxplot.patchartist: `False`

_no description_

boxplot.showmeans: `False`

_no description_

boxplot.showcaps: `True`

_no description_

boxplot.showbox: `True`

_no description_

boxplot.showfliers: `True`

_no description_

boxplot.meanline: `False`

_no description_

boxplot.flierprops.color: `'black'`

_no description_

boxplot.flierprops.marker: `'o'`

_no description_

boxplot.flierprops.markerfacecolor: `'none'`

_no description_

boxplot.flierprops.markeredgecolor: `'black'`

_no description_

boxplot.flierprops.markeredgewidth: `1.0`

_no description_

boxplot.flierprops.markersize: `6.0`

_no description_

boxplot.flierprops.linestyle: `'none'`

_no description_

boxplot.flierprops.linewidth: `1.0`

_no description_

boxplot.boxprops.color: `'black'`

_no description_

boxplot.boxprops.linewidth: `1.0`

_no description_

boxplot.boxprops.linestyle: `'-'`

_no description_

boxplot.whiskerprops.color: `'black'`

_no description_

boxplot.whiskerprops.linewidth: `1.0`

_no description_

boxplot.whiskerprops.linestyle: `'-'`

_no description_

boxplot.capprops.color: `'black'`

_no description_

boxplot.capprops.linewidth: `1.0`

_no description_

boxplot.capprops.linestyle: `'-'`

_no description_

boxplot.medianprops.color: `'C1'`

_no description_

boxplot.medianprops.linewidth: `1.0`

_no description_

boxplot.medianprops.linestyle: `'-'`

_no description_

boxplot.meanprops.color: `'C2'`

_no description_

boxplot.meanprops.marker: `'^'`

_no description_

boxplot.meanprops.markerfacecolor: `'C2'`

_no description_

boxplot.meanprops.markeredgecolor: `'C2'`

_no description_

boxplot.meanprops.markersize: `6.0`

_no description_

boxplot.meanprops.linestyle: `'--'`

_no description_

boxplot.meanprops.linewidth: `1.0`

_no description_

Font[#](https://matplotlib.org/stable/users/explain/configuration.html#font "Link to this heading")

----------------------------------------------------------------------------------------------------

The font properties used by [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 See [https://matplotlib.org/stable/api/font\_manager\_api.html](https://matplotlib.org/stable/api/font_manager_api.html)
 for more information on font properties. The 6 font properties used for font matching are given below with their default values.

font.family: `['sans-serif']`

_no description_

font.style: `'normal'`

_no description_

font.variant: `'normal'`

_no description_

font.weight: `'normal'`

_no description_

font.stretch: `'normal'`

_no description_

font.size: `10.0`

_no description_

font.serif: `['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']`

_no description_

font.sans-serif: `['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']`

_no description_

font.cursive: `['Apple Chancery', 'Textile', 'Zapf Chancery', 'Sand', 'Script MT', 'Felipa', 'Comic Neue', 'Comic Sans MS', 'cursive']`

_no description_

font.fantasy: `['Chicago', 'Charcoal', 'Impact', 'Western', 'xkcd script', 'fantasy']`

_no description_

font.monospace: `['DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Computer Modern Typewriter', 'Andale Mono', 'Nimbus Mono L', 'Courier New', 'Courier', 'Fixed', 'Terminal', 'monospace']`

_no description_

font.enable\_last\_resort: `True`

If True, then Unicode Consortium's Last Resort font will be appended to all font selections. This ensures that there will always be a glyph displayed.

Text properties[#](https://matplotlib.org/stable/users/explain/configuration.html#text-properties "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

text.color: `'black'`

_no description_

text.language: `None`

The language of the text in a format accepted by libraqm, namely [a BCP47 language code](https://www.w3.org/International/articles/language-tags/)
. If None, then no particular language will be implied, and default font settings will be used.

text.hinting: `'default'`

FreeType hinting flag ("foo" corresponds to FT\_LOAD\_FOO); may be one of the following (Proprietary Matplotlib-specific synonyms are given in parentheses, but their use is discouraged): - default: Use the font's native hinter if possible, else FreeType's auto-hinter. ("either" is a synonym).- no\_autohint: Use the font's native hinter if possible, else don't hint. ("native" is a synonym.)- force\_autohint: Use FreeType's auto-hinter. ("auto" is a synonym.)- no\_hinting: Disable hinting. ("none" is a synonym.)

text.hinting\_factor: `None`

\[DEPRECATED\] This setting has no effect.

text.kerning\_factor: `None`

\[DEPRECATED\] Specifies the scaling factor for kerning values. This is provided solely to allow old test images to remain unchanged. Set to 6 to obtain previous behavior. Values other than 0 or 6 have no defined meaning.

text.antialiased: `True`

If True (default), the text will be antialiased. This only affects raster outputs.

text.parse\_math: `True`

Use mathtext if there is an even number of unescaped dollar signs.

Mathtext and LaTeX[#](https://matplotlib.org/stable/users/explain/configuration.html#mathtext-and-latex "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

text.usetex: `False`

use latex for all text handling. The following fonts are supported through the usual rc parameter settings: new century schoolbook, bookman, times, palatino, zapf chancery, charter, serif, sans-serif, helvetica, avant garde, courier, monospace, computer modern roman, computer modern sans serif, computer modern typewriter

text.latex.engine: `'latex'`

The TeX engine/format to use. The following values are supported: - 'latex': The classic TeX engine (the current default). All backends render TeX's output by parsing the DVI output into glyphs and boxes and emitting those one by one. - 'latex+dvipng': The same as 'latex', with the exception that Agg-based backends rely on dvipng to rasterize TeX's output. This value was the default up to Matplotlib 3.10.

text.latex.preamble: `''`

IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO. text.latex.preamble is a single line of LaTeX code that will be passed on to the LaTeX system. It may contain any code that is valid for the LaTeX "preamble", i.e. between the "documentclass" and "begin{document}" statements. Note that it has to be put on a single line, which may become quite long. The following packages are always loaded with usetex, so beware of package collisions: color, fix-cm, geometry, graphicx, textcomp. PostScript (PSNFSS) font packages may also be loaded, depending on your font settings.

mathtext.fontset: `'dejavusans'`

Should be 'dejavusans' (default), 'dejavuserif', 'cm' (Computer Modern), 'stix', 'stixsans' or 'custom'

mathtext.bf: `'sans:bold'`

_no description_

mathtext.bfit: `'sans:italic:bold'`

_no description_

mathtext.cal: `'cursive'`

_no description_

mathtext.it: `'sans:italic'`

_no description_

mathtext.rm: `'sans'`

_no description_

mathtext.sf: `'sans'`

_no description_

mathtext.tt: `'monospace'`

_no description_

mathtext.fallback: `'cm'`

Select fallback font from \['cm' (Computer Modern), 'stix', 'stixsans'\] when a symbol cannot be found in one of the custom math fonts. Select 'None' to not perform fallback and replace the missing character by a dummy symbol.

mathtext.default: `'normal'`

The default font to use for math. Can be any of the LaTeX font names, including the special name "regular" for the same font used in regular text.

Axes[#](https://matplotlib.org/stable/users/explain/configuration.html#axes "Link to this heading")

----------------------------------------------------------------------------------------------------

axes.facecolor: `'white'`

axes background color

axes.edgecolor: `'black'`

axes edge color

axes.linewidth: `0.8`

edge line width

axes.grid: `False`

display grid or not

axes.grid.axis: `'both'`

which axis the grid should apply to

axes.grid.which: `'major'`

grid lines at {major, minor, both} ticks

axes.titlelocation: `'center'`

alignment of the title: {left, right, center}

axes.titlesize: `'large'`

font size of the axes title

axes.titleweight: `'normal'`

font weight of title

axes.titlecolor: `'auto'`

color of the axes title, auto falls back to text.color as default value

axes.titley: `None`

position title (axes relative units). None implies auto

axes.titlepad: `6.0`

pad between axes and title in points

axes.labelsize: `'medium'`

font size of the x and y labels

axes.labelpad: `4.0`

space between label and axis

axes.labelweight: `'normal'`

weight of the x and y labels

axes.labelcolor: `'black'`

_no description_

axes.axisbelow: `'line'`

draw axis gridlines and ticks: - below patches (True) - above patches but below lines ('line') - above all (False)

axes.formatter.limits: `[-5, 6]`

use scientific notation if log10 of the axis range is smaller than the first or larger than the second

axes.formatter.use\_locale: `False`

When True, format tick labels according to the user's locale. For example, use ',' as a decimal separator in the fr\_FR locale.

axes.formatter.use\_mathtext: `False`

When True, use mathtext for scientific notation.

axes.formatter.min\_exponent: `0`

minimum exponent to format in scientific notation

axes.formatter.useoffset: `True`

If True, the tick label formatter will default to labeling ticks relative to an offset when the data range is small compared to the minimum absolute value of the data.

axes.formatter.offset\_threshold: `4`

When useoffset is True, the offset will be used when it can remove at least this number of significant digits from tick labels.

axes.spines.left: `True`

display axis spines

axes.spines.bottom: `True`

_no description_

axes.spines.top: `True`

_no description_

axes.spines.right: `True`

_no description_

axes.unicode\_minus: `True`

use Unicode for the minus symbol rather than hyphen. See [https://en.wikipedia.org/wiki/Plus\_and\_minus\_signs#Character\_codes](https://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes)

axes.prop\_cycle: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`

_no description_

axes.xmargin: `0.05`

x margin. See [`margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")

axes.ymargin: `0.05`

y margin. See [`margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")

axes.zmargin: `0.05`

z margin. See [`margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")

axes.autolimit\_mode: `'data'`

If "data", use axes.xmargin and axes.ymargin as is. If "round\_numbers", after application of margins, axis limits are further expanded to the nearest "round" number.

### Polar Axes[#](https://matplotlib.org/stable/users/explain/configuration.html#polar-axes "Link to this heading")

polaraxes.grid: `True`

display grid on polar axes

### 3D Axes[#](https://matplotlib.org/stable/users/explain/configuration.html#d-axes "Link to this heading")

axes3d.grid: `True`

display grid on 3D axes

axes3d.automargin: `False`

automatically add margin when manually setting 3D axis limits

axes3d.xaxis.panecolor: `(0.95, 0.95, 0.95, 0.5)`

background pane on 3D axes

axes3d.yaxis.panecolor: `(0.9, 0.9, 0.9, 0.5)`

background pane on 3D axes

axes3d.zaxis.panecolor: `(0.925, 0.925, 0.925, 0.5)`

background pane on 3D axes

axes3d.depthshade: `True`

depth shade for 3D scatter plots

axes3d.depthshade\_minalpha: `0.3`

minimum alpha value for depth shading

axes3d.mouserotationstyle: `'arcball'`

{azel, trackball, sphere, arcball} See also [https://matplotlib.org/stable/api/toolkits/mplot3d/view\_angles.html#rotation-with-mouse](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#rotation-with-mouse)

axes3d.trackballsize: `0.667`

trackball diameter, in units of the Axes bbox

axes3d.trackballborder: `0.2`

trackball border width, in units of the Axes bbox (only for 'sphere' and 'arcball' style)

Axis[#](https://matplotlib.org/stable/users/explain/configuration.html#axis "Link to this heading")

----------------------------------------------------------------------------------------------------

axes3d.snap\_rotation: `5.0`

Snap angle (in degrees) for 3D rotation when holding Control.

xaxis.labellocation: `'center'`

alignment of the xaxis label: {left, right, center}

yaxis.labellocation: `'center'`

alignment of the yaxis label: {bottom, top, center}

Dates[#](https://matplotlib.org/stable/users/explain/configuration.html#dates "Link to this heading")

------------------------------------------------------------------------------------------------------

Default properties for date tick labels. These are used by the [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
 when the appropriate time unit is detected.See [https://matplotlib.org/stable/api/dates\_api.html#date-formatters](https://matplotlib.org/stable/api/dates_api.html#date-formatters)
 for more information.

date.autoformatter.year: `'%Y'`

_no description_

date.autoformatter.month: `'%Y-%m'`

_no description_

date.autoformatter.day: `'%Y-%m-%d'`

_no description_

date.autoformatter.hour: `'%m-%d %H'`

_no description_

date.autoformatter.minute: `'%d %H:%M'`

_no description_

date.autoformatter.second: `'%H:%M:%S'`

_no description_

date.autoformatter.microsecond: `'%M:%S.%f'`

_no description_

date.epoch: `'1970-01-01T00:00:00'`

The reference date for Matplotlib's internal date representation. See [https://matplotlib.org/stable/gallery/ticks/date\_precision\_and\_epochs.html](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)

date.converter: `'auto'`

'auto', 'concise'

date.interval\_multiples: `True`

For auto converter whether to use interval\_multiples

Ticks[#](https://matplotlib.org/stable/users/explain/configuration.html#ticks "Link to this heading")

------------------------------------------------------------------------------------------------------

xtick.top: `False`

draw ticks on the top side

xtick.bottom: `True`

draw ticks on the bottom side

xtick.labeltop: `False`

draw label on the top

xtick.labelbottom: `True`

draw label on the bottom

xtick.major.size: `3.5`

major tick size in points

xtick.minor.size: `2.0`

minor tick size in points

xtick.major.width: `0.8`

major tick width in points

xtick.minor.width: `0.6`

minor tick width in points

xtick.major.pad: `3.5`

distance to major tick label in points

xtick.minor.pad: `3.4`

distance to the minor tick label in points

xtick.color: `'black'`

color of the ticks

xtick.labelcolor: `'inherit'`

color of the tick labels or inherit from xtick.color

xtick.labelsize: `'medium'`

font size of the tick labels

xtick.direction: `'out'`

direction: {in, out, inout}

xtick.minor.visible: `False`

visibility of minor ticks on x-axis

xtick.major.top: `True`

draw x axis top major ticks

xtick.major.bottom: `True`

draw x axis bottom major ticks

xtick.minor.top: `True`

draw x axis top minor ticks

xtick.minor.bottom: `True`

draw x axis bottom minor ticks

xtick.minor.ndivs: `'auto'`

number of minor ticks between the major ticks on x-axis

xtick.alignment: `'center'`

alignment of xticks

ytick.left: `True`

draw ticks on the left side

ytick.right: `False`

draw ticks on the right side

ytick.labelleft: `True`

draw tick labels on the left side

ytick.labelright: `False`

draw tick labels on the right side

ytick.major.size: `3.5`

major tick size in points

ytick.minor.size: `2.0`

minor tick size in points

ytick.major.width: `0.8`

major tick width in points

ytick.minor.width: `0.6`

minor tick width in points

ytick.major.pad: `3.5`

distance to major tick label in points

ytick.minor.pad: `3.4`

distance to the minor tick label in points

ytick.color: `'black'`

color of the ticks

ytick.labelcolor: `'inherit'`

color of the tick labels or inherit from ytick.color

ytick.labelsize: `'medium'`

font size of the tick labels

ytick.direction: `'out'`

direction: {in, out, inout}

ytick.minor.visible: `False`

visibility of minor ticks on y-axis

ytick.major.left: `True`

draw y axis left major ticks

ytick.major.right: `True`

draw y axis right major ticks

ytick.minor.left: `True`

draw y axis left minor ticks

ytick.minor.right: `True`

draw y axis right minor ticks

ytick.minor.ndivs: `'auto'`

number of minor ticks between the major ticks on y-axis

ytick.alignment: `'center_baseline'`

alignment of yticks

Grid[#](https://matplotlib.org/stable/users/explain/configuration.html#grid "Link to this heading")

----------------------------------------------------------------------------------------------------

grid.color: `'#b0b0b0'`

b0b0b0" # grid color

grid.linestyle: `'-'`

solid

grid.linewidth: `0.8`

in points

grid.alpha: `1.0`

transparency, between 0.0 and 1.0

grid.major.color: `None`

If None defaults to grid.color

grid.major.linestyle: `None`

If None defaults to grid.linestyle

grid.major.linewidth: `None`

If None defaults to grid.linewidth

grid.major.alpha: `None`

If None defaults to grid.alpha

grid.minor.color: `None`

If None defaults to grid.color

grid.minor.linestyle: `None`

If None defaults to grid.linestyle

grid.minor.linewidth: `None`

If None defaults to grid.linewidth

grid.minor.alpha: `None`

If None defaults to grid.alpha

Legend[#](https://matplotlib.org/stable/users/explain/configuration.html#legend "Link to this heading")

--------------------------------------------------------------------------------------------------------

legend.loc: `'best'`

_no description_

legend.frameon: `True`

if True, draw the legend on a background patch

legend.framealpha: `0.8`

legend patch transparency

legend.facecolor: `'inherit'`

inherit from axes.facecolor; or color spec

legend.edgecolor: `'0.8'`

background patch boundary color

legend.linewidth: `None`

line width of the legend frame, None means inherit from patch.linewidth

legend.fancybox: `True`

if True, use a rounded box for the legend background, else a rectangle

legend.shadow: `False`

if True, give background a shadow effect

legend.numpoints: `1`

the number of marker points in the legend line

legend.scatterpoints: `1`

number of scatter points

legend.markerscale: `1.0`

the relative size of legend markers vs. original

legend.fontsize: `'medium'`

_no description_

legend.labelcolor: `'None'`

_no description_

legend.title\_fontsize: `None`

None sets to the same as the default axes.

legend.borderpad: `0.4`

border whitespace

legend.labelspacing: `0.5`

the vertical space between the legend entries

legend.handlelength: `2.0`

the length of the legend lines

legend.handleheight: `0.7`

the height of the legend handle

legend.handletextpad: `0.8`

the space between the legend line and legend text

legend.borderaxespad: `0.5`

the border between the axes and legend edge

legend.columnspacing: `2.0`

column separation

Figure[#](https://matplotlib.org/stable/users/explain/configuration.html#figure "Link to this heading")

--------------------------------------------------------------------------------------------------------

figure.titlesize: `'large'`

size of the figure title (`Figure.suptitle()`)

figure.titleweight: `'normal'`

weight of the figure title

figure.labelsize: `'large'`

size of the figure label (`Figure.sup[x|y]label()`)

figure.labelweight: `'normal'`

weight of the figure label

figure.figsize: `[6.4, 4.8]`

figure size in inches

figure.dpi: `100.0`

figure dots per inch

figure.facecolor: `'white'`

figure face color

figure.edgecolor: `'white'`

figure edge color

figure.frameon: `True`

enable figure frame

figure.max\_open\_warning: `20`

The maximum number of figures to open through the pyplot interface before emitting a warning. If less than one this feature is disabled.

figure.raise\_window: `True`

Raise the GUI window to front when show() is called. If set to False, we currently do not take any further actions and whether the window appears on the front may depend on the GUI framework and window manager.

figure.subplot.left: `0.125`

the left side of the subplots of the figure

figure.subplot.right: `0.9`

the right side of the subplots of the figure

figure.subplot.bottom: `0.11`

the bottom of the subplots of the figure

figure.subplot.top: `0.88`

the top of the subplots of the figure

figure.subplot.wspace: `0.2`

the amount of width reserved for space between subplots, expressed as a fraction of the average axis width

figure.subplot.hspace: `0.2`

the amount of height reserved for space between subplots, expressed as a fraction of the average axis height

figure.autolayout: `False`

When True, automatically adjust subplot parameters to make the plot fit the figure using [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")

figure.constrained\_layout.use: `False`

When True, automatically make plot elements fit on the figure. (Not compatible with "figure.autolayout", above).

figure.constrained\_layout.h\_pad: `0.04167`

Padding (in inches) around axes; defaults to 3/72 inches, i.e. 3 points

figure.constrained\_layout.w\_pad: `0.04167`

Padding (in inches) around axes; defaults to 3/72 inches, i.e. 3 points

figure.constrained\_layout.hspace: `0.02`

Spacing between subplots, relative to the subplot sizes. Much smaller than for tight\_layout (figure.subplot.hspace, figure.subplot.wspace) as constrained\_layout already takes surrounding texts (titles, labels, # ticklabels) into account.

figure.constrained\_layout.wspace: `0.02`

Spacing between subplots, relative to the subplot sizes. Much smaller than for tight\_layout (figure.subplot.hspace, figure.subplot.wspace) as constrained\_layout already takes surrounding texts (titles, labels, # ticklabels) into account.

Images[#](https://matplotlib.org/stable/users/explain/configuration.html#images "Link to this heading")

--------------------------------------------------------------------------------------------------------

image.aspect: `'equal'`

{equal, auto} or a number

image.interpolation: `'auto'`

see help(imshow) for options

image.interpolation\_stage: `'auto'`

see help(imshow) for options

image.cmap: `'viridis'`

A colormap name (plasma, magma, etc.)

image.lut: `256`

the size of the colormap lookup table

image.origin: `'upper'`

{lower, upper}

image.resample: `True`

_no description_

image.composite\_image: `True`

When True, all the images on a set of axes are combined into a single composite image before saving a figure as a vector graphics file, such as a PDF.

Contour plots[#](https://matplotlib.org/stable/users/explain/configuration.html#contour-plots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

contour.negative\_linestyle: `'dashed'`

string or on-off ink sequence

contour.corner\_mask: `True`

{True, False}

contour.linewidth: `None`

{float, None} Size of the contour line widths. If set to None, it falls back to "line.linewidth".

contour.algorithm: `'mpl2014'`

{mpl2005, mpl2014, serial, threaded}

Errorbar plots[#](https://matplotlib.org/stable/users/explain/configuration.html#errorbar-plots "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

errorbar.capsize: `0.0`

length of end cap on error bars in pixels

errorbar.capthick: `None`

thickness of end cap on error bars in points.

errorbar.elinewidth: `None`

line width of the error bar lines in points.

Histogram plots[#](https://matplotlib.org/stable/users/explain/configuration.html#histogram-plots "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

hist.bins: `10`

The default number of histogram bins or 'auto'.

Scatter plots[#](https://matplotlib.org/stable/users/explain/configuration.html#scatter-plots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

scatter.marker: `'o'`

The default marker type for scatter plots.

scatter.edgecolors: `'face'`

The default edge colors for scatter plots.

AGG rendering[#](https://matplotlib.org/stable/users/explain/configuration.html#agg-rendering "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

agg.path.chunksize: `0`

0 to disable; values in the range 10000 to 100000 can improve speed slightly and prevent an Agg rendering failure when plotting very large data sets, especially if they are very gappy. It may cause minor artifacts, though. A value of 20000 is probably a good starting point.

Paths[#](https://matplotlib.org/stable/users/explain/configuration.html#paths "Link to this heading")

------------------------------------------------------------------------------------------------------

path.simplify: `True`

When True, simplify paths by removing "invisible" points to reduce file size and increase rendering speed

path.simplify\_threshold: `0.111111111111`

The threshold of similarity below which vertices will be removed in the simplification process.

path.snap: `True`

When True, rectilinear axis-aligned paths will be snapped to the nearest pixel when certain criteria are met. When False, paths will never be snapped.

path.sketch: `None`

May be None, or a tuple of the form:path.sketch: (scale, length, randomness)- _scale_ is the amplitude of the wiggle perpendicular to the line (in pixels).- _length_ is the length of the wiggle along the line (in pixels).- _randomness_ is the factor by which the length is randomly scaled.

path.effects: `[]`

_no description_

Saving figures[#](https://matplotlib.org/stable/users/explain/configuration.html#saving-figures "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

savefig.dpi: `'figure'`

figure dots per inch or 'figure'

savefig.facecolor: `'auto'`

figure face color when saving

savefig.edgecolor: `'auto'`

figure edge color when saving

savefig.format: `'png'`

{png, ps, pdf, svg}

savefig.bbox: `None`

{tight, standard} 'tight' is incompatible with generating frames for animation

savefig.pad\_inches: `0.1`

padding to be used, when bbox is set to 'tight'

savefig.directory: `'~'`

default directory in savefig dialog, gets updated after interactive saves, unless set to the empty string (i.e. the current directory); use '.' to start at the current directory but update after interactive saves

savefig.transparent: `False`

whether figures are saved with a transparent background by default

savefig.orientation: `'portrait'`

orientation of saved figure, for PostScript output only

### Mac OSX backend parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#mac-osx-backend-parameters "Link to this heading")

macosx.window\_mode: `'system'`

How to open new figures (system, tab, window) system uses the MacOS system preferences

### Tk backend parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#tk-backend-parameters "Link to this heading")

tk.window\_focus: `False`

Maintain shell focus for TkAgg

### PS backend parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#ps-backend-parameters "Link to this heading")

ps.papersize: `'letter'`

{figure, letter, legal, ledger, A0-A10, B0-B10}

ps.useafm: `False`

use AFM fonts, results in small files

ps.usedistiller: `None`

{ghostscript, xpdf, None} Experimental: may produce smaller files. xpdf intended for production of publication quality files, but requires ghostscript, xpdf and ps2eps

ps.distiller.res: `6000`

dpi

ps.fonttype: `3`

Output Type 3 (Type3) or Type 42 (TrueType)

### PDF backend parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#pdf-backend-parameters "Link to this heading")

pdf.compression: `6`

integer from 0 to 9 0 disables compression (good for debugging)

pdf.fonttype: `3`

Output Type 3 (Type3) or Type 42 (TrueType)

pdf.use14corefonts: `False`

_no description_

pdf.inheritcolor: `False`

_no description_

### SVG backend parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#svg-backend-parameters "Link to this heading")

svg.image\_inline: `True`

Write raster image data directly into the SVG file

svg.fonttype: `'path'`

How to handle SVG fonts: path: Embed characters as paths -- supported by most SVG renderersnone: Assume fonts are installed on the machine where the SVG will be viewed.

svg.hashsalt: `None`

If not None, use this string as hash salt instead of uuid4

svg.id: `None`

If not None, use this string as the value for the [`id`](https://docs.python.org/3/library/functions.html#id "(in Python v3.14)")
 attribute in the top <svg> tag

### PGF parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#pgf-parameters "Link to this heading")

pgf.rcfonts: `True`

_no description_

pgf.preamble: `''`

See text.latex.preamble for documentation

pgf.texsystem: `'xelatex'`

_no description_

### Docstring parameters[#](https://matplotlib.org/stable/users/explain/configuration.html#docstring-parameters "Link to this heading")

docstring.hardcopy: `False`

set this when you want to generate hardcopy docstring

Interactive keymaps[#](https://matplotlib.org/stable/users/explain/configuration.html#interactive-keymaps "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Default key mappings for interactive navigation. See [Navigation keyboard shortcuts](https://matplotlib.org/stable/users/explain/figure/interactive.html#key-event-handling)
.

keymap.fullscreen: `['f', 'ctrl+f']`

toggling

keymap.home: `['h', 'r', 'home']`

home or reset mnemonic

keymap.back: `['left', 'c', 'backspace', 'MouseButton.BACK']`

forward / backward keys

keymap.forward: `['right', 'v', 'MouseButton.FORWARD']`

for quick navigation

keymap.pan: `['p']`

pan mnemonic

keymap.zoom: `['o']`

zoom mnemonic

keymap.save: `['s', 'ctrl+s']`

saving current figure

keymap.help: `['f1']`

display help about active tools

keymap.quit: `['ctrl+w', 'cmd+w', 'q']`

close the current figure

keymap.quit\_all: `[]`

close all figures

keymap.grid: `['g']`

switching on/off major grids in current axes

keymap.grid\_minor: `['G']`

switching on/off minor grids in current axes

keymap.yscale: `['l']`

toggle scaling of y-axes ('log'/'linear')

keymap.xscale: `['k', 'L']`

toggle scaling of x-axes ('log'/'linear')

keymap.copy: `['ctrl+c', 'cmd+c']`

copy figure to clipboard

Animation[#](https://matplotlib.org/stable/users/explain/configuration.html#animation "Link to this heading")

--------------------------------------------------------------------------------------------------------------

animation.html: `'none'`

How to display the animation as HTML in the IPython notebook: - 'html5' uses HTML5 video tag - 'jshtml' creates a JavaScript animation

animation.writer: `'ffmpeg'`

MovieWriter 'backend' to use

animation.codec: `'h264'`

Codec to use for writing movie

animation.bitrate: `-1`

Controls size/quality trade-off for movie. -1 implies let utility auto-determine

animation.frame\_format: `'png'`

Controls frame format used by temp files

animation.ffmpeg\_path: `'ffmpeg'`

Path to ffmpeg binary. Unqualified paths are resolved by subprocess.Popen.

animation.ffmpeg\_args: `[]`

Additional arguments to pass to ffmpeg

animation.convert\_path: `'convert'`

Path to ImageMagick's convert binary. Unqualified paths are resolved by subprocess.Popen, except that on Windows, we look up an install of ImageMagick in the registry (as convert is also the name of a system tool).

animation.convert\_args: `['-layers', 'OptimizePlus']`

Additional arguments to pass to convert

animation.embed\_limit: `20.0`

Limit, in MB, of size of base64 encoded animation in HTML (i.e. IPython notebook)

backend: `None`

_no description_

[`Download Jupyter notebook: configuration.ipynb`](https://matplotlib.org/stable/_downloads/8d9e5801a95b7e1d5c79cf8dddffca68/configuration.ipynb)

[`Download Python source code: configuration.py`](https://matplotlib.org/stable/_downloads/26ceb9bd4ed786cc8334722f293d9fc8/configuration.py)

[`Download zipped: configuration.zip`](https://matplotlib.org/stable/_downloads/6de9b53f8d019a64e238a3a6fc421cb5/configuration.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page