Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/optim.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/optim.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/optim.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/optim.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/optim.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/optim.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/optim.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/optim.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/optim.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/optim.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/optim.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/optim.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/optim.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/optim.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/optim.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/optim.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/optim.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/optim.html)
[v1.13](https://docs.pytorch.org/docs/1.13/optim.html)
[v1.12](https://docs.pytorch.org/docs/1.12/optim.html)
[v1.11](https://docs.pytorch.org/docs/1.11/optim.html)
[v1.10](https://docs.pytorch.org/docs/1.10/optim.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/optim.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/optim.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/optim.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/optim.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/optim.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/optim.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/optim.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/optim.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/optim.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/optim.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/optim.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/optim.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/optim.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/optim.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/optim.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/optim.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/optim.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/optim.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/optim.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/optim.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/optim.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/optim.html)

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

torch.optim[#](https://docs.pytorch.org/docs/2.15/optim.html#module-torch.optim "Link to this heading")

========================================================================================================

Created On: Jun 13, 2025 | Last Updated On: Aug 27, 2026

[`torch.optim`](https://docs.pytorch.org/docs/2.15/optim.html#module-torch.optim "torch.optim")
 is a package implementing various optimization algorithms.

Most commonly used methods are already supported, and the interface is general enough, so that more sophisticated ones can also be easily integrated in the future.

How to use an optimizer[#](https://docs.pytorch.org/docs/2.15/optim.html#how-to-use-an-optimizer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

To use [`torch.optim`](https://docs.pytorch.org/docs/2.15/optim.html#module-torch.optim "torch.optim")
 you have to construct an optimizer object that will hold the current state and will update the parameters based on the computed gradients.

### Constructing it[#](https://docs.pytorch.org/docs/2.15/optim.html#constructing-it "Link to this heading")

To construct an [`Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 you have to give it an iterable containing the parameters (all should be `Parameter` s) or named parameters (tuples of (str, `Parameter`)) to optimize. Then, you can specify optimizer-specific options such as the learning rate, weight decay, etc.

Example:

optimizer \= optim.SGD(model.parameters(), lr\=0.01, momentum\=0.9)
optimizer \= optim.Adam(\[var1, var2\], lr\=0.0001)

Copy to clipboard

Named parameters example:

optimizer \= optim.SGD(model.named\_parameters(), lr\=0.01, momentum\=0.9)
optimizer \= optim.Adam(\[('layer0', var1), ('layer1', var2)\], lr\=0.0001)

Copy to clipboard

### Per-parameter options[#](https://docs.pytorch.org/docs/2.15/optim.html#per-parameter-options "Link to this heading")

[`Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 s also support specifying per-parameter options. To do this, instead of passing an iterable of `Variable` s, pass in an iterable of [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
 s. Each of them will define a separate parameter group, and should contain a `params` key, containing a list of parameters belonging to it. Other keys should match the keyword arguments accepted by the optimizers, and will be used as optimization options for this group.

For example, this is very useful when one wants to specify per-layer learning rates:

optim.SGD(\[\
    {'params': model.base.parameters(), 'lr': 1e-2},\
    {'params': model.classifier.parameters()}\
\], lr\=1e-3, momentum\=0.9)

optim.SGD(\[\
    {'params': model.base.named\_parameters(), 'lr': 1e-2},\
    {'params': model.classifier.named\_parameters()}\
\], lr\=1e-3, momentum\=0.9)

Copy to clipboard

This means that `model.base`’s parameters will use a learning rate of `1e-2`, whereas `model.classifier`’s parameters will stick to the default learning rate of `1e-3`. Finally a momentum of `0.9` will be used for all parameters.

Note

You can still pass options as keyword arguments. They will be used as defaults, in the groups that didn’t override them. This is useful when you only want to vary a single option, while keeping all others consistent between parameter groups.

Also consider the following example related to the distinct penalization of parameters. Remember that [`parameters()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.parameters "torch.nn.Module.parameters")
 returns an iterable that contains all learnable parameters, including biases and other parameters that may prefer distinct penalization. To address this, one can specify individual penalization weights for each parameter group:

bias\_params \= \[p for name, p in self.named\_parameters() if 'bias' in name\]
others \= \[p for name, p in self.named\_parameters() if 'bias' not in name\]

optim.SGD(\[\
    {'params': others},\
    {'params': bias\_params, 'weight\_decay': 0}\
\], weight\_decay\=1e-2, lr\=1e-2)

Copy to clipboard

In this manner, bias terms are isolated from non-bias terms, and a `weight_decay` of `0` is set specifically for the bias terms, as to avoid any penalization for this group.

### Taking an optimization step[#](https://docs.pytorch.org/docs/2.15/optim.html#taking-an-optimization-step "Link to this heading")

All optimizers implement a [`step()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step "torch.optim.Optimizer.step")
 method, that updates the parameters. It can be used in two ways:

#### `optimizer.step()`[#](https://docs.pytorch.org/docs/2.15/optim.html#optimizer-step "Link to this heading")

This is a simplified version supported by most optimizers. The function can be called once the gradients are computed using e.g. `backward()`.

Example:

for input, target in dataset:
    optimizer.zero\_grad()
    output \= model(input)
    loss \= loss\_fn(output, target)
    loss.backward()
    optimizer.step()

Copy to clipboard

#### `optimizer.step(closure)`[#](https://docs.pytorch.org/docs/2.15/optim.html#optimizer-step-closure "Link to this heading")

Some optimization algorithms such as Conjugate Gradient and LBFGS need to reevaluate the function multiple times, so you have to pass in a closure that allows them to recompute your model. The closure should clear the gradients, compute the loss, and return it.

Example:

for input, target in dataset:
    def closure():
        optimizer.zero\_grad()
        output \= model(input)
        loss \= loss\_fn(output, target)
        loss.backward()
        return loss
    optimizer.step(closure)

Copy to clipboard

Base class[#](https://docs.pytorch.org/docs/2.15/optim.html#base-class "Link to this heading")

-----------------------------------------------------------------------------------------------

_class_ torch.optim.Optimizer(_params_, _defaults_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/optimizer.py#L368)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "Link to this definition")

Base class for all optimizers.

Warning

Parameters need to be specified as collections that have a deterministic ordering that is consistent between runs. Examples of objects that don’t satisfy those properties are sets and iterators over values of dictionaries.

Parameters:

*   **params** (_iterable_) – an iterable of [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     s or [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
     s. Specifies what Tensors should be optimized.
    
*   **defaults** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – (dict): a dict containing default values of optimization options (used when a parameter group doesn’t specify them).
    

|     |     |
| --- | --- |
| [`Optimizer.add_param_group`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.add_param_group.html#torch.optim.Optimizer.add_param_group "torch.optim.Optimizer.add_param_group") | Add a param group to the [`Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")<br> s param\_groups. |
| [`Optimizer.load_state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict "torch.optim.Optimizer.load_state_dict") | Load the optimizer state. |
| [`Optimizer.register_load_state_dict_pre_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_load_state_dict_pre_hook.html#torch.optim.Optimizer.register_load_state_dict_pre_hook "torch.optim.Optimizer.register_load_state_dict_pre_hook") | Register a load\_state\_dict pre-hook which will be called before [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict "torch.optim.Optimizer.load_state_dict")<br> is called. It should have the following signature::. |
| [`Optimizer.register_load_state_dict_post_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_load_state_dict_post_hook.html#torch.optim.Optimizer.register_load_state_dict_post_hook "torch.optim.Optimizer.register_load_state_dict_post_hook") | Register a load\_state\_dict post-hook which will be called after [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict "torch.optim.Optimizer.load_state_dict")<br> is called. It should have the following signature::. |
| [`Optimizer.state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict "torch.optim.Optimizer.state_dict") | Return the state of the optimizer as a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")<br>. |
| [`Optimizer.register_state_dict_pre_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_state_dict_pre_hook.html#torch.optim.Optimizer.register_state_dict_pre_hook "torch.optim.Optimizer.register_state_dict_pre_hook") | Register a state dict pre-hook which will be called before [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict "torch.optim.Optimizer.state_dict")<br> is called. |
| [`Optimizer.register_state_dict_post_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_state_dict_post_hook.html#torch.optim.Optimizer.register_state_dict_post_hook "torch.optim.Optimizer.register_state_dict_post_hook") | Register a state dict post-hook which will be called after [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict "torch.optim.Optimizer.state_dict")<br> is called. |
| [`Optimizer.step`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step "torch.optim.Optimizer.step") | Perform a single optimization step to update parameter. |
| [`Optimizer.register_step_pre_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_step_pre_hook.html#torch.optim.Optimizer.register_step_pre_hook "torch.optim.Optimizer.register_step_pre_hook") | Register an optimizer step pre hook which will be called before optimizer step. |
| [`Optimizer.register_step_post_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_step_post_hook.html#torch.optim.Optimizer.register_step_post_hook "torch.optim.Optimizer.register_step_post_hook") | Register an optimizer step post hook which will be called after optimizer step. |
| [`Optimizer.zero_grad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "torch.optim.Optimizer.zero_grad") | Reset the gradients of all optimized [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")<br> s. |

Algorithms[#](https://docs.pytorch.org/docs/2.15/optim.html#algorithms "Link to this heading")

-----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adadelta.html#torch.optim.Adadelta "torch.optim.Adadelta") | Implements Adadelta algorithm. |
| [`Adafactor`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adafactor.html#torch.optim.Adafactor "torch.optim.Adafactor") | Implements Adafactor algorithm. |
| [`Adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adagrad.html#torch.optim.Adagrad "torch.optim.Adagrad") | Implements Adagrad algorithm. |
| [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html#torch.optim.Adam "torch.optim.Adam") | Implements Adam algorithm. |
| [`AdamW`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.AdamW.html#torch.optim.AdamW "torch.optim.AdamW") | Implements AdamW algorithm, where weight decay does not accumulate in the momentum nor variance. |
| [`SparseAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam "torch.optim.SparseAdam") | SparseAdam implements a masked version of the Adam algorithm suitable for sparse gradients. |
| [`Adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adamax.html#torch.optim.Adamax "torch.optim.Adamax") | Implements Adamax algorithm (a variant of Adam based on infinity norm). |
| [`ASGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.ASGD.html#torch.optim.ASGD "torch.optim.ASGD") | Implements Averaged Stochastic Gradient Descent. |
| [`LBFGS`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.LBFGS.html#torch.optim.LBFGS "torch.optim.LBFGS") | Implements L-BFGS algorithm. |
| [`Muon`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Muon.html#torch.optim.Muon "torch.optim.Muon") | Implements Muon algorithm. |
| [`NAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.NAdam.html#torch.optim.NAdam "torch.optim.NAdam") | Implements NAdam algorithm. |
| [`RAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RAdam.html#torch.optim.RAdam "torch.optim.RAdam") | Implements RAdam algorithm. |
| [`RMSprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RMSprop.html#torch.optim.RMSprop "torch.optim.RMSprop") | Implements RMSprop algorithm. |
| [`Rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Rprop.html#torch.optim.Rprop "torch.optim.Rprop") | Implements the resilient backpropagation algorithm. |
| [`SGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SGD.html#torch.optim.SGD "torch.optim.SGD") | Implements stochastic gradient descent (optionally with momentum). |

Many of our algorithms have various implementations optimized for performance, readability and/or generality, so we attempt to default to the generally fastest implementation for the current device if no particular implementation has been specified by the user.

We have 3 major categories of implementations: for-loop, foreach (multi-tensor), and fused. The most straightforward implementations are for-loops over the parameters with big chunks of computation. For-looping is usually slower than our foreach implementations, which combine parameters into a multi-tensor and run the big chunks of computation all at once, thereby saving many sequential kernel calls. A few of our optimizers have even faster fused implementations, which fuse the big chunks of computation into one kernel. We can think of foreach implementations as fusing horizontally and fused implementations as fusing vertically on top of that.

In general, the performance ordering of the 3 implementations is fused > foreach > for-loop. So when applicable, we default to foreach over for-loop. Applicable means the foreach implementation is available, the user has not specified any implementation-specific kwargs (e.g., fused, foreach, differentiable), and all tensors are native. Note that while fused should be even faster than foreach, the implementations are newer and we would like to give them more bake-in time before flipping the switch everywhere. We summarize the stability status for each implementation on the second table below, you are welcome to try them out though!

Below is a table showing the available and default implementations of each algorithm:

   
| Algorithm | Default | Has foreach? | Has fused? |
| --- | --- | --- | --- |
| [`Adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adadelta.html#torch.optim.Adadelta "torch.optim.Adadelta") | foreach | yes | no  |
| [`Adafactor`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adafactor.html#torch.optim.Adafactor "torch.optim.Adafactor") | for-loop | no  | no  |
| [`Adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adagrad.html#torch.optim.Adagrad "torch.optim.Adagrad") | foreach | yes | yes (cpu only) |
| [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html#torch.optim.Adam "torch.optim.Adam") | foreach | yes | yes |
| [`AdamW`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.AdamW.html#torch.optim.AdamW "torch.optim.AdamW") | foreach | yes | yes |
| [`SparseAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam "torch.optim.SparseAdam") | for-loop | no  | no  |
| [`Adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adamax.html#torch.optim.Adamax "torch.optim.Adamax") | foreach | yes | no  |
| [`ASGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.ASGD.html#torch.optim.ASGD "torch.optim.ASGD") | foreach | yes | no  |
| [`LBFGS`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.LBFGS.html#torch.optim.LBFGS "torch.optim.LBFGS") | for-loop | no  | no  |
| [`Muon`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Muon.html#torch.optim.Muon "torch.optim.Muon") | for-loop | no  | no  |
| [`NAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.NAdam.html#torch.optim.NAdam "torch.optim.NAdam") | foreach | yes | no  |
| [`RAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RAdam.html#torch.optim.RAdam "torch.optim.RAdam") | foreach | yes | no  |
| [`RMSprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RMSprop.html#torch.optim.RMSprop "torch.optim.RMSprop") | foreach | yes | no  |
| [`Rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Rprop.html#torch.optim.Rprop "torch.optim.Rprop") | foreach | yes | no  |
| [`SGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SGD.html#torch.optim.SGD "torch.optim.SGD") | foreach | yes | yes |

Below table is showing the stability status for fused implementations:

   
| Algorithm | CPU | CUDA | MPS |
| --- | --- | --- | --- |
| [`Adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adadelta.html#torch.optim.Adadelta "torch.optim.Adadelta") | unsupported | unsupported | unsupported |
| [`Adafactor`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adafactor.html#torch.optim.Adafactor "torch.optim.Adafactor") | unsupported | unsupported | unsupported |
| [`Adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adagrad.html#torch.optim.Adagrad "torch.optim.Adagrad") | beta | unsupported | unsupported |
| [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html#torch.optim.Adam "torch.optim.Adam") | beta | stable | beta |
| [`AdamW`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.AdamW.html#torch.optim.AdamW "torch.optim.AdamW") | beta | stable | beta |
| [`SparseAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam "torch.optim.SparseAdam") | unsupported | unsupported | unsupported |
| [`Adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adamax.html#torch.optim.Adamax "torch.optim.Adamax") | unsupported | unsupported | unsupported |
| [`ASGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.ASGD.html#torch.optim.ASGD "torch.optim.ASGD") | unsupported | unsupported | unsupported |
| [`LBFGS`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.LBFGS.html#torch.optim.LBFGS "torch.optim.LBFGS") | unsupported | unsupported | unsupported |
| [`Muon`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Muon.html#torch.optim.Muon "torch.optim.Muon") | unsupported | unsupported | unsupported |
| [`NAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.NAdam.html#torch.optim.NAdam "torch.optim.NAdam") | unsupported | unsupported | unsupported |
| [`RAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RAdam.html#torch.optim.RAdam "torch.optim.RAdam") | unsupported | unsupported | unsupported |
| [`RMSprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RMSprop.html#torch.optim.RMSprop "torch.optim.RMSprop") | unsupported | unsupported | unsupported |
| [`Rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Rprop.html#torch.optim.Rprop "torch.optim.Rprop") | unsupported | unsupported | unsupported |
| [`SGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SGD.html#torch.optim.SGD "torch.optim.SGD") | beta | beta | beta |

Functional optimizer API[#](https://docs.pytorch.org/docs/2.15/optim.html#functional-optimizer-api "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Optimizer classes are the recommended interface for most use cases: they own optimizer state, read gradients from parameter `.grad` attributes, organize parameter groups, and provide state-dict integration. The module-level functional optimizer APIs are lower-level building blocks for cases where one may want to control those details explicitly. For example, a distributed training system may apply an update as soon as a gradient becomes available, or a caller may choose a different storage dtype for optimizer state to save memory.

Functional optimizer calls update parameters and state tensors according to the respective algorithm in place; they are not pure functions and do not initialize optimizer state. Call them under [`torch.no_grad`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")
 unless intentionally constructing a differentiable update with an API that supports `differentiable=True`. Each tensor list is positional, so entries at the same index must correspond to the same parameter.

The caller has full control and responsibility for creating and retaining state, filtering parameters without gradients from every list consistently, and saving and restoring that state. Most APIs receive step counters as singleton tensors and update them in place, except [`torch.optim.functional.sparse_adam()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.sparse_adam.html#torch.optim.functional.sparse_adam "torch.optim.functional.sparse_adam")
 which has step represented by a Python number.

The public functional optimizer APIs are exposed uniformly from [`torch.optim.functional`](https://docs.pytorch.org/docs/2.15/optim.functional.html#module-torch.optim.functional "torch.optim.functional")
:

| Optimizer | Functional API |
| --- | --- |
| [`Adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adadelta.html#torch.optim.Adadelta "torch.optim.Adadelta") | [`torch.optim.functional.adadelta()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adadelta.html#torch.optim.functional.adadelta "torch.optim.functional.adadelta") |
| [`Adafactor`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adafactor.html#torch.optim.Adafactor "torch.optim.Adafactor") | [`torch.optim.functional.adafactor()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adafactor.html#torch.optim.functional.adafactor "torch.optim.functional.adafactor") |
| [`Adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adagrad.html#torch.optim.Adagrad "torch.optim.Adagrad") | [`torch.optim.functional.adagrad()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adagrad.html#torch.optim.functional.adagrad "torch.optim.functional.adagrad") |
| [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html#torch.optim.Adam "torch.optim.Adam") | [`torch.optim.functional.adam()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html#torch.optim.functional.adam "torch.optim.functional.adam") |
| [`Adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adamax.html#torch.optim.Adamax "torch.optim.Adamax") | [`torch.optim.functional.adamax()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adamax.html#torch.optim.functional.adamax "torch.optim.functional.adamax") |
| [`AdamW`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.AdamW.html#torch.optim.AdamW "torch.optim.AdamW") | [`torch.optim.functional.adamw()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adamw.html#torch.optim.functional.adamw "torch.optim.functional.adamw") |
| [`ASGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.ASGD.html#torch.optim.ASGD "torch.optim.ASGD") | [`torch.optim.functional.asgd()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.asgd.html#torch.optim.functional.asgd "torch.optim.functional.asgd") |
| [`Muon`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Muon.html#torch.optim.Muon "torch.optim.Muon") | [`torch.optim.functional.muon()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.muon.html#torch.optim.functional.muon "torch.optim.functional.muon") |
| [`NAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.NAdam.html#torch.optim.NAdam "torch.optim.NAdam") | [`torch.optim.functional.nadam()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.nadam.html#torch.optim.functional.nadam "torch.optim.functional.nadam") |
| [`RAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RAdam.html#torch.optim.RAdam "torch.optim.RAdam") | [`torch.optim.functional.radam()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.radam.html#torch.optim.functional.radam "torch.optim.functional.radam") |
| [`RMSprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.RMSprop.html#torch.optim.RMSprop "torch.optim.RMSprop") | [`torch.optim.functional.rmsprop()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.rmsprop.html#torch.optim.functional.rmsprop "torch.optim.functional.rmsprop") |
| [`Rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Rprop.html#torch.optim.Rprop "torch.optim.Rprop") | [`torch.optim.functional.rprop()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.rprop.html#torch.optim.functional.rprop "torch.optim.functional.rprop") |
| [`SGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SGD.html#torch.optim.SGD "torch.optim.SGD") | [`torch.optim.functional.sgd()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.sgd.html#torch.optim.functional.sgd "torch.optim.functional.sgd") |
| [`SparseAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam "torch.optim.SparseAdam") | [`torch.optim.functional.sparse_adam()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.sparse_adam.html#torch.optim.functional.sparse_adam "torch.optim.functional.sparse_adam") |

[`LBFGS`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.LBFGS.html#torch.optim.LBFGS "torch.optim.LBFGS")
 does not currently expose a functional API. Its update is coupled to repeated closure evaluations and optional line-search orchestration, rather than implemented as a standalone functional kernel.

### AdamW with BF16 optimizer state[#](https://docs.pytorch.org/docs/2.15/optim.html#adamw-with-bf16-optimizer-state "Link to this heading")

One use of the functional API is storing optimizer state in a lower precision dtype to save memory, for example storing AdamW’s first- and second-moment buffers in BF16 while keeping parameters and gradients in FP32. As seen in DeepSeek-V3, this optimization halves the memory occupied by the two moment buffers. In particular, PyTorch’s fused CUDA implementations for Adam and AdamW supports loading the BF16 moments, performing the update in FP32, and storing the updated moments back in BF16. This can be combined with BF16 autocast for forward and backward while the stored model parameters remain FP32.

The following example keeps the optimizer state outside an [`Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 and applies the functional update after backward:

import torch
from torch.optim.functional import adamw

model \= torch.nn.Linear(16, 4, device\="cuda", dtype\=torch.float32)
params \= list(model.parameters())
state \= \[\
    {\
        "step": torch.zeros((), device\=p.device, dtype\=torch.float32),\
        "exp\_avg": torch.zeros\_like(p, dtype\=torch.bfloat16),\
        "exp\_avg\_sq": torch.zeros\_like(p, dtype\=torch.bfloat16),\
    }\
    for p in params\
\]

@torch.no\_grad()
def functional\_adamw\_step():
    active \= \[\
        (p, p\_state)\
        for p, p\_state in zip(params, state, strict\=True)\
        if p.grad is not None\
    \]
    if not active:
        return

    adamw(
        params\=\[p for p, \_ in active\],
        grads\=\[p.grad for p, \_ in active\],
        exp\_avgs\=\[p\_state\["exp\_avg"\] for \_, p\_state in active\],
        exp\_avg\_sqs\=\[p\_state\["exp\_avg\_sq"\] for \_, p\_state in active\],
        max\_exp\_avg\_sqs\=\[\],
        state\_steps\=\[p\_state\["step"\] for \_, p\_state in active\],
        fused\=True,
        amsgrad\=False,
        beta1\=0.9,
        beta2\=0.999,
        lr\=1e-3,
        weight\_decay\=1e-2,
        eps\=1e-8,
        maximize\=False,
    )

inputs \= torch.randn(8, 16, device\="cuda")
with torch.autocast("cuda", dtype\=torch.bfloat16):
    loss \= model(inputs).square().mean()
loss.backward()
functional\_adamw\_step()
model.zero\_grad(set\_to\_none\=True)

Copy to clipboard

Note that PyTorch only currently supports this specific mixed-dtype fused CUDA path: parameters and gradients must be FP32, the moment buffers must be BF16, and the step counters must be FP32 tensors on the same device. If `amsgrad=True`, the caller must also create and pass aligned BF16 `max_exp_avg_sqs` buffers. Lower-precision moments may affect convergence, so validate the choice for the target workload.

Optimizer step hooks[#](https://docs.pytorch.org/docs/2.15/optim.html#optimizer-step-hooks "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

Optimizer [`register_step_pre_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_step_pre_hook.html#torch.optim.Optimizer.register_step_pre_hook "torch.optim.Optimizer.register_step_pre_hook")
 and [`register_step_post_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.register_step_post_hook.html#torch.optim.Optimizer.register_step_post_hook "torch.optim.Optimizer.register_step_post_hook")
 hooks are useful for observing or coordinating work around an optimizer update without taking ownership of its state. Typical uses include profiling, memory tracking, and recording events before or after the update. A pre-hook may also replace the positional and keyword arguments passed to `step()`. Use a functional optimizer API instead when customization requires directly controlling optimizer-state tensors or supplying gradients separately from parameter `.grad` attributes.

Profiler traces contain many low-level operator events, so a custom `record_function()` range gives the complete optimizer update a stable, application-level label that is easy to find and compare in the trace. Hooks add this instrumentation without modifying the training loop or optimizer implementation. The active ranges are tracked outside the optimizer, and the returned handles can remove the hooks when they are no longer needed.

import torch

parameter \= torch.nn.Parameter(torch.tensor(2.0))
optimizer \= torch.optim.SGD(\[parameter\], lr\=0.01)
active\_ranges \= {}

def begin\_optimizer\_step(optimizer, args, kwargs):
    profile\_range \= torch.profiler.record\_function("optimizer.step")
    profile\_range.\_\_enter\_\_()
    active\_ranges\[optimizer\] \= profile\_range

def end\_optimizer\_step(optimizer, args, kwargs):
    active\_ranges.pop(optimizer).\_\_exit\_\_(None, None, None)

pre\_handle \= optimizer.register\_step\_pre\_hook(begin\_optimizer\_step)
post\_handle \= optimizer.register\_step\_post\_hook(end\_optimizer\_step)

with torch.profiler.profile() as profile:
    parameter.grad \= torch.tensor(0.1)
    optimizer.step()

pre\_handle.remove()
post\_handle.remove()

print(profile.key\_averages().table())

Copy to clipboard

Use [`torch.optim.optimizer.register_optimizer_step_pre_hook()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.optimizer.register_optimizer_step_pre_hook "torch.optim.optimizer.register_optimizer_step_pre_hook")
 and [`torch.optim.optimizer.register_optimizer_step_post_hook()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.optimizer.register_optimizer_step_post_hook "torch.optim.optimizer.register_optimizer_step_post_hook")
 to register hooks that apply to every optimizer instead of one optimizer instance.

torch.optim.optimizer.register\_optimizer\_step\_post\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/optimizer.py#L338)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.optimizer.register_optimizer_step_post_hook "Link to this definition")

Register a post hook common to all optimizers.

The hook should have the following signature:

hook(optimizer, args, kwargs) \-> None

Copy to clipboard

Parameters:

**hook** (_Callable_) – A user defined hook which is registered on all optimizers.

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

torch.optim.optimizer.register\_optimizer\_step\_pre\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/optimizer.py#L318)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.optimizer.register_optimizer_step_pre_hook "Link to this definition")

Register a pre hook common to all optimizers.

The hook should have the following signature:

hook(optimizer, args, kwargs) \-> None or modified args and kwargs

Copy to clipboard

Parameters:

**hook** (_Callable_) – A user defined hook which is registered on all optimizers.

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

Utilities[#](https://docs.pytorch.org/docs/2.15/optim.html#utilities "Link to this heading")

---------------------------------------------------------------------------------------------

torch.optim.swap\_in\_optimizer\_params\_and\_state(_optimizer_, _swapin\_parameters_, _swapin\_optim\_state_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/_stateless.py#L192)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swap_in_optimizer_params_and_state "Link to this definition")

Temporarily replace an optimizer’s parameters and state with the supplied params and optim states, then restore them on exit.

For the duration of the context, all optimizer APIs (including user hooks) see the swap-in values; the live optimizer is restored on exit.

The difference between this API and `optimizer.load_state_dict` is that `optimizer.load_state_dict` only updates the optimizer’s state and leaves the parameters in `param_groups` untouched. This API also swaps in the parameters, so that `optimizer.step()` acts on the swap-in parameter tensors you supply.

Parameters:

*   **optimizer** ([_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.optimizer.Optimizer")
    ) – the live optimizer; its state must already be initialized.
    
*   **swapin\_parameters** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – tensors to use as parameters during the context, provided in the same order as the existing input parameters to the optimizer (most commonly in `model.named_parameters()` order).
    
*   **swapin\_optim\_state** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – an `optimizer.state_dict()`\-shaped dict (`{"state": ..., "param_groups": ...}`) holding the state to install. `"state"` is keyed by packed integer parameter ids and `"param_groups"` mirrors `optimizer.param_groups`, with each `"params"` entry as a list of those packed ids and the remaining keys carrying per-group hyperparameters (`lr`, `betas`, `foreach`, `capturable`, …). Only in-place tensor edits propagate back to the user supplied `swapin_optim_state`; all other side-effects (e.g., assigning a new tensor to the optim state) are ignored.
    

Example

One use of this API is to run `optimizer.step()` against `FakeTensor` versions of the parameters and state for nonstrict tracing — capturing an FX graph of the step without touching the live optimizer:

from torch.fx.experimental.proxy\_tensor import make\_fx
from torch.\_subclasses import FakeTensorMode
from torch.utils import \_pytree as pytree

fake\_mode \= FakeTensorMode(allow\_non\_fake\_inputs\=True)
with fake\_mode:
    fake\_params \= {
        n: fake\_mode.from\_tensor(p) for n, p in model.named\_parameters()
    }
    fake\_osd \= pytree.tree\_map\_only(
        torch.Tensor, fake\_mode.from\_tensor, optimizer.state\_dict()
    )

def step\_fn(params, osd):
    with swap\_in\_optimizer\_params\_and\_state(optimizer, params, osd):
        optimizer.step()
    return params, osd

gm \= make\_fx(step\_fn)(fake\_params, fake\_osd)

Copy to clipboard

How to adjust learning rate[#](https://docs.pytorch.org/docs/2.15/optim.html#how-to-adjust-learning-rate "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

[`torch.optim.lr_scheduler.LRScheduler`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler "torch.optim.lr_scheduler.LRScheduler")
 provides several methods to adjust the learning rate based on the number of epochs. [`torch.optim.lr_scheduler.ReduceLROnPlateau`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html#torch.optim.lr_scheduler.ReduceLROnPlateau "torch.optim.lr_scheduler.ReduceLROnPlateau")
 allows dynamic learning rate reducing based on some validation measurements.

Learning rate scheduling should be applied after optimizer’s update; e.g., you should write your code this way:

Example:

optimizer \= optim.SGD(model.parameters(), lr\=0.01, momentum\=0.9)
scheduler \= ExponentialLR(optimizer, gamma\=0.9)

for epoch in range(20):
    for input, target in dataset:
        optimizer.zero\_grad()
        output \= model(input)
        loss \= loss\_fn(output, target)
        loss.backward()
        optimizer.step()
    scheduler.step()

Copy to clipboard

Most learning rate schedulers can be called back-to-back (also referred to as chaining schedulers). The result is that each scheduler is applied one after the other on the learning rate obtained by the one preceding it.

Example:

optimizer \= optim.SGD(model.parameters(), lr\=0.01, momentum\=0.9)
scheduler1 \= ExponentialLR(optimizer, gamma\=0.9)
scheduler2 \= MultiStepLR(optimizer, milestones\=\[30,80\], gamma\=0.1)

for epoch in range(20):
    for input, target in dataset:
        optimizer.zero\_grad()
        output \= model(input)
        loss \= loss\_fn(output, target)
        loss.backward()
        optimizer.step()
    scheduler1.step()
    scheduler2.step()

Copy to clipboard

In many places in the documentation, we will use the following template to refer to schedulers algorithms.

\>>> scheduler \= ...
\>>> for epoch in range(100):
\>>>     train(...)
\>>>     validate(...)
\>>>     scheduler.step()

Copy to clipboard

Warning

Prior to PyTorch 1.1.0, the learning rate scheduler was expected to be called before the optimizer’s update; 1.1.0 changed this behavior in a BC-breaking way. If you use the learning rate scheduler (calling `scheduler.step()`) before the optimizer’s update (calling `optimizer.step()`), this will skip the first value of the learning rate schedule. If you are unable to reproduce results after upgrading to PyTorch 1.1.0, please check if you are calling `scheduler.step()` at the wrong time.

|     |     |
| --- | --- |
| [`lr_scheduler.LRScheduler`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler "torch.optim.lr_scheduler.LRScheduler") | Base class for all learning rate schedulers. |
| [`lr_scheduler.LambdaLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.LambdaLR.html#torch.optim.lr_scheduler.LambdaLR "torch.optim.lr_scheduler.LambdaLR") | Sets the initial learning rate. |
| [`lr_scheduler.MultiplicativeLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.MultiplicativeLR.html#torch.optim.lr_scheduler.MultiplicativeLR "torch.optim.lr_scheduler.MultiplicativeLR") | Multiply the learning rate of each parameter group by the factor given in the specified function. |
| [`lr_scheduler.StepLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.StepLR.html#torch.optim.lr_scheduler.StepLR "torch.optim.lr_scheduler.StepLR") | Decays the learning rate of each parameter group by gamma every step\_size epochs. |
| [`lr_scheduler.MultiStepLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.MultiStepLR.html#torch.optim.lr_scheduler.MultiStepLR "torch.optim.lr_scheduler.MultiStepLR") | Decays the learning rate of each parameter group by gamma once the number of epoch reaches one of the milestones. |
| [`lr_scheduler.ConstantLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.ConstantLR.html#torch.optim.lr_scheduler.ConstantLR "torch.optim.lr_scheduler.ConstantLR") | Multiply the learning rate of each parameter group by a small constant factor. |
| [`lr_scheduler.LinearLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.LinearLR.html#torch.optim.lr_scheduler.LinearLR "torch.optim.lr_scheduler.LinearLR") | Decays the learning rate of each parameter group by linearly changing small multiplicative factor. |
| [`lr_scheduler.ExponentialLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.ExponentialLR.html#torch.optim.lr_scheduler.ExponentialLR "torch.optim.lr_scheduler.ExponentialLR") | Decays the learning rate of each parameter group by gamma every epoch. |
| [`lr_scheduler.PolynomialLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.PolynomialLR.html#torch.optim.lr_scheduler.PolynomialLR "torch.optim.lr_scheduler.PolynomialLR") | Decays the learning rate of each parameter group using a polynomial function in the given total\_iters. |
| [`lr_scheduler.CosineAnnealingLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.CosineAnnealingLR.html#torch.optim.lr_scheduler.CosineAnnealingLR "torch.optim.lr_scheduler.CosineAnnealingLR") | Set the learning rate of each parameter group using a cosine annealing schedule. |
| [`lr_scheduler.ChainedScheduler`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.ChainedScheduler.html#torch.optim.lr_scheduler.ChainedScheduler "torch.optim.lr_scheduler.ChainedScheduler") | Chains a list of learning rate schedulers. |
| [`lr_scheduler.SequentialLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.SequentialLR.html#torch.optim.lr_scheduler.SequentialLR "torch.optim.lr_scheduler.SequentialLR") | Contains a list of schedulers expected to be called sequentially during the optimization process. |
| [`lr_scheduler.ReduceLROnPlateau`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html#torch.optim.lr_scheduler.ReduceLROnPlateau "torch.optim.lr_scheduler.ReduceLROnPlateau") | Reduce learning rate when a metric has stopped improving. |
| [`lr_scheduler.CyclicLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.CyclicLR.html#torch.optim.lr_scheduler.CyclicLR "torch.optim.lr_scheduler.CyclicLR") | Sets the learning rate of each parameter group according to cyclical learning rate policy (CLR). |
| [`lr_scheduler.OneCycleLR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.OneCycleLR.html#torch.optim.lr_scheduler.OneCycleLR "torch.optim.lr_scheduler.OneCycleLR") | Sets the learning rate of each parameter group according to the 1cycle learning rate policy. |
| [`lr_scheduler.CosineAnnealingWarmRestarts`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lr_scheduler.CosineAnnealingWarmRestarts.html#torch.optim.lr_scheduler.CosineAnnealingWarmRestarts "torch.optim.lr_scheduler.CosineAnnealingWarmRestarts") | Set the learning rate of each parameter group using a cosine annealing schedule. |

How to utilize named parameters to load optimizer state dict[#](https://docs.pytorch.org/docs/2.15/optim.html#how-to-utilize-named-parameters-to-load-optimizer-state-dict "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The function [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict "torch.optim.Optimizer.load_state_dict")
 stores the optional `param_names` content from the loaded state dict if present. However, the process of loading the optimizer state is not affected, as the order of the parameters matters to maintain compatibility (in case of different ordering). To utilize the loaded parameters names from the loaded state dict, a custom `register_load_state_dict_pre_hook` needs to be implemented according to the desired behavior.

This can be useful, for instance, when the model architecture changes, but the weights and optimizer states need to remain unchanged. The following example demonstrates how to implement this customization.

Example:

class OneLayerModel(nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.fc \= nn.Linear(3, 4)

    def forward(self, x):
        return self.fc(x)

model \= OneLayerModel()
optimizer \= optim.SGD(model.named\_parameters(), lr\=0.01, momentum\=0.9)
\# training..
torch.save(optimizer.state\_dict(), PATH)

Copy to clipboard

Let’s say that `model` implements an expert (MoE), and we want to duplicate it and resume training for two experts, both initialized the same way as the `fc` layer. For the following `model2` we create two layers identical to `fc` and resume training by loading the model weights and optimizer states from `model` into both `fc1` and `fc2` of `model2` (and adjust them accordingly):

class TwoLayerModel(nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.fc1 \= nn.Linear(3, 4)
        self.fc2 \= nn.Linear(3, 4)

    def forward(self, x):
        return (self.fc1(x) + self.fc2(x)) / 2

model2 \= TwoLayerModel()
\# adapt and load model weights..
optimizer2 \= optim.SGD(model2.named\_parameters(), lr\=0.01, momentum\=0.9)

Copy to clipboard

To load the state dict for `optimizer2` with the state dict of the previous optimizer such that both `fc1` and `fc2` will be initialized with a copy of `fc` optimizer states (to resume training for each layer from `fc`), we can use the following hook:

def adapt\_state\_dict\_ids(optimizer, state\_dict):
    adapted\_state\_dict \= deepcopy(optimizer.state\_dict())
    \# Copy setup parameters (lr, weight\_decay, etc.), in case they differ in the loaded state dict.
    for k, v in state\_dict\['param\_groups'\]\[0\].items():
        if k not in \['params', 'param\_names'\]:
            adapted\_state\_dict\['param\_groups'\]\[0\]\[k\] \= v

    lookup\_dict \= {
        'fc1.weight': 'fc.weight',
        'fc1.bias': 'fc.bias',
        'fc2.weight': 'fc.weight',
        'fc2.bias': 'fc.bias'
    }
    clone\_deepcopy \= lambda d: {k: (v.clone() if isinstance(v, torch.Tensor) else deepcopy(v)) for k, v in d.items()}
    for param\_id, param\_name in zip(
            optimizer.state\_dict()\['param\_groups'\]\[0\]\['params'\],
            optimizer.state\_dict()\['param\_groups'\]\[0\]\['param\_names'\]):
        name\_in\_loaded \= lookup\_dict\[param\_name\]
        index\_in\_loaded\_list \= state\_dict\['param\_groups'\]\[0\]\['param\_names'\].index(name\_in\_loaded)
        id\_in\_loaded \= state\_dict\['param\_groups'\]\[0\]\['params'\]\[index\_in\_loaded\_list\]
        \# Copy the state of the corresponding parameter
        if id\_in\_loaded in state\_dict\['state'\]:
            adapted\_state\_dict\['state'\]\[param\_id\] \= clone\_deepcopy(state\_dict\['state'\]\[id\_in\_loaded\])

    return adapted\_state\_dict

optimizer2.register\_load\_state\_dict\_pre\_hook(adapt\_state\_dict\_ids)
optimizer2.load\_state\_dict(torch.load(PATH)) \# The previous optimizer saved state\_dict

Copy to clipboard

This ensures that the adapted state\_dict with the correct states for the layers of `model2` will be used during model loading. Note that this code is designed specifically for this example (e.g., assuming a single parameter group), and other cases might require different adaptations.

The following example shows how to handle missing parameters in a loaded `state dict` when the model structure changes. The `Model_bypass` adds a new `bypass` layer, which is not present in the original `Model1`. To resume training, a custom `adapt_state_dict_missing_param` hook is used to adapt the optimizer’s `state_dict`, ensuring existing parameters are mapped correctly, while missing ones (like the bypass layer) remain unchanged (as initialized in this example). This approach enables smooth loading and resuming of the optimizer state despite model changes. The new bypass layer will be trained from scratch:

class Model1(nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.fc \= nn.Linear(5, 5)

    def forward(self, x):
        return self.fc(x) + x

model \= Model1()
optimizer \= optim.SGD(model.named\_parameters(), lr\=0.01, momentum\=0.9)
\# training..
torch.save(optimizer.state\_dict(), PATH)

class Model\_bypass(nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.fc \= nn.Linear(5, 5)
        self.bypass \= nn.Linear(5, 5, bias\=False)
        torch.nn.init.eye\_(self.bypass.weight)

    def forward(self, x):
        return self.fc(x) + self.bypass(x)

model2 \= Model\_bypass()
optimizer2 \= optim.SGD(model2.named\_parameters(), lr\=0.01, momentum\=0.9)

def adapt\_state\_dict\_missing\_param(optimizer, state\_dict):
    adapted\_state\_dict \= deepcopy(optimizer.state\_dict())
    \# Copy setup parameters (lr, weight\_decay, etc.), in case they differ in the loaded state dict.
    for k, v in state\_dict\['param\_groups'\]\[0\].items():
        if k not in \['params', 'param\_names'\]:
            adapted\_state\_dict\['param\_groups'\]\[0\]\[k\] \= v

    lookup\_dict \= {
        'fc.weight': 'fc.weight',
        'fc.bias': 'fc.bias',
        'bypass.weight': None,
    }

    clone\_deepcopy \= lambda d: {k: (v.clone() if isinstance(v, torch.Tensor) else deepcopy(v)) for k, v in d.items()}
    for param\_id, param\_name in zip(
            optimizer.state\_dict()\['param\_groups'\]\[0\]\['params'\],
            optimizer.state\_dict()\['param\_groups'\]\[0\]\['param\_names'\]):
        name\_in\_loaded \= lookup\_dict\[param\_name\]
        if name\_in\_loaded in state\_dict\['param\_groups'\]\[0\]\['param\_names'\]:
            index\_in\_loaded\_list \= state\_dict\['param\_groups'\]\[0\]\['param\_names'\].index(name\_in\_loaded)
            id\_in\_loaded \= state\_dict\['param\_groups'\]\[0\]\['params'\]\[index\_in\_loaded\_list\]
            \# Copy the state of the corresponding parameter
            if id\_in\_loaded in state\_dict\['state'\]:
                adapted\_state\_dict\['state'\]\[param\_id\] \= clone\_deepcopy(state\_dict\['state'\]\[id\_in\_loaded\])

    return adapted\_state\_dict

optimizer2.register\_load\_state\_dict\_pre\_hook(adapt\_state\_dict\_ids)
optimizer2.load\_state\_dict(torch.load(PATH)) \# The previous optimizer saved state\_dict

Copy to clipboard

As a third example, instead of loading a state according to the order of parameters (the default approach), this hook can be used to load according to the parameters’ names:

def names\_matching(optimizer, state\_dict):
    assert len(state\_dict\['param\_groups'\]) \== len(optimizer.state\_dict()\['param\_groups'\])
    adapted\_state\_dict \= deepcopy(optimizer.state\_dict())
    for g\_ind in range(len(state\_dict\['param\_groups'\])):
        assert len(state\_dict\['param\_groups'\]\[g\_ind\]\['params'\]) \== len(
            optimizer.state\_dict()\['param\_groups'\]\[g\_ind\]\['params'\])

        for k, v in state\_dict\['param\_groups'\]\[g\_ind\].items():
            if k not in \['params', 'param\_names'\]:
                adapted\_state\_dict\['param\_groups'\]\[g\_ind\]\[k\] \= v

        for param\_id, param\_name in zip(
                optimizer.state\_dict()\['param\_groups'\]\[g\_ind\]\['params'\],
                optimizer.state\_dict()\['param\_groups'\]\[g\_ind\]\['param\_names'\]):
            index\_in\_loaded\_list \= state\_dict\['param\_groups'\]\[g\_ind\]\['param\_names'\].index(param\_name)
            id\_in\_loaded \= state\_dict\['param\_groups'\]\[g\_ind\]\['params'\]\[index\_in\_loaded\_list\]
            \# Copy the state of the corresponding parameter
            if id\_in\_loaded in state\_dict\['state'\]:
                adapted\_state\_dict\['state'\]\[param\_id\] \= deepcopy(state\_dict\['state'\]\[id\_in\_loaded\])

    return adapted\_state\_dict

Copy to clipboard

Weight Averaging (SWA and EMA)[#](https://docs.pytorch.org/docs/2.15/optim.html#weight-averaging-swa-and-ema "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

[`torch.optim.swa_utils.AveragedModel`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel "torch.optim.swa_utils.AveragedModel")
 implements Stochastic Weight Averaging (SWA) and Exponential Moving Average (EMA), [`torch.optim.swa_utils.SWALR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.SWALR.html#torch.optim.swa_utils.SWALR "torch.optim.swa_utils.SWALR")
 implements the SWA learning rate scheduler and [`torch.optim.swa_utils.update_bn()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swa_utils.update_bn "torch.optim.swa_utils.update_bn")
 is a utility function used to update SWA/EMA batch normalization statistics at the end of training.

SWA has been proposed in [Averaging Weights Leads to Wider Optima and Better Generalization](https://arxiv.org/abs/1803.05407)
.

EMA is a widely known technique to reduce the training time by reducing the number of weight updates needed. It is a variation of [Polyak averaging](https://paperswithcode.com/method/polyak-averaging)
, but using exponential weights instead of equal weights across iterations.

### Constructing averaged models[#](https://docs.pytorch.org/docs/2.15/optim.html#constructing-averaged-models "Link to this heading")

The `AveragedModel` class serves to compute the weights of the SWA or EMA model.

You can create an SWA averaged model by running:

\>>> averaged\_model \= AveragedModel(model)

Copy to clipboard

EMA models are constructed by specifying the `multi_avg_fn` argument as follows:

\>>> decay \= 0.999
\>>> averaged\_model \= AveragedModel(model, multi\_avg\_fn\=get\_ema\_multi\_avg\_fn(decay))

Copy to clipboard

Decay is a parameter between 0 and 1 that controls how fast the averaged parameters are decayed. If not provided to [`torch.optim.swa_utils.get_ema_multi_avg_fn()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swa_utils.get_ema_multi_avg_fn "torch.optim.swa_utils.get_ema_multi_avg_fn")
, the default is 0.999. Decay value should be close to 1.0, as smaller values can cause optimization convergence issues.

[`torch.optim.swa_utils.get_ema_multi_avg_fn()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swa_utils.get_ema_multi_avg_fn "torch.optim.swa_utils.get_ema_multi_avg_fn")
 returns a function that applies the following EMA equation to the weights:

W0EMA\=W0modelW\_0^{\\text{EMA}} = W\_0^{\\text{model}}W0EMA​\=W0model​

Wt+1EMA\=decay×WtEMA+(1−decay)×Wt+1modelW\_{t+1}^{\\text{EMA}} = \\text{decay} \\times W\_t^{\\text{EMA}} + (1 - \\text{decay}) \\times W\_{t+1}^{\\text{model}}Wt+1EMA​\=decay×WtEMA​+(1−decay)×Wt+1model​

where `W_t^{\text{EMA}}` is the EMA parameter at step `t`, `W_t^{\text{model}}` is the model parameter at step `t`, and decay is the EMA decay rate (default: 0.999).

Here the model `model` can be an arbitrary [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 object. `averaged_model` will keep track of the running averages of the parameters of the `model`. To update these averages, you should use the `update_parameters()` function after the `optimizer.step()`:

\>>> averaged\_model.update\_parameters(model)

Copy to clipboard

For SWA and EMA, this call is usually done right after the optimizer `step()`. In the case of SWA, this is usually skipped for some numbers of steps at the beginning of the training.

### Custom averaging strategies[#](https://docs.pytorch.org/docs/2.15/optim.html#custom-averaging-strategies "Link to this heading")

By default, [`torch.optim.swa_utils.AveragedModel`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel "torch.optim.swa_utils.AveragedModel")
 computes a running equal average of the parameters that you provide, but you can also use custom averaging functions with the `avg_fn` or `multi_avg_fn` parameters:

*   `avg_fn` allows defining a function operating on each parameter tuple (averaged parameter, model parameter) and should return the new averaged parameter.
    
*   `multi_avg_fn` allows defining more efficient operations acting on a tuple of parameter lists, (averaged parameter list, model parameter list), at the same time, for example using the `torch._foreach*` functions. This function must update the averaged parameters in-place.
    

In the following example `ema_model` computes an exponential moving average using the `avg_fn` parameter:

\>>> ema\_avg \= lambda averaged\_model\_parameter, model\_parameter, num\_averaged:\\
\>>>         0.9 \* averaged\_model\_parameter + 0.1 \* model\_parameter
\>>> ema\_model \= torch.optim.swa\_utils.AveragedModel(model, avg\_fn\=ema\_avg)

Copy to clipboard

In the following example `ema_model` computes an exponential moving average using the more efficient `multi_avg_fn` parameter:

\>>> ema\_model \= AveragedModel(model, multi\_avg\_fn\=get\_ema\_multi\_avg\_fn(0.9))

Copy to clipboard

### SWA learning rate schedules[#](https://docs.pytorch.org/docs/2.15/optim.html#swa-learning-rate-schedules "Link to this heading")

Typically, in SWA the learning rate is set to a high constant value. `SWALR` is a learning rate scheduler that anneals the learning rate to a fixed value, and then keeps it constant. For example, the following code creates a scheduler that linearly anneals the learning rate from its initial value to 0.05 in 5 epochs within each parameter group:

\>>> swa\_scheduler \= torch.optim.swa\_utils.SWALR(optimizer, \\
\>>>         anneal\_strategy\="linear", anneal\_epochs\=5, swa\_lr\=0.05)

Copy to clipboard

You can also use cosine annealing to a fixed value instead of linear annealing by setting `anneal_strategy="cos"`.

### Taking care of batch normalization[#](https://docs.pytorch.org/docs/2.15/optim.html#taking-care-of-batch-normalization "Link to this heading")

`update_bn()` is a utility function that allows to compute the batchnorm statistics for the SWA model on a given dataloader `loader` at the end of training:

\>>> torch.optim.swa\_utils.update\_bn(loader, swa\_model)

Copy to clipboard

`update_bn()` applies the `swa_model` to every element in the dataloader and computes the activation statistics for each batch normalization layer in the model.

Warning

`update_bn()` assumes that each batch in the dataloader `loader` is either a tensors or a list of tensors where the first element is the tensor that the network `swa_model` should be applied to. If your dataloader has a different structure, you can update the batch normalization statistics of the `swa_model` by doing a forward pass with the `swa_model` on each element of the dataset.

### Putting it all together: SWA[#](https://docs.pytorch.org/docs/2.15/optim.html#putting-it-all-together-swa "Link to this heading")

In the example below, `swa_model` is the SWA model that accumulates the averages of the weights. We train the model for a total of 300 epochs and we switch to the SWA learning rate schedule and start to collect SWA averages of the parameters at epoch 160:

\>>> loader, optimizer, model, loss\_fn \= ...
\>>> swa\_model \= torch.optim.swa\_utils.AveragedModel(model)
\>>> scheduler \= torch.optim.lr\_scheduler.CosineAnnealingLR(optimizer, T\_max\=300)
\>>> swa\_start \= 160
\>>> swa\_scheduler \= SWALR(optimizer, swa\_lr\=0.05)
\>>>
\>>> for epoch in range(300):
\>>>       for input, target in loader:
\>>>           optimizer.zero\_grad()
\>>>           loss\_fn(model(input), target).backward()
\>>>           optimizer.step()
\>>>       if epoch \> swa\_start:
\>>>           swa\_model.update\_parameters(model)
\>>>           swa\_scheduler.step()
\>>>       else:
\>>>           scheduler.step()
\>>>
\>>> \# Update bn statistics for the swa\_model at the end
\>>> torch.optim.swa\_utils.update\_bn(loader, swa\_model)
\>>> \# Use swa\_model to make predictions on test data
\>>> preds \= swa\_model(test\_input)

Copy to clipboard

### Putting it all together: EMA[#](https://docs.pytorch.org/docs/2.15/optim.html#putting-it-all-together-ema "Link to this heading")

In the example below, `ema_model` is the EMA model that accumulates the exponentially-decayed averages of the weights with a decay rate of 0.999. We train the model for a total of 300 epochs and start to collect EMA averages immediately.

\>>> loader, optimizer, model, loss\_fn \= ...
\>>> ema\_model \= torch.optim.swa\_utils.AveragedModel(model, \\
\>>>             multi\_avg\_fn\=torch.optim.swa\_utils.get\_ema\_multi\_avg\_fn(0.999))
\>>>
\>>> for epoch in range(300):
\>>>       for input, target in loader:
\>>>           optimizer.zero\_grad()
\>>>           loss\_fn(model(input), target).backward()
\>>>           optimizer.step()
\>>>           ema\_model.update\_parameters(model)
\>>>
\>>> \# Update bn statistics for the ema\_model at the end
\>>> torch.optim.swa\_utils.update\_bn(loader, ema\_model)
\>>> \# Use ema\_model to make predictions on test data
\>>> preds \= ema\_model(test\_input)

Copy to clipboard

|     |     |
| --- | --- |
| [`swa_utils.AveragedModel`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel "torch.optim.swa_utils.AveragedModel") | Implements averaged model for Stochastic Weight Averaging (SWA) and Exponential Moving Average (EMA). |
| [`swa_utils.SWALR`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.SWALR.html#torch.optim.swa_utils.SWALR "torch.optim.swa_utils.SWALR") | Anneals the learning rate in each parameter group to a fixed value. |
| [`swa_utils.get_ema_avg_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.get_ema_avg_fn.html#torch.optim.swa_utils.get_ema_avg_fn "torch.optim.swa_utils.get_ema_avg_fn") | Get the function applying exponential moving average (EMA) across multiple params. |
| [`swa_utils.get_swa_avg_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.get_swa_avg_fn.html#torch.optim.swa_utils.get_swa_avg_fn "torch.optim.swa_utils.get_swa_avg_fn") | Get the function applying stochastic weight average (SWA) across a single param. |
| [`swa_utils.get_swa_multi_avg_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.swa_utils.get_swa_multi_avg_fn.html#torch.optim.swa_utils.get_swa_multi_avg_fn "torch.optim.swa_utils.get_swa_multi_avg_fn") | Get the function applying stochastic weight average (SWA) across multiple params. |

torch.optim.swa\_utils.get\_ema\_multi\_avg\_fn(_decay\=0.999_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/swa_utils.py#L42)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swa_utils.get_ema_multi_avg_fn "Link to this definition")

Get the function applying exponential moving average (EMA) across multiple params.

The EMA is computed as:

W0EMA\=W0modelW\_0^{\\text{EMA}} = W\_0^{\\text{model}} W0EMA​\=W0model​

Wt+1EMA\=decay×WtEMA+(1−decay)×Wt+1modelW\_{t+1}^{\\text{EMA}} = \\text{decay} \\times W\_t^{\\text{EMA}} + (1 - \\text{decay}) \\times W\_{t+1}^{\\text{model}} Wt+1EMA​\=decay×WtEMA​+(1−decay)×Wt+1model​

where WtEMAW\_t^{\\text{EMA}}WtEMA​ is the EMA parameter at step ttt, WtmodelW\_t^{\\text{model}}Wtmodel​ is the model parameter at step ttt, and decay\\text{decay}decay is the decay rate (default: 0.999).

Parameters:

**decay** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
) – Decay rate for EMA. Must be in the range \[0, 1\]. Default: 0.999

Returns:

A function that updates EMA parameters given current model parameters

Return type:

Callable

torch.optim.swa\_utils.update\_bn(_loader_, _model_, _device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/swa_utils.py#L371)
[#](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.swa_utils.update_bn "Link to this definition")

Update BatchNorm running\_mean, running\_var buffers in the model.

It performs one pass over data in loader to estimate the activation statistics for BatchNorm layers in the model.

Parameters:

*   **loader** ([_torch.utils.data.DataLoader_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
    ) – dataset loader to compute the activation statistics on. Each data batch should be either a tensor, or a list/tuple whose first element is a tensor containing data.
    
*   **model** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – model for which we seek to update BatchNorm statistics.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    _,_ _optional_) – If set, data will be transferred to `device` before being passed into `model`.
    

Example

\>>> loader, model \= ...
\>>> torch.optim.swa\_utils.update\_bn(loader, model)

Copy to clipboard

Note

The update\_bn utility assumes that each data batch in `loader` is either a tensor or a list or tuple of tensors; in the latter case it is assumed that `model.forward()` should be called on the first element of the list or tuple corresponding to the data batch.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/optim.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/optim.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |