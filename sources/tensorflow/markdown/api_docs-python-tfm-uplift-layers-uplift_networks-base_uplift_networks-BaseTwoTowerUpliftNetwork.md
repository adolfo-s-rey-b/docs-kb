[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fuplift%2Flayers%2Fuplift_networks%2Fbase_uplift_networks%2FBaseTwoTowerUpliftNetwork&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.layers.uplift\_networks.base\_uplift\_networks.BaseTwoTowerUpliftNetwork Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/base_uplift_networks.py#L24-L39)

Abstract class for uplift layers that compute control and treatment logits.

tfm.uplift.layers.uplift_networks.base_uplift_networks.BaseTwoTowerUpliftNetwork(
        trainable=True, name=None, dtype=None, dynamic=False, **kwargs
    )

A TwoTowerUpliftNetwork layer is expected to take in a dictionary of feature tensors and compute two sets of logits: one for the control group and one for treatment group.

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/base_uplift_networks.py#L32-L39)

@abc.abstractmethod

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.