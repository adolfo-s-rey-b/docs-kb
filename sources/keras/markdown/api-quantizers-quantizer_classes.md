None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Quantizer classes](https://keras.io/api/quantizers/quantizer_classes/)
 [Quantizer utilities](https://keras.io/api/quantizers/quantizer_utils/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Quantizers](https://keras.io/api/quantizers/)
 / Quantizer classes

Quantizer classes
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L19)

### `Quantizer` class

Copied!

`keras.quantizers.Quantizer(output_dtype="int8")`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L307)

### `AbsMaxQuantizer` class

Copied!

`keras.quantizers.AbsMaxQuantizer(     axis=None, value_range=(-127, 127), epsilon=1e-07, output_dtype="int8" )`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L6)

### `QuantizationConfig` class

Copied!

`keras.quantizers.QuantizationConfig(weight_quantizer=None, activation_quantizer=None)`

Base class for quantization configs.

Subclasses must implement the `mode` property and the `get_config` and `from_config` class methods.

**Arguments**

*   **weight\_quantizer**: Quantizer for weights.
*   **activation\_quantizer**: Quantizer for activations.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L65)

### `Int8QuantizationConfig` class

Copied!

`keras.quantizers.Int8QuantizationConfig(     weight_quantizer=None, activation_quantizer="default" )`

Int8 quantization config.

**Arguments**

*   **weight\_quantizer**: Quantizer for weights.
*   **activation\_quantizer**: Quantizer for activations. If "default", uses AbsMaxQuantizer with axis=-1.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L94)

### `Int4QuantizationConfig` class

Copied!

`keras.quantizers.Int4QuantizationConfig(     weight_quantizer=None, activation_quantizer="default", block_size=128 )`

Int4 quantization config.

**Arguments**

*   **weight\_quantizer**: Quantizer for weights.
*   **activation\_quantizer**: Quantizer for activations. If "default", uses AbsMaxQuantizer with axis=-1.
*   **block\_size**: Size of groups along the input dimension for sub-channel quantization. If a positive integer, uses sub-channel quantization with `ceil(input_dim / block_size)` groups. If `None` or `-1`, uses per-channel quantization (one scale per output channel). Default: `128` (sub-channel with 128-element groups).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L184)

### `Float8QuantizationConfig` class

Copied!

`keras.quantizers.Float8QuantizationConfig()`

FP8 quantization config.

FP8 mixed-precision training does not support user defined quantizers. This config is only used to indicate that FP8 mixed-precision training should be used.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/gptq_config.py#L5)

### `GPTQConfig` class

Copied!

`keras.quantizers.GPTQConfig(     dataset,     tokenizer,     weight_bits: int = 4,     num_samples: int = 128,     per_channel: bool = True,     sequence_length: int = 512,     hessian_damping: float = 0.01,     group_size: int = 128,     symmetric: bool = False,     activation_order: bool = False,     quantization_layer_structure: dict = None, )`

Configuration class for the GPTQ (Gradient-based Post-Training Quantization) algorithm.

GPTQ is a post-training quantization method that quantizes neural network weights to lower precision (e.g., 4-bit) while minimizing the impact on model accuracy. It works by analyzing the Hessian matrix of the loss function with respect to the weights and applying optimal quantization that preserves the most important weight values.

**When to use GPTQ:** - You want to reduce model size and memory usage - You need faster inference on hardware that supports low-precision operations - You want to maintain model accuracy as much as possible - You have a pre-trained model that you want to quantize without retraining

**How it works:** 1. Uses calibration data to compute the Hessian matrix for each layer 2. Applies iterative quantization with error correction 3. Reorders weights based on activation importance (optional) 4. Quantizes weights while minimizing quantization error

**Example usage:**

Copied!

`from keras.quantizers import GPTQConfig from keras import Model  # Create configuration for 4-bit quantization config = GPTQConfig(     dataset=calibration_data,          # Your calibration dataset     tokenizer=your_tokenizer,          # Tokenizer for text data     weight_bits=4,                     # Quantize to 4 bits     num_samples=128,                   # Number of calibration samples     sequence_length=512,               # Sequence length for each sample     hessian_damping=0.01,             # Hessian stabilization factor     group_size=128,                    # Weight grouping for quantization     symmetric=False,                   # Use asymmetric quantization     activation_order=True              # Reorder weights by importance )  # Apply quantization to your model model = Model(...)  # Your pre-trained model model.quantize("gptq", config=config)  # The model now has quantized weights and can be used for inference`

