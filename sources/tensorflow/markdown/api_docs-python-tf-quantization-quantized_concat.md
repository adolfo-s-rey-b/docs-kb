[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fquantization%2Fquantized_concat&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.quantized\_concat Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat#returns)
    

Concatenates quantized tensors along one dimension.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.quantization.quantized_concat`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat)
, [`tf.compat.v1.quantized_concat`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat)

tf.quantization.quantized_concat(
        concat_dim: Annotated[Any, _atypes.Int32],
        values: Annotated[List[Any], TV_QuantizedConcat_T],
        input_mins: Annotated[List[Any], _atypes.Float32],
        input_maxes: Annotated[List[Any], _atypes.Float32],
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `concat_dim` | A `Tensor` of type `int32`. 0-D. The dimension along which to concatenate. Must be in the range \[0, rank(values)). |\
| `values` | A list of at least 2 `Tensor` objects with the same type. The `N` Tensors to concatenate. Their ranks and types must match, and their sizes must match in all dimensions except `concat_dim`. |\
| `input_mins` | A list with the same length as `values` of `Tensor` objects with type `float32`. The minimum scalar values for each of the input tensors. |\
| `input_maxes` | A list with the same length as `values` of `Tensor` objects with type `float32`. The maximum scalar values for each of the input tensors. |\
| `name` | A name for the operation (optional). |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| A tuple of `Tensor` objects (output, output\_min, output\_max). |     |\
| `output` | A `Tensor`. Has the same type as `values`. |\
| `output_min` | A `Tensor` of type `float32`. |\
| `output_max` | A `Tensor` of type `float32`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.