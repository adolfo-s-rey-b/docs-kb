Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nn.functional.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nn.functional.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nn.functional.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nn.functional.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nn.functional.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nn.functional.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nn.functional.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nn.functional.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nn.functional.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nn.functional.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nn.functional.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nn.functional.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nn.functional.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nn.functional.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nn.functional.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nn.functional.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nn.functional.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nn.functional.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nn.functional.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nn.functional.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nn.functional.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nn.functional.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nn.functional.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nn.functional.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nn.functional.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nn.functional.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nn.functional.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nn.functional.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nn.functional.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nn.functional.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nn.functional.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nn.functional.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nn.functional.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nn.functional.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nn.functional.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nn.functional.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nn.functional.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nn.functional.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nn.functional.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nn.functional.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nn.functional.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nn.functional.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nn.functional.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nn.functional.html)

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

torch.nn.functional[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#torch-nn-functional "Link to this heading")

=========================================================================================================================

Created On: Jun 11, 2019 | Last Updated On: Sep 08, 2026

Convolution functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#convolution-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`conv1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv1d.html#torch.nn.functional.conv1d "torch.nn.functional.conv1d") | Applies a 1D convolution over an input signal composed of several input planes. |
| [`conv2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv2d.html#torch.nn.functional.conv2d "torch.nn.functional.conv2d") | Applies a 2D convolution over an input image composed of several input planes. |
| [`conv3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv3d.html#torch.nn.functional.conv3d "torch.nn.functional.conv3d") | Applies a 3D convolution over an input image composed of several input planes. |
| [`conv_transpose1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv_transpose1d.html#torch.nn.functional.conv_transpose1d "torch.nn.functional.conv_transpose1d") | Applies a 1D transposed convolution operator over an input signal composed of several input planes, sometimes also called "deconvolution". |
| [`conv_transpose2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv_transpose2d.html#torch.nn.functional.conv_transpose2d "torch.nn.functional.conv_transpose2d") | Applies a 2D transposed convolution operator over an input image composed of several input planes, sometimes also called "deconvolution". |
| [`conv_transpose3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.conv_transpose3d.html#torch.nn.functional.conv_transpose3d "torch.nn.functional.conv_transpose3d") | Applies a 3D transposed convolution operator over an input image composed of several input planes, sometimes also called "deconvolution" |
| [`unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.unfold.html#torch.nn.functional.unfold "torch.nn.functional.unfold") | Extract sliding local blocks from a batched input tensor. |
| [`fold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.fold.html#torch.nn.functional.fold "torch.nn.functional.fold") | Combine an array of sliding local blocks into a large containing tensor. |

Pooling functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#pooling-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`avg_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.avg_pool1d.html#torch.nn.functional.avg_pool1d "torch.nn.functional.avg_pool1d") | Applies a 1D average pooling over an input signal composed of several input planes. |
| [`avg_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.avg_pool2d.html#torch.nn.functional.avg_pool2d "torch.nn.functional.avg_pool2d") | Applies 2D average-pooling operation in kH×kWkH \\times kWkH×kW regions by step size sH×sWsH \\times sWsH×sW steps. |
| [`avg_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.avg_pool3d.html#torch.nn.functional.avg_pool3d "torch.nn.functional.avg_pool3d") | Applies 3D average-pooling operation in kT×kH×kWkT \\times kH \\times kWkT×kH×kW regions by step size sT×sH×sWsT \\times sH \\times sWsT×sH×sW steps. |
| [`max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_pool1d.html#torch.nn.functional.max_pool1d "torch.nn.functional.max_pool1d") | Applies a 1D max pooling over an input signal composed of several input planes. |
| [`max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_pool2d.html#torch.nn.functional.max_pool2d "torch.nn.functional.max_pool2d") | Applies a 2D max pooling over an input signal composed of several input planes. |
| [`max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_pool3d.html#torch.nn.functional.max_pool3d "torch.nn.functional.max_pool3d") | Applies a 3D max pooling over an input signal composed of several input planes. |
| [`max_unpool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_unpool1d.html#torch.nn.functional.max_unpool1d "torch.nn.functional.max_unpool1d") | Compute a partial inverse of `MaxPool1d`. |
| [`max_unpool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_unpool2d.html#torch.nn.functional.max_unpool2d "torch.nn.functional.max_unpool2d") | Compute a partial inverse of `MaxPool2d`. |
| [`max_unpool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.max_unpool3d.html#torch.nn.functional.max_unpool3d "torch.nn.functional.max_unpool3d") | Compute a partial inverse of `MaxPool3d`. |
| [`lp_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.lp_pool1d.html#torch.nn.functional.lp_pool1d "torch.nn.functional.lp_pool1d") | Apply a 1D power-average pooling over an input signal composed of several input planes. |
| [`lp_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.lp_pool2d.html#torch.nn.functional.lp_pool2d "torch.nn.functional.lp_pool2d") | Apply a 2D power-average pooling over an input signal composed of several input planes. |
| [`lp_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.lp_pool3d.html#torch.nn.functional.lp_pool3d "torch.nn.functional.lp_pool3d") | Apply a 3D power-average pooling over an input signal composed of several input planes. |
| [`adaptive_max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_max_pool1d.html#torch.nn.functional.adaptive_max_pool1d "torch.nn.functional.adaptive_max_pool1d") | Applies a 1D adaptive max pooling over an input signal composed of several input planes. |
| [`adaptive_max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_max_pool2d.html#torch.nn.functional.adaptive_max_pool2d "torch.nn.functional.adaptive_max_pool2d") | Applies a 2D adaptive max pooling over an input signal composed of several input planes. |
| [`adaptive_max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_max_pool3d.html#torch.nn.functional.adaptive_max_pool3d "torch.nn.functional.adaptive_max_pool3d") | Applies a 3D adaptive max pooling over an input signal composed of several input planes. |
| [`adaptive_avg_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_avg_pool1d.html#torch.nn.functional.adaptive_avg_pool1d "torch.nn.functional.adaptive_avg_pool1d") | Applies a 1D adaptive average pooling over an input signal composed of several input planes. |
| [`adaptive_avg_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_avg_pool2d.html#torch.nn.functional.adaptive_avg_pool2d "torch.nn.functional.adaptive_avg_pool2d") | Apply a 2D adaptive average pooling over an input signal composed of several input planes. |
| [`adaptive_avg_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.adaptive_avg_pool3d.html#torch.nn.functional.adaptive_avg_pool3d "torch.nn.functional.adaptive_avg_pool3d") | Apply a 3D adaptive average pooling over an input signal composed of several input planes. |
| [`fractional_max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.fractional_max_pool2d.html#torch.nn.functional.fractional_max_pool2d "torch.nn.functional.fractional_max_pool2d") | Applies 2D fractional max pooling over an input signal composed of several input planes. |
| [`fractional_max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.fractional_max_pool3d.html#torch.nn.functional.fractional_max_pool3d "torch.nn.functional.fractional_max_pool3d") | Applies 3D fractional max pooling over an input signal composed of several input planes. |

Attention Mechanisms[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#attention-mechanisms "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The [`torch.nn.attention.bias`](https://docs.pytorch.org/docs/2.15/nn.attention.bias.html#module-torch.nn.attention.bias "torch.nn.attention.bias")
 module contains attention\_biases that are designed to be used with scaled\_dot\_product\_attention.

|     |     |
| --- | --- |
| [`scaled_dot_product_attention`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_dot_product_attention.html#torch.nn.functional.scaled_dot_product_attention "torch.nn.functional.scaled_dot_product_attention") | scaled\_dot\_product\_attention(query, key, value, attn\_mask=None, dropout\_p=0.0, |

Non-linear activation functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#non-linear-activation-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`threshold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.threshold.html#torch.nn.functional.threshold "torch.nn.functional.threshold") | Apply a threshold to each element of the input Tensor. |
| [`threshold_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.threshold_.html#torch.nn.functional.threshold_ "torch.nn.functional.threshold_") | In-place version of [`threshold()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.threshold.html#torch.nn.functional.threshold "torch.nn.functional.threshold")<br>. |
| [`relu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.relu.html#torch.nn.functional.relu "torch.nn.functional.relu") | Applies the rectified linear unit function element-wise. |
| [`relu_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.relu_.html#torch.nn.functional.relu_ "torch.nn.functional.relu_") | In-place version of [`relu()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.relu.html#torch.nn.functional.relu "torch.nn.functional.relu")<br>. |
| [`hardtanh`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardtanh.html#torch.nn.functional.hardtanh "torch.nn.functional.hardtanh") | Applies the HardTanh function element-wise. |
| [`hardtanh_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardtanh_.html#torch.nn.functional.hardtanh_ "torch.nn.functional.hardtanh_") | In-place version of [`hardtanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardtanh.html#torch.nn.functional.hardtanh "torch.nn.functional.hardtanh")<br>. |
| [`hardswish`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardswish.html#torch.nn.functional.hardswish "torch.nn.functional.hardswish") | Apply hardswish function, element-wise. |
| [`relu6`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.relu6.html#torch.nn.functional.relu6 "torch.nn.functional.relu6") | Applies the element-wise function ReLU6(x)\=min⁡(max⁡(0,x),6)\\text{ReLU6}(x) = \\min(\\max(0,x), 6)ReLU6(x)\=min(max(0,x),6). |
| [`elu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.elu.html#torch.nn.functional.elu "torch.nn.functional.elu") | Apply the Exponential Linear Unit (ELU) function element-wise. |
| [`elu_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.elu_.html#torch.nn.functional.elu_ "torch.nn.functional.elu_") | In-place version of [`elu()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.elu.html#torch.nn.functional.elu "torch.nn.functional.elu")<br>. |
| [`selu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.selu.html#torch.nn.functional.selu "torch.nn.functional.selu") | Applies element-wise, SELU(x)\=scale∗(max⁡(0,x)+min⁡(0,α∗(exp⁡(x)−1)))\\text{SELU}(x) = scale \* (\\max(0,x) + \\min(0, \\alpha \* (\\exp(x) - 1)))SELU(x)\=scale∗(max(0,x)+min(0,α∗(exp(x)−1))), with α\=1.6732632423543772848170429916717\\alpha=1.6732632423543772848170429916717α\=1.6732632423543772848170429916717 and scale\=1.0507009873554804934193349852946scale=1.0507009873554804934193349852946scale\=1.0507009873554804934193349852946. |
| [`celu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.celu.html#torch.nn.functional.celu "torch.nn.functional.celu") | Applies element-wise, CELU(x)\=max⁡(0,x)+min⁡(0,α∗(exp⁡(x/α)−1))\\text{CELU}(x) = \\max(0,x) + \\min(0, \\alpha \* (\\exp(x/\\alpha) - 1))CELU(x)\=max(0,x)+min(0,α∗(exp(x/α)−1)). |
| [`leaky_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.leaky_relu.html#torch.nn.functional.leaky_relu "torch.nn.functional.leaky_relu") | Applies element-wise, LeakyReLU(x)\=max⁡(0,x)+negative\_slope∗min⁡(0,x)\\text{LeakyReLU}(x) = \\max(0, x) + \\text{negative\\\_slope} \* \\min(0, x)LeakyReLU(x)\=max(0,x)+negative\_slope∗min(0,x) |
| [`leaky_relu_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.leaky_relu_.html#torch.nn.functional.leaky_relu_ "torch.nn.functional.leaky_relu_") | In-place version of [`leaky_relu()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.leaky_relu.html#torch.nn.functional.leaky_relu "torch.nn.functional.leaky_relu")<br>. |
| [`prelu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.prelu.html#torch.nn.functional.prelu "torch.nn.functional.prelu") | Applies element-wise the function PReLU(x)\=max⁡(0,x)+weight∗min⁡(0,x)\\text{PReLU}(x) = \\max(0,x) + \\text{weight} \* \\min(0,x)PReLU(x)\=max(0,x)+weight∗min(0,x) where weight is a learnable parameter. |
| [`rrelu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.rrelu.html#torch.nn.functional.rrelu "torch.nn.functional.rrelu") | Randomized leaky ReLU. |
| [`rrelu_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.rrelu_.html#torch.nn.functional.rrelu_ "torch.nn.functional.rrelu_") | In-place version of [`rrelu()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.rrelu.html#torch.nn.functional.rrelu "torch.nn.functional.rrelu")<br>. |
| [`glu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.glu.html#torch.nn.functional.glu "torch.nn.functional.glu") | The gated linear unit. |
| [`gelu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.gelu.html#torch.nn.functional.gelu "torch.nn.functional.gelu") | When the approximate argument is 'none', it applies element-wise the function GELU(x)\=x∗Φ(x)\\text{GELU}(x) = x \* \\Phi(x)GELU(x)\=x∗Φ(x) |
| [`logsigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.logsigmoid.html#torch.nn.functional.logsigmoid "torch.nn.functional.logsigmoid") | Applies element-wise LogSigmoid(xi)\=log⁡(11+exp⁡(−xi))\\text{LogSigmoid}(x\_i) = \\log \\left(\\frac{1}{1 + \\exp(-x\_i)}\\right)LogSigmoid(xi​)\=log(1+exp(−xi​)1​) |
| [`hardshrink`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardshrink.html#torch.nn.functional.hardshrink "torch.nn.functional.hardshrink") | Applies the hard shrinkage function element-wise |
| [`tanhshrink`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.tanhshrink.html#torch.nn.functional.tanhshrink "torch.nn.functional.tanhshrink") | Applies element-wise, Tanhshrink(x)\=x−Tanh(x)\\text{Tanhshrink}(x) = x - \\text{Tanh}(x)Tanhshrink(x)\=x−Tanh(x) |
| [`softsign`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softsign.html#torch.nn.functional.softsign "torch.nn.functional.softsign") | Applies element-wise, the function SoftSign(x)\=x1+∣x∣\\text{SoftSign}(x) = \\frac{x}{1 + \|x\|}SoftSign(x)\=1+∣x∣x​ |
| [`softplus`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softplus.html#torch.nn.functional.softplus "torch.nn.functional.softplus") | Applies element-wise, the function Softplus(x)\=1β∗log⁡(1+exp⁡(β∗x))\\text{Softplus}(x) = \\frac{1}{\\beta} \* \\log(1 + \\exp(\\beta \* x))Softplus(x)\=β1​∗log(1+exp(β∗x)). |
| [`softmin`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softmin.html#torch.nn.functional.softmin "torch.nn.functional.softmin") | Apply a softmin function. |
| [`softmax`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softmax.html#torch.nn.functional.softmax "torch.nn.functional.softmax") | Apply a softmax function. |
| [`softshrink`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softshrink.html#torch.nn.functional.softshrink "torch.nn.functional.softshrink") | Applies the soft shrinkage function elementwise |
| [`gumbel_softmax`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.gumbel_softmax.html#torch.nn.functional.gumbel_softmax "torch.nn.functional.gumbel_softmax") | Sample from the Gumbel-Softmax distribution ([Link 1](https://docs.pytorch.org/docs/2.15/nn.functional.html#link-1)<br> [Link 2](https://docs.pytorch.org/docs/2.15/nn.functional.html#link-2)<br>) and optionally discretize. |
| [`log_softmax`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.log_softmax.html#torch.nn.functional.log_softmax "torch.nn.functional.log_softmax") | Apply a softmax followed by a logarithm. |
| [`tanh`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.tanh.html#torch.nn.functional.tanh "torch.nn.functional.tanh") | Applies element-wise, Tanh(x)\=tanh⁡(x)\=exp⁡(x)−exp⁡(−x)exp⁡(x)+exp⁡(−x)\\text{Tanh}(x) = \\tanh(x) = \\frac{\\exp(x) - \\exp(-x)}{\\exp(x) + \\exp(-x)}Tanh(x)\=tanh(x)\=exp(x)+exp(−x)exp(x)−exp(−x)​ |
| [`sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.sigmoid.html#torch.nn.functional.sigmoid "torch.nn.functional.sigmoid") | Applies the element-wise function Sigmoid(x)\=11+exp⁡(−x)\\text{Sigmoid}(x) = \\frac{1}{1 + \\exp(-x)}Sigmoid(x)\=1+exp(−x)1​ |
| [`hardsigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardsigmoid.html#torch.nn.functional.hardsigmoid "torch.nn.functional.hardsigmoid") | Apply the Hardsigmoid function element-wise. |
| [`silu`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.silu.html#torch.nn.functional.silu "torch.nn.functional.silu") | Apply the Sigmoid Linear Unit (SiLU) function, element-wise. |
| [`mish`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.mish.html#torch.nn.functional.mish "torch.nn.functional.mish") | Apply the Mish function, element-wise. |
| [`batch_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.batch_norm.html#torch.nn.functional.batch_norm "torch.nn.functional.batch_norm") | Apply Batch Normalization for each channel across a batch of data. |
| [`group_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.group_norm.html#torch.nn.functional.group_norm "torch.nn.functional.group_norm") | Apply Group Normalization for last certain number of dimensions. |
| [`instance_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.instance_norm.html#torch.nn.functional.instance_norm "torch.nn.functional.instance_norm") | Apply Instance Normalization independently for each channel in every data sample within a batch. |
| [`layer_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.layer_norm.html#torch.nn.functional.layer_norm "torch.nn.functional.layer_norm") | Apply Layer Normalization for last certain number of dimensions. |
| [`local_response_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.local_response_norm.html#torch.nn.functional.local_response_norm "torch.nn.functional.local_response_norm") | Apply local response normalization over an input signal. |
| [`rms_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.rms_norm.html#torch.nn.functional.rms_norm "torch.nn.functional.rms_norm") | Apply Root Mean Square Layer Normalization. |
| [`normalize`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.normalize.html#torch.nn.functional.normalize "torch.nn.functional.normalize") | Perform LpL\_pLp​ normalization of inputs over specified dimension. |

Linear functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#linear-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linear`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.linear.html#torch.nn.functional.linear "torch.nn.functional.linear") | Applies a linear transformation to the incoming data: y\=xAT+by = xA^T + by\=xAT+b. |
| [`bilinear`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.bilinear.html#torch.nn.functional.bilinear "torch.nn.functional.bilinear") | Applies a bilinear transformation to the incoming data: y\=x1TAx2+by = x\_1^T A x\_2 + by\=x1T​Ax2​+b |

Dropout functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#dropout-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.dropout.html#torch.nn.functional.dropout "torch.nn.functional.dropout") | During training, randomly zeroes some elements of the input tensor with probability `p`. |
| [`alpha_dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.alpha_dropout.html#torch.nn.functional.alpha_dropout "torch.nn.functional.alpha_dropout") | Apply alpha dropout to the input. |
| [`feature_alpha_dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.feature_alpha_dropout.html#torch.nn.functional.feature_alpha_dropout "torch.nn.functional.feature_alpha_dropout") | Randomly masks out entire channels (a channel is a feature map). |
| [`dropout1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.dropout1d.html#torch.nn.functional.dropout1d "torch.nn.functional.dropout1d") | Randomly zero out entire channels (a channel is a 1D feature map). |
| [`dropout2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.dropout2d.html#torch.nn.functional.dropout2d "torch.nn.functional.dropout2d") | Randomly zero out entire channels (a channel is a 2D feature map). |
| [`dropout3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.dropout3d.html#torch.nn.functional.dropout3d "torch.nn.functional.dropout3d") | Randomly zero out entire channels (a channel is a 3D feature map). |

Sparse functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#sparse-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`embedding`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.embedding.html#torch.nn.functional.embedding "torch.nn.functional.embedding") | Generate a simple lookup table that looks up embeddings in a fixed dictionary and size. |
| [`embedding_bag`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.embedding_bag.html#torch.nn.functional.embedding_bag "torch.nn.functional.embedding_bag") | Compute sums, means or maxes of bags of embeddings. |
| [`one_hot`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.one_hot.html#torch.nn.functional.one_hot "torch.nn.functional.one_hot") | Takes LongTensor with index values of shape `(*)` and returns a tensor of shape `(*, num_classes)` that have zeros everywhere except where the index of last dimension matches the corresponding value of the input tensor, in which case it will be 1. |

Distance functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#distance-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`pairwise_distance`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pairwise_distance.html#torch.nn.functional.pairwise_distance "torch.nn.functional.pairwise_distance") | See [`torch.nn.PairwiseDistance`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.PairwiseDistance.html#torch.nn.PairwiseDistance "torch.nn.PairwiseDistance")<br> for details |
| [`cosine_similarity`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.cosine_similarity.html#torch.nn.functional.cosine_similarity "torch.nn.functional.cosine_similarity") | Returns cosine similarity between `x1` and `x2`, computed along dim. |
| [`pdist`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pdist.html#torch.nn.functional.pdist "torch.nn.functional.pdist") | Computes the p-norm distance between every pair of row vectors in the input. |

Loss functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#loss-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`binary_cross_entropy`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.binary_cross_entropy.html#torch.nn.functional.binary_cross_entropy "torch.nn.functional.binary_cross_entropy") | Compute Binary Cross Entropy between the target and input probabilities. |
| [`binary_cross_entropy_with_logits`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.binary_cross_entropy_with_logits.html#torch.nn.functional.binary_cross_entropy_with_logits "torch.nn.functional.binary_cross_entropy_with_logits") | Compute Binary Cross Entropy between target and input logits. |
| [`poisson_nll_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.poisson_nll_loss.html#torch.nn.functional.poisson_nll_loss "torch.nn.functional.poisson_nll_loss") | Compute the Poisson negative log likelihood loss. |
| [`cosine_embedding_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.cosine_embedding_loss.html#torch.nn.functional.cosine_embedding_loss "torch.nn.functional.cosine_embedding_loss") | Compute the cosine embedding loss. |
| [`cross_entropy`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy "torch.nn.functional.cross_entropy") | Compute the cross entropy loss between input logits and target. |
| [`ctc_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.ctc_loss.html#torch.nn.functional.ctc_loss "torch.nn.functional.ctc_loss") | Compute the Connectionist Temporal Classification loss. |
| [`gaussian_nll_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.gaussian_nll_loss.html#torch.nn.functional.gaussian_nll_loss "torch.nn.functional.gaussian_nll_loss") | Compute the Gaussian negative log likelihood loss. |
| [`hinge_embedding_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hinge_embedding_loss.html#torch.nn.functional.hinge_embedding_loss "torch.nn.functional.hinge_embedding_loss") | Compute the hinge embedding loss. |
| [`kl_div`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.kl_div.html#torch.nn.functional.kl_div "torch.nn.functional.kl_div") | Compute the KL Divergence loss. |
| [`l1_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.l1_loss.html#torch.nn.functional.l1_loss "torch.nn.functional.l1_loss") | Compute the L1 loss, with optional weighting. |
| [`linear_cross_entropy`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.linear_cross_entropy.html#torch.nn.functional.linear_cross_entropy "torch.nn.functional.linear_cross_entropy") | Compute the cross entropy loss between inputs, transformed linearly, and target. |
| [`mse_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.mse_loss.html#torch.nn.functional.mse_loss "torch.nn.functional.mse_loss") | Compute the element-wise mean squared error, with optional weighting. |
| [`margin_ranking_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.margin_ranking_loss.html#torch.nn.functional.margin_ranking_loss "torch.nn.functional.margin_ranking_loss") | Compute the margin ranking loss. |
| [`multilabel_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.multilabel_margin_loss.html#torch.nn.functional.multilabel_margin_loss "torch.nn.functional.multilabel_margin_loss") | Compute the multilabel margin loss. |
| [`multilabel_soft_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.multilabel_soft_margin_loss.html#torch.nn.functional.multilabel_soft_margin_loss "torch.nn.functional.multilabel_soft_margin_loss") | Compute the multilabel soft margin loss. |
| [`multi_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.multi_margin_loss.html#torch.nn.functional.multi_margin_loss "torch.nn.functional.multi_margin_loss") | Compute the multi margin loss, with optional weighting. |
| [`nll_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.nll_loss.html#torch.nn.functional.nll_loss "torch.nn.functional.nll_loss") | Compute the negative log likelihood loss. |
| [`huber_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.huber_loss.html#torch.nn.functional.huber_loss "torch.nn.functional.huber_loss") | Compute the Huber loss, with optional weighting. |
| [`smooth_l1_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.smooth_l1_loss.html#torch.nn.functional.smooth_l1_loss "torch.nn.functional.smooth_l1_loss") | Compute the Smooth L1 loss. |
| [`soft_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.soft_margin_loss.html#torch.nn.functional.soft_margin_loss "torch.nn.functional.soft_margin_loss") | Compute the soft margin loss. |
| [`triplet_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.triplet_margin_loss.html#torch.nn.functional.triplet_margin_loss "torch.nn.functional.triplet_margin_loss") | Compute the triplet loss between given input tensors and a margin greater than 0. |
| [`triplet_margin_with_distance_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.triplet_margin_with_distance_loss.html#torch.nn.functional.triplet_margin_with_distance_loss "torch.nn.functional.triplet_margin_with_distance_loss") | Compute the triplet margin loss for input tensors using a custom distance function. |

Vision functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#vision-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`pixel_shuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pixel_shuffle.html#torch.nn.functional.pixel_shuffle "torch.nn.functional.pixel_shuffle") | Rearranges elements in a tensor of shape (∗,C×r2,H,W)(\*, C \\times r^2, H, W)(∗,C×r2,H,W) to a tensor of shape (∗,C,H×r,W×r)(\*, C, H \\times r, W \\times r)(∗,C,H×r,W×r), where r is the `upscale_factor`. |
| [`pixel_unshuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pixel_unshuffle.html#torch.nn.functional.pixel_unshuffle "torch.nn.functional.pixel_unshuffle") | Reverses the [`PixelShuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.PixelShuffle.html#torch.nn.PixelShuffle "torch.nn.PixelShuffle")<br> operation by rearranging elements in a tensor of shape (∗,C,H×r,W×r)(\*, C, H \\times r, W \\times r)(∗,C,H×r,W×r) to a tensor of shape (∗,C×r2,H,W)(\*, C \\times r^2, H, W)(∗,C×r2,H,W), where r is the `downscale_factor`. |
| [`pad`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#torch.nn.functional.pad "torch.nn.functional.pad") | Pads tensor. |
| [`interpolate`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#torch.nn.functional.interpolate "torch.nn.functional.interpolate") | Down/up samples the input. |
| [`upsample`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.upsample.html#torch.nn.functional.upsample "torch.nn.functional.upsample") | Upsample input. |
| [`upsample_nearest`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.upsample_nearest.html#torch.nn.functional.upsample_nearest "torch.nn.functional.upsample_nearest") | Upsamples the input, using nearest neighbours' pixel values. |
| [`upsample_bilinear`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.upsample_bilinear.html#torch.nn.functional.upsample_bilinear "torch.nn.functional.upsample_bilinear") | Upsamples the input, using bilinear upsampling. |
| [`grid_sample`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#torch.nn.functional.grid_sample "torch.nn.functional.grid_sample") | Compute grid sample. |
| [`affine_grid`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.affine_grid.html#torch.nn.functional.affine_grid "torch.nn.functional.affine_grid") | Generate 2D or 3D flow field (sampling grid), given a batch of affine matrices `theta`. |

DataParallel functions (multi-GPU, distributed)[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#dataparallel-functions-multi-gpu-distributed "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### data\_parallel[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#data-parallel "Link to this heading")

|     |     |
| --- | --- |
| `torch.nn.parallel.data_parallel` | Evaluate module(input) in parallel across the GPUs given in device\_ids. |

Low-Precision functions[#](https://docs.pytorch.org/docs/2.15/nn.functional.html#low-precision-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ScalingType`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.ScalingType.html#torch.nn.functional.ScalingType "torch.nn.functional.ScalingType") | alias of `_ScalingType` |
| [`SwizzleType`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.SwizzleType.html#torch.nn.functional.SwizzleType "torch.nn.functional.SwizzleType") | alias of `_SwizzleType` |
| [`grouped_mm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grouped_mm.html#torch.nn.functional.grouped_mm "torch.nn.functional.grouped_mm") | Computes a grouped matrix multiply that shares weight shapes across experts but allows jagged token counts per expert, which is common in Mixture-of-Experts (MoE) layers. |
| [`scaled_mm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm "torch.nn.functional.scaled_mm") | scaled\_mm(mat\_a, mat\_b, scale\_a, scale\_recipe\_a, scale\_b, scale\_recipe\_b, swizzle\_a, swizzle\_b, bias, output\_dtype, |
| [`scaled_addmm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_addmm.html#torch.nn.functional.scaled_addmm "torch.nn.functional.scaled_addmm") | Compute a scaled matrix product and add it to `input`. |
| [`scaled_addmm_`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_addmm_.html#torch.nn.functional.scaled_addmm_ "torch.nn.functional.scaled_addmm_") | In-place version of [`scaled_addmm()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_addmm.html#torch.nn.functional.scaled_addmm "torch.nn.functional.scaled_addmm")<br>. |
| [`scaled_grouped_mm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_grouped_mm.html#torch.nn.functional.scaled_grouped_mm "torch.nn.functional.scaled_grouped_mm") | scaled\_grouped\_mm(mat\_a, mat\_b, scale\_a, scale\_recipe\_a, scale\_b, scale\_recipe\_b, swizzle\_a, swizzle\_b, bias, offs, |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nn.functional.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nn.functional.md.txt)

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