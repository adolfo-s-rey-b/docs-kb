Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributions.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributions.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributions.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributions.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributions.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributions.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributions.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributions.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributions.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributions.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributions.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributions.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributions.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributions.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributions.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributions.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributions.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributions.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributions.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributions.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributions.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributions.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributions.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributions.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributions.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributions.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributions.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributions.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributions.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributions.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributions.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributions.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributions.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributions.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributions.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributions.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributions.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributions.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributions.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributions.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributions.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributions.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributions.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributions.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

Probability distributions - torch.distributions[#](https://docs.pytorch.org/docs/2.15/distributions.html#module-torch.distributions "Link to this heading")

============================================================================================================================================================

Created On: Oct 19, 2017 | Last Updated On: Apr 24, 2026

The `distributions` package contains parameterizable probability distributions and sampling functions. This allows the construction of stochastic computation graphs and stochastic gradient estimators for optimization. This package generally follows the design of the [TensorFlow Distributions](https://docs.pytorch.org/docs/2.15/distributions.html#tensorflow-distributions)
 package.

It is not possible to directly backpropagate through random samples. However, there are two main methods for creating surrogate functions that can be backpropagated through. These are the score function estimator/likelihood ratio estimator/REINFORCE and the pathwise derivative estimator. REINFORCE is commonly seen as the basis for policy gradient methods in reinforcement learning, and the pathwise derivative estimator is commonly seen in the reparameterization trick in variational autoencoders. Whilst the score function only requires the value of samples f(x)f(x)f(x), the pathwise derivative requires the derivative f′(x)f'(x)f′(x). The next sections discuss these two in a reinforcement learning example. For more details see [Gradient Estimation Using Stochastic Computation Graphs](https://docs.pytorch.org/docs/2.15/distributions.html#gradient-estimation-using-stochastic-computation-graphs)
 .

Score function[#](https://docs.pytorch.org/docs/2.15/distributions.html#score-function "Link to this heading")

---------------------------------------------------------------------------------------------------------------

When the probability density function is differentiable with respect to its parameters, we only need `sample()` and `log_prob()` to implement REINFORCE:

Δθ\=αr∇θlog⁡πθ(a∣s)\\Delta\\theta = \\alpha r \\nabla\_\\theta \\log \\pi\_\\theta(a \\mid s)Δθ\=αr∇θ​logπθ​(a∣s)

where θ\\thetaθ are the parameters, α\\alphaα is the learning rate, rrr is the reward and πθ(a∣s)\\pi\_\\theta(a \\mid s)πθ​(a∣s) is the probability of taking action aaa in state sss given policy πθ\\pi\_\\thetaπθ​.

In practice we would sample an action from the output of a network, apply this action in an environment, and then use `log_prob` to construct an equivalent loss function. Note that we use a negative because optimizers use gradient descent, whilst the rule above assumes gradient ascent. With a categorical policy, the code for implementing REINFORCE would be as follows:

probs \= policy\_network(state)
\# Note that this is equivalent to what used to be called multinomial
m \= Categorical(probs)
action \= m.sample()
next\_state, reward \= env.step(action)
loss \= \-m.log\_prob(action) \* reward
loss.backward()

Copy to clipboard

Pathwise derivative[#](https://docs.pytorch.org/docs/2.15/distributions.html#pathwise-derivative "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

The other way to implement these stochastic/policy gradients would be to use the reparameterization trick from the `rsample()` method, where the parameterized random variable can be constructed via a parameterized deterministic function of a parameter-free random variable. The reparameterized sample therefore becomes differentiable. The code for implementing the pathwise derivative would be as follows:

params \= policy\_network(state)
m \= Normal(\*params)
\# Any distribution with .has\_rsample == True could work based on the application
action \= m.rsample()
next\_state, reward \= env.step(action)  \# Assuming that reward is differentiable
loss \= \-reward
loss.backward()

Copy to clipboard

Distribution[#](https://docs.pytorch.org/docs/2.15/distributions.html#distribution "Link to this heading")

-----------------------------------------------------------------------------------------------------------

_class_ torch.distributions.distribution.Distribution(_batch\_shape\=()_, _event\_shape\=()_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L22)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "Link to this definition")

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")

Distribution is the abstract base class for probability distributions.

Parameters:

*   **batch\_shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
    ) – The shape over which parameters are batched.
    
*   **event\_shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
    ) – The shape of a single sample (without batching).
    
*   **validate\_args** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to validate arguments. Default: None.
    

_property_ arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.arg_constraints "Link to this definition")

Returns a dictionary from argument names to [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")
 objects that should be satisfied by each argument of this distribution. Args that are not tensors need not appear in this dict.

_property_ batch\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.batch_shape "Link to this definition")

Returns the shape over which parameters are batched.

cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L214)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.cdf "Link to this definition")

Returns the cumulative density/mass function evaluated at value.

Parameters:

**value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) –

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L258)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.entropy "Link to this definition")

Returns entropy of distribution, batched over batch\_shape.

Returns:

Tensor of shape batch\_shape.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L234)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.enumerate_support "Link to this definition")

Returns tensor containing all values supported by a discrete distribution. The result will enumerate over dimension 0, so the shape of the result will be (cardinality,) + batch\_shape + event\_shape (where event\_shape = () for univariate distributions).

Note that this enumerates over all batched tensors in lock-step \[\[0, 0\], \[1, 1\], …\]. With expand=False, enumeration happens along dim 0, but with the remaining batch dimensions being singleton dimensions, \[\[0\], \[1\], ...\
\
To iterate over the full Cartesian product use itertools.product(m.enumerate\_support()).\
\
Parameters:\
\
**expand** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
) – whether to expand the support over the batch dims to match the distribution’s batch\_shape.\
\
Returns:\
\
Tensor iterating over dimension 0.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_property_ event\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.event_shape "Link to this definition")\
\
Returns the shape of a single sample (without batching).\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L96)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.expand "Link to this definition")\
\
Returns a new distribution instance (or populates an existing instance provided by a derived class) with batch dimensions expanded to batch\_shape. This method calls [`expand`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand.html#torch.Tensor.expand "torch.Tensor.expand")\
 on the distribution’s parameters. As such, this does not allocate new memory for the expanded distribution instance. Additionally, this does not repeat any args checking or parameter broadcasting in \_\_init\_\_.py, when an instance is first created.\
\
Parameters:\
\
*   **batch\_shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
    ) – the desired expanded size.\
    \
*   **\_instance** – new instance provided by subclasses that need to override .expand.\
    \
\
Returns:\
\
New distribution instance with batch dimensions expanded to batch\_shape.\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L224)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.icdf "Link to this definition")\
\
Returns the inverse cumulative density/mass function evaluated at value.\
\
Parameters:\
\
**value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) –\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L204)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.log_prob "Link to this definition")\
\
Returns the log of the probability density/mass function evaluated at value.\
\
Parameters:\
\
**value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) –\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.mean "Link to this definition")\
\
Returns the mean of the distribution.\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.mode "Link to this definition")\
\
Returns the mode of the distribution.\
\
perplexity()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L267)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.perplexity "Link to this definition")\
\
Returns perplexity of distribution, batched over batch\_shape.\
\
Returns:\
\
Tensor of shape batch\_shape.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L185)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.rsample "Link to this definition")\
\
Generates a sample\_shape shaped reparameterized sample or sample\_shape shaped batch of reparameterized samples if the distribution parameters are batched.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L177)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.sample "Link to this definition")\
\
Generates a sample\_shape shaped sample or sample\_shape shaped batch of samples if the distribution parameters are batched.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample\_n(_n_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L193)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.sample_n "Link to this definition")\
\
Generates n samples or n batches of samples if the distribution parameters are batched.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_static_ set\_default\_validate\_args(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/distribution.py#L36)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.set_default_validate_args "Link to this definition")\
\
Sets whether validation is enabled or disabled.\
\
The default behavior mimics Python’s `assert` statement: validation is on by default, but is disabled if Python is run in optimized mode (via `python -O`). Validation may be expensive, so you may want to disable it once a model is working.\
\
Parameters:\
\
**value** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
) – Whether to enable validation.\
\
_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.stddev "Link to this definition")\
\
Returns the standard deviation of the distribution.\
\
_property_ support_: [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.support "Link to this definition")\
\
Returns a [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
 object representing this distribution’s support.\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution.variance "Link to this definition")\
\
Returns the variance of the distribution.\
\
ExponentialFamily[#](https://docs.pytorch.org/docs/2.15/distributions.html#exponentialfamily "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.exp\_family.ExponentialFamily(_batch\_shape\=()_, _event\_shape\=()_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exp_family.py#L11)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
ExponentialFamily is the abstract base class for probability distributions belonging to an exponential family, whose probability mass/density function is defined below\
\
pF(x;θ)\=exp⁡(⟨t(x),θ⟩−F(θ)+k(x))p\_{F}(x; \\theta) = \\exp(\\langle t(x), \\theta\\rangle - F(\\theta) + k(x))pF​(x;θ)\=exp(⟨t(x),θ⟩−F(θ)+k(x))\
\
where θ\\thetaθ denotes the natural parameters, t(x)t(x)t(x) denotes the sufficient statistic, F(θ)F(\\theta)F(θ) is the log normalizer function for a given family and k(x)k(x)k(x) is the carrier measure.\
\
Note\
\
This class is an intermediary between the Distribution class and distributions which belong to an exponential family mainly to check the correctness of the .entropy() and analytic KL divergence methods. We use this class to compute the entropy and KL divergence using the AD framework and Bregman divergences (courtesy of: Frank Nielsen and Richard Nock, Entropies and Cross-entropies of Exponential Families).\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exp_family.py#L55)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily.entropy "Link to this definition")\
\
Method to compute the entropy using Bregman divergence of the log normalizer.\
\
Bernoulli[#](https://docs.pytorch.org/docs/2.15/distributions.html#bernoulli "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.bernoulli.Bernoulli(_probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L20)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a Bernoulli distribution parameterized by [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.probs "torch.distributions.bernoulli.Bernoulli.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.logits "torch.distributions.bernoulli.Bernoulli.logits")\
 (but not both).\
\
Samples are binary (0 or 1). They take the value 1 with probability p and 0 with probability 1 - p.\
\
Example:\
\
\>>> m \= Bernoulli(torch.tensor(\[0.3\]))\
\>>> m.sample()  \# 30% chance 1; 70% chance 0\
tensor(\[ 0.\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **probs** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the probability of sampling 1\
    \
*   **logits** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the log-odds of sampling 1\
    \
*   **validate\_args** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – whether to validate arguments, None by default\
    \
\
arg\_constraints _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L127)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.entropy "Link to this definition")\
\
enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L132)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.enumerate_support "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L74)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.expand "Link to this definition")\
\
has\_enumerate\_support _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.has_enumerate_support "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L121)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.mode "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.probs "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/bernoulli.py#L116)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.sample "Link to this definition")\
\
support _\= Boolean()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.bernoulli.Bernoulli.variance "Link to this definition")\
\
Beta[#](https://docs.pytorch.org/docs/2.15/distributions.html#beta "Link to this heading")\
\
-------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.beta.Beta(_concentration1_, _concentration0_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/beta.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Beta distribution parameterized by [`concentration1`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.concentration1 "torch.distributions.beta.Beta.concentration1")\
 and [`concentration0`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.concentration0 "torch.distributions.beta.Beta.concentration0")\
.\
\
Example:\
\
\>>> m \= Beta(torch.tensor(\[0.5\]), torch.tensor(\[0.5\]))\
\>>> m.sample()  \# Beta distributed with concentration concentration1 and concentration0\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **concentration1** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – 1st concentration parameter of the distribution (often referred to as alpha)\
    \
*   **concentration0** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – 2nd concentration parameter of the distribution (often referred to as beta)\
    \
\
arg\_constraints _\= {'concentration0': GreaterThan(lower\_bound=0.0), 'concentration1': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.arg_constraints "Link to this definition")\
\
_property_ concentration0_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.concentration0 "Link to this definition")\
\
_property_ concentration1_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.concentration1 "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/beta.py#L93)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/beta.py#L63)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/beta.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/beta.py#L84)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= Interval(lower\_bound=0.0, upper\_bound=1.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.beta.Beta.variance "Link to this definition")\
\
Binomial[#](https://docs.pytorch.org/docs/2.15/distributions.html#binomial "Link to this heading")\
\
---------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.binomial.Binomial(_total\_count\=1_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L23)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a Binomial distribution parameterized by `total_count` and either [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.probs "torch.distributions.binomial.Binomial.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.logits "torch.distributions.binomial.Binomial.logits")\
 (but not both). `total_count` must be broadcastable with [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.probs "torch.distributions.binomial.Binomial.probs")\
