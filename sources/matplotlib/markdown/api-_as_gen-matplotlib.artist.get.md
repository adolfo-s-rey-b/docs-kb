[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.get.html#main-content)

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
    

matplotlib.artist.get[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.get.html#matplotlib-artist-get "Link to this heading")

============================================================================================================================================

matplotlib.artist.get(_obj_, _property\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1792-L1825)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.get.html#matplotlib.artist.get "Link to this definition")

Return the value of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
's _property_, or print all of them.

Parameters:

**obj**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The queried artist; e.g., a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, or an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

**property**str or None, default: None

If _property_ is 'somename', this function returns `obj.get_somename()`.

If it's None (or unset), it _prints_ all gettable properties from _obj_. Many properties have aliases for shorter typing, e.g. 'lw' is an alias for 'linewidth'. In the output, aliases and full property names will be listed as:

> property or alias = value

e.g.:

> linewidth or lw = 2

See also

[`setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")

On this page