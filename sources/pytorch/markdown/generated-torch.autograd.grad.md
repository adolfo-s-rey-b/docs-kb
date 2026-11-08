Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.autograd.grad.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.autograd.grad.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.autograd.grad.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.autograd.grad.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.autograd.grad.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.autograd.grad.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.autograd.grad.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.autograd.grad.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.autograd.grad.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.autograd.grad.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.autograd.grad.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.autograd.grad.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.autograd.grad.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.autograd.grad.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.autograd.grad.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.autograd.grad.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.autograd.grad.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.autograd.grad.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.autograd.grad.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.autograd.grad.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.autograd.grad.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.autograd.grad.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.autograd.grad.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.autograd.grad.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.autograd.grad.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.autograd.grad.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.autograd.grad.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.autograd.grad.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.autograd.grad.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.autograd.grad.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.autograd.grad.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.autograd.grad.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.autograd.grad.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.autograd.grad.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.autograd.grad.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.autograd.grad.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.autograd.grad.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.autograd.grad.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.autograd.grad.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.autograd.grad.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.autograd.grad.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.autograd.grad.html)

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

torch.autograd.grad[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch-autograd-grad "Link to this heading")

=========================================================================================================================================

torch.autograd.grad(_outputs: \_TensorOrTensorsOrGradEdge_, _inputs: \_TensorOrTensorsOrGradEdge_, _grad\_outputs: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _retain\_graph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _create\_graph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _only\_inputs: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _allow\_unused: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _is\_grads\_batched: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _materialize\_grads: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, ...\][\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/__init__.py#L434)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "Link to this definition")

torch.autograd.grad(_outputs: \_TensorOrTensorsOrGradEdge_, _inputs: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _grad\_outputs: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _retain\_graph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _create\_graph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _only\_inputs: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _allow\_unused: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _is\_grads\_batched: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _materialize\_grads: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_) → [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Compute and return the sum of gradients of outputs with respect to the inputs.

`grad_outputs` should be a sequence of length matching `output` containing the “vector” in vector-Jacobian product, usually the pre-computed gradients w.r.t. each of the outputs. If an output doesn’t require\_grad, then the gradient can be `None`).

Note

If you run any forward ops, create `grad_outputs`, and/or call `grad` in a user-specified CUDA stream context, see [Stream semantics of backward passes](https://docs.pytorch.org/docs/2.15/notes/cuda.html#bwd-cuda-stream-semantics)
.

Note

`only_inputs` argument is deprecated and is ignored now (defaults to `True`). To accumulate gradient for other parts of the graph, please use `torch.autograd.backward`.

Parameters:

*   **outputs** (_sequence_ _of_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ [_GradientEdge_](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.GradientEdge "torch.autograd.graph.GradientEdge")
    ) – outputs of the differentiated function.
    
*   **inputs** (_sequence_ _of_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ [_GradientEdge_](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.GradientEdge "torch.autograd.graph.GradientEdge")
     _or_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Inputs w.r.t. which the gradient will be returned (and not accumulated into `.grad`). When a dict is provided (e.g. `dict(model.named_parameters())`), the result is returned as a dict with matching keys.
    
*   **grad\_outputs** (_sequence_ _of_ _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _or_ _None__\] or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – The “vector” in the vector-Jacobian product. Usually gradients w.r.t. each output. None values can be specified for scalar Tensors or ones that don’t require grad. If a None value would be acceptable for all grad\_tensors, then this argument is optional. Default: None.
    
*   **retain\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, the graph used to compute the grad will be freed. Note that in nearly all cases setting this option to `True` is not needed and often can be worked around in a much more efficient way. Defaults to the value of `create_graph`.
    
*   **create\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, graph of the derivative will be constructed, allowing to compute higher order derivative products. Default: `False`.
    
*   **allow\_unused** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__,_ _optional_) – If `False`, specifying inputs that were not used when computing outputs (and therefore their grad is always zero) is an error. Defaults to the value of `materialize_grads`.
    
*   **is\_grads\_batched** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, the first dimension of each tensor in `grad_outputs` will be interpreted as the batch dimension. Instead of computing a single vector-Jacobian product, we compute a batch of vector-Jacobian products for each “vector” in the batch. We use the vmap prototype feature as the backend to vectorize calls to the autograd engine so that this computation can be performed in a single call. This should lead to performance improvements when compared to manually looping and performing backward multiple times. Note that due to this feature being experimental, there may be performance cliffs. Please use `torch._C._debug_only_display_vmap_fallback_warnings(True)` to show any performance warnings and file an issue on github if warnings exist for your use case. Defaults to `False`.
    
*   **materialize\_grads** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, set the gradient for unused inputs to zero instead of None. This is useful when computing higher-order derivatives. If `materialize_grads` is `True` and `allow_unused` is `False`, an error will be raised. Defaults to `False`.
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.autograd.grad.rst.txt)

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