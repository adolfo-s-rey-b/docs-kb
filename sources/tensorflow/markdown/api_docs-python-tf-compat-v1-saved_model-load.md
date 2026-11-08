[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.load Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/loader_impl.py#L278-L345)

Loads the model from a SavedModel as specified by tags. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.loader.load`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load)

tf.compat.v1.saved_model.load(
        sess, tags, export_dir, import_scope=None, **saver_kwargs
    )

Migrate to TF2
--------------

[`tf.compat.v1.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load)
 or [`tf.compat.v1.saved_model.loader.load`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load)
 is not compatible with eager execution. Please use [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
 instead to load your model. You can refer to the [SavedModel guide](https://www.tensorflow.org/guide/saved_model)
 for more information as well as "Importing SavedModels from TensorFlow 1.x" in the [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
 docstring.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `sess` | Not supported | \-  |
| `tags` | `tags` | \-  |
| `export_dir` | `export_dir` | \-  |
| `import_scope` | Not supported | Name scopes are not needed. By default, variables are associated with the loaded object and function names are deduped. |
| `saver_kwargs` | Not supported | \-  |

#### Before & After Usage Example

Before:

with tf.compat.v1.Session(graph=tf.Graph()) as sess:
      tf.compat.v1.saved_model.loader.load(sess, ["foo-tag"], export_dir)

After:

model = tf.saved_model.load(export_dir, tags=["foo-tag"])

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sess` | The TensorFlow session to restore the variables. |
| `tags` | Set of string tags to identify the required MetaGraphDef. These should correspond to the tags used when saving the variables using the SavedModel `save()` API. |
| `export_dir` | Directory in which the SavedModel protocol buffer and variables to be loaded are located. |
| `import_scope` | Optional `string` -- if specified, prepend this string followed by '/' to all loaded tensor names. This scope is applied to tensor instances loaded into the passed session, but it is _not_ written through to the static `MetaGraphDef` protocol buffer that is returned. |
| `**saver_kwargs` | Optional keyword arguments passed through to Saver. |

|     |
| --- |
| Returns<br>------- |     |
| The `MetaGraphDef` protocol buffer loaded in the provided session. This can be used to further extract signature-defs, collection-defs, etc. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | MetaGraphDef associated with the tags cannot be found. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.