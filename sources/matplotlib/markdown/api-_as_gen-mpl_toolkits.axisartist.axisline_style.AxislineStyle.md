[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#main-content)

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
    

mpl\_toolkits.axisartist.axisline\_style.AxislineStyle[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl-toolkits-axisartist-axisline-style-axislinestyle "Link to this heading")

===========================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.axisline\_style.AxislineStyle(_stylename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L93-L192)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle "Link to this definition")

Bases: `_Style`

A container class which defines style classes for AxisArtists.

An instance of any axisline style class is a callable object, whose call signature is

\_\_call\_\_(self, axis\_artist, path, transform)

When called, this should return an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 with the following methods:

def set\_path(self, path):
    \# set the path for axisline.

def set\_line\_mutation\_scale(self, scale):
    \# set the scale

def draw(self, renderer):
    \# draw

Return the instance of the subclass with the given style name.

class FilledArrow(_size\=1_, _facecolor\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L161-L190)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.FilledArrow "Link to this definition")

Bases: [`SimpleArrow`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.SimpleArrow "mpl_toolkits.axisartist.axisline_style.AxislineStyle.SimpleArrow")

An arrow with a filled head.

Parameters:

**size**float

Size of the arrow as a fraction of the ticklabel size.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: `[rcParams["axes.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.edgecolor#rcparam-axes-edgecolor) ` (default: `'black'`)

Fill color.

Added in version 3.7.

ArrowAxisClass[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L82-L90)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.FilledArrow.ArrowAxisClass "Link to this definition")

alias of `FilledArrow`

new\_line(_axis\_artist_, _transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L185-L190)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.FilledArrow.new_line "Link to this definition")

class SimpleArrow(_size\=1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L134-L157)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.SimpleArrow "Link to this definition")

Bases: `_Base`

A simple arrow.

Parameters:

**size**float

Size of the arrow as a fraction of the ticklabel size.

ArrowAxisClass[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L15-L80)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.SimpleArrow.ArrowAxisClass "Link to this definition")

alias of `SimpleArrow`

new\_line(_axis\_artist_, _transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axisline_style.py#L152-L157)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.AxislineStyle.html#mpl_toolkits.axisartist.axisline_style.AxislineStyle.SimpleArrow.new_line "Link to this definition")

On this page