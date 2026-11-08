[Skip to main content](https://matplotlib.org/stable/api/legend_handler_api.html#main-content)

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
    

`matplotlib.legend_handler`[#](https://matplotlib.org/stable/api/legend_handler_api.html#module-matplotlib.legend_handler "Link to this heading")

==================================================================================================================================================

Default legend handlers.

Important

This is a low-level legend API, which most end users do not need.

We recommend that you are familiar with the [legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 before reading this documentation.

Legend handlers are expected to be a callable object with a following signature:

legend\_handler(legend, orig\_handle, fontsize, handlebox)

Where _legend_ is the legend itself, _orig\_handle_ is the original plot, _fontsize_ is the fontsize in pixels, and _handlebox_ is an [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 instance. Within the call, you should create relevant artists (using relevant properties from the _legend_ and/or _orig\_handle_) and add them into the _handlebox_. The artists need to be scaled according to the _fontsize_ (note that the size is in pixels, i.e., this is dpi-scaled value).

This module includes definition of several legend handler classes derived from the base class (HandlerBase) with the following method:

def legend\_artist(self, legend, orig\_handle, fontsize, handlebox)

class matplotlib.legend\_handler.HandlerBase(_xpad\=0.0_, _ypad\=0.0_, _update\_func\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L46-L163)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "Link to this definition")

A base class for default legend handlers.

The derived classes are meant to override _create\_artists_ method, which has the following signature:

def create\_artists(self, legend, orig\_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):

The overridden method needs to create artists of the given transform that fits in the given dimension (xdescent, ydescent, width, height) that are scaled by fontsize if necessary.

Parameters:

**xpad**float, optional

Padding in x-direction.

**ypad**float, optional

Padding in y-direction.

**update\_func**callable, optional

Function for updating the legend handler properties from another legend handler, used by [`update_prop`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.update_prop "matplotlib.legend_handler.HandlerBase.update_prop")
.

adjust\_drawing\_area(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L94-L101)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.adjust_drawing_area "Link to this definition")

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L140-L163)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

legend\_artist(_legend_, _orig\_handle_, _fontsize_, _handlebox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L103-L138)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.legend_artist "Link to this definition")

Return the artist that this HandlerBase generates for the given original artist/handle.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`matplotlib.artist.Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**fontsize**int

The fontsize in pixels. The artists being created should be scaled according to the given fontsize.

**handlebox**[`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

The box which has been created to hold this legend entry's artists. Artists created in the [`legend_artist`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.legend_artist "matplotlib.legend_handler.HandlerBase.legend_artist")
 method must be added to this handlebox inside this method.

update\_prop(_legend\_handle_, _orig\_handle_, _legend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L86-L92)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.update_prop "Link to this definition")

class matplotlib.legend\_handler.HandlerCircleCollection(_yoffsets\=None_, _sizes\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L513-L518)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerCircleCollection "Link to this definition")

Handler for [`CircleCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.CircleCollection "matplotlib.collections.CircleCollection")
s.

Parameters:

**numpoints**int

Number of points to show in legend entry.

**yoffsets**array of floats

Length _numpoints_ list of y offsets for each point in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerNpoints`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints "matplotlib.legend_handler.HandlerNpoints")
.

create\_collection(_orig\_handle_, _sizes_, _offsets_, _offset\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L516-L518)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerCircleCollection.create_collection "Link to this definition")

class matplotlib.legend\_handler.HandlerErrorbar(_xerr\_size\=0.5_, _yerr\_size\=None_, _marker\_pad\=0.3_, _numpoints\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L521-L625)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerErrorbar "Link to this definition")

Handler for Errorbars.

Parameters:

**marker\_pad**float

Padding between points in legend entry.

**numpoints**int

Number of points to show in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L543-L625)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerErrorbar.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

get\_err\_size(_legend_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L532-L541)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerErrorbar.get_err_size "Link to this definition")

