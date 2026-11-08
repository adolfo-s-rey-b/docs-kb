[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/distribute#main-content)

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
    

tf.data.experimental.service.distribute Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/data_service_ops.py#L577-L826)

A transformation that moves dataset processing to the tf.data service.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.service.distribute`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/distribute)

tf.data.experimental.service.distribute(
        processing_mode,
        service,
        job_name=None,
        consumer_index=None,
        num_consumers=None,
        max_outstanding_requests=None,
        data_transfer_protocol=None,
        compression='AUTO',
        cross_trainer_cache=None,
        target_workers='AUTO'
    ) -> Callable[tf.data.Dataset, tf.data.Dataset]

When you iterate over a dataset containing the `distribute` transformation, the tf.data service creates a "job" which produces data for the dataset iteration.

The tf.data service uses a cluster of workers to prepare data for training your model. The `processing_mode` argument to [`tf.data.experimental.service.distribute`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/distribute)
 describes how to leverage multiple workers to process the input dataset. Currently, there are two processing modes to choose from: "distributed\_epoch" and "parallel\_epochs".

"distributed\_epoch" means that the dataset will be split across all tf.data service workers. The dispatcher produces "splits" for the dataset and sends them to workers for further processing. For example, if a dataset begins with a list of filenames, the dispatcher will iterate through the filenames and send the filenames to tf.data workers, which will perform the rest of the dataset transformations on those files. "distributed\_epoch" is useful when your model needs to see each element of the dataset exactly once, or if it needs to see the data in a generally-sequential order. "distributed\_epoch" only works for datasets with splittable sources, such as [`Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices)
, [`Dataset.list_files`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#list_files)
, or [`Dataset.range`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#range)
.

"parallel\_epochs" means that the entire input dataset will be processed independently by each of the tf.data service workers. For this reason, it is important to shuffle data (e.g. filenames) non-deterministically, so that each worker will process the elements of the dataset in a different order. "parallel\_epochs" can be used to distribute datasets that aren't splittable.

With two workers, "parallel\_epochs" will produce every element of the dataset twice:

    dispatcher = tf.data.experimental.service.DispatchServer()

"distributed\_epoch", on the other hand, will still produce each element once:

    dispatcher = tf.data.experimental.service.DispatchServer()

When using `apply(tf.data.experimental.service.distribute(...))`, the dataset before the `apply` transformation executes within the tf.data service, while the operations after `apply` happen within the local process.

    dispatcher = tf.data.experimental.service.DispatchServer()

In the above example, the dataset operations (before applying the `distribute` function on the elements) will be executed on the tf.data workers, and the elements are provided over RPC. The remaining transformations (after the call to `distribute`) will be executed locally. The dispatcher and the workers will bind to usused free ports (which are chosen at random), in order to communicate with each other. However, to bind them to specific ports, the `port` parameter can be passed.

The `job_name` argument allows jobs to be shared across multiple datasets. Instead of each dataset creating its own job, all datasets with the same `job_name` will consume from the same job. A new job will be created for each iteration of the dataset (with each repetition of [`Dataset.repeat`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#repeat)
 counting as a new iteration). Suppose the `DispatchServer` is serving on `localhost:5000` and two training workers (in either a single client or multi-client setup) iterate over the below dataset, and there is a single tf.data worker:

range5_dataset = tf.data.Dataset.range(5)
    dataset = range5_dataset.apply(tf.data.experimental.service.distribute(
        "parallel_epochs", "localhost:5000", job_name="my_job_name"))
    for iteration in range(3):
      print(list(dataset))

The elements of each job will be split between the two processes, with elements being consumed by the processes on a first-come first-served basis. One possible result is that process 1 prints

[0, 2, 4]
    [0, 1, 3]
    [1]

and process 2 prints

[1, 3]
    [2, 4]
    [0, 2, 3, 4]

Job names must not be re-used across different training jobs within the lifetime of the tf.data service. In general, the tf.data service is expected to live for the duration of a single training job. To use the tf.data service with multiple training jobs, make sure to use different job names to avoid conflicts. For example, suppose a training job calls `distribute` with `job_name="job"` and reads until end of input. If another independent job connects to the same tf.data service and tries to read from `job_name="job"`, it will immediately receive end of input, without getting any data.

**Coordinated data read**

By default, when multiple consumers read from the same job, they receive data on a first-come first-served basis. In some use cases, it is advantageous to coordinate the consumers. At each step, consumers read data from the same worker.

For example, the tf.data service can be used to coordinate example sizes across a cluster during synchronous training, so that during each step all replicas train on similar-sized elements. To achieve this, define a dataset which generates rounds of `num_consumers` consecutive similar-sized batches, then enable coordinated reads by setting `consumer_index` and `num_consumers`.

**Keras and Distribution Strategies**

The dataset produced by the `distribute` transformation can be passed to Keras' [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 or Distribution Strategy's [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)
 like any other [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
. We recommend setting a `job_name` on the call to `distribute` so that if there are multiple workers, they read data from the same job. Note that the autosharding normally performed by `experimental_distribute_dataset` will be disabled when setting a `job_name`, since sharing the job already results in splitting data across the workers. When using a shared job, data will be dynamically balanced across workers, so that they reach end of input about the same time. This results in better worker utilization than with autosharding, where each worker processes an independent set of files, and some workers may run out of data earlier than others.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `processing_mode` | A [`tf.data.experimental.service.ShardingPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/ShardingPolicy)<br> specifying how to shard the dataset among tf.data workers. See [`tf.data.experimental.service.ShardingPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/ShardingPolicy)<br> for details. For backwards compatibility, `processing_mode` may also be set to the strings `"parallel_epochs"` or `"distributed_epoch"`, which are respectively equivalent to [`ShardingPolicy.OFF`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/ShardingPolicy#OFF)<br> and [`ShardingPolicy.DYNAMIC`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/ShardingPolicy#DYNAMIC)<br>. |
| `service` | A string or a tuple indicating how to connect to the tf.data service. If it's a string, it should be in the format `[<protocol>://]<address>`, where `<address>` identifies the dispatcher address and `<protocol>` can optionally be used to override the default protocol to use. If it's a tuple, it should be (protocol, address). |
| `job_name` | (Optional.) The name of the job. If provided, it must be a non-empty string. This argument makes it possible for multiple datasets to share the same job. The default behavior is that the dataset creates anonymous, exclusively owned jobs. |
| `consumer_index` | (Optional.) The index of the consumer in the range from `0` to `num_consumers`. Must be specified alongside `num_consumers`. When specified, consumers will read from the job in a strict round-robin order, instead of the default first-come-first-served order. |
| `num_consumers` | (Optional.) The number of consumers which will consume from the job. Must be specified alongside `consumer_index`. When specified, consumers will read from the job in a strict round-robin order, instead of the default first-come-first-served order. When `num_consumers` is specified, the dataset must have infinite cardinality to prevent a producer from running out of data early and causing consumers to go out of sync. |
| `max_outstanding_requests` | (Optional.) A limit on how many elements may be requested at the same time. You can use this option to control the amount of memory used, since `distribute` won't use more than `element_size` \* `max_outstanding_requests` of memory. |
| `data_transfer_protocol` | (Optional.) The protocol to use for transferring data with the tf.data service. If not provided, a protocol is determined at runtime. |
| `compression` | How to compress the dataset's elements before transferring them over the network. "AUTO" leaves the decision of how to compress up to the tf.data service runtime. `None` indicates not to compress. "SNAPPY" forces the use of snappy compression. |
| `cross_trainer_cache` | (Optional.) If a `CrossTrainerCache` object is provided, dataset iteration will be shared across concurrently running trainers. See https://www.tensorflow.org/api\_docs/python/tf/data/experimental/service#sharing\_tfdata\_service\_with\_concurrent\_trainers for details. |
| `target_workers` | (Optional.) Which workers to read from. If `"AUTO"`, tf.data runtime decides which workers to read from. If `"ANY"`, reads from any tf.data service workers. If `"LOCAL"`, only reads from local in-process tf.data service workers. `"AUTO"` works well for most cases, while users can specify other targets. For example, `"LOCAL"` helps avoid RPCs and data copy if every TF worker colocates with a tf.data service worker. Consumers of a shared job must use the same `target_workers`. Defaults to `"AUTO"`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Dataset` | A `Dataset` of the elements produced by the data service. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.