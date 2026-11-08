[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.enable\_mixed\_precision\_graph\_rewrite Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/mixed_precision.py#L80-L213)

Enable mixed precision via a graph rewrite.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.enable_mixed_precision_graph_rewrite`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/enable_mixed_precision_graph_rewrite)

tf.compat.v1.mixed_precision.enable_mixed_precision_graph_rewrite(
        opt, loss_scale='dynamic'
    )

Mixed precision is the use of both float32 and float16 data types when training a model to improve performance. This is achieved via a graph rewrite operation and a loss-scale optimizer.

Performing arithmetic operations in float16 takes advantage of specialized processing units, such as NVIDIA Tensor Cores, for much higher arithmetic throughput. However, due to the smaller representable range, performing the entire training with float16 can result in gradient underflow, that is, small gradient values becoming zeroes. Instead, performing only select arithmetic operations in float16 results in higher throughput and decreased training time when using compatible hardware accelerators while also reducing memory usage, typically without sacrificing model accuracy.

#### Example:

model = tf.keras.models.Sequential([\
        tf.keras.layers.Dense(64, activation='relu'),\
        tf.keras.layers.Dense(64, activation='softmax'),\
    ])
    
    opt = tf.keras.optimizers.SGD()
    opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
    model.compile(loss="mse", optimizer=opt)
    
    x_train = np.random.random((1024, 64))
    y_train = np.random.random((1024, 64))
    model.fit(x_train, y_train)

Calling `enable_mixed_precision_graph_rewrite(opt)` enables the graph rewrite operation before computing gradients. The function additionally returns an `Optimizer` (`opt`) wrapped with a `LossScaleOptimizer`. This prevents underflow in the float16 tensors during the backward pass. An optimizer of type `tf.train.Optimizer` or [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 must be passed to this function, which will then be wrapped to use loss scaling.

The graph rewrite operation changes the `dtype` of certain operations in the graph from float32 to float16. There are several categories of operations that are either included or excluded by this rewrite operation. The following categories of Ops are defined inside corresponding functions under the class `AutoMixedPrecisionLists` in [auto\_mixed\_precision\_lists.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/grappler/optimizers/auto_mixed_precision_lists.h)
:

*   `ClearList`: Ops that do not have numerically significant adverse effects. E.g. `ArgMax` and `Floor`.
*   `AllowList`: Ops that are considered numerically safe for execution in float16, and thus are always converted. E.g. `Conv2D`.
*   `DenyList`: Ops that are numerically unsafe to execute in float16 and can negatively affect downstream nodes. E.g. `Softmax`.
*   `GrayList`: Ops that are considered numerically safe for execution in float16 unless downstream from a DenyList Op. E.g. `Add` and `AvgPool`.

When this function is used, gradients should only be computed and applied with the returned optimizer, either by calling `opt.minimize()` or `opt.compute_gradients()` followed by `opt.apply_gradients()`. Gradients should not be computed with [`tf.gradients`](https://www.tensorflow.org/api_docs/python/tf/gradients)
 or [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
. This is because the returned optimizer will apply loss scaling, and [`tf.gradients`](https://www.tensorflow.org/api_docs/python/tf/gradients)
 or [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 will not. If you do directly use [`tf.gradients`](https://www.tensorflow.org/api_docs/python/tf/gradients)
 or [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
, your model may not converge due to float16 underflow problems.

When eager execution is enabled, the mixed precision graph rewrite is only enabled within [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s, as outside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s, there is no graph.

For NVIDIA GPUs with Tensor cores, as a general performance guide, dimensions (such as batch size, input size, output size, and channel counts) should be powers of two if under 256, or otherwise divisible by 8 if above 256. For more information, check out the [NVIDIA Deep Learning Performance Guide](https://docs.nvidia.com/deeplearning/sdk/dl-performance-guide/index.html)
.

Currently, mixed precision is only enabled on NVIDIA Tensor Core GPUs with Compute Capability 7.0 and above (Volta, Turing, or newer architectures). The parts of the graph on CPUs and TPUs are untouched by the graph rewrite.

|     |
| --- |
| Raises<br>------ |     |
| `ValueError`, if the [`tf.keras.mixed_precision`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision)<br> API is also used by calling [`tf.keras.mixed_precision.set_global_policy`](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_dtype_policy)<br>. Only one mixed precision API can be used. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `opt` | An instance of a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)<br> or a `tf.train.Optimizer`. |
| `loss_scale` | Either an int/float, the string `"dynamic"`, or an instance of a `tf.mixed_precision.experimental.LossScale`. The loss scale to use. It is recommended to keep this as its default value of `"dynamic"`, which will adjust the scaling automatically to prevent `Inf` or `NaN` values. |

|     |
| --- |
| Returns<br>------- |     |
| A version of `opt` that will use loss scaling to prevent underflow. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.