[Skip to main content](https://matplotlib.org/stable/api/scale_api.html#main-content)

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
    

`matplotlib.scale`[#](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "Link to this heading")

=======================================================================================================================

Scales define the distribution of data values on an axis, e.g. a log scaling.

The mapping is implemented through [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 subclasses.

The following scales are built-in:

| Name | Class | Transform | Inverted transform |
| --- | --- | --- | --- |
| "asinh" | [`AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale") | [`AsinhTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform "matplotlib.scale.AsinhTransform") | [`InvertedAsinhTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform "matplotlib.scale.InvertedAsinhTransform") |
| "function" | [`FuncScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "matplotlib.scale.FuncScale") | [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform") | [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform") |
| "functionlog" | [`FuncScaleLog`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScaleLog "matplotlib.scale.FuncScaleLog") | [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform")<br> + [`LogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "matplotlib.scale.LogTransform") | [`InvertedLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform "matplotlib.scale.InvertedLogTransform")<br> + [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform") |
| "linear" | [`LinearScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale "matplotlib.scale.LinearScale") | [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform") | [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform") |
| "log" | [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale") | [`LogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "matplotlib.scale.LogTransform") | [`InvertedLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform "matplotlib.scale.InvertedLogTransform") |
| "logit" | [`LogitScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale "matplotlib.scale.LogitScale") | [`LogitTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform "matplotlib.scale.LogitTransform") | [`LogisticTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform "matplotlib.scale.LogisticTransform") |
| "symlog" | [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale") | [`SymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "matplotlib.scale.SymmetricalLogTransform") | [`InvertedSymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform "matplotlib.scale.InvertedSymmetricalLogTransform") |

A user will often only use the scale name, e.g. when setting the scale through [`set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
: `ax.set_xscale("log")`.

See also the [scales examples](https://matplotlib.org/stable/gallery/scales/index.html#sphx-glr-gallery-scales)
 in the documentation.

Custom scaling can be achieved through [`FuncScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "matplotlib.scale.FuncScale")
, or by creating your own [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 subclass and corresponding transforms (see [Custom scale](https://matplotlib.org/stable/gallery/scales/custom_scale.html)
). Third parties can register their scales by name through [`register_scale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
.

class matplotlib.scale.ScaleBase(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L47-L134)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The base class for all scales.

Scales are separable transformations, working on a single dimension.

Subclasses should override

`name`

The scale's name.

[`get_transform()`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.get_transform "matplotlib.scale.ScaleBase.get_transform")

A method returning a [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, which converts data coordinates to scaled coordinates. This transform should be invertible, so that e.g. mouse positions can be converted back to data coordinates.

[`set_default_locators_and_formatters()`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.set_default_locators_and_formatters "matplotlib.scale.ScaleBase.set_default_locators_and_formatters")

A method that sets default locators and formatters for an [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 that uses this scale.

[`limit_range_for_scale()`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.limit_range_for_scale "matplotlib.scale.ScaleBase.limit_range_for_scale")

An optional method that "fixes" the axis range to acceptable values, e.g. restricting log-scaled axes to positive values.

Construct a new scale.

Notes

The following note is for scale implementers.

For back-compatibility reasons, scales take an [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 object as the first argument.

Deprecated since version 3.11: The _axis_ parameter is now optional, i.e. matplotlib is compatible with [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 subclasses that do not take an _axis_ parameter.

The _axis_ parameter is pending-deprecated. It will be deprecated in matplotlib 3.13, and removed in matplotlib 3.15.

3rd-party scales are recommended to remove the _axis_ parameter now if they can afford to restrict compatibility to matplotlib >= 3.11 already. Otherwise, they may keep the _axis_ parameter and remove it in time for matplotlib 3.13.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L94-L98)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 object associated with this scale.

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L100-L105)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

limit\_range\_for\_scale(_vmin_, _vmax_, _minpos_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L107-L115)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.limit_range_for_scale "Link to this definition")

Return the range _vmin_, _vmax_, restricted to the domain supported by this scale (if any).

_minpos_ should be the minimum positive value in the data. This is used by log scales to determine a minimum value.

val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L117-L134)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase.val_in_range "Link to this definition")

Return whether the value(s) are within the valid range for this scale.

Accepts a scalar or array-like `val`. For a scalar, returns a Python `bool`. For an array, returns a bool ndarray of the same shape. This is a generic implementation, and subclasses may implement more efficient solutions for their domain.

class matplotlib.scale.LinearScale(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L188-L230)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The default linear scale.

name \= 'linear'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale.name "Link to this definition")

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L203-L213)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L215-L220)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale.get_transform "Link to this definition")

Return the transform for linear scaling, which is just the [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
.

val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L222-L230)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale.val_in_range "Link to this definition")

Return whether the value(s) are within the valid range for this scale.

This is True for all values, except +-inf and NaN.

class matplotlib.scale.FuncTransform(_forward_, _inverse_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L233-L266)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

A simple transform that takes and arbitrary function for the forward and inverse transform.

Parameters:

**forward**callable

The forward function for the transform. This function must have an inverse and, for best behavior, be monotonic. It must have the signature:

def forward(values: array\-like) \-> array\-like

**inverse**callable

The inverse of the forward function. Signature as `forward`.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L262-L263)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L265-L266)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.FuncScale(_axis_, _functions_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L269-L315)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

Provide an arbitrary scale with user-supplied function for the axis.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis for the scale.

Note

This parameter is unused and will be removed in an imminent release. It can already be left out because of special preprocessing, so that `FuncScale(functions)` is valid.

**functions**(callable, callable)

two-tuple of the forward and inverse functions for the scale. The forward function must be monotonic.

Both functions must have the signature:

def forward(values: array\-like) \-> array\-like

name \= 'function'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale.name "Link to this definition")

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L301-L303)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale.get_transform "Link to this definition")

Return the [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform")
 associated with this scale.

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L305-L315)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

class matplotlib.scale.LogTransform(_base_, _nonpositive\='clip'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L318-L356)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L334-L353)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L355-L356)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.InvertedLogTransform(_base_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L359-L378)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L370-L375)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L377-L378)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.LogScale(_axis\=None_, _\*_, _base\=10_, _subs\=None_, _nonpositive\='clip'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L381-L445)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

A standard logarithmic scale. Care is taken to only plot positive values.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis for the scale.

Note

This parameter is unused and about to be removed in the future. It can already now be left out because of special preprocessing, so that `LogScale(base=2)` is valid.

**base**float, default: 10

The base of the logarithm.

**nonpositive**{'clip', 'mask'}, default: 'clip'

Determines the behavior for non-positive values. They can either be masked as invalid, or clipped to a very small positive number.

**subs**sequence of int, default: None

Where to place the subticks between each major tick. For example, in a log10 scale, `[2, 3, 4, 5, 6, 7, 8, 9]` will place 8 logarithmically spaced minor ticks between each major tick.

name \= 'log'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.name "Link to this definition")

property base[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.base "Link to this definition")

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L415-L422)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L424-L426)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.get_transform "Link to this definition")

Return the [`LogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "matplotlib.scale.LogTransform")
 associated with this scale.

limit\_range\_for\_scale(_vmin_, _vmax_, _minpos_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L428-L434)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.limit_range_for_scale "Link to this definition")

Limit the domain to positive values.

val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L436-L445)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale.val_in_range "Link to this definition")

Return whether the value(s) are within the valid range for this scale.

This is True for value(s) > 0 except +inf and NaN.

class matplotlib.scale.FuncScaleLog(_axis_, _functions_, _base\=10_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L448-L489)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScaleLog "Link to this definition")

Bases: [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")

Provide an arbitrary scale with user-supplied function for the axis and then put on a logarithmic axes.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis for the scale.

Note

This parameter is unused and about to be removed in the future. It can already now be left out because of special preprocessing, so that `FuncScaleLog(functions=(forward, inverse))` is valid.

**functions**(callable, callable)

two-tuple of the forward and inverse functions for the scale. The forward function must be monotonic.

Both functions must have the signature:

def forward(values: array\-like) \-> array\-like

**base**float, default: 10

Logarithmic base of the scale.

name \= 'functionlog'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScaleLog.name "Link to this definition")

property base[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScaleLog.base "Link to this definition")

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L487-L489)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScaleLog.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 associated with this scale.

class matplotlib.scale.SymmetricalLogTransform(_base_, _linthresh_, _linscale_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L492-L524)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L507-L520)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L522-L524)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.InvertedSymmetricalLogTransform(_base_, _linthresh_, _linscale_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L527-L565)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

