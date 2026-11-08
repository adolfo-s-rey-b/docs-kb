[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/TensorShape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/TensorShape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/TensorShape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorShape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorShape#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorShape#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorShape#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorShape#methods)
    *   [as\_list](https://www.tensorflow.org/api_docs/python/tf/TensorShape#as_list)
        
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#as_proto)
        
    *   [assert\_has\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_has_rank)
        
    *   [assert\_is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_is_compatible_with)
        
    *   [assert\_is\_fully\_defined](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_is_fully_defined)
        
    *   [assert\_same\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_same_rank)
        
    *   [concatenate](https://www.tensorflow.org/api_docs/python/tf/TensorShape#concatenate)
        
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_compatible_with)
        
    *   [is\_fully\_defined](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_fully_defined)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_subtype_of)
        
    *   [merge\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#merge_with)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorShape#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_shape](https://www.tensorflow.org/api_docs/python/tf/TensorShape#most_specific_compatible_shape)
        
    *   [num\_elements](https://www.tensorflow.org/api_docs/python/tf/TensorShape#num_elements)
        
    *   [with\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank)
        
    *   [with\_rank\_at\_least](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank_at_least)
        
    *   [with\_rank\_at\_most](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank_at_most)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__add__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__bool__)
        
    *   [\_\_concat\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__concat__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__len__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__nonzero__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__radd__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.TensorShape Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorShape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorShape#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorShape#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorShape#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorShape#methods)
    *   [as\_list](https://www.tensorflow.org/api_docs/python/tf/TensorShape#as_list)
        
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#as_proto)
        
    *   [assert\_has\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_has_rank)
        
    *   [assert\_is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_is_compatible_with)
        
    *   [assert\_is\_fully\_defined](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_is_fully_defined)
        
    *   [assert\_same\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#assert_same_rank)
        
    *   [concatenate](https://www.tensorflow.org/api_docs/python/tf/TensorShape#concatenate)
        
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorShape#experimental_type_proto)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_compatible_with)
        
    *   [is\_fully\_defined](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_fully_defined)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_subtype_of)
        
    *   [merge\_with](https://www.tensorflow.org/api_docs/python/tf/TensorShape#merge_with)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorShape#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_shape](https://www.tensorflow.org/api_docs/python/tf/TensorShape#most_specific_compatible_shape)
        
    *   [num\_elements](https://www.tensorflow.org/api_docs/python/tf/TensorShape#num_elements)
        
    *   [with\_rank](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank)
        
    *   [with\_rank\_at\_least](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank_at_least)
        
    *   [with\_rank\_at\_most](https://www.tensorflow.org/api_docs/python/tf/TensorShape#with_rank_at_most)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__add__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__bool__)
        
    *   [\_\_concat\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__concat__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__len__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__nonzero__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorShape#__radd__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L747-L1516)

Represents the shape of a `Tensor`.

Inherits From: [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)

tf.TensorShape(
        dims
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [TensorFlow 1.x vs TensorFlow 2 - Behaviors and APIs](https://www.tensorflow.org/guide/migrate/tf1_vs_tf2)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns) | *   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [Tensorflow datasets from MongoDB collections](https://www.tensorflow.org/io/tutorials/mongodb) |

    t = tf.constant([[1,2,3],[4,5,6]])

`TensorShape` is the _static_ shape representation of a Tensor. During eager execution a Tensor always has a fully specified shape but when tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 it may be one of the following:

*   _Fully-known shape:_ has a known number of dimensions and a known size for each dimension. e.g. `TensorShape([16, 256])`
*   _Partially-known shape:_ has a known number of dimensions, and an unknown size for one or more dimension. e.g. `TensorShape([None, 256])`
*   _Unknown shape:_ has an unknown number of dimensions, and an unknown size in all dimensions. e.g. `TensorShape(None)`

During function tracing `t.shape` will return a `TensorShape` object representing the shape of Tensor as it is known during tracing. This static representation will be partially defined in cases where the exact shape depends on the values within the tensors. To get the _dynamic_ representation, please use [`tf.shape(t)`](https://www.tensorflow.org/api_docs/python/tf/shape)
 which will return Tensor representing the fully defined shape of `t`. This way, you can express logic that manipulates the shapes of tensors by building other tensors that depend on the dynamic shape of `t`.

For example, this function prints the `TensorShape' (`t.shape`), when you trace the function, and returns a tensor <a href="../tf/shape"><code>tf.shape(t)</code></a> for given input`t\`:

    @tf.function

Just calling the function traces it with a fully-specified static shape:

    result = get_dynamic_shape(tf.constant([[1, 1, 1], [0, 0, 0]]))

But [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 can also trace the function with a partially specified (or even unspecified) shape:

    cf1 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(

    cf2 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(shape=None))

If a tensor is produced by an operation of type `"Foo"`, its shape may be inferred if there is a registered shape function for `"Foo"`. See [Shape functions](https://www.tensorflow.org/guide/create_op#shape_functions_in_c)
 for details of shape functions and how to register them. Alternatively, you may set the shape explicitly using `tf.Tensor.ensure_shape`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dims` | A list of Dimensions, or None if the shape is unspecified. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If dims cannot be converted to a list of dimensions. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dims` | Deprecated. Returns list of dimensions for this shape.<br><br>Suggest [`TensorShape.as_list`](https://www.tensorflow.org/api_docs/python/tf/TensorShape#as_list)<br> instead. |
| `ndims` | Deprecated accessor for `rank`. |
| `rank` | Returns the rank of this shape, or None if it is unspecified. |

Methods
-------

### `as_list`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1431-L1442)

as_list()

Returns a list of integers or `None` for each dimension.

|     |
| --- |
| Returns |     |
| A list of integers or `None` for each dimension. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` is an unknown shape with an unknown rank. |

### `as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1444-L1452)

as_proto()

Returns this shape as a `TensorShapeProto`.

### `assert_has_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1097-L1107)

assert_has_rank(
        rank
    )

Raises an exception if `self` is not compatible with the given `rank`.

|     |     |
| --- | --- |
| Args |     |
| `rank` | An integer. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` does not represent a shape with the given `rank`. |

### `assert_is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1372-L1385)

assert_is_compatible_with(
        other
    )

Raises exception if `self` and `other` do not represent the same shape.

This method can be used to assert that there exists a shape that both `self` and `other` represent.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another TensorShape. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` and `other` do not represent the same shape. |

### `assert_is_fully_defined`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1422-L1429)

assert_is_fully_defined()

Raises an exception if `self` is not fully defined in every dimension.

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` does not have a known value for every dimension. |

### `assert_same_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1081-L1095)

assert_same_rank(
        other
    )

Raises an exception if `self` and `other` do not have compatible ranks.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `TensorShape`. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` and `other` do not represent shapes with the same rank. |

### `concatenate`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1058-L1079)

concatenate(
        other
    )

Returns the concatenation of the dimension in `self` and `other`.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `TensorShape`. |

|     |
| --- |
| Returns |     |
| A `TensorShape` whose dimensions are the concatenation of the dimensions in `self` and `other`. |     |

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1319-L1321)

experimental_as_proto() -> tensor_shape_pb2.TensorShapeProto

Returns a proto representation of the TensorShape instance.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1313-L1317)

@classmethod

Returns a TensorShape instance based on the serialized proto.

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1308-L1311)

@classmethod

Returns the type of proto associated with TensorShape serialization.

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1324-L1370)

is_compatible_with(
        other
    )

Returns True iff `self` is compatible with `other`.

Two possibly-partially-defined shapes are compatible if there exists a fully-defined shape that both shapes can represent. Thus, compatibility allows the shape inference code to reason about partially-defined shapes. For example:

*   TensorShape(None) is compatible with all shapes.
    
*   TensorShape(\[None, None\]) is compatible with all two-dimensional shapes, such as TensorShape(\[32, 784\]), and also TensorShape(None). It is not compatible with, for example, TensorShape(\[None\]) or TensorShape(\[None, None, None\]).
    
*   TensorShape(\[32, None\]) is compatible with all two-dimensional shapes with size 32 in the 0th dimension, and also TensorShape(\[None, None\]) and TensorShape(None). It is not compatible with, for example, TensorShape(\[32\]), TensorShape(\[32, None, 1\]) or TensorShape(\[64, None\]).
    
*   TensorShape(\[32, 784\]) is compatible with itself, and also TensorShape(\[32, None\]), TensorShape(\[None, 784\]), TensorShape(\[None, None\]) and TensorShape(None). It is not compatible with, for example, TensorShape(\[32, 1, 784\]) or TensorShape(\[None\]).
    

The compatibility relation is reflexive and symmetric, but not transitive. For example, TensorShape(\[32, 784\]) is compatible with TensorShape(None), and TensorShape(None) is compatible with TensorShape(\[4, 4\]), but TensorShape(\[32, 784\]) is not compatible with TensorShape(\[4, 4\]).

|     |     |
| --- | --- |
| Args |     |
| `other` | Another TensorShape. |

|     |
| --- |
| Returns |     |
| True iff `self` is compatible with `other`. |     |

### `is_fully_defined`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1417-L1420)

is_fully_defined()

Returns True iff `self` is fully defined in every dimension.

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1167-L1225)

is_subtype_of(
        other: tf.types.experimental.TraceType
    ) -> bool

Returns True iff `self` is subtype of `other`.

Shape A is a subtype of shape B if shape B can successfully represent it:

*   A `TensorShape` of any rank is a subtype of `TensorShape(None)`.
    
*   TensorShapes of equal ranks are covariant, i.e. `TensorShape([A1, A2, ..])` is a subtype of `TensorShape([B1, B2, ..])` iff An is a subtype of Bn.
    
    An is subtype of Bn iff An == Bn or Bn is None.
    
*   TensorShapes of different defined ranks have no subtyping relation.
    

The subtyping relation is reflexive and transitive, but not symmetric.

#### Some examples:

*   `TensorShape([32, 784])` is a subtype of `TensorShape(None)`, and `TensorShape([4, 4])` is also a subtype of `TensorShape(None)` but `TensorShape([32, 784])` and `TensorShape([4, 4])` are not subtypes of each other.
    
*   All two-dimensional shapes are subtypes of `TensorShape([None, None])`, such as `TensorShape([32, 784])`. There is no subtype relationship with, for example, `TensorShape([None])` or `TensorShape([None, None, None])`.
    
*   `TensorShape([32, None])` is also a subtype of `TensorShape([None, None])` and `TensorShape(None)`. It is not a subtype of, for example, `TensorShape([32])`, `TensorShape([32, None, 1])`, `TensorShape([64, None])` or `TensorShape([None, 32])`.
    
*   `TensorShape([32, 784])` is a subtype of itself, and also `TensorShape([32, None])`, `TensorShape([None, 784])`, `TensorShape([None, None])` and `TensorShape(None)`. It has no subtype relation with, for example, `TensorShape([32, 1, 784])` or `TensorShape([None])`.
    

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `TensorShape`. |

|     |
| --- |
| Returns |     |
| True iff `self` is subtype of `other`. |     |

### `merge_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L998-L1048)

merge_with(
        other
    )

Returns a `TensorShape` combining the information in `self` and `other`.

The dimensions in `self` and `other` are merged element-wise, according to the rules below:

Dimension(n).merge_with(Dimension(None)) == Dimension(n)
    Dimension(None).merge_with(Dimension(n)) == Dimension(n)
    Dimension(None).merge_with(Dimension(None)) == Dimension(None)
    # raises ValueError for n != m
    Dimension(n).merge_with(Dimension(m))

> > ts = tf.TensorShape(\[1,2\]) ot1 = tf.TensorShape(\[1,2\]) ts.merge\_with(ot).as\_list() \[1,2\]

> > ot2 = tf.TensorShape(\[1,None\]) ts.merge\_with(ot2).as\_list() \[1,2\]

> > ot3 = tf.TensorShape(\[None, None\]) ot3.merge\_with(ot2).as\_list() \[1, None\]

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `TensorShape`. |

|     |
| --- |
| Returns |     |
| A `TensorShape` containing the combined information of `self` and `other`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` and `other` are not compatible. |

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1227-L1281)

most_specific_common_supertype(
        others: Sequence[tf.types.experimental.TraceType]
    ) -> Optional['TensorShape']

Returns the most specific supertype `TensorShape` of self and others.

*   `TensorShape([None, 1])` is the most specific `TensorShape` supertyping both `TensorShape([2, 1])` and `TensorShape([5, 1])`. Note that `TensorShape(None)` is also a supertype but it is not "most specific".
    
*   `TensorShape([1, 2, 3])` is the most specific `TensorShape` supertyping both `TensorShape([1, 2, 3])` and `TensorShape([1, 2, 3]`). There are other less specific TensorShapes that supertype above mentioned TensorShapes, e.g. `TensorShape([1, 2, None])`, `TensorShape(None)`.
    
    *   `TensorShape([None, None])` is the most specific `TensorShape` supertyping both `TensorShape([2, None])` and `TensorShape([None, 3])`. As always, `TensorShape(None)` is also a supertype but not the most specific one.
        
    *   `TensorShape(None`) is the only `TensorShape` supertyping both `TensorShape([1, 2, 3])` and `TensorShape([1, 2])`. In general, any two shapes that have different ranks will only have `TensorShape(None)` as a common supertype.
        
    *   `TensorShape(None)` is the only `TensorShape` supertyping both `TensorShape([1, 2, 3])` and `TensorShape(None)`. In general, the common supertype of any shape with `TensorShape(None)` is `TensorShape(None)`.
        

|     |     |
| --- | --- |
| Args |     |
| `others` | Sequence of `TensorShape`. |

|     |
| --- |
| Returns |     |
| A `TensorShape` which is the most specific supertype shape of `self` and `others`. None if it does not exist. |     |

### `most_specific_compatible_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1387-L1415)

most_specific_compatible_shape(
        other
    ) -> 'TensorShape'

Returns the most specific TensorShape compatible with `self` and `other`.

*   TensorShape(\[None, 1\]) is the most specific TensorShape compatible with both TensorShape(\[2, 1\]) and TensorShape(\[5, 1\]). Note that TensorShape(None) is also compatible with above mentioned TensorShapes.
    
*   TensorShape(\[1, 2, 3\]) is the most specific TensorShape compatible with both TensorShape(\[1, 2, 3\]) and TensorShape(\[1, 2, 3\]). There are more less specific TensorShapes compatible with above mentioned TensorShapes, e.g. TensorShape(\[1, 2, None\]), TensorShape(None).
    

|     |     |
| --- | --- |
| Args |     |
| `other` | Another `TensorShape`. |

|     |
| --- |
| Returns |     |
| A `TensorShape` which is the most specific compatible shape of `self` and `other`. |     |

### `num_elements`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L991-L996)

num_elements()

Returns the total number of elements, or none for incomplete shapes.

### `with_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1109-L1127)

with_rank(
        rank
    )

Returns a shape based on `self` with the given rank.

This method promotes a completely unknown shape to one with a known rank.

|     |     |
| --- | --- |
| Args |     |
| `rank` | An integer. |

|     |
| --- |
| Returns |     |
| A shape that is at least as specific as `self` with the given rank. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` does not represent a shape with the given `rank`. |

### `with_rank_at_least`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1129-L1146)

with_rank_at_least(
        rank
    )

Returns a shape based on `self` with at least the given rank.

|     |     |
| --- | --- |
| Args |     |
| `rank` | An integer. |

|     |
| --- |
| Returns |     |
| A shape that is at least as specific as `self` with at least the given rank. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` does not represent a shape with at least the given `rank`. |

### `with_rank_at_most`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1148-L1165)

with_rank_at_most(
        rank
    )

Returns a shape based on `self` with at most the given rank.

|     |     |
| --- | --- |
| Args |     |
| `rank` | An integer. |

|     |
| --- |
| Returns |     |
| A shape that is at least as specific as `self` with at most the given rank. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `self` does not represent a shape with at most the given `rank`. |

### `__add__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1050-L1051)

__add__(
        other
    )

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L924-L926)

__bool__()

Returns True if this shape contains non-zero information.

### `__concat__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1515-L1516)

__concat__(
        other
    )

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1454-L1507)

__eq__(
        other
    )

Returns True if `self` is equivalent to `other`.

It first tries to convert `other` to `TensorShape`. `TypeError` is thrown when the conversion fails. Otherwise, it compares each element in the TensorShape dimensions.

*   Two _Fully known_ shapes, return True iff each element is equal.

>>> t_a = tf.TensorShape([1,2])
    >>> a = [1, 2]
    >>> t_b = tf.TensorShape([1,2])
    >>> t_c = tf.TensorShape([1,2,3])
    >>> t_a.__eq__(a)
    True
    >>> t_a.__eq__(t_b)
    True
    >>> t_a.__eq__(t_c)
    False

*   Two _Partially-known_ shapes, return True iff each element is equal.

>>> p_a = tf.TensorShape([1,None])
    >>> p_b = tf.TensorShape([1,None])
    >>> p_c = tf.TensorShape([2,None])
    >>> p_a.__eq__(p_b)
    True
    >>> t_a.__eq__(p_a)
    False
    >>> p_a.__eq__(p_c)
    False

*   Two _Unknown shape_, return True.

>>> unk_a = tf.TensorShape(None)
    >>> unk_b = tf.TensorShape(None)
    >>> unk_a.__eq__(unk_b)
    True
    >>> unk_a.__eq__(t_a)
    False

|     |     |
| --- | --- |
| Args |     |
| `other` | A `TensorShape` or type that can be converted to `TensorShape`. |

|     |
| --- |
| Returns |     |
| True if the dimensions are all equal. |     |

|     |
| --- |
| Raises |     |
| TypeError if `other` can not be converted to `TensorShape`. |     |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L941-L989)

__getitem__(
        key
    )

Returns the value of a dimension or a shape, depending on the key.

|     |     |
| --- | --- |
| Args |     |
| `key` | If `key` is an integer, returns the dimension at that index; otherwise if `key` is a slice, returns a TensorShape whose dimensions are those selected by the slice from `self`. |

|     |
| --- |
| Returns |     |
| An integer if `key` is an integer, or a `TensorShape` if `key` is a slice. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `key` is a slice and `self` is completely unknown and the step is set. |

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L931-L939)

__iter__()

Returns `self.dims` if the rank is known, otherwise raises ValueError.

### `__len__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L918-L922)

__len__()

Returns the rank of this shape, or raises ValueError if unspecified.

### `__nonzero__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L924-L926)

__nonzero__()

Returns True if this shape contains non-zero information.

### `__radd__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L1053-L1056)

__radd__(
        other
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.