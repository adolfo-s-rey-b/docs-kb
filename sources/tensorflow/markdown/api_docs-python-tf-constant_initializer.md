[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/constant_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/constant_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.constant\_initializer Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/constant_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L204-L299)

Initializer that generates tensors with constant values.

tf.constant_initializer(
        value=0, support_partition=False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Probabilistic Layers: Regression](https://www.tensorflow.org/probability/examples/Probabilistic_Layers_Regression) |

Initializers allow you to pre-specify an initialization strategy, encoded in the Initializer object, without knowing the shape and dtype of the variable being initialized.

[`tf.constant_initializer`](https://www.tensorflow.org/api_docs/python/tf/constant_initializer)
 returns an object which when called returns a tensor populated with the `value` specified in the constructor. This `value` must be convertible to the requested `dtype`.

The argument `value` can be a scalar constant value, or a list of values. Scalars broadcast to whichever shape is requested from the initializer.

If `value` is a list, then the length of the list must be equal to the number of elements implied by the desired shape of the tensor. If the total number of elements in `value` is not equal to the number of elements required by the tensor shape, the initializer will raise a `TypeError`.

#### Examples:

    def make_variables(k, initializer):

    value = [0, 1, 2, 3, 4, 5, 6, 7]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A Python scalar, list or tuple of values, or a N-dimensional numpy array. All elements of the initialized variable will be set to the corresponding value in the `value` argument. |
| `support_partition` | If true, the initizer supports passing partition offset and partition shape arguments to variable creators. This is particularly useful when initializing sharded variables where each variable shard is initialized to a slice of constant initializer. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the input `value` is not one of the expected types. |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L76-L96)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L298-L299)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L280-L296)

__call__(
        shape, dtype=None, **kwargs
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. If not provided the dtype of the tensor created will be the type of the inital value. |
| `**kwargs` | Additional keyword arguments. |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If the initializer cannot create a tensor of the requested dtype. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.