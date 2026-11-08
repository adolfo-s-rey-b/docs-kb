Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.GRU.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GRU.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.GRU.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.GRU.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.GRU.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.GRU.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.GRU.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.GRU.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.GRU.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.GRU.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.GRU.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.GRU.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.GRU.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.GRU.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.GRU.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.GRU.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.GRU.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.GRU.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.GRU.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.GRU.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.GRU.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.GRU.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.GRU.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.GRU.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.GRU.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.GRU.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.GRU.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.GRU.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.GRU.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.GRU.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.GRU.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.GRU.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.GRU.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.GRU.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.GRU.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.GRU.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.GRU.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.GRU.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.GRU.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.GRU.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.GRU.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.GRU.html)

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

GRU[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html#gru "Link to this heading")

==================================================================================================

_class_ torch.nn.GRU(_input\_size_, _hidden\_size_, _num\_layers\=1_, _bias\=True_, _batch\_first\=False_, _dropout\=0.0_, _bidirectional\=False_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/rnn.py#L1207)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html#torch.nn.GRU "Link to this definition")

Apply a multi-layer gated recurrent unit (GRU) RNN to an input sequence. For each element in the input sequence, each layer computes the following function:

rt\=σ(Wirxt+bir+Whrh(t−1)+bhr)zt\=σ(Wizxt+biz+Whzh(t−1)+bhz)nt\=tanh⁡(Winxt+bin+rt⊙(Whnh(t−1)+bhn))ht\=(1−zt)⊙nt+zt⊙h(t−1)\\begin{array}{ll} r\_t = \\sigma(W\_{ir} x\_t + b\_{ir} + W\_{hr} h\_{(t-1)} + b\_{hr}) \\\\ z\_t = \\sigma(W\_{iz} x\_t + b\_{iz} + W\_{hz} h\_{(t-1)} + b\_{hz}) \\\\ n\_t = \\tanh(W\_{in} x\_t + b\_{in} + r\_t \\odot (W\_{hn} h\_{(t-1)}+ b\_{hn})) \\\\ h\_t = (1 - z\_t) \\odot n\_t + z\_t \\odot h\_{(t-1)} \\end{array} rt​\=σ(Wir​xt​+bir​+Whr​h(t−1)​+bhr​)zt​\=σ(Wiz​xt​+biz​+Whz​h(t−1)​+bhz​)nt​\=tanh(Win​xt​+bin​+rt​⊙(Whn​h(t−1)​+bhn​))ht​\=(1−zt​)⊙nt​+zt​⊙h(t−1)​​

where hth\_tht​ is the hidden state at time t, xtx\_txt​ is the input at time t, h(t−1)h\_{(t-1)}h(t−1)​ is the hidden state of the layer at time t-1 or the initial hidden state at time 0, and rtr\_trt​, ztz\_tzt​, ntn\_tnt​ are the reset, update, and new gates, respectively. σ\\sigmaσ is the sigmoid function, and ⊙\\odot⊙ is the Hadamard product.

In a multilayer GRU, the input xt(l)x^{(l)}\_txt(l)​ of the lll -th layer (l≥2l \\ge 2l≥2) is the hidden state ht(l−1)h^{(l-1)}\_tht(l−1)​ of the previous layer multiplied by dropout δt(l−1)\\delta^{(l-1)}\_tδt(l−1)​ where each δt(l−1)\\delta^{(l-1)}\_tδt(l−1)​ is a Bernoulli random variable which is 000 with probability `dropout`.

Parameters:

*   **input\_size** – The number of expected features in the input x
    
*   **hidden\_size** – The number of features in the hidden state h
    
*   **num\_layers** – Number of recurrent layers. E.g., setting `num_layers=2` would mean stacking two GRUs together to form a stacked GRU, with the second GRU taking in outputs of the first GRU and computing the final results. Default: 1
    
*   **bias** – If `False`, then the layer does not use bias weights b\_ih and b\_hh. Default: `True`
    
*   **batch\_first** – If `True`, then the input and output tensors are provided as (batch, seq, feature) instead of (seq, batch, feature). Note that this does not apply to hidden or cell states. See the Inputs/Outputs sections below for details. Default: `False`
    
*   **dropout** – If non-zero, introduces a Dropout layer on the outputs of each GRU layer except the last layer, with dropout probability equal to `dropout`. Default: 0
    
*   **bidirectional** – If `True`, becomes a bidirectional GRU. Default: `False`
    

Inputs: input, h\_0

*   **input**: tensor of shape (L,Hin)(L, H\_{in})(L,Hin​) for unbatched input, (L,N,Hin)(L, N, H\_{in})(L,N,Hin​) when `batch_first=False` or (N,L,Hin)(N, L, H\_{in})(N,L,Hin​) when `batch_first=True` containing the features of the input sequence. The input can also be a packed variable length sequence. See [`torch.nn.utils.rnn.pack_padded_sequence()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.rnn.pack_padded_sequence.html#torch.nn.utils.rnn.pack_padded_sequence "torch.nn.utils.rnn.pack_padded_sequence")
     or [`torch.nn.utils.rnn.pack_sequence()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.rnn.pack_sequence.html#torch.nn.utils.rnn.pack_sequence "torch.nn.utils.rnn.pack_sequence")
     for details.
    
*   **h\_0**: tensor of shape (D∗num\_layers,Hout)(D \* \\text{num\\\_layers}, H\_{out})(D∗num\_layers,Hout​) or (D∗num\_layers,N,Hout)(D \* \\text{num\\\_layers}, N, H\_{out})(D∗num\_layers,N,Hout​) containing the initial hidden state for the input sequence. Defaults to zeros if not provided.
    

where:

N\=batch sizeL\=sequence lengthD\=2 if bidirectional=True otherwise 1Hin\=input\_sizeHout\=hidden\_size\\begin{aligned} N ={} & \\text{batch size} \\\\ L ={} & \\text{sequence length} \\\\ D ={} & 2 \\text{ if bidirectional=True otherwise } 1 \\\\ H\_{in} ={} & \\text{input\\\_size} \\\\ H\_{out} ={} & \\text{hidden\\\_size} \\end{aligned} N\=L\=D\=Hin​\=Hout​\=​batch sizesequence length2 if bidirectional=True otherwise 1input\_sizehidden\_size​

Outputs: output, h\_n

*   **output**: tensor of shape (L,D∗Hout)(L, D \* H\_{out})(L,D∗Hout​) for unbatched input, (L,N,D∗Hout)(L, N, D \* H\_{out})(L,N,D∗Hout​) when `batch_first=False` or (N,L,D∗Hout)(N, L, D \* H\_{out})(N,L,D∗Hout​) when `batch_first=True` containing the output features (h\_t) from the last layer of the GRU, for each t. If a [`torch.nn.utils.rnn.PackedSequence`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence "torch.nn.utils.rnn.PackedSequence")
     has been given as the input, the output will also be a packed sequence.
    
*   **h\_n**: tensor of shape (D∗num\_layers,Hout)(D \* \\text{num\\\_layers}, H\_{out})(D∗num\_layers,Hout​) or (D∗num\_layers,N,Hout)(D \* \\text{num\\\_layers}, N, H\_{out})(D∗num\_layers,N,Hout​) containing the final hidden state for the input sequence.
    

Variables:

*   **weight\_ih\_l\[k\]** – the learnable input-hidden weights of the kth\\text{k}^{th}kth layer (W\_ir|W\_iz|W\_in), of shape (3\*hidden\_size, input\_size) for k = 0. Otherwise, the shape is (3\*hidden\_size, num\_directions \* hidden\_size)
    
*   **weight\_hh\_l\[k\]** – the learnable hidden-hidden weights of the kth\\text{k}^{th}kth layer (W\_hr|W\_hz|W\_hn), of shape (3\*hidden\_size, hidden\_size)
    
*   **bias\_ih\_l\[k\]** – the learnable input-hidden bias of the kth\\text{k}^{th}kth layer (b\_ir|b\_iz|b\_in), of shape (3\*hidden\_size)
    
*   **bias\_hh\_l\[k\]** – the learnable hidden-hidden bias of the kth\\text{k}^{th}kth layer (b\_hr|b\_hz|b\_hn), of shape (3\*hidden\_size)
    

Note

All the weights and biases are initialized from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​) where k\=1hidden\_sizek = \\frac{1}{\\text{hidden\\\_size}}k\=hidden\_size1​

Note

For bidirectional GRUs, forward and backward are directions 0 and 1 respectively. Example of splitting the output layers when `batch_first=False`: `output.view(seq_len, batch, num_directions, hidden_size)`.

Note

`batch_first` argument is ignored for unbatched inputs.

Note

The calculation of new gate ntn\_tnt​ subtly differs from the original paper and other frameworks. In the original implementation, the Hadamard product (⊙)(\\odot)(⊙) between rtr\_trt​ and the previous hidden state h(t−1)h\_{(t-1)}h(t−1)​ is done before the multiplication with the weight matrix W and addition of bias:

nt\=tanh⁡(Winxt+bin+Whn(rt⊙h(t−1))+bhn)\\begin{aligned} n\_t = \\tanh(W\_{in} x\_t + b\_{in} + W\_{hn} ( r\_t \\odot h\_{(t-1)} ) + b\_{hn}) \\end{aligned} nt​\=tanh(Win​xt​+bin​+Whn​(rt​⊙h(t−1)​)+bhn​)​

This is in contrast to PyTorch implementation, which is done after Whnh(t−1)W\_{hn} h\_{(t-1)}Whn​h(t−1)​

nt\=tanh⁡(Winxt+bin+rt⊙(Whnh(t−1)+bhn))\\begin{aligned} n\_t = \\tanh(W\_{in} x\_t + b\_{in} + r\_t \\odot (W\_{hn} h\_{(t-1)}+ b\_{hn})) \\end{aligned} nt​\=tanh(Win​xt​+bin​+rt​⊙(Whn​h(t−1)​+bhn​))​

This implementation differs on purpose for efficiency.

Note

If the following conditions are satisfied: 1) cudnn is enabled, 2) input data is on the GPU 3) input data has dtype `torch.float16` 4) V100 GPU is used, 5) input data is not in `PackedSequence` format persistent algorithm can be selected to improve performance.

Examples:

\>>> rnn \= nn.GRU(10, 20, 2)
\>>> input \= torch.randn(5, 3, 10)
\>>> h0 \= torch.randn(2, 3, 20)
\>>> output, hn \= rnn(input, h0)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.GRU.rst.txt)

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