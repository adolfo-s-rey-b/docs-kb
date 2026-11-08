Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/foreach.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/foreach.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/foreach.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/foreach.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/foreach.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/foreach.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/foreach.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/foreach.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/foreach.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/foreach.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/foreach.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/foreach.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/foreach.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/foreach.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/foreach.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/foreach.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/foreach.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/foreach.html)
[v1.13](https://docs.pytorch.org/docs/1.13/foreach.html)
[v1.12](https://docs.pytorch.org/docs/1.12/foreach.html)
[v1.11](https://docs.pytorch.org/docs/1.11/foreach.html)
[v1.10](https://docs.pytorch.org/docs/1.10/foreach.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/foreach.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/foreach.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/foreach.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/foreach.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/foreach.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/foreach.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/foreach.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/foreach.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/foreach.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/foreach.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/foreach.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/foreach.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/foreach.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/foreach.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/foreach.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/foreach.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/foreach.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/foreach.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/foreach.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/foreach.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/foreach.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/foreach.html)

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

torch.foreach[#](https://docs.pytorch.org/docs/2.15/foreach.html#module-torch.foreach "Link to this heading")

==============================================================================================================

Created On: Aug 20, 2026 | Last Updated On: Aug 20, 2026

Operations over lists of tensors.

Warning

`torch.foreach` is a beta API. Its signatures may change based on user feedback. Existing private `torch._foreach_*` functions remain available for compatibility during migration.

Each function applies the corresponding ordinary PyTorch operation to every position in one or more tensor lists.

The functions will use an accelerated multi-tensor implementation when their inputs meet its requirements. Otherwise they use a semantically equivalent per-tensor fallback. Calling a function in this module does not guarantee a single or fused kernel.

`torch.foreach` applies familiar PyTorch operations across lists of tensors. For example, `torch.foreach.add(inputs, other)` is semantically equivalent to a Python loop that applies [`torch.add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
 at every list position. When available on an accelerator and certain conditions are met, a foreach operation will use a horizontally fused multi-tensor kernel to improve runtime. On CUDA, common eligibility requirements include strided, non-overlapping dense tensors on the same device, compatible dtypes, and matching sizes and strides for corresponding tensors.

inputs \= \[torch.ones(2), torch.ones(3)\]
result \= torch.foreach.add(inputs, 2)
\# Equivalent to tuple(torch.add(tensor, 2) for tensor in inputs)

torch.foreach.mul\_(inputs, 3)
\# Mutates each tensor and returns \`inputs\`.

Copy to clipboard

API Coverage[#](https://docs.pytorch.org/docs/2.15/foreach.html#api-coverage "Link to this heading")

-----------------------------------------------------------------------------------------------------

A foreach API lifts an ordinary tensor operation over a list of inputs. This creates a combinatorial space of possible signatures. Depending on the operation, a tensor argument could be shared as a Tensor or supplied elementwise as a TensorList, while a scalar argument could be a Scalar, a ScalarList, a shared 0-D Tensor, or a packed 1-D CPU Tensor.

You can then imagine that one operation may take on various forms such as TensorList/TensorList, TensorList/Tensor, TensorList/ScalarList, TensorList/Scalar, etc. Operations with more parameters would have more combinations. The public foreach APIs support a subset of these combinations based on usage. If you would like to see an implementation of a missing combination, please file an [issue](https://github.com/pytorch/pytorch/issues/new/choose)
!

Across the supported signatures, we maintain constraints that TensorList and ScalarList arguments must be non-empty, and corresponding tensor and scalar lists must have the same length.

Only signatures that explicitly list `Tensor` include it in the supported typed surface. A 0-D Tensor that does not require gradients may sometimes be accepted for a `Scalar` parameter through implicit scalar conversion. Converting an accelerator Tensor this way reads its value on the host, which may be expensive. On CUDA, this synchronizes eager execution and is unsupported during CUDA graph capture, so it should not be relied upon as a Tensor overload.

The public foreach API also does not support `out=` variants and may have a higher memory footprint than looping through the non-foreach original API, as multiple intermediates can be alive simultaneously.

Migrating from the private API[#](https://docs.pytorch.org/docs/2.15/foreach.html#migrating-from-the-private-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

You may be familiar with the private spellings of foreach APIs, e.g., for [`torch.add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
:

torch.\_foreach\_add(inputs, other)  \# Private spelling
torch.foreach.add(inputs, other)   \# Public beta spelling

Copy to clipboard

The private spellings remain available with unchanged signatures for backward compatibility. Public functions call the same ATen operators but improve API consistency in two ways:

1.  All required operands are positional-only, and all optional parameters are keyword-only.
    
2.  Parameter names align with the corresponding ordinary operation.
    

The primary tensor-list argument that the foreach API applies over is named `inputs`, and other arguments retain the ordinary operation’s logical name, even when the currently supported form requires a list. This keeps signatures descriptive as operand forms evolve.

Unary operations[#](https://docs.pytorch.org/docs/2.15/foreach.html#unary-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`abs`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.abs.html#torch.foreach.abs "torch.foreach.abs") | Applies [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs")<br> to each tensor in `inputs`. |
| [`abs_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.abs_.html#torch.foreach.abs_ "torch.foreach.abs_") | Applies [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs")<br> to each tensor in `inputs` in-place. |
| [`acos`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.acos.html#torch.foreach.acos "torch.foreach.acos") | Applies [`torch.acos()`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos")<br> to each tensor in `inputs`. |
| [`acos_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.acos_.html#torch.foreach.acos_ "torch.foreach.acos_") | Applies [`torch.acos()`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos")<br> to each tensor in `inputs` in-place. |
| [`asin`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.asin.html#torch.foreach.asin "torch.foreach.asin") | Applies [`torch.asin()`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin")<br> to each tensor in `inputs`. |
| [`asin_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.asin_.html#torch.foreach.asin_ "torch.foreach.asin_") | Applies [`torch.asin()`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin")<br> to each tensor in `inputs` in-place. |
| [`atan`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.atan.html#torch.foreach.atan "torch.foreach.atan") | Applies [`torch.atan()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan")<br> to each tensor in `inputs`. |
| [`atan_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.atan_.html#torch.foreach.atan_ "torch.foreach.atan_") | Applies [`torch.atan()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan")<br> to each tensor in `inputs` in-place. |
| [`ceil`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.ceil.html#torch.foreach.ceil "torch.foreach.ceil") | Applies [`torch.ceil()`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil.html#torch.ceil "torch.ceil")<br> to each tensor in `inputs`. |
| [`ceil_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.ceil_.html#torch.foreach.ceil_ "torch.foreach.ceil_") | Applies [`torch.ceil()`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil.html#torch.ceil "torch.ceil")<br> to each tensor in `inputs` in-place. |
| [`clone`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.clone.html#torch.foreach.clone "torch.foreach.clone") | Clones every tensor in `inputs`. |
| [`cos`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.cos.html#torch.foreach.cos "torch.foreach.cos") | Applies [`torch.cos()`](https://docs.pytorch.org/docs/2.15/generated/torch.cos.html#torch.cos "torch.cos")<br> to each tensor in `inputs`. |
| [`cos_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.cos_.html#torch.foreach.cos_ "torch.foreach.cos_") | Applies [`torch.cos()`](https://docs.pytorch.org/docs/2.15/generated/torch.cos.html#torch.cos "torch.cos")<br> to each tensor in `inputs` in-place. |
| [`cosh`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.cosh.html#torch.foreach.cosh "torch.foreach.cosh") | Applies [`torch.cosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh.html#torch.cosh "torch.cosh")<br> to each tensor in `inputs`. |
| [`cosh_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.cosh_.html#torch.foreach.cosh_ "torch.foreach.cosh_") | Applies [`torch.cosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh.html#torch.cosh "torch.cosh")<br> to each tensor in `inputs` in-place. |
| [`erf`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.erf.html#torch.foreach.erf "torch.foreach.erf") | Applies [`torch.erf()`](https://docs.pytorch.org/docs/2.15/generated/torch.erf.html#torch.erf "torch.erf")<br> to each tensor in `inputs`. |
| [`erf_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.erf_.html#torch.foreach.erf_ "torch.foreach.erf_") | Applies [`torch.erf()`](https://docs.pytorch.org/docs/2.15/generated/torch.erf.html#torch.erf "torch.erf")<br> to each tensor in `inputs` in-place. |
| [`erfc`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.erfc.html#torch.foreach.erfc "torch.foreach.erfc") | Applies [`torch.erfc()`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc.html#torch.erfc "torch.erfc")<br> to each tensor in `inputs`. |
| [`erfc_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.erfc_.html#torch.foreach.erfc_ "torch.foreach.erfc_") | Applies [`torch.erfc()`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc.html#torch.erfc "torch.erfc")<br> to each tensor in `inputs` in-place. |
| [`exp`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.exp.html#torch.foreach.exp "torch.foreach.exp") | Applies [`torch.exp()`](https://docs.pytorch.org/docs/2.15/generated/torch.exp.html#torch.exp "torch.exp")<br> to each tensor in `inputs`. |
| [`exp_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.exp_.html#torch.foreach.exp_ "torch.foreach.exp_") | Applies [`torch.exp()`](https://docs.pytorch.org/docs/2.15/generated/torch.exp.html#torch.exp "torch.exp")<br> to each tensor in `inputs` in-place. |
| [`expm1`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.expm1.html#torch.foreach.expm1 "torch.foreach.expm1") | Applies [`torch.expm1()`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1.html#torch.expm1 "torch.expm1")<br> to each tensor in `inputs`. |
| [`expm1_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.expm1_.html#torch.foreach.expm1_ "torch.foreach.expm1_") | Applies [`torch.expm1()`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1.html#torch.expm1 "torch.expm1")<br> to each tensor in `inputs` in-place. |
| [`floor`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.floor.html#torch.foreach.floor "torch.foreach.floor") | Applies [`torch.floor()`](https://docs.pytorch.org/docs/2.15/generated/torch.floor.html#torch.floor "torch.floor")<br> to each tensor in `inputs`. |
| [`floor_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.floor_.html#torch.foreach.floor_ "torch.foreach.floor_") | Applies [`torch.floor()`](https://docs.pytorch.org/docs/2.15/generated/torch.floor.html#torch.floor "torch.floor")<br> to each tensor in `inputs` in-place. |
| [`frac`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.frac.html#torch.foreach.frac "torch.foreach.frac") | Applies [`torch.frac()`](https://docs.pytorch.org/docs/2.15/generated/torch.frac.html#torch.frac "torch.frac")<br> to each tensor in `inputs`. |
| [`frac_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.frac_.html#torch.foreach.frac_ "torch.foreach.frac_") | Applies [`torch.frac()`](https://docs.pytorch.org/docs/2.15/generated/torch.frac.html#torch.frac "torch.frac")<br> to each tensor in `inputs` in-place. |
| [`lgamma`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.lgamma.html#torch.foreach.lgamma "torch.foreach.lgamma") | Applies [`torch.lgamma()`](https://docs.pytorch.org/docs/2.15/generated/torch.lgamma.html#torch.lgamma "torch.lgamma")<br> to each tensor in `inputs`. |
| [`lgamma_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.lgamma_.html#torch.foreach.lgamma_ "torch.foreach.lgamma_") | Applies [`torch.lgamma()`](https://docs.pytorch.org/docs/2.15/generated/torch.lgamma.html#torch.lgamma "torch.lgamma")<br> to each tensor in `inputs` in-place. |
| [`log`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log.html#torch.foreach.log "torch.foreach.log") | Applies [`torch.log()`](https://docs.pytorch.org/docs/2.15/generated/torch.log.html#torch.log "torch.log")<br> to each tensor in `inputs`. |
| [`log_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log_.html#torch.foreach.log_ "torch.foreach.log_") | Applies [`torch.log()`](https://docs.pytorch.org/docs/2.15/generated/torch.log.html#torch.log "torch.log")<br> to each tensor in `inputs` in-place. |
| [`log10`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log10.html#torch.foreach.log10 "torch.foreach.log10") | Applies [`torch.log10()`](https://docs.pytorch.org/docs/2.15/generated/torch.log10.html#torch.log10 "torch.log10")<br> to each tensor in `inputs`. |
| [`log10_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log10_.html#torch.foreach.log10_ "torch.foreach.log10_") | Applies [`torch.log10()`](https://docs.pytorch.org/docs/2.15/generated/torch.log10.html#torch.log10 "torch.log10")<br> to each tensor in `inputs` in-place. |
| [`log1p`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log1p.html#torch.foreach.log1p "torch.foreach.log1p") | Applies [`torch.log1p()`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p")<br> to each tensor in `inputs`. |
| [`log1p_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log1p_.html#torch.foreach.log1p_ "torch.foreach.log1p_") | Applies [`torch.log1p()`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p")<br> to each tensor in `inputs` in-place. |
| [`log2`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log2.html#torch.foreach.log2 "torch.foreach.log2") | Applies [`torch.log2()`](https://docs.pytorch.org/docs/2.15/generated/torch.log2.html#torch.log2 "torch.log2")<br> to each tensor in `inputs`. |
| [`log2_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.log2_.html#torch.foreach.log2_ "torch.foreach.log2_") | Applies [`torch.log2()`](https://docs.pytorch.org/docs/2.15/generated/torch.log2.html#torch.log2 "torch.log2")<br> to each tensor in `inputs` in-place. |
| [`neg`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.neg.html#torch.foreach.neg "torch.foreach.neg") | Applies [`torch.neg()`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg")<br> to each tensor in `inputs`. |
| [`neg_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.neg_.html#torch.foreach.neg_ "torch.foreach.neg_") | Applies [`torch.neg()`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg")<br> to each tensor in `inputs` in-place. |
| [`reciprocal`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.reciprocal.html#torch.foreach.reciprocal "torch.foreach.reciprocal") | Applies [`torch.reciprocal()`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal.html#torch.reciprocal "torch.reciprocal")<br> to each tensor in `inputs`. |
| [`reciprocal_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.reciprocal_.html#torch.foreach.reciprocal_ "torch.foreach.reciprocal_") | Applies [`torch.reciprocal()`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal.html#torch.reciprocal "torch.reciprocal")<br> to each tensor in `inputs` in-place. |
| [`round`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.round.html#torch.foreach.round "torch.foreach.round") | Applies [`torch.round()`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round")<br> to each tensor in `inputs`. |
| [`round_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.round_.html#torch.foreach.round_ "torch.foreach.round_") | Applies [`torch.round()`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round")<br> to each tensor in `inputs` in-place. |
| [`rsqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.rsqrt.html#torch.foreach.rsqrt "torch.foreach.rsqrt") | Applies [`torch.rsqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt.html#torch.rsqrt "torch.rsqrt")<br> to each tensor in `inputs`. |
| [`rsqrt_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.rsqrt_.html#torch.foreach.rsqrt_ "torch.foreach.rsqrt_") | Applies [`torch.rsqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt.html#torch.rsqrt "torch.rsqrt")<br> to each tensor in `inputs` in-place. |
| [`sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sigmoid.html#torch.foreach.sigmoid "torch.foreach.sigmoid") | Applies [`torch.sigmoid()`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid.html#torch.sigmoid "torch.sigmoid")<br> to each tensor in `inputs`. |
| [`sigmoid_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sigmoid_.html#torch.foreach.sigmoid_ "torch.foreach.sigmoid_") | Applies [`torch.sigmoid()`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid.html#torch.sigmoid "torch.sigmoid")<br> to each tensor in `inputs` in-place. |
| [`sign`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sign.html#torch.foreach.sign "torch.foreach.sign") | Applies [`torch.sign()`](https://docs.pytorch.org/docs/2.15/generated/torch.sign.html#torch.sign "torch.sign")<br> to each tensor in `inputs`. |
| [`sign_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sign_.html#torch.foreach.sign_ "torch.foreach.sign_") | Applies [`torch.sign()`](https://docs.pytorch.org/docs/2.15/generated/torch.sign.html#torch.sign "torch.sign")<br> to each tensor in `inputs` in-place. |
| [`sin`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sin.html#torch.foreach.sin "torch.foreach.sin") | Applies [`torch.sin()`](https://docs.pytorch.org/docs/2.15/generated/torch.sin.html#torch.sin "torch.sin")<br> to each tensor in `inputs`. |
| [`sin_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sin_.html#torch.foreach.sin_ "torch.foreach.sin_") | Applies [`torch.sin()`](https://docs.pytorch.org/docs/2.15/generated/torch.sin.html#torch.sin "torch.sin")<br> to each tensor in `inputs` in-place. |
| [`sinh`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sinh.html#torch.foreach.sinh "torch.foreach.sinh") | Applies [`torch.sinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh.html#torch.sinh "torch.sinh")<br> to each tensor in `inputs`. |
| [`sinh_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sinh_.html#torch.foreach.sinh_ "torch.foreach.sinh_") | Applies [`torch.sinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh.html#torch.sinh "torch.sinh")<br> to each tensor in `inputs` in-place. |
| [`sqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sqrt.html#torch.foreach.sqrt "torch.foreach.sqrt") | Applies [`torch.sqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt.html#torch.sqrt "torch.sqrt")<br> to each tensor in `inputs`. |
| [`sqrt_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sqrt_.html#torch.foreach.sqrt_ "torch.foreach.sqrt_") | Applies [`torch.sqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt.html#torch.sqrt "torch.sqrt")<br> to each tensor in `inputs` in-place. |
| [`tan`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.tan.html#torch.foreach.tan "torch.foreach.tan") | Applies [`torch.tan()`](https://docs.pytorch.org/docs/2.15/generated/torch.tan.html#torch.tan "torch.tan")<br> to each tensor in `inputs`. |
| [`tan_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.tan_.html#torch.foreach.tan_ "torch.foreach.tan_") | Applies [`torch.tan()`](https://docs.pytorch.org/docs/2.15/generated/torch.tan.html#torch.tan "torch.tan")<br> to each tensor in `inputs` in-place. |
| [`tanh`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.tanh.html#torch.foreach.tanh "torch.foreach.tanh") | Applies [`torch.tanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh.html#torch.tanh "torch.tanh")<br> to each tensor in `inputs`. |
| [`tanh_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.tanh_.html#torch.foreach.tanh_ "torch.foreach.tanh_") | Applies [`torch.tanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh.html#torch.tanh "torch.tanh")<br> to each tensor in `inputs` in-place. |
| [`trunc`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.trunc.html#torch.foreach.trunc "torch.foreach.trunc") | Applies [`torch.trunc()`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc")<br> to each tensor in `inputs`. |
| [`trunc_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.trunc_.html#torch.foreach.trunc_ "torch.foreach.trunc_") | Applies [`torch.trunc()`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc")<br> to each tensor in `inputs` in-place. |
| [`zero_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.zero_.html#torch.foreach.zero_ "torch.foreach.zero_") | Fills every tensor in `inputs` with zero. |

Binary operations[#](https://docs.pytorch.org/docs/2.15/foreach.html#binary-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`add`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.add.html#torch.foreach.add "torch.foreach.add") | Applies [`torch.add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")<br> to every tensor in `inputs`. |
| [`add_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.add_.html#torch.foreach.add_ "torch.foreach.add_") | Applies [`torch.add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")<br> to every tensor in `inputs`. |
| [`sub`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sub.html#torch.foreach.sub "torch.foreach.sub") | Applies [`torch.sub()`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub")<br> to every tensor in `inputs`. |
| [`sub_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.sub_.html#torch.foreach.sub_ "torch.foreach.sub_") | Applies [`torch.sub()`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub")<br> to every tensor in `inputs`. |
| [`mul`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.mul.html#torch.foreach.mul "torch.foreach.mul") | Applies [`torch.mul()`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul")<br> to every tensor in `inputs`. |
| [`mul_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.mul_.html#torch.foreach.mul_ "torch.foreach.mul_") | Applies [`torch.mul()`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul")<br> to every tensor in `inputs`. |
| [`div`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.div.html#torch.foreach.div "torch.foreach.div") | Applies [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br> to every tensor in `inputs`. |
| [`div_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.div_.html#torch.foreach.div_ "torch.foreach.div_") | Applies [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br> to every tensor in `inputs`. |
| [`clamp_min`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.clamp_min.html#torch.foreach.clamp_min "torch.foreach.clamp_min") | Applies [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br> to every tensor in `inputs`. |
| [`clamp_min_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.clamp_min_.html#torch.foreach.clamp_min_ "torch.foreach.clamp_min_") | Applies [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br> to every tensor in `inputs`. |
| [`clamp_max`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.clamp_max.html#torch.foreach.clamp_max "torch.foreach.clamp_max") | Applies [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br> to every tensor in `inputs`. |
| [`clamp_max_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.clamp_max_.html#torch.foreach.clamp_max_ "torch.foreach.clamp_max_") | Applies [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br> to every tensor in `inputs`. |
| [`minimum`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.minimum.html#torch.foreach.minimum "torch.foreach.minimum") | Applies [`torch.minimum()`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum")<br> to every tensor in `inputs`. |
| [`minimum_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.minimum_.html#torch.foreach.minimum_ "torch.foreach.minimum_") | Applies [`torch.minimum()`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum")<br> to every tensor in `inputs`. |
| [`maximum`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.maximum.html#torch.foreach.maximum "torch.foreach.maximum") | Applies [`torch.maximum()`](https://docs.pytorch.org/docs/2.15/generated/torch.maximum.html#torch.maximum "torch.maximum")<br> to every tensor in `inputs`. |
| [`maximum_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.maximum_.html#torch.foreach.maximum_ "torch.foreach.maximum_") | Applies [`torch.maximum()`](https://docs.pytorch.org/docs/2.15/generated/torch.maximum.html#torch.maximum "torch.maximum")<br> to every tensor in `inputs`. |
| [`pow`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.pow.html#torch.foreach.pow "torch.foreach.pow") | Applies [`torch.pow()`](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#torch.pow "torch.pow")<br> at each list position. |
| [`pow_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.pow_.html#torch.foreach.pow_ "torch.foreach.pow_") | In-place version of [`torch.foreach.pow()`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.pow.html#torch.foreach.pow "torch.foreach.pow")<br>. |
| [`copy_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.copy_.html#torch.foreach.copy_ "torch.foreach.copy_") | Copies each tensor in `src` into the corresponding tensor in `inputs`, following [`torch.Tensor.copy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.copy_.html#torch.Tensor.copy_ "torch.Tensor.copy_")<br>. |

Pointwise operations[#](https://docs.pytorch.org/docs/2.15/foreach.html#pointwise-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`addcmul`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.addcmul.html#torch.foreach.addcmul "torch.foreach.addcmul") | Applies [`torch.addcmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#torch.addcmul "torch.addcmul")<br> to corresponding tensors from the three input lists. |
| [`addcmul_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.addcmul_.html#torch.foreach.addcmul_ "torch.foreach.addcmul_") | Applies [`torch.addcmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#torch.addcmul "torch.addcmul")<br> to corresponding tensors from the three input lists. |
| [`addcdiv`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.addcdiv.html#torch.foreach.addcdiv "torch.foreach.addcdiv") | Applies [`torch.addcdiv()`](https://docs.pytorch.org/docs/2.15/generated/torch.addcdiv.html#torch.addcdiv "torch.addcdiv")<br> to corresponding tensors from the three input lists. |
| [`addcdiv_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.addcdiv_.html#torch.foreach.addcdiv_ "torch.foreach.addcdiv_") | Applies [`torch.addcdiv()`](https://docs.pytorch.org/docs/2.15/generated/torch.addcdiv.html#torch.addcdiv "torch.addcdiv")<br> to corresponding tensors from the three input lists. |
| [`lerp`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.lerp.html#torch.foreach.lerp "torch.foreach.lerp") | Applies [`torch.lerp()`](https://docs.pytorch.org/docs/2.15/generated/torch.lerp.html#torch.lerp "torch.lerp")<br> to corresponding tensors in `inputs` and `end`. |
| [`lerp_`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.lerp_.html#torch.foreach.lerp_ "torch.foreach.lerp_") | In-place version of [`torch.foreach.lerp()`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.lerp.html#torch.foreach.lerp "torch.foreach.lerp")<br>. |

Reductions and matrix operations[#](https://docs.pytorch.org/docs/2.15/foreach.html#reductions-and-matrix-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.max.html#torch.foreach.max "torch.foreach.max") | Returns the maximum value of each tensor in `inputs`. |
| [`norm`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.norm.html#torch.foreach.norm "torch.foreach.norm") | Returns the vector norm of each tensor in `inputs`. |
| [`mm`](https://docs.pytorch.org/docs/2.15/generated/torch.foreach.mm.html#torch.foreach.mm "torch.foreach.mm") | Multiplies corresponding matrices from `inputs` and `mat2` using [`torch.mm()`](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#torch.mm "torch.mm")<br>. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/foreach.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/foreach.md.txt)

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