/[`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.logits "torch.distributions.binomial.Binomial.logits")\
.\
\
Example:\
\
\>>> m \= Binomial(100, torch.tensor(\[0 , .2, .8, 1\]))\
\>>> x \= m.sample()\
tensor(\[   0.,   22.,   71.,  100.\])\
\
\>>> m \= Binomial(torch.tensor(\[\[5.\], \[10.\]\]), torch.tensor(\[0.5, 0.8\]))\
\>>> x \= m.sample()\
tensor(\[\[ 4.,  5.\],\
        \[ 7.,  6.\]\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **total\_count** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – number of Bernoulli trials\
    \
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Event probabilities\
    \
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Event log-odds\
    \
\
arg\_constraints _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0), 'total\_count': IntegerGreaterThan(lower\_bound=0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L160)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.entropy "Link to this definition")\
\
enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L170)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.enumerate_support "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.expand "Link to this definition")\
\
has\_enumerate\_support _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.has_enumerate_support "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L140)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.mode "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.probs "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/binomial.py#L133)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.sample "Link to this definition")\
\
_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.binomial.Binomial.variance "Link to this definition")\
\
Categorical[#](https://docs.pytorch.org/docs/2.15/distributions.html#categorical "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.categorical.Categorical(_probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L13)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a categorical distribution parameterized by either [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.probs "torch.distributions.categorical.Categorical.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.logits "torch.distributions.categorical.Categorical.logits")\
 (but not both).\
\
Note\
\
It is equivalent to the distribution that [`torch.multinomial()`](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#torch.multinomial "torch.multinomial")\
 samples from.\
\
Samples are integers from {0,…,K−1}\\{0, \\ldots, K-1\\}{0,…,K−1} where K is `probs.size(-1)`.\
\
If probs is 1-dimensional with length-K, each element is the relative probability of sampling the class at that index.\
\
If probs is N-dimensional, the first N-1 dimensions are treated as a batch of relative probability vectors.\
\
Note\
\
The probs argument must be non-negative, finite and have a non-zero sum, and it will be normalized to sum to 1 along the last dimension. [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.probs "torch.distributions.categorical.Categorical.probs")\
 will return this normalized value. The logits argument will be interpreted as unnormalized log probabilities and can therefore be any real number. It will likewise be normalized so that the resulting probabilities sum to 1 along the last dimension. [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.logits "torch.distributions.categorical.Categorical.logits")\
 will return this normalized value.\
\
See also: [`torch.multinomial()`](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#torch.multinomial "torch.multinomial")\
\
Example:\
\
\>>> m \= Categorical(torch.tensor(\[ 0.25, 0.25, 0.25, 0.25 \]))\
\>>> m.sample()  \# equal probability of 0, 1, 2, 3\
tensor(3)\
\
Copy to clipboard\
\
Parameters:\
\
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – event probabilities\
    \
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – event log probabilities (unnormalized)\
    \
\
arg\_constraints _\= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L159)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.entropy "Link to this definition")\
\
enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L165)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.enumerate_support "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.expand "Link to this definition")\
\
has\_enumerate\_support _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.has_enumerate_support "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L151)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.mode "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.probs "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/categorical.py#L144)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.sample "Link to this definition")\
\
_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical.variance "Link to this definition")\
\
Cauchy[#](https://docs.pytorch.org/docs/2.15/distributions.html#cauchy "Link to this heading")\
\
-----------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.cauchy.Cauchy(_loc_, _scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Samples from a Cauchy (Lorentz) distribution. The distribution of the ratio of independent normally distributed random variables with means 0 follows a Cauchy distribution.\
\
Example:\
\
\>>> m \= Cauchy(torch.tensor(\[0.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# sample from a Cauchy distribution with loc=0 and scale=1\
tensor(\[ 2.3214\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – mode or median of the distribution.\
    \
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – half width at half maximum.\
    \
\
arg\_constraints _\= {'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L90)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L98)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L51)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L95)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.icdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L81)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/cauchy.py#L76)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy.variance "Link to this definition")\
\
Chi2[#](https://docs.pytorch.org/docs/2.15/distributions.html#chi2 "Link to this heading")\
\
-------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.chi2.Chi2(_df_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/chi2.py#L11)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.chi2.Chi2 "Link to this definition")\
\
Bases: [`Gamma`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma "torch.distributions.gamma.Gamma")\
\
Creates a Chi-squared distribution parameterized by shape parameter [`df`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.chi2.Chi2.df "torch.distributions.chi2.Chi2.df")\
. This is exactly equivalent to `Gamma(alpha=0.5*df, beta=0.5)`\
\
Example:\
\
\>>> m \= Chi2(torch.tensor(\[1.0\]))\
\>>> m.sample()  \# Chi2 distributed with shape df=1\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
**df** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) – shape parameter of the distribution\
\
arg\_constraints _\= {'df': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.chi2.Chi2.arg_constraints "Link to this definition")\
\
_property_ df_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.chi2.Chi2.df "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/chi2.py#L36)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.chi2.Chi2.expand "Link to this definition")\
\
ContinuousBernoulli[#](https://docs.pytorch.org/docs/2.15/distributions.html#continuousbernoulli "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.continuous\_bernoulli.ContinuousBernoulli(_probs\=None_, _logits\=None_, _lims\=(0.499, 0.501)_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L22)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a continuous Bernoulli distribution parameterized by [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.probs "torch.distributions.continuous_bernoulli.ContinuousBernoulli.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.logits "torch.distributions.continuous_bernoulli.ContinuousBernoulli.logits")\
 (but not both).\
\
The distribution is supported in \[0, 1\] and parameterized by ‘probs’ (in (0,1)) or ‘logits’ (real-valued). Note that, unlike the Bernoulli, ‘probs’ does not correspond to a probability and ‘logits’ does not correspond to log-odds, but the same names are used due to the similarity with the Bernoulli. See \[1\] for more details.\
\
Example:\
\
\>>> m \= ContinuousBernoulli(torch.tensor(\[0.3\]))\
\>>> m.sample()\
tensor(\[ 0.2538\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **probs** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – (0,1) valued parameters\
    \
*   **logits** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – real valued parameters whose sigmoid matches ‘probs’\
    \
\
\[1\] The continuous Bernoulli: fixing a pervasive error in variational autoencoders, Loaiza-Ganem G and Cunningham JP, NeurIPS 2019. [https://arxiv.org/abs/1907.06845](https://arxiv.org/abs/1907.06845)\
\
arg\_constraints _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L196)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L224)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L91)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L212)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.icdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L187)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.mean "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.probs "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L182)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/continuous_bernoulli.py#L176)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.sample "Link to this definition")\
\
_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.stddev "Link to this definition")\
\
support _\= Interval(lower\_bound=0.0, upper\_bound=1.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.continuous_bernoulli.ContinuousBernoulli.variance "Link to this definition")\
\
Dirichlet[#](https://docs.pytorch.org/docs/2.15/distributions.html#dirichlet "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.dirichlet.Dirichlet(_concentration_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/dirichlet.py#L38)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a Dirichlet distribution parameterized by concentration `concentration`.\
\
Example:\
\
\>>> m \= Dirichlet(torch.tensor(\[0.5, 0.5\]))\
\>>> m.sample()  \# Dirichlet distributed with concentration \[0.5, 0.5\]\
tensor(\[ 0.1046,  0.8954\])\
\
Copy to clipboard\
\
Parameters:\
\
**concentration** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) – concentration parameter of the distribution (often referred to as alpha)\
\
arg\_constraints _\= {'concentration': IndependentConstraint(GreaterThan(lower\_bound=0.0), 1)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/dirichlet.py#L122)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/dirichlet.py#L75)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/dirichlet.py#L90)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/dirichlet.py#L85)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= Simplex()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.dirichlet.Dirichlet.variance "Link to this definition")\
\
Exponential[#](https://docs.pytorch.org/docs/2.15/distributions.html#exponential "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.exponential.Exponential(_rate_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L14)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates an Exponential distribution parameterized by `rate`.\
\
Example:\
\
\>>> m \= Exponential(torch.tensor(\[1.0\]))\
\>>> m.sample()  \# Exponential distributed with rate=1\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
**rate** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) – rate = 1 / scale of the distribution\
\
arg\_constraints _\= {'rate': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L77)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L85)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L60)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L82)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.icdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L72)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/exponential.py#L68)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.stddev "Link to this definition")\
\
support _\= GreaterThanEq(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exponential.Exponential.variance "Link to this definition")\
\
FisherSnedecor[#](https://docs.pytorch.org/docs/2.15/distributions.html#fishersnedecor "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.fishersnedecor.FisherSnedecor(_df1_, _df2_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/fishersnedecor.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a Fisher-Snedecor distribution parameterized by `df1` and `df2`.\
\
Example:\
\
\>>> m \= FisherSnedecor(torch.tensor(\[1.0\]), torch.tensor(\[2.0\]))\
\>>> m.sample()  \# Fisher-Snedecor-distributed with df1=1 and df2=2\
tensor(\[ 0.2453\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **df1** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – degrees of freedom parameter 1\
    \
*   **df2** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – degrees of freedom parameter 2\
    \
\
arg\_constraints _\= {'df1': GreaterThan(lower\_bound=0.0), 'df2': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.arg_constraints "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/fishersnedecor.py#L52)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/fishersnedecor.py#L98)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/fishersnedecor.py#L86)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= GreaterThan(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.fishersnedecor.FisherSnedecor.variance "Link to this definition")\
\
Gamma[#](https://docs.pytorch.org/docs/2.15/distributions.html#gamma "Link to this heading")\
\
---------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.gamma.Gamma(_concentration_, _rate_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L18)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a Gamma distribution parameterized by shape `concentration` and `rate`.\
\
Example:\
\
\>>> m \= Gamma(torch.tensor(\[1.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# Gamma distributed with concentration=1 and rate=1\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **concentration** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – shape parameter of the distribution (often referred to as alpha)\
    \
*   **rate** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – rate parameter of the distribution (often referred to as beta), rate = 1 / scale\
    \
\
arg\_constraints _\= {'concentration': GreaterThan(lower\_bound=0.0), 'rate': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L129)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L113)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L70)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L102)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L88)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample(_sample\_shape\=()_, _\*_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gamma.py#L79)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.sample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= GreaterThanEq(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma.variance "Link to this definition")\
\
GeneralizedPareto[#](https://docs.pytorch.org/docs/2.15/distributions.html#generalizedpareto "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.generalized\_pareto.GeneralizedPareto(_loc_, _scale_, _concentration_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L14)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a Generalized Pareto distribution parameterized by `loc`, `scale`, and `concentration`.\
\
The Generalized Pareto distribution is a family of continuous probability distributions on the real line. Special cases include Exponential (when `loc` = 0, `concentration` = 0), Pareto (when `concentration` > 0, `loc` = `scale` / `concentration`), and Uniform (when `concentration` = -1).\
\
This distribution is often used to model the tails of other distributions. This implementation is based on the implementation in TensorFlow Probability.\
\
Example:\
\
\>>> m \= GeneralizedPareto(torch.tensor(\[0.1\]), torch.tensor(\[2.0\]), torch.tensor(\[0.4\]))\
\>>> m.sample()  \# sample from a Generalized Pareto distribution with loc=0.1, scale=2.0, and concentration=0.4\
tensor(\[ 1.5623\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Location parameter of the distribution\
    \
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Scale parameter of the distribution\
    \
*   **concentration** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Concentration parameter of the distribution\
    \
\
arg\_constraints _\= {'concentration': Real(), 'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L104)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L137)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L60)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L107)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.icdf "Link to this definition")\
\
log\_cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L101)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.log_cdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L75)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.log_prob "Link to this definition")\
\
log\_survival\_function(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L90)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.log_survival_function "Link to this definition")\
\
_property_ mean[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.mean "Link to this definition")\
\
_property_ mode[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/generalized_pareto.py#L70)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.rsample "Link to this definition")\
\
_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
_property_ variance[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.generalized_pareto.GeneralizedPareto.variance "Link to this definition")\
\
Geometric[#](https://docs.pytorch.org/docs/2.15/distributions.html#geometric "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.geometric.Geometric(_probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/geometric.py#L20)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a Geometric distribution parameterized by [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.probs "torch.distributions.geometric.Geometric.probs")\
, where [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.probs "torch.distributions.geometric.Geometric.probs")\
 is the probability of success of Bernoulli trials.\
\
P(X\=k)\=(1−p)kp,k\=0,1,...P(X=k) = (1-p)^{k} p, k = 0, 1, ...P(X\=k)\=(1−p)kp,k\=0,1,...\
\
Note\
\
[`torch.distributions.geometric.Geometric()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric "torch.distributions.geometric.Geometric")\
 (k+1)(k+1)(k+1)\-th trial is the first success hence draws samples in {0,1,…}\\{0, 1, \\ldots\\}{0,1,…}, whereas [`torch.Tensor.geometric_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.geometric_.html#torch.Tensor.geometric_ "torch.Tensor.geometric_")\
 k\-th trial is the first success hence draws samples in {1,2,…}\\{1, 2, \\ldots\\}{1,2,…}.\
\
Example:\
\
\>>> m \= Geometric(torch.tensor(\[0.3\]))\
\>>> m.sample()  \# underlying Bernoulli has 30% chance 1; 70% chance 0\
tensor(\[ 2.\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **probs** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the probability of sampling 1. Must be in range (0, 1\]
    
*   **logits** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the log-odds of sampling 1.
    

arg\_constraints _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.arg_constraints "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/geometric.py#L140)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/geometric.py#L89)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.expand "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/geometric.py#L132)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.log_prob "Link to this definition")

_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.logits "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.mode "Link to this definition")

_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.probs "Link to this definition")

sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/geometric.py#L120)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.sample "Link to this definition")

support _\= IntegerGreaterThan(lower\_bound=0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.geometric.Geometric.variance "Link to this definition")

Gumbel[#](https://docs.pytorch.org/docs/2.15/distributions.html#gumbel "Link to this heading")

-----------------------------------------------------------------------------------------------

_class_ torch.distributions.gumbel.Gumbel(_loc_, _scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gumbel.py#L17)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Samples from a Gumbel Distribution.

Examples:

\>>> m \= Gumbel(torch.tensor(\[1.0\]), torch.tensor(\[2.0\]))
\>>> m.sample()  \# sample from Gumbel distribution with loc=1, scale=2
tensor(\[ 1.0124\])

Copy to clipboard

Parameters:

*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Location parameter of the distribution
    
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Scale parameter of the distribution
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.arg_constraints "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gumbel.py#L90)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gumbel.py#L61)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.expand "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/gumbel.py#L68)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.mode "Link to this definition")

_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.stddev "Link to this definition")

support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel.variance "Link to this definition")

HalfCauchy[#](https://docs.pytorch.org/docs/2.15/distributions.html#halfcauchy "Link to this heading")

-------------------------------------------------------------------------------------------------------

_class_ torch.distributions.half\_cauchy.HalfCauchy(_scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L15)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Creates a half-Cauchy distribution parameterized by scale where:

X ~ Cauchy(0, scale)
Y \= |X| ~ HalfCauchy(scale)

Copy to clipboard

Example:

\>>> m \= HalfCauchy(torch.tensor(\[1.0\]))
\>>> m.sample()  \# half-cauchy distributed with scale=1
tensor(\[ 2.3214\])

Copy to clipboard

Parameters:

**scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – scale of the full Cauchy distribution

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.arg_constraints "Link to this definition")

base\_dist_: [Cauchy](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.cauchy.Cauchy "torch.distributions.cauchy.Cauchy")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.base_dist "Link to this definition")

cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L83)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.cdf "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L91)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L48)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.has_rsample "Link to this definition")

icdf(_prob_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L88)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.icdf "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_cauchy.py#L73)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.mode "Link to this definition")

_property_ scale_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.scale "Link to this definition")

support _\= GreaterThanEq(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy.variance "Link to this definition")

HalfNormal[#](https://docs.pytorch.org/docs/2.15/distributions.html#halfnormal "Link to this heading")

-------------------------------------------------------------------------------------------------------

_class_ torch.distributions.half\_normal.HalfNormal(_scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L15)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Creates a half-normal distribution parameterized by scale where:

X ~ Normal(0, scale)
Y \= |X| ~ HalfNormal(scale)

Copy to clipboard

Example:

\>>> m \= HalfNormal(torch.tensor(\[1.0\]))
\>>> m.sample()  \# half-normal distributed with scale=1
tensor(\[ 0.1046\])

Copy to clipboard

Parameters:

**scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – scale of the full Normal distribution

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.arg_constraints "Link to this definition")

base\_dist_: [Normal](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal "torch.distributions.normal.Normal")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.base_dist "Link to this definition")

cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L75)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.cdf "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L83)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L48)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.has_rsample "Link to this definition")

icdf(_prob_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L80)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.icdf "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/half_normal.py#L68)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.mode "Link to this definition")

_property_ scale_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.scale "Link to this definition")

support _\= GreaterThanEq(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal.variance "Link to this definition")

Independent[#](https://docs.pytorch.org/docs/2.15/distributions.html#independent "Link to this heading")

---------------------------------------------------------------------------------------------------------

_class_ torch.distributions.independent.Independent(_base\_distribution_, _reinterpreted\_batch\_ndims_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L18)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")
, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.15)")
\[`D`\]

Reinterprets some of the batch dims of a distribution as event dims.

This is mainly useful for changing the shape of the result of [`log_prob()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.log_prob "torch.distributions.independent.Independent.log_prob")
. For example to create a diagonal Normal distribution with the same shape as a Multivariate Normal distribution (so they are interchangeable), you can:

