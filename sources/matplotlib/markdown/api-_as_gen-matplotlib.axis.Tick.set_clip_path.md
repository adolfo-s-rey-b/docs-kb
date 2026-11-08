[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_clip_path.html#main-content)

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
    

matplotlib.axis.Tick.set\_clip\_path[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_clip_path.html#matplotlib-axis-tick-set-clip-path "Link to this heading")

=====================================================================================================================================================================================

Tick.set\_clip\_path(_path_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L252-L256)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_clip_path.html#matplotlib.axis.Tick.set_clip_path "Link to this definition")

Set the artist's clip path.

Parameters:

**path**[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 or [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 or [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 or None

The clip path. If given a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, _transform_ must be provided as well. If _None_, a previously set clip path is removed.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

Only used if _path_ is a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, in which case the given [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 is converted to a [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 using _transform_.

Notes

For efficiency, if _path_ is a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 this method will set the clipping box to the corresponding rectangle and set the clipping path to `None`.

For technical reasons (support of [`set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
), a tuple (_path_, _transform_) is also accepted as a single positional parameter.

On this page