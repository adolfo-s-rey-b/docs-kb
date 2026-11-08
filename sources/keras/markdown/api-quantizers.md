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
 / Quantizers

Quantizers
==========

### [Quantizer classes](https://keras.io/api/quantizers/quantizer_classes/)

*   [Quantizer class](https://keras.io/api/quantizers/quantizer_classes/#quantizer-class)
    
*   [AbsMaxQuantizer class](https://keras.io/api/quantizers/quantizer_classes/#absmaxquantizer-class)
    
*   [QuantizationConfig class](https://keras.io/api/quantizers/quantizer_classes/#quantizationconfig-class)
    
*   [Int8QuantizationConfig class](https://keras.io/api/quantizers/quantizer_classes/#int8quantizationconfig-class)
    
*   [Int4QuantizationConfig class](https://keras.io/api/quantizers/quantizer_classes/#int4quantizationconfig-class)
    
*   [Float8QuantizationConfig class](https://keras.io/api/quantizers/quantizer_classes/#float8quantizationconfig-class)
    
*   [GPTQConfig class](https://keras.io/api/quantizers/quantizer_classes/#gptqconfig-class)
    

### [Quantizer utilities](https://keras.io/api/quantizers/quantizer_utils/)

*   [abs\_max\_quantize function](https://keras.io/api/quantizers/quantizer_utils/#abs_max_quantize-function)
    
*   [compute\_float8\_amax\_history function](https://keras.io/api/quantizers/quantizer_utils/#compute_float8_amax_history-function)
    
*   [compute\_float8\_scale function](https://keras.io/api/quantizers/quantizer_utils/#compute_float8_scale-function)
    
*   [fake\_quant\_with\_min\_max\_vars function](https://keras.io/api/quantizers/quantizer_utils/#fake_quant_with_min_max_vars-function)
    
*   [pack\_int4 function](https://keras.io/api/quantizers/quantizer_utils/#pack_int4-function)
    
*   [quantize\_and\_dequantize function](https://keras.io/api/quantizers/quantizer_utils/#quantize_and_dequantize-function)
    
*   [unpack\_int4 function](https://keras.io/api/quantizers/quantizer_utils/#unpack_int4-function)
    

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L19)

### `Quantizer` class

Copied!

`keras.Quantizer(output_dtype="int8")`

* * *

[Quantizers](https://keras.io/api/quantizers/#quantizers)

[Quantizer classes](https://keras.io/api/quantizers/#quantizer-classes)

[Quantizer utilities](https://keras.io/api/quantizers/#quantizer-utilities)

[`Quantizer` class](https://keras.io/api/quantizers/#quantizer-class)