Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/while_loop.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/while_loop.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/while_loop.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/while_loop.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/while_loop.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/while_loop.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/while_loop.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/while_loop.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/while_loop.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/while_loop.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/while_loop.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/while_loop.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/while_loop.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/while_loop.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/while_loop.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/while_loop.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/while_loop.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/while_loop.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/while_loop.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/while_loop.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/while_loop.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/while_loop.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/while_loop.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/while_loop.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/while_loop.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/while_loop.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/while_loop.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/while_loop.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/while_loop.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/while_loop.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/while_loop.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/while_loop.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/while_loop.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/while_loop.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/while_loop.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/while_loop.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/while_loop.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/while_loop.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/while_loop.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/while_loop.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/while_loop.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/while_loop.html)

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

Control Flow - While Loop[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#control-flow-while-loop "Link to this heading")

=================================================================================================================================================

Created On: Feb 14, 2026 | Last Updated On: Feb 14, 2026

`torch.while_loop` is a structured control flow operator that runs a body function while a condition is true. It can logically be seen as implemented as follows:

def while\_loop(
    cond\_fn: Callable\[..., bool\],
    body\_fn: Callable\[..., tuple\],
    carried\_inputs: tuple,
):
    val \= carried\_inputs
    while cond\_fn(\*val):
        val \= body\_fn(\*val)
    return val

Copy to clipboard

Warning

`torch.while_loop` is a prototype feature in PyTorch. It has limited support for input and output types. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Examples[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Below is a basic example that uses while\_loop to iterate until a condition is met:

import torch
from torch.\_higher\_order\_ops import while\_loop

class M(torch.nn.Module):

    def cond\_fn(self, iter\_count, x):
        return iter\_count.sum() > 0

    def body\_fn(self, iter\_count, x):
        return iter\_count - 1, x \* 2

    def forward(self, init\_iter, init\_x):
        final\_iter, final\_x = while\_loop(self.cond\_fn, self.body\_fn, (init\_iter, init\_x))
        return final\_iter, final\_x

m = M()

Copy to clipboard

We can eagerly run the model and expect the results vary based on input shape:

\_, final\_x = m(torch.tensor(\[3\]), torch.ones(3))
assert torch.equal(final\_x, torch.ones(3) \* 2\*\*3)

\_, final\_x = m(torch.tensor(\[10\]), torch.ones(3))
assert torch.equal(final\_x, torch.ones(3) \* 2\*\*10)

Copy to clipboard

We can export the model for further transformations and deployment. This gives us an exported program that preserves the while\_loop structure:

ep = torch.export.export(M(), (torch.tensor(\[10\]), torch.ones(3)))
print(ep)

Copy to clipboard

Notice that both the condition and body functions become sub-graph attributes of the top-level graph module.

Restrictions[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#restrictions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

*   `body_fn` must return tensors or integers with the same metadata (shape, dtype) as inputs.
    
*   `body_fn` and `cond_fn` must not in-place mutate the `carried_inputs`. A clone before mutation is required.
    
*   `body_fn` and `cond_fn` must not mutate Python variables (e.g., list/dict) created outside the function.
    
*   `body_fn` and `cond_fn`’s output cannot alias any of the inputs. A clone is required.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#api-reference "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

torch.\_higher\_order\_ops.while\_loop.while\_loop(_cond\_fn_, _body\_fn_, _carried\_inputs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/while_loop.py#L136)
[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html#torch._higher_order_ops.while_loop.while_loop "Link to this definition")

Run `body_fn(*carried_inputs)` while `cond_fn(*carried_inputs)` returns a True scalar tensor. Returns the output of body\_fn or initial carried\_inputs.

Warning

torch.while\_loop is a prototype feature in PyTorch. It has limited support for input and output types and doesn’t support training currently. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

while\_loop is a structured control flow operator. It preserves the loop semantic across the torch.compile and torch.export.

while\_loop is equivalent to the following:

def while\_loop(cond\_fn, body\_fn, carried\_inputs):
    val \= carried\_inputs
    while cond\_fn(\*val):
        val \= body\_fn(\*val)
    return val

Copy to clipboard

Parameters:

*   **cond\_fn** (_Callable_) – A callable function that returns a boolean Scalar tensor or a python boolean.
    
*   **body\_fn** (_Callable_) – A callable function that takes the same inputs as cond\_fn and returns a tuple of tensors or ints
    
*   **carried\_inputs** (_Tuple_ _of_ _possibly nested dict/list/tuple_ _of_ _tensors_ _or_ _ints_) – A tuple of inputs to cond\_fn and body\_fn. It’s also the initial value of states that are carried across iterations. Note that when pass an integer as carry, the corresponding return of while\_loop will be another int with unknown values because we don’t know how many iterations while\_loop will run.
    

Example 1:

def cond\_fn(iter, x):
    return iter.sum() < 10

def body\_fn(iter, x):
    return iter + 1, x.sin()

while\_loop(cond\_fn, body\_fn, (torch.zeros(1), torch.randn(3, 4)))

Copy to clipboard

Example 2:

def cond\_fn(int\_iter, x):
    return 2 \* int\_iter < x.shape\[0\]

def body\_fn(int\_iter, x):
    return int\_iter + 1, x + int\_iter

while\_loop(cond\_fn, body\_fn, (0, torch.randn(3, 4)))

Copy to clipboard

Restrictions:

> *   body\_fn must return tensors or int with the same metadata (e.g.shape, dtype) as inputs.
>     
> *   body\_fn and cond\_fn must not in-place mutate the carried\_inputs. A clone before the mutation is required.
>     
> *   body\_fn and cond\_fn must not mutate python variables (e.g. list/dict) created outside of the body\_fn.
>     
> *   body\_fn and cond\_fn’s output cannot alias any of the inputs. A clone is required.
>     
> *   During inference, body\_fn and cond\_fn can in-place mutate tensors that are not carried\_inputs, such as module buffers and captured tensors from the enclosing scope.
>     

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/while_loop.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/while_loop.md.txt)

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