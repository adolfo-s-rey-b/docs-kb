[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/CrossTrainerCache#main-content)

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
    

tf.data.experimental.service.CrossTrainerCache Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/data_service_ops.py#L120-L158)

Options related to the tf.data service cross trainer cache.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.service.CrossTrainerCache`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/CrossTrainerCache)

tf.data.experimental.service.CrossTrainerCache(
        trainer_id
    )

This is used to enable cross-trainer cache when distributing a dataset. For example:

dataset = dataset.apply(tf.data.experimental.service.distribute(
        processing_mode=tf.data.experimental.service.ShardingPolicy.OFF,
        service=FLAGS.tf_data_service_address,
        job_name="job",
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id=trainer_id())))

For more details, refer to [https://www.tensorflow.org/api\_docs/python/tf/data/experimental/service#sharing\_tfdata\_service\_with\_concurrent\_trainers](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#sharing_tfdata_service_with_concurrent_trainers)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `trainer_id` | Each training job has a unique ID. Once a job has consumed data, the data remains in the cache and is re-used by jobs with different `trainer_id`s. Requests with the same `trainer_id` do not re-use data. |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if `trainer_id` is empty. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.