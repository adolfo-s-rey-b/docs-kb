[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.get_state.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.get_state.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.get_state.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.get_state.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.get_state.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.get_state.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.get_state.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.get_state.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.get_state.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.get_state.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.get_state.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.get_state.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.get_state.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.get_state.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.get_state.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.get_state.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.get_state.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.get_state.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.get_state.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.get_state.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.get\_state[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html#numpy-random-get-state "Link to this heading")

==============================================================================================================================================================

random.get\_state(_legacy\=True_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html#numpy.random.get_state "Link to this definition")

Return a tuple representing the internal state of the generator.

For more details, see [`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.set_state.html#numpy.random.set_state "numpy.random.set_state")
.

Parameters:

**legacy**bool, optional

Flag indicating to return a legacy tuple state when the BitGenerator is MT19937, instead of a dict. Raises ValueError if the underlying bit generator is not an instance of MT19937.

Returns:

**out**{tuple(str, ndarray of 624 uints, int, int, float), dict}

If legacy is True, the returned tuple has the following items:

1.  the string ‘MT19937’.
    
2.  a 1-D array of 624 unsigned integer keys.
    
3.  an integer `pos`.
    
4.  an integer `has_gauss`.
    
5.  a float `cached_gaussian`.
    

If _legacy_ is False, or the BitGenerator is not MT19937, then state is returned as a dictionary.

See also

[`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.set_state.html#numpy.random.set_state "numpy.random.set_state")

Notes

[`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.set_state.html#numpy.random.set_state "numpy.random.set_state")
 and [`get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html#numpy.random.get_state "numpy.random.get_state")
 are not needed to work with any of the random distributions in NumPy. If the internal state is manually altered, the user should know exactly what he/she is doing.

On this page