**Benefits:** - **Memory reduction**: 4-bit quantization reduces memory by ~8x compared to float32 - **Faster inference**: Lower precision operations are faster on supported hardware - **Accuracy preservation**: Minimizes accuracy loss through optimal quantization - **No retraining required**: Works with pre-trained models

**Advanced usage examples:**

**Per-channel quantization (recommended for most cases):**

Copied!

`config = GPTQConfig(     dataset=calibration_data,     tokenizer=tokenizer,     weight_bits=4,     group_size=-1,  # -1 enables per-channel quantization     symmetric=False )`

**Grouped quantization (for specific hardware requirements):**

Copied!

`config = GPTQConfig(     dataset=calibration_data,     tokenizer=tokenizer,     weight_bits=4,     group_size=64,  # 64 weights share the same scale factor     symmetric=True   # Use symmetric quantization )`

**High-accuracy quantization with activation ordering:**

Copied!

`config = GPTQConfig(     dataset=calibration_data,     tokenizer=tokenizer,     weight_bits=4,     activation_order=True,  # Reorder weights by importance     hessian_damping=0.005,  # Lower damping for more precise     # quantization     num_samples=256          # More samples for better accuracy )`

**References:** - Original GPTQ paper: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers" - Implementation based on: https://github.com/IST-DASLab/gptq - Suitable for: Transformer models, large language models, and other deep neural networks

**Note:** The quality of quantization depends heavily on the calibration dataset. Use representative data that covers the expected input distribution for best results.

**Arguments**

*   **dataset**: The calibration dataset. It can be an iterable that yields strings or pre-tokenized numerical tensors (e.g., a list of strings, a generator, or a NumPy array). This data is used to analyze the model's activations.
*   **tokenizer**: A `keras_nlp.Tokenizer` instance (or a similar callable) that is used to process the `dataset` if it contains strings.
*   **weight\_bits**: (int, optional) The number of bits to quantize weights to. Defaults to 4.
*   **num\_samples**: (int, optional) The number of calibration data samples to use from the dataset. Defaults to 128.
*   **sequence\_length**: (int, optional) The sequence length to use for each calibration sample. Defaults to 512.
*   **hessian\_damping**: (float, optional) The % of Hessian damping to use for stabilization during inverse calculation. Defaults to 0.01.
*   **group\_size**: (int, optional) The size of weight groups to quantize together. A `group_size` of -1 indicates per-channel quantization. Defaults to 128.
*   **symmetric**: (bool, optional) If `True`, uses symmetric quantization. If `False`, uses asymmetric quantization. Defaults to `False`.
*   **activation\_order**: (bool, optional) If `True`, reorders weight columns based on activation magnitude, which can improve quantization accuracy. Defaults to `False`.
*   **quantization\_layer\_structure**: (dict, optional) A dictionary defining the model's quantization structure. It should contain:
    *   "pre\_block\_layers": list of layers to run before the first block.
    *   "sequential\_blocks": list of blocks to be quantized sequentially. If not provided, the model must implement `get_quantization_layer_structure`.

* * *

[Quantizer classes](https://keras.io/api/quantizers/quantizer_classes/#quantizer-classes)

[`Quantizer` class](https://keras.io/api/quantizers/quantizer_classes/#quantizer-class)

[`AbsMaxQuantizer` class](https://keras.io/api/quantizers/quantizer_classes/#absmaxquantizer-class)

[`QuantizationConfig` class](https://keras.io/api/quantizers/quantizer_classes/#quantizationconfig-class)

[`Int8QuantizationConfig` class](https://keras.io/api/quantizers/quantizer_classes/#int8quantizationconfig-class)

[`Int4QuantizationConfig` class](https://keras.io/api/quantizers/quantizer_classes/#int4quantizationconfig-class)

[`Float8QuantizationConfig` class](https://keras.io/api/quantizers/quantizer_classes/#float8quantizationconfig-class)

[`GPTQConfig` class](https://keras.io/api/quantizers/quantizer_classes/#gptqconfig-class)