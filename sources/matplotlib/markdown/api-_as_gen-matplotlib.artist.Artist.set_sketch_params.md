[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#main-content)

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
    

matplotlib.artist.Artist.set\_sketch\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib-artist-artist-set-sketch-params "Link to this heading")

=============================================================================================================================================================================================================

Artist.set\_sketch\_params(_scale\=None_, _length\=None_, _randomness\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L710-L736)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "Link to this definition")

Set the sketch parameters.

Parameters:

**scale**float, optional

The amplitude of the wiggle perpendicular to the source line, in pixels. If scale is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, or not provided, no sketch filter will be provided.

**length**float, optional

The length of the wiggle along the line, in pixels (default 128.0)

**randomness**float, optional

The scale factor by which the length is shrunken or expanded (default 16.0)

The PGF backend uses this argument as an RNG seed and not as described above. Using the same seed yields the same random shape.

On this page