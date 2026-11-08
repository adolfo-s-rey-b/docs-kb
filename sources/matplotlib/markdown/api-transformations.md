[Skip to main content](https://matplotlib.org/stable/api/transformations.html#main-content)

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
    

`matplotlib.transforms`[#](https://matplotlib.org/stable/api/transformations.html#matplotlib-transforms "Link to this heading")

================================================================================================================================

Inheritance diagram of matplotlib.transforms

Matplotlib includes a framework for arbitrary geometric transformations that is used to determine the final position of all elements drawn on the canvas.

Transforms are composed into trees of [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")
 objects whose actual value depends on their children. When the contents of children change, their parents are automatically invalidated. The next time an invalidated transform is accessed, it is recomputed to reflect those changes. This invalidation/caching approach prevents unnecessary recomputations of transforms, and contributes to better interactive performance.

For example, here is a graph of the transform tree used to plot data to the figure:

Diagram of transform tree from data to figure coordinates.

The framework can be used for both affine and non-affine transformations. However, for speed, we want to use the backend renderers to perform affine transformations whenever possible. Therefore, it is possible to perform just the affine or non-affine part of a transformation on a set of data. The affine is always assumed to occur after the non-affine. For any transform:

full transform \== non\-affine part + affine part

The backends are not expected to handle non-affine transformations themselves.

See the tutorial [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
 for examples of how to use transforms.

class matplotlib.transforms.Affine2D(_matrix\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1941-L2160)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A mutable 2D affine transformation.

Initialize an Affine transform from a 3x3 numpy float array:

a c e
b d f
0 0 1

If _matrix_ is None, initialize with the identity transform.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2023-L2030)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.clear "Link to this definition")

Reset the underlying matrix to the identity transform.

static from\_values(_a_, _b_, _c_, _d_, _e_, _f_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1972-L1984)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.from_values "Link to this definition")

Create a new Affine2D instance from the given values:

a c e
b d f
0 0 1

.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1986-L1999)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.get_matrix "Link to this definition")

Get the underlying transformation matrix as a 3x3 array:

a c e
b d f
0 0 1

.

rotate(_theta_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2032-L2053)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "Link to this definition")

Add a rotation (in radians) to this transform in place.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

rotate\_around(_x_, _y_, _theta_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2065-L2073)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_around "Link to this definition")

Add a rotation (in radians) around the point (x, y) in place.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

rotate\_deg(_degrees_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2055-L2063)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "Link to this definition")

Add a rotation (in degrees) to this transform in place.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

rotate\_deg\_around(_x_, _y_, _degrees_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2075-L2085)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg_around "Link to this definition")

Add a rotation (in degrees) around the point (x, y) in place.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

scale(_sx_, _sy\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2100-L2121)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "Link to this definition")

Add a scale in place.

If _sy_ is None, the same scale is applied in both the _x_\- and _y_\-directions.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

set(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2014-L2021)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.set "Link to this definition")

Set this transformation from the frozen copy of another [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")
 object.

set\_matrix(_mtx_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2001-L2012)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.set_matrix "Link to this definition")

Set the underlying transformation matrix from a 3x3 array:

a c e
b d f
0 0 1

.

skew(_xShear_, _yShear_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2123-L2147)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew "Link to this definition")

Add a skew in place.

_xShear_ and _yShear_ are the shear angles along the _x_\- and _y_\-axes, respectively, in radians.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

skew\_deg(_xShear_, _yShear_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2149-L2160)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew_deg "Link to this definition")

Add a skew in place.

_xShear_ and _yShear_ are the shear angles along the _x_\- and _y_\-axes, respectively, in degrees.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

translate(_tx_, _ty_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2087-L2098)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "Link to this definition")

Add a translation in place.

