Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/exportdb/torch.operator.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/exportdb/torch.operator.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/exportdb/torch.operator.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/exportdb/torch.operator.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/exportdb/torch.operator.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/exportdb/torch.operator.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/exportdb/torch.operator.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/exportdb/torch.operator.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/exportdb/torch.operator.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/exportdb/torch.operator.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/exportdb/torch.operator.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/exportdb/torch.operator.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/exportdb/torch.operator.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/exportdb/torch.operator.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/exportdb/torch.operator.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/exportdb/torch.operator.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/exportdb/torch.operator.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/exportdb/torch.operator.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/exportdb/torch.operator.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/exportdb/torch.operator.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/exportdb/torch.operator.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/exportdb/torch.operator.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/exportdb/torch.operator.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/exportdb/torch.operator.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/exportdb/torch.operator.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/exportdb/torch.operator.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/exportdb/torch.operator.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/exportdb/torch.operator.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/exportdb/torch.operator.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/exportdb/torch.operator.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/exportdb/torch.operator.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/exportdb/torch.operator.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/exportdb/torch.operator.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/exportdb/torch.operator.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/exportdb/torch.operator.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/exportdb/torch.operator.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/exportdb/torch.operator.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/exportdb/torch.operator.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/exportdb/torch.operator.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/exportdb/torch.operator.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/exportdb/torch.operator.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/exportdb/torch.operator.html)

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

torch.operator[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html#torch-operator "Link to this heading")

===================================================================================================================================

unsupported\_operator[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html#unsupported-operator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Note

Tags: [torch.operator](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html#)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch
from torch.\_export.db.case import SupportLevel

class TorchSymMin(torch.nn.Module):
    """
    torch.sym\_min operator is supported in export.
    """

    def forward(self, x):
        return x.sum() + torch.sym\_min(x.size(0), 100)

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.operator"}
support\_level \= SupportLevel.SUPPORTED
model \= TorchSymMin()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                sum\_1: "f32\[\]" \= torch.ops.aten.sum.default(x);  x \= None
            add: "f32\[\]" \= torch.ops.aten.add.Tensor(sum\_1, 3);  sum\_1 \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/exportdb/torch.operator.rst.txt)

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