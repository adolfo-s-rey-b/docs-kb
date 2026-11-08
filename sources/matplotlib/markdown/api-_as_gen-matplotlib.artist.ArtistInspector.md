[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#main-content)

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
    

matplotlib.artist.ArtistInspector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib-artist-artistinspector "Link to this heading")

================================================================================================================================================================================

class matplotlib.artist.ArtistInspector(_o_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1490-L1789)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A helper class to inspect an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 and return information about its settable properties and their current values.

Initialize the artist inspector with an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or an iterable of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s. If an iterable is used, we assume it is a homogeneous sequence (all [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s are of the same type) and it is your responsibility to make sure this is so.

aliased\_name(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1632-L1641)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.aliased_name "Link to this definition")

Return 'PROPNAME or alias' if _s_ has an alias, else return 'PROPNAME'.

For example, for the line markerfacecolor property, which has an alias, return 'markerfacecolor or mfc' and for the transform property, which does not, return 'transform'.

aliased\_name\_rest(_s_, _target_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1659-L1674)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.aliased_name_rest "Link to this definition")

Return 'PROPNAME or alias' if _s_ has an alias, else return 'PROPNAME', formatted for reST.

For example, for the line markerfacecolor property, which has an alias, return 'markerfacecolor or mfc' and for the transform property, which does not, return 'transform'.

get\_aliases()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1516-L1538)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_aliases "Link to this definition")

Get a dict mapping property fullnames to sets of aliases for each alias in the [`ArtistInspector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector "matplotlib.artist.ArtistInspector")
.

e.g., for lines:

{'markerfacecolor': {'mfc'},
 'linewidth'      : {'lw'},
}

get\_setters()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1594-L1611)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_setters "Link to this definition")

Get the attribute strings with setters for object.

For example, for a line, return `['markerfacecolor', 'linewidth', ....]`.

get\_valid\_values(_attr_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1544-L1581)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_valid_values "Link to this definition")

Get the legal arguments for the setter associated with _attr_.

This is done by querying the docstring of the setter for a line that begins with "ACCEPTS:" or ".. ACCEPTS:", and then by looking for a numpydoc-style documentation for the setter's first argument.

static is\_alias(_method_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1619-L1630)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.is_alias "Link to this definition")

Return whether the object _method_ is an alias for another method.

static number\_of\_parameters(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1613-L1617)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.number_of_parameters "Link to this definition")

Return number of parameters of the callable _func_.

pprint\_getters()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1776-L1789)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_getters "Link to this definition")

Return the getters and actual values as list of strings.

pprint\_setters(_prop\=None_, _leadingspace\=2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1676-L1698)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_setters "Link to this definition")

If _prop_ is _None_, return a list of strings of all settable properties and their valid values.

If _prop_ is not _None_, it is a valid property name and that property will be returned as a string of property : valid values.

pprint\_setters\_rest(_prop\=None_, _leadingspace\=4_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1700-L1753)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_setters_rest "Link to this definition")

If _prop_ is _None_, return a list of reST-formatted strings of all settable properties and their valid values.

If _prop_ is not _None_, it is a valid property name and that property will be returned as a string of "property : valid" values.

properties()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1755-L1774)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.properties "Link to this definition")

Return a dictionary mapping property name -> value.

On this page