class matplotlib.legend\_handler.HandlerLine2D(_marker\_pad\=0.3_, _numpoints\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L275-L311)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "Link to this definition")

Handler for [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances.

See also

[`HandlerLine2DCompound`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2DCompound "matplotlib.legend_handler.HandlerLine2DCompound")

An earlier handler implementation, which used one artist for the line and another for the marker(s).

Parameters:

**marker\_pad**float

Padding between points in legend entry.

**numpoints**int

Number of points to show in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L285-L311)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

class matplotlib.legend\_handler.HandlerLine2DCompound(_marker\_pad\=0.3_, _numpoints\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L238-L272)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2DCompound "Link to this definition")

Original handler for [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances, that relies on combining a line-only with a marker-only artist. May be deprecated in the future.

Parameters:

**marker\_pad**float

Padding between points in legend entry.

**numpoints**int

Number of points to show in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L244-L272)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2DCompound.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

class matplotlib.legend\_handler.HandlerLineCollection(_marker\_pad\=0.3_, _numpoints\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L398-L427)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection "Link to this definition")

Handler for [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 instances.

Parameters:

**marker\_pad**float

Padding between points in legend entry.

**numpoints**int

Number of points to show in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L416-L427)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

get\_numpoints(_legend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L402-L406)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection.get_numpoints "Link to this definition")

class matplotlib.legend\_handler.HandlerNpoints(_marker\_pad\=0.3_, _numpoints\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L166-L205)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints "Link to this definition")

A legend handler that shows _numpoints_ points in the legend entry.

Parameters:

**marker\_pad**float

Padding between points in legend entry.

**numpoints**int

Number of points to show in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

get\_numpoints(_legend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L187-L191)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints.get_numpoints "Link to this definition")

get\_xdata(_legend_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L193-L205)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints.get_xdata "Link to this definition")

class matplotlib.legend\_handler.HandlerNpointsYoffsets(_numpoints\=None_, _yoffsets\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L208-L235)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpointsYoffsets "Link to this definition")

A legend handler that shows _numpoints_ in the legend, and allows them to be individually offset in the y-direction.

Parameters:

**numpoints**int

Number of points to show in legend entry.

**yoffsets**array of floats

Length _numpoints_ list of y offsets for each point in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerNpoints`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints "matplotlib.legend_handler.HandlerNpoints")
.

get\_ydata(_legend_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L229-L235)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpointsYoffsets.get_ydata "Link to this definition")

class matplotlib.legend\_handler.HandlerPatch(_patch\_func\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L314-L358)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPatch "Link to this definition")

Handler for [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 instances.

Parameters:

**patch\_func**callable, optional

The function that creates the legend key artist. _patch\_func_ should have the signature:

def patch\_func(legend\=legend, orig\_handle\=orig\_handle,
               xdescent\=xdescent, ydescent\=ydescent,
               width\=width, height\=height, fontsize\=fontsize)

Subsequently, the created artist will have its `update_prop` method called and the appropriate transform will be applied.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L351-L358)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPatch.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

class matplotlib.legend\_handler.HandlerPathCollection(_yoffsets\=None_, _sizes\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L503-L510)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPathCollection "Link to this definition")

Handler for [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
s, which are used by [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
.

Parameters:

**numpoints**int

Number of points to show in legend entry.

**yoffsets**array of floats

Length _numpoints_ list of y offsets for each point in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerNpoints`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints "matplotlib.legend_handler.HandlerNpoints")
.

create\_collection(_orig\_handle_, _sizes_, _offsets_, _offset\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L506-L510)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPathCollection.create_collection "Link to this definition")

class matplotlib.legend\_handler.HandlerPolyCollection(_xpad\=0.0_, _ypad\=0.0_, _update\_func\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L772-L811)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPolyCollection "Link to this definition")

