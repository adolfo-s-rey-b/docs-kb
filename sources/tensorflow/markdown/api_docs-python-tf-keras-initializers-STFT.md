[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.STFT Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L157-L284)

Initializer of Conv kernels for Short-term Fourier Transformation (STFT).

Inherits From: [`Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.STFTInitializer`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT)
, [`tf.keras.initializers.stft`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/STFT)

tf.keras.initializers.STFT(
        side='real',
        window='hann',
        scaling='density',
        periodic=False
    )

Since the formula involves complex numbers, this class compute either the real or the imaginary components of the final output.

Additionally, this initializer supports windowing functions across the time dimension as commonly used in STFT. Windowing functions from the module `scipy.signal.windows` are supported, including the common `hann` and `hamming` windowing functions. This layer supports periodic windows and scaling-based normalization.

This is primarily intended for use in the `STFTSpectrogram` layer.

#### Examples:

    # Standalone usage:

|     |     |
| --- | --- |
| Args<br>---- |     |
| `side` | String, `"real"` or `"imag"` deciding if the kernel will compute the real side or the imaginary side of the output. Defaults to `"real"`. |
| `window` | String for the name of the windowing function in the `scipy.signal.windows` module, or array\_like for the window values, or `None` for no windowing. |
| `scaling` | String, `"density"` or `"spectrum"` for scaling of the window for normalization, either L2 or L1 normalization. `None` for no scaling. |
| `periodic` | Boolean, if True, the window function will be treated as periodic. Defaults to `False`. |

Methods
-------

### `clone`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L96-L97)

clone()

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L76-L94)

@classmethod

Instantiates an initializer from a configuration dictionary.

#### Example:

initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, the output of `get_config()`. |

|     |
| --- |
| Returns |     |
| An `Initializer` instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L278-L284)

get_config()

Returns the initializer's configuration as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L216-L276)

__call__(
        shape, dtype=None
    )

Returns a tensor object initialized as specified by the initializer.

The shape is assumed to be `(T, 1, F // 2 + 1)`, where `T` is the size of the given window, and `F` is the number of frequency bands. Only half the frequency bands are used, which is a common practice in STFT, because the second half are the conjugates of the first half in a reversed order.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. Only numeric or boolean dtypes are supported. If not specified, [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is used, which default to `float32` unless you configured it otherwise (via [`keras.backend.set_floatx(float_dtype)`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.