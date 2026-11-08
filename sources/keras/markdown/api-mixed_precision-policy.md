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
 [Mixed precision policy API](https://keras.io/api/mixed_precision/policy/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Mixed precision](https://keras.io/api/mixed_precision/)
 / Mixed precision policy API

Mixed precision policy API
==========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L9)

### `DTypePolicy` class

Copied!

`keras.dtype_policies.DTypePolicy(name=None)`

A dtype policy for a Keras layer.

A dtype policy determines a layer's computation and variable dtypes. Each layer has a policy. Policies can be passed to the `dtype` argument of layer constructors, or a global policy can be set with [`keras.config.set_dtype_policy`](https://keras.io/api/mixed_precision/policy#setdtypepolicy-function)
.

**Arguments**

*   **name**: The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`.

Typically you only need to interact with dtype policies when using mixed precision, which is the use of float16 or bfloat16 for computations and float32 for variables. This is why the term `mixed_precision` appears in the API name. Mixed precision can be enabled by passing `"mixed_float16"` or `"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

Copied!

`>>> keras.config.set_dtype_policy("mixed_float16") >>> layer1 = keras.layers.Dense(10) >>> layer1.dtype_policy  # layer1 will automatically use mixed precision <DTypePolicy "mixed_float16"> >>> # Can optionally override layer to use float32 >>> # instead of mixed precision. >>> layer2 = keras.layers.Dense(10, dtype="float32") >>> layer2.dtype_policy <DTypePolicy "float32"> >>> # Set policy back to initial float32. >>> keras.config.set_dtype_policy('float32')`

In the example above, passing `dtype="float32"` to the layer is equivalent to passing `dtype=keras.config.DTypePolicy("float32")`. In general, passing a dtype policy name to a layer is equivalent to passing the corresponding policy, so it is never necessary to explicitly construct a `DTypePolicy` object.

**Guides and examples using `DTypePolicy`**

*   [Image Segmentation using Composable Fully-Convolutional Networks](https://keras.io/examples/vision/fully_convolutional_network/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L9)

### `DTypePolicyMap` class

Copied!

`keras.dtype_policies.DTypePolicyMap(default_policy=None, policy_map=None)`

Dict-like object mapping layer paths to `DTypePolicy` instances.

`DTypePolicyMap` can be used in `get_config` in layers and subclasses to support a complex configurations of dtype policies.

For example, we can modify `get_config` in `layers.MultiHeadAttention` as follows to support the mixing of dtype policies, such as quantization.

Copied!

`@keras.saving.register_keras_serializable("MyPackage") class MyMultiHeadAttention(keras.layers.MultiHeadAttention):     def get_config(self):         config = super().get_config()         dtype_policy_map = dtype_policies.DTypePolicyMap()         for layer in self._flatten_layers():             if layer.dtype_policy.quantization_mode is not None:                 dtype_policy_map[layer.path] = layer.dtype_policy         if len(dtype_policy_map) > 0:             config.update({"dtype": dtype_policy_map})         return config`

Internally, `DTypePolicyMap` uses a string as a key and a `DTypePolicy` as the value. Typically, the key used for querying is the `Layer.path`. However, it is also possible to set a regex as the key. See the docstring of `get` for more details.

**Arguments**

*   **default\_policy**: An optional `DTypePolicy` instance specifying the default dtype policy. If not specified, the value will default to `keras.config.dtype_policy()`.
*   **policy\_map**: An optional dict that maps string to `DTypePolicy` instances. Defaults to `None`

**Example**

Copied!

` ```python >>> from keras.src import dtype_policies >>> bfloat16 = dtype_policies.DTypePolicy("bfloat16") >>> float16 = dtype_policies.DTypePolicy("float16") >>> float32 = dtype_policies.DTypePolicy("float32") >>> policy_map = DTypePolicyMap(default_policy=float32) `

Set policies using an exact path and a regex pattern.
=====================================================

Note: "decoder" will only match the exact path, not its children.
=================================================================

Copied!

`>>> policy_map["encoder/layer_0/dense"] = bfloat16 >>> policy_map["encoder/.*"] = float16 >>> policy_map["decoder"] = bfloat16`

1\. An exact match is found and returned directly.
==================================================

Copied!

`>>> policy_map["encoder/layer_0/dense"].name 'bfloat16'`

2\. A regex match is found for a child layer.
=============================================

It matches the "encoder/.\*" pattern.
=====================================

Copied!

`>>> policy_map["encoder/attention/query"].name 'float16'`

3\. No implicit prefix matching occurs.
=======================================

"decoder/attention" does not match the key "decoder".
=====================================================

The default policy is returned.
===============================

Copied!

`>>> policy_map["decoder/attention"].name 'float32'`

4\. A ValueError is raised if a path matches multiple patterns.
===============================================================

Copied!

`>>> policy_map["encoder/attention/.*"] = bfloat16 __"encoder/attention/query" now matches two patterns__  :  __- "encoder/.*__  "  __- "encoder/attention/.*__  "  >>> try: ...     policy_map["encoder/attention/query"] ... except ValueError as e: ...     print(e) Path 'encoder/attention/query' matches multiple dtype policy ..`

Copied!

``----  <span style="float:right;">[[source]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L207)</span>  ### `FloatDTypePolicy` class   ```python keras.dtype_policies.FloatDTypePolicy(name=None)``

A dtype policy for a Keras layer.

A dtype policy determines a layer's computation and variable dtypes. Each layer has a policy. Policies can be passed to the `dtype` argument of layer constructors, or a global policy can be set with [`keras.config.set_dtype_policy`](https://keras.io/api/mixed_precision/policy#setdtypepolicy-function)
.

**Arguments**

*   **name**: The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`.

Typically you only need to interact with dtype policies when using mixed precision, which is the use of float16 or bfloat16 for computations and float32 for variables. This is why the term `mixed_precision` appears in the API name. Mixed precision can be enabled by passing `"mixed_float16"` or `"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

Copied!

`>>> keras.config.set_dtype_policy("mixed_float16") >>> layer1 = keras.layers.Dense(10) >>> layer1.dtype_policy  # layer1 will automatically use mixed precision <DTypePolicy "mixed_float16"> >>> # Can optionally override layer to use float32 >>> # instead of mixed precision. >>> layer2 = keras.layers.Dense(10, dtype="float32") >>> layer2.dtype_policy <DTypePolicy "float32"> >>> # Set policy back to initial float32. >>> keras.config.set_dtype_policy('float32')`

In the example above, passing `dtype="float32"` to the layer is equivalent to passing `dtype=keras.config.DTypePolicy("float32")`. In general, passing a dtype policy name to a layer is equivalent to passing the corresponding policy, so it is never necessary to explicitly construct a `DTypePolicy` object.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L215)

