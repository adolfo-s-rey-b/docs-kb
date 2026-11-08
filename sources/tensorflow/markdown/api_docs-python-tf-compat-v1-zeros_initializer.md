[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fzeros_initializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#used-in-the-notebooks)
        
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.zeros\_initializer Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#used-in-the-notebooks)
        
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L97-L179)

Initializer that generates tensors initialized to 0.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.zeros`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer)

tf.compat.v1.zeros_initializer(
        dtype=tf.dtypes.float32
    )

Migrate to TF2
--------------

[`tf.compat.v1.zeros_initializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer)
 is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

To migrate to TF2, please use [`tf.zeros_initializer`](https://www.tensorflow.org/api_docs/python/tf/zeros_initializer)
 instead. The `dtype` argument in [`tf.compat.v1.zeros_initializer.__init__()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer#__init__)
 does not exist in [`tf.zeros_initializer.__init__()`](https://www.tensorflow.org/api_docs/python/tf/zeros_initializer#__init__)
. However, you can specify the `dtype` in `__call__()` in both cases.

#### Structural Mapping to TF2

Before:

initializer = tf.compat.v1.zeros_initializer(dtype=tf.float32)
    variable = tf.Variable(initializer(shape=[3, 3]))

After:

initializer = tf.zeros_initializer()
    variable = tf.Variable(initializer(shape=[3, 3], dtype=tf.float32))

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `dtype` | `dtype` | In `__call__()` method |
| `partition_info` | \-  | (`__call__` arg in TF1) Not supported |

#### Before & After Usage Example

Before:

    initializer = tf.compat.v1.zeros_initializer(dtype=tf.float32)

After:

    initializer = tf.zeros_initializer()

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints) |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L178-L179)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L173-L176)

__call__(
        shape, dtype=None, partition_info=None
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