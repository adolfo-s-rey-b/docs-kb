[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_sketch_params.html#main-content)

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
    

matplotlib.artist.Artist.get\_sketch\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_sketch_params.html#matplotlib-artist-artist-get-sketch-params "Link to this heading")

=============================================================================================================================================================================================================

Artist.get\_sketch\_params()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L690-L708)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_sketch_params.html#matplotlib.artist.Artist.get_sketch_params "Link to this definition")

Return the sketch parameters for the artist.

Returns:

tuple or None

A 3-tuple with the following elements:

*   _scale_: The amplitude of the wiggle perpendicular to the source line.
    
*   _length_: The length of the wiggle along the line.
    
*   _randomness_: The scale factor by which the length is shrunken or expanded.
    

Returns _None_ if no sketch parameters were set.

On this page