[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/Asset#main-content)

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
    

tf.saved\_model.Asset Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/trackable/asset.py#L30-L112)

Represents a file asset to hermetically include in a SavedModel.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.Asset`](https://www.tensorflow.org/api_docs/python/tf/saved_model/Asset)

tf.saved_model.Asset(
        path
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) |

A SavedModel can include arbitrary files, called assets, that are needed for its use. For example a vocabulary file used initialize a lookup table.

When a trackable object is exported via [`tf.saved_model.save()`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
, all the `Asset`s reachable from it are copied into the SavedModel assets directory. Upon loading, the assets and the serialized functions that depend on them will refer to the correct filepaths inside the SavedModel directory.

#### Example:

filename = tf.saved_model.Asset("file.txt")
    
    @tf.function(input_signature=[])
    def func():
      return tf.io.read_file(filename)
    
    trackable_obj = tf.train.Checkpoint()
    trackable_obj.func = func
    trackable_obj.filename = filename
    tf.saved_model.save(trackable_obj, "/tmp/saved_model")
    
    # The created SavedModel is hermetic, it does not depend on
    # the original file and can be moved to another path.
    tf.io.gfile.remove("file.txt")
    tf.io.gfile.rename("/tmp/saved_model", "/tmp/new_location")
    
    reloaded_obj = tf.saved_model.load("/tmp/new_location")
    print(reloaded_obj.func())

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `asset_path` | A path, or a 0-D [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> tensor with path to the asset. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.