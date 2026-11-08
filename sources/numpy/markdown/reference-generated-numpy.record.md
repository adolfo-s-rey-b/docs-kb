[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.record.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.record.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.record.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.record.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.record.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.record.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.record.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.record.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.record.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.record.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.record.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.record.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.record.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.record.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.record.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.record.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.record.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.record.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.record.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.record.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.record.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.record.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.record[#](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy-record "Link to this heading")

========================================================================================================================

_class_ numpy.record(_length\_or\_data_, _/_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "Link to this definition")

A data-type scalar that allows field access as attribute lookup.

Attributes:

[`T`](https://numpy.org/doc/stable/reference/generated/numpy.record.T.html#numpy.record.T "numpy.record.T")

Scalar attribute identical to [`ndarray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T")
.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.record.base.html#numpy.record.base "numpy.record.base")

base object

[`data`](https://numpy.org/doc/stable/reference/generated/numpy.record.data.html#numpy.record.data "numpy.record.data")

Pointer to start of data.

**device**

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

dtype object

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.record.flags.html#numpy.record.flags "numpy.record.flags")

integer value of flags

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.record.flat.html#numpy.record.flat "numpy.record.flat")

A 1-D view of the scalar.

[`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")

The imaginary part of the scalar.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.record.itemsize.html#numpy.record.itemsize "numpy.record.itemsize")

The length of one element in bytes.

**nbytes**

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

The number of array dimensions.

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")

The real part of the scalar.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Tuple of array dimensions.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")

The number of elements in the gentype.

[`strides`](https://numpy.org/doc/stable/reference/generated/numpy.record.strides.html#numpy.record.strides "numpy.record.strides")

Tuple of bytes steps in each dimension.

Methods

|     |     |
| --- | --- |
| [`all`](https://numpy.org/doc/stable/reference/generated/numpy.record.all.html#numpy.record.all "numpy.record.all")<br>(/\[, axis, out, keepdims, where\]) | Scalar method identical to [`ndarray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")<br>. |
| [`any`](https://numpy.org/doc/stable/reference/generated/numpy.record.any.html#numpy.record.any "numpy.record.any")<br>(/\[, axis, out, keepdims, where\]) | Scalar method identical to [`ndarray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")<br>. |
| [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.record.argmax.html#numpy.record.argmax "numpy.record.argmax")<br>(/\[, axis, out, keepdims\]) | Scalar method identical to [`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")<br>. |
| [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.record.argmin.html#numpy.record.argmin "numpy.record.argmin")<br>(/\[, axis, out, keepdims\]) | Scalar method identical to [`ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")<br>. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.record.argsort.html#numpy.record.argsort "numpy.record.argsort")<br>(/\[, axis, kind, order, stable, ...\]) | Scalar method identical to [`ndarray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html#numpy.ndarray.argsort "numpy.ndarray.argsort")<br>. |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.record.astype.html#numpy.record.astype "numpy.record.astype")<br>(/, dtype\[, order, casting, subok, copy\]) | Scalar method identical to [`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")<br>. |
| [`byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.record.byteswap.html#numpy.record.byteswap "numpy.record.byteswap")<br>(/\[, inplace\]) | Scalar method identical to [`ndarray.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.byteswap.html#numpy.ndarray.byteswap "numpy.ndarray.byteswap")<br>. |
| [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.record.choose.html#numpy.record.choose "numpy.record.choose")<br>(/, choices\[, out, mode\]) | Scalar method identical to [`ndarray.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html#numpy.ndarray.choose "numpy.ndarray.choose")<br>. |
| [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.record.clip.html#numpy.record.clip "numpy.record.clip")<br>(/\[, min, max, out\]) | Scalar method identical to [`ndarray.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.clip.html#numpy.ndarray.clip "numpy.ndarray.clip")<br>. |
| [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.record.compress.html#numpy.record.compress "numpy.record.compress")<br>(/, condition\[, axis, out\]) | Scalar method identical to [`ndarray.compress`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html#numpy.ndarray.compress "numpy.ndarray.compress")<br>. |
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.record.conj.html#numpy.record.conj "numpy.record.conj")<br>(/) | Scalar method identical to [`ndarray.conj`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conj.html#numpy.ndarray.conj "numpy.ndarray.conj")<br>. |
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.record.conjugate.html#numpy.record.conjugate "numpy.record.conjugate")<br>(/) | Scalar method identical to [`ndarray.conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conjugate.html#numpy.ndarray.conjugate "numpy.ndarray.conjugate")<br>. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.record.copy.html#numpy.record.copy "numpy.record.copy")<br>(/\[, order\]) | Scalar method identical to [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")<br>. |
| [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.record.cumprod.html#numpy.record.cumprod "numpy.record.cumprod")<br>(/\[, axis, dtype, out\]) | Scalar method identical to [`ndarray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")<br>. |
| [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.record.cumsum.html#numpy.record.cumsum "numpy.record.cumsum")<br>(/\[, axis, dtype, out\]) | Scalar method identical to [`ndarray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html#numpy.ndarray.cumsum "numpy.ndarray.cumsum")<br>. |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.record.diagonal.html#numpy.record.diagonal "numpy.record.diagonal")<br>(/\[, offset, axis1, axis2\]) | Scalar method identical to [`ndarray.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.diagonal.html#numpy.ndarray.diagonal "numpy.ndarray.diagonal")<br>. |
| [`dump`](https://numpy.org/doc/stable/reference/generated/numpy.record.dump.html#numpy.record.dump "numpy.record.dump")<br>(/, file) | Scalar method identical to [`ndarray.dump`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dump.html#numpy.ndarray.dump "numpy.ndarray.dump")<br>. |
| [`dumps`](https://numpy.org/doc/stable/reference/generated/numpy.record.dumps.html#numpy.record.dumps "numpy.record.dumps")<br>(/) | Scalar method identical to [`ndarray.dumps`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dumps.html#numpy.ndarray.dumps "numpy.ndarray.dumps")<br>. |
| [`fill`](https://numpy.org/doc/stable/reference/generated/numpy.record.fill.html#numpy.record.fill "numpy.record.fill")<br>(/, value) | Scalar method identical to [`ndarray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill")<br>. |
| [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.record.flatten.html#numpy.record.flatten "numpy.record.flatten")<br>(/\[, order\]) | Scalar method identical to [`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")<br>. |
| [`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.record.getfield.html#numpy.record.getfield "numpy.record.getfield") | Scalar method identical to [`ndarray.getfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.getfield.html#numpy.ndarray.getfield "numpy.ndarray.getfield")<br>. |
| [`item`](https://numpy.org/doc/stable/reference/generated/numpy.record.item.html#numpy.record.item "numpy.record.item")<br>(\*args) | Scalar method identical to [`ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")<br>. |
| [`max`](https://numpy.org/doc/stable/reference/generated/numpy.record.max.html#numpy.record.max "numpy.record.max")<br>(/\[, axis, out\]) | Scalar method identical to [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")<br>. |
| [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.record.mean.html#numpy.record.mean "numpy.record.mean")<br>(/\[, axis, dtype, out\]) | Scalar method identical to [`ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "numpy.ndarray.mean")<br>. |
| [`min`](https://numpy.org/doc/stable/reference/generated/numpy.record.min.html#numpy.record.min "numpy.record.min")<br>(/\[, axis, out\]) | Scalar method identical to [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")<br>. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.record.nonzero.html#numpy.record.nonzero "numpy.record.nonzero")<br>(/) | Scalar method identical to [`ndarray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")<br>. |
| [`pprint`](https://numpy.org/doc/stable/reference/generated/numpy.record.pprint.html#numpy.record.pprint "numpy.record.pprint")<br>() | Pretty-print all fields. |
| [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.record.prod.html#numpy.record.prod "numpy.record.prod")<br>(/\[, axis, dtype, out\]) | Scalar method identical to [`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")<br>. |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.record.put.html#numpy.record.put "numpy.record.put")<br>(indices, values, /\[, mode\]) | Scalar method identical to [`ndarray.put`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.put.html#numpy.ndarray.put "numpy.ndarray.put")<br>. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.record.ravel.html#numpy.record.ravel "numpy.record.ravel")<br>(/\[, order\]) | Scalar method identical to [`ndarray.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html#numpy.ndarray.ravel "numpy.ndarray.ravel")<br>. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.record.repeat.html#numpy.record.repeat "numpy.record.repeat")<br>(repeats, /\[, axis\]) | Scalar method identical to [`ndarray.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.repeat.html#numpy.ndarray.repeat "numpy.ndarray.repeat")<br>. |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.record.reshape.html#numpy.record.reshape "numpy.record.reshape")<br>(\*shape\[, order, copy\]) | Scalar method identical to [`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")<br>. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.record.resize.html#numpy.record.resize "numpy.record.resize")<br>(\*new\_shape\[, refcheck\]) | Scalar method identical to [`ndarray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize")<br>. |
| [`round`](https://numpy.org/doc/stable/reference/generated/numpy.record.round.html#numpy.record.round "numpy.record.round")<br>(/\[, decimals, out\]) | Scalar method identical to [`ndarray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")<br>. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.record.searchsorted.html#numpy.record.searchsorted "numpy.record.searchsorted")<br>(v, /\[, side, sorter\]) | Scalar method identical to [`ndarray.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html#numpy.ndarray.searchsorted "numpy.ndarray.searchsorted")<br>. |
| [`setfield`](https://numpy.org/doc/stable/reference/generated/numpy.record.setfield.html#numpy.record.setfield "numpy.record.setfield") | Scalar method identical to [`ndarray.setfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setfield.html#numpy.ndarray.setfield "numpy.ndarray.setfield")<br>. |
| [`setflags`](https://numpy.org/doc/stable/reference/generated/numpy.record.setflags.html#numpy.record.setflags "numpy.record.setflags")<br>(\*\[, write, align, uic\]) | Scalar method identical to [`ndarray.setflags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags "numpy.ndarray.setflags")<br>. |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.record.sort.html#numpy.record.sort "numpy.record.sort")<br>(/\[, axis, kind, order, stable, descending\]) | Scalar method identical to [`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")<br>. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.record.squeeze.html#numpy.record.squeeze "numpy.record.squeeze")<br>(/\[, axis\]) | Scalar method identical to [`ndarray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html#numpy.ndarray.squeeze "numpy.ndarray.squeeze")<br>. |
| [`std`](https://numpy.org/doc/stable/reference/generated/numpy.record.std.html#numpy.record.std "numpy.record.std")<br>(/\[, axis, dtype, out, ddof\]) | Scalar method identical to [`ndarray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html#numpy.ndarray.std "numpy.ndarray.std")<br>. |
| [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.record.sum.html#numpy.record.sum "numpy.record.sum")<br>(/\[, axis, dtype, out\]) | Scalar method identical to [`ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")<br>. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.record.swapaxes.html#numpy.record.swapaxes "numpy.record.swapaxes")<br>(axis1, axis2, /) | Scalar method identical to [`ndarray.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.swapaxes.html#numpy.ndarray.swapaxes "numpy.ndarray.swapaxes")<br>. |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.record.take.html#numpy.record.take "numpy.record.take")<br>(indices, /\[, axis, out, mode\]) | Scalar method identical to [`ndarray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take")<br>. |
| [`to_device`](https://numpy.org/doc/stable/reference/generated/numpy.record.to_device.html#numpy.record.to_device "numpy.record.to_device")<br>(device, \*\[, stream\]) | Scalar method identical to [`ndarray.to_device`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.to_device.html#numpy.ndarray.to_device "numpy.ndarray.to_device")<br>. |
| [`tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.record.tobytes.html#numpy.record.tobytes "numpy.record.tobytes")<br>(/\[, order\]) | Scalar method identical to [`ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")<br>. |
| [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.record.tofile.html#numpy.record.tofile "numpy.record.tofile")<br>(fid, /\[, sep, format\]) | Scalar method identical to [`ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")<br>. |
| [`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.record.tolist.html#numpy.record.tolist "numpy.record.tolist")<br>(/) | Scalar method identical to [`ndarray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "numpy.ndarray.tolist")<br>. |
| [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.record.trace.html#numpy.record.trace "numpy.record.trace")<br>(/\[, offset, axis1, axis2, dtype, out\]) | Scalar method identical to [`ndarray.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.trace.html#numpy.ndarray.trace "numpy.ndarray.trace")<br>. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.record.transpose.html#numpy.record.transpose "numpy.record.transpose")<br>(\*axes) | Scalar method identical to [`ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")<br>. |
| [`var`](https://numpy.org/doc/stable/reference/generated/numpy.record.var.html#numpy.record.var "numpy.record.var")<br>(/\[, axis, dtype, out, ddof\]) | Scalar method identical to [`ndarray.var`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html#numpy.ndarray.var "numpy.ndarray.var")<br>. |
| [`view`](https://numpy.org/doc/stable/reference/generated/numpy.record.view.html#numpy.record.view "numpy.record.view")<br>(\*args, \*\*kwargs) | Scalar method identical to [`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")<br>. |

On this page