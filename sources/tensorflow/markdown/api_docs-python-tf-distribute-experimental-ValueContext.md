[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.ValueContext Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ValueContext#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L913-L976)

A class wrapping information needed by a distribute function.

tf.distribute.experimental.ValueContext(
        replica_id_in_sync_group=0, num_replicas_in_sync=1
    )

This is a context class that is passed to the `value_fn` in `strategy.experimental_distribute_values_from_function` and contains information about the compute replicas. The `num_replicas_in_sync` and `replica_id` can be used to customize the value on each replica.

#### Example usage:

1.  Directly constructed.
    
    def value_fn(context):
        
2.  Passed in by `experimental_distribute_values_from_function`.
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        

|     |     |
| --- | --- |
| Args<br>---- |     |
| `replica_id_in_sync_group` | the current replica\_id, should be an int in \[0,`num_replicas_in_sync`). |\
| `num_replicas_in_sync` | the number of replicas that are in sync. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `num_replicas_in_sync` | Returns the number of compute replicas in sync. |\
| `replica_id_in_sync_group` | Returns the replica ID. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.