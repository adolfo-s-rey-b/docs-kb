[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.simple\_save Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/simple_save.py#L26-L84)

Convenience function to build a SavedModel suitable for serving. (deprecated)

tf.compat.v1.saved_model.simple_save(
        session, export_dir, inputs, outputs, legacy_init_op=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

In many common cases, saving models for serving will be as simple as:

simple_save(session,
                export_dir,
                inputs={"x": x, "y": y},
                outputs={"z": z})

Although in many cases it's not necessary to understand all of the many ways to configure a SavedModel, this method has a few practical implications:

*   It will be treated as a graph for inference / serving (i.e. uses the tag [`saved_model.SERVING`](https://www.tensorflow.org/api_docs/python/tf/saved_model#SERVING)
    )
*   The SavedModel will load in TensorFlow Serving and supports the [Predict API](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/apis/predict.proto)
    . To use the Classify, Regress, or MultiInference APIs, please see the [SavedModel APIs](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md)
    .
*   Some TensorFlow ops depend on information on disk or other information called "assets". These are generally handled automatically by adding the assets to the `GraphKeys.ASSET_FILEPATHS` collection. Only assets in that collection are exported; if you need more custom behavior, you'll need to use the [SavedModelBuilder](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/builder.py)
    .

More information about SavedModel and signatures can be found here: [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved\_model/README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `session` | The TensorFlow session from which to save the meta graph and variables. |
| `export_dir` | The path to which the SavedModel will be stored. |
| `inputs` | dict mapping string input names to tensors. These are added to the SignatureDef as the inputs. |
| `outputs` | dict mapping string output names to tensors. These are added to the SignatureDef as the outputs. |
| `legacy_init_op` | Legacy support for op or group of ops to execute after the restore op upon a load. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.