### `QuantizedDTypePolicy` class

Copied!

`keras.dtype_policies.QuantizedDTypePolicy(mode, source_name=None)`

A dtype policy for a Keras layer.

A dtype policy determines a layer's computation and variable dtypes. Each layer has a policy. Policies can be passed to the `dtype` argument of layer constructors, or a global policy can be set with [`keras.config.set_dtype_policy`](https://keras.io/api/mixed_precision/policy#setdtypepolicy-function)
.

**Arguments**

*   **name**: The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`.

Typically you only need to interact with dtype policies when using mixed precision, which is the use of float16 or bfloat16 for computations and float32 for variables. This is why the term `mixed_precision` appears in the API name. Mixed precision can be enabled by passing `"mixed_float16"` or `"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

Copied!

`>>> keras.config.set_dtype_policy("mixed_float16") >>> layer1 = keras.layers.Dense(10) >>> layer1.dtype_policy  # layer1 will automatically use mixed precision <DTypePolicy "mixed_float16"> >>> # Can optionally override layer to use float32 >>> # instead of mixed precision. >>> layer2 = keras.layers.Dense(10, dtype="float32") >>> layer2.dtype_policy <DTypePolicy "float32"> >>> # Set policy back to initial float32. >>> keras.config.set_dtype_policy('float32')`

In the example above, passing `dtype="float32"` to the layer is equivalent to passing `dtype=keras.config.DTypePolicy("float32")`. In general, passing a dtype policy name to a layer is equivalent to passing the corresponding policy, so it is never necessary to explicitly construct a `DTypePolicy` object.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L259)

### `QuantizedFloat8DTypePolicy` class

Copied!

`keras.dtype_policies.QuantizedFloat8DTypePolicy(     mode, source_name=None, amax_history_length=1024 )`

A dtype policy for a Keras layer.

A dtype policy determines a layer's computation and variable dtypes. Each layer has a policy. Policies can be passed to the `dtype` argument of layer constructors, or a global policy can be set with [`keras.config.set_dtype_policy`](https://keras.io/api/mixed_precision/policy#setdtypepolicy-function)
.

**Arguments**

