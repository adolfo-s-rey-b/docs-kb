[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#methods)
    *   [get\_per\_replica\_batch\_size](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#get_per_replica_batch_size)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.InputContext Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#methods)
    *   [get\_per\_replica\_batch\_size](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext#get_per_replica_batch_size)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L840-L910)

A class wrapping information needed by an input function.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)

tf.distribute.InputContext(
        num_input_pipelines=1, input_pipeline_id=0, num_replicas_in_sync=1
    )

This is a context class that is passed to the user's input function and contains information about the compute replicas and input pipelines. The number of compute replicas (in sync training) helps compute the local batch size from the desired global batch size for each replica. The input pipeline information can be used to return a different subset of the input in each replica (for e.g. shard the input pipeline, use a different input source etc).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_input_pipelines` | the number of input pipelines in a cluster. |
| `input_pipeline_id` | the current input pipeline id, should be an int in \[0,`num_input_pipelines`). |\
| `num_replicas_in_sync` | the number of replicas that are in sync. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input_pipeline_id` | Returns the input pipeline ID. |\
| `num_input_pipelines` | Returns the number of input pipelines. |\
| `num_replicas_in_sync` | Returns the number of compute replicas in sync. |\
\
Methods\
-------\
\
### `get_per_replica_batch_size`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L888-L906)\
\
get_per_replica_batch_size(\
        global_batch_size\
    )\
\
Returns the per-replica batch size.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `global_batch_size` | the global batch size which should be divisible by `num_replicas_in_sync`. |\
\
|     |\
| --- |\
| Returns |     |\
| the per-replica batch size. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if `global_batch_size` not divisible by `num_replicas_in_sync`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.