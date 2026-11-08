[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#main-content)

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
    

matplotlib.colors.MultiNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib-colors-multinorm "Link to this heading")

==============================================================================================================================================================

class matplotlib.colors.MultiNorm(_norms_, _vmin\=None_, _vmax\=None_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3354-L3645)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm "Link to this definition")

Bases: [`Norm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm "matplotlib.colors.Norm")

A class which contains multiple scalar norms.

Parameters:

**norms**list of (str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
)

The constituent norms. The list must have a minimum length of 1.

**vmin, vmax**None or list of (float or None)

Limits of the constituent norms. If a list, one value is assigned to each of the constituent norms. If None, the limits of the constituent norms are not changed.

**clip**None or list of bools, default: None

Determines the behavior for mapping values outside the range `[vmin, vmax]` for the constituent norms. If a list, each value is assigned to each of the constituent norms. If None, the behaviour of the constituent norms is not changed.

\_\_call\_\_(_values_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3479-L3521)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.__call__ "Link to this definition")

Normalize the data and return the normalized data.

Each component of the input is normalized via the constituent norm.

Parameters:

**values**array-like

The input data, as an iterable or a structured numpy array.

*   If iterable, must be of length [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
    . Each element can be a scalar or array-like and is normalized through the corresponding norm.
    
*   If structured array, must have [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
     fields. Each field is normalized through the corresponding norm.
    

**clip**list of bools or None, optional

Determines the behavior for mapping values outside the range `[vmin, vmax]`. See the description of the parameter _clip_ in [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
. If `None`, defaults to `self.clip` (which defaults to `False`).

Returns:

tuple

Normalized input values

Notes

If not already initialized, `self.vmin` and `self.vmax` are initialized using `self.autoscale_None(values)`.

autoscale(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3542-L3561)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.autoscale "Link to this definition")

For each constituent norm, set _vmin_, _vmax_ to min, max of the corresponding component in _A_.

Parameters:

**A**array-like

The input data, as an iterable or a structured numpy array.

*   If iterable, must be of length [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
    . Each element is used for the limits of one constituent norm.
    
*   If structured array, must have [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
     fields. Each field is used for the limits of one constituent norm.
    

autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3563-L3582)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.autoscale_None "Link to this definition")

If _vmin_ or _vmax_ are not set on any constituent norm, use the min/max of the corresponding component in _A_ to set them.

Parameters:

**A**array-like

The input data, as an iterable or a structured numpy array.

*   If iterable, must be of length [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
    . Each element is used for the limits of one constituent norm.
    
*   If structured array, must have [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
     fields. Each field is used for the limits of one constituent norm.
    

property clip[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.clip "Link to this definition")

The clip behaviour of each constituent norm.

inverse(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3523-L3540)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.inverse "Link to this definition")

Map the normalized values (i.e., index in the colormap) back to data values.

Parameters:

**values**array-like

The input data, as an iterable or a structured numpy array.

*   If iterable, must be of length [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
    . Each element can be a scalar or array-like and is mapped through the corresponding norm.
    
*   If structured array, must have [`n_components`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "matplotlib.colors.MultiNorm.n_components")
     fields. Each field is mapped through the corresponding norm.
    

property n\_components[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.n_components "Link to this definition")

Number of norms held by this [`MultiNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm "matplotlib.colors.MultiNorm")
.

property norms[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.norms "Link to this definition")

The individual norms held by this [`MultiNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm "matplotlib.colors.MultiNorm")
.

scaled()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3584-L3586)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.scaled "Link to this definition")

Return whether both _vmin_ and _vmax_ are set on all constituent norms.

property vmax[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.vmax "Link to this definition")

The upper limit of each constituent norm.

property vmin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm.vmin "Link to this definition")

The lower limit of each constituent norm.

On this page