Returns _self_, so this method can easily be chained with more calls to [`rotate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate "matplotlib.transforms.Affine2D.rotate")
, [`rotate_deg()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
, [`translate()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.translate "matplotlib.transforms.Affine2D.translate")
 and [`scale()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
.

class matplotlib.transforms.Affine2DBase(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1873-L1938)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "Link to this definition")

Bases: [`AffineBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase "matplotlib.transforms.AffineBase")

The base class of all 2D affine transformations.

2D affine transformations are performed using a 3x3 numpy array:

a c e
b d f
0 0 1

This class provides the read-only interface. For a mutable 2D affine transformation, use [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
.

Subclasses of this class will generally only need to override a constructor and [`get_matrix`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.get_matrix "matplotlib.transforms.Transform.get_matrix")
 that generates a custom 3x3 matrix.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1892-L1894)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

has\_inverse \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= 2[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1929-L1938)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

property is\_separable[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.is_separable "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

output\_dims \= 2[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

to\_values()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1901-L1906)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.to_values "Link to this definition")

Return the values of the matrix as an `(a, b, c, d, e, f)` tuple.

transform\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1908-L1913)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.transform_affine "Link to this definition")

Apply only the affine part of this transformation on the given array of values.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally a no-op. In affine transformations, this is equivalent to `transform(values)`.

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

class matplotlib.transforms.AffineBase(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1823-L1870)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The base class of all affine transformations of any number of dimensions.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1868-L1870)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.get_affine "Link to this definition")

Get the affine part of this transform.

is\_affine \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.is_affine "Link to this definition")

transform(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1842-L1844)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform "Link to this definition")

Apply this transformation on the given array of _values_.

Parameters:

**values**array-like

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

transform\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1846-L1849)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform_affine "Link to this definition")

Apply only the affine part of this transformation on the given array of values.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally a no-op. In affine transformations, this is equivalent to `transform(values)`.

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

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1851-L1853)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform_non_affine "Link to this definition")

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

transform\_path(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1855-L1857)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform_path "Link to this definition")

Apply the transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

In some cases, this transform may insert curves into the path that began as line segments.

transform\_path\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1859-L1862)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform_path_affine "Link to this definition")

Apply the affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1864-L1866)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineBase.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

class matplotlib.transforms.AffineDeltaTransform(_transform_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2745-L2775)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineDeltaTransform "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A transform wrapper for transforming displacements between pairs of points.

This class is intended to be used to transform displacements ("position deltas") between pairs of points (e.g., as the `offset_transform` of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s): given a transform `t` such that `t = AffineDeltaTransform(t) + offset`, `AffineDeltaTransform` satisfies `AffineDeltaTransform(a - b) == AffineDeltaTransform(a) - AffineDeltaTransform(b)`.

This is implemented by forcing the offset components of the transform matrix to zero.

This class is experimental as of 3.3, and the API may change.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2771-L2775)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineDeltaTransform.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

pass\_through \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineDeltaTransform.pass_through "Link to this definition")

If pass\_through is True, all ancestors will always be invalidated, even if 'self' is already invalid.

class matplotlib.transforms.Bbox(_points_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L692-L1129)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "Link to this definition")

Bases: [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

A mutable bounding box.

Examples

**Create from known bounds**

The default constructor takes the boundary "points" `[[xmin, ymin], [xmax, ymax]]`.

\>>> Bbox(\[\[1, 1\], \[3, 7\]\])
Bbox(\[\[1.0, 1.0\], \[3.0, 7.0\]\])

Alternatively, a Bbox can be created from the flattened points array, the so-called "extents" `(xmin, ymin, xmax, ymax)`

\>>> Bbox.from\_extents(1, 1, 3, 7)
Bbox(\[\[1.0, 1.0\], \[3.0, 7.0\]\])

or from the "bounds" `(xmin, ymin, width, height)`.

\>>> Bbox.from\_bounds(1, 1, 2, 6)
Bbox(\[\[1.0, 1.0\], \[3.0, 7.0\]\])

**Create from collections of points**

The "empty" object for accumulating Bboxs is the null bbox, which is a stand-in for the empty set.

\>>> Bbox.null()
Bbox(\[\[inf, inf\], \[-inf, -inf\]\])

Adding points to the null bbox will give you the bbox of those points.

\>>> box \= Bbox.null()
\>>> box.update\_from\_data\_xy(\[\[1, 1\]\])
\>>> box
Bbox(\[\[1.0, 1.0\], \[1.0, 1.0\]\])
\>>> box.update\_from\_data\_xy(\[\[2, 3\], \[3, 2\]\], ignore\=False)
\>>> box
Bbox(\[\[1.0, 1.0\], \[3.0, 3.0\]\])

Setting `ignore=True` is equivalent to starting over from a null bbox.

\>>> box.update\_from\_data\_xy(\[\[1, 1\]\], ignore\=True)
\>>> box
Bbox(\[\[1.0, 1.0\], \[1.0, 1.0\]\])

Warning

It is recommended to always specify `ignore` explicitly. If not, the default value of `ignore` can be changed at any time by code with access to your Bbox, for example using the method [`ignore`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "matplotlib.transforms.Bbox.ignore")
.

**Properties of the \`\`null\`\` bbox**

Note

The current behavior of [`Bbox.null()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.null "matplotlib.transforms.Bbox.null")
 may be surprising as it does not have all of the properties of the "empty set", and as such does not behave like a "zero" object in the mathematical sense. We may change that in the future (with a deprecation period).

The null bbox is the identity for intersections

\>>> Bbox.intersection(Bbox(\[\[1, 1\], \[3, 7\]\]), Bbox.null())
Bbox(\[\[1.0, 1.0\], \[3.0, 7.0\]\])

except with itself, where it returns the full space.

\>>> Bbox.intersection(Bbox.null(), Bbox.null())
Bbox(\[\[-inf, -inf\], \[inf, inf\]\])

A union containing null will always return the full space (not the other set!)

\>>> Bbox.union(\[Bbox(\[\[0, 0\], \[0, 0\]\]), Bbox.null()\])
Bbox(\[\[-inf, -inf\], \[inf, inf\]\])

Parameters:

**points**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

A (2, 2) array of the form `[[x0, y0], [x1, y1]]`.

property bounds[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.bounds "Link to this definition")

Return ([`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x0 "matplotlib.transforms.Bbox.x0")
, [`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "matplotlib.transforms.Bbox.y0")
, [`width`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "matplotlib.transforms.BboxBase.width")
, [`height`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "matplotlib.transforms.BboxBase.height")
).

static from\_bounds(_x0_, _y0_, _width_, _height_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L819-L826)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_bounds "Link to this definition")

Create a new [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 from _x0_, _y0_, _width_ and _height_.

_width_ and _height_ may be negative.

static from\_extents(_\*args_, _minpos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L828-L847)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_extents "Link to this definition")

Create a new Bbox from _left_, _bottom_, _right_ and _top_.

The _y_\-axis increases upwards.

Parameters:

**left, bottom, right, top**float

The four extents of the bounding box.

**minpos**float or None

If this is supplied, the Bbox will have a minimum positive value set. This is useful when dealing with logarithmic scales and other scales where negative bounds result in floating point errors.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L803-L807)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.frozen "Link to this definition")

The base class for anything that participates in the transform tree and needs to invalidate its parents or be invalidated. This includes classes that are not really transforms, such as bounding boxes, since some transforms depend on bounding boxes to compute their values.

get\_points()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1091-L1097)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.get_points "Link to this definition")

Get the points of the bounding box as an array of the form `[[x0, y0], [x1, y1]]`.

ignore(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L860-L871)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "Link to this definition")

