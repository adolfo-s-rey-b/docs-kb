[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fvariable_creator_scope&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.variable\_creator\_scope Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_creator_scope#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L2643-L2715)

Scope which defines a variable creation function to be used by variable().

@tf_contextlib.contextmanager

variable\_creator is expected to be a function with the following signature:

  def variable_creator(next_creator, **kwargs)

The creator is supposed to eventually call the next\_creator to create a variable if it does want to create a variable and not call Variable or ResourceVariable directly. This helps make creators composable. A creator may choose to create multiple variables, return already existing variables, or simply register that a variable was created and defer to the next creators in line. Creators can also modify the keyword arguments seen by the next creators.

Custom getters in the variable scope will eventually resolve down to these custom creators when they do create variables.

The valid keyword arguments in kwds are:

*   initial\_value: A `Tensor`, or Python object convertible to a `Tensor`, which is the initial value for the Variable. The initial value must have a shape specified unless `validate_shape` is set to False. Can also be a callable with no argument that returns the initial value when called. In that case, `dtype` must be specified. (Note that initializer functions from init\_ops.py must first be bound to a shape before being used here.)
*   trainable: If `True`, the default, also adds the variable to the graph collection `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as the default list of variables to use by the `Optimizer` classes. `trainable` defaults to `True`, unless `synchronization` is set to `ON_READ`, in which case it defaults to `False`.
*   collections: List of graph collections keys. The new variable is added to these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
*   validate\_shape: If `False`, allows the variable to be initialized with a value of unknown shape. If `True`, the default, the shape of `initial_value` must be known.
*   caching\_device: Optional device string describing where the Variable should be cached for reading. Defaults to the Variable's device. If not `None`, caches on another device. Typical use is to cache on the device where the Ops using the Variable reside, to deduplicate copying through `Switch` and other conditional statements.
*   name: Optional name for the variable. Defaults to `'Variable'` and gets uniquified automatically.
*   dtype: If set, initial\_value will be converted to the given type. If `None`, either the datatype will be kept (if `initial_value` is a Tensor), or `convert_to_tensor` will decide.
*   constraint: A constraint function to be applied to the variable after updates by some algorithms.
*   use\_resource: if True, a ResourceVariable is always created.
*   synchronization: Indicates when a distributed a variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableSynchronization`](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization)
    . By default the synchronization is set to `AUTO` and the current `DistributionStrategy` chooses when to synchronize.
*   aggregation: Indicates how a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableAggregation`](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation)
    .

This set may grow over time, so it's important the signature of creators is as mentioned above.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `variable_creator` | the passed creator |

|     |
| --- |
| Yields<br>------ |     |
| A scope in which the creator is active |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.