[Skip to main content](https://matplotlib.org/stable/api/cm_api.html#main-content)

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
    

`matplotlib.cm`[#](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "Link to this heading")

==============================================================================================================

Builtin colormaps, colormap handling utilities, and the [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 mixin.

See also

[Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
 for a list of builtin colormaps.

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
 for examples of how to make colormaps.

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
 an in-depth discussion of choosing colormaps.

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)
 for more details about data normalization.

class matplotlib.cm.ColormapRegistry(_cmaps_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py#L66-L233)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "Link to this definition")

Bases: [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")

Container for colormaps that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. There should be no need for users to instantiate [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 themselves.

Read access uses a dict-like interface mapping names to [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s:

import matplotlib as mpl
cmap \= mpl.colormaps\['viridis'\]

Returned [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s are copies, so that their modification does not change the global definition of the colormap.

Additional colormaps can be added via [`ColormapRegistry.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
:

mpl.colormaps.register(my\_colormap)

To get a list of all registered colormaps, you can do:

from matplotlib import colormaps
list(colormaps)

get\_cmap(_cmap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py#L203-L233)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.get_cmap "Link to this definition")

Return a color map specified through _cmap_.

Parameters:

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 or None

*   if a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
    , return it
    
*   if a string, look it up in `mpl.colormaps`
    
*   if None, return the Colormap defined in `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)
    

Returns:

Colormap

register(_cmap_, _\*_, _name\=None_, _force\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py#L121-L169)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "Link to this definition")

Register a new colormap.

The colormap name can then be used as a string argument to any `cmap` parameter in Matplotlib. It is also available in `pyplot.get_cmap`.

The colormap registry stores a copy of the given colormap, so that future changes to the original colormap instance do not affect the registered colormap. Think of this as the registry taking a snapshot of the colormap at registration.

Parameters:

**cmap**matplotlib.colors.Colormap

The colormap to register.

**name**str, optional

The name for the colormap. If not given, `cmap.name` is used.

**force**bool, default: False

If False, a ValueError is raised if trying to overwrite an already registered name. True supports overwriting registered colormaps other than the builtin colormaps.

unregister(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py#L171-L201)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.unregister "Link to this definition")

Remove a colormap from the registry.

You cannot remove built-in colormaps.

If the named colormap is not registered, returns with no error, raises if you try to de-register a default colormap.

Warning

Colormap names are currently a shared namespace that may be used by multiple packages. Use [`unregister`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.unregister "matplotlib.cm.ColormapRegistry.unregister")
 only if you know you have registered that name before. In particular, do not unregister just in case to clean the name before registering a new colormap.

Parameters:

**name**str

The name of the colormap to be removed.

Raises:

ValueError

If you try to remove a default built-in colormap.

class matplotlib.cm.ScalarMappable(_colorizer_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L518-L630)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "Link to this definition")

autoscale()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L436-L441)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.autoscale "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array

autoscale\_None()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L443-L448)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.autoscale_None "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array, changing only limits that are None

changed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L604-L610)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.changed "Link to this definition")

Call this whenever the mappable is changed to notify all the callbackSM listeners to the 'changed' signal.

property colorbar[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.colorbar "Link to this definition")

The last colorbar associated with this object. May be None

get\_alpha()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L384-L388)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.get_alpha "Link to this definition")

get\_array()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L595-L602)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.get_array "Link to this definition")

Return the array of values, that are mapped to colors.

The base class [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 does not make any assumptions on the dimensionality and shape of the array.

get\_clim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L360-L364)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.get_clim "Link to this definition")

Return the values (min, max) that are mapped to the colormap limits.

get\_cmap()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L398-L400)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.get_cmap "Link to this definition")

Return the [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 instance.

property norm[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.norm "Link to this definition")

set\_array(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L562-L593)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_array "Link to this definition")

Set the value array from array-like _A_.

Parameters:

**A**array-like or None

The values that are mapped to colors.

The base class [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 does not make any assumptions on the dimensionality and shape of the value array _A_.

set\_clim(_vmin\=None_, _vmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L366-L382)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_clim "Link to this definition")

Set the norm limits for image scaling.

Parameters:

**vmin, vmax**float

The limits.

For scalar data, the limits may also be passed as a tuple (_vmin_, _vmax_) as a single positional argument.

set\_cmap(_cmap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L402-L410)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_cmap "Link to this definition")

Set the colormap for luminance data.

Parameters:

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 or str or None

set\_norm(_norm_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L420-L434)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_norm "Link to this definition")

Set the normalization instance.

Parameters:

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 or str or None

Notes

If there are any colorbars using the mappable for this norm, setting the norm of the mappable will reset the norm, locator, and formatters on the colorbar to default.

to\_rgba(_x_, _alpha\=None_, _bytes\=False_, _norm\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L328-L358)
[#](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.to_rgba "Link to this definition")

Return a normalized RGBA array corresponding to _x_.

In the normal case, _x_ is a 1D or 2D sequence of scalars, and the corresponding [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of RGBA values will be returned, based on the norm and colormap set for this Colorizer.

There is one special case, for handling images that are already RGB or RGBA, such as might have been read from an image file. If _x_ is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 with 3 dimensions, and the last dimension is either 3 or 4, then it will be treated as an RGB or RGBA array, and no mapping will be done. The array can be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
, or it can be floats with values in the 0-1 range; otherwise a ValueError will be raised. Any NaNs or masked elements will be set to 0 alpha. If the last dimension is 3, the _alpha_ kwarg (defaulting to 1) will be used to fill in the transparency. If the last dimension is 4, the _alpha_ kwarg is ignored; it does not replace the preexisting alpha. A ValueError will be raised if the third dimension is other than 3 or 4.

In either case, if _bytes_ is _False_ (default), the RGBA array will be floats in the 0-1 range; if it is _True_, the returned RGBA array will be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 in the 0 to 255 range.

If norm is False, no normalization of the input data is performed, and it is assumed to be in the range (0-1).

On this page