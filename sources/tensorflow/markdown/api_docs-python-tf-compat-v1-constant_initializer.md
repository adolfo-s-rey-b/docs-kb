[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fconstant_initializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#examples)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.constant\_initializer Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#examples)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L219-L394)

Initializer that generates tensors with constant values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.constant`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer)

tf.compat.v1.constant_initializer(
        value=0,
        dtype=tf.dtypes.float32,
        verify_shape=False
    )

Migrate to TF2
--------------

Although it is a legacy API endpoint, [`tf.compat.v1.constant_initializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer)
 is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

To migrate to a non-legacy TF2 API, please use [`tf.constant_initializer`](https://www.tensorflow.org/api_docs/python/tf/constant_initializer)
 instead. The `dtype` argument in [`tf.compat.v1.constant_initializer.__init__()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer#__init__)
 does not exist in [`tf.constant_initializer.__init__()`](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#__init__)
. However, you can specify the `dtype` in `__call__()` in both cases.

In the [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 symbol, if `verify_shape` is set to `True`, an exception is raised when initializing a variable with a different shape from `value`. If set to `False`, `value` is reshaped to initialize the variable if necessary. An exception would only be raised when the number of elements are different.

The `verify_shape` argument is not supported in TF2. Using [`tf.constant_initializer`](https://www.tensorflow.org/api_docs/python/tf/constant_initializer)
 is equivalent to setting `verify_shape` to `False`.

#### Structural Mapping to TF2

Before:

value = [0, 1, 2, 3, 4, 5, 6, 7]
    initializer = tf.compat.v1.constant_initializer(
        value=value,
        dtype=tf.float32,
        verify_shape=False)
    variable = tf.Variable(initializer(shape=[2, 4]))

After:

value = [0, 1, 2, 3, 4, 5, 6, 7]
    initializer = tf.constant_initializer(value=value)
    tf.Variable(initializer(shape=[2, 4], dtype=tf.float32))

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `value` | `value` | In constructor |
| `dtype` | `dtype` | In `__call__()` method |
| `verify_shape` | Not Supported | Equivalent to set to `False` |
| `partition_info` | \-  | (`__call__` arg in TF1) Not supported |

#### Before & After Usage Example

Before:

    value = [1., 2., 3., 4.]

After:

    value = [1., 2., 3., 4.]

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping) |

The resulting tensor is populated with values of type `dtype`, as specified by arguments `value` following the desired `shape` of the new tensor (see examples below).

The argument `value` can be a constant value, or a list of values of type `dtype`. If `value` is a list, then the length of the list must be less than or equal to the number of elements implied by the desired shape of the tensor. In the case where the total number of elements in `value` is less than the number of elements required by the tensor shape, the last element in `value` will be used to fill the remaining entries. If the total number of elements in `value` is greater than the number of elements required by the tensor shape, the initializer will raise a `ValueError`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A Python scalar, list or tuple of values, or a N-dimensional numpy array. All elements of the initialized variable will be set to the corresponding value in the `value` argument. |
| `dtype` | Default data type, used if no `dtype` argument is provided when calling the initializer. |
| `verify_shape` | Boolean that enables verification of the shape of `value`. If `True`, the initializer will throw an error if the shape of `value` is not compatible with the shape of the initialized tensor. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the input `value` is not one of the expected types. |

|     |
| --- |
| Examples<br>-------- |     |
| The following example can be rewritten using a numpy.ndarray instead of the `value` list, even reshaped, as shown in the two commented lines below the `value` list initialization. |     |

    value = [0, 1, 2, 3, 4, 5, 6, 7]

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L75-L94)

@classmethod

Instantiates an initializer from a configuration dictionary.

#### Example:

initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary. It will typically be the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An Initializer instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L389-L394)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L381-L387)

__call__(
        shape, dtype=None, partition_info=None, verify_shape=None
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. If not provided use the initializer dtype. |
| `partition_info` | Optional information about the possible partitioning of a tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.