[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsaved_model%2Fsignature_def_utils%2FMethodNameUpdater&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#methods)
    *   [replace\_method\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#replace_method_name)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#save)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.signature\_def\_utils.MethodNameUpdater Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#methods)
    *   [replace\_method\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#replace_method_name)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater#save)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/method_name_updater.py#L30-L143)

Updates the method name(s) of the SavedModel stored in the given path.

tf.compat.v1.saved_model.signature_def_utils.MethodNameUpdater(
        export_dir
    )

The `MethodNameUpdater` class provides the functionality to update the method name field in the signature\_defs of the given SavedModel. For example, it can be used to replace the `predict` `method_name` to `regress`.

Typical usages of the `MethodNameUpdater`

...
    updater = tf.compat.v1.saved_model.signature_def_utils.MethodNameUpdater(
        export_dir)
    # Update all signature_defs with key "foo" in all meta graph defs.
    updater.replace_method_name(signature_key="foo", method_name="regress")
    # Update a single signature_def with key "bar" in the meta graph def with
    # tags ["serve"]
    updater.replace_method_name(signature_key="bar", method_name="classify",
                                tags="serve")
    updater.save(new_export_dir)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | Directory containing the SavedModel files. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `IOError` | If the saved model file does not exist, or cannot be successfully parsed. |

Methods
-------

### `replace_method_name`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/method_name_updater.py#L69-L111)

replace_method_name(
        signature_key, method_name, tags=None
    )

Replaces the method\_name in the specified signature\_def.

This will match and replace multiple sig defs iff tags is None (i.e when multiple `MetaGraph`s have a signature\_def with the same key). If tags is not None, this will only replace a single signature\_def in the `MetaGraph` with matching tags.

|     |     |
| --- | --- |
| Args |     |
| `signature_key` | Key of the signature\_def to be updated. |
| `method_name` | new method\_name to replace the existing one. |
| `tags` | A tag or sequence of tags identifying the `MetaGraph` to update. If None, all meta graphs will be updated. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if signature\_key or method\_name are not defined or if no metagraphs were found with the associated tags or if no meta graph has a signature\_def that matches signature\_key. |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/method_name_updater.py#L113-L143)

save(
        new_export_dir=None
    )

Saves the updated `SavedModel`.

|     |     |
| --- | --- |
| Args |     |
| `new_export_dir` | Path where the updated `SavedModel` will be saved. If None, the input `SavedModel` will be overriden with the updates. |

|     |     |
| --- | --- |
| Raises |     |
| [`errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | If there are errors during the file save operation. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.