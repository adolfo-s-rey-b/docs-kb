[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#methods)
    *   [batch\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#batch_shape_tensor)
        
    *   [cdf](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#cdf)
        
    *   [copy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#copy)
        
    *   [covariance](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#covariance)
        
    *   [cross\_entropy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#cross_entropy)
        
    *   [entropy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#entropy)
        
    *   [event\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#event_shape_tensor)
        
    *   [is\_scalar\_batch](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#is_scalar_batch)
        
    *   [is\_scalar\_event](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#is_scalar_event)
        
    *   [kl\_divergence](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#kl_divergence)
        
    *   [log\_cdf](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_cdf)
        
    *   [log\_prob](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_prob)
        
    *   [log\_survival\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_survival_function)
        
    *   [mean](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#mean)
        
    *   [mode](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#mode)
        
    *   [param\_shapes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#param_shapes)
        
    *   [param\_static\_shapes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#param_static_shapes)
        
    *   [prob](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#prob)
        
    *   [quantile](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#quantile)
        
    *   [sample](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#sample)
        
    *   [stddev](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#stddev)
        
    *   [survival\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#survival_function)
        
    *   [variance](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#variance)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.distributions.Laplace Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#methods)
    *   [batch\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#batch_shape_tensor)
        
    *   [cdf](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#cdf)
        
    *   [copy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#copy)
        
    *   [covariance](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#covariance)
        
    *   [cross\_entropy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#cross_entropy)
        
    *   [entropy](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#entropy)
        
    *   [event\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#event_shape_tensor)
        
    *   [is\_scalar\_batch](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#is_scalar_batch)
        
    *   [is\_scalar\_event](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#is_scalar_event)
        
    *   [kl\_divergence](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#kl_divergence)
        
    *   [log\_cdf](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_cdf)
        
    *   [log\_prob](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_prob)
        
    *   [log\_survival\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#log_survival_function)
        
    *   [mean](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#mean)
        
    *   [mode](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#mode)
        
    *   [param\_shapes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#param_shapes)
        
    *   [param\_static\_shapes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#param_static_shapes)
        
    *   [prob](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#prob)
        
    *   [quantile](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#quantile)
        
    *   [sample](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#sample)
        
    *   [stddev](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#stddev)
        
    *   [survival\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#survival_function)
        
    *   [variance](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace#variance)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/laplace.py#L42-L213)

The Laplace distribution with location `loc` and `scale` parameters.

Inherits From: [`Distribution`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Distribution)

tf.compat.v1.distributions.Laplace(
        loc,
        scale,
        validate_args=False,
        allow_nan_stats=True,
        name='Laplace'
    )

#### Mathematical details

The probability density function (pdf) of this distribution is,

pdf(x; mu, sigma) = exp(-|x - mu| / sigma) / Z
    Z = 2 sigma

where `loc = mu`, `scale = sigma`, and `Z` is the normalization constant.

Note that the Laplace distribution can be thought of two exponential distributions spliced together "back-to-back."

The Lpalce distribution is a member of the [location-scale family](https://en.wikipedia.org/wiki/Location-scale_family)
, i.e., it can be constructed as,

X ~ Laplace(loc=0, scale=1)
    Y = loc + scale * X

|     |     |
| --- | --- |
| Args<br>---- |     |
| `loc` | Floating point tensor which characterizes the location (center) of the distribution. |
| `scale` | Positive floating point tensor which characterizes the spread of the distribution. |
| `validate_args` | Python `bool`, default `False`. When `True` distribution parameters are checked for validity despite possibly degrading runtime performance. When `False` invalid inputs may silently render incorrect outputs. |
| `allow_nan_stats` | Python `bool`, default `True`. When `True`, statistics (e.g., mean, mode, variance) use the value "`NaN`" to indicate the result is undefined. When `False`, an exception is raised if one or more of the statistic's batch members are undefined. |
| `name` | Python `str` name prefixed to Ops created by this class. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `loc` and `scale` are of different dtype. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `allow_nan_stats` | Python `bool` describing behavior when a stat is undefined.<br><br>Stats return +/- infinity when it makes sense. E.g., the variance of a Cauchy distribution is infinity. However, sometimes the statistic is undefined, e.g., if a distribution's pdf does not achieve a maximum within the support of the distribution, the mode is undefined. If the mean is undefined, then by definition the variance is undefined. E.g. the mean for Student's T for df = 1 is undefined (no clear way to say it is either + or - infinity), so the variance = E\[(X - mean)\*\*2\] is also undefined. |
| `batch_shape` | Shape of a single sample from a single event index as a `TensorShape`.<br><br>May be partially defined or unknown.<br><br>The batch dimensions are indexes into independent, non-identical parameterizations of this distribution. |
| `dtype` | The `DType` of `Tensor`s handled by this `Distribution`. |
| `event_shape` | Shape of a single sample from a single batch as a `TensorShape`.<br><br>May be partially defined or unknown. |
| `loc` | Distribution parameter for the location. |
| `name` | Name prepended to all ops created by this `Distribution`. |
| `parameters` | Dictionary of parameters used to instantiate this `Distribution`. |
| `reparameterization_type` | Describes how samples from the distribution are reparameterized.<br><br>Currently this is one of the static instances [`distributions.FULLY_REPARAMETERIZED`](https://www.tensorflow.org/probability/oryx/api_docs/python/oryx/distributions#FULLY_REPARAMETERIZED)<br> or [`distributions.NOT_REPARAMETERIZED`](https://www.tensorflow.org/probability/oryx/api_docs/python/oryx/distributions#NOT_REPARAMETERIZED)<br>. |
| `scale` | Distribution parameter for scale. |
| `validate_args` | Python `bool` indicating possibly expensive checks are enabled. |

Methods
-------

### `batch_shape_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L633-L650)

batch_shape_tensor(
        name='batch_shape_tensor'
    )

Shape of a single sample from a single event index as a 1-D `Tensor`.

The batch dimensions are indexes into independent, non-identical parameterizations of this distribution.

|     |     |
| --- | --- |
| Args |     |
| `name` | name to give to the op |

|     |     |
| --- | --- |
| Returns |     |
| `batch_shape` | `Tensor`. |

### `cdf`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L877-L894)

cdf(
        value, name='cdf'
    )

Cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

cdf(x) := P[X <= x]

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `cdf` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `copy`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L611-L627)

copy(
        **override_parameters_kwargs
    )

Creates a deep copy of the distribution.

|     |     |
| --- | --- |
| Args |     |
| `**override_parameters_kwargs` | String/value dictionary of initialization arguments to override with new values. |

|     |     |
| --- | --- |
| Returns |     |
| `distribution` | A new instance of `type(self)` initialized from the union of self.parameters and override\_parameters\_kwargs, i.e., `dict(self.parameters, **override_parameters_kwargs)`. |

### `covariance`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1090-L1127)

covariance(
        name='covariance'
    )

Covariance.

Covariance is (possibly) defined only for non-scalar-event distributions.

For example, for a length-`k`, vector-valued distribution, it is calculated as,

Cov[i, j] = Covariance(X_i, X_j) = E[(X_i - E[X_i]) (X_j - E[X_j])]

where `Cov` is a (batch of) `k x k` matrix, `0 <= (i, j) < k`, and `E` denotes expectation.

Alternatively, for non-vector, multivariate distributions (e.g., matrix-valued, Wishart), `Covariance` shall return a (batch of) matrices under some vectorization of the events, i.e.,

Cov[i, j] = Covariance(Vec(X)_i, Vec(X)_j) = [as above]

where `Cov` is a (batch of) `k' x k'` matrices, `0 <= (i, j) < k' = reduce_prod(event_shape)`, and `Vec` is some function mapping indices of this distribution's event dimensions to indices of a length-`k'` vector.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `covariance` | Floating-point `Tensor` with shape `[B1, ..., Bn, k', k']` where the first `n` dimensions are batch coordinates and `k' = reduce_prod(self.event_shape)`. |

### `cross_entropy`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1142-L1165)

cross_entropy(
        other, name='cross_entropy'
    )

Computes the (Shannon) cross entropy.

Denote this distribution (`self`) by `P` and the `other` distribution by `Q`. Assuming `P, Q` are absolutely continuous with respect to one another and permit densities `p(x) dr(x)` and `q(x) dr(x)`, (Shanon) cross entropy is defined as:

H[P, Q] = E_p[-log q(X)] = -int_F p(x) log q(x) dr(x)

where `F` denotes the support of the random variable `X ~ P`.

|     |     |
| --- | --- |
| Args |     |
| `other` | [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> instance. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `cross_entropy` | `self.dtype` `Tensor` with shape `[B1, ..., Bn]` representing `n` different calculations of (Shanon) cross entropy. |

### `entropy`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L978-L981)

entropy(
        name='entropy'
    )

Shannon entropy in nats.

### `event_shape_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L673-L687)

event_shape_tensor(
        name='event_shape_tensor'
    )

Shape of a single sample from a single batch as a 1-D int32 `Tensor`.

|     |     |
| --- | --- |
| Args |     |
| `name` | name to give to the op |

|     |     |
| --- | --- |
| Returns |     |
| `event_shape` | `Tensor`. |

### `is_scalar_batch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L717-L729)

is_scalar_batch(
        name='is_scalar_batch'
    )

Indicates that `batch_shape == []`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `is_scalar_batch` | `bool` scalar `Tensor`. |

### `is_scalar_event`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L703-L715)

is_scalar_event(
        name='is_scalar_event'
    )

Indicates that `event_shape == []`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `is_scalar_event` | `bool` scalar `Tensor`. |

### `kl_divergence`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1171-L1197)

kl_divergence(
        other, name='kl_divergence'
    )

Computes the Kullback--Leibler divergence.

Denote this distribution (`self`) by `p` and the `other` distribution by `q`. Assuming `p, q` are absolutely continuous with respect to reference measure `r`, the KL divergence is defined as:

KL[p, q] = E_p[log(p(X)/q(X))]
             = -int_F p(x) log q(x) dr(x) + int_F p(x) log p(x) dr(x)
             = H[p, q] - H[p]

where `F` denotes the support of the random variable `X ~ p`, `H[., .]` denotes (Shanon) cross entropy, and `H[.]` denotes (Shanon) entropy.

|     |     |
| --- | --- |
| Args |     |
| `other` | [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> instance. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `kl_divergence` | `self.dtype` `Tensor` with shape `[B1, ..., Bn]` representing `n` different calculations of the Kullback-Leibler divergence. |

### `log_cdf`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L838-L859)

log_cdf(
        value, name='log_cdf'
    )

Log cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

log_cdf(x) := Log[ P[X <= x] ]

Often, a numerical approximation can be used for `log_cdf(x)` that yields a more accurate answer than simply taking the logarithm of the `cdf` when `x << -1`.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `logcdf` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `log_prob`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L780-L791)

log_prob(
        value, name='log_prob'
    )

Log probability density/mass function.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `log_prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `log_survival_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L913-L935)

log_survival_function(
        value, name='log_survival_function'
    )

Log survival function.

Given random variable `X`, the survival function is defined:

log_survival_function(x) = Log[ P[X > x] ]
                             = Log[ 1 - P[X <= x] ]
                             = Log[ 1 - cdf(x) ]

Typically, different numerical approximations can be used for the log survival function, which are more accurate than `1 - cdf(x)` when `x >> 1`.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |
| --- |
| Returns |     |
| `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |     |

### `mean`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L987-L990)

mean(
        name='mean'
    )

Mean.

### `mode`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1133-L1136)

mode(
        name='mode'
    )

Mode.

### `param_shapes`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L493-L512)

@classmethod

Shapes of parameters given the desired shape of a call to `sample()`.

This is a class method that describes what key/value arguments are required to instantiate the given `Distribution` so that a particular shape is returned for that instance's call to `sample()`.

Subclasses should override class method `_param_shapes`.

|     |     |
| --- | --- |
| Args |     |
| `sample_shape` | `Tensor` or python list/tuple. Desired shape of a call to `sample()`. |
| `name` | name to prepend ops with. |

|     |
| --- |
| Returns |     |
| `dict` of parameter name to `Tensor` shapes. |     |

### `param_static_shapes`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L514-L551)

@classmethod

param\_shapes with static (i.e. `TensorShape`) shapes.

This is a class method that describes what key/value arguments are required to instantiate the given `Distribution` so that a particular shape is returned for that instance's call to `sample()`. Assumes that the sample's shape is known statically.

Subclasses should override class method `_param_shapes` to return constant-valued tensors when constant values are fed.

|     |     |
| --- | --- |
| Args |     |
| `sample_shape` | `TensorShape` or python list/tuple. Desired shape of a call to `sample()`. |

|     |
| --- |
| Returns |     |
| `dict` of parameter name to `TensorShape`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if `sample_shape` is a `TensorShape` and is not fully defined. |

### `prob`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L809-L820)

prob(
        value, name='prob'
    )

Probability density/mass function.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `quantile`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1002-L1019)

quantile(
        value, name='quantile'
    )

Quantile function. Aka "inverse cdf" or "percent point function".

Given random variable `X` and `p in [0, 1]`, the `quantile` is:

quantile(p) := x such that P[X <= x] == p

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `quantile` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `sample`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L748-L762)

sample(
        sample_shape=(), seed=None, name='sample'
    )

Generate samples of the specified shape.

Note that a call to `sample()` without arguments will generate a single sample.

|     |     |
| --- | --- |
| Args |     |
| `sample_shape` | 0D or 1D `int32` `Tensor`. Shape of the generated samples. |
| `seed` | Python integer seed for RNG |
| `name` | name to give to the op. |

|     |     |
| --- | --- |
| Returns |     |
| `samples` | a `Tensor` with prepended dimensions `sample_shape`. |

### `stddev`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1057-L1084)

stddev(
        name='stddev'
    )

Standard deviation.

Standard deviation is defined as,

stddev = E[(X - E[X])**2]**0.5

where `X` is the random variable associated with this distribution, `E` denotes expectation, and `stddev.shape = batch_shape + event_shape`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `stddev` | Floating-point `Tensor` with shape identical to `batch_shape + event_shape`, i.e., the same shape as `self.mean()`. |

### `survival_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L953-L972)

survival_function(
        value, name='survival_function'
    )

Survival function.

Given random variable `X`, the survival function is defined:

survival_function(x) = P[X > x]
                         = 1 - P[X <= x]
                         = 1 - cdf(x).

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |
| --- |
| Returns |     |
| `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |     |

### `variance`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/distribution.py#L1025-L1051)

variance(
        name='variance'
    )

Variance.

Variance is defined as,

Var = E[(X - E[X])**2]

where `X` is the random variable associated with this distribution, `E` denotes expectation, and `Var.shape = batch_shape + event_shape`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |

|     |     |
| --- | --- |
| Returns |     |
| `variance` | Floating-point `Tensor` with shape identical to `batch_shape + event_shape`, i.e., the same shape as `self.mean()`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.