Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/exportdb/python.closure.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/exportdb/python.closure.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/exportdb/python.closure.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/exportdb/python.closure.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/exportdb/python.closure.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/exportdb/python.closure.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/exportdb/python.closure.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/exportdb/python.closure.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/exportdb/python.closure.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/exportdb/python.closure.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/exportdb/python.closure.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/exportdb/python.closure.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/exportdb/python.closure.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/exportdb/python.closure.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/exportdb/python.closure.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/exportdb/python.closure.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/exportdb/python.closure.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/exportdb/python.closure.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/exportdb/python.closure.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/exportdb/python.closure.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/exportdb/python.closure.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/exportdb/python.closure.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/exportdb/python.closure.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/exportdb/python.closure.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/exportdb/python.closure.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/exportdb/python.closure.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/exportdb/python.closure.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/exportdb/python.closure.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/exportdb/python.closure.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/exportdb/python.closure.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/exportdb/python.closure.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/exportdb/python.closure.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/exportdb/python.closure.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/exportdb/python.closure.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/exportdb/python.closure.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/exportdb/python.closure.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/exportdb/python.closure.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/exportdb/python.closure.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/exportdb/python.closure.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/exportdb/python.closure.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/exportdb/python.closure.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/exportdb/python.closure.html)

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

python.closure[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#python-closure "Link to this heading")

===================================================================================================================================

cond\_closed\_over\_variable[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#cond-closed-over-variable "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

Tags: [python.closure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#)
, [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class CondClosedOverVariable(torch.nn.Module):
    """
    torch.cond() supports branches closed over arbitrary variables.
    """

    def forward(self, pred, x):
        def true\_fn(val):
            return x \* 2

        def false\_fn(val):
            return x \- 2

        return cond(pred, true\_fn, false\_fn, \[x + 1\])

example\_args \= (torch.tensor(True), torch.randn(3, 2))
tags \= {"torch.cond", "python.closure"}
model \= CondClosedOverVariable()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, pred: "b8\[\]", x: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 1);  add \= None
            true\_graph\_0 \= self.true\_graph\_0
            false\_graph\_0 \= self.false\_graph\_0
            cond \= torch.ops.higher\_order.cond(pred, true\_graph\_0, false\_graph\_0, (x,));  pred \= true\_graph\_0 \= false\_graph\_0 \= x \= None
            getitem: "f32\[3, 2\]" \= cond\[0\];  cond \= None
            return (getitem,)

        class true\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[3, 2\]"):
                        mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(x, 2);  x \= None
                return (mul,)

        class false\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[3, 2\]"):
                        sub: "f32\[3, 2\]" \= torch.ops.aten.sub.Tensor(x, 2);  x \= None
                return (sub,)

Graph signature:
    \# inputs
    pred: USER\_INPUT
    x: USER\_INPUT

    \# outputs
    getitem: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

nested\_function[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#nested-function "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Note

Tags: [python.closure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html#)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class NestedFunction(torch.nn.Module):
    """
    Nested functions are traced through. Side effects on global captures
    are not supported though.
    """

    def forward(self, a, b):
        x \= a + b
        z \= a \- b

        def closure(y):
            nonlocal x
            x += 1
            return x \* y + z

        return closure(x)

example\_args \= (torch.randn(3, 2), torch.randn(2))
tags \= {"python.closure"}
model \= NestedFunction()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, a: "f32\[3, 2\]", b: "f32\[2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(a, b)

                sub: "f32\[3, 2\]" \= torch.ops.aten.sub.Tensor(a, b);  a \= b \= None

                add\_: "f32\[3, 2\]" \= torch.ops.aten.add\_.Tensor(add, 1);  add \= None

                mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(add\_, add\_);  add\_ \= None
            add\_1: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(mul, sub);  mul \= sub \= None
            return (add\_1,)

Graph signature:
    \# inputs
    a: USER\_INPUT
    b: USER\_INPUT

    \# outputs
    add\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/exportdb/python.closure.rst.txt)

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