Set whether the existing bounds of the box should be ignored by subsequent calls to [`update_from_data_xy()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_xy "matplotlib.transforms.Bbox.update_from_data_xy")
.

valuebool

*   When `True`, subsequent calls to [`update_from_data_xy`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_xy "matplotlib.transforms.Bbox.update_from_data_xy")
     will ignore the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `False`, subsequent calls to [`update_from_data_xy`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_xy "matplotlib.transforms.Bbox.update_from_data_xy")
     will include the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    

property intervalx[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.intervalx "Link to this definition")

The pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be sorted from left to right.

property intervaly[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.intervaly "Link to this definition")

The pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be sorted from bottom to top.

property minpos[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.minpos "Link to this definition")

The minimum positive value in both directions within the Bbox.

This is useful when dealing with logarithmic scales and other scales where negative bounds result in floating point errors, and will be used as the minimum extent instead of _p0_.

property minposx[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.minposx "Link to this definition")

The minimum positive value in the _x_\-direction within the Bbox.

This is useful when dealing with logarithmic scales and other scales where negative bounds result in floating point errors, and will be used as the minimum _x_\-extent instead of _x0_.

property minposy[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.minposy "Link to this definition")

The minimum positive value in the _y_\-direction within the Bbox.

This is useful when dealing with logarithmic scales and other scales where negative bounds result in floating point errors, and will be used as the minimum _y_\-extent instead of _y0_.

mutated()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1117-L1119)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.mutated "Link to this definition")

Return whether the bbox has changed since init.

mutatedx()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1121-L1124)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.mutatedx "Link to this definition")

Return whether the x-limits have changed since init.

mutatedy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1126-L1129)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.mutatedy "Link to this definition")

Return whether the y-limits have changed since init.

static null()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L814-L817)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.null "Link to this definition")

Create a new null [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 from (inf, inf) to (-inf, -inf).

property p0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.p0 "Link to this definition")

The first pair of (_x_, _y_) coordinates that define the bounding box.

This is not guaranteed to be the bottom-left corner (for that, use [`min`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.min "matplotlib.transforms.BboxBase.min")
).

property p1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.p1 "Link to this definition")

The second pair of (_x_, _y_) coordinates that define the bounding box.

This is not guaranteed to be the top-right corner (for that, use [`max`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.max "matplotlib.transforms.BboxBase.max")
).

set(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1109-L1115)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.set "Link to this definition")

Set this bounding box from the "frozen" bounds of another [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

set\_points(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1099-L1107)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.set_points "Link to this definition")

Set the points of the bounding box directly from an array of the form `[[x0, y0], [x1, y1]]`. No error checking is performed, as this method is mainly for internal use.

static unit()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L809-L812)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.unit "Link to this definition")

Create a new unit [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 from (0, 0) to (1, 1).

update\_from\_data\_x(_x_, _ignore\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L933-L951)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_x "Link to this definition")

Update the x-bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 based on the passed in data. After updating, the bounds will have positive _width_, and _x0_ will be the minimal value.

Parameters:

**x**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

Array of x-values.

**ignore**bool, optional

*   When `True`, ignore the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `False`, include the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `None`, use the last value passed to [`ignore()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "matplotlib.transforms.Bbox.ignore")
    .
    

update\_from\_data\_xy(_xy_, _ignore\=None_, _updatex\=True_, _updatey\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L973-L996)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_xy "Link to this definition")

Update the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 bounds based on the passed in _xy_ coordinates.

After updating, the bounds will have positive _width_ and _height_; _x0_ and _y0_ will be the minimal values.

Parameters:

**xy**(N, 2) array-like

The (x, y) coordinates.

**ignore**bool, optional

*   When `True`, ignore the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `False`, include the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `None`, use the last value passed to [`ignore()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "matplotlib.transforms.Bbox.ignore")
    .
    

**updatex, updatey**bool, default: True

When `True`, update the x/y values.

update\_from\_data\_y(_y_, _ignore\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L953-L971)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_data_y "Link to this definition")

Update the y-bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 based on the passed in data. After updating, the bounds will have positive _height_, and _y0_ will be the minimal value.

Parameters:

**y**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

Array of y-values.

**ignore**bool, optional

*   When `True`, ignore the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `False`, include the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `None`, use the last value passed to [`ignore()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "matplotlib.transforms.Bbox.ignore")
    .
    

update\_from\_path(_path_, _ignore\=None_, _updatex\=True_, _updatey\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L873-L931)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.update_from_path "Link to this definition")

Update the bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 to contain the vertices of the provided path. After updating, the bounds will have positive _width_ and _height_; _x0_ and _y0_ will be the minimal values.

Parameters:

**path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

**ignore**bool, optional

*   When `True`, ignore the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `False`, include the existing bounds of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    
*   When `None`, use the last value passed to [`ignore()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.ignore "matplotlib.transforms.Bbox.ignore")
    .
    

**updatex, updatey**bool, default: True

When `True`, update the x/y values.

property x0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x0 "Link to this definition")

The first of the pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be less than [`x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x1 "matplotlib.transforms.Bbox.x1")
 (for that, use [`xmin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmin "matplotlib.transforms.BboxBase.xmin")
).

property x1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x1 "Link to this definition")

The second of the pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be greater than [`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x0 "matplotlib.transforms.Bbox.x0")
 (for that, use [`xmax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmax "matplotlib.transforms.BboxBase.xmax")
).

property y0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "Link to this definition")

The first of the pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be less than [`y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y1 "matplotlib.transforms.Bbox.y1")
 (for that, use [`ymin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymin "matplotlib.transforms.BboxBase.ymin")
).

property y1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y1 "Link to this definition")

The second of the pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be greater than [`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "matplotlib.transforms.Bbox.y0")
 (for that, use [`ymax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymax "matplotlib.transforms.BboxBase.ymax")
).

class matplotlib.transforms.BboxBase(_shorthand\_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L207-L686)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "Link to this definition")

Bases: [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")

The base class of all bounding boxes.

This class is immutable; [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 is a mutable subclass.

The canonical representation is as two points, with no restrictions on their ordering. Convenience properties are provided to get the left, bottom, right and top edges and width and height, but these are not stored explicitly.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

anchored(_c_, _container_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L503-L525)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.anchored "Link to this definition")

Return a copy of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 anchored to _c_ within _container_.

Parameters:

**c**(float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...}

Either an (_x_, _y_) pair of relative coordinates (0 is left or bottom, 1 is right or top), 'C' (center), or a cardinal direction ('SW', southwest, is bottom left, etc.).

**container**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

The box within which the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 is positioned.

See also

[`Axes.set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")

property bounds[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.bounds "Link to this definition")

Return ([`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "matplotlib.transforms.BboxBase.x0")
, [`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "matplotlib.transforms.BboxBase.y0")
, [`width`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "matplotlib.transforms.BboxBase.width")
, [`height`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "matplotlib.transforms.BboxBase.height")
).

coefs \= {'C': (0.5, 0.5), 'E': (1.0, 0.5), 'N': (0.5, 1.0), 'NE': (1.0, 1.0), 'NW': (0, 1.0), 'S': (0.5, 0), 'SE': (1.0, 0), 'SW': (0, 0), 'W': (0, 0.5)}[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.coefs "Link to this definition")

contains(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L417-L421)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.contains "Link to this definition")

Return whether `(x, y)` is in the bounding box or on its edge.

containsx(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L403-L408)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.containsx "Link to this definition")

Return whether _x_ is in the closed ([`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "matplotlib.transforms.BboxBase.x0")
, [`x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x1 "matplotlib.transforms.BboxBase.x1")
) interval.

containsy(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L410-L415)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.containsy "Link to this definition")

Return whether _y_ is in the closed ([`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "matplotlib.transforms.BboxBase.y0")
, [`y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y1 "matplotlib.transforms.BboxBase.y1")
) interval.

corners()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L644-L652)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.corners "Link to this definition")

