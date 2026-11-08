Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fsdca_optimizer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.sdca\_optimizer Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_optimizer#returns)
    

Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

tf.compat.v1.train.sdca_optimizer(
        sparse_example_indices: Annotated[List[Any], _atypes.Int64],
        sparse_feature_indices: Annotated[List[Any], _atypes.Int64],
        sparse_feature_values: Annotated[List[Any], _atypes.Float32],
        dense_features: Annotated[List[Any], _atypes.Float32],
        example_weights: Annotated[Any, _atypes.Float32],
        example_labels: Annotated[Any, _atypes.Float32],
        sparse_indices: Annotated[List[Any], _atypes.Int64],
        sparse_weights: Annotated[List[Any], _atypes.Float32],
        dense_weights: Annotated[List[Any], _atypes.Float32],
        example_state_data: Annotated[Any, _atypes.Float32],
        loss_type: str,
        l1: float,
        l2: float,
        num_loss_partitions: int,
        num_inner_iterations: int,
        adaptative: bool = True,
        name=None
    )

linear models with L1 + L2 regularization. As global optimization objective is strongly-convex, the optimizer optimizes the dual objective at each step. The optimizer applies each update one example at a time. Examples are sampled uniformly, and the optimizer is learning rate free and enjoys linear convergence rate.

[Proximal Stochastic Dual Coordinate Ascent](http://arxiv.org/pdf/1211.2717v1.pdf)
.  
Shai Shalev-Shwartz, Tong Zhang. 2012

LossObjective\=∑fi(wxi)+(l2/2)∗|w|2+l1∗|w|

[Adding vs. Averaging in Distributed Primal-Dual Optimization](http://arxiv.org/abs/1502.03508)
.  
Chenxin Ma, Virginia Smith, Martin Jaggi, Michael I. Jordan, Peter Richtarik, Martin Takac. 2015

[Stochastic Dual Coordinate Ascent with Adaptive Probabilities](https://arxiv.org/abs/1502.08053)
.  
Dominik Csiba, Zheng Qu, Peter Richtarik. 2015

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sparse_example_indices` | A list of `Tensor` objects with type `int64`. a list of vectors which contain example indices. |
| `sparse_feature_indices` | A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`. a list of vectors which contain feature indices. |
| `sparse_feature_values` | A list of `Tensor` objects with type `float32`. a list of vectors which contains feature value associated with each feature group. |
| `dense_features` | A list of `Tensor` objects with type `float32`. a list of matrices which contains the dense feature values. |
| `example_weights` | A `Tensor` of type `float32`. a vector which contains the weight associated with each example. |
| `example_labels` | A `Tensor` of type `float32`. a vector which contains the label/target associated with each example. |
| `sparse_indices` | A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`. a list of vectors where each value is the indices which has corresponding weights in sparse\_weights. This field maybe omitted for the dense approach. |
| `sparse_weights` | A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`. a list of vectors where each value is the weight associated with a sparse feature group. |
| `dense_weights` | A list with the same length as `dense_features` of `Tensor` objects with type `float32`. a list of vectors where the values are the weights associated with a dense feature group. |
| `example_state_data` | A `Tensor` of type `float32`. a list of vectors containing the example state data. |
| `loss_type` | A `string` from: `"logistic_loss", "squared_loss", "hinge_loss", "smooth_hinge_loss", "poisson_loss"`. Type of the primal loss. Currently SdcaSolver supports logistic, squared and hinge losses. |
| `l1` | A `float`. Symmetric l1 regularization strength. |
| `l2` | A `float`. Symmetric l2 regularization strength. |
| `num_loss_partitions` | An `int` that is `>= 1`. Number of partitions of the global loss function. |
| `num_inner_iterations` | An `int` that is `>= 1`. Number of iterations per mini-batch. |
| `adaptative` | An optional `bool`. Defaults to `True`. Whether to use Adaptive SDCA for the inner loop. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (out\_example\_state\_data, out\_delta\_sparse\_weights, out\_delta\_dense\_weights). |     |
| `out_example_state_data` | A `Tensor` of type `float32`. |
| `out_delta_sparse_weights` | A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`. |
| `out_delta_dense_weights` | A list with the same length as `dense_features` of `Tensor` objects with type `float32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.