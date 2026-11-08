Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Embedding.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Embedding.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Embedding.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Embedding.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Embedding.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Embedding.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Embedding.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Embedding.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Embedding.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Embedding.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Embedding.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Embedding.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Embedding.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Embedding.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Embedding.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Embedding.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Embedding.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Embedding.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Embedding.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Embedding.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Embedding.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Embedding.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Embedding.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Embedding.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Embedding.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Embedding.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Embedding.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Embedding.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Embedding.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Embedding.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Embedding.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Embedding.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Embedding.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Embedding.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Embedding.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Embedding.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Embedding.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Embedding.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Embedding.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Embedding.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Embedding.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Embedding.html)

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

Embedding[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#embedding "Link to this heading")

====================================================================================================================

_class_ torch.nn.Embedding(_num\_embeddings_, _embedding\_dim_, _padding\_idx\=None_, _max\_norm\=None_, _norm\_type\=2.0_, _scale\_grad\_by\_freq\=False_, _sparse\=False_, _\_weight\=None_, _\_freeze\=False_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/sparse.py#L14)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#torch.nn.Embedding "Link to this definition")

A simple lookup table that stores embeddings of a fixed dictionary and size.

This module is often used to store word embeddings and retrieve them using indices. The input to the module is a list of indices, and the output is the corresponding word embeddings.

Parameters:

*   **num\_embeddings** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – size of the dictionary of embeddings
    
*   **embedding\_dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the size of each embedding vector
    
*   **padding\_idx** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – If specified, the entries at `padding_idx` do not contribute to the gradient; therefore, the embedding vector at `padding_idx` is not updated during training, i.e. it remains as a fixed “pad”. For a newly constructed Embedding, the embedding vector at `padding_idx` will default to all zeros, but can be updated to another value to be used as the padding vector.
    
*   **max\_norm** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – If given, each embedding vector with norm larger than `max_norm` is renormalized to have norm `max_norm`.
    
*   **norm\_type** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – The p of the p-norm to compute for the `max_norm` option. Default `2`.
    
*   **scale\_grad\_by\_freq** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If given, this will scale gradients by the inverse of frequency of the words in the mini-batch. Default `False`.
    
*   **sparse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, gradient w.r.t. `weight` matrix will be a sparse tensor. See Notes for more details regarding sparse gradients.
    

Variables:

**weight** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the learnable weights of the module of shape (num\_embeddings, embedding\_dim) initialized from N(0,1)\\mathcal{N}(0, 1)N(0,1)

Shape:

*   Input: (∗)(\*)(∗), IntTensor or LongTensor of arbitrary shape containing the indices to extract
    
*   Output: (∗,H)(\*, H)(∗,H), where \* is the input shape and H\=embedding\_dimH=\\text{embedding\\\_dim}H\=embedding\_dim
    

Note

Keep in mind that only a limited number of optimizers support sparse gradients: currently it’s `optim.SGD` (CUDA and CPU), `optim.SparseAdam` (CUDA and CPU) and `optim.Adagrad` (CPU)

Note

When `max_norm` is not `None`, [`Embedding`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#torch.nn.Embedding "torch.nn.Embedding")
’s forward method will modify the `weight` tensor in-place. Since tensors needed for gradient computations cannot be modified in-place, performing a differentiable operation on `Embedding.weight` before calling [`Embedding`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#torch.nn.Embedding "torch.nn.Embedding")
’s forward method requires cloning `Embedding.weight` when `max_norm` is not `None`. For example:

n, d, m \= 3, 5, 7
embedding \= nn.Embedding(n, d, max\_norm\=1.0)
W \= torch.randn((m, d), requires\_grad\=True)
idx \= torch.tensor(\[1, 2\])
a \= (
    embedding.weight.clone() @ W.t()
)  \# weight must be cloned for this to be differentiable
b \= embedding(idx) @ W.t()  \# modifies weight in-place
out \= a.unsqueeze(0) + b.unsqueeze(1)
loss \= out.sigmoid().prod()
loss.backward()

Copy to clipboard

Examples:

\>>> \# an Embedding module containing 10 tensors of size 3
\>>> embedding \= nn.Embedding(10, 3)
\>>> \# a batch of 2 samples of 4 indices each
\>>> input \= torch.LongTensor(\[\[1, 2, 4, 5\], \[4, 3, 2, 9\]\])
\>>> embedding(input)
tensor(\[\[\[-0.0251, -1.6902,  0.7172\],\
         \[-0.6431,  0.0748,  0.6969\],\
         \[ 1.4970,  1.3448, -0.9685\],\
         \[-0.3677, -2.7265, -0.1685\]\],\
\
        \[\[ 1.4970,  1.3448, -0.9685\],\
         \[ 0.4362, -0.4004,  0.9400\],\
         \[-0.6431,  0.0748,  0.6969\],\
         \[ 0.9124, -2.3616,  1.1151\]\]\])

\>>> \# example with padding\_idx
\>>> embedding \= nn.Embedding(10, 3, padding\_idx\=0)
\>>> input \= torch.LongTensor(\[\[0, 2, 0, 5\]\])
\>>> embedding(input)
tensor(\[\[\[ 0.0000,  0.0000,  0.0000\],\
         \[ 0.1535, -2.0309,  0.9315\],\
         \[ 0.0000,  0.0000,  0.0000\],\
         \[-0.1655,  0.9897,  0.0635\]\]\])

\>>> \# example of changing \`pad\` vector
\>>> padding\_idx \= 0
\>>> embedding \= nn.Embedding(3, 3, padding\_idx\=padding\_idx)
\>>> embedding.weight
Parameter containing:
tensor(\[\[ 0.0000,  0.0000,  0.0000\],\
        \[-0.7895, -0.7089, -0.0364\],\
        \[ 0.6778,  0.5803,  0.2678\]\], requires\_grad=True)
\>>> with torch.no\_grad():
...     embedding.weight\[padding\_idx\] \= torch.ones(3)
\>>> embedding.weight
Parameter containing:
tensor(\[\[ 1.0000,  1.0000,  1.0000\],\
        \[-0.7895, -0.7089, -0.0364\],\
        \[ 0.6778,  0.5803,  0.2678\]\], requires\_grad=True)

Copy to clipboard

_classmethod_ from\_pretrained(_embeddings_, _freeze\=True_, _padding\_idx\=None_, _max\_norm\=None_, _norm\_type\=2.0_, _scale\_grad\_by\_freq\=False_, _sparse\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/sparse.py#L213)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html#torch.nn.Embedding.from_pretrained "Link to this definition")

Create Embedding instance from given 2-dimensional FloatTensor.

Parameters:

*   **embeddings** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – FloatTensor containing weights for the Embedding. First dimension is being passed to Embedding as `num_embeddings`, second as `embedding_dim`.
    
*   **freeze** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, the tensor does not get updated in the learning process. Equivalent to `embedding.weight.requires_grad = False`. Default: `True`
    
*   **padding\_idx** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – If specified, the entries at `padding_idx` do not contribute to the gradient; therefore, the embedding vector at `padding_idx` is not updated during training, i.e. it remains as a fixed “pad”.
    
*   **max\_norm** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – See module initialization documentation.
    
*   **norm\_type** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – See module initialization documentation. Default `2`.
    
*   **scale\_grad\_by\_freq** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – See module initialization documentation. Default `False`.
    
*   **sparse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – See module initialization documentation.
    

Examples:

\>>> \# FloatTensor containing pretrained weights
\>>> weight \= torch.FloatTensor(\[\[1, 2.3, 3\], \[4, 5.1, 6.3\]\])
\>>> embedding \= nn.Embedding.from\_pretrained(weight)
\>>> \# Get embeddings for index 1
\>>> input \= torch.LongTensor(\[1\])
\>>> embedding(input)
tensor(\[\[ 4.0000,  5.1000,  6.3000\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Embedding.rst.txt)

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