[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/remat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/remat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/remat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fremat&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/remat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/remat#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.remat Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/remat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/remat#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/remat.py#L137-L186)

Applies rematerialization to a function or layer for memory optimization.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.remat`](https://www.tensorflow.org/api_docs/python/tf/keras/remat)

tf.keras.remat(
        f
    )

Rematerialization is a memory optimization technique that trades off computation for memory. Instead of storing intermediate results (e.g. activations) for backpropagation, they are recomputed during the backward pass. This reduces peak memory usage at the cost of increased computation time, allowing the training of larger models or using larger batch sizes within the same memory constraints.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | A callable function, to which rematerialization is applied. This is typically a computationally expensive operation where intermediate states can be recomputed instead of stored. |

|     |
| --- |
| Returns<br>------- |     |
| A wrapped function that applies rematerialization. The returned function defines a custom gradient, ensuring that during the backward pass, the forward computation is recomputed as needed. |     |

#### Example:

from keras import Model
    class CustomRematLayer(layers.Layer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.remat_function = remat(self.intermediate_function)
    
        def intermediate_function(self, x):
            for _ in range(2):
                x = x + x * 0.1  # Simple scaled transformation
            return x
    
        def call(self, inputs):
            return self.remat_function(inputs)
    
    # Define a simple model using the custom layer
    inputs = layers.Input(shape=(4,))
    x = layers.Dense(4, activation="relu")(inputs)
    x = CustomRematLayer()(x)  # Custom layer with rematerialization
    outputs = layers.Dense(1)(x)
    
    # Create and compile the model
    model = Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer="sgd", loss="mse")

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.