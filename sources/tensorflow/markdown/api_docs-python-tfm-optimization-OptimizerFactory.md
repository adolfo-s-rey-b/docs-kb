[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#methods)
    *   [build\_learning\_rate](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#build_learning_rate)
        
    *   [build\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#build_optimizer)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.OptimizerFactory Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#methods)
    *   [build\_learning\_rate](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#build_learning_rate)
        
    *   [build\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory#build_optimizer)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/optimizer_factory.py#L103-L267)

Optimizer factory class.

#### View aliases

**Main aliases**

[`tfm.optimization.optimizer_factory.OptimizerFactory`](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory)

tfm.optimization.OptimizerFactory(
        config: tfm.optimization.OptimizationConfig
    )

This class builds learning rate and optimizer based on an optimization config. To use this class, you need to do the following: (1) Define optimization config, this includes optimizer, and learning rate schedule. (2) Initialize the class using the optimization config. (3) Build learning rate. (4) Build optimizer.

This is a typical example for using this class:

params = {
          'optimizer': {
              'type': 'sgd',
              'sgd': {'momentum': 0.9}
          },
          'learning_rate': {
              'type': 'stepwise',
              'stepwise': {'boundaries': [10000, 20000],
                           'values': [0.1, 0.01, 0.001]}
          },
          'warmup': {
              'type': 'linear',
              'linear': {'warmup_steps': 500, 'warmup_learning_rate': 0.01}
          }
      }
    opt_config = OptimizationConfig(params)
    opt_factory = OptimizerFactory(opt_config)
    lr = opt_factory.build_learning_rate()
    optimizer = opt_factory.build_optimizer(lr)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | OptimizationConfig instance contain optimization config. |

Methods
-------

### `build_learning_rate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/optimizer_factory.py#L164-L183)

build_learning_rate()

Build learning rate.

Builds learning rate from config. Learning rate schedule is built according to the learning rate config. If learning rate type is consant, lr\_config.learning\_rate is returned.

|     |
| --- |
| Returns |     |
| tf\_keras.optimizers.schedules.LearningRateSchedule instance. If learning rate type is consant, lr\_config.learning\_rate is returned. |     |

### `build_optimizer`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/optimizer_factory.py#L185-L267)

build_optimizer(
        lr: Union[tf_keras.optimizers.schedules.LearningRateSchedule, float],
        gradient_aggregator: Optional[Callable[[List[Tuple[tf.Tensor, tf.Tensor]]], List[Tuple[tf.Tensor,\
            tf.Tensor]]]] = None,
        gradient_transformers: Optional[List[Callable[[List[Tuple[tf.Tensor, tf.Tensor]]], List[Tuple[tf.\
            Tensor, tf.Tensor]]]]] = None,
        postprocessor: Optional[Callable[[tf_keras.optimizers.Optimizer], tf_keras.optimizers.\
            Optimizer]] = None,
        use_legacy_optimizer: bool = True
    )

Build optimizer.

Builds optimizer from config. It takes learning rate as input, and builds the optimizer according to the optimizer config. Typically, the learning rate built using self.build\_lr() is passed as an argument to this method.

|     |     |
| --- | --- |
| Args |     |
| `lr` | A floating point value, or a tf\_keras.optimizers.schedules.LearningRateSchedule instance. |
| `gradient_aggregator` | Optional function to overwrite gradient aggregation. |
| `gradient_transformers` | Optional list of functions to use to transform gradients before applying updates to Variables. The functions are applied after gradient\_aggregator. The functions should accept and return a list of (gradient, variable) tuples. clipvalue, clipnorm, global\_clipnorm should not be set when gradient\_transformers is passed. |
| `postprocessor` | An optional function for postprocessing the optimizer. It takes an optimizer and returns an optimizer. |
| `use_legacy_optimizer` | A boolean that indicates if using legacy optimizers. |

|     |
| --- |
| Returns |     |
| `tf_keras.optimizers.legacy.Optimizer` or `tf_keras.optimizers.experimental.Optimizer` instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.