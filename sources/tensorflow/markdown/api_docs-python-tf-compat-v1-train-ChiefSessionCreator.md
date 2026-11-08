[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#methods)
    *   [create\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#create_session)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.ChiefSessionCreator Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#methods)
    *   [create\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/ChiefSessionCreator#create_session)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L622-L673)

Creates a tf.compat.v1.Session for a chief.

Inherits From: [`SessionCreator`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionCreator)

tf.compat.v1.train.ChiefSessionCreator(
        scaffold=None,
        master='',
        config=None,
        checkpoint_dir=None,
        checkpoint_filename_with_path=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scaffold` | A `Scaffold` used for gathering or building supportive ops. If not specified a default one is created. It's used to finalize the graph. |
| `master` | `String` representation of the TensorFlow master to use. |
| `config` | `ConfigProto` proto used to configure the session. |
| `checkpoint_dir` | A string. Optional path to a directory where to restore variables. |
| `checkpoint_filename_with_path` | Full file name path to the checkpoint file. |

Methods
-------

### `create_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L663-L673)

create_session()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.