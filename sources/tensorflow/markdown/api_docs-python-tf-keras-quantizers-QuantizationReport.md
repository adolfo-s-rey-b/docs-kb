[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationReport#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.QuantizationReport Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L11-L114)

Structured summary of a single `model.quantize()` call.

tf.keras.quantizers.QuantizationReport(
        mode=None
    )

A report is returned by `model.quantize()` and also stored on the model as `model._quantization_report`. It records, per leaf layer, whether the layer was quantized or skipped (with the reason).

The possible skip reasons are available as class attributes on `QuantizationReport` (`SKIP_NO_SUPPORT`, `SKIP_FILTERED`, `SKIP_ALREADY_QUANTIZED`, `SKIP_OUTSIDE_STRUCTURE`).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | The resolved quantization mode for the call (e.g. `"int8"`). Defaults to `None`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `mode` | The resolved quantization mode for the call. |
| `quantized` | A list of `(path, mode, scheme)` tuples, one per quantized layer, where `scheme` is a short description of the resolved quantization scheme (e.g. the layer's dtype-policy name). |
| `skipped` | A list of `(path, reason)` tuples. `reason` is one of `SKIP_NO_SUPPORT` (the layer does not implement quantization), `SKIP_FILTERED` (the layer was excluded by `filters`), `SKIP_ALREADY_QUANTIZED` (the layer was already quantized), or `SKIP_OUTSIDE_STRUCTURE` (a GPTQ/AWQ call whose quantization layer structure does not cover the layer). |
| `num_quantized` |     |
| `num_skipped` |     |

Methods
-------

### `add_quantized`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L51-L52)

add_quantized(
        path, mode, scheme
    )

### `add_skipped`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L54-L55)

add_skipped(
        path, reason
    )

### `render`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L91-L108)

render()

Return the full report as a multi-line string.

### `skipped_by_reason`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L65-L67)

skipped_by_reason(
        reason
    )

Return the list of layer paths that were skipped for `reason`.

### `summary_warning`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/report.py#L69-L89)

summary_warning(
        max_examples=5
    )

Return a single warning message, or `None` if nothing to warn about.

This replaces the previous behavior of emitting one `UserWarning` per non-quantizable leaf layer with a single message that reports counts and up to `max_examples` example layer names.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| SKIP\_ALREADY\_QUANTIZED | `'already quantized'` |
| SKIP\_FILTERED | `'filtered out'` |
| SKIP\_NO\_SUPPORT | `'no quantize support'` |
| SKIP\_OUTSIDE\_STRUCTURE | `'outside quantization structure'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.