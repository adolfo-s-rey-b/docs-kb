[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#activation_quantizer_or_default)
        
    *   [dtype\_policy\_string](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#dtype_policy_string)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#weight_quantizer_or_default)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.GPTQConfig Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#activation_quantizer_or_default)
        
    *   [dtype\_policy\_string](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#dtype_policy_string)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/GPTQConfig?version=stable#weight_quantizer_or_default)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/gptq_config.py#L5-L219)

Configuration class for the GPTQ (Gradient-based Post-Training Quantization) algorithm.

Inherits From: [`QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig)

tf.keras.quantizers.GPTQConfig(
        dataset,
        tokenizer,
        *,
        weight_bits: int = 4,
        num_samples: int = 128,
        per_channel: bool = True,
        sequence_length: int = 512,
        hessian_damping: float = 0.01,
        group_size: int = 128,
        symmetric: bool = False,
        activation_order: bool = False,
        quantization_layer_structure: dict = None
    )

GPTQ is a post-training quantization method that quantizes neural network weights to lower precision (e.g., 4-bit) while minimizing the impact on model accuracy. It works by analyzing the Hessian matrix of the loss function with respect to the weights and applying optimal quantization that preserves the most important weight values.

**When to use GPTQ:**

*   You want to reduce model size and memory usage
*   You need faster inference on hardware that supports low-precision operations
*   You want to maintain model accuracy as much as possible
*   You have a pre-trained model that you want to quantize without retraining

**How it works:**

1.  Uses calibration data to compute the Hessian matrix for each layer
2.  Applies iterative quantization with error correction
3.  Reorders weights based on activation importance (optional)
4.  Quantizes weights while minimizing quantization error

**Example usage:**

from keras.quantizers import GPTQConfig
    from keras import Model
    
    # Create configuration for 4-bit quantization
    config = GPTQConfig(
        dataset=calibration_data,          # Your calibration dataset
        tokenizer=your_tokenizer,          # Tokenizer for text data
        weight_bits=4,                     # Quantize to 4 bits
        num_samples=128,                   # Number of calibration samples
        sequence_length=512,               # Sequence length for each sample
        hessian_damping=0.01,             # Hessian stabilization factor
        group_size=128,                    # Weight grouping for quantization
        symmetric=False,                   # Use asymmetric quantization
        activation_order=True              # Reorder weights by importance
    )
    
    # Apply quantization to your model
    model = Model(...)  # Your pre-trained model
    model.quantize("gptq", config=config)
    
    # The model now has quantized weights and can be used for inference

**Benefits:**

*   **Memory reduction**: 4-bit quantization reduces memory by ~8x compared to float32
*   **Faster inference**: Lower precision operations are faster on supported hardware
*   **Accuracy preservation**: Minimizes accuracy loss through optimal quantization
*   **No retraining required**: Works with pre-trained models

**Advanced usage examples:**

**Per-channel quantization (recommended for most cases):**

config = GPTQConfig(
        dataset=calibration_data,
        tokenizer=tokenizer,
        weight_bits=4,
        group_size=-1,  # -1 enables per-channel quantization
        symmetric=False
    )

**Grouped quantization (for specific hardware requirements):**

config = GPTQConfig(
        dataset=calibration_data,
        tokenizer=tokenizer,
        weight_bits=4,
        group_size=64,  # 64 weights share the same scale factor
        symmetric=True   # Use symmetric quantization
    )

**High-accuracy quantization with activation ordering:**

config = GPTQConfig(
        dataset=calibration_data,
        tokenizer=tokenizer,
        weight_bits=4,
        activation_order=True,  # Reorder weights by importance
        hessian_damping=0.005,  # Lower damping for more precise
        # quantization
        num_samples=256          # More samples for better accuracy
    )

**References:**

*   Original GPTQ paper: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
*   Implementation based on: [https://github.com/IST-DASLab/gptq](https://github.com/IST-DASLab/gptq)
    
*   Suitable for: Transformer models, large language models, and other deep neural networks

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | The calibration dataset. It can be an iterable that yields strings or pre-tokenized numerical tensors (e.g., a list of strings, a generator, or a NumPy array). This data is used to analyze the model's activations. |
| `tokenizer` | A `keras_nlp.Tokenizer` instance (or a similar callable) that is used to process the `dataset` if it contains strings. |
| `weight_bits` | (int, optional) The number of bits to quantize weights to. Defaults to 4. |
| `num_samples` | (int, optional) The number of calibration data samples to use from the dataset. Defaults to 128. |
| `sequence_length` | (int, optional) The sequence length to use for each calibration sample. Defaults to 512. |
| `hessian_damping` | (float, optional) The % of Hessian damping to use for stabilization during inverse calculation. Defaults to 0.01. |
| `group_size` | (int, optional) The size of weight groups to quantize together. A `group_size` of -1 indicates per-channel quantization. Defaults to 128. |
| `symmetric` | (bool, optional) If `True`, uses symmetric quantization. If `False`, uses asymmetric quantization. Defaults to `False`. |
| `activation_order` | (bool, optional) If `True`, reorders weight columns based on activation magnitude, which can improve quantization accuracy. Defaults to `False`. |
| `quantization_layer_structure` | (dict, optional) A dictionary defining the model's quantization structure. It should contain:<br><br>*   "pre\_block\_layers": list of layers to run before the first block.<br>*   "sequential\_blocks": list of blocks to be quantized sequentially. If not provided, the model must implement `get_quantization_layer_structure`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `mode` |     |

Methods
-------

### `activation_quantizer_or_default`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L58-L62)

@staticmethod

### `dtype_policy_string`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/gptq_config.py#L213-L219)

dtype_policy_string()

Returns the dtype policy string for this configuration.

|     |
| --- |
| Returns |     |
| A string representing the dtype policy, e.g. "gptq\_4bit". |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/gptq_config.py#L205-L207)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/gptq_config.py#L188-L203)

get_config()

### `weight_quantizer_or_default`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L52-L56)

@staticmethod

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.