Return the corners of this rectangle as an array of points.

Specifically, this returns the array `[[x0, y0], [x0, y1], [x1, y0], [x1, y1]]`.

count\_contains(_vertices_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L584-L598)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.count_contains "Link to this definition")

Count the number of vertices contained in the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. Any vertices with a non-finite x or y value are ignored.

Parameters:

**vertices**(N, 2) array

count\_overlaps(_bboxes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L600-L609)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.count_overlaps "Link to this definition")

Count the number of bounding boxes that overlap this one.

Parameters:

**bboxes**sequence of [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

expanded(_sw_, _sh_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L611-L621)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.expanded "Link to this definition")

Construct a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 by expanding this one around its center by the factors _sw_ and _sh_.

property extents[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.extents "Link to this definition")

Return ([`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "matplotlib.transforms.BboxBase.x0")
, [`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "matplotlib.transforms.BboxBase.y0")
, [`x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x1 "matplotlib.transforms.BboxBase.x1")
, [`y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y1 "matplotlib.transforms.BboxBase.y1")
).

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L230-L231)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.frozen "Link to this definition")

The base class for anything that participates in the transform tree and needs to invalidate its parents or be invalidated. This includes classes that are not really transforms, such as bounding boxes, since some transforms depend on bounding boxes to compute their values.

fully\_contains(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L457-L461)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.fully_contains "Link to this definition")

Return whether `x, y` is in the bounding box, but not on its edge.

fully\_containsx(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L443-L448)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.fully_containsx "Link to this definition")

Return whether _x_ is in the open ([`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "matplotlib.transforms.BboxBase.x0")
, [`x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x1 "matplotlib.transforms.BboxBase.x1")
) interval.

fully\_containsy(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L450-L455)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.fully_containsy "Link to this definition")

Return whether _y_ is in the open ([`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "matplotlib.transforms.BboxBase.y0")
, [`y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y1 "matplotlib.transforms.BboxBase.y1")
) interval.

fully\_overlaps(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L463-L482)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.fully_overlaps "Link to this definition")

Return whether this bounding box overlaps with the other bounding box, not including the edges.

Parameters:

**other**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

get\_points()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L377-L378)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.get_points "Link to this definition")

property height[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "Link to this definition")

The (signed) height of the bounding box.

static intersection(_bbox1_, _bbox2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L676-L686)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.intersection "Link to this definition")

Return the intersection of _bbox1_ and _bbox2_ if they intersect, or None if they don't.

property intervalx[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.intervalx "Link to this definition")

The pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be sorted from left to right.

property intervaly[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.intervaly "Link to this definition")

The pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be sorted from bottom to top.

is\_affine \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.is_affine "Link to this definition")

property max[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.max "Link to this definition")

The top-right corner of the bounding box.

property min[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.min "Link to this definition")

The bottom-left corner of the bounding box.

overlaps(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L423-L441)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.overlaps "Link to this definition")

Return whether this bounding box overlaps with the other bounding box.

Parameters:

**other**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

property p0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.p0 "Link to this definition")

The first pair of (_x_, _y_) coordinates that define the bounding box.

This is not guaranteed to be the bottom-left corner (for that, use [`min`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.min "matplotlib.transforms.BboxBase.min")
).

property p1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.p1 "Link to this definition")

The second pair of (_x_, _y_) coordinates that define the bounding box.

This is not guaranteed to be the top-right corner (for that, use [`max`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.max "matplotlib.transforms.BboxBase.max")
).

padded(_w\_pad_, _h\_pad\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L623-L638)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.padded "Link to this definition")

Construct a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 by padding this one on all four sides.

Parameters:

**w\_pad**float

Width pad

**h\_pad**float, optional

Height pad. Defaults to _w\_pad_.

rotated(_radians_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L654-L663)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.rotated "Link to this definition")

Return the axes-aligned bounding box that bounds the result of rotating this [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 by an angle of _radians_.

shrunk(_mx_, _my_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L527-L536)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.shrunk "Link to this definition")

Return a copy of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, shrunk by the factor _mx_ in the _x_ direction and the factor _my_ in the _y_ direction. The lower left corner of the box remains unchanged. Normally _mx_ and _my_ will be less than 1, but this is not enforced.

shrunk\_to\_aspect(_box\_aspect_, _container\=None_, _fig\_aspect\=1.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L538-L560)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.shrunk_to_aspect "Link to this definition")