*   **name**: The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`.

Typically you only need to interact with dtype policies when using mixed precision, which is the use of float16 or bfloat16 for computations and float32 for variables. This is why the term `mixed_precision` appears in the API name. Mixed precision can be enabled by passing `"mixed_float16"` or `"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

Copied!

`>>> keras.config.set_dtype_policy("mixed_float16") >>> layer1 = keras.layers.Dense(10) >>> layer1.dtype_policy  # layer1 will automatically use mixed precision <DTypePolicy "mixed_float16"> >>> # Can optionally override layer to use float32 >>> # instead of mixed precision. >>> layer2 = keras.layers.Dense(10, dtype="float32") >>> layer2.dtype_policy <DTypePolicy "float32"> >>> # Set policy back to initial float32. >>> keras.config.set_dtype_policy('float32')`

In the example above, passing `dtype="float32"` to the layer is equivalent to passing `dtype=keras.config.DTypePolicy("float32")`. In general, passing a dtype policy name to a layer is equivalent to passing the corresponding policy, so it is never necessary to explicitly construct a `DTypePolicy` object.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L364)

### `GPTQDTypePolicy` class

Copied!

`keras.dtype_policies.GPTQDTypePolicy(mode, source_name=None)`

Quantized dtype policy for GPTQ quantization.

This policy helps propagate quantization settings for GPTQ when loading a GPTQ quantized model in Keras format.

**Arguments**

*   **mode**: The quantization mode. This should be a string in the format `"gptq/<weight_bits>/<group_size>"`. - `"gptq"`: The identifier for the quantization algorithm. - `<weight_bits>`: Number of bits to quantize weights to. Supported values are 2, 3, 4, and 8. - `<group_size>`: The group size for quantization. Supported values are -1 (for whole-tensor quantization) or any positive integer. Typically a smaller group size leads to better accuracy but slower speed. # Example `"gptq/4/128"`. source\_name: The source dtype policy name, e.g. "float32".

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L570)

### `dtype_policy` function

Copied!

`keras.config.dtype_policy()`

Returns the current default dtype policy object.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L539)

### `set_dtype_policy` function

Copied!

`keras.config.set_dtype_policy(policy)`

Sets the default dtype policy globally.

**Example**

Copied!

`>>> keras.config.set_dtype_policy("mixed_float16")`

**Guides and examples using `set_dtype_policy`**

*   [How to use Keras with NNX backend](https://keras.io/guides/keras_nnx_guide/)
    
*   [Loading Hugging Face Transformers Checkpoints](https://keras.io/keras_hub/guides/hugging_face_keras_integration/)
    
*   [Function Calling with KerasHub models](https://keras.io/keras_hub/guides/function_calling_with_keras_hub/)
    
*   [RAG Pipeline with KerasHub](https://keras.io/keras_hub/guides/rag_pipeline_with_keras_hub/)
    
*   [Segment Anything](https://keras.io/keras_hub/guides/segment_anything_in_keras_hub/)
    
*   [Parameter-efficient fine-tuning of Gemma with LoRA and QLoRA](https://keras.io/examples/keras_recipes/parameter_efficient_finetuning_of_gemma_with_lora_and_qlora/)
    
*   [Float8 training and inference with a simple Transformer model](https://keras.io/examples/keras_recipes/float8_training_and_inference_with_transformer/)
    
*   [Image Segmentation using Composable Fully-Convolutional Networks](https://keras.io/examples/vision/fully_convolutional_network/)
    

* * *

[Mixed precision policy API](https://keras.io/api/mixed_precision/policy/#mixed-precision-policy-api)

[`DTypePolicy` class](https://keras.io/api/mixed_precision/policy/#dtypepolicy-class)

[`DTypePolicyMap` class](https://keras.io/api/mixed_precision/policy/#dtypepolicymap-class)

[`FloatDTypePolicy` class](https://keras.io/api/mixed_precision/policy/#floatdtypepolicy-class)

[`QuantizedDTypePolicy` class](https://keras.io/api/mixed_precision/policy/#quantizeddtypepolicy-class)

[`QuantizedFloat8DTypePolicy` class](https://keras.io/api/mixed_precision/policy/#quantizedfloat8dtypepolicy-class)

[`GPTQDTypePolicy` class](https://keras.io/api/mixed_precision/policy/#gptqdtypepolicy-class)

[`dtype_policy` function](https://keras.io/api/mixed_precision/policy/#dtypepolicy-function)

[`set_dtype_policy` function](https://keras.io/api/mixed_precision/policy/#setdtypepolicy-function)