\>>> from torch.distributions.multivariate\_normal import MultivariateNormal
\>>> from torch.distributions.normal import Normal
\>>> loc \= torch.zeros(3)
\>>> scale \= torch.ones(3)
\>>> mvn \= MultivariateNormal(loc, scale\_tril\=torch.diag(scale))
\>>> \[mvn.batch\_shape, mvn.event\_shape\]
\[torch.Size(\[\]), torch.Size(\[3\])\]
\>>> normal \= Normal(loc, scale)
\>>> \[normal.batch\_shape, normal.event\_shape\]
\[torch.Size(\[3\]), torch.Size(\[\])\]
\>>> diagn \= Independent(normal, 1)
\>>> \[diagn.batch\_shape, diagn.event\_shape\]
\[torch.Size(\[\]), torch.Size(\[3\])\]

Copy to clipboard

Parameters:

*   **base\_distribution** ([_torch.distributions.distribution.Distribution_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")
    ) – a base distribution
    
*   **reinterpreted\_batch\_ndims** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of batch dims to reinterpret as event dims
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.arg_constraints "Link to this definition")

base\_dist_: D_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.base_dist "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L124)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.entropy "Link to this definition")

enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L128)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.enumerate_support "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L71)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.expand "Link to this definition")

_property_ has\_enumerate\_support_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.has_enumerate_support "Link to this definition")

_property_ has\_rsample_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.has_rsample "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L120)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.mode "Link to this definition")

rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L117)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.rsample "Link to this definition")

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/independent.py#L114)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.sample "Link to this definition")

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.support "Link to this definition")

Return type:

\_DependentProperty

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.independent.Independent.variance "Link to this definition")

InverseGamma[#](https://docs.pytorch.org/docs/2.15/distributions.html#inversegamma "Link to this heading")

-----------------------------------------------------------------------------------------------------------

_class_ torch.distributions.inverse\_gamma.InverseGamma(_concentration_, _rate_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/inverse_gamma.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Creates an inverse gamma distribution parameterized by [`concentration`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.concentration "torch.distributions.inverse_gamma.InverseGamma.concentration")
 and [`rate`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.rate "torch.distributions.inverse_gamma.InverseGamma.rate")
 where:

X ~ Gamma(concentration, rate)
Y \= 1 / X ~ InverseGamma(concentration, rate)

Copy to clipboard

Example:

\>>> m \= InverseGamma(torch.tensor(\[2.0\]), torch.tensor(\[3.0\]))
\>>> m.sample()
tensor(\[ 1.2953\])

Copy to clipboard

Parameters:

*   **concentration** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – shape parameter of the distribution (often referred to as alpha)
    
*   **rate** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – rate = 1 / scale of the distribution (often referred to as beta)
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'concentration': GreaterThan(lower\_bound=0.0), 'rate': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.arg_constraints "Link to this definition")

base\_dist_: [Gamma](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gamma.Gamma "torch.distributions.gamma.Gamma")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.base_dist "Link to this definition")

_property_ concentration_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.concentration "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/inverse_gamma.py#L86)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/inverse_gamma.py#L58)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.has_rsample "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.mode "Link to this definition")

_property_ rate_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.rate "Link to this definition")

support _\= GreaterThan(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.inverse_gamma.InverseGamma.variance "Link to this definition")

