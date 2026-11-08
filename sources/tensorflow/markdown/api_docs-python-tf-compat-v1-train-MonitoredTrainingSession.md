[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.MonitoredTrainingSession Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredTrainingSession#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L427-L609)

Creates a `MonitoredSession` for training.

tf.compat.v1.train.MonitoredTrainingSession(
        master='',
        is_chief=True,
        checkpoint_dir=None,
        scaffold=None,
        hooks=None,
        chief_only_hooks=None,
        save_checkpoint_secs=USE_DEFAULT,
        save_summaries_steps=USE_DEFAULT,
        save_summaries_secs=USE_DEFAULT,
        config=None,
        stop_grace_period_secs=120,
        log_step_count_steps=100,
        max_wait_secs=7200,
        save_checkpoint_steps=USE_DEFAULT,
        summary_dir=None,
        save_graph_def=True
    )

Migrate to TF2
--------------

This API is not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, rewrite the code to be compatible with eager execution. Check the [migration guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
 on replacing `Session.run` calls. In Keras, session hooks can be replaced by Callbacks e.g. [logging hook notebook](https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb)
 For more details please read [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings) |

For a chief, this utility sets proper session initializer/restorer. It also creates hooks related to checkpoint and summary saving. For workers, this utility sets proper session creator which waits for the chief to initialize/restore. Please check [`tf.compat.v1.train.MonitoredSession`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession)
 for more information.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `master` | `String` the TensorFlow master to use. |
| `is_chief` | If `True`, it will take care of initialization and recovery the underlying TensorFlow session. If `False`, it will wait on a chief to initialize or recover the TensorFlow session. |
| `checkpoint_dir` | A string. Optional path to a directory where to restore variables. |
| `scaffold` | A `Scaffold` used for gathering or building supportive ops. If not specified, a default one is created. It's used to finalize the graph. |
| `hooks` | Optional list of `SessionRunHook` objects. |
| `chief_only_hooks` | list of `SessionRunHook` objects. Activate these hooks if `is_chief==True`, ignore otherwise. |
| `save_checkpoint_secs` | The frequency, in seconds, that a checkpoint is saved using a default checkpoint saver. If both `save_checkpoint_steps` and `save_checkpoint_secs` are set to `None`, then the default checkpoint saver isn't used. If both are provided, then only `save_checkpoint_secs` is used. Default 600. |
| `save_summaries_steps` | The frequency, in number of global steps, that the summaries are written to disk using a default summary saver. If both `save_summaries_steps` and `save_summaries_secs` are set to `None`, then the default summary saver isn't used. Default 100. |
| `save_summaries_secs` | The frequency, in secs, that the summaries are written to disk using a default summary saver. If both `save_summaries_steps` and `save_summaries_secs` are set to `None`, then the default summary saver isn't used. Default not enabled. |
| `config` | an instance of [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> proto used to configure the session. It's the `config` argument of constructor of [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br>. |
| `stop_grace_period_secs` | Number of seconds given to threads to stop after `close()` has been called. |
| `log_step_count_steps` | The frequency, in number of global steps, that the global step/sec is logged. |
| `max_wait_secs` | Maximum time workers should wait for the session to become available. This should be kept relatively short to help detect incorrect code, but sometimes may need to be increased if the chief takes a while to start up. |
| `save_checkpoint_steps` | The frequency, in number of global steps, that a checkpoint is saved using a default checkpoint saver. If both `save_checkpoint_steps` and `save_checkpoint_secs` are set to `None`, then the default checkpoint saver isn't used. If both are provided, then only `save_checkpoint_secs` is used. Default not enabled. |
| `summary_dir` | A string. Optional path to a directory where to save summaries. If None, checkpoint\_dir is used instead. |
| `save_graph_def` | Whether to save the GraphDef and MetaGraphDef to `checkpoint_dir`. The GraphDef is saved after the session is created as `graph.pbtxt`. MetaGraphDefs are saved out for every checkpoint as `model.ckpt-*.meta`. |

|     |
| --- |
| Returns<br>------- |     |
| A `MonitoredSession` object. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.