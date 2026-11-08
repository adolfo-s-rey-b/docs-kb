[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.set\_memory\_growth Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L741-L766)

Set if memory growth should be enabled for a `PhysicalDevice`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.set_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)

tf.config.experimental.set_memory_growth(
        device, enable
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model) | *   [Universal Sentence Encoder SentEval demo](https://www.tensorflow.org/hub/tutorials/senteval_for_universal_sentence_encoder_cmlm)<br>    <br>*   [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://www.tensorflow.org/probability/examples/Bayesian_Gaussian_Mixture_Model)<br>    <br>*   [Modeling COVID-19 spread in Europe and the effect of interventions](https://www.tensorflow.org/probability/examples/Estimating_COVID_19_in_11_European_countries) |

If memory growth is enabled for a `PhysicalDevice`, the runtime initialization will not allocate all memory on the device. Memory growth cannot be configured on a `PhysicalDevice` with virtual devices configured.

#### For example:

    physical_devices = tf.config.list_physical_devices('GPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | `PhysicalDevice` to configure |
| `enable` | (Boolean) Whether to enable or disable memory growth |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Invalid `PhysicalDevice` specified. |
| `RuntimeError` | Runtime is already initialized. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.