property invlinthresh[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.invlinthresh "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use .inverted().transform(linthresh) instead.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L549-L561)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L563-L565)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedSymmetricalLogTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.SymmetricalLogScale(_axis\=None_, _\*_, _base\=10_, _linthresh\=2_, _subs\=None_, _linscale\=1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L568-L641)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The symmetrical logarithmic scale is logarithmic in both the positive and negative directions from the origin.

Since the values close to zero tend toward infinity, there is a need to have a range around zero that is linear. The parameter _linthresh_ allows the user to specify the size of this range (-_linthresh_, _linthresh_).

See [Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)
 for a detailed description.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis for the scale.

Note

This parameter is unused and about to be removed in the future. It can already now be left out because of special preprocessing, so that `SymmetricalLocSacle(base=2)` is valid.

**base**float, default: 10

The base of the logarithm.

**linthresh**float, default: 2

Defines the range `(-x, x)`, within which the plot is linear. This avoids having the plot go to infinity around zero.

**subs**sequence of int

Where to place the subticks between each major tick. For example, in a log10 scale: `[2, 3, 4, 5, 6, 7, 8, 9]` will place 8 logarithmically spaced minor ticks between each major tick.

**linscale**float, optional

This allows the linear range `(-linthresh, linthresh)` to be stretched relative to the logarithmic range. Its value is the number of decades to use for each half of the linear range. For example, when _linscale_ == 1.0 (the default), the space used for the positive and negative halves of the linear range will be equal to one decade in the logarithmic range.

Construct a new scale.

Notes

The following note is for scale implementers.

For back-compatibility reasons, scales take an [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 object as the first argument.

Deprecated since version 3.11: The _axis_ parameter is now optional, i.e. matplotlib is compatible with [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 subclasses that do not take an _axis_ parameter.

The _axis_ parameter is pending-deprecated. It will be deprecated in matplotlib 3.13, and removed in matplotlib 3.15.

3rd-party scales are recommended to remove the _axis_ parameter now if they can afford to restrict compatibility to matplotlib >= 3.11 already. Otherwise, they may keep the _axis_ parameter and remove it in time for matplotlib 3.13.

name \= 'symlog'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.name "Link to this definition")

property base[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.base "Link to this definition")

property linthresh[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.linthresh "Link to this definition")

property linscale[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.linscale "Link to this definition")

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L621-L627)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L629-L631)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.get_transform "Link to this definition")

