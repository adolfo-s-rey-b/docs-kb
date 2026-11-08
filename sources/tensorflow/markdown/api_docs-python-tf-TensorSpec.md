[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/TensorSpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FTensorSpec&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_type_proto)
        
    *   [from\_spec](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#from_spec)
        
    *   [from\_tensor](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#from_tensor)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.TensorSpec Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#methods)
    *   [experimental\_as\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_as_proto)
        
    *   [experimental\_from\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_from_proto)
        
    *   [experimental\_type\_proto](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#experimental_type_proto)
        
    *   [from\_spec](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#from_spec)
        
    *   [from\_tensor](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#from_tensor)
        
    *   [is\_compatible\_with](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#is_compatible_with)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#most_specific_common_supertype)
        
    *   [most\_specific\_compatible\_type](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#most_specific_compatible_type)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/TensorSpec#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L916-L1218)

Describes the type of a tf.Tensor.

Inherits From: [`TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
, [`TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)

tf.TensorSpec(
        shape,
        dtype=tf.dtypes.float32,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Load video data](https://www.tensorflow.org/tutorials/load_data/video)<br>    <br>*   [Transfer learning for video classification with MoViNet](https://www.tensorflow.org/tutorials/video/transfer_learning_with_movinet)<br>    <br>*   [Video classification with a 3D convolutional neural network](https://www.tensorflow.org/tutorials/video/video_classification) |

    t = tf.constant([[1,2,3],[4,5,6]])

Contains metadata for describing the nature of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 objects accepted or returned by some TensorFlow APIs.

For example, it can be used to constrain the type of inputs accepted by a tf.function:

    @tf.function(input_signature=[tf.TensorSpec([1, None])])

Now the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 is able to assume that `t` is always of the type `tf.TensorSpec([1, None])` which will avoid retracing as well as enforce the type restriction on inputs.

As a result, the following call with tensor of type `tf.TensorSpec([1, 2])` triggers a trace and succeeds:

>>> constrained_foo(tf.constant([[1., 2]])).numpy()
    tracing...
    array([[1., 2.]], dtype=float32)

The following subsequent call with tensor of type `tf.TensorSpec([1, 4])` does not trigger a trace and succeeds:

>>> constrained_foo(tf.constant([[1., 2, 3, 4]])).numpy()
    array([[1., 2., 3., 4.], dtype=float32)\
\
But the following call with tensor of type `tf.TensorSpec([2, 2])` fails:\
\
>>> constrained_foo(tf.constant([[1., 2], [3, 4]])).numpy()\
    Traceback (most recent call last):\
    ...\
    TypeError: Binding inputs to tf.function `constrained_foo` failed ...\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `shape` | Value convertible to [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>. The shape of the tensor. |\
| `dtype` | Value convertible to [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. The type of the tensor values. |\
| `name` | Optional name for the Tensor. |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If shape is not convertible to a [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>, or dtype is not convertible to a [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `dtype` | Returns the `dtype` of elements in the tensor. |\
| `name` | Returns the (optionally provided) name of the described tensor. |\
| `shape` | Returns the `TensorShape` that represents the shape of the tensor. |\
| `value_type` | The Python type for values that are compatible with this TypeSpec. |\
\
Methods\
-------\
\
### `experimental_as_proto`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L976-L981)\
\
experimental_as_proto() -> struct_pb2.TensorSpecProto\
\
Returns a proto representation of the TensorSpec instance.\
\
### `experimental_from_proto`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L967-L974)\
\
@classmethod\
\
Returns a TensorSpec instance based on the serialized proto.\
\
### `experimental_type_proto`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L962-L965)\
\
@classmethod\
\
Returns the type of proto associated with TensorSpec serialization.\
\
### `from_spec`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L1125-L1137)\
\
@classmethod\
\
Returns a `TensorSpec` with the same shape and dtype as `spec`.\
\
    spec = tf.TensorSpec(shape=[8, 3], dtype=tf.int32, name="OriginalName")\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `spec` | The `TypeSpec` used to create the new `TensorSpec`. |\
| `name` | The name for the new `TensorSpec`. Defaults to `spec.name`. |\
\
### `from_tensor`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L1139-L1160)\
\
@classmethod\
\
Returns a `TensorSpec` that describes `tensor`.\
\
    tf.TensorSpec.from_tensor(tf.constant([1, 2, 3]))\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `tensor` | The [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> that should be described. |\
| `name` | A name for the `TensorSpec`. Defaults to `tensor.op.name`. |\
\
|     |\
| --- |\
| Returns |     |\
| A `TensorSpec` that describes `tensor`. |     |\
\
### `is_compatible_with`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L983-L995)\
\
is_compatible_with(\
        spec_or_tensor\
    )\
\
Returns True if spec\_or\_tensor is compatible with this TensorSpec.\
\
Two tensors are considered compatible if they have the same dtype and their shapes are compatible (see [`tf.TensorShape.is_compatible_with`](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_compatible_with)\
).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `spec_or_tensor` | A tf.TensorSpec or a tf.Tensor |\
\
|     |\
| --- |\
| Returns |     |\
| True if spec\_or\_tensor is compatible with self. |     |\
\
### `is_subtype_of`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L997-L1005)\
\
is_subtype_of(\
        other\
    )\
\
Returns True if `self` is a subtype of `other`.\
\
Implements the tf.types.experimental.func.TraceType interface.\
\
If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `other` | A TraceType object. |\
\
### `most_specific_common_supertype`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L148-L194)\
\
most_specific_common_supertype(\
        others: Sequence[tf.types.experimental.TraceType]\
    ) -> Optional['TypeSpec']\
\
Returns the most specific supertype TypeSpec of `self` and `others`.\
\
Implements the tf.types.experimental.func.TraceType interface.\
\
If not overridden by a subclass, the default behavior is to assume the TypeSpec is covariant upon attributes that implement TraceType and invariant upon rest of the attributes as well as the structure and type of the TypeSpec.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `others` | A sequence of TraceTypes. |\
\
### `most_specific_compatible_type`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L323-L341)\
\
most_specific_compatible_type(\
        other: 'TypeSpec'\
    ) -> 'TypeSpec'\
\
Returns the most specific TypeSpec compatible with `self` and `other`. (deprecated)\
\
Deprecated. Please use `most_specific_common_supertype` instead. Do not override this function.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `other` | A `TypeSpec`. |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If there is no TypeSpec that is compatible with both `self` and `other`. |\
\
### `__eq__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L895-L898)\
\
__eq__(\
        other\
    )\
\
Return self==value.\
\
### `__ne__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor.py#L900-L901)\
\
__ne__(\
        other\
    )\
\
Return self!=value.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.