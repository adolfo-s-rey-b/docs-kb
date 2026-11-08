[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

Hyperparameter[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#hyperparameter "Link to this heading")

================================================================================================================================================================

class sklearn.gaussian\_process.kernels.Hyperparameter(_name_, _value\_type_, _bounds_, _n\_elements\=1_, _fixed\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L58)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter "Link to this definition")

A kernel hyperparameter’s specification in form of a namedtuple.

Added in version 0.18.

Attributes:

**name**str

The name of the hyperparameter. Note that a kernel using a hyperparameter with name “x” must have the attributes self.x and self.x\_bounds

**value\_type**str

The type of the hyperparameter. Currently, only “numeric” hyperparameters are supported.

**bounds**pair of floats >= 0 or “fixed”

The lower and upper bound on the parameter. If n\_elements>1, a pair of 1d array with n\_elements each may be given alternatively. If the string “fixed” is passed as bounds, the hyperparameter’s value cannot be changed.

**n\_elements**int, default=1

The number of elements of the hyperparameter value. Defaults to 1, which corresponds to a scalar hyperparameter. n\_elements > 1 corresponds to a hyperparameter which is vector-valued, such as, e.g., anisotropic length-scales.

**fixed**bool, default=None

Whether the value of this hyperparameter is fixed, i.e., cannot be changed during hyperparameter tuning. If None is passed, the “fixed” is derived based on the given bounds.

Examples

\>>> from sklearn.gaussian\_process.kernels import ConstantKernel
\>>> from sklearn.datasets import make\_friedman2
\>>> from sklearn.gaussian\_process import GaussianProcessRegressor
\>>> from sklearn.gaussian\_process.kernels import Hyperparameter
\>>> X, y \= make\_friedman2(n\_samples\=50, noise\=0, random\_state\=0)
\>>> kernel \= ConstantKernel(constant\_value\=1.0,
...    constant\_value\_bounds\=(0.0, 10.0))

Copy to clipboard

We can access each hyperparameter:

\>>> for hyperparameter in kernel.hyperparameters:
...    print(hyperparameter)
Hyperparameter(name='constant\_value', value\_type='numeric',
bounds=array(\[\[ 0., 10.\]\]), n\_elements=1, fixed=False)

Copy to clipboard

\>>> params \= kernel.get\_params()
\>>> for key in sorted(params): print(f"{key} : {params\[key\]}")
constant\_value : 1.0
constant\_value\_bounds : (0.0, 10.0)

Copy to clipboard

bounds[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/collections/__init__.py#L)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.bounds "Link to this definition")

Alias for field number 2

count(_value_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.count "Link to this definition")

Return number of occurrences of value.

fixed[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/collections/__init__.py#L)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.fixed "Link to this definition")

Alias for field number 4

index(_value_, _start\=0_, _stop\=sys.maxsize_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.index "Link to this definition")

Return first index of value.

Raises ValueError if the value is not present.

n\_elements[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/collections/__init__.py#L)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.n_elements "Link to this definition")

Alias for field number 3

name[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/collections/__init__.py#L)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.name "Link to this definition")

Alias for field number 0

value\_type[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/collections/__init__.py#L)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter.value_type "Link to this definition")

Alias for field number 1

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_thumb.png)

[Gaussian processes on discrete data structures](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)

Gaussian processes on discrete data structures

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)