Return the [`SymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "matplotlib.scale.SymmetricalLogTransform")
 associated with this scale.

val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L633-L641)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale.val_in_range "Link to this definition")

Return whether the value(s) are within the valid range for this scale.

This is True for all values, except +-inf and NaN.

class matplotlib.scale.AsinhTransform(_linear\_width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L644-L659)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Inverse hyperbolic-sine transformation used by [`AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L655-L656)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L658-L659)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.InvertedAsinhTransform(_linear\_width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L662-L674)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Hyperbolic sine transformation used by [`AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L670-L671)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L673-L674)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedAsinhTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.AsinhScale(_axis\=None_, _\*_, _linear\_width\=1.0_, _base\=10_, _subs\='auto'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L677-L777)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

A quasi-logarithmic scale based on the inverse hyperbolic sine (asinh)

For values close to zero, this is essentially a linear scale, but for large magnitude values (either positive or negative) it is asymptotically logarithmic. The transition between these linear and logarithmic regimes is smooth, and has no discontinuities in the function gradient in contrast to the [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
 ("symlog") scale.

Specifically, the transformation of an axis coordinate \\(a\\) is \\(a \\rightarrow a\_0 \\sinh^{-1} (a / a\_0)\\) where \\(a\_0\\) is the effective width of the linear region of the transformation. In that region, the transformation is \\(a \\rightarrow a + \\mathcal{O}(a^3)\\). For large values of \\(a\\) the transformation behaves as \\(a \\rightarrow a\_0 \\, \\mathrm{sgn}(a) \\ln |a| + \\mathcal{O}(1)\\).

Note

This API is provisional and may be revised in the future based on early user feedback.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis for the scale.

Note

This parameter is unused and about to be removed in the future. It can already now be left out because of special preprocessing, so that `AsinhScale()` is valid.

**linear\_width**float, default: 1

The scale parameter (elsewhere referred to as \\(a\_0\\)) defining the extent of the quasi-linear region, and the coordinate values beyond which the transformation becomes asymptotically logarithmic.

**base**int, default: 10

The number base used for rounding tick locations on a logarithmic scale. If this is less than one, then rounding is to the nearest integer multiple of powers of ten.

**subs**sequence of int

Multiples of the number base used for minor ticks. If set to 'auto', this will use built-in defaults, e.g. (2, 5) for base=10.

name \= 'asinh'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.name "Link to this definition")

auto\_tick\_multipliers \= {3: (2,), 4: (2,), 5: (2,), 8: (2, 4), 10: (2, 5), 16: (2, 4, 8), 64: (4, 16), 1024: (256, 512)}[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.auto_tick_multipliers "Link to this definition")

property linear\_width[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.linear_width "Link to this definition")

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L754-L755)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 object associated with this scale.

set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L757-L767)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.set_default_locators_and_formatters "Link to this definition")

Set the locators and formatters of _axis_ to instances suitable for this scale.

val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L769-L777)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale.val_in_range "Link to this definition")

Return whether the value(s) are within the valid range for this scale.

This is True for all values, except +-inf and NaN.

class matplotlib.scale.LogitTransform(_nonpositive\='mask'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L780-L802)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L789-L796)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.transform_non_affine "Link to this definition")

logit transform (base 10), masked or clipped

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L798-L799)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.LogisticTransform(_nonpositive\='mask'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L805-L820)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

input\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

output\_dims \= 1[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L812-L814)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.transform_non_affine "Link to this definition")

logistic transform (base 10)

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L816-L817)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

has\_inverse \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogisticTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.scale.LogitScale(_axis\=None_, _nonpositive\='mask'_, _\*_, _one\_half\='\\\\frac{1}{2}'_, _use\_overline\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L823-L901)
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale "Link to this definition")

Bases: [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

Logit scale for data between zero and one, both excluded.

This scale is similar to a log scale close to zero and to one, and almost linear around 0.5. It maps the interval \]0, 1\[ onto \]-infty, +infty\[.\
\
Parameters:\
\
**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")\
\
The axis for the scale.\
\
Note\
\
This parameter is unused and about to be removed in the future. It can already now be left out because of special preprocessing, so that `LogitScale()` is valid.\
\
**nonpositive**{'mask', 'clip'}\
\
Determines the behavior for values beyond the open interval \]0, 1\[. They can either be masked as invalid, or clipped to a number very close to 0 or 1.\
\
**use\_overline**bool, default: False\
\
Indicate the usage of survival notation (overline{x}) in place of standard notation (1-x) for probability close to one.\
\
**one\_half**str, default: r"frac{1}{2}"\
\
The string used for ticks formatter to represent 1/2.\
\
name \= 'logit'[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale.name "Link to this definition")\
\
get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L860-L862)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale.get_transform "Link to this definition")\
\
Return the [`LogitTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitTransform "matplotlib.scale.LogitTransform")\
 associated with this scale.\
