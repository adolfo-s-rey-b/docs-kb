[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#activation_quantizer_or_default)
        
    *   [dtype\_policy\_string](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#dtype_policy_string)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#weight_quantizer_or_default)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.AWQConfig Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#activation_quantizer_or_default)
        
    *   [dtype\_policy\_string](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#dtype_policy_string)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AWQConfig?version=stable#weight_quantizer_or_default)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/awq_config.py#L5-L140)

Configuration class for AWQ (Activation-aware Weight Quantization).

Inherits From: [`QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig)

tf.keras.quantizers.AWQConfig(
        dataset,
        tokenizer,
        *,
        weight_bits: int = 4,
        num_samples: int = 128,
        sequence_length: int = 512,
        group_size: int = 128,
        num_grid_points: int = 20,
        quantization_layer_structure: dict = None
    )

AWQ is a post-training quantization method that identifies and protects salient weights based on activation magnitudes. It applies per-channel scaling before quantization to minimize accuracy loss.

#### Methodology:

1.  Collects activation statistics from calibration data
2.  Identifies salient weight channels based on activation magnitudes
3.  Searches for optimal per-channel scaling factors via grid search
4.  Applies scaling before quantization to protect important weights

#### References:

*   Original AWQ paper: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration" ([https://arxiv.org/abs/2306.00978](https://arxiv.org/abs/2306.00978)
    )
*   Reference implementation: [https://github.com/mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq)
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | The calibration dataset. It can be an iterable that yields strings or pre-tokenized numerical tensors (e.g., a list of strings, a generator, or a NumPy array). This data is used to analyze activation patterns. |
| `tokenizer` | A tokenizer instance (or a similar callable) that is used to process the `dataset`. |
| `weight_bits` | The number of bits for weight quantization. AWQ presently only supports 4-bit quantization. Defaults to 4. |
| `num_samples` | The number of calibration data samples to use from the dataset. Defaults to 128. |
| `sequence_length` | The sequence length to use for each calibration sample. Defaults to 512. |
| `group_size` | The size of weight groups to quantize together. A `group_size` of -1 indicates per-channel quantization. Defaults to 128. |
| `num_grid_points` | The number of grid search points for finding optimal per-channel scales. Higher values may find better scales but take longer. Defaults to 20. |
| `quantization_layer_structure` | A dictionary defining the model's quantization structure. It should contain:<br><br>*   "pre\_block\_layers": list of layers to run before the first block (e.g., embedding layer).<br>*   "sequential\_blocks": list of transformer blocks to quantize sequentially. If not provided, the model must implement `get_quantization_layer_structure`. |

#### Example:

from keras.quantizers import AWQConfig
    
    # Create configuration for 4-bit AWQ quantization
    config = AWQConfig(
        dataset=calibration_data,          # Your calibration dataset
        tokenizer=your_tokenizer,          # Tokenizer for text data
        num_samples=128,                   # Number of calibration samples
        sequence_length=512,               # Sequence length for each sample
        group_size=128,                    # Weight grouping for quantization
        num_grid_points=20,                # Grid search points for scale search
    )
    
    # Apply quantization to your model
    model.quantize("awq", config=config)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/awq_config.py#L116-L122)

dtype_policy_string()

Returns the dtype policy string for this configuration.

|     |
| --- |
| Returns |     |
| A string representing the dtype policy, e.g. "awq/4/128". |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/awq_config.py#L138-L140)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/awq_config.py#L124-L136)

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