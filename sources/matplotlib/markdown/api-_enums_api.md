[Skip to main content](https://matplotlib.org/stable/api/_enums_api.html#main-content)

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
    

`matplotlib._enums`[#](https://matplotlib.org/stable/api/_enums_api.html#module-matplotlib._enums "Link to this heading")

==========================================================================================================================

Enums representing sets of strings that Matplotlib uses as input parameters.

Matplotlib often uses simple data types like strings or tuples to define a concept; e.g. the line capstyle can be specified as one of 'butt', 'round', or 'projecting'. The classes in this module are used internally and serve to document these concepts formally.

As an end-user you will not use these classes directly, but only the values they define.

class matplotlib.\_enums.JoinStyle(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_enums.py#L17-L101)
[#](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "Link to this definition")

Define how the connection between two line segments is drawn.

For a visual impression of each _JoinStyle_, [`view these docs online`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
, or run [`JoinStyle.demo`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle.demo "matplotlib._enums.JoinStyle.demo")
.

Lines in Matplotlib are typically defined by a 1D [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 and a finite `linewidth`, where the underlying 1D [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 represents the center of the stroked line.

By default, [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 defines the boundaries of a stroked line to simply be every point within some radius, `linewidth/2`, away from any point of the center line. However, this results in corners appearing "rounded", which may not be the desired behavior if you are drawing, for example, a polygon or pointed star.

**Supported values:**

'miter'

the "arrow-tip" style. Each boundary of the filled-in area will extend in a straight line parallel to the tangent vector of the centerline at the point it meets the corner, until they meet in a sharp point.

'round'

stokes every point within a radius of `linewidth/2` of the center lines.

'bevel'

the "squared-off" style. It can be thought of as a rounded corner where the "circular" part of the corner has been cut off.

Note

Very long miter tips are cut off (to form a _bevel_) after a backend-dependent limit called the "miter limit", which specifies the maximum allowed ratio of miter length to line width. For example, the PDF backend uses the default value of 10 specified by the PDF standard, while the SVG backend does not even specify the miter limit, resulting in a default value of 4 per the SVG specification. Matplotlib does not currently allow the user to adjust this parameter.

A more detailed description of the effect of a miter limit can be found in the [Mozilla Developer Docs](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-miterlimit)

([`Source code`](https://matplotlib.org/stable/_downloads/a767b3522d485612a385152a693c30a5/_enums_api-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/87490f189f9047700c7e958bfc89ec6e/_enums_api-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7f1ba2b30a0bb4e49c2850a31a0412c6/_enums_api-1.png)
)

[![Demo of possible JoinStyle's](https://matplotlib.org/stable/_images/api-_enums_api-1.2x.png)](https://matplotlib.org/stable/_images/api-_enums_api-1.2x.png)

static demo()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_enums.py#L76-L101)
[#](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle.demo "Link to this definition")

Demonstrate how each JoinStyle looks for various join angles.

class matplotlib.\_enums.CapStyle(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_enums.py#L109-L167)
[#](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "Link to this definition")

Define how the two endpoints (caps) of an unclosed line are drawn.

How to draw the start and end points of lines that represent a closed curve (i.e. that end in a [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
) is controlled by the line's [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
. For all other lines, how the start and end points are drawn is controlled by the _CapStyle_.

For a visual impression of each _CapStyle_, [`view these docs online`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or run [`CapStyle.demo`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle.demo "matplotlib._enums.CapStyle.demo")
.

By default, [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 draws a stroked line as squared off at its endpoints.

**Supported values:**

'butt'

the line is squared off at its endpoint.

'projecting'

the line is squared off as in _butt_, but the filled in area extends beyond the endpoint a distance of `linewidth/2`.

'round'

like _butt_, but a semicircular cap is added to the end of the line, of radius `linewidth/2`.

([`Source code`](https://matplotlib.org/stable/_downloads/3cfb8ad256cb73cd5348f0ae6fc1d910/_enums_api-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b1fae3869f60948b188df0c4b0be835a/_enums_api-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8428af7349869d5dabcaf3e2284c5853/_enums_api-2.png)
)

[![Demo of possible CapStyle's](https://matplotlib.org/stable/_images/api-_enums_api-2.2x.png)](https://matplotlib.org/stable/_images/api-_enums_api-2.2x.png)

static demo()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_enums.py#L148-L167)
[#](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle.demo "Link to this definition")

Demonstrate how each CapStyle looks for a thick line segment.

On this page