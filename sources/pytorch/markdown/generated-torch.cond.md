Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cond.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cond.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cond.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cond.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cond.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cond.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cond.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cond.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cond.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cond.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cond.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cond.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cond.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cond.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cond.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cond.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cond.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cond.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cond.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cond.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cond.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cond.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cond.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cond.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cond.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cond.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cond.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cond.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cond.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cond.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cond.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cond.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cond.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cond.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cond.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cond.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cond.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cond.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cond.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cond.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cond.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cond.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cond.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cond.html)

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

torch.cond[#](https://docs.pytorch.org/docs/2.15/generated/torch.cond.html#torch-cond "Link to this heading")

==============================================================================================================

torch.cond(_pred_, _true\_fn_, _false\_fn_, _operands\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/cond.py#L94)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cond.html#torch.cond "Link to this definition")

Conditionally applies true\_fn or false\_fn.

Warning

torch.cond is a prototype feature in PyTorch. It has limited support for input and output types. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

cond is structured control flow operator. That is, it is like a Python if-statement, but has restrictions on true\_fn, false\_fn, and operands that enable it to be capturable using torch.compile and torch.export.

Assuming the constraints on cond’s arguments are met, cond is equivalent to the following:

def cond(pred, true\_branch, false\_branch, operands):
    if pred:
        return true\_branch(\*operands)
    else:
        return false\_branch(\*operands)

Copy to clipboard

Parameters:

*   **pred** (_Union__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ [_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – A boolean expression or a tensor with one element, indicating which branch function to apply.
    
*   **true\_fn** (_Callable_) – A callable function (a -> b) that is within the scope that is being traced.
    
*   **false\_fn** (_Callable_) – A callable function (a -> b) that is within the scope that is being traced. The true branch and false branch must have consistent input and outputs, meaning the inputs have to be the same, and the outputs have to be the same type and shape. Int output is also allowed. We’ll make the output dynamic by turning it into a symint.
    
*   **operands** (_Tuple_ _of_ _possibly nested dict/list/tuple_ _of_ [_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – A tuple of inputs to the true/false functions. It can be empty if true\_fn/false\_fn doesn’t require input. Defaults to ().
    

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

Example:

def true\_fn(x: torch.Tensor):
    return x.cos()

def false\_fn(x: torch.Tensor):
    return x.sin()

return cond(x.shape\[0\] \> 4, true\_fn, false\_fn, (x,))

Copy to clipboard

Restrictions:

*   The conditional statement (aka pred) must meet one of the following constraints:
    
    *   It’s a torch.Tensor with only one element, and torch.bool dtype
        
    *   It’s a boolean expression, e.g. x.shape\[0\] > 10 or x.dim() > 1 and x.shape\[1\] > 10
        
*   The branch function (aka true\_fn/false\_fn) must meet all of the following constraints:
    
    *   The function signature must match with operands.
        
    *   The function must return a tensor with the same metadata, e.g. shape, dtype, etc.
        
    *   The function cannot have in-place mutations on global variables. (Note: in-place tensor operations such as add\_ for intermediate results are allowed in a branch)
        
    *   The function can perform in-place mutations on its input tensors during inference (i.e., when torch.is\_grad\_enabled() is False). Note: When using torch.compile() with a non-constant predicate, the outputs will always be new tensors that do not share object identity with the original inputs.
        
        Example:
        
        def true\_fn(x):
            return x.sin\_()
        
        def false\_fn(x):
            return x + 1
        
        def f(x):
            return cond(x.sum() \> 0, true\_fn, false\_fn, (x,))
        
        x \= torch.ones(4)
        with torch.no\_grad():
            result \= torch.compile(f)(x)
        assert result is not x  \# result is a new tensor, not the original x
        
        Copy to clipboard
        

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cond.rst.txt)

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