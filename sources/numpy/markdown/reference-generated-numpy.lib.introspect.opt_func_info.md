[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.introspect.opt_func_info.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.introspect.opt_func_info.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.introspect.opt_func_info.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.introspect.opt_func_info.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.introspect.opt\_func\_info[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.introspect.opt_func_info.html#numpy-lib-introspect-opt-func-info "Link to this heading")

============================================================================================================================================================================================

lib.introspect.opt\_func\_info(_func\_name\=None_, _signature\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/introspect.py#L8-L94)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.introspect.opt_func_info.html#numpy.lib.introspect.opt_func_info "Link to this definition")

Returns a dictionary containing the currently supported CPU dispatched features for all optimized functions.

Parameters:

**func\_name**str (optional)

Regular expression to filter by function name.

**signature**str (optional)

Regular expression to filter by data type.

Returns:

dict

A dictionary where keys are optimized function names and values are nested dictionaries indicating supported targets based on data types.

Examples

Try it in your browser!

Retrieve dispatch information for functions named ‘add’ or ‘sub’ and data types ‘float64’ or ‘float32’:

\>>> import numpy as np
\>>> dict \= np.lib.introspect.opt\_func\_info(
...     func\_name\="add|abs", signature\="float64|complex64"
... )
\>>> import json
\>>> print(json.dumps(dict, indent\=2))   \# may vary (architecture)
    {
      "absolute": {
        "dd": {
          "current": "SSE41",
          "available": "SSE41 baseline(SSE SSE2 SSE3)"
        },
        "Ff": {
          "current": "FMA3\_\_AVX2",
          "available": "AVX512F FMA3\_\_AVX2 baseline(SSE SSE2 SSE3)"
        },
        "Dd": {
          "current": "FMA3\_\_AVX2",
          "available": "AVX512F FMA3\_\_AVX2 baseline(SSE SSE2 SSE3)"
        }
      },
      "add": {
        "ddd": {
          "current": "FMA3\_\_AVX2",
          "available": "FMA3\_\_AVX2 baseline(SSE SSE2 SSE3)"
        },
        "FFF": {
          "current": "FMA3\_\_AVX2",
          "available": "FMA3\_\_AVX2 baseline(SSE SSE2 SSE3)"
        }
      }
    }

Copy to clipboard

Go BackOpen In Tab

On this page