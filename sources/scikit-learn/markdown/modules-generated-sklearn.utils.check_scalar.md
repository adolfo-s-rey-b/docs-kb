[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.check_scalar.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.check_scalar.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.check_scalar.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.check_scalar.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.check_scalar.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.check_scalar.html)

Collapse Sidebar Expand Sidebar

check\_scalar[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#check-scalar "Link to this heading")

========================================================================================================================================

sklearn.utils.check\_scalar(_x_, _name_, _target\_type_, _\*_, _min\_val\=None_, _max\_val\=None_, _include\_boundaries\='both'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1794)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#sklearn.utils.check_scalar "Link to this definition")

Validate scalar parameters type and value.

Parameters:

**x**object

The scalar parameter to validate.

**name**str

The name of the parameter to be printed in error messages.

**target\_type**type or tuple

Acceptable data types for the parameter.

**min\_val**float or int, default=None

The minimum valid value the parameter can take. If None (default) it is implied that the parameter does not have a lower bound.

**max\_val**float or int, default=None

The maximum valid value the parameter can take. If None (default) it is implied that the parameter does not have an upper bound.

**include\_boundaries**{“left”, “right”, “both”, “neither”}, default=”both”

Whether the interval defined by `min_val` and `max_val` should include the boundaries. Possible choices are:

*   `"left"`: only `min_val` is included in the valid interval. It is equivalent to the interval `[ min_val, max_val )`.\
    \
*   `"right"`: only `max_val` is included in the valid interval. It is equivalent to the interval `( min_val, max_val ]`.
    
*   `"both"`: `min_val` and `max_val` are included in the valid interval. It is equivalent to the interval `[ min_val, max_val ]`.
    
*   `"neither"`: neither `min_val` nor `max_val` are included in the valid interval. It is equivalent to the interval `( min_val, max_val )`.
    

Returns:

**x**numbers.Number

The validated number.

Raises:

TypeError

If the parameter’s type does not match the desired type.

ValueError

If the parameter’s value violates the given bounds. If `min_val`, `max_val` and `include_boundaries` are inconsistent.

Examples

\>>> from sklearn.utils.validation import check\_scalar
\>>> check\_scalar(10, "x", int, min\_val\=1, max\_val\=20)
10

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)