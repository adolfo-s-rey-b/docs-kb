[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/register_model_builder#main-content)

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
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.factory\_3d.register\_model\_builder Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/factory_3d.py#L27-L52)

Decorates a builder of model class.

tfm.vision.factory_3d.register_model_builder(
        key: str
    )

The builder should be a Callable (a class or a function). This decorator supports registration of backbone builder as follows:

class MyModel(tf_keras.Model):
      pass
    
    @register_backbone_builder('mybackbone')
    def builder(input_specs, config, l2_reg):
      return MyModel(...)
    
    # Builds a MyModel object.
    my_backbone = build_backbone_3d(input_specs, config, l2_reg)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | the key to look up the builder. |

|     |
| --- |
| Returns<br>------- |     |
| A callable for use as class decorator that registers the decorated class for creation from an instance of model class. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.