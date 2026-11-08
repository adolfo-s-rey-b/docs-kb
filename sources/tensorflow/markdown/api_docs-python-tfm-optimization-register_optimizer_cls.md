[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.register\_optimizer\_cls Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/optimizer_factory.py#L76-L100)

Register customize optimizer cls.

#### View aliases

**Main aliases**

[`tfm.optimization.optimizer_factory.register_optimizer_cls`](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls)

tfm.optimization.register_optimizer_cls(
        key: str,
        optimizer_config_cls: Union[tf_keras.optimizers.Optimizer, tf_keras.optimizers.legacy.Optimizer,\
            tf_keras.optimizers.experimental.Optimizer],
        use_legacy_optimizer: bool = True
    )

The user will still need to subclass data classes in configs.optimization\_config to be used with OptimizerFactory.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | A string to that the optimizer\_config\_cls is registered with. |
| `optimizer_config_cls` | A class which inherits tf\_keras.optimizers.Optimizer. |
| `use_legacy_optimizer` | A boolean that indicates if using legacy optimizers. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.