Kumaraswamy[#](https://docs.pytorch.org/docs/2.15/distributions.html#kumaraswamy "Link to this heading")

---------------------------------------------------------------------------------------------------------

_class_ torch.distributions.kumaraswamy.Kumaraswamy(_concentration1_, _concentration0_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/kumaraswamy.py#L24)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Samples from a Kumaraswamy distribution.

Example:

\>>> m \= Kumaraswamy(torch.tensor(\[1.0\]), torch.tensor(\[1.0\]))
\>>> m.sample()  \# sample from a Kumaraswamy distribution with concentration alpha=1 and beta=1
tensor(\[ 0.1729\])

Copy to clipboard

Parameters:

*   **concentration1** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – 1st concentration parameter of the distribution (often referred to as alpha)
    
*   **concentration0** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – 2nd concentration parameter of the distribution (often referred to as beta)
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'concentration0': GreaterThan(lower\_bound=0.0), 'concentration1': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.arg_constraints "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/kumaraswamy.py#L98)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/kumaraswamy.py#L72)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.has_rsample "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.mode "Link to this definition")

support _\= Interval(lower\_bound=0.0, upper\_bound=1.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kumaraswamy.Kumaraswamy.variance "Link to this definition")

LKJCholesky[#](https://docs.pytorch.org/docs/2.15/distributions.html#lkjcholesky "Link to this heading")

---------------------------------------------------------------------------------------------------------

_class_ torch.distributions.lkj\_cholesky.LKJCholesky(_dim_, _concentration\=1.0_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lkj_cholesky.py#L23)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

LKJ distribution for lower Cholesky factor of correlation matrices. The distribution is controlled by `concentration` parameter η\\etaη to make the probability of the correlation matrix MMM generated from a Cholesky factor proportional to det⁡(M)η−1\\det(M)^{\\eta - 1}det(M)η−1. Because of that, when `concentration == 1`, we have a uniform distribution over Cholesky factors of correlation matrices:

L ~ LKJCholesky(dim, concentration)
X \= L @ L' ~ LKJCorr(dim, concentration)

Copy to clipboard

Note that this distribution samples the Cholesky factor of correlation matrices and not the correlation matrices themselves and thereby differs slightly from the derivations in \[1\] for the LKJCorr distribution. For sampling, this uses the Onion method from \[1\] Section 3.

Example:

\>>> l \= LKJCholesky(3, 0.5)
\>>> l.sample()  \# l @ l.T is a sample of a correlation 3x3 matrix
tensor(\[\[ 1.0000,  0.0000,  0.0000\],\
        \[ 0.3516,  0.9361,  0.0000\],\
        \[-0.1899,  0.4748,  0.8593\]\])

Copy to clipboard

Parameters:

*   **dimension** (_dim_) – dimension of the matrices
    
*   **concentration** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – concentration/shape parameter of the distribution (often referred to as eta)
    

**References**

\[1\] Generating random correlation matrices based on vines and extended onion method (2009), Daniel Lewandowski, Dorota Kurowicka, Harry Joe. Journal of Multivariate Analysis. 100. 10.1016/j.jmva.2009.04.008

arg\_constraints _\= {'concentration': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky.arg_constraints "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lkj_cholesky.py#L93)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky.expand "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lkj_cholesky.py#L126)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky.log_prob "Link to this definition")

sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lkj_cholesky.py#L105)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky.sample "Link to this definition")

support _\= CorrCholesky()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lkj_cholesky.LKJCholesky.support "Link to this definition")

Laplace[#](https://docs.pytorch.org/docs/2.15/distributions.html#laplace "Link to this heading")

-------------------------------------------------------------------------------------------------

_class_ torch.distributions.laplace.Laplace(_loc_, _scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

Creates a Laplace distribution parameterized by `loc` and `scale`.

Example:

\>>> m \= Laplace(torch.tensor(\[0.0\]), torch.tensor(\[1.0\]))
\>>> m.sample()  \# Laplace distributed with loc=0, scale=1
tensor(\[ 0.1046\])

Copy to clipboard

Parameters:

*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – mean of the distribution
    
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – scale of the distribution
    

arg\_constraints _\= {'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.arg_constraints "Link to this definition")

cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L92)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.cdf "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L103)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L64)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.has_rsample "Link to this definition")

icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L99)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.icdf "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L87)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.mode "Link to this definition")

rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/laplace.py#L73)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.rsample "Link to this definition")

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.stddev "Link to this definition")

support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.laplace.Laplace.variance "Link to this definition")

LogNormal[#](https://docs.pytorch.org/docs/2.15/distributions.html#lognormal "Link to this heading")

-----------------------------------------------------------------------------------------------------

_class_ torch.distributions.log\_normal.LogNormal(_loc_, _scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/log_normal.py#L13)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal "Link to this definition")

Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")

Creates a log-normal distribution parameterized by [`loc`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.loc "torch.distributions.log_normal.LogNormal.loc")
 and [`scale`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.scale "torch.distributions.log_normal.LogNormal.scale")
 where:

X ~ Normal(loc, scale)
Y \= exp(X) ~ LogNormal(loc, scale)

Copy to clipboard

Example:

\>>> m \= LogNormal(torch.tensor(\[0.0\]), torch.tensor(\[1.0\]))
\>>> m.sample()  \# log-normal distributed with mean=0 and stddev=1
tensor(\[ 0.1046\])

Copy to clipboard

Parameters:

*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – mean of log of distribution
    
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – standard deviation of log of the distribution
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.arg_constraints "Link to this definition")

base\_dist_: [Normal](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal "torch.distributions.normal.Normal")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.base_dist "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/log_normal.py#L74)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/log_normal.py#L49)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.has_rsample "Link to this definition")

_property_ loc_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.loc "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.mode "Link to this definition")

_property_ scale_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.scale "Link to this definition")

support _\= GreaterThan(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal.variance "Link to this definition")

LowRankMultivariateNormal[#](https://docs.pytorch.org/docs/2.15/distributions.html#lowrankmultivariatenormal "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

_class_ torch.distributions.lowrank\_multivariate\_normal.LowRankMultivariateNormal(_loc_, _cov\_factor_, _cov\_diag_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lowrank_multivariate_normal.py#L54)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

Creates a multivariate normal distribution with covariance matrix having a low-rank form parameterized by `cov_factor` and `cov_diag`:

covariance\_matrix \= cov\_factor @ cov\_factor.T + cov\_diag

Copy to clipboard

Example

\>>> m \= LowRankMultivariateNormal(
...     torch.zeros(2), torch.tensor(\[\[1.0\], \[0.0\]\]), torch.ones(2)
... )
\>>> m.sample()  \# normally distributed with mean=\`\[0,0\]\`, cov\_factor=\`\[\[1\],\[0\]\]\`, cov\_diag=\`\[1,1\]\`
tensor(\[-0.2102, -0.5429\])

Copy to clipboard

Parameters:

*   **loc** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – mean of the distribution with shape batch\_shape + event\_shape
    
*   **cov\_factor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – factor part of low-rank form of covariance matrix with shape batch\_shape + event\_shape + (rank,)
    
*   **cov\_diag** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – diagonal part of low-rank form of covariance matrix with shape batch\_shape + event\_shape
    

Note

The computation for determinant and inverse of covariance matrix is avoided when cov\_factor.shape\[1\] << cov\_factor.shape\[0\] thanks to [Woodbury matrix identity](https://en.wikipedia.org/wiki/Woodbury_matrix_identity)
 and [matrix determinant lemma](https://en.wikipedia.org/wiki/Matrix_determinant_lemma)
. Thanks to these formulas, we just need to compute the determinant and inverse of the small size “capacitance” matrix:

capacitance \= I + cov\_factor.T @ inv(cov\_diag) @ cov\_factor

Copy to clipboard

arg\_constraints _\= {'cov\_diag': IndependentConstraint(GreaterThan(lower\_bound=0.0), 1), 'cov\_factor': IndependentConstraint(Real(), 2), 'loc': IndependentConstraint(Real(), 1)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.arg_constraints "Link to this definition")

_property_ covariance\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.covariance_matrix "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lowrank_multivariate_normal.py#L242)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lowrank_multivariate_normal.py#L141)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.has_rsample "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lowrank_multivariate_normal.py#L225)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.mode "Link to this definition")

_property_ precision\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.precision_matrix "Link to this definition")

rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/lowrank_multivariate_normal.py#L214)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.rsample "Link to this definition")

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

_property_ scale\_tril_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.scale_tril "Link to this definition")

support _\= IndependentConstraint(Real(), 1)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal.variance "Link to this definition")

MixtureSameFamily[#](https://docs.pytorch.org/docs/2.15/distributions.html#mixturesamefamily "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

_class_ torch.distributions.mixture\_same\_family.MixtureSameFamily(_mixture\_distribution_, _component\_distribution_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/mixture_same_family.py#L13)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

The MixtureSameFamily distribution implements a (batch of) mixture distribution where all components are from different parameterizations of the same distribution type. It is parameterized by a Categorical “selecting distribution” (over k components) and a component distribution, i.e., a Distribution with a rightmost batch shape (equal to \[k\]) which indexes each (batch of) component.

Examples:

\>>> \# Construct Gaussian Mixture Model in 1D consisting of 5 equally
\>>> \# weighted normal distributions
\>>> mix \= D.Categorical(torch.ones(5,))
\>>> comp \= D.Normal(torch.randn(5,), torch.rand(5,))
\>>> gmm \= MixtureSameFamily(mix, comp)

\>>> \# Construct Gaussian Mixture Model in 2D consisting of 5 equally
\>>> \# weighted bivariate normal distributions
\>>> mix \= D.Categorical(torch.ones(5,))
\>>> comp \= D.Independent(D.Normal(
...          torch.randn(5,2), torch.rand(5,2)), 1)
\>>> gmm \= MixtureSameFamily(mix, comp)

\>>> \# Construct a batch of 3 Gaussian Mixture Models in 2D each
\>>> \# consisting of 5 random weighted bivariate normal distributions
\>>> mix \= D.Categorical(torch.rand(3,5))
\>>> comp \= D.Independent(D.Normal(
...         torch.randn(3,5,2), torch.rand(3,5,2)), 1)
\>>> gmm \= MixtureSameFamily(mix, comp)

Copy to clipboard

Parameters:

*   **mixture\_distribution** ([_Categorical_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical "torch.distributions.categorical.Categorical")
    ) – torch.distributions.Categorical\-like instance. Manages the probability of selecting components. The number of categories must match the rightmost batch dimension of the component\_distribution. Must have either scalar batch\_shape or batch\_shape matching component\_distribution.batch\_shape\[:-1\]
    
*   **component\_distribution** ([_Distribution_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")
    ) – torch.distributions.Distribution\-like instance. Right-most batch dimension indexes component.
    

arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.arg_constraints "Link to this definition")

cdf(_x_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/mixture_same_family.py#L161)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.cdf "Link to this definition")

_property_ component\_distribution_: [Distribution](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.component_distribution "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/mixture_same_family.py#L111)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.expand "Link to this definition")

has\_rsample _\= False_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.has_rsample "Link to this definition")

log\_prob(_x_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/mixture_same_family.py#L168)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.mean "Link to this definition")

_property_ mixture\_distribution_: [Categorical](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.categorical.Categorical "torch.distributions.categorical.Categorical")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.mixture_distribution "Link to this definition")

sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/mixture_same_family.py#L178)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.sample "Link to this definition")

_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.support "Link to this definition")

Return type:

\_DependentProperty

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.mixture_same_family.MixtureSameFamily.variance "Link to this definition")

Multinomial[#](https://docs.pytorch.org/docs/2.15/distributions.html#multinomial "Link to this heading")

---------------------------------------------------------------------------------------------------------

_class_ torch.distributions.multinomial.Multinomial(_total\_count\=1_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multinomial.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

Creates a Multinomial distribution parameterized by [`total_count`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.total_count "torch.distributions.multinomial.Multinomial.total_count")
 and either [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.probs "torch.distributions.multinomial.Multinomial.probs")
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.logits "torch.distributions.multinomial.Multinomial.logits")
 (but not both). The innermost dimension of [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.probs "torch.distributions.multinomial.Multinomial.probs")
 indexes over categories. All other dimensions index over batches.

Note that [`total_count`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.total_count "torch.distributions.multinomial.Multinomial.total_count")
 need not be specified if only [`log_prob()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.log_prob "torch.distributions.multinomial.Multinomial.log_prob")
 is called (see example below)

Note

The probs argument must be non-negative, finite and have a non-zero sum, and it will be normalized to sum to 1 along the last dimension. [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.probs "torch.distributions.multinomial.Multinomial.probs")
 will return this normalized value. The logits argument will be interpreted as unnormalized log probabilities and can therefore be any real number. It will likewise be normalized so that the resulting probabilities sum to 1 along the last dimension. [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.logits "torch.distributions.multinomial.Multinomial.logits")
 will return this normalized value.

*   [`sample()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.sample "torch.distributions.multinomial.Multinomial.sample")
     requires a single shared total\_count for all parameters and samples.
    
*   [`log_prob()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.log_prob "torch.distributions.multinomial.Multinomial.log_prob")
     allows different total\_count for each parameter and sample.
    

Example:

\>>> m \= Multinomial(100, torch.tensor(\[ 1., 1., 1., 1.\]))
\>>> x \= m.sample()  \# equal probability of 0, 1, 2, 3
tensor(\[ 21.,  24.,  30.,  25.\])

\>>> Multinomial(probs\=torch.tensor(\[1., 1., 1., 1.\])).log\_prob(x)
tensor(\[-4.1338\])

Copy to clipboard

Parameters:

*   **total\_count** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of trials
    
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – event probabilities
    
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – event log probabilities (unnormalized)
    

arg\_constraints _\= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.arg_constraints "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multinomial.py#L127)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multinomial.py#L81)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.expand "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multinomial.py#L144)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.log_prob "Link to this definition")

_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.logits "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.mean "Link to this definition")

_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.param_shape "Link to this definition")

_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.probs "Link to this definition")

sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multinomial.py#L113)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.sample "Link to this definition")

_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.support "Link to this definition")

Return type:

\_DependentProperty

total\_count_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.total_count "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial.variance "Link to this definition")

MultivariateNormal[#](https://docs.pytorch.org/docs/2.15/distributions.html#multivariatenormal "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

_class_ torch.distributions.multivariate\_normal.MultivariateNormal(_loc_, _covariance\_matrix\=None_, _precision\_matrix\=None_, _scale\_tril\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multivariate_normal.py#L88)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

Creates a multivariate normal (also called Gaussian) distribution parameterized by a mean vector and a covariance matrix.

The multivariate normal distribution can be parameterized either in terms of a positive definite covariance matrix Σ\\mathbf{\\Sigma}Σ or a positive definite precision matrix Σ−1\\mathbf{\\Sigma}^{-1}Σ−1 or a lower-triangular matrix L\\mathbf{L}L with positive-valued diagonal entries, such that Σ\=LL⊤\\mathbf{\\Sigma} = \\mathbf{L}\\mathbf{L}^\\topΣ\=LL⊤. This triangular matrix can be obtained via e.g. Cholesky decomposition of the covariance.

Example

\>>> m \= MultivariateNormal(torch.zeros(2), torch.eye(2))
\>>> m.sample()  \# normally distributed with mean=\`\[0,0\]\` and covariance\_matrix=\`I\`
tensor(\[-0.2102, -0.5429\])

Copy to clipboard

Parameters:

*   **loc** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – mean of the distribution
    
*   **covariance\_matrix** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – positive-definite covariance matrix
    
*   **precision\_matrix** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – positive-definite precision matrix
    
*   **scale\_tril** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – lower-triangular factor of covariance, with positive-valued diagonal
    

Note

Only one of [`covariance_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.covariance_matrix "torch.distributions.multivariate_normal.MultivariateNormal.covariance_matrix")
 or [`precision_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.precision_matrix "torch.distributions.multivariate_normal.MultivariateNormal.precision_matrix")
 or [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.scale_tril "torch.distributions.multivariate_normal.MultivariateNormal.scale_tril")
 can be specified.

Using [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.scale_tril "torch.distributions.multivariate_normal.MultivariateNormal.scale_tril")
 will be more efficient: all computations internally are based on [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.scale_tril "torch.distributions.multivariate_normal.MultivariateNormal.scale_tril")
. If [`covariance_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.covariance_matrix "torch.distributions.multivariate_normal.MultivariateNormal.covariance_matrix")
 or [`precision_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.precision_matrix "torch.distributions.multivariate_normal.MultivariateNormal.precision_matrix")
 is passed instead, it is only used to compute the corresponding lower triangular matrices using a Cholesky decomposition.

arg\_constraints _\= {'covariance\_matrix': PositiveDefinite(), 'loc': IndependentConstraint(Real(), 1), 'precision\_matrix': PositiveDefinite(), 'scale\_tril': LowerCholesky()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.arg_constraints "Link to this definition")

_property_ covariance\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.covariance_matrix "Link to this definition")

entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multivariate_normal.py#L266)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.entropy "Link to this definition")

expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multivariate_normal.py#L198)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.expand "Link to this definition")

has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.has_rsample "Link to this definition")

log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multivariate_normal.py#L256)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.log_prob "Link to this definition")

_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.mean "Link to this definition")

_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.mode "Link to this definition")

_property_ precision\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.precision_matrix "Link to this definition")

rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/multivariate_normal.py#L251)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.rsample "Link to this definition")

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

_property_ scale\_tril_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.scale_tril "Link to this definition")

support _\= IndependentConstraint(Real(), 1)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.support "Link to this definition")

_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multivariate_normal.MultivariateNormal.variance "Link to this definition")

NegativeBinomial[#](https://docs.pytorch.org/docs/2.15/distributions.html#negativebinomial "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

_class_ torch.distributions.negative\_binomial.NegativeBinomial(_total\_count_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/negative_binomial.py#L20)
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial "Link to this definition")

Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")

Creates a Negative Binomial distribution, i.e. distribution of the number of successful independent and identical Bernoulli trials before `total_count` failures are achieved. The probability of success of each Bernoulli trial is [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.probs "torch.distributions.negative_binomial.NegativeBinomial.probs")
.

Parameters:

*   **total\_count** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – non-negative number of negative Bernoulli trials to stop, although the distribution is still valid for real valued count
    
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Event probabilities of success in the half open interval \[0, 1)\
    \
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Event log-odds for probabilities of success\
    \
\
arg\_constraints _\= {'logits': Real(), 'probs': HalfOpenInterval(lower\_bound=0.0, upper\_bound=1.0), 'total\_count': GreaterThanEq(lower\_bound=0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.arg_constraints "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/negative_binomial.py#L75)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.expand "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/negative_binomial.py#L130)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.mode "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.probs "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/negative_binomial.py#L125)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.sample "Link to this definition")\
\
support _\= IntegerGreaterThan(lower\_bound=0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.negative_binomial.NegativeBinomial.variance "Link to this definition")\
\
Normal[#](https://docs.pytorch.org/docs/2.15/distributions.html#normal "Link to this heading")\
\
-----------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.normal.Normal(_loc_, _scale_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a normal (also called Gaussian) distribution parameterized by `loc` and `scale`.\
\
Example:\
\
\>>> m \= Normal(torch.tensor(\[0.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# normally distributed with loc=0 and scale=1\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – mean of the distribution (often referred to as mu)\
    \
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – standard deviation of the distribution (often referred to as sigma)\
    \
\
arg\_constraints _\= {'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L103)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L113)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L68)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L110)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.icdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L82)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/normal.py#L77)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.sample "Link to this definition")\
\
_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.stddev "Link to this definition")\
\
support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.normal.Normal.variance "Link to this definition")\
\
OneHotCategorical[#](https://docs.pytorch.org/docs/2.15/distributions.html#onehotcategorical "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.one\_hot\_categorical.OneHotCategorical(_probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L14)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a one-hot categorical distribution parameterized by [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.probs "torch.distributions.one_hot_categorical.OneHotCategorical.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.logits "torch.distributions.one_hot_categorical.OneHotCategorical.logits")\
.\
\
Samples are one-hot coded vectors of size `probs.size(-1)`.\
\
Note\
\
The probs argument must be non-negative, finite and have a non-zero sum, and it will be normalized to sum to 1 along the last dimension. [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.probs "torch.distributions.one_hot_categorical.OneHotCategorical.probs")\
 will return this normalized value. The logits argument will be interpreted as unnormalized log probabilities and can therefore be any real number. It will likewise be normalized so that the resulting probabilities sum to 1 along the last dimension. [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.logits "torch.distributions.one_hot_categorical.OneHotCategorical.logits")\
 will return this normalized value.\
\
See also: `torch.distributions.Categorical()` for specifications of [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.probs "torch.distributions.one_hot_categorical.OneHotCategorical.probs")\
 and [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.logits "torch.distributions.one_hot_categorical.OneHotCategorical.logits")\
.\
\
Example:\
\
\>>> m \= OneHotCategorical(torch.tensor(\[ 0.25, 0.25, 0.25, 0.25 \]))\
\>>> m.sample()  \# equal probability of 0, 1, 2, 3\
tensor(\[ 0.,  0.,  0.,  1.\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – event probabilities\
    \
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – event log probabilities (unnormalized)\
    \
\
arg\_constraints _\= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L117)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.entropy "Link to this definition")\
\
enumerate\_support(_expand\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L120)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.enumerate_support "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L61)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.expand "Link to this definition")\
\
has\_enumerate\_support _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.has_enumerate_support "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L111)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.logits "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.mode "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.probs "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/one_hot_categorical.py#L104)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.sample "Link to this definition")\
\
support _\= OneHot()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.one_hot_categorical.OneHotCategorical.variance "Link to this definition")\
\
Pareto[#](https://docs.pytorch.org/docs/2.15/distributions.html#pareto "Link to this heading")\
\
-----------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.pareto.Pareto(_scale_, _alpha_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/pareto.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto "Link to this definition")\
\
Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
\
Samples from a Pareto Type 1 distribution.\
\
Example:\
\
\>>> m \= Pareto(torch.tensor(\[1.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# sample from a Pareto distribution with scale=1 and alpha=1\
tensor(\[ 1.5623\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Scale parameter of the distribution\
    \
*   **alpha** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Shape parameter of the distribution\
    \
\
arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'alpha': GreaterThan(lower\_bound=0.0), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/pareto.py#L73)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.entropy "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/pareto.py#L45)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.expand "Link to this definition")\
\
Return type:\
\
[_Pareto_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto "torch.distributions.pareto.Pareto")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.mode "Link to this definition")\
\
_property_ support_: [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto.variance "Link to this definition")\
\
Poisson[#](https://docs.pytorch.org/docs/2.15/distributions.html#poisson "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.poisson.Poisson(_rate_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/poisson.py#L14)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a Poisson distribution parameterized by `rate`, the rate parameter.\
\
Samples are nonnegative integers, with a pmf given by\
\
rateke−ratek!\\mathrm{rate}^k \\frac{e^{-\\mathrm{rate}}}{k!} ratekk!e−rate​\
\
Example:\
\
\>>> m \= Poisson(torch.tensor(\[4\]))\
\>>> m.sample()\
tensor(\[ 3.\])\
\
Copy to clipboard\
\
Parameters:\
\
**rate** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
) – the rate parameter\
\
arg\_constraints _\= {'rate': GreaterThanEq(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.arg_constraints "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/poisson.py#L62)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.expand "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/poisson.py#L75)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.mode "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/poisson.py#L70)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.sample "Link to this definition")\
\
support _\= IntegerGreaterThan(lower\_bound=0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.poisson.Poisson.variance "Link to this definition")\
\
RelaxedBernoulli[#](https://docs.pytorch.org/docs/2.15/distributions.html#relaxedbernoulli "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.relaxed\_bernoulli.RelaxedBernoulli(_temperature_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L122)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli "Link to this definition")\
\
Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
\
Creates a RelaxedBernoulli distribution, parameterized by [`temperature`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.temperature "torch.distributions.relaxed_bernoulli.RelaxedBernoulli.temperature")\
, and either [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.probs "torch.distributions.relaxed_bernoulli.RelaxedBernoulli.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.logits "torch.distributions.relaxed_bernoulli.RelaxedBernoulli.logits")\
 (but not both). This is a relaxed version of the Bernoulli distribution, so the values are in (0, 1), and has reparametrizable samples.\
\
Example:\
\
\>>> m \= RelaxedBernoulli(torch.tensor(\[2.2\]),\
...                      torch.tensor(\[0.1, 0.2, 0.3, 0.99\]))\
\>>> m.sample()\
tensor(\[ 0.2951,  0.3442,  0.8918,  0.9021\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **temperature** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – relaxation temperature\
    \
*   **probs** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the probability of sampling 1\
    \
*   **logits** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the log-odds of sampling 1\
    \
\
arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.arg_constraints "Link to this definition")\
\
base\_dist_: [LogitRelaxedBernoulli](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli "torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.base_dist "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L160)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.has_rsample "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.logits "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.probs "Link to this definition")\
\
support _\= Interval(lower\_bound=0.0, upper\_bound=1.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.support "Link to this definition")\
\
_property_ temperature_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli.temperature "Link to this definition")\
\
LogitRelaxedBernoulli[#](https://docs.pytorch.org/docs/2.15/distributions.html#logitrelaxedbernoulli "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.relaxed\_bernoulli.LogitRelaxedBernoulli(_temperature_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L22)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a LogitRelaxedBernoulli distribution parameterized by [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.probs "torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.logits "torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.logits")\
 (but not both), which is the logit of a RelaxedBernoulli distribution.\
\
Samples are logits of values in (0, 1). See \[1\] for more details.\
\
Parameters:\
\
*   **temperature** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – relaxation temperature\
    \
*   **probs** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the probability of sampling 1\
    \
*   **logits** (_Number__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – the log-odds of sampling 1\
    \
\
\[1\] The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables (Maddison et al., 2017)\
\
\[2\] Categorical Reparametrization with Gumbel-Softmax (Jang et al., 2017)\
\
arg\_constraints _\= {'logits': Real(), 'probs': Interval(lower\_bound=0.0, upper\_bound=1.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.arg_constraints "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L75)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.expand "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L114)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.log_prob "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.logits "Link to this definition")\
\
_property_ param\_shape_: [Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.param_shape "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.probs "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_bernoulli.py#L104)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli.support "Link to this definition")\
\
RelaxedOneHotCategorical[#](https://docs.pytorch.org/docs/2.15/distributions.html#relaxedonehotcategorical "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.relaxed\_categorical.RelaxedOneHotCategorical(_temperature_, _probs\=None_, _logits\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_categorical.py#L109)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical "Link to this definition")\
\
Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
\
Creates a RelaxedOneHotCategorical distribution parameterized by [`temperature`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.temperature "torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.temperature")\
, and either [`probs`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.probs "torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.probs")\
 or [`logits`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.logits "torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.logits")\
. This is a relaxed version of the `OneHotCategorical` distribution, so its samples are on simplex, and are reparametrizable.\
\
Example:\
\
\>>> m \= RelaxedOneHotCategorical(torch.tensor(\[2.2\]),\
...                              torch.tensor(\[0.1, 0.2, 0.3, 0.4\]))\
\>>> m.sample()\
tensor(\[ 0.1294,  0.2324,  0.3859,  0.2523\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **temperature** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – relaxation temperature\
    \
*   **probs** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – event probabilities\
    \
*   **logits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – unnormalized log probability for each event\
    \
\
arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.arg_constraints "Link to this definition")\
\
base\_dist_: ExpRelaxedCategorical_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.base_dist "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/relaxed_categorical.py#L149)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.has_rsample "Link to this definition")\
\
_property_ logits_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.logits "Link to this definition")\
\
_property_ probs_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.probs "Link to this definition")\
\
support _\= Simplex()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.support "Link to this definition")\
\
_property_ temperature_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical.temperature "Link to this definition")\
\
StudentT[#](https://docs.pytorch.org/docs/2.15/distributions.html#studentt "Link to this heading")\
\
---------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.studentT.StudentT(_df_, _loc\=0.0_, _scale\=1.0_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/studentT.py#L15)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Creates a Student’s t-distribution parameterized by degree of freedom `df`, mean `loc` and scale `scale`.\
\
Example:\
\
\>>> m \= StudentT(torch.tensor(\[2.0\]))\
\>>> m.sample()  \# Student's t-distributed with degrees of freedom=2\
tensor(\[ 0.1046\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **df** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – degrees of freedom\
    \
*   **loc** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – mean of the distribution\
    \
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – scale of the distribution\
    \
\
arg\_constraints _\= {'df': GreaterThan(lower\_bound=0.0), 'loc': Real(), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/studentT.py#L114)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/studentT.py#L76)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/studentT.py#L101)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/studentT.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.studentT.StudentT.variance "Link to this definition")\
\
TransformedDistribution[#](https://docs.pytorch.org/docs/2.15/distributions.html#transformeddistribution "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.transformed\_distribution.TransformedDistribution(_base\_distribution_, _transforms_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L16)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Extension of the Distribution class, which applies a sequence of Transforms to a base distribution. Let f be the composition of transforms applied:\
\
X ~ BaseDistribution\
Y \= f(X) ~ TransformedDistribution(BaseDistribution, f)\
log p(Y) \= log p(X) + log |det (dX/dY)|\
\
Copy to clipboard\
\
Note that the `.event_shape` of a [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
 is the maximum shape of its base distribution and its transforms, since transforms can introduce correlations among events.\
\
An example for the usage of [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
 would be:\
\
\# Building a Logistic Distribution\
\# X ~ Uniform(0, 1)\
\# f = a + b \* logit(X)\
\# Y ~ f(X) ~ Logistic(a, b)\
base\_distribution \= Uniform(0, 1)\
transforms \= \[SigmoidTransform().inv, AffineTransform(loc\=a, scale\=b)\]\
logistic \= TransformedDistribution(base\_distribution, transforms)\
\
Copy to clipboard\
\
For more examples, please look at the implementations of [`Gumbel`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.gumbel.Gumbel "torch.distributions.gumbel.Gumbel")\
, [`HalfCauchy`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_cauchy.HalfCauchy "torch.distributions.half_cauchy.HalfCauchy")\
, [`HalfNormal`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.half_normal.HalfNormal "torch.distributions.half_normal.HalfNormal")\
, [`LogNormal`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.log_normal.LogNormal "torch.distributions.log_normal.LogNormal")\
, [`Pareto`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.pareto.Pareto "torch.distributions.pareto.Pareto")\
, [`Weibull`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull "torch.distributions.weibull.Weibull")\
, [`RelaxedBernoulli`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_bernoulli.RelaxedBernoulli "torch.distributions.relaxed_bernoulli.RelaxedBernoulli")\
 and [`RelaxedOneHotCategorical`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.relaxed_categorical.RelaxedOneHotCategorical "torch.distributions.relaxed_categorical.RelaxedOneHotCategorical")\
\
arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L204)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.cdf "Link to this definition")\
\
Computes the cumulative distribution function by inverting the transform(s) and computing the score of the base distribution.\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L112)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.expand "Link to this definition")\
\
_property_ has\_rsample_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L217)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.icdf "Link to this definition")\
\
Computes the inverse cumulative distribution function using transform(s) and computing the score of the base distribution.\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L168)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.log_prob "Link to this definition")\
\
Scores the sample by inverting the transform(s) and computing the score using the score of the base distribution and the log abs det jacobian.\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L156)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.rsample "Link to this definition")\
\
Generates a sample\_shape shaped reparameterized sample or sample\_shape shaped batch of reparameterized samples if the distribution parameters are batched. Samples first from base distribution and applies transform() for every transform in the list.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transformed_distribution.py#L143)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.sample "Link to this definition")\
\
Generates a sample\_shape shaped sample or sample\_shape shaped batch of samples if the distribution parameters are batched. Samples first from base distribution and applies transform() for every transform in the list.\
\
_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
Uniform[#](https://docs.pytorch.org/docs/2.15/distributions.html#uniform "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.uniform.Uniform(_low_, _high_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L14)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
Generates uniformly distributed random samples from the half-open interval `[low, high)`.\
\
Example:\
\
\>>> m \= Uniform(torch.tensor(\[0.0\]), torch.tensor(\[5.0\]))\
\>>> m.sample()  \# uniformly distributed in the range \[0.0, 5.0)\
tensor(\[ 2.3418\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **low** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – lower range (inclusive).\
    \
*   **high** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – upper range (exclusive).\
    \
\
_property_ arg\_constraints[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.arg_constraints "Link to this definition")\
\
cdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L97)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.cdf "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L107)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L71)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.has_rsample "Link to this definition")\
\
icdf(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L103)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.icdf "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L90)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.mode "Link to this definition")\
\
rsample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/uniform.py#L85)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.rsample "Link to this definition")\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_property_ stddev_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.stddev "Link to this definition")\
\
_property_ support[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.support "Link to this definition")\
\
Return type:\
\
\_DependentProperty\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.uniform.Uniform.variance "Link to this definition")\
\
VonMises[#](https://docs.pytorch.org/docs/2.15/distributions.html#vonmises "Link to this heading")\
\
---------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.von\_mises.VonMises(_loc_, _concentration_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/von_mises.py#L110)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises "Link to this definition")\
\
Bases: [`Distribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
\
A circular von Mises distribution.\
\
This implementation uses polar coordinates. The `loc` and `value` args can be any real number (to facilitate unconstrained optimization), but are interpreted as angles modulo 2 pi.\
\
Example::\
\
\>>> m \= VonMises(torch.tensor(\[1.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# von Mises distributed with loc=1 and concentration=1\
tensor(\[1.9777\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **loc** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – an angle in radians.\
    \
*   **concentration** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – concentration parameter\
    \
\
arg\_constraints _\= {'concentration': GreaterThan(lower\_bound=0.0), 'loc': Real()}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.arg_constraints "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/von_mises.py#L190)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.expand "Link to this definition")\
\
has\_rsample _\= False_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/von_mises.py#L144)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.mean "Link to this definition")\
\
The provided mean is the circular one.\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.mode "Link to this definition")\
\
sample(_sample\_shape\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/von_mises.py#L173)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.sample "Link to this definition")\
\
The sampling algorithm for the von Mises distribution is based on the following paper: D.J. Best and N.I. Fisher, “Efficient simulation of the von Mises distribution.” Applied Statistics (1979): 152-157.\
\
Sampling is always done in double precision internally to avoid a hang in \_rejection\_sample() for small values of the concentration, which starts to happen for single precision around 1e-4 (see issue #88443).\
\
support _\= Real()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.von_mises.VonMises.variance "Link to this definition")\
\
The provided variance is the circular one.\
\
Weibull[#](https://docs.pytorch.org/docs/2.15/distributions.html#weibull "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.weibull.Weibull(_scale_, _concentration_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/weibull.py#L16)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull "Link to this definition")\
\
Bases: [`TransformedDistribution`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transformed_distribution.TransformedDistribution "torch.distributions.transformed_distribution.TransformedDistribution")\
\
Samples from a two-parameter Weibull distribution.\
\
Example\
\
\>>> m \= Weibull(torch.tensor(\[1.0\]), torch.tensor(\[1.0\]))\
\>>> m.sample()  \# sample from a Weibull distribution with scale=1, concentration=1\
tensor(\[ 0.4784\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Scale parameter of distribution (lambda).\
    \
*   **concentration** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Concentration parameter of distribution (k/shape).\
    \
*   **validate\_args** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether to validate arguments. Default: None.\
    \
\
arg\_constraints_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Constraint](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
\]_ _\= {'concentration': GreaterThan(lower\_bound=0.0), 'scale': GreaterThan(lower\_bound=0.0)}_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.arg_constraints "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/weibull.py#L91)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/weibull.py#L58)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.expand "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.mode "Link to this definition")\
\
support _\= GreaterThan(lower\_bound=0.0)_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.weibull.Weibull.variance "Link to this definition")\
\
Wishart[#](https://docs.pytorch.org/docs/2.15/distributions.html#wishart "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.wishart.Wishart(_df_, _covariance\_matrix\=None_, _precision\_matrix\=None_, _scale\_tril\=None_, _validate\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/wishart.py#L33)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart "Link to this definition")\
\
Bases: [`ExponentialFamily`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.exp_family.ExponentialFamily "torch.distributions.exp_family.ExponentialFamily")\
\
Creates a Wishart distribution parameterized by a symmetric positive definite matrix Σ\\SigmaΣ, or its Cholesky decomposition Σ\=LL⊤\\mathbf{\\Sigma} = \\mathbf{L}\\mathbf{L}^\\topΣ\=LL⊤\
\
Example\
\
\>>> m \= Wishart(torch.Tensor(\[2\]), covariance\_matrix\=torch.eye(2))\
\>>> m.sample()  \# Wishart distributed with mean=\`df \* I\` and\
\>>> \# variance(x\_ij)=\`df\` for i != j and variance(x\_ij)=\`2 \* df\` for i == j\
\
Copy to clipboard\
\
Parameters:\
\
*   **df** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – real-valued parameter larger than the (dimension of Square matrix) - 1\
    \
*   **covariance\_matrix** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – positive-definite covariance matrix\
    \
*   **precision\_matrix** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – positive-definite precision matrix\
    \
*   **scale\_tril** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – lower-triangular factor of covariance, with positive-valued diagonal\
    \
\
Note\
\
Only one of [`covariance_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.covariance_matrix "torch.distributions.wishart.Wishart.covariance_matrix")\
 or [`precision_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.precision_matrix "torch.distributions.wishart.Wishart.precision_matrix")\
 or [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.scale_tril "torch.distributions.wishart.Wishart.scale_tril")\
 can be specified. Using [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.scale_tril "torch.distributions.wishart.Wishart.scale_tril")\
 will be more efficient: all computations internally are based on [`scale_tril`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.scale_tril "torch.distributions.wishart.Wishart.scale_tril")\
. If [`covariance_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.covariance_matrix "torch.distributions.wishart.Wishart.covariance_matrix")\
 or [`precision_matrix`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.precision_matrix "torch.distributions.wishart.Wishart.precision_matrix")\
 is passed instead, it is only used to compute the corresponding lower triangular matrices using a Cholesky decomposition. ‘torch.distributions.LKJCholesky’ is a restricted Wishart distribution.\[1\]\
\
**References**\
\
\[1\] Wang, Z., Wu, Y. and Chu, H., 2018. On equivalence of the LKJ distribution and the restricted Wishart distribution. \[2\] Sawyer, S., 2007. Wishart Distributions and Inverse-Wishart Sampling. \[3\] Anderson, T. W., 2003. An Introduction to Multivariate Statistical Analysis (3rd ed.). \[4\] Odell, P. L. & Feiveson, A. H., 1966. A Numerical Procedure to Generate a Sample Covariance Matrix. JASA, 61(313):199-203. \[5\] Ku, Y.-C. & Bloomfield, P., 2010. Generating Random Wishart Matrices with Fractional Degrees of Freedom in OX.\
\
_property_ arg\_constraints[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.arg_constraints "Link to this definition")\
\
_property_ covariance\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.covariance_matrix "Link to this definition")\
\
entropy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/wishart.py#L324)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.entropy "Link to this definition")\
\
expand(_batch\_shape_, _\_instance\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/wishart.py#L160)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.expand "Link to this definition")\
\
has\_rsample _\= True_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.has_rsample "Link to this definition")\
\
log\_prob(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/wishart.py#L303)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.log_prob "Link to this definition")\
\
_property_ mean_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.mean "Link to this definition")\
\
_property_ mode_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.mode "Link to this definition")\
\
_property_ precision\_matrix_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.precision_matrix "Link to this definition")\
\
rsample(_sample\_shape\=()_, _max\_try\_correction\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/wishart.py#L251)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.rsample "Link to this definition")\
\
Warning\
\
In some cases, sampling algorithm based on Bartlett decomposition may return singular matrix samples. Several tries to correct singular samples are performed by default, but it may end up returning singular matrix samples. Singular samples may return \-inf values in .log\_prob(). In those cases, the user should validate the samples and either fix the value of df or adjust max\_try\_correction value for argument in .rsample accordingly.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
_property_ scale\_tril_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.scale_tril "Link to this definition")\
\
support _\= PositiveDefinite()_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.support "Link to this definition")\
\
_property_ variance_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.wishart.Wishart.variance "Link to this definition")\
\
`KL Divergence`[#](https://docs.pytorch.org/docs/2.15/distributions.html#module-torch.distributions.kl "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------\
\
torch.distributions.kl.kl\_divergence(_p_, _q_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/kl.py#L165)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kl.kl_divergence "Link to this definition")\
\
Compute Kullback-Leibler divergence KL(p∥q)KL(p \\| q)KL(p∥q) between two distributions.\
\
KL(p∥q)\=∫p(x)log⁡p(x)q(x) dxKL(p \\| q) = \\int p(x) \\log\\frac {p(x)} {q(x)} \\,dxKL(p∥q)\=∫p(x)logq(x)p(x)​dx\
\
Parameters:\
\
*   **p** ([_Distribution_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
    ) – A `Distribution` object.\
    \
*   **q** ([_Distribution_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
    ) – A `Distribution` object.\
    \
\
Returns:\
\
A batch of KL divergences of shape batch\_shape.\
\
Return type:\
\
[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
Raises:\
\
[**NotImplementedError**](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "(in Python v3.15)")\
 – If the distribution types have not been registered via [`register_kl()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kl.register_kl "torch.distributions.kl.register_kl")\
.\
\
KL divergence is currently implemented for the following distribution pairs:\
\
*   `Bernoulli` and `Bernoulli`\
    \
*   `Bernoulli` and `Poisson`\
    \
*   `Beta` and `Beta`\
    \
*   `Beta` and `ContinuousBernoulli`\
    \
*   `Beta` and `Exponential`\
    \
*   `Beta` and `Gamma`\
    \
*   `Beta` and `Normal`\
    \
*   `Beta` and `Pareto`\
    \
*   `Beta` and `Uniform`\
    \
*   `Binomial` and `Binomial`\
    \
*   `Categorical` and `Categorical`\
    \
*   `Cauchy` and `Cauchy`\
    \
*   `ContinuousBernoulli` and `ContinuousBernoulli`\
    \
*   `ContinuousBernoulli` and `Exponential`\
    \
*   `ContinuousBernoulli` and `Normal`\
    \
*   `ContinuousBernoulli` and `Pareto`\
    \
*   `ContinuousBernoulli` and `Uniform`\
    \
*   `Dirichlet` and `Dirichlet`\
    \
*   `Exponential` and `Beta`\
    \
*   `Exponential` and `ContinuousBernoulli`\
    \
*   `Exponential` and `Exponential`\
    \
*   `Exponential` and `Gamma`\
    \
*   `Exponential` and `Gumbel`\
    \
*   `Exponential` and `Normal`\
    \
*   `Exponential` and `Pareto`\
    \
*   `Exponential` and `Uniform`\
    \
*   `ExponentialFamily` and `ExponentialFamily`\
    \
*   `Gamma` and `Beta`\
    \
*   `Gamma` and `ContinuousBernoulli`\
    \
*   `Gamma` and `Exponential`\
    \
*   `Gamma` and `Gamma`\
    \
*   `Gamma` and `Gumbel`\
    \
*   `Gamma` and `Normal`\
    \
*   `Gamma` and `Pareto`\
    \
*   `Gamma` and `Uniform`\
    \
*   `Geometric` and `Geometric`\
    \
*   `Gumbel` and `Beta`\
    \
*   `Gumbel` and `ContinuousBernoulli`\
    \
*   `Gumbel` and `Exponential`\
    \
*   `Gumbel` and `Gamma`\
    \
*   `Gumbel` and `Gumbel`\
    \
*   `Gumbel` and `Normal`\
    \
*   `Gumbel` and `Pareto`\
    \
*   `Gumbel` and `Uniform`\
    \
*   `HalfNormal` and `HalfNormal`\
    \
*   `Independent` and `Independent`\
    \
*   `Laplace` and `Beta`\
    \
*   `Laplace` and `ContinuousBernoulli`\
    \
*   `Laplace` and `Exponential`\
    \
*   `Laplace` and `Gamma`\
    \
*   `Laplace` and `Laplace`\
    \
*   `Laplace` and `Normal`\
    \
*   `Laplace` and `Pareto`\
    \
*   `Laplace` and `Uniform`\
    \
*   `LowRankMultivariateNormal` and `LowRankMultivariateNormal`\
    \
*   `LowRankMultivariateNormal` and `MultivariateNormal`\
    \
*   `MultivariateNormal` and `LowRankMultivariateNormal`\
    \
*   `MultivariateNormal` and `MultivariateNormal`\
    \
*   `Normal` and `Beta`\
    \
*   `Normal` and `ContinuousBernoulli`\
    \
*   `Normal` and `Exponential`\
    \
*   `Normal` and `Gamma`\
    \
*   `Normal` and `Gumbel`\
    \
*   `Normal` and `Laplace`\
    \
*   `Normal` and `Normal`\
    \
*   `Normal` and `Pareto`\
    \
*   `Normal` and `Uniform`\
    \
*   `OneHotCategorical` and `OneHotCategorical`\
    \
*   `Pareto` and `Beta`\
    \
*   `Pareto` and `ContinuousBernoulli`\
    \
*   `Pareto` and `Exponential`\
    \
*   `Pareto` and `Gamma`\
    \
*   `Pareto` and `Normal`\
    \
*   `Pareto` and `Pareto`\
    \
*   `Pareto` and `Uniform`\
    \
*   `Poisson` and `Bernoulli`\
    \
*   `Poisson` and `Binomial`\
    \
*   `Poisson` and `Poisson`\
    \
*   `TransformedDistribution` and `TransformedDistribution`\
    \
*   `Uniform` and `Beta`\
    \
*   `Uniform` and `ContinuousBernoulli`\
    \
*   `Uniform` and `Exponential`\
    \
*   `Uniform` and `Gamma`\
    \
*   `Uniform` and `Gumbel`\
    \
*   `Uniform` and `Normal`\
    \
*   `Uniform` and `Pareto`\
    \
*   `Uniform` and `Uniform`\
    \
\
torch.distributions.kl.register\_kl(_type\_p_, _type\_q_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/kl.py#L51)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kl.register_kl "Link to this definition")\
\
Decorator to register a pairwise function with [`kl_divergence()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.kl.kl_divergence "torch.distributions.kl.kl_divergence")\
. Usage:\
\
@register\_kl(Normal, Normal)\
def kl\_normal\_normal(p, q):\
    \# insert implementation here\
\
Copy to clipboard\
\
Lookup returns the most specific (type,type) match ordered by subclass. If the match is ambiguous, a RuntimeWarning is raised. For example to resolve the ambiguous situation:\
\
@register\_kl(BaseP, DerivedQ)\
def kl\_version1(p, q): ...\
@register\_kl(DerivedP, BaseQ)\
def kl\_version2(p, q): ...\
\
Copy to clipboard\
\
you should register a third most-specific implementation, e.g.:\
\
register\_kl(DerivedP, DerivedQ)(kl\_version1)  \# Break the tie.\
\
Copy to clipboard\
\
Parameters:\
\
*   **type\_p** ([_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
    ) – A subclass of `Distribution`.\
    \
*   **type\_q** ([_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
    ) – A subclass of `Distribution`.\
    \
\
`Transforms`[#](https://docs.pytorch.org/docs/2.15/distributions.html#module-torch.distributions.transforms "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.transforms.AbsTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L736)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.AbsTransform "Link to this definition")\
\
Transform via the mapping y\=∣x∣y = |x|y\=∣x∣.\
\
_class_ torch.distributions.transforms.AffineTransform(_loc_, _scale_, _event\_dim\=0_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L752)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.AffineTransform "Link to this definition")\
\
Transform via the pointwise affine mapping y\=loc+scale×xy = \\text{loc} + \\text{scale} \\times xy\=loc+scale×x.\
\
Parameters:\
\
*   **loc** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _or_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    ) – Location parameter.\
    \
*   **scale** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _or_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    ) – Scale parameter.\
    \
*   **event\_dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Optional size of event\_shape. This should be zero for univariate random variables, 1 for distributions over vectors, 2 for distributions over matrices, etc.\
    \
\
_class_ torch.distributions.transforms.CatTransform(_tseq_, _dim\=0_, _lengths\=None_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L1076)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.CatTransform "Link to this definition")\
\
Transform functor that applies a sequence of transforms tseq component-wise to each submatrix at dim, of length lengths\[dim\], in a way compatible with [`torch.cat()`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat")\
.\
\
Example:\
\
x0 \= torch.cat(\[torch.range(1, 10), torch.range(1, 10)\], dim\=0)\
x \= torch.cat(\[x0, x0\], dim\=0)\
t0 \= CatTransform(\[ExpTransform(), identity\_transform\], dim\=0, lengths\=\[10, 10\])\
t \= CatTransform(\[t0, t0\], dim\=0, lengths\=\[20, 20\])\
y \= t(x)\
\
Copy to clipboard\
\
_class_ torch.distributions.transforms.ComposeTransform(_parts_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L286)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.ComposeTransform "Link to this definition")\
\
Composes multiple transforms in a chain. The transforms being composed are responsible for caching.\
\
Parameters:\
\
*   **parts** (list of [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
    ) – A list of transforms to compose.\
    \
*   **cache\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Size of cache. If zero, no caching is done. If one, the latest single value is cached. Only 0 and 1 are supported.\
    \
\
_class_ torch.distributions.transforms.CorrCholeskyTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L859)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.CorrCholeskyTransform "Link to this definition")\
\
Transforms an unconstrained real vector xxx with length D∗(D−1)/2D\*(D-1)/2D∗(D−1)/2 into the Cholesky factor of a D-dimension correlation matrix. This Cholesky factor is a lower triangular matrix with positive diagonals and unit Euclidean norm for each row. The transform is processed as follows:\
\
> 1.  First we convert x into a lower triangular matrix in row order.\
>     \
> 2.  For each row XiX\_iXi​ of the lower triangular part, we apply a _signed_ version of class [`StickBreakingTransform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.StickBreakingTransform "torch.distributions.transforms.StickBreakingTransform")\
>      to transform XiX\_iXi​ into a unit Euclidean length vector using the following steps: - Scales into the interval (−1,1)(-1, 1)(−1,1) domain: ri\=tanh⁡(Xi)r\_i = \\tanh(X\_i)ri​\=tanh(Xi​). - Transforms into an unsigned domain: zi\=ri2z\_i = r\_i^2zi​\=ri2​. - Applies si\=StickBreakingTransform(zi)s\_i = StickBreakingTransform(z\_i)si​\=StickBreakingTransform(zi​). - Transforms back into signed domain: yi\=sign(ri)∗siy\_i = sign(r\_i) \* \\sqrt{s\_i}yi​\=sign(ri​)∗si​​.\
>     \
\
_class_ torch.distributions.transforms.CumulativeDistributionTransform(_distribution_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L1319)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.CumulativeDistributionTransform "Link to this definition")\
\
Transform via the cumulative distribution function of a probability distribution.\
\
Parameters:\
\
**distribution** ([_Distribution_](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.distribution.Distribution "torch.distributions.distribution.Distribution")\
) – Distribution whose cumulative distribution function to use for the transformation.\
\
Example:\
\
\# Construct a Gaussian copula from a multivariate normal.\
base\_dist \= MultivariateNormal(\
    loc\=torch.zeros(2),\
    scale\_tril\=LKJCholesky(2).sample(),\
)\
transform \= CumulativeDistributionTransform(Normal(0, 1))\
copula \= TransformedDistribution(base\_dist, \[transform\])\
\
Copy to clipboard\
\
_class_ torch.distributions.transforms.ExpTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L571)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.ExpTransform "Link to this definition")\
\
Transform via the mapping y\=exp⁡(x)y = \\exp(x)y\=exp(x).\
\
_class_ torch.distributions.transforms.IndependentTransform(_base\_transform_, _reinterpreted\_batch\_ndims_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L417)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.IndependentTransform "Link to this definition")\
\
Wrapper around another transform to treat `reinterpreted_batch_ndims`\-many extra of the right most dimensions as dependent. This has no effect on the forward or backward transforms, but does sum out `reinterpreted_batch_ndims`\-many of the rightmost dimensions in `log_abs_det_jacobian()`.\
\
Parameters:\
\
*   **base\_transform** ([`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
    ) – A base transform.\
    \
*   **reinterpreted\_batch\_ndims** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The number of extra rightmost dimensions to treat as dependent.\
    \
\
_class_ torch.distributions.transforms.LowerCholeskyTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L1034)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.LowerCholeskyTransform "Link to this definition")\
\
Transform from unconstrained matrices to lower-triangular matrices with nonnegative diagonal entries.\
\
This is useful for parameterizing positive definite matrices in terms of their Cholesky factorization.\
\
_class_ torch.distributions.transforms.PositiveDefiniteTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L1056)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.PositiveDefiniteTransform "Link to this definition")\
\
Transform from unconstrained matrices to positive-definite matrices.\
\
_class_ torch.distributions.transforms.PowerTransform(_exponent_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L594)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.PowerTransform "Link to this definition")\
\
Transform via the mapping y\=xexponenty = x^{\\text{exponent}}y\=xexponent.\
\
_class_ torch.distributions.transforms.ReshapeTransform(_in\_shape_, _out\_shape_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L495)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.ReshapeTransform "Link to this definition")\
\
Unit Jacobian transform to reshape the rightmost part of a tensor.\
\
Note that `in_shape` and `out_shape` must have the same number of elements, just as for [`torch.Tensor.reshape()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape.html#torch.Tensor.reshape "torch.Tensor.reshape")\
.\
\
Parameters:\
\
*   **in\_shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
    ) – The input event shape.\
    \
*   **out\_shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")\
    ) – The output event shape.\
    \
*   **cache\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Size of cache. If zero, no caching is done. If one, the latest single value is cached. Only 0 and 1 are supported. (Default 0.)\
    \
\
_class_ torch.distributions.transforms.SigmoidTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L642)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.SigmoidTransform "Link to this definition")\
\
Transform via the mapping y\=11+exp⁡(−x)y = \\frac{1}{1 + \\exp(-x)}y\=1+exp(−x)1​ and x\=logit(y)x = \\text{logit}(y)x\=logit(y).\
\
_class_ torch.distributions.transforms.SoftplusTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L667)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.SoftplusTransform "Link to this definition")\
\
Transform via the mapping Softplus(x)\=log⁡(1+exp⁡(x))\\text{Softplus}(x) = \\log(1 + \\exp(x))Softplus(x)\=log(1+exp(x)). The implementation reverts to the linear function when x\>20x > 20x\>20.\
\
_class_ torch.distributions.transforms.TanhTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L691)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.TanhTransform "Link to this definition")\
\
Transform via the mapping y\=tanh⁡(x)y = \\tanh(x)y\=tanh(x).\
\
It is equivalent to\
\
ComposeTransform(\
    \[\
        AffineTransform(0.0, 2.0),\
        SigmoidTransform(),\
        AffineTransform(\-1.0, 2.0),\
    \]\
)\
\
Copy to clipboard\
\
However this might not be numerically stable, thus it is recommended to use TanhTransform instead.\
\
Note that one should use cache\_size=1 when it comes to NaN/Inf values.\
\
_class_ torch.distributions.transforms.SoftmaxTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L942)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.SoftmaxTransform "Link to this definition")\
\
Transform from unconstrained space to the simplex via y\=exp⁡(x)y = \\exp(x)y\=exp(x) then normalizing.\
\
This is not bijective and cannot be used for HMC. However this acts mostly coordinate-wise (except for the final normalization), and thus is appropriate for coordinate-wise optimization algorithms.\
\
_class_ torch.distributions.transforms.StackTransform(_tseq_, _dim\=0_, _cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L1218)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.StackTransform "Link to this definition")\
\
Transform functor that applies a sequence of transforms tseq component-wise to each submatrix at dim in a way compatible with [`torch.stack()`](https://docs.pytorch.org/docs/2.15/generated/torch.stack.html#torch.stack "torch.stack")\
.\
\
Example:\
\
x \= torch.stack(\[torch.range(1, 10), torch.range(1, 10)\], dim\=1)\
t \= StackTransform(\[ExpTransform(), identity\_transform\], dim\=1)\
y \= t(x)\
\
Copy to clipboard\
\
_class_ torch.distributions.transforms.StickBreakingTransform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L978)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.StickBreakingTransform "Link to this definition")\
\
Transform from unconstrained space to the simplex of one additional dimension via a stick-breaking process.\
\
This transform arises as an iterated sigmoid transform in a stick-breaking construction of the Dirichlet distribution: the first logit is transformed via sigmoid to the first probability and the probability of everything else, and then the process recurses.\
\
This is bijective and appropriate for use in HMC; however it mixes coordinates together and is less appropriate for optimization.\
\
_class_ torch.distributions.transforms.Transform(_cache\_size\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L47)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "Link to this definition")\
\
Abstract class for invertible transformations with computable log det jacobians. They are primarily used in `torch.distributions.TransformedDistribution`.\
\
Caching is useful for transforms whose inverses are either expensive or numerically unstable. Note that care must be taken with memoized values since the autograd graph may be reversed. For example while the following works with or without caching:\
\
y \= t(x)\
t.log\_abs\_det\_jacobian(x, y).backward()  \# x will receive gradients.\
\
Copy to clipboard\
\
However the following will error when caching due to dependency reversal:\
\
y \= t(x)\
z \= t.inv(y)\
grad(z.sum(), \[y\])  \# error because z is x\
\
Copy to clipboard\
\
Derived classes should implement one or both of `_call()` or `_inverse()`. Derived classes that set bijective=True should also implement [`log_abs_det_jacobian()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.log_abs_det_jacobian "torch.distributions.transforms.Transform.log_abs_det_jacobian")\
.\
\
Parameters:\
\
**cache\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
) – Size of cache. If zero, no caching is done. If one, the latest single value is cached. Only 0 and 1 are supported.\
\
Variables:\
\
*   **domain** ([`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
    ) – The constraint representing valid inputs to this transform.\
    \
*   **codomain** ([`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
    ) – The constraint representing valid outputs to this transform which are inputs to the inverse transform.\
    \
*   **bijective** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether this transform is bijective. A transform `t` is bijective iff `t.inv(t(x)) == x` and `t(t.inv(y)) == y` for every `x` in the domain and `y` in the codomain. Transforms that are not bijective should at least maintain the weaker pseudoinverse properties `t(t.inv(t(x)) == t(x)` and `t.inv(t(t.inv(y))) == t.inv(y)`.\
    \
*   **sign** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – For bijective univariate transforms, this should be +1 or -1 depending on whether transform is monotone increasing or decreasing.\
    \
\
_property_ inv_: [Transform](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.inv "Link to this definition")\
\
Returns the inverse [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
 of this transform. This should satisfy `t.inv.inv is t`.\
\
_property_ sign_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.sign "Link to this definition")\
\
Returns the sign of the determinant of the Jacobian, if applicable. In general this only makes sense for bijective transforms.\
\
log\_abs\_det\_jacobian(_x_, _y_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L190)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.log_abs_det_jacobian "Link to this definition")\
\
Computes the log det jacobian log |dy/dx| given input and output.\
\
forward\_shape(_shape_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L199)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.forward_shape "Link to this definition")\
\
Infers the shape of the forward computation, given the input shape. Defaults to preserving shape.\
\
inverse\_shape(_shape_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/transforms.py#L206)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform.inverse_shape "Link to this definition")\
\
Infers the shapes of the inverse computation, given the output shape. Defaults to preserving shape.\
\
|     |     |\
| --- | --- |\
| [`identity_transform`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.transforms.identity_transform.html#torch.distributions.transforms.identity_transform "torch.distributions.transforms.identity_transform") | Composes multiple transforms in a chain. |\
\
`Constraints`[#](https://docs.pytorch.org/docs/2.15/distributions.html#module-torch.distributions.constraints "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------\
\
_class_ torch.distributions.constraints.Constraint[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L80)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "Link to this definition")\
\
Abstract base class for constraints.\
\
A constraint object represents a region over which a variable is valid, e.g. within which a variable can be optimized.\
\
Variables:\
\
*   **is\_discrete** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether constrained space is discrete. Defaults to False.\
    \
*   **event\_dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Number of rightmost dimensions that together define an event. The [`check()`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint.check "torch.distributions.constraints.Constraint.check")\
     method will remove this many dimensions when computing validity.\
    \
\
check(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L98)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint.check "Link to this definition")\
\
Returns a byte tensor of `sample_shape + batch_shape` indicating whether each event in value satisfies this constraint.\
\
torch.distributions.constraints.cat[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L653)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.cat "Link to this definition")\
\
alias of `_Cat`\
\
torch.distributions.constraints.dependent\_property[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L182)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.dependent_property "Link to this definition")\
\
alias of `_DependentProperty`\
\
torch.distributions.constraints.greater\_than[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L428)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.greater_than "Link to this definition")\
\
alias of `_GreaterThan`\
\
torch.distributions.constraints.greater\_than\_eq[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L446)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.greater_than_eq "Link to this definition")\
\
alias of `_GreaterThanEq`\
\
torch.distributions.constraints.independent[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L231)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.independent "Link to this definition")\
\
alias of `_IndependentConstraint`\
\
torch.distributions.constraints.integer\_interval[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L354)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.integer_interval "Link to this definition")\
\
alias of `_IntegerInterval`\
\
torch.distributions.constraints.interval[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L482)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.interval "Link to this definition")\
\
alias of `_Interval`\
\
torch.distributions.constraints.half\_open\_interval[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L503)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.half_open_interval "Link to this definition")\
\
alias of `_HalfOpenInterval`\
\
torch.distributions.constraints.is\_dependent(_constraint_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L156)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.is_dependent "Link to this definition")\
\
Checks if `constraint` is a `_Dependent` object.\
\
Parameters:\
\
**constraint** – A `Constraint` object.\
\
Returns:\
\
True if `constraint` can be refined to the type `_Dependent`, False otherwise.\
\
Return type:\
\
`bool`\
\
Examples\
\
\>>> import torch\
\>>> from torch.distributions import Bernoulli\
\>>> from torch.distributions.constraints import is\_dependent\
\
Copy to clipboard\
\
\>>> dist \= Bernoulli(probs\=torch.tensor(\[0.6\], requires\_grad\=True))\
\>>> constraint1 \= dist.arg\_constraints\["probs"\]\
\>>> constraint2 \= dist.arg\_constraints\["logits"\]\
\
Copy to clipboard\
\
\>>> for constraint in \[constraint1, constraint2\]:\
\>>>     if is\_dependent(constraint):\
\>>>         continue\
\
Copy to clipboard\
\
torch.distributions.constraints.less\_than[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L464)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.less_than "Link to this definition")\
\
alias of `_LessThan`\
\
_class_ torch.distributions.constraints.MixtureSameFamilyConstraint(_base\_constraint_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L280)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.MixtureSameFamilyConstraint "Link to this definition")\
\
Constraint for the `MixtureSameFamily` distribution that adds back the rightmost batch dimension before performing the validity check with the component distribution constraint.\
\
Parameters:\
\
**base\_constraint** – The `Constraint` object of the component distribution of the `MixtureSameFamily` distribution.\
\
check(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L309)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.MixtureSameFamilyConstraint.check "Link to this definition")\
\
Check validity of `value` as a possible outcome of sampling the `MixtureSameFamily` distribution.\
\
torch.distributions.constraints.multinomial[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L536)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.multinomial "Link to this definition")\
\
alias of `_Multinomial`\
\
torch.distributions.constraints.stack[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraints.py#L696)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.stack "Link to this definition")\
\
alias of `_Stack`\
\
|     |     |\
| --- | --- |\
| [`dependent`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.constraints.dependent.html#torch.distributions.constraints.dependent "torch.distributions.constraints.dependent") | Placeholder for variables whose support depends on other variables. |\
\
`Constraint Registry`[#](https://docs.pytorch.org/docs/2.15/distributions.html#module-torch.distributions.constraint_registry "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------\
\
PyTorch provides two global [`ConstraintRegistry`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraint_registry.ConstraintRegistry "torch.distributions.constraint_registry.ConstraintRegistry")\
 objects that link [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
 objects to [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
 objects. These objects both input constraints and return transforms, but they have different guarantees on bijectivity.\
\
1.  `biject_to(constraint)` looks up a bijective [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
     from `constraints.real` to the given `constraint`. The returned transform is guaranteed to have `.bijective = True` and should implement `.log_abs_det_jacobian()`.\
    \
2.  `transform_to(constraint)` looks up a not-necessarily bijective [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
     from `constraints.real` to the given `constraint`. The returned transform is not guaranteed to implement `.log_abs_det_jacobian()`.\
    \
\
The `transform_to()` registry is useful for performing unconstrained optimization on constrained parameters of probability distributions, which are indicated by each distribution’s `.arg_constraints` dict. These transforms often overparameterize a space in order to avoid rotation; they are thus more suitable for coordinate-wise optimization algorithms like Adam:\
\
loc \= torch.zeros(100, requires\_grad\=True)\
unconstrained \= torch.zeros(100, requires\_grad\=True)\
scale \= transform\_to(Normal.arg\_constraints\["scale"\])(unconstrained)\
loss \= \-Normal(loc, scale).log\_prob(data).sum()\
\
Copy to clipboard\
\
The `biject_to()` registry is useful for Hamiltonian Monte Carlo, where samples from a probability distribution with constrained `.support` are propagated in an unconstrained space, and algorithms are typically rotation invariant.:\
\
dist \= Exponential(rate)\
unconstrained \= torch.zeros(100, requires\_grad\=True)\
sample \= biject\_to(dist.support)(unconstrained)\
potential\_energy \= \-dist.log\_prob(sample).sum()\
\
Copy to clipboard\
\
Note\
\
An example where `transform_to` and `biject_to` differ is `constraints.simplex`: `transform_to(constraints.simplex)` returns a [`SoftmaxTransform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.SoftmaxTransform "torch.distributions.transforms.SoftmaxTransform")\
 that simply exponentiates and normalizes its inputs; this is a cheap and mostly coordinate-wise operation appropriate for algorithms like SVI. In contrast, `biject_to(constraints.simplex)` returns a [`StickBreakingTransform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.StickBreakingTransform "torch.distributions.transforms.StickBreakingTransform")\
 that bijects its input down to a one-fewer-dimensional space; this is a more expensive less numerically stable transform but is needed for algorithms like HMC.\
\
The `biject_to` and `transform_to` objects can be extended by user-defined constraints and transforms using their `.register()` method either as a function on singleton constraints:\
\
transform\_to.register(my\_constraint, my\_transform)\
\
Copy to clipboard\
\
or as a decorator on parameterized constraints:\
\
@transform\_to.register(MyConstraintClass)\
def my\_factory(constraint):\
    assert isinstance(constraint, MyConstraintClass)\
    return MyTransform(constraint.param1, constraint.param2)\
\
Copy to clipboard\
\
You can create your own registry by creating a new [`ConstraintRegistry`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraint_registry.ConstraintRegistry "torch.distributions.constraint_registry.ConstraintRegistry")\
 object.\
\
_class_ torch.distributions.constraint\_registry.ConstraintRegistry[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraint_registry.py#L80)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraint_registry.ConstraintRegistry "Link to this definition")\
\
Registry to link constraints to transforms.\
\
register(_constraint_, _factory\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributions/constraint_registry.py#L89)\
[#](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraint_registry.ConstraintRegistry.register "Link to this definition")\
\
Registers a [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
 subclass in this registry. Usage:\
\
@my\_registry.register(MyConstraintClass)\
def construct\_transform(constraint):\
    assert isinstance(constraint, MyConstraint)\
    return MyTransform(constraint.arg\_constraints)\
\
Copy to clipboard\
\
Parameters:\
\
*   **constraint** (subclass of [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
    ) – A subclass of [`Constraint`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.constraints.Constraint "torch.distributions.constraints.Constraint")\
    , or a singleton object of the desired class.\
    \
*   **factory** (_Callable_) – A callable that inputs a constraint object and returns a [`Transform`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.transforms.Transform "torch.distributions.transforms.Transform")\
     object.\
    \
\
|     |     |\
| --- | --- |\
| [`biject_to`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.constraint_registry.biject_to.html#torch.distributions.constraint_registry.biject_to "torch.distributions.constraint_registry.biject_to") | Registry to link constraints to transforms. |\
| [`transform_to`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.constraint_registry.transform_to.html#torch.distributions.constraint_registry.transform_to "torch.distributions.constraint_registry.transform_to") | Registry to link constraints to transforms. |\
\
|     |     |\
| --- | --- |\
| [`broadcast_all`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.broadcast_all.html#torch.distributions.utils.broadcast_all "torch.distributions.utils.broadcast_all") | Given a list of values (possibly containing numbers), returns a list where each value is broadcasted based on the following rules: |\
| [`clamp_probs`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.clamp_probs.html#torch.distributions.utils.clamp_probs "torch.distributions.utils.clamp_probs") | Clamps the probabilities to be in the open interval (0, 1). |\
| [`logits_to_probs`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.logits_to_probs.html#torch.distributions.utils.logits_to_probs "torch.distributions.utils.logits_to_probs") | Converts a tensor of logits into probabilities. |\
| [`probs_to_logits`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.probs_to_logits.html#torch.distributions.utils.probs_to_logits "torch.distributions.utils.probs_to_logits") | Converts a tensor of probabilities into logits. |\
| [`tril_matrix_to_vec`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.tril_matrix_to_vec.html#torch.distributions.utils.tril_matrix_to_vec "torch.distributions.utils.tril_matrix_to_vec") | Convert a D x D matrix or a batch of matrices into a (batched) vector which comprises lower triangular elements from the matrix in row order. |\
| [`vec_to_tril_matrix`](https://docs.pytorch.org/docs/2.15/generated/torch.distributions.utils.vec_to_tril_matrix.html#torch.distributions.utils.vec_to_tril_matrix "torch.distributions.utils.vec_to_tril_matrix") | Convert a vector or a batch of vectors into a batched D x D lower triangular matrix containing elements from the vector in row order. |\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributions.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributions.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |