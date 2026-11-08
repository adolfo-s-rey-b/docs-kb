[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#methods)
    *   [add\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#add_meta_graph)
        
    *   [add\_meta\_graph\_and\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#add_meta_graph_and_variables)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#save)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.Builder Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#methods)
    *   [add\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#add_meta_graph)
        
    *   [add\_meta\_graph\_and\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#add_meta_graph_and_variables)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder#save)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/builder_impl.py#L474-L668)

Builds the `SavedModel` protocol buffer and saves variables and assets.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.builder.SavedModelBuilder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder)

tf.compat.v1.saved_model.Builder(
        export_dir
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

The `SavedModelBuilder` class provides the functionality to build a `SavedModel` protocol buffer. Specifically, this allows multiple meta graphs to be saved as part of a single language-neutral `SavedModel`, while sharing variables and assets.

To build a SavedModel, the first meta graph must be saved with variables. Subsequent meta graphs will simply be saved with their graph definitions. If assets need to be saved and written or copied to disk, they can be provided when the meta graph def is added. If multiple meta graph defs are associated an asset of the same name, only the first version is retained.

Each meta graph added to the SavedModel must be annotated with tags. The tags provide a means to identify the specific meta graph to load and restore, along with the shared set of variables and assets.

Typical usage for the `SavedModelBuilder`:

...
    builder = tf.compat.v1.saved_model.Builder(export_dir)
    
    with tf.compat.v1.Session(graph=tf.Graph()) as sess:
      ...
      builder.add_meta_graph_and_variables(sess,
                                      ["foo-tag"],
                                      signature_def_map=foo_signatures,
                                      assets_collection=foo_assets)
    ...
    
    with tf.compat.v1.Session(graph=tf.Graph()) as sess:
      ...
      builder.add_meta_graph(["bar-tag", "baz-tag"])
    ...
    
    builder.save()

Methods
-------

### `add_meta_graph`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/builder_impl.py#L559-L601)

add_meta_graph(
        tags,
        signature_def_map=None,
        assets_collection=None,
        legacy_init_op=None,
        clear_devices=False,
        main_op=None,
        strip_default_attrs=False,
        saver=None
    )

Adds the current meta graph to the SavedModel.

Creates a Saver in the current scope and uses the Saver to export the meta graph def. Invoking this API requires the `add_meta_graph_and_variables()` API to have been invoked before.

|     |     |
| --- | --- |
| Args |     |
| `tags` | The set of tags to annotate the meta graph def with. |
| `signature_def_map` | The map of signature defs to be added to the meta graph def. |
| `assets_collection` | Assets to be saved with SavedModel. Note that this list should be a subset of the assets saved as part of the first meta graph in the SavedModel. |
| `clear_devices` | Set to true if the device info on the default graph should be cleared. |
| `init_op` | Op or group of ops to execute when the graph is loaded. Note that when the init\_op is specified it is run after the restore op at load-time. |
| `train_op` | Op or group of opts that trains the model when run. This will not be run automatically when the graph is loaded, instead saved in a SignatureDef accessible through the exported MetaGraph. |
| `saver` | An instance of tf.compat.v1.train.Saver that will be used to export the metagraph. If None, a sharded Saver that restores all variables will be used. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | If the variables for the SavedModel have not been saved yet, or if the graph already contains one or more legacy init ops. |

### `add_meta_graph_and_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/builder_impl.py#L603-L661)

add_meta_graph_and_variables(
        sess,
        tags,
        signature_def_map=None,
        assets_collection=None,
        legacy_init_op=None,
        clear_devices=False,
        main_op=None,
        strip_default_attrs=False,
        saver=None
    )

Adds the current meta graph to the SavedModel and saves variables.

Creates a Saver to save the variables from the provided session. Exports the corresponding meta graph def. This function assumes that the variables to be saved have been initialized. For a given `SavedModelBuilder`, this API must be called exactly once and for the first meta graph to save. For subsequent meta graph defs to be added, the `add_meta_graph()` API must be used.

|     |     |
| --- | --- |
| Args |     |
| `sess` | The TensorFlow session from which to save the meta graph and variables. |
| `tags` | The set of tags with which to save the meta graph. |
| `signature_def_map` | The map of signature def map to add to the meta graph def. |
| `assets_collection` | Assets to be saved with SavedModel. |
| `clear_devices` | Set to true if the device info on the default graph should be cleared. |
| `init_op` | Op or group of ops to execute when the graph is loaded. Note that when the init\_op is specified it is run after the restore op at load-time. |
| `train_op` | Op or group of ops that trains the model when run. This will not be run automatically when the graph is loaded, instead saved in a SignatureDef accessible through the exported MetaGraph. |
| `strip_default_attrs` | Boolean. If `True`, default-valued attributes will be removed from the NodeDefs. For a detailed guide, see [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)<br>. |
| `saver` | An instance of tf.compat.v1.train.Saver that will be used to export the metagraph and save variables. If None, a sharded Saver that restores all variables will be used. |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/builder_impl.py#L399-L471)

save(
        as_text=False,
        experimental_image_format=False,
        experimental_image_writer_options=None
    )

Writes a `SavedModel` protocol buffer to disk.

The function writes the SavedModel protocol buffer to the export directory in a serialized format.

|     |     |
| --- | --- |
| Args |     |
| `as_text` | Writes the SavedModel protocol buffer in text format to disk. Protocol buffers in text format are useful for debugging, but parsing fails when it encounters an unknown field and so is not forward compatible. This means changes to TensorFlow may prevent deployment of new text format SavedModels to existing serving binaries. Do not deploy `as_text` SavedModels to production. |
| `experimental_image_format` | Writes the SavedModel protobuf in the experimental image format. See [https://www.tensorflow.org/api\_docs/python/tf/saved\_model/SaveOptions](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)<br> for more details. This allows `SavedModelBuilder` to save models larger than 2 GiB. |
| `experimental_image_writer_options` | Optional options for the experimental image writer. See [https://github.com/google/riegeli/blob/master/doc/record\_writer\_options.md](https://github.com/google/riegeli/blob/master/doc/record_writer_options.md)<br> for available options. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | When trying to use `proto_splitter` but `proto_splitter` is not imported. This check is here because `proto_splitter` is not available in OSS at the moment. |

|     |
| --- |
| Returns |     |
| The path to which the SavedModel protocol buffer was written. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.