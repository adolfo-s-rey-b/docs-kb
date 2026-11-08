[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/device#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/device)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/device?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/device#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.device Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/device#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/__init__.py#L75-L144)

Context manager for backend-agnostic device placement.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.device`](https://www.tensorflow.org/api_docs/python/tf/keras/device)

tf.keras.device(
        device_name
    )

Use this context manager to control on which device operations are performed and tensors are allocated. This works across all backends (TensorFlow, JAX, PyTorch). This is useful for memory management, data preprocessing, and multi-device setups.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_name` | String specifying the device in format `"device_type:device_index"`. For example: `"cpu:0"`, `"gpu:0"`, `"gpu:1"`. For the PyTorch backend, `"gpu"` is automatically converted to `"cuda"`. |

#### Example:

Basic usage with CPU and GPU:

# Allocate tensors on CPU
    with keras.device("cpu:0"):
        cpu_tensor = keras.ops.ones((2, 2))
    
    # Allocate tensors on GPU (if available)
    with keras.device("gpu:0"):
        gpu_tensor = keras.ops.ones((2, 2))

Practical example with CPU preprocessing and GPU training:

# Create dummy data and model
    x_raw = np.random.rand(128, 784)
    y_train = np.random.randint(0, 10, size=(128,))
    model = keras.Sequential([\
        keras.Input(shape=(784,)),\
        keras.layers.Dense(10)\
    ])
    model.compile(
        optimizer="adam",
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    )
    
    # Preprocess data on CPU
    with keras.device("cpu:0"):
        x_processed = keras.ops.cast(x_raw, "float32")
    
    # Train on GPU (if available)
    with keras.device("gpu:0"):
        model.fit(x_processed, y_train, epochs=2)

#### Use cases:

*   **Memory management**: Keep large tensors on CPU to save GPU memory
*   **Data preprocessing**: Process data on CPU before training on GPU
*   **GPU / TPU setups**: Control what runs on GPU / TPU vs CPU
*   **Multi-device setups**: Control which device receives which tensors

Device naming conventions:

*   `"cpu:0"` - First CPU
*   `"gpu:0"` - First GPU (works across all backends)
*   `"gpu:1"` - Second GPU

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.