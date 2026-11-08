[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Fdistributions%2FNoisyNormalMixture&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#methods)
    *   [batch\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#batch_shape_tensor)
        
    *   [cdf](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#cdf)
        
    *   [copy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#copy)
        
    *   [covariance](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#covariance)
        
    *   [cross\_entropy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#cross_entropy)
        
    *   [entropy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#entropy)
        
    *   [event\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#event_shape_tensor)
        
    *   [experimental\_default\_event\_space\_bijector](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_default_event_space_bijector)
        
    *   [experimental\_fit](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_fit)
        
    *   [experimental\_local\_measure](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_local_measure)
        
    *   [experimental\_sample\_and\_log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_sample_and_log_prob)
        
    *   [is\_scalar\_batch](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#is_scalar_batch)
        
    *   [is\_scalar\_event](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#is_scalar_event)
        
    *   [kl\_divergence](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#kl_divergence)
        
    *   [log\_cdf](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_cdf)
        
    *   [log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_prob)
        
    *   [log\_survival\_function](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_survival_function)
        
    *   [mean](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#mean)
        
    *   [mode](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#mode)
        
    *   [param\_shapes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#param_shapes)
        
    *   [param\_static\_shapes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#param_static_shapes)
        
    *   [parameter\_properties](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#parameter_properties)
        
    *   [posterior\_marginal](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#posterior_marginal)
        
    *   [posterior\_mode](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#posterior_mode)
        
    *   [prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#prob)
        
    *   [quantile](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#quantile)
        
    *   [sample](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#sample)
        
    *   [stddev](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#stddev)
        
    *   [survival\_function](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#survival_function)
        
    *   [unnormalized\_log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#unnormalized_log_prob)
        
    *   [variance](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#variance)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#with_name_scope)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.distributions.NoisyNormalMixture Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#methods)
    *   [batch\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#batch_shape_tensor)
        
    *   [cdf](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#cdf)
        
    *   [copy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#copy)
        
    *   [covariance](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#covariance)
        
    *   [cross\_entropy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#cross_entropy)
        
    *   [entropy](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#entropy)
        
    *   [event\_shape\_tensor](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#event_shape_tensor)
        
    *   [experimental\_default\_event\_space\_bijector](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_default_event_space_bijector)
        
    *   [experimental\_fit](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_fit)
        
    *   [experimental\_local\_measure](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_local_measure)
        
    *   [experimental\_sample\_and\_log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#experimental_sample_and_log_prob)
        
    *   [is\_scalar\_batch](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#is_scalar_batch)
        
    *   [is\_scalar\_event](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#is_scalar_event)
        
    *   [kl\_divergence](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#kl_divergence)
        
    *   [log\_cdf](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_cdf)
        
    *   [log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_prob)
        
    *   [log\_survival\_function](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#log_survival_function)
        
    *   [mean](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#mean)
        
    *   [mode](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#mode)
        
    *   [param\_shapes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#param_shapes)
        
    *   [param\_static\_shapes](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#param_static_shapes)
        
    *   [parameter\_properties](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#parameter_properties)
        
    *   [posterior\_marginal](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#posterior_marginal)
        
    *   [posterior\_mode](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#posterior_mode)
        
    *   [prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#prob)
        
    *   [quantile](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#quantile)
        
    *   [sample](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#sample)
        
    *   [stddev](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#stddev)
        
    *   [survival\_function](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#survival_function)
        
    *   [unnormalized\_log\_prob](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#unnormalized_log_prob)
        
    *   [variance](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#variance)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#with_name_scope)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture#__iter__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/distributions/uniform_noise.py#L281-L297)

Mixture of normal distributions with additive i.i.d. uniform noise.

Inherits From: [`NoisyMixtureSameFamily`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyMixtureSameFamily)

#### View aliases

**Main aliases**

[`tfc.NoisyNormalMixture`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture)

tfc.distributions.NoisyNormalMixture(
        loc, scale, weight, name='NoisyNormalMixture'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `loc` | Location parameters of `tfpd.Normal` component distributions. |
| `scale` | Scale parameters of `tfpd.Normal` component distributions. |
| `weight` | `probs` parameter of `tfpd.Categorical` mixture distribution. |
| `name` | A name for this distribution. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `allow_nan_stats` | Python `bool` describing behavior when a stat is undefined.<br><br>Stats return +/- infinity when it makes sense. E.g., the variance of a Cauchy distribution is infinity. However, sometimes the statistic is undefined, e.g., if a distribution's pdf does not achieve a maximum within the support of the distribution, the mode is undefined. If the mean is undefined, then by definition the variance is undefined. E.g. the mean for Student's T for df = 1 is undefined (no clear way to say it is either + or - infinity), so the variance = E\[(X - mean)\*\*2\] is also undefined. |
| `base` | The base distribution (without uniform noise). |
| `batch_shape` | Shape of a single sample from a single event index as a `TensorShape`.<br><br>May be partially defined or unknown.<br><br>The batch dimensions are indexes into independent, non-identical parameterizations of this distribution. |
| `components_distribution` |     |
| `dtype` | The `DType` of `Tensor`s handled by this `Distribution`. |
| `event_shape` | Shape of a single sample from a single batch as a `TensorShape`.<br><br>May be partially defined or unknown. |
| `experimental_is_sharded` |     |
| `experimental_shard_axis_names` | The list or structure of lists of active shard axis names. |
| `mixture_distribution` |     |
| `name` | Name prepended to all ops created by this `Distribution`. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `parameters` | Dictionary of parameters used to instantiate this `Distribution`. |
| `reparameterization_type` | Describes how samples from the distribution are reparameterized.<br><br>Currently this is one of the static instances `tfd.FULLY_REPARAMETERIZED` or `tfd.NOT_REPARAMETERIZED`. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `validate_args` | Python `bool` indicating possibly expensive checks are enabled. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `batch_shape_tensor`

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

cdf(
        value, name='cdf', **kwargs
    )

Cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

cdf(x) := P[X <= x]

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `cdf` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `copy`

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

covariance(
        name='covariance', **kwargs
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
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `covariance` | Floating-point `Tensor` with shape `[B1, ..., Bn, k', k']` where the first `n` dimensions are batch coordinates and `k' = reduce_prod(self.event_shape)`. |

### `cross_entropy`

cross_entropy(
        other, name='cross_entropy'
    )

Computes the (Shannon) cross entropy.

Denote this distribution (`self`) by `P` and the `other` distribution by `Q`. Assuming `P, Q` are absolutely continuous with respect to one another and permit densities `p(x) dr(x)` and `q(x) dr(x)`, (Shannon) cross entropy is defined as:

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
| `cross_entropy` | `self.dtype` `Tensor` with shape `[B1, ..., Bn]` representing `n` different calculations of (Shannon) cross entropy. |

### `entropy`

entropy(
        name='entropy', **kwargs
    )

Shannon entropy in nats.

### `event_shape_tensor`

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

### `experimental_default_event_space_bijector`

experimental_default_event_space_bijector(
        *args, **kwargs
    )

Bijector mapping the reals (R\*\*n) to the event space of the distribution.

Distributions with continuous support may implement `_default_event_space_bijector` which returns a subclass of [`tfp.bijectors.Bijector`](https://www.tensorflow.org/probability/api_docs/python/tfp/bijectors/Bijector)
 that maps R\*\*n to the distribution's event space. For example, the default bijector for the `Beta` distribution is [`tfp.bijectors.Sigmoid()`](https://www.tensorflow.org/probability/api_docs/python/tfp/bijectors/Sigmoid)
, which maps the real line to `[0, 1]`, the support of the `Beta` distribution. The default bijector for the `CholeskyLKJ` distribution is [`tfp.bijectors.CorrelationCholesky`](https://www.tensorflow.org/probability/api_docs/python/tfp/bijectors/CorrelationCholesky)
, which maps R^(k \* (k-1) // 2) to the submanifold of k x k lower triangular matrices with ones along the diagonal.

The purpose of `experimental_default_event_space_bijector` is to enable gradient descent in an unconstrained space for Variational Inference and Hamiltonian Monte Carlo methods. Some effort has been made to choose bijectors such that the tails of the distribution in the unconstrained space are between Gaussian and Exponential.

For distributions with discrete event space, or for which TFP currently lacks a suitable bijector, this function returns `None`.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Passed to implementation `_default_event_space_bijector`. |
| `**kwargs` | Passed to implementation `_default_event_space_bijector`. |

|     |     |
| --- | --- |
| Returns |     |
| `event_space_bijector` | `Bijector` instance or `None`. |

### `experimental_fit`

@classmethod

Instantiates a distribution that maximizes the likelihood of `x`.

|     |     |
| --- | --- |
| Args |     |
| `value` | a `Tensor` valid sample from this distribution family. |
| `sample_ndims` | Positive `int` Tensor number of leftmost dimensions of `value` that index i.i.d. samples. Default value: `1`. |
| `validate_args` | Python `bool`, default `False`. When `True`, distribution parameters are checked for validity despite possibly degrading runtime performance. When `False`, invalid inputs may silently render incorrect outputs. Default value: `False`. |
| `**init_kwargs` | Additional keyword arguments passed through to `cls.__init__`. These take precedence in case of collision with the fitted parameters; for example, `tfd.Normal.experimental_fit([1., 1.], scale=20.)` returns a Normal distribution with `scale=20.` rather than the maximum likelihood parameter `scale=0.`. |

|     |     |
| --- | --- |
| Returns |     |
| `maximum_likelihood_instance` | instance of `cls` with parameters that maximize the likelihood of `value`. |

### `experimental_local_measure`

experimental_local_measure(
        value, backward_compat=False, **kwargs
    )

Returns a log probability density together with a `TangentSpace`.

A `TangentSpace` allows us to calculate the correct push-forward density when we apply a transformation to a `Distribution` on a strict submanifold of R^n (typically via a `Bijector` in the `TransformedDistribution` subclass). The density correction uses the basis of the tangent space.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `backward_compat` | `bool` specifying whether to fall back to returning `FullSpace` as the tangent space, and representing R^n with the standard basis. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `log_prob` | a `Tensor` representing the log probability density, of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |
| `tangent_space` | a `TangentSpace` object (by default `FullSpace`) representing the tangent space to the manifold at `value`. |

|     |
| --- |
| Raises |     |
| UnspecifiedTangentSpaceError if `backward_compat` is False and the `_experimental_tangent_space` attribute has not been defined. |     |

### `experimental_sample_and_log_prob`

experimental_sample_and_log_prob(
        sample_shape=(), seed=None, name='sample_and_log_prob', **kwargs
    )

Samples from this distribution and returns the log density of the sample.

The default implementation simply calls `sample` and `log_prob`:

def _sample_and_log_prob(self, sample_shape, seed, **kwargs):
      x = self.sample(sample_shape=sample_shape, seed=seed, **kwargs)
      return x, self.log_prob(x, **kwargs)

However, some subclasses may provide more efficient and/or numerically stable implementations.

|     |     |
| --- | --- |
| Args |     |
| `sample_shape` | integer `Tensor` desired shape of samples to draw. Default value: `()`. |
| `seed` | PRNG seed; see [`tfp.random.sanitize_seed`](https://www.tensorflow.org/probability/api_docs/python/tfp/random/sanitize_seed)<br> for details. Default value: `None`. |
| `name` | name to give to the op. Default value: `'sample_and_log_prob'`. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `samples` | a `Tensor`, or structure of `Tensor`s, with prepended dimensions `sample_shape`. |
| `log_prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `is_scalar_batch`

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

kl_divergence(
        other, name='kl_divergence'
    )

Computes the Kullback--Leibler divergence.

Denote this distribution (`self`) by `p` and the `other` distribution by `q`. Assuming `p, q` are absolutely continuous with respect to reference measure `r`, the KL divergence is defined as:

KL[p, q] = E_p[log(p(X)/q(X))]
             = -int_F p(x) log q(x) dr(x) + int_F p(x) log p(x) dr(x)
             = H[p, q] - H[p]

where `F` denotes the support of the random variable `X ~ p`, `H[., .]` denotes (Shannon) cross entropy, and `H[.]` denotes (Shannon) entropy.

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

log_cdf(
        value, name='log_cdf', **kwargs
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
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `logcdf` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `log_prob`

log_prob(
        value, name='log_prob', **kwargs
    )

Log probability density/mass function.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `log_prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `log_survival_function`

log_survival_function(
        value, name='log_survival_function', **kwargs
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
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |
| --- |
| Returns |     |
| `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |     |

### `mean`

mean(
        name='mean', **kwargs
    )

Mean.

### `mode`

mode(
        name='mode', **kwargs
    )

Mode.

### `param_shapes`

@classmethod

Shapes of parameters given the desired shape of a call to `sample()`. (deprecated)

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

@classmethod

param\_shapes with static (i.e. `TensorShape`) shapes. (deprecated)

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

### `parameter_properties`

@classmethod

Returns a dict mapping constructor arg names to property annotations.

This dict should include an entry for each of the distribution's `Tensor`\-valued constructor arguments.

Distribution subclasses are not required to implement `_parameter_properties`, so this method may raise `NotImplementedError`. Providing a `_parameter_properties` implementation enables several advanced features, including:

*   Distribution batch slicing (`sliced_distribution = distribution[i:j]`).
*   Automatic inference of `_batch_shape` and `_batch_shape_tensor`, which must otherwise be computed explicitly.
*   Automatic instantiation of the distribution within TFP's internal property tests.
*   Automatic construction of 'trainable' instances of the distribution using appropriate bijectors to avoid violating parameter constraints. This enables the distribution family to be used easily as a surrogate posterior in variational inference.

In the future, parameter property annotations may enable additional functionality; for example, returning Distribution instances from [`tf.vectorized_map`](https://www.tensorflow.org/api_docs/python/tf/vectorized_map)
.

|     |     |
| --- | --- |
| Args |     |
| `dtype` | Optional float `dtype` to assume for continuous-valued parameters. Some constraining bijectors require advance knowledge of the dtype because certain constants (e.g., `tfb.Softplus.low`) must be instantiated with the same dtype as the values to be transformed. |
| `num_classes` | Optional `int` `Tensor` number of classes to assume when inferring the shape of parameters for categorical-like distributions. Otherwise ignored. |

|     |     |
| --- | --- |
| Returns |     |
| `parameter_properties` | A `str ->`tfp.python.internal.parameter\_properties.ParameterProperties`dict mapping constructor argument names to`ParameterProperties\` instances. |

|     |     |
| --- | --- |
| Raises |     |
| `NotImplementedError` | if the distribution class does not implement `_parameter_properties`. |

### `posterior_marginal`

posterior_marginal(
        observations, name='posterior_marginals'
    )

Compute the marginal posterior distribution for a batch of observations.

|     |     |
| --- | --- |
| Args |     |
| `observations` | A tensor representing observations from the mixture. Must be broadcastable with the mixture's batch shape. |
| `name` | A string naming a scope. |

|     |     |
| --- | --- |
| Returns |     |
| `posterior_marginals` | A `Categorical` distribution object representing the marginal probability of the components of the mixture. The batch shape of the `Categorical` will be the broadcast shape of `observations` and the mixture batch shape; the number of classes will equal the number of mixture components. |

### `posterior_mode`

posterior_mode(
        observations, name='posterior_mode'
    )

Compute the posterior mode for a batch of distributions.

|     |     |
| --- | --- |
| Args |     |
| `observations` | A tensor representing observations from the mixture. Must be broadcastable with the mixture's batch shape. |
| `name` | A string naming a scope. |

|     |
| --- |
| Returns |     |
| A Tensor representing the mode (most likely component) for each observation. The shape will be equal to the broadcast shape of the observations and the batch shape. |     |

### `prob`

prob(
        value, name='prob', **kwargs
    )

Probability density/mass function.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `quantile`

quantile(
        value, name='quantile', **kwargs
    )

Quantile function. Aka 'inverse cdf' or 'percent point function'.

Given random variable `X` and `p in [0, 1]`, the `quantile` is:

quantile(p) := x such that P[X <= x] == p

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `quantile` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `sample`

sample(
        sample_shape=(), seed=None, name='sample', **kwargs
    )

Generate samples of the specified shape.

Note that a call to `sample()` without arguments will generate a single sample.

|     |     |
| --- | --- |
| Args |     |
| `sample_shape` | 0D or 1D `int32` `Tensor`. Shape of the generated samples. |
| `seed` | PRNG seed; see [`tfp.random.sanitize_seed`](https://www.tensorflow.org/probability/api_docs/python/tfp/random/sanitize_seed)<br> for details. |
| `name` | name to give to the op. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `samples` | a `Tensor` with prepended dimensions `sample_shape`. |

### `stddev`

stddev(
        name='stddev', **kwargs
    )

Standard deviation.

Standard deviation is defined as,

stddev = E[(X - E[X])**2]**0.5

where `X` is the random variable associated with this distribution, `E` denotes expectation, and `stddev.shape = batch_shape + event_shape`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `stddev` | Floating-point `Tensor` with shape identical to `batch_shape + event_shape`, i.e., the same shape as `self.mean()`. |

### `survival_function`

survival_function(
        value, name='survival_function', **kwargs
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
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |
| --- |
| Returns |     |
| `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |     |

### `unnormalized_log_prob`

unnormalized_log_prob(
        value, name='unnormalized_log_prob', **kwargs
    )

Potentially unnormalized log probability density/mass function.

This function is similar to `log_prob`, but does not require that the return value be normalized. (Normalization here refers to the total integral of probability being one, as it should be by definition for any probability distribution.) This is useful, for example, for distributions where the normalization constant is difficult or expensive to compute. By default, this simply calls `log_prob`.

|     |     |
| --- | --- |
| Args |     |
| `value` | `float` or `double` `Tensor`. |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `unnormalized_log_prob` | a `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type `self.dtype`. |

### `variance`

variance(
        name='variance', **kwargs
    )

Variance.

Variance is defined as,

Var = E[(X - E[X])**2]

where `X` is the random variable associated with this distribution, `E` denotes expectation, and `Var.shape = batch_shape + event_shape`.

|     |     |
| --- | --- |
| Args |     |
| `name` | Python `str` prepended to names of ops created by this function. |
| `**kwargs` | Named arguments forwarded to subclass implementation. |

|     |     |
| --- | --- |
| Returns |     |
| `variance` | Floating-point `Tensor` with shape identical to `batch_shape + event_shape`, i.e., the same shape as `self.mean()`. |

### `with_name_scope`

@classmethod

Decorator to automatically enter the module name scope.

    class MyModule(tf.Module):

Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s whose names included the module name:

    mod = MyModule()

|     |     |
| --- | --- |
| Args |     |
| `method` | The method to wrap. |

|     |
| --- |
| Returns |     |
| The original method wrapped such that it enters the module's name scope. |     |

### `__getitem__`

__getitem__(
        slices
    )

Slices the batch axes of this distribution, returning a new instance.

b = tfd.Bernoulli(logits=tf.zeros([3, 5, 7, 9]))
    b.batch_shape  # => [3, 5, 7, 9]
    b2 = b[:, tf.newaxis, ..., -2:, 1::2]
    b2.batch_shape  # => [3, 1, 5, 2, 4]
    
    x = tf.random.normal([5, 3, 2, 2])
    cov = tf.matmul(x, x, transpose_b=True)
    chol = tf.linalg.cholesky(cov)
    loc = tf.random.normal([4, 1, 3, 1])
    mvn = tfd.MultivariateNormalTriL(loc, chol)
    mvn.batch_shape  # => [4, 5, 3]
    mvn.event_shape  # => [2]
    mvn2 = mvn[:, 3:, ..., ::-1, tf.newaxis]
    mvn2.batch_shape  # => [4, 2, 3, 1]
    mvn2.event_shape  # => [2]

|     |     |
| --- | --- |
| Args |     |
| `slices` | slices from the \[\] operator |

|     |     |
| --- | --- |
| Returns |     |
| `dist` | A new `tfd.Distribution` instance with sliced parameters. |

### `__iter__`

__iter__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.