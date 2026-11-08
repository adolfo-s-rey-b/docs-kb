[Skip to main content](https://numpy.org/doc/stable/reference/security.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/security.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/security.html)
[2.4](https://numpy.org/doc/2.4/reference/security.html)
[2.3](https://numpy.org/doc/2.3/reference/security.html)
[2.2](https://numpy.org/doc/2.2/reference/security.html)
[2.1](https://numpy.org/doc/2.1/reference/security.html)
[2.0](https://numpy.org/doc/2.0/reference/security.html)
[1.26](https://numpy.org/doc/1.26/reference/security.html)
[1.25](https://numpy.org/doc/1.25/reference/security.html)
[1.24](https://numpy.org/doc/1.24/reference/security.html)
[1.23](https://numpy.org/doc/1.23/reference/security.html)
[1.22](https://numpy.org/doc/1.22/reference/security.html)
[1.21](https://numpy.org/doc/1.21/reference/security.html)
[1.20](https://numpy.org/doc/1.20/reference/security.html)
[1.19](https://numpy.org/doc/1.19/reference/security.html)
[1.18](https://numpy.org/doc/1.18/reference/security.html)
[1.17](https://numpy.org/doc/1.17/reference/security.html)
[1.16](https://numpy.org/doc/1.16/reference/security.html)
[1.15](https://numpy.org/doc/1.15/reference/security.html)
[1.14](https://numpy.org/doc/1.14/reference/security.html)
[1.13](https://numpy.org/doc/1.13/reference/security.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NumPy security[#](https://numpy.org/doc/stable/reference/security.html#numpy-security "Link to this heading")

==============================================================================================================

Security issues can be reported privately as described in the project README and when opening a [new issue on the issue tracker](https://github.com/numpy/numpy/issues/new/choose)
.

NumPy’s maintainers are not security experts. However, we are conscientious about security and experts of both the NumPy codebase and how it’s used. Please do notify us before creating security advisories against NumPy as we are happy to prioritize issues or help with assessing the severity of a bug. A security advisory we are not aware of beforehand can lead to a lot of work for all involved parties.

Important[#](https://numpy.org/doc/stable/reference/security.html#important "Link to this heading")

----------------------------------------------------------------------------------------------------

NumPy is not designed to be exposed directly to untrusted users. A user who can freely execute NumPy (or Python) functions must be considered to have the same privileges as the process/Python interpreter.

If one can already execute Python code, there are far worse things one can do than use all available CPU cycles, or provoke a symptom of a bug in Code like use-after-free or a segfault. Therefore, while such issues may be bugs, they are not security issues.

Before reporting a security issue, please consider and describe the attack vector in detail - and in particular whether that attack vector assumes being able to freely execute NumPy functions.

Advice for using NumPy on untrusted data[#](https://numpy.org/doc/stable/reference/security.html#advice-for-using-numpy-on-untrusted-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy should be generally safe to use on _data_ provided by unprivileged users and read through safe API functions (e.g. loaded from a text file or `.npy` file without pickle support). Malicious _values_ or _data sizes_ should never lead to privilege escalation. Note that the above refers to _array data_. We do not currently consider for example `f2py` to be safe: it is typically used to compile a program that is then run. Any `f2py` invocation must thus use the same privilege as the later execution.

The following points may be useful or should be noted when working with untrusted data:

*   Exhausting memory can result in an out-of-memory kill, which is a possible denial of service attack. Possible causes could be:
    
    *   Functions reading text files, which may require much more memory than the original input file size.
        
    *   If users can create arbitrarily shaped arrays, NumPy’s broadcasting means that intermediate or result arrays can be much larger than the inputs.
        
*   NumPy structured dtypes allow for a large amount of complexity. Fortunately, most code fails gracefully when a structured dtype is provided unexpectedly. However, code should either disallow untrusted users to provide these (e.g. via `.npy` files) or carefully check the fields included for nested structured/subarray dtypes.
    
*   Passing on user input should generally be considered unsafe (except for the data being read). An example would be `np.dtype(user_string)` or `dtype=user_string`.
    
*   The speed of operations can depend on values and memory order can lead to larger temporary memory use and slower execution. This means that operations may be significantly slower or use more memory compared to simple test cases.
    
*   When reading data, consider enforcing a specific shape (e.g. one dimensional) or dtype such as `float64`, `float32`, or `int64` to reduce complexity.
    

When working with non-trivial untrusted data, it is advisable to sandbox the analysis to guard against potential privilege escalation. This is especially advisable if further libraries based on NumPy are used since these add additional complexity and potential security issues.

On this page