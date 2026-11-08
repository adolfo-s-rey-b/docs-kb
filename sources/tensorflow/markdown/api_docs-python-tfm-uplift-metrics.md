[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics#modules)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.uplift.metrics Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics#modules)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/__init__.py)

Metrics package definition.

Modules
-------

[`label_mean`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/label_mean)
 module: Keras metric for computing the label mean sliced by treatment group.

[`label_variance`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/label_variance)
 module: Keras metric for computing the label variance sliced by treatment group.

[`loss_metric`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric)
 module: Keras metric for computing a loss sliced by treatment group.

[`metric_configs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs)
 module: Metric configurations for TF Model Garden.

[`poisson_metrics`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics)
 module: Poisson regression metrics.

[`sliced_metric`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric)
 module: Keras metric for reporting metrics sliced by a feature.

[`treatment_fraction`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/treatment_fraction)
 module: Keras metric for computing fraction of treated examples.

[`treatment_sliced_metric`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/treatment_sliced_metric)
 module: Keras metric for computing sliced metric values based on treatment group.

[`uplift_mean`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/uplift_mean)
 module: Keras metric for computing the mean uplift sliced by treatment group.

[`variance`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/variance)
 module: Keras metric for computing the (weighted) variance of a tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.