Return a copy of the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, shrunk so that it is as large as it can be while having the desired aspect ratio, _box\_aspect_. If the box coordinates are relative (i.e. fractions of a larger box such as a figure) then the physical aspect ratio of that figure is specified with _fig\_aspect_, so that _box\_aspect_ can also be given as a ratio of the absolute dimensions, not the relative dimensions.

property size[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.size "Link to this definition")

The (signed) width and height of the bounding box.

splitx(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L562-L571)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.splitx "Link to this definition")

Return a list of new [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 objects formed by splitting the original one with vertical lines at fractional positions given by _args_.

splity(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L573-L582)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.splity "Link to this definition")

Return a list of new [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 objects formed by splitting the original one with horizontal lines at fractional positions given by _args_.

transformed(_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L484-L491)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.transformed "Link to this definition")

Construct a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 by statically transforming this one by _transform_.

translated(_tx_, _ty_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L640-L642)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.translated "Link to this definition")

Construct a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 by translating this one by _tx_ and _ty_.

static union(_bboxes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L665-L674)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.union "Link to this definition")

Return a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 that contains all of the given _bboxes_.

property width[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "Link to this definition")

The (signed) width of the bounding box.

property x0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "Link to this definition")

The first of the pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be less than [`x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x1 "matplotlib.transforms.BboxBase.x1")
 (for that, use [`xmin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmin "matplotlib.transforms.BboxBase.xmin")
).

property x1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x1 "Link to this definition")

The second of the pair of _x_ coordinates that define the bounding box.

This is not guaranteed to be greater than [`x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.x0 "matplotlib.transforms.BboxBase.x0")
 (for that, use [`xmax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmax "matplotlib.transforms.BboxBase.xmax")
).

property xmax[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmax "Link to this definition")

The right edge of the bounding box.

property xmin[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmin "Link to this definition")

The left edge of the bounding box.

property y0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "Link to this definition")

The first of the pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be less than [`y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y1 "matplotlib.transforms.BboxBase.y1")
 (for that, use [`ymin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymin "matplotlib.transforms.BboxBase.ymin")
).

property y1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y1 "Link to this definition")

The second of the pair of _y_ coordinates that define the bounding box.

This is not guaranteed to be greater than [`y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.y0 "matplotlib.transforms.BboxBase.y0")
 (for that, use [`ymax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymax "matplotlib.transforms.BboxBase.ymax")
).

property ymax[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymax "Link to this definition")

The top edge of the bounding box.

property ymin[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymin "Link to this definition")

The bottom edge of the bounding box.

class matplotlib.transforms.BboxTransform(_boxin_, _boxout_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2585-L2624)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

[`BboxTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform "matplotlib.transforms.BboxTransform")
 linearly transforms points from one [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 to another.

Create a new [`BboxTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform "matplotlib.transforms.BboxTransform")
 that linearly transforms points from _boxin_ to _boxout_.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2608-L2624)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.transforms.BboxTransformFrom(_boxin_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2665-L2697)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformFrom "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

[`BboxTransformFrom`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformFrom "matplotlib.transforms.BboxTransformFrom")
 linearly transforms points from a given [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 to the unit bounding box.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2683-L2697)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformFrom.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformFrom.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.transforms.BboxTransformTo(_boxout_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2627-L2662)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

[`BboxTransformTo`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
 is a transformation that linearly transforms points from the unit bounding box to a given [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

Create a new [`BboxTransformTo`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
 that linearly transforms points from the unit bounding box to _boxout_.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2650-L2662)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.transforms.BlendedAffine2D(_x\_transform_, _y\_transform_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2324-L2374)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D "Link to this definition")

Bases: `_BlendedMixin`, [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A "blended" transform uses one transform for the _x_\-direction, and another transform for the _y_\-direction.

This version is an optimization for the case where both child transforms are of type [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")
.

Create a new "blended" transform using _x\_transform_ to transform the _x_\-axis and _y\_transform_ to transform the _y_\-axis.

Both _x\_transform_ and _y\_transform_ must be 2D affine transforms.

You will generally not call this constructor directly but use the [`blended_transform_factory`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
 function instead, which can determine automatically which kind of blended transform to create.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2361-L2374)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

is\_separable \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

class matplotlib.transforms.BlendedGenericTransform(_x\_transform_, _y\_transform_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2231-L2321)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform "Link to this definition")

Bases: `_BlendedMixin`, [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

A "blended" transform uses one transform for the _x_\-direction, and another transform for the _y_\-direction.

This "generic" version can handle any given child transform in the _x_\- and _y_\-directions.

Create a new "blended" transform using _x\_transform_ to transform the _x_\-axis and _y\_transform_ to transform the _y_\-axis.

You will generally not call this constructor directly but use the [`blended_transform_factory`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
 function instead, which can determine automatically which kind of blended transform to create.

contains\_branch(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2263-L2266)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.contains_branch "Link to this definition")

Return whether the given transform is a sub-tree of this transform.

This routine uses transform equality to identify sub-trees, therefore in many situations it is object id which will be used.

For the case where the given transform represents the whole of this transform, returns True.

property depth[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.depth "Link to this definition")

Return the number of transforms which have been chained together to form this Transform instance.

Note

For the special case of a Composite transform, the maximum depth of the two is returned.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2272-L2274)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2308-L2321)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.get_affine "Link to this definition")

Get the affine part of this transform.

property has\_inverse[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.has_inverse "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

input\_dims \= 2[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2304-L2306)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

property is\_affine[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.is_affine "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

is\_separable \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

output\_dims \= 2[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

pass\_through \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.pass_through "Link to this definition")

If pass\_through is True, all ancestors will always be invalidated, even if 'self' is already invalid.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2276-L2302)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedGenericTransform.transform_non_affine "Link to this definition")

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

class matplotlib.transforms.CompositeAffine2D(_a_, _b_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2505-L2555)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeAffine2D "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A composite transform formed by applying transform _a_ then transform _b_.

