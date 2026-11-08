[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc/ops#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfc.ops Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc/ops#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/ops/__init__.py)

TensorFlow operations and functions.

Functions
---------

[`create_range_decoder(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_decoder)
: Creates range decoder objects to be used by `EntropyDecode*` ops.

[`create_range_encoder(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder)
: Creates range encoder objects to be used by `EntropyEncode*` ops.

[`entropy_decode_channel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel)
: Decodes the encoded stream inside `handle`.

[`entropy_decode_finalize(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize)
: Finalizes the decoding process.

[`entropy_decode_index(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_index)
: Decodes the encoded stream inside `handle`.

[`entropy_encode_channel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel)
: Encodes each input in `value`.

[`entropy_encode_finalize(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_finalize)
: Finalizes the encoding process and extracts byte stream from the encoder.

[`entropy_encode_index(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_index)
: Encodes each input in `value` according to a distribution selected by `index`.

[`lower_bound(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound)
: Same as [`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
, but with helpful gradient for `inputs < bound`.

[`perturb_and_apply(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply)
: Perturbs the inputs of a pointwise function.

[`pmf_to_quantized_cdf(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf)
: Converts a PMF into a quantized CDF for range coding.

[`round_st(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/round_st)
: Straight-through round with optional quantization offset.

[`run_length_decode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode)
: Decodes `data` using run-length coding.

[`run_length_encode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_encode)
: Encodes `data` using run-length coding.

[`run_length_gamma_decode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_decode)
: Decodes `data` using run-length and Elias gamma coding.

[`run_length_gamma_encode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode)
: Encodes `data` using run-length and Elias gamma coding.

[`same_padding_for_kernel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel)
: Determine correct amount of padding for `same` convolution.

[`soft_round(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round)
: Differentiable approximation to `round`.

[`soft_round_conditional_mean(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean)
: Conditional mean of inputs given noisy soft rounded values.

[`soft_round_inverse(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_inverse)
: Inverse of `soft_round`.

[`stochastic_round(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/stochastic_round)
: Rounds `inputs / step_size` stochastically.

[`upper_bound(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/upper_bound)
: Same as [`tf.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)
, but with helpful gradient for `inputs > bound`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.