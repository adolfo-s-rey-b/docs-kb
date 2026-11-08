Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/exportdb/python.assert.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/exportdb/python.assert.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/exportdb/python.assert.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/exportdb/python.assert.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/exportdb/python.assert.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/exportdb/python.assert.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/exportdb/python.assert.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/exportdb/python.assert.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/exportdb/python.assert.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/exportdb/python.assert.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/exportdb/python.assert.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/exportdb/python.assert.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/exportdb/python.assert.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/exportdb/python.assert.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/exportdb/python.assert.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/exportdb/python.assert.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/exportdb/python.assert.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/exportdb/python.assert.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/exportdb/python.assert.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/exportdb/python.assert.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/exportdb/python.assert.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/exportdb/python.assert.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/exportdb/python.assert.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/exportdb/python.assert.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/exportdb/python.assert.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/exportdb/python.assert.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/exportdb/python.assert.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/exportdb/python.assert.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/exportdb/python.assert.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/exportdb/python.assert.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/exportdb/python.assert.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/exportdb/python.assert.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/exportdb/python.assert.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/exportdb/python.assert.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/exportdb/python.assert.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/exportdb/python.assert.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/exportdb/python.assert.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/exportdb/python.assert.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/exportdb/python.assert.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/exportdb/python.assert.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/exportdb/python.assert.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/exportdb/python.assert.html)

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

python.assert[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#python-assert "Link to this heading")

================================================================================================================================

dynamic\_shape\_assert[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#dynamic-shape-assert "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Note

Tags: [python.assert](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeAssert(torch.nn.Module):
    """
    A basic usage of python assertion.
    """

    def forward(self, x):
        \# assertion with error message
        assert x.shape\[0\] \> 2, f"{x.shape\[0\]} is greater than 2"  \# noqa: S101
        \# assertion without error message
        assert x.shape\[0\] \> 1  \# noqa: S101
        return x

example\_args \= (torch.randn(3, 2),)
tags \= {"python.assert"}
model \= DynamicShapeAssert()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
            return (x,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    x: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

list\_contains[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#list-contains "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Note

Tags: [python.assert](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html#)
, [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ListContains(torch.nn.Module):
    """
    List containment relation can be checked on a dynamic shape or constants.
    """

    def forward(self, x):
        assert x.size(\-1) in \[6, 2\]  \# noqa: S101
        assert x.size(0) not in \[4, 5, 6\]  \# noqa: S101
        assert "monkey" not in \["cow", "pig"\]  \# noqa: S101
        return x + x

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.dynamic-shape", "python.data-structure", "python.assert"}
model \= ListContains()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, x);  x \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/exportdb/python.assert.rst.txt)

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