This version is an optimization that handles the case where both _a_ and _b_ are 2D affines.

Create a new composite transform that is the result of applying [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")
 _a_ then [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")
 _b_.

You will generally not call this constructor directly but write `a + b` instead, which will automatically choose the best kind of composite transform instance to create.

property depth[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeAffine2D.depth "Link to this definition")

Return the number of transforms which have been chained together to form this Transform instance.

Note

For the special case of a Composite transform, the maximum depth of the two is returned.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2547-L2555)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeAffine2D.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

class matplotlib.transforms.CompositeGenericTransform(_a_, _b_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2391-L2502)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

A composite transform formed by applying transform _a_ then transform _b_.

This "generic" version can handle any two arbitrary transformations.

Create a new composite transform that is the result of applying transform _a_ then transform _b_.

You will generally not call this constructor directly but write `a + b` instead, which will automatically choose the best kind of composite transform instance to create.

contains\_branch\_separately(_other\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2450-L2457)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.contains_branch_separately "Link to this definition")

Return whether the given branch is a sub-tree of this transform on each separate dimension.

A common use for this method is to identify if a transform is a blended transform containing an Axes' data transform. e.g.:

x\_isdata, y\_isdata \= trans.contains\_branch\_separately(ax.transData)

property depth[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.depth "Link to this definition")

Return the number of transforms which have been chained together to form this Transform instance.

Note

For the special case of a Composite transform, the maximum depth of the two is returned.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2421-L2428)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2491-L2497)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.get_affine "Link to this definition")

Get the affine part of this transform.

property has\_inverse[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.has_inverse "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2499-L2502)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

property is\_affine[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.is_affine "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

property is\_separable[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.is_separable "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

pass\_through \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.pass_through "Link to this definition")

If pass\_through is True, all ancestors will always be invalidated, even if 'self' is already invalid.

transform\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2468-L2470)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.transform_affine "Link to this definition")

Apply only the affine part of this transformation on the given array of values.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally a no-op. In affine transformations, this is equivalent to `transform(values)`.

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

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2472-L2479)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.transform_non_affine "Link to this definition")

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

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2481-L2489)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

class matplotlib.transforms.IdentityTransform(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2163-L2210)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A special class that does one thing, the identity transform, in a fast way.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2170-L2172)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2204-L2206)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.get_affine "Link to this definition")

Get the affine part of this transform.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2176-L2178)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2208-L2210)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2180-L2182)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform "Link to this definition")

Apply this transformation on the given array of _values_.

Parameters:

**values**array-like

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

transform\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2184-L2186)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform_affine "Link to this definition")

Apply only the affine part of this transformation on the given array of values.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally a no-op. In affine transformations, this is equivalent to `transform(values)`.

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

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2188-L2190)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform_non_affine "Link to this definition")

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

transform\_path(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2192-L2194)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform_path "Link to this definition")

Apply the transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

In some cases, this transform may insert curves into the path that began as line segments.

transform\_path\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2196-L2198)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform_path_affine "Link to this definition")

Apply the affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2200-L2202)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

class matplotlib.transforms.LockableBbox(_bbox_, _x0\=None_, _y0\=None_, _x1\=None_, _y1\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1207-L1325)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox "Link to this definition")

Bases: [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

A [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 where some elements may be locked at certain values.

When the child bounding box changes, the bounds of this bbox will update accordingly with the exception of the locked elements.

Parameters:

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

The child bounding box to wrap.

**x0**float or None

The locked value for x0, or None to leave unlocked.

**y0**float or None

The locked value for y0, or None to leave unlocked.

**x1**float or None

The locked value for x1, or None to leave unlocked.

**y1**float or None

The locked value for y1, or None to leave unlocked.

get\_points()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1245-L1253)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox.get_points "Link to this definition")

property locked\_x0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox.locked_x0 "Link to this definition")

float or None: The value used for the locked x0.

property locked\_x1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox.locked_x1 "Link to this definition")

float or None: The value used for the locked x1.

property locked\_y0[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox.locked_y0 "Link to this definition")

float or None: The value used for the locked y0.

property locked\_y1[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.LockableBbox.locked_y1 "Link to this definition")

float or None: The value used for the locked y1.

class matplotlib.transforms.ScaledTranslation(_xt_, _yt_, _scale\_trans_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2700-L2723)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

A transformation that translates by _xt_ and _yt_, after _xt_ and _yt_ have been transformed by _scale\_trans_.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2715-L2723)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

class matplotlib.transforms.Transform(_shorthand\_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1328-L1742)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "Link to this definition")

