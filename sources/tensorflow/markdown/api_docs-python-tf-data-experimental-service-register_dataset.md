[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/register_dataset#main-content)

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
    

tf.data.experimental.service.register\_dataset Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/data_service_ops.py#L894-L947)

Registers a dataset with the tf.data service.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.service.register_dataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/register_dataset)

tf.data.experimental.service.register_dataset(
        service, dataset, compression='AUTO', dataset_id=None
    ) -> tf.Tensor

`register_dataset` registers a dataset with the tf.data service so that datasets can be created later with [`tf.data.experimental.service.from_dataset_id`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/from_dataset_id)
. This is useful when the dataset is registered by one process, then used in another process. When the same process is both registering and reading from the dataset, it is simpler to use [`tf.data.experimental.service.distribute`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/distribute)
 instead.

If the dataset is already registered with the tf.data service, `register_dataset` returns the already-registered dataset's id.

    dispatcher = tf.data.experimental.service.DispatchServer()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `service` | A string or a tuple indicating how to connect to the tf.data service. If it's a string, it should be in the format `[<protocol>://]<address>`, where `<address>` identifies the dispatcher address and `<protocol>` can optionally be used to override the default protocol to use. If it's a tuple, it should be (protocol, address). |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> to register with the tf.data service. |
| `compression` | (Optional.) How to compress the dataset's elements before transferring them over the network. "AUTO" leaves the decision of how to compress up to the tf.data service runtime. "SNAPPY" forces snappy compression. `None` indicates not to compress. |
| `dataset_id` | (Optional.) By default, tf.data service generates a unique (string) ID for each registered dataset. If a `dataset_id` is provided, it will use the specified ID. If a dataset with a matching ID already exists, no new dataset is registered. This is useful if multiple training jobs want to (re)use the same dataset for training. In this case, they can register the dataset with the same dataset ID. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar string tensor representing the dataset ID. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.