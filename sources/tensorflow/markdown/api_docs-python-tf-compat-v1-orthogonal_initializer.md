[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Forthogonal_initializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#args)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#references)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.orthogonal\_initializer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#args)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#references)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L895-L963)

Initializer that generates an orthogonal matrix.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.orthogonal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer)

tf.compat.v1.orthogonal_initializer(
        gain=1.0,
        seed=None,
        dtype=tf.dtypes.float32
    )

If the shape of the tensor to initialize is two-dimensional, it is initialized with an orthogonal matrix obtained from the QR decomposition of a matrix of random numbers drawn from a normal distribution. If the matrix has fewer rows than columns then the output will have orthogonal rows. Otherwise, the output will have orthogonal columns.

If the shape of the tensor to initialize is more than two-dimensional, a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])` is initialized, where `n` is the length of the shape vector. The matrix is subsequently reshaped to give a tensor of the desired shape.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `gain` | multiplicative factor to apply to the orthogonal matrix |
| `seed` | A Python integer. Used to create random seeds. See [`tf.compat.v1.set_random_seed`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)<br> for behavior. |
| `dtype` | Default data type, used if no `dtype` argument is provided when calling the initializer. Only floating point types are supported. |

|     |
| --- |
| References<br>---------- |     |
| [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)<br> ([pdf](https://arxiv.org/pdf/1312.6120.pdf)<br>) |     |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L962-L963)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L931-L960)

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