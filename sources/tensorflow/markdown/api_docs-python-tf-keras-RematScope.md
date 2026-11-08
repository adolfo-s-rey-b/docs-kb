[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.RematScope Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L8-L111)

A context manager for enabling rematerialization in Keras.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.RematScope`](https://www.tensorflow.org/api_docs/python/tf/keras/RematScope)

tf.keras.RematScope(
        mode='full', output_size_threshold=1024, layer_names=None
    )

Rematerialization (gradient checkpointing) trades memory for computation by recomputing intermediate activations during the backward pass. This is particularly useful for training large models or large batch sizes within limited memory constraints.

This should be used when initializing the layer (e.g., `layer(input)`). Rematerialization applies at execution time, not at creation time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | Rematerialization mode to apply. Options:<br><br>*   `"full"`: Apply rematerialization globally to all supported operations.<br>*   `"activations"`: Apply rematerialization to activations on any layers that contain [`keras.activations`](https://www.tensorflow.org/api_docs/python/tf/keras/activations)<br>     (e.g., `Dense(..., activation=relu)`).<br>*   `"larger_than"`: Apply rematerialization to layers with output sizes larger than `output_size_threshold`.<br>*   `"list_of_layers"`: Apply rematerialization to a specific list of layer names.<br>*   `None`: Disable rematerialization. |
| `output_size_threshold` | Output size threshold for the `"larger_than"` mode. Layers producing outputs larger than this threshold will be rematerialized. Default is `1024`. |
| `layer_names` | List of layer names for the `"list_of_layers"` mode. Default is an empty list. |

#### Examples:

Using "list\_of\_layers" mode:

from keras import RematScope
    input_tensor = tf.random.normal((1, 32, 32, 3))
    with RematScope(mode="list_of_layers", layer_names=["dense_1",\
    "conv2d_1"]):
        layer1 = keras.layers.Dense(128, name="dense_1")
        layer2 = keras.layers.Conv2D(64, (3, 3), name="conv2d_1")
        layer3 = keras.layers.Dense(64, name="dense_2")
        # Only layer1 and layer2 will apply rematerialization
        output1 = layer1(input_tensor)
        output2 = layer2(output1)
        output3 = layer3(output2)

Using "larger\_than" mode with a specific output size threshold:

with RematScope(mode="larger_than", output_size_threshold=2048):
        layer = keras.layers.Conv2D(64, (3, 3))
        output = layer(input_tensor)  # Conv2D outputs larger than 2048

Nested scopes for fine-grained control:

with RematScope(mode="full"):
        # Create layers
        layer1 = keras.layers.Dense(128, activation='relu')
        output1 = layer1(input_tensor)  # layer1 is fully rematerialized
        with RematScope(mode="larger_than", output_size_threshold=512):
            layer2 = keras.layers.Conv2D(32, (3, 3))
            output2 = layer2(output1) # layer2 is conditionally rematerialized
            # if output > 512

Methods
-------

### `__enter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L98-L104)

__enter__()

### `__exit__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L106-L111)

__exit__(
        *args, **kwargs
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.