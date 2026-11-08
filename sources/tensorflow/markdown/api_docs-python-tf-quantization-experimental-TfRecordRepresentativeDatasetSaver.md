[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#methods)
    *   [save](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#save)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.experimental.TfRecordRepresentativeDatasetSaver Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#methods)
    *   [save](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver#save)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset.py#L81-L238)

Representative dataset saver in TFRecord format.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.quantization.experimental.TfRecordRepresentativeDatasetSaver`](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/TfRecordRepresentativeDatasetSaver)

tf.quantization.experimental.TfRecordRepresentativeDatasetSaver(
        path_map: Mapping[str, os.PathLike[str]],
        expected_input_key_map: Optional[Mapping[str, Collection[str]]] = None
    )

Saves representative datasets for quantization calibration in TFRecord format. The samples are serialized as `RepresentativeDataSample`.

The `save` method return a signature key to `RepresentativeDatasetFile` map, which can be used for QuantizationOptions.

#### Example usage:

# Creating the representative dataset.
    representative_dataset = [{"input": tf.random.uniform(shape=(3, 3))}\
                          for _ in range(256)]
    
    # Saving to a TFRecord file.
    dataset_file_map = (
      tf.quantization.experimental.TfRecordRepresentativeDatasetSaver(
            path_map={'serving_default': '/tmp/representative_dataset_path'}
        ).save({'serving_default': representative_dataset})
    )
    
    # Using in QuantizationOptions.
    quantization_options = tf.quantization.experimental.QuantizationOptions(
        signature_keys=['serving_default'],
        representative_datasets=dataset_file_map,
    )
    tf.quantization.experimental.quantize_saved_model(
        '/tmp/input_model',
        '/tmp/output_model',
        quantization_options=quantization_options,
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path_map` | Signature def key -> path mapping. Each path is a TFRecord file to which a `RepresentativeDataset` is saved. The signature def keys should be a subset of the `SignatureDef` keys of the `representative_dataset` argument of the `save()` call. |
| `expected_input_key_map` | Signature def key -> expected input keys. If set, validate that the sample has same set of input keys before saving. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `KeyError` | If path\_map and expected\_input\_key\_map have different keys. |

Methods
-------

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset.py#L209-L238)

save(
        representative_dataset: RepresentativeDatasetMapping
    ) -> Mapping[str, _RepresentativeDatasetFile]

Saves the representative dataset.

|     |     |
| --- | --- |
| Args |     |
| `representative_dataset` | Signature def key -> representative dataset mapping. Each dataset is saved in a separate TFRecord file whose path matches the signature def key of `path_map`. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | When the signature def key in `representative_dataset` is not present in the `path_map`. |

|     |
| --- |
| Returns |     |
| A map from signature key to the RepresentativeDatasetFile instance contains the path to the saved file. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.