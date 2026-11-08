[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#call)
        
    *   [reset\_covariance\_matrix](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#reset_covariance_matrix)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.RandomFeatureGaussianProcess Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#call)
        
    *   [reset\_covariance\_matrix](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess#reset_covariance_matrix)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/gaussian_process.py#L23-L267)

Gaussian process layer with random feature approximation \[1\].

tfm.nlp.layers.RandomFeatureGaussianProcess(
        units,
        num_inducing=1024,
        gp_kernel_type='gaussian',
        gp_kernel_scale=1.0,
        gp_output_bias=0.0,
        normalize_input=False,
        gp_kernel_scale_trainable=False,
        gp_output_bias_trainable=False,
        gp_cov_momentum=0.999,
        gp_cov_ridge_penalty=1.0,
        scale_random_features=True,
        use_custom_random_features=True,
        custom_random_features_initializer=None,
        custom_random_features_activation=None,
        l2_regularization=1e-06,
        gp_cov_likelihood='gaussian',
        return_gp_cov=True,
        return_random_features=False,
        dtype=None,
        name='random_feature_gaussian_process',
        **gp_output_kwargs
    )

During training, the model updates the maximum a posteriori (MAP) logits estimates and posterior precision matrix using minibatch statistics. During inference, the model divides the MAP logit estimates by the predictive standard deviation, which is equivalent to approximating the posterior mean of the predictive probability via the mean-field approximation.

User can specify different types of random features by setting `use_custom_random_features=True`, and change the initializer and activations of the custom random features. For example:

MLP Kernel: initializer='random\_normal', activation=tf.nn.relu RBF Kernel: initializer='random\_normal', activation=tf.math.cos

A linear kernel can also be specified by setting gp\_kernel\_type='linear' and `use_custom_random_features=True`.

\[1\]: Ali Rahimi and Benjamin Recht. Random Features for Large-Scale Kernel Machines. In _Neural Information Processing Systems_, 2007. [https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | (int) Number of output units. |
| `num_inducing` | (int) Number of random Fourier features used for approximating the Gaussian process. |
| `gp_kernel_type` | (string) The type of kernel function to use for Gaussian process. Currently default to 'gaussian' which is the Gaussian RBF kernel. |
| `gp_kernel_scale` | (float) The length-scale parameter of the a shift-invariant kernel function, i.e., for RBF kernel: exp(-\|x1 - x2\|**2 / gp\_kernel\_scale).** |
| `gp_output_bias` | (float) Scalar initial value for the bias vector. |
| `normalize_input` | (bool) Whether to normalize the input to Gaussian process. |
| `gp_kernel_scale_trainable` | (bool) Whether the length scale variable is trainable. |
| `gp_output_bias_trainable` | (bool) Whether the bias is trainable. |
| `gp_cov_momentum` | (float) A discount factor used to compute the moving average for posterior covariance matrix. |
| `gp_cov_ridge_penalty` | (float) Initial Ridge penalty to posterior covariance matrix. |
| `scale_random_features` | (bool) Whether to scale the random feature by sqrt(2. / num\_inducing). |
| `use_custom_random_features` | (bool) Whether to use custom random features implemented using tf\_keras.layers.Dense. |
| `custom_random_features_initializer` | (str or callable) Initializer for the random features. Default to random normal which approximates a RBF kernel function if activation function is cos. |
| `custom_random_features_activation` | (callable) Activation function for the random feature layer. Default to cosine which approximates a RBF kernel function. |
| `l2_regularization` | (float) The strength of l2 regularization on the output weights. |
| `gp_cov_likelihood` | (string) Likelihood to use for computing Laplace approximation for covariance matrix. Default to `gaussian`. |
| `return_gp_cov` | (bool) Whether to also return GP covariance matrix. If False then no covariance learning is performed. |
| `return_random_features` | (bool) Whether to also return random features. |
| `dtype` | (tf.DType) Input data type. |
| `name` | (string) Layer name. |
| `**gp_output_kwargs`<a id="gp\_output\_kwargs"> | Additional keyword arguments to dense output layer. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `units` | (int) The dimensionality of layer. |
| `num_inducing` | (int) The number of random features for the approximation. |
| `is_training` | (tf.bool) Whether the layer is set in training mode. If so the layer updates the Gaussian process' variance estimate using statistics computed from the incoming minibatches. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/gaussian_process.py#L233-L267)

call(
        inputs, global_step=None, training=None
    )

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

### `reset_covariance_matrix`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/gaussian_process.py#L225-L231)

reset_covariance_matrix()

Resets covariance matrix of the GP layer.

This function is useful for reseting the model's covariance matrix at the beginning of a new epoch.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.