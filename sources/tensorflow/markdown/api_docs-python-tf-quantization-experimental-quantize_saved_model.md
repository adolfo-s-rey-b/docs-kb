[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.experimental.quantize\_saved\_model Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py#L798-L926)

Quantizes the SavedModel with the given quantization options.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.quantization.experimental.quantize_saved_model`](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/quantize_saved_model)

tf.quantization.experimental.quantize_saved_model(
        saved_model_path: str,
        output_directory: Optional[str] = None,
        quantization_options: Optional[tf.quantization.experimental.QuantizationOptions] = None,
        representative_dataset: Optional[repr_dataset.RepresentativeDatasetOrMapping] = None,
        *,
        overwrite_output_directory: bool = False
    ) -> autotrackable.AutoTrackable

#### Example usage:

# Quantizing a model trained with QAT.
    quantization_options = tf.quantization.experimental.QuantizationOptions(
        signature_keys=['your_signature_key'],
    )
    tf.quantization.experimental.quantize_saved_model(
        '/tmp/input_model',
        '/tmp/output_model',
        quantization_options=quantization_options,
    )
    
    # When quantizing a model trained without QAT (Post-Training Quantization),
    # a representative dataset is required.
    representative_dataset = [{"input": tf.random.uniform(shape=(3, 3))}\
                          for _ in range(256)]
    tf.quantization.experimental.quantize_saved_model(
        '/tmp/input_model',
        '/tmp/output_model',
        quantization_options=quantization_options,
        representative_dataset={'your_signature_key': representative_dataset},
      )
    
    # In addition to preset quantization methods, fine-grained control of
    # quantization for each component is also supported.
    _QuantizationComponentSpec = (
        tf.quantization.experimental.QuantizationComponentSpec
    )
    quantization_options = tf.quantization.experimental.QuantizationOptions(
        signature_keys=['your_signature_key'],
        quantization_method=tf.quantization.experimental.QuantizationMethod(
            quantization_component_specs=[\
                _QuantizationComponentSpec(\
                    quantization_component=(\
                        _QuantizationComponentSpec.COMPONENT_ACTIVATION\
                    ),\
                    tensor_type=_QuantizationComponentSpec.TENSORTYPE_INT_8,\
                )\
            ]
        )
    )
    tf.quantization.experimental.quantize_saved_model(
        '/tmp/input_model',
        '/tmp/output_model',
        quantization_options=quantization_options,
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `saved_model_path` | Path to the saved model. When representative\_dataset is not provided, this should be a model trained with QAT. |
| `output_directory` | The path to save the output SavedModel. Set `overwrite_output_directory` to `True` to overwrite any existing contents in the directory if not empty. |
| `quantization_options` | A set of options for quantization. If None, it uses post-training static range quantization with XLA opset by default. |
| `representative_dataset` | an iterator that returns a dictionary of {input\_key: input\_value} or a map from signature key to a dictionary of {input\_key: input\_value} that feeds calibration data for quantizing model. The representative should be provided when the model is a PTQ model. It can be provided either via this parameter or via the `representative_datasets` field in `QuantizationOptions`. |
| `overwrite_output_directory` | If set to true, overwrites the output directory iff it isn't empty. The default value is false. |

|     |
| --- |
| Returns<br>------- |     |
| A SavedModel object with TF quantization applied, or None if no quantization is performed. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When 1) representative\_dataset is not provided for non QAT model for enabling static range quantization, 2) invalid value is provided as a quantization method, or 3) provide representative dataset via both argument and QuantizationOptions. |
| `ValueError` | When the specified quantization method is not yet supported. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.