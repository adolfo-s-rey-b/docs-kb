[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Frandom_normal_initializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.random\_normal\_initializer Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L487-L574)

Initializer that generates tensors with a normal distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.random_normal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer)

tf.compat.v1.random_normal_initializer(
        mean=0.0,
        stddev=1.0,
        seed=None,
        dtype=tf.dtypes.float32
    )

Migrate to TF2
--------------

Although it is a legacy [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 API, this symbol is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

To switch to TF2, switch to using either `tf.initializers.RandomNormal` or [`tf.keras.initializers.RandomNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomNormal)
 (neither from [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
) and pass the dtype when calling the initializer. Keep in mind that the default stddev and the behavior of fixed seeds have changed.

#### Structural Mapping to TF2

Before:

initializer = tf.compat.v1.random_normal_initializer(
      mean=mean,
      stddev=stddev,
      seed=seed,
      dtype=dtype)
    
    weight_one = tf.Variable(initializer(shape_one))
    weight_two = tf.Variable(initializer(shape_two))

After:

initializer = tf.initializers.RandomNormal(
      mean=mean,
      seed=seed,
      stddev=stddev)
    
    weight_one = tf.Variable(initializer(shape_one, dtype=dtype))
    weight_two = tf.Variable(initializer(shape_two, dtype=dtype))

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `mean` | `mean` | No change to defaults |
| `stddev` | `stddev` | Default changes from 1.0 to 0.05 |
| `seed` | `seed` |     |
| `dtype` | `dtype` | The TF2 native api only takes it as a `__call__` arg, not a constructor arg. |
| `partition_info` | \-  | (`__call__` arg in TF1) Not supported. |

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mean` | a python scalar or a scalar tensor. Mean of the random values to generate. |
| `stddev` | a python scalar or a scalar tensor. Standard deviation of the random values to generate. |
| `seed` | A Python integer. Used to create random seeds. See [`tf.compat.v1.set_random_seed`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)<br> for behavior. |
| `dtype` | Default data type, used if no `dtype` argument is provided when calling the initializer. Only floating point types are supported. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L568-L574)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L562-L566)

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