\
set\_default\_locators\_and\_formatters(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L864-L881)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale.set_default_locators_and_formatters "Link to this definition")\
\
Set the locators and formatters of _axis_ to instances suitable for this scale.\
\
limit\_range\_for\_scale(_vmin_, _vmax_, _minpos_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L883-L890)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale.limit_range_for_scale "Link to this definition")\
\
Limit the domain to values between 0 and 1 (excluded).\
\
val\_in\_range(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L892-L901)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogitScale.val_in_range "Link to this definition")\
\
Return whether the value(s) are within the valid range for this scale.\
\
This is True for value(s) which are between 0 and 1 (excluded).\
\
matplotlib.scale.get\_scale\_names()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L929-L931)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.get_scale_names "Link to this definition")\
\
Return the names of the available scales.\
\
matplotlib.scale.scale\_factory(_scale_, _axis_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L934-L948)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.scale_factory "Link to this definition")\
\
Return a scale class by name.\
\
Parameters:\
\
**scale**{'asinh', 'function', 'functionlog', 'linear', 'log', 'logit', 'symlog'}\
\
**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")\
\
matplotlib.scale.register\_scale(_scale\_class_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/scale.py#L956-L979)\
[#](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "Link to this definition")\
\
Register a new kind of scale.\
\
Parameters:\
\
**scale\_class**subclass of [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")\
\
The scale to register.\
\
On this page