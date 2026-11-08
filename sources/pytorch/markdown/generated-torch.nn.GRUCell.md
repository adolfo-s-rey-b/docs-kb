Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRUCell.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.GRUCell.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRUCell.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GRUCell.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.GRUCell.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.GRUCell.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.GRUCell.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.GRUCell.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.GRUCell.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.GRUCell.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.GRUCell.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.GRUCell.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.GRUCell.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.GRUCell.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.GRUCell.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.GRUCell.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.GRUCell.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.GRUCell.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.GRUCell.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.GRUCell.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.GRUCell.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.GRUCell.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.GRUCell.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.GRUCell.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.GRUCell.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.GRUCell.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.GRUCell.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.GRUCell.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.GRUCell.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.GRUCell.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.GRUCell.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.GRUCell.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.GRUCell.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.GRUCell.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.GRUCell.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.GRUCell.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.GRUCell.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.GRUCell.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.GRUCell.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.GRUCell.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.GRUCell.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.GRUCell.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.GRUCell.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.GRUCell.html)

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

GRUCell[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRUCell.html#grucell "Link to this heading")

==============================================================================================================

_class_ torch.nn.GRUCell(_input\_size_, _hidden\_size_, _bias\=True_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/rnn.py#L1772)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRUCell.html#torch.nn.GRUCell "Link to this definition")

A gated recurrent unit (GRU) cell.

r\=σ(Wirx+bir+Whrh+bhr)z\=σ(Wizx+biz+Whzh+bhz)n\=tanh⁡(Winx+bin+r⊙(Whnh+bhn))h′\=(1−z)⊙n+z⊙h\\begin{array}{ll} r = \\sigma(W\_{ir} x + b\_{ir} + W\_{hr} h + b\_{hr}) \\\\ z = \\sigma(W\_{iz} x + b\_{iz} + W\_{hz} h + b\_{hz}) \\\\ n = \\tanh(W\_{in} x + b\_{in} + r \\odot (W\_{hn} h + b\_{hn})) \\\\ h' = (1 - z) \\odot n + z \\odot h \\end{array}r\=σ(Wir​x+bir​+Whr​h+bhr​)z\=σ(Wiz​x+biz​+Whz​h+bhz​)n\=tanh(Win​x+bin​+r⊙(Whn​h+bhn​))h′\=(1−z)⊙n+z⊙h​

where σ\\sigmaσ is the sigmoid function, and ⊙\\odot⊙ is the Hadamard product.

Parameters:

*   **input\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The number of expected features in the input x
    
*   **hidden\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The number of features in the hidden state h
    
*   **bias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `False`, then the layer does not use bias weights b\_ih and b\_hh. Default: `True`
    

Inputs: input, hidden

*   **input** : tensor containing input features
    
*   **hidden** : tensor containing the initial hidden state for each element in the batch. Defaults to zero if not provided.
    

Outputs: h’

*   **h’** : tensor containing the next hidden state for each element in the batch
    

Shape:

*   input: (N,Hin)(N, H\_{in})(N,Hin​) or (Hin)(H\_{in})(Hin​) tensor containing input features where HinH\_{in}Hin​ = input\_size.
    
*   hidden: (N,Hout)(N, H\_{out})(N,Hout​) or (Hout)(H\_{out})(Hout​) tensor containing the initial hidden state where HoutH\_{out}Hout​ = hidden\_size. Defaults to zero if not provided.
    
*   output: (N,Hout)(N, H\_{out})(N,Hout​) or (Hout)(H\_{out})(Hout​) tensor containing the next hidden state.
    

Variables:

*   **weight\_ih** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the learnable input-hidden weights, of shape (3\*hidden\_size, input\_size)
    
*   **weight\_hh** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the learnable hidden-hidden weights, of shape (3\*hidden\_size, hidden\_size)
    
*   **bias\_ih** – the learnable input-hidden bias, of shape (3\*hidden\_size)
    
*   **bias\_hh** – the learnable hidden-hidden bias, of shape (3\*hidden\_size)
    

Note

All the weights and biases are initialized from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​) where k\=1hidden\_sizek = \\frac{1}{\\text{hidden\\\_size}}k\=hidden\_size1​

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Examples:

\>>> rnn \= nn.GRUCell(10, 20)
\>>> input \= torch.randn(6, 3, 10)
\>>> hx \= torch.randn(3, 20)
\>>> output \= \[\]
\>>> for i in range(6):
...     hx \= rnn(input\[i\], hx)
...     output.append(hx)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.GRUCell.rst.txt)

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