Handler for [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 used in [`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 and [`stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
.

Parameters:

**xpad**float, optional

Padding in x-direction.

**ypad**float, optional

Padding in y-direction.

**update\_func**callable, optional

Function for updating the legend handler properties from another legend handler, used by [`update_prop`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.update_prop "matplotlib.legend_handler.HandlerBase.update_prop")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L804-L811)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPolyCollection.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

class matplotlib.legend\_handler.HandlerRegularPolyCollection(_yoffsets\=None_, _sizes\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L430-L500)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection "Link to this definition")

Handler for [`RegularPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
s.

Parameters:

**numpoints**int

Number of points to show in legend entry.

**yoffsets**array of floats

Length _numpoints_ list of y offsets for each point in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerNpoints`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpoints "matplotlib.legend_handler.HandlerNpoints")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L481-L500)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

create\_collection(_orig\_handle_, _sizes_, _offsets_, _offset\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L474-L479)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection.create_collection "Link to this definition")

get\_numpoints(_legend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L438-L442)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection.get_numpoints "Link to this definition")

get\_sizes(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L444-L463)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection.get_sizes "Link to this definition")

update\_prop(_legend\_handle_, _orig\_handle_, _legend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L465-L472)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerRegularPolyCollection.update_prop "Link to this definition")

class matplotlib.legend\_handler.HandlerStem(_marker\_pad\=0.3_, _numpoints\=None_, _bottom\=None_, _yoffsets\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L628-L716)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerStem "Link to this definition")

Handler for plots produced by [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
.

Parameters:

**marker\_pad**float, default: 0.3

Padding between points in legend entry.

**numpoints**int, optional

Number of points to show in legend entry.

**bottom**float, optional

**yoffsets**array of floats, optional

Length _numpoints_ list of y offsets for each point in legend entry.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerNpointsYoffsets`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerNpointsYoffsets "matplotlib.legend_handler.HandlerNpointsYoffsets")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L662-L708)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerStem.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

get\_ydata(_legend_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L654-L660)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerStem.get_ydata "Link to this definition")

class matplotlib.legend\_handler.HandlerStepPatch(_xpad\=0.0_, _ypad\=0.0_, _update\_func\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L361-L395)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerStepPatch "Link to this definition")

Handler for [`StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
 instances.

Parameters:

**xpad**float, optional

Padding in x-direction.

**ypad**float, optional

Padding in y-direction.

**update\_func**callable, optional

Function for updating the legend handler properties from another legend handler, used by [`update_prop`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.update_prop "matplotlib.legend_handler.HandlerBase.update_prop")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L385-L395)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerStepPatch.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

class matplotlib.legend\_handler.HandlerTuple(_ndivide\=1_, _pad\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L719-L769)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "Link to this definition")

Handler for Tuple.

Parameters:

**ndivide**int or None, default: 1

The number of sections to divide the legend area into. If None, use the length of the input tuple.

**pad**float, default: `[rcParams["legend.borderpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.borderpad#rcparam-legend-borderpad) ` (default: `0.4`)

Padding in units of fraction of font size.

**\*\*kwargs**

Keyword arguments forwarded to [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
.

create\_artists(_legend_, _orig\_handle_, _xdescent_, _ydescent_, _width_, _height_, _fontsize_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L740-L769)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple.create_artists "Link to this definition")

Return the legend artists generated.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The legend for which these legend artists are being created.

**orig\_handle**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or similar

The object for which these legend artists are being created.

**xdescent, ydescent, width, height**int

The rectangle (_xdescent_, _ydescent_, _width_, _height_) that the legend artists being created should fit within.

**fontsize**int

The fontsize in pixels. The legend artists being created should be scaled according to the given fontsize.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform that is applied to the legend artists being created. Typically from unit coordinates in the handler box to screen coordinates.

matplotlib.legend\_handler.update\_from\_first\_child(_tgt_, _src_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend_handler.py#L40-L43)
[#](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.update_from_first_child "Link to this definition")

On this page