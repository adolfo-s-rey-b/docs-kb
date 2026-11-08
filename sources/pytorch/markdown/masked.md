Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/masked.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/masked.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/masked.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/masked.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/masked.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/masked.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/masked.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/masked.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/masked.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/masked.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/masked.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/masked.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/masked.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/masked.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/masked.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/masked.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/masked.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/masked.html)
[v1.13](https://docs.pytorch.org/docs/1.13/masked.html)
[v1.12](https://docs.pytorch.org/docs/1.12/masked.html)
[v1.11](https://docs.pytorch.org/docs/1.11/masked.html)
[v1.10](https://docs.pytorch.org/docs/1.10/masked.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/masked.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/masked.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/masked.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/masked.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/masked.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/masked.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/masked.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/masked.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/masked.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/masked.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/masked.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/masked.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/masked.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/masked.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/masked.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/masked.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/masked.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/masked.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/masked.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/masked.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/masked.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/masked.html)

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

torch.masked[#](https://docs.pytorch.org/docs/2.15/masked.html#torch-masked "Link to this heading")

====================================================================================================

Created On: Aug 15, 2022 | Last Updated On: Apr 13, 2026

Introduction[#](https://docs.pytorch.org/docs/2.15/masked.html#introduction "Link to this heading")

----------------------------------------------------------------------------------------------------

### Motivation[#](https://docs.pytorch.org/docs/2.15/masked.html#motivation "Link to this heading")

Warning

The PyTorch API of masked tensors is in the prototype stage and may or may not change in the future.

MaskedTensor serves as an extension to [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 that provides the user with the ability to:

*   use any masked semantics (e.g. variable length tensors, nan\* operators, etc.)
    
*   differentiate between 0 and NaN gradients
    
*   various sparse applications (see tutorial below)
    

“Specified” and “unspecified” have a long history in PyTorch without formal semantics and certainly without consistency; indeed, MaskedTensor was born out of a build up of issues that the vanilla [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 class could not properly address. Thus, a primary goal of MaskedTensor is to become the source of truth for said “specified” and “unspecified” values in PyTorch where they are a first class citizen instead of an afterthought. In turn, this should further unlock [sparsity’s](https://pytorch.org/docs/stable/sparse.html)
 potential, enable safer and more consistent operators, and provide a smoother and more intuitive experience for users and developers alike.

### What is a MaskedTensor?[#](https://docs.pytorch.org/docs/2.15/masked.html#what-is-a-maskedtensor "Link to this heading")

A MaskedTensor is a tensor subclass that consists of 1) an input (data), and 2) a mask. The mask tells us which entries from the input should be included or ignored.

By way of example, suppose that we wanted to mask out all values that are equal to 0 (represented by the gray) and take the max:

[![_images/tensor_comparison.jpg](https://docs.pytorch.org/docs/2.15/_images/tensor_comparison.jpg)](https://docs.pytorch.org/docs/2.15/_images/tensor_comparison.jpg)

On top is the vanilla tensor example while the bottom is MaskedTensor where all the 0’s are masked out. This clearly yields a different result depending on whether we have the mask, but this flexible structure allows the user to systematically ignore any elements they’d like during computation.

There are already a number of existing tutorials that we’ve written to help users onboard, such as:

*   [Overview – the place to start for new users, discusses how to use MaskedTensors and why they’re useful](https://docs.pytorch.org/tutorials/unstable/maskedtensor_overview)
    
*   [Sparsity – MaskedTensor supports sparse COO and CSR data and mask Tensors](https://docs.pytorch.org/tutorials/unstable/maskedtensor_sparsity)
    
*   [Adagrad sparse semantics – a practical example of how MaskedTensor can simplify sparse semantics and implementations](https://docs.pytorch.org/tutorials/unstable/maskedtensor_adagrad)
    
*   [Advanced semantics – discussion on why certain decisions were made (e.g. requiring masks to match for binary/reduction operations), differences with NumPy’s MaskedArray, and reduction semantics](https://docs.pytorch.org/tutorials/unstable/maskedtensor_advanced_semantics)
    

Supported Operators[#](https://docs.pytorch.org/docs/2.15/masked.html#supported-operators "Link to this heading")

------------------------------------------------------------------------------------------------------------------

### Unary Operators[#](https://docs.pytorch.org/docs/2.15/masked.html#unary-operators "Link to this heading")

Unary operators are operators that only contain only a single input. Applying them to MaskedTensors is relatively straightforward: if the data is masked out at a given index, we apply the operator, otherwise we’ll continue to mask out the data.

The available unary operators are:

|     |     |
| --- | --- |
| [`abs`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs") | Computes the absolute value of each element in `input`. |
| [`absolute`](https://docs.pytorch.org/docs/2.15/generated/torch.absolute.html#torch.absolute "torch.absolute") | Alias for [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs") |
| [`acos`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos") | Returns a new tensor with the arccosine (in radians) of each element in `input`. |
| [`arccos`](https://docs.pytorch.org/docs/2.15/generated/torch.arccos.html#torch.arccos "torch.arccos") | Alias for [`torch.acos()`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos")<br>. |
| [`acosh`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh.html#torch.acosh "torch.acosh") | Returns a new tensor with the inverse hyperbolic cosine of the elements of `input`. |
| [`arccosh`](https://docs.pytorch.org/docs/2.15/generated/torch.arccosh.html#torch.arccosh "torch.arccosh") | Alias for [`torch.acosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh.html#torch.acosh "torch.acosh")<br>. |
| [`angle`](https://docs.pytorch.org/docs/2.15/generated/torch.angle.html#torch.angle "torch.angle") | Computes the element-wise angle (in radians) of the given `input` tensor. |
| [`asin`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin") | Returns a new tensor with the arcsine of the elements (in radians) in the `input` tensor. |
| [`arcsin`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsin.html#torch.arcsin "torch.arcsin") | Alias for [`torch.asin()`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin")<br>. |
| [`asinh`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh.html#torch.asinh "torch.asinh") | Returns a new tensor with the inverse hyperbolic sine of the elements of `input`. |
| [`arcsinh`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsinh.html#torch.arcsinh "torch.arcsinh") | Alias for [`torch.asinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh.html#torch.asinh "torch.asinh")<br>. |
| [`atan`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan") | Returns a new tensor with the arctangent of the elements (in radians) in the `input` tensor. |
| [`arctan`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan.html#torch.arctan "torch.arctan") | Alias for [`torch.atan()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan")<br>. |
| [`atanh`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh.html#torch.atanh "torch.atanh") | Returns a new tensor with the inverse hyperbolic tangent of the elements of `input`. |
| [`arctanh`](https://docs.pytorch.org/docs/2.15/generated/torch.arctanh.html#torch.arctanh "torch.arctanh") | Alias for [`torch.atanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh.html#torch.atanh "torch.atanh")<br>. |
| [`bitwise_not`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_not.html#torch.bitwise_not "torch.bitwise_not") | Computes the bitwise NOT of the given input tensor. |
| [`ceil`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil.html#torch.ceil "torch.ceil") | Returns a new tensor with the ceil of the elements of `input`, the smallest integer greater than or equal to each element. |
| [`clamp`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp") | Clamps all elements in `input` into the range \[ [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min")<br>, [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")<br> \]. |
| [`clip`](https://docs.pytorch.org/docs/2.15/generated/torch.clip.html#torch.clip "torch.clip") | Alias for [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br>. |
| [`conj_physical`](https://docs.pytorch.org/docs/2.15/generated/torch.conj_physical.html#torch.conj_physical "torch.conj_physical") | Computes the element-wise conjugate of the given `input` tensor. |
| [`cos`](https://docs.pytorch.org/docs/2.15/generated/torch.cos.html#torch.cos "torch.cos") | Returns a new tensor with the cosine of the elements of `input` given in radians. |
| [`cosh`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh.html#torch.cosh "torch.cosh") | Returns a new tensor with the hyperbolic cosine of the elements of `input`. |
| [`deg2rad`](https://docs.pytorch.org/docs/2.15/generated/torch.deg2rad.html#torch.deg2rad "torch.deg2rad") | Returns a new tensor with each of the elements of `input` converted from angles in degrees to radians. |
| [`digamma`](https://docs.pytorch.org/docs/2.15/generated/torch.digamma.html#torch.digamma "torch.digamma") | Alias for [`torch.special.digamma()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.digamma "torch.special.digamma")<br>. |
| [`erf`](https://docs.pytorch.org/docs/2.15/generated/torch.erf.html#torch.erf "torch.erf") | Alias for [`torch.special.erf()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erf "torch.special.erf")<br>. |
| [`erfc`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc.html#torch.erfc "torch.erfc") | Alias for [`torch.special.erfc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfc "torch.special.erfc")<br>. |
| [`erfinv`](https://docs.pytorch.org/docs/2.15/generated/torch.erfinv.html#torch.erfinv "torch.erfinv") | Alias for [`torch.special.erfinv()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfinv "torch.special.erfinv")<br>. |
| [`exp`](https://docs.pytorch.org/docs/2.15/generated/torch.exp.html#torch.exp "torch.exp") | Returns a new tensor with the exponential of the elements of the input tensor `input`. |
| [`exp2`](https://docs.pytorch.org/docs/2.15/generated/torch.exp2.html#torch.exp2 "torch.exp2") | Alias for [`torch.special.exp2()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.exp2 "torch.special.exp2")<br>. |
| [`expm1`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1.html#torch.expm1 "torch.expm1") | Alias for [`torch.special.expm1()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expm1 "torch.special.expm1")<br>. |
| [`fix`](https://docs.pytorch.org/docs/2.15/generated/torch.fix.html#torch.fix "torch.fix") | Alias for [`torch.trunc()`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc") |
| [`floor`](https://docs.pytorch.org/docs/2.15/generated/torch.floor.html#torch.floor "torch.floor") | Returns a new tensor with the floor of the elements of `input`, the largest integer less than or equal to each element. |
| [`frac`](https://docs.pytorch.org/docs/2.15/generated/torch.frac.html#torch.frac "torch.frac") | Computes the fractional portion of each element in `input`. |
| [`lgamma`](https://docs.pytorch.org/docs/2.15/generated/torch.lgamma.html#torch.lgamma "torch.lgamma") | Computes the natural logarithm of the absolute value of the gamma function on `input`. |
| [`log`](https://docs.pytorch.org/docs/2.15/generated/torch.log.html#torch.log "torch.log") | Returns a new tensor with the natural logarithm of the elements of `input`. |
| [`log10`](https://docs.pytorch.org/docs/2.15/generated/torch.log10.html#torch.log10 "torch.log10") | Returns a new tensor with the logarithm to the base 10 of the elements of `input`. |
| [`log1p`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p") | Returns a new tensor with the natural logarithm of (1 + `input`). |
| [`log2`](https://docs.pytorch.org/docs/2.15/generated/torch.log2.html#torch.log2 "torch.log2") | Returns a new tensor with the logarithm to the base 2 of the elements of `input`. |
| [`logit`](https://docs.pytorch.org/docs/2.15/generated/torch.logit.html#torch.logit "torch.logit") | Alias for [`torch.special.logit()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.logit "torch.special.logit")<br>. |
| [`i0`](https://docs.pytorch.org/docs/2.15/generated/torch.i0.html#torch.i0 "torch.i0") | Alias for [`torch.special.i0()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i0 "torch.special.i0")<br>. |
| [`isnan`](https://docs.pytorch.org/docs/2.15/generated/torch.isnan.html#torch.isnan "torch.isnan") | Returns a new tensor with boolean elements representing if each element of `input` is NaN or not. |
| [`nan_to_num`](https://docs.pytorch.org/docs/2.15/generated/torch.nan_to_num.html#torch.nan_to_num "torch.nan_to_num") | Replaces `NaN`, positive infinity, and negative infinity values in `input` with the values specified by `nan`, `posinf`, and `neginf`, respectively. |
| [`neg`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg") | Returns a new tensor with the negative of the elements of `input`. |
| [`negative`](https://docs.pytorch.org/docs/2.15/generated/torch.negative.html#torch.negative "torch.negative") | Alias for [`torch.neg()`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg") |
| [`positive`](https://docs.pytorch.org/docs/2.15/generated/torch.positive.html#torch.positive "torch.positive") | Returns `input`. |
| [`pow`](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#torch.pow "torch.pow") | Takes the power of each element in `input` with `exponent` and returns a tensor with the result. |
| [`rad2deg`](https://docs.pytorch.org/docs/2.15/generated/torch.rad2deg.html#torch.rad2deg "torch.rad2deg") | Returns a new tensor with each of the elements of `input` converted from angles in radians to degrees. |
| [`reciprocal`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal.html#torch.reciprocal "torch.reciprocal") | Returns a new tensor with the reciprocal of the elements of `input` |
| [`round`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round") | Rounds elements of `input` to the nearest integer. |
| [`rsqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt.html#torch.rsqrt "torch.rsqrt") | Returns a new tensor with the reciprocal of the square-root of each of the elements of `input`. |
| [`sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid.html#torch.sigmoid "torch.sigmoid") | Alias for [`torch.special.expit()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expit "torch.special.expit")<br>. |
| [`sign`](https://docs.pytorch.org/docs/2.15/generated/torch.sign.html#torch.sign "torch.sign") | Returns a new tensor with the signs of the elements of `input`. |
| [`sgn`](https://docs.pytorch.org/docs/2.15/generated/torch.sgn.html#torch.sgn "torch.sgn") | This function is an extension of torch.sign() to complex tensors. |
| [`signbit`](https://docs.pytorch.org/docs/2.15/generated/torch.signbit.html#torch.signbit "torch.signbit") | Tests if each element of `input` has its sign bit set or not. |
| [`sin`](https://docs.pytorch.org/docs/2.15/generated/torch.sin.html#torch.sin "torch.sin") | Returns a new tensor with the sine of the elements in the `input` tensor, where each value in this input tensor is in radians. |
| [`sinc`](https://docs.pytorch.org/docs/2.15/generated/torch.sinc.html#torch.sinc "torch.sinc") | Alias for [`torch.special.sinc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.sinc "torch.special.sinc")<br>. |
| [`sinh`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh.html#torch.sinh "torch.sinh") | Returns a new tensor with the hyperbolic sine of the elements of `input`. |
| [`sqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt.html#torch.sqrt "torch.sqrt") | Returns a new tensor with the square-root of the elements of `input`. |
| [`square`](https://docs.pytorch.org/docs/2.15/generated/torch.square.html#torch.square "torch.square") | Returns a new tensor with the square of the elements of `input`. |
| [`tan`](https://docs.pytorch.org/docs/2.15/generated/torch.tan.html#torch.tan "torch.tan") | Returns a new tensor with the tangent of the elements in the `input` tensor, where each value in this input tensor is in radians. |
| [`tanh`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh.html#torch.tanh "torch.tanh") | Returns a new tensor with the hyperbolic tangent of the elements of `input`. |
| [`trunc`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc") | Returns a new tensor with the truncated integer values of the elements of `input`. |

The available inplace unary operators are all of the above **except**:

|     |     |
| --- | --- |
| [`angle`](https://docs.pytorch.org/docs/2.15/generated/torch.angle.html#torch.angle "torch.angle") | Computes the element-wise angle (in radians) of the given `input` tensor. |
| [`positive`](https://docs.pytorch.org/docs/2.15/generated/torch.positive.html#torch.positive "torch.positive") | Returns `input`. |
| [`signbit`](https://docs.pytorch.org/docs/2.15/generated/torch.signbit.html#torch.signbit "torch.signbit") | Tests if each element of `input` has its sign bit set or not. |
| [`isnan`](https://docs.pytorch.org/docs/2.15/generated/torch.isnan.html#torch.isnan "torch.isnan") | Returns a new tensor with boolean elements representing if each element of `input` is NaN or not. |

### Binary Operators[#](https://docs.pytorch.org/docs/2.15/masked.html#binary-operators "Link to this heading")

As you may have seen in the tutorial, `MaskedTensor` also has binary operations implemented with the caveat that the masks in the two MaskedTensors must match or else an error will be raised. As noted in the error, if you need support for a particular operator or have proposed semantics for how they should behave instead, please open an issue on GitHub. For now, we have decided to go with the most conservative implementation to ensure that users know exactly what is going on and are being intentional about their decisions with masked semantics.

The available binary operators are:

|     |     |
| --- | --- |
| [`add`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add") | Adds `other`, scaled by `alpha`, to `input`. |
| [`atan2`](https://docs.pytorch.org/docs/2.15/generated/torch.atan2.html#torch.atan2 "torch.atan2") | Element-wise arctangent of inputi/otheri\\text{input}\_{i} / \\text{other}\_{i}inputi​/otheri​ with consideration of the quadrant. |
| [`arctan2`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan2.html#torch.arctan2 "torch.arctan2") | Alias for [`torch.atan2()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan2.html#torch.atan2 "torch.atan2")<br>. |
| [`bitwise_and`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_and.html#torch.bitwise_and "torch.bitwise_and") | Computes the bitwise AND of `input` and `other`. |
| [`bitwise_or`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_or.html#torch.bitwise_or "torch.bitwise_or") | Computes the bitwise OR of `input` and `other`. |
| [`bitwise_xor`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_xor.html#torch.bitwise_xor "torch.bitwise_xor") | Computes the bitwise XOR of `input` and `other`. |
| [`bitwise_left_shift`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_left_shift.html#torch.bitwise_left_shift "torch.bitwise_left_shift") | Computes the left arithmetic shift of `input` by `other` bits. |
| [`bitwise_right_shift`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_right_shift.html#torch.bitwise_right_shift "torch.bitwise_right_shift") | Computes the right arithmetic shift of `input` by `other` bits. |
| [`div`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div") | Divides each element of the input `input` by the corresponding element of `other`. |
| [`divide`](https://docs.pytorch.org/docs/2.15/generated/torch.divide.html#torch.divide "torch.divide") | Alias for [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br>. |
| [`floor_divide`](https://docs.pytorch.org/docs/2.15/generated/torch.floor_divide.html#torch.floor_divide "torch.floor_divide") |     |
| [`fmod`](https://docs.pytorch.org/docs/2.15/generated/torch.fmod.html#torch.fmod "torch.fmod") | Applies C++'s [std::fmod](https://en.cppreference.com/w/cpp/numeric/math/fmod)<br> entrywise. |
| [`logaddexp`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp.html#torch.logaddexp "torch.logaddexp") | Logarithm of the sum of exponentiations of the inputs. |
| [`logaddexp2`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp2.html#torch.logaddexp2 "torch.logaddexp2") | Logarithm of the sum of exponentiations of the inputs in base-2. |
| [`mul`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul") | Multiplies `input` by `other`. |
| [`multiply`](https://docs.pytorch.org/docs/2.15/generated/torch.multiply.html#torch.multiply "torch.multiply") | Alias for [`torch.mul()`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul")<br>. |
| [`nextafter`](https://docs.pytorch.org/docs/2.15/generated/torch.nextafter.html#torch.nextafter "torch.nextafter") | Return the next floating-point value after `input` towards `other`, elementwise. |
| [`remainder`](https://docs.pytorch.org/docs/2.15/generated/torch.remainder.html#torch.remainder "torch.remainder") | Computes [Python's modulus operation](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)<br> entrywise. |
| [`sub`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub") | Subtracts `other`, scaled by `alpha`, from `input`. |
| [`subtract`](https://docs.pytorch.org/docs/2.15/generated/torch.subtract.html#torch.subtract "torch.subtract") | Alias for [`torch.sub()`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub")<br>. |
| [`true_divide`](https://docs.pytorch.org/docs/2.15/generated/torch.true_divide.html#torch.true_divide "torch.true_divide") | Alias for [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br> with `rounding_mode=None`. |
| [`eq`](https://docs.pytorch.org/docs/2.15/generated/torch.eq.html#torch.eq "torch.eq") | Computes element-wise equality |
| [`ne`](https://docs.pytorch.org/docs/2.15/generated/torch.ne.html#torch.ne "torch.ne") | Computes input≠other\\text{input} \\neq \\text{other}input\=other element-wise. |
| [`le`](https://docs.pytorch.org/docs/2.15/generated/torch.le.html#torch.le "torch.le") | Computes input≤other\\text{input} \\leq \\text{other}input≤other element-wise. |
| [`ge`](https://docs.pytorch.org/docs/2.15/generated/torch.ge.html#torch.ge "torch.ge") | Computes input≥other\\text{input} \\geq \\text{other}input≥other element-wise. |
| [`greater`](https://docs.pytorch.org/docs/2.15/generated/torch.greater.html#torch.greater "torch.greater") | Alias for [`torch.gt()`](https://docs.pytorch.org/docs/2.15/generated/torch.gt.html#torch.gt "torch.gt")<br>. |
| [`greater_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.greater_equal.html#torch.greater_equal "torch.greater_equal") | Alias for [`torch.ge()`](https://docs.pytorch.org/docs/2.15/generated/torch.ge.html#torch.ge "torch.ge")<br>. |
| [`gt`](https://docs.pytorch.org/docs/2.15/generated/torch.gt.html#torch.gt "torch.gt") | Computes input\>other\\text{input} > \\text{other}input\>other element-wise. |
| [`less_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.less_equal.html#torch.less_equal "torch.less_equal") | Alias for [`torch.le()`](https://docs.pytorch.org/docs/2.15/generated/torch.le.html#torch.le "torch.le")<br>. |
| [`lt`](https://docs.pytorch.org/docs/2.15/generated/torch.lt.html#torch.lt "torch.lt") | Computes input<other\\text{input} < \\text{other}input<other element-wise. |
| [`less`](https://docs.pytorch.org/docs/2.15/generated/torch.less.html#torch.less "torch.less") | Alias for [`torch.lt()`](https://docs.pytorch.org/docs/2.15/generated/torch.lt.html#torch.lt "torch.lt")<br>. |
| [`maximum`](https://docs.pytorch.org/docs/2.15/generated/torch.maximum.html#torch.maximum "torch.maximum") | Computes the element-wise maximum of `input` and `other`. |
| [`minimum`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum") | Computes the element-wise minimum of `input` and `other`. |
| [`fmax`](https://docs.pytorch.org/docs/2.15/generated/torch.fmax.html#torch.fmax "torch.fmax") | Computes the element-wise maximum of `input` and `other`. |
| [`fmin`](https://docs.pytorch.org/docs/2.15/generated/torch.fmin.html#torch.fmin "torch.fmin") | Computes the element-wise minimum of `input` and `other`. |
| [`not_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.not_equal.html#torch.not_equal "torch.not_equal") | Alias for [`torch.ne()`](https://docs.pytorch.org/docs/2.15/generated/torch.ne.html#torch.ne "torch.ne")<br>. |

The available inplace binary operators are all of the above **except**:

|     |     |
| --- | --- |
| [`logaddexp`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp.html#torch.logaddexp "torch.logaddexp") | Logarithm of the sum of exponentiations of the inputs. |
| [`logaddexp2`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp2.html#torch.logaddexp2 "torch.logaddexp2") | Logarithm of the sum of exponentiations of the inputs in base-2. |
| [`equal`](https://docs.pytorch.org/docs/2.15/generated/torch.equal.html#torch.equal "torch.equal") | `True` if two tensors have the same size and elements, `False` otherwise. |
| [`fmin`](https://docs.pytorch.org/docs/2.15/generated/torch.fmin.html#torch.fmin "torch.fmin") | Computes the element-wise minimum of `input` and `other`. |
| [`minimum`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum") | Computes the element-wise minimum of `input` and `other`. |
| [`fmax`](https://docs.pytorch.org/docs/2.15/generated/torch.fmax.html#torch.fmax "torch.fmax") | Computes the element-wise maximum of `input` and `other`. |

### Reductions[#](https://docs.pytorch.org/docs/2.15/masked.html#reductions "Link to this heading")

The following reductions are available (with autograd support). For more information, the [Overview](https://pytorch.org/tutorials/unstable/maskedtensor_overview.html)
 tutorial details some examples of reductions, while the [Advanced semantics](https://pytorch.org/tutorials/unstable/maskedtensor_advanced_semantics.html)
 tutorial has some further in-depth discussions about how we decided on certain reduction semantics.

|     |     |
| --- | --- |
| [`sum`](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html#torch.sum "torch.sum") | Returns the sum of all elements in the `input` tensor. |
| [`mean`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean") |     |
| [`amin`](https://docs.pytorch.org/docs/2.15/generated/torch.amin.html#torch.amin "torch.amin") | Returns the minimum value of each slice of the `input` tensor in the given dimension(s) `dim`. |
| [`amax`](https://docs.pytorch.org/docs/2.15/generated/torch.amax.html#torch.amax "torch.amax") | Returns the maximum value of each slice of the `input` tensor in the given dimension(s) `dim`. |
| [`argmin`](https://docs.pytorch.org/docs/2.15/generated/torch.argmin.html#torch.argmin "torch.argmin") | Returns the indices of the minimum value(s) of the flattened tensor or along a dimension |
| [`argmax`](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#torch.argmax "torch.argmax") | Returns the indices of the maximum value of all elements in the `input` tensor. |
| [`prod`](https://docs.pytorch.org/docs/2.15/generated/torch.prod.html#torch.prod "torch.prod") | Returns the product of all elements in the `input` tensor. |
| [`all`](https://docs.pytorch.org/docs/2.15/generated/torch.all.html#torch.all "torch.all") | Tests if all elements in `input` evaluate to True. |
| [`norm`](https://docs.pytorch.org/docs/2.15/generated/torch.norm.html#torch.norm "torch.norm") | Returns the matrix norm or vector norm of a given tensor. |
| [`var`](https://docs.pytorch.org/docs/2.15/generated/torch.var.html#torch.var "torch.var") | Calculates the variance over the dimensions specified by `dim`. |
| [`std`](https://docs.pytorch.org/docs/2.15/generated/torch.std.html#torch.std "torch.std") | Calculates the standard deviation over the dimensions specified by `dim`. |

### View and select functions[#](https://docs.pytorch.org/docs/2.15/masked.html#view-and-select-functions "Link to this heading")

We’ve included a number of view and select functions as well; intuitively, these operators will apply to both the data and the mask and then wrap the result in a `MaskedTensor`. For a quick example, consider [`select()`](https://docs.pytorch.org/docs/2.15/generated/torch.select.html#torch.select "torch.select")
:

    \>>> data \= torch.arange(12, dtype\=torch.float).reshape(3, 4)
    \>>> data
    tensor(\[\[ 0.,  1.,  2.,  3.\],\
            \[ 4.,  5.,  6.,  7.\],\
            \[ 8.,  9., 10., 11.\]\])
    \>>> mask \= torch.tensor(\[\[True, False, False, True\], \[False, True, False, False\], \[True, True, True, True\]\])
    \>>> mt \= masked\_tensor(data, mask)
    \>>> data.select(0, 1)
    tensor(\[4., 5., 6., 7.\])
    \>>> mask.select(0, 1)
    tensor(\[False,  True, False, False\])
    \>>> mt.select(0, 1)
    MaskedTensor(
      \[      \--,   5.0000,       \--,       \--\]
    )

Copy to clipboard

The following ops are currently supported:

|     |     |
| --- | --- |
| [`atleast_1d`](https://docs.pytorch.org/docs/2.15/generated/torch.atleast_1d.html#torch.atleast_1d "torch.atleast_1d") | Returns a 1-dimensional view of each input tensor with zero dimensions. |
| [`broadcast_tensors`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_tensors.html#torch.broadcast_tensors "torch.broadcast_tensors") | Broadcasts the given tensors according to [Broadcasting semantics](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)<br>. |
| [`broadcast_to`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_to.html#torch.broadcast_to "torch.broadcast_to") | Broadcasts `input` to the shape `shape`. |
| [`cat`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat") | Concatenates the given sequence of tensors in `tensors` in the given dimension. |
| [`chunk`](https://docs.pytorch.org/docs/2.15/generated/torch.chunk.html#torch.chunk "torch.chunk") | Attempts to split a tensor into the specified number of chunks. |
| [`column_stack`](https://docs.pytorch.org/docs/2.15/generated/torch.column_stack.html#torch.column_stack "torch.column_stack") | Creates a new tensor by horizontally stacking the tensors in `tensors`. |
| [`dsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.dsplit.html#torch.dsplit "torch.dsplit") | Splits `input`, a tensor with three or more dimensions, into multiple tensors depthwise according to `indices_or_sections`. |
| [`flatten`](https://docs.pytorch.org/docs/2.15/generated/torch.flatten.html#torch.flatten "torch.flatten") | Flattens `input` by reshaping it into a one-dimensional tensor. |
| [`hsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.hsplit.html#torch.hsplit "torch.hsplit") | Splits `input`, a tensor with one or more dimensions, into multiple tensors horizontally according to `indices_or_sections`. |
| [`hstack`](https://docs.pytorch.org/docs/2.15/generated/torch.hstack.html#torch.hstack "torch.hstack") | Stack tensors in sequence horizontally (column wise). |
| [`kron`](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html#torch.kron "torch.kron") | Computes the Kronecker product, denoted by ⊗\\otimes⊗, of `input` and `other`. |
| [`meshgrid`](https://docs.pytorch.org/docs/2.15/generated/torch.meshgrid.html#torch.meshgrid "torch.meshgrid") | Creates grids of coordinates specified by the 1D inputs in attr:tensors. |
| [`narrow`](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html#torch.narrow "torch.narrow") | Returns a new tensor that is a narrowed version of `input` tensor. |
| [`nn.functional.unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.unfold.html#torch.nn.functional.unfold "torch.nn.functional.unfold") | Extract sliding local blocks from a batched input tensor. |
| [`ravel`](https://docs.pytorch.org/docs/2.15/generated/torch.ravel.html#torch.ravel "torch.ravel") | Return a contiguous flattened tensor. |
| [`select`](https://docs.pytorch.org/docs/2.15/generated/torch.select.html#torch.select "torch.select") | Slices the `input` tensor along the selected dimension at the given index. |
| [`split`](https://docs.pytorch.org/docs/2.15/generated/torch.split.html#torch.split "torch.split") | Splits the tensor into chunks. |
| [`stack`](https://docs.pytorch.org/docs/2.15/generated/torch.stack.html#torch.stack "torch.stack") | Concatenates a sequence of tensors along a new dimension. |
| [`t`](https://docs.pytorch.org/docs/2.15/generated/torch.t.html#torch.t "torch.t") | Expects `input` to be <= 2-D tensor and transposes dimensions 0 and 1. |
| [`transpose`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose.html#torch.transpose "torch.transpose") | Returns a tensor that is a transposed version of `input`. |
| [`vsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.vsplit.html#torch.vsplit "torch.vsplit") | Splits `input`, a tensor with two or more dimensions, into multiple tensors vertically according to `indices_or_sections`. |
| [`vstack`](https://docs.pytorch.org/docs/2.15/generated/torch.vstack.html#torch.vstack "torch.vstack") | Stack tensors in sequence vertically (row wise). |
| [`Tensor.expand`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand.html#torch.Tensor.expand "torch.Tensor.expand") | Returns a new view of the `self` tensor with singleton dimensions expanded to a larger size. |
| [`Tensor.expand_as`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand_as.html#torch.Tensor.expand_as "torch.Tensor.expand_as") | Expand this tensor to the same size as `other`. |
| [`Tensor.reshape`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape.html#torch.Tensor.reshape "torch.Tensor.reshape") | Returns a tensor with the same data and number of elements as `self` but with the specified shape. |
| [`Tensor.reshape_as`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape_as.html#torch.Tensor.reshape_as "torch.Tensor.reshape_as") | Returns this tensor as the same shape as `other`. |
| [`Tensor.unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.unfold.html#torch.Tensor.unfold "torch.Tensor.unfold") | Returns a view of the original tensor which contains all slices of size `size` from `self` tensor in the dimension `dimension`. |
| [`Tensor.view`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view") | Returns a new tensor with the same data as the `self` tensor but of a different `shape`. |

torch.masked.maskedtensor.core[#](https://docs.pytorch.org/docs/2.15/masked.html#torch-masked-maskedtensor-core "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`is_masked_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.masked.maskedtensor.core.is_masked_tensor.html#torch.masked.maskedtensor.core.is_masked_tensor "torch.masked.maskedtensor.core.is_masked_tensor") | Returns True if the input is a MaskedTensor, else False |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/masked.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/masked.md.txt)

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