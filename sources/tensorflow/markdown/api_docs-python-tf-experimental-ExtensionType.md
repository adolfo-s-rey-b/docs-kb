[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2FExtensionType&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#examples)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.ExtensionType Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#examples)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L99-L329)

Base class for TensorFlow `ExtensionType` classes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)

tf.experimental.ExtensionType(
        *args, **kwargs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

Tensorflow `ExtensionType` classes are specialized Python classes that can be used transparently with TensorFlow -- e.g., they can be used with ops such as [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
 or [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
 and used as inputs or outputs for [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 and Keras layers.

New `ExtensionType` classes are defined by creating a subclass of `tf.ExtensionType` that contains type annotations for all instance variables. The following type annotations are supported:

| Type | Example |
| --- | --- |
| Python integers | `i: int` |
| Python floats | `f: float` |
| Python strings | `s: str` |
| Python booleans | `b: bool` |
| Python None | `n: None` |
| Python tuple | `params: tuple[int, float, int, int]` |
| Python tuple w/ Ellipsis | `lengths: tuple[int, ...]` |
| Tensors | `t: tf.Tensor` |
| Composite Tensors | `rt: tf.RaggedTensor` |
| Extension Types | `m: MyMaskedTensor` |
| Tensor shapes | `shape: tf.TensorShape` |
| Tensor dtypes | `dtype: tf.DType` |
| Type unions | `length: typing.Union[int, float]` |
| Tuples | `params: typing.Tuple[int, float, int, int]` |
| Tuples w/ Ellipsis | `lengths: typing.Tuple[int, ...]` |
| Mappings | `tags: typing.Mapping[str, str]` |

Fields annotated with `typing.Mapping` will be stored using an immutable mapping type.

ExtensionType values are immutable -- i.e., once constructed, you can not modify or delete any of their instance members.

### Examples

    class MaskedTensor(ExtensionType):

    class Toy(ExtensionType):

    class ToyStore(ExtensionType):

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L276-L305)

__eq__(
        other
    )

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L307-L312)

__ne__(
        other
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.