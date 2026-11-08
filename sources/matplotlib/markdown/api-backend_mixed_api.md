[Skip to main content](https://matplotlib.org/stable/api/backend_mixed_api.html#main-content)

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
    

`matplotlib.backends.backend_mixed`[#](https://matplotlib.org/stable/api/backend_mixed_api.html#module-matplotlib.backends.backend_mixed "Link to this heading")

=================================================================================================================================================================

class matplotlib.backends.backend\_mixed.MixedModeRenderer(_figure_, _width_, _height_, _dpi_, _vector\_renderer_, _raster\_renderer\_class\=None_, _bbox\_inches\_restore\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_mixed.py#L8-L122)
[#](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A helper class to implement a renderer that switches between vector and raster drawing. An example may be a PDF writer, where most things are drawn with PDF vector commands, but some very complex objects, such as quad meshes, are rasterised and then output as images.

Parameters:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure instance.

**width**float

The width of the canvas in logical units

**height**float

The height of the canvas in logical units

**dpi**float

The dpi of the canvas

**vector\_renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

An instance of a subclass of [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 that will be used for the vector drawing.

**raster\_renderer\_class**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

The renderer class to use for the raster drawing. If not provided, this will use the Agg backend (which is currently the only viable option anyway.)

start\_rasterizing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_mixed.py#L71-L87)
[#](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.start_rasterizing "Link to this definition")

Enter "raster" mode. All subsequent drawing commands (until [`stop_rasterizing`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.stop_rasterizing "matplotlib.backends.backend_mixed.MixedModeRenderer.stop_rasterizing")
 is called) will be drawn with the raster backend.

stop\_rasterizing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_mixed.py#L89-L122)
[#](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.stop_rasterizing "Link to this definition")

Exit "raster" mode. All of the drawing that was done since the last [`start_rasterizing`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.start_rasterizing "matplotlib.backends.backend_mixed.MixedModeRenderer.start_rasterizing")
 call will be copied to the vector backend by calling draw\_image.

On this page