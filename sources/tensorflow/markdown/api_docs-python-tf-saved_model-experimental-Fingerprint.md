[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#methods)
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#from_proto)
        
    *   [singleprint](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#singleprint)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.experimental.Fingerprint Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#methods)
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#from_proto)
        
    *   [singleprint](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#singleprint)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/fingerprinting.py#L28-L148)

The SavedModel fingerprint.

tf.saved_model.experimental.Fingerprint(
        saved_model_checksum: int = None,
        graph_def_program_hash: int = None,
        signature_def_hash: int = None,
        saved_object_graph_hash: int = None,
        checkpoint_hash: int = None,
        version: int = None
    )

Each attribute of this class is named after a field name in the FingerprintDef proto and contains the value of the respective field in the protobuf.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `saved_model_checksum` | Value of the`saved_model_checksum`. |
| `graph_def_program_hash` | Value of the `graph_def_program_hash`. |
| `signature_def_hash` | Value of the `signature_def_hash`. |
| `saved_object_graph_hash` | Value of the `saved_object_graph_hash`. |
| `checkpoint_hash` | Value of the `checkpoint_hash`. |
| `version` | Value of the producer field of the VersionDef. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `saved_model_checksum` | A uint64 containing the `saved_model_checksum`. |
| `graph_def_program_hash` | A uint64 containing `graph_def_program_hash`. |
| `signature_def_hash` | A uint64 containing the `signature_def_hash`. |
| `saved_object_graph_hash` | A uint64 containing the `saved_object_graph_hash`. |
| `checkpoint_hash` | A uint64 containing the`checkpoint_hash`. |
| `version` | An int32 containing the producer field of the VersionDef. |

Methods
-------

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/fingerprinting.py#L71-L87)

@classmethod

Constructs Fingerprint object from protocol buffer message.

### `singleprint`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/fingerprinting.py#L120-L148)

singleprint() -> fingerprinting_pywrap.Singleprint

Canonical fingerprinting ID for a SavedModel.

Uniquely identifies a SavedModel based on the regularized fingerprint attributes. (saved\_model\_checksum is sensitive to immaterial changes and thus non-deterministic.)

|     |
| --- |
| Returns |     |
| The string concatenation of `graph_def_program_hash`, `signature_def_hash`, `saved_object_graph_hash`, and `checkpoint_hash` fingerprint attributes (separated by '/'). |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the fingerprint fields cannot be used to construct the singleprint. |

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/fingerprinting.py#L89-L101)

__eq__(
        other: Any
    ) -> bool

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.