[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#get_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.InputSpec Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec#get_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/input_spec.py#L6-L119)

Specifies the rank, dtype and shape of every input to a layer.

#### View aliases

**Main aliases**

[`tf.keras.layers.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)

tf.keras.InputSpec(
        dtype=None,
        shape=None,
        ndim=None,
        max_ndim=None,
        min_ndim=None,
        axes=None,
        allow_last_axis_squeeze=False,
        name=None,
        optional=False
    )

Layers can expose (if appropriate) an `input_spec` attribute: an instance of `InputSpec`, or a nested structure of `InputSpec` instances (one per input tensor). These objects enable the layer to run input compatibility checks for input structure, input rank, input shape, and input dtype for the first argument of [`Layer.**call**`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#__call__)
.

A `None` entry in a shape is compatible with any dimension.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | Expected dtype of the input. |
| `shape` | Shape tuple, expected shape of the input (may include `None` for dynamic axes). Includes the batch size. |
| `ndim` | Integer, expected rank of the input. |
| `max_ndim` | Integer, maximum rank of the input. |
| `min_ndim` | Integer, minimum rank of the input. |
| `axes` | Dictionary mapping integer axes to a specific dimension value. |
| `allow_last_axis_squeeze` | If `True`, allow inputs of rank N+1 as long as the last axis of the input is 1, as well as inputs of rank N-1 as long as the last axis of the spec is 1. |
| `name` | Expected key corresponding to this input when passing data as a dictionary. |
| `optional` | Boolean, whether the input is optional or not. An optional input can accept `None` values. |

#### Example:

class MyLayer(Layer):
        def __init__(self):
            super().__init__()
            # The layer will accept inputs with
            # shape (*, 28, 28) & (*, 28, 28, 1)
            # and raise an appropriate error message otherwise.
            self.input_spec = InputSpec(
                shape=(None, 28, 28, 1),
                allow_last_axis_squeeze=True)

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/input_spec.py#L117-L119)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/input_spec.py#L106-L115)

get_config()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.