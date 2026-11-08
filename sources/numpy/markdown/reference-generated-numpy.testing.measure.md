[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.measure.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.measure.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.measure.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.measure.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.measure.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.measure.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.measure.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.measure.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.measure.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.measure.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.measure.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.measure.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.measure.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.measure.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.measure.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.measure.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.measure.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.measure.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.measure.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.measure.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.measure.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.measure.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.measure[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.measure.html#numpy-testing-measure "Link to this heading")

===================================================================================================================================================

testing.measure(_code\_str_, _times\=1_, _label\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1599-L1642)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.measure.html#numpy.testing.measure "Link to this definition")

Return elapsed time for executing code in the namespace of the caller.

The supplied code string is compiled with the Python builtin `compile`. The precision of the timing is 10 milli-seconds. If the code will execute fast on this timescale, it can be executed many times to get reasonable timing accuracy.

Parameters:

**code\_str**str

The code to be timed.

**times**int, optional

The number of times the code is executed. Default is 1. The code is only compiled once.

**label**str, optional

A label to identify _code\_str_ with. This is passed into `compile` as the second argument (for run-time error messages).

Returns:

**elapsed**float

Total elapsed time in seconds for executing _code\_str_ _times_ times.

Examples

Try it in your browser!

\>>> times \= 10
\>>> etime \= np.testing.measure('for i in range(1000): np.sqrt(i\*\*2)', times\=times)
\>>> print("Time for a single execution : ", etime / times, "s")  
Time for a single execution :  0.005 s

Copy to clipboard

Go BackOpen In Tab

On this page