Bases: [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")

The base class of all [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")
 instances that actually perform a transformation.

All non-affine transformations should be subclasses of this class. New affine transformations should be subclasses of [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
.

Subclasses of this class should override the following members (at minimum):

*   [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
    
*   [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
    
*   [`transform()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
    
*   [`inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
     (if an inverse exists)
    

The following attributes may be overridden if the default is unsuitable:

*   [`is_separable`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.is_separable "matplotlib.transforms.Transform.is_separable")
     (defaults to True for 1D -> 1D transforms, False otherwise)
    
*   [`has_inverse`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.has_inverse "matplotlib.transforms.Transform.has_inverse")
     (defaults to True if [`inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
     is overridden, False otherwise)
    

If the transform needs to do something non-standard with [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 objects, such as adding curves where there were once line segments, it should override:

*   [`transform_path()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_path "matplotlib.transforms.Transform.transform_path")
    

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

\_\_add\_\_(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1392-L1401)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.__add__ "Link to this definition")

Compose two transforms together so that _self_ is followed by _other_.

`A + B` returns a transform `C` so that `C.transform(x) == B.transform(A.transform(x))`.

\_\_sub\_\_(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1475-L1523)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.__sub__ "Link to this definition")

Compose _self_ with the inverse of _other_, cancelling identical terms if any:

\# In general:
A \- B \== A + B.inverted()
\# (but see note regarding frozen transforms below).

\# If A "ends with" B (i.e. A == A' + B for some A') we can cancel
\# out B:
(A' + B) - B == A'

\# Likewise, if B "starts with" A (B = A + B'), we can cancel out A:
A \- (A + B') == B'.inverted() \== B'^-1

Cancellation (rather than naively returning `A + B.inverted()`) is important for multiple reasons:

*   It avoids floating-point inaccuracies when computing the inverse of B: `B - B` is guaranteed to cancel out exactly (resulting in the identity transform), whereas `B + B.inverted()` may differ by a small epsilon.
    
*   `B.inverted()` always returns a frozen transform: if one computes `A + B + B.inverted()` and later mutates `B`, then `B.inverted()` won't be updated and the last two terms won't cancel out anymore; on the other hand, `A + B - B` will always be equal to `A` even if `B` is mutated.
    

contains\_branch(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1433-L1450)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.contains_branch "Link to this definition")

Return whether the given transform is a sub-tree of this transform.

This routine uses transform equality to identify sub-trees, therefore in many situations it is object id which will be used.

For the case where the given transform represents the whole of this transform, returns True.

contains\_branch\_separately(_other\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1452-L1468)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.contains_branch_separately "Link to this definition")

Return whether the given branch is a sub-tree of this transform on each separate dimension.

A common use for this method is to identify if a transform is a blended transform containing an Axes' data transform. e.g.:

x\_isdata, y\_isdata \= trans.contains\_branch\_separately(ax.transData)

property depth[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.depth "Link to this definition")

Return the number of transforms which have been chained together to form this Transform instance.

Note

For the special case of a Composite transform, the maximum depth of the two is returned.

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1629-L1631)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.get_affine "Link to this definition")

Get the affine part of this transform.

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1633-L1635)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

has\_inverse \= False[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= None[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1732-L1742)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

is\_separable \= False[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.is_separable "Link to this definition")

True if this transform is separable in the x- and y- dimensions.

output\_dims \= None[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1529-L1564)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "Link to this definition")

Apply this transformation on the given array of _values_.

Parameters:

**values**array-like

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

transform\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1566-L1590)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_affine "Link to this definition")

Apply only the affine part of this transformation on the given array of values.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally a no-op. In affine transformations, this is equivalent to `transform(values)`.

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

transform\_angles(_angles_, _pts_, _radians\=False_, _pushoff\=1e-05_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1683-L1730)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_angles "Link to this definition")

Transform a set of angles anchored at specific locations.

Parameters:

**angles**(N,) array-like

The angles to transform.

**pts**(N, 2) array-like

The points where the angles are anchored.

**radians**bool, default: False

Whether _angles_ are radians or degrees.

**pushoff**float

For each point in _pts_ and angle in _angles_, the transformed angle is computed by transforming a segment of length _pushoff_ starting at that point and making that angle relative to the horizontal axis, and measuring the angle between the horizontal axis and the transformed segment.

Returns:

(N,) array

transform\_bbox(_bbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1620-L1627)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_bbox "Link to this definition")

Transform the given bounding box.

For smarter transforms including caching (a common requirement in Matplotlib), see [`TransformedBbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1592-L1618)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_non_affine "Link to this definition")

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

transform\_path(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1653-L1660)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_path "Link to this definition")

Apply the transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

In some cases, this transform may insert curves into the path that began as line segments.

transform\_path\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1662-L1670)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_path_affine "Link to this definition")

Apply the affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1672-L1681)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

transform\_point(_point_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1637-L1651)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_point "Link to this definition")

Return a transformed point.

This function is only kept for backcompatibility; the more general [`transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
 method is capable of transforming both a list of points and a single point.

The point is given as a sequence of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
. The transformed point is returned as a sequence of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
.

class matplotlib.transforms.TransformNode(_shorthand\_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L82-L204)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The base class for anything that participates in the transform tree and needs to invalidate its parents or be invalidated. This includes classes that are not really transforms, such as bounding boxes, since some transforms depend on bounding boxes to compute their values.

Parameters:

**shorthand\_name**str

A string representing the "name" of the transform. The name carries no significance other than to improve the readability of `str(transform)` when DEBUG=True.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L197-L204)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

invalidate()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L154-L161)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode.invalidate "Link to this definition")

Invalidate this [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")
 and triggers an invalidation of its ancestors. Should be called any time the transform changes.

is\_affine \= False[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode.is_affine "Link to this definition")

pass\_through \= False[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode.pass_through "Link to this definition")

If pass\_through is True, all ancestors will always be invalidated, even if 'self' is already invalid.

set\_children(_\*children_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L178-L195)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode.set_children "Link to this definition")

Set the children of the transform, to let the invalidation system know which transforms can invalidate this transform. Should be called from the constructor of any transforms that depend on other transforms.

class matplotlib.transforms.TransformWrapper(_child_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1745-L1820)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

A helper class that holds a single child transform and acts equivalently to it.

This is useful if a node of the transform tree must be replaced at run time with a transform of a different type. This class allows that replacement to correctly trigger invalidation.

[`TransformWrapper`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper "matplotlib.transforms.TransformWrapper")
 instances must have the same input and output dimensions during their entire lifetime, so the child transform may only be replaced with another child transform of the same dimensions.

_child_: A [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance. This child may later be replaced with [`set()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.set "matplotlib.transforms.TransformWrapper.set")
.

frozen()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1775-L1777)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.frozen "Link to this definition")

Return a frozen copy of this transform node. The frozen copy will not be updated when its children change. Useful for storing a previously known state of a transform where `copy.deepcopy()` might normally be used.

property has\_inverse[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.has_inverse "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

property input\_dims[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.input_dims "Link to this definition")

The type of the None singleton.

property is\_affine[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.is_affine "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

property is\_separable[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.is_separable "Link to this definition")

Returns True when the argument is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

property output\_dims[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.output_dims "Link to this definition")

The type of the None singleton.

pass\_through \= True[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.pass_through "Link to this definition")

If pass\_through is True, all ancestors will always be invalidated, even if 'self' is already invalid.

set(_child_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1779-L1814)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformWrapper.set "Link to this definition")

Replace the current child of this transform with another one.

The new child must have the same number of input and output dimensions as the current child.

class matplotlib.transforms.TransformedBbox(_bbox_, _transform_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1132-L1204)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "Link to this definition")

Bases: [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

A [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 that is automatically transformed by a given transform. When either the child bounding box or transform changes, the bounds of this bbox will update accordingly.

Parameters:

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

contains(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1198-L1200)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox.contains "Link to this definition")

Return whether `(x, y)` is in the bounding box or on its edge.

fully\_contains(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1202-L1204)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox.fully_contains "Link to this definition")

Return whether `x, y` is in the bounding box, but not on its edge.

get\_points()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L1160-L1188)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox.get_points "Link to this definition")

class matplotlib.transforms.TransformedPatchPath(_patch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2849-L2873)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPatchPath "Link to this definition")

Bases: [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")

A [`TransformedPatchPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPatchPath "matplotlib.transforms.TransformedPatchPath")
 caches a non-affine transformed copy of the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
. This cached copy is automatically updated when the non-affine part of the transform or the patch changes.

Parameters:

**patch**[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")

class matplotlib.transforms.TransformedPath(_path_, _transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2778-L2846)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "Link to this definition")

Bases: [`TransformNode`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformNode "matplotlib.transforms.TransformNode")

A [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 caches a non-affine transformed copy of the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
. This cached copy is automatically updated when the non-affine part of the transform changes.

Note

Paths are considered immutable by this class. Any update to the path's vertices/codes will not trigger a transform recomputation.

Parameters:

**path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

get\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2845-L2846)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath.get_affine "Link to this definition")

get\_fully\_transformed\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2838-L2843)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath.get_fully_transformed_path "Link to this definition")

Return a fully-transformed copy of the child path.

get\_transformed\_path\_and\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2829-L2836)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath.get_transformed_path_and_affine "Link to this definition")

Return a copy of the child path, with the non-affine part of the transform already applied, along with the affine part of the path necessary to complete the transformation.

get\_transformed\_points\_and\_affine()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2818-L2827)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath.get_transformed_points_and_affine "Link to this definition")

Return a copy of the child path, with the non-affine part of the transform already applied, along with the affine part of the path necessary to complete the transformation. Unlike [`get_transformed_path_and_affine()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath.get_transformed_path_and_affine "matplotlib.transforms.TransformedPath.get_transformed_path_and_affine")
, no interpolation will be performed.

matplotlib.transforms.blended\_transform\_factory(_x\_transform_, _y\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2377-L2388)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "Link to this definition")

Create a new "blended" transform using _x\_transform_ to transform the _x_\-axis and _y\_transform_ to transform the _y_\-axis.

A faster version of the blended transform is returned for the case where both child transforms are affine.

matplotlib.transforms.composite\_transform\_factory(_a_, _b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2558-L2582)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.composite_transform_factory "Link to this definition")

Create a new composite transform that is the result of applying transform a then transform b.

Shortcut versions of the blended transform are provided for the case where both child transforms are affine, or one or the other is the identity transform.

Composite transforms may also be created using the '+' operator, e.g.:

c \= a + b

matplotlib.transforms.interval\_contains(_interval_, _val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2962-L2965)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.interval_contains "Link to this definition")

\[_Deprecated_\] Check, inclusively, whether an interval includes a given value.

Parameters:

**interval**(float, float)

The endpoints of the interval.

**val**float

Value to check is within interval.

Returns:

bool

Whether _val_ is within the _interval_.

Notes

Deprecated since version 3.11.

matplotlib.transforms.interval\_contains\_open(_interval_, _val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L3017-L3020)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.interval_contains_open "Link to this definition")

\[_Deprecated_\] Check, excluding endpoints, whether an interval includes a given value.

Parameters:

**interval**(float, float)

The endpoints of the interval.

**val**float

Value to check is within interval.

Returns:

bool

Whether _val_ is within the _interval_.

Notes

Deprecated since version 3.11.

matplotlib.transforms.nonsingular(_vmin_, _vmax_, _expander\=0.001_, _tiny\=1e-15_, _increasing\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L2934-L2937)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.nonsingular "Link to this definition")

\[_Deprecated_\] Modify the endpoints of a range as needed to avoid singularities.

Parameters:

**vmin, vmax**float

The initial endpoints.

**expander**float, default: 0.001

Fractional amount by which _vmin_ and _vmax_ are expanded if the original interval is too small, based on _tiny_.

**tiny**float, default: 1e-15

Threshold for the ratio of the interval to the maximum absolute value of its endpoints. If the interval is smaller than this, it will be expanded. This value should be around 1e-15 or larger; otherwise the interval will be approaching the double precision resolution limit.

**increasing**bool, default: True

If True, swap _vmin_, _vmax_ if _vmin_ > _vmax_.

Returns:

**vmin, vmax**float

Endpoints, expanded and/or swapped if necessary. If either input is inf or NaN, or if both inputs are 0 or very close to zero, it returns -_expander_, _expander_.

Notes

Deprecated since version 3.11.

matplotlib.transforms.offset\_copy(_trans_, _fig\=None_, _x\=0.0_, _y\=0.0_, _units\='inches'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/transforms.py#L3023-L3052)
[#](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "Link to this definition")

Return a new transform with an added offset.

Parameters:

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 subclass

Any transform, to which offset will be applied.

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, default: None

Current figure. It can be None if _units_ are 'dots'.

**x, y**float, default: 0.0

The offset to apply.

**units**{'inches', 'points', 'dots'}, default: 'inches'

Units of the offset.

Returns:

[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 subclass

Transform with applied offset.

On this page