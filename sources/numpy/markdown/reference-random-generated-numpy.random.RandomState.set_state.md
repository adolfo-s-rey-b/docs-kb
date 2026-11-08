[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.set_state.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.set_state.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.set_state.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.set\_state[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#numpy-random-randomstate-set-state "Link to this heading")

==================================================================================================================================================================================================

method

random.RandomState.set\_state(_state_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#numpy.random.RandomState.set_state "Link to this definition")

Set the internal state of the generator from a tuple.

For use if one has reason to manually (re-)set the internal state of the bit generator used by the RandomState instance. By default, RandomState uses the “Mersenne Twister”[\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#rd62dfb5ffa26-1)
 pseudo-random number generating algorithm.

Parameters:

**state**{tuple(str, ndarray of 624 uints, int, int, float), dict}

The _state_ tuple has the following items:

1.  the string ‘MT19937’, specifying the Mersenne Twister algorithm.
    
2.  a 1-D array of 624 unsigned integers `keys`.
    
3.  an integer `pos`.
    
4.  an integer `has_gauss`.
    
5.  a float `cached_gaussian`.
    

If state is a dictionary, it is directly set using the BitGenerators _state_ property.

Returns:

**out**None

Returns ‘None’ on success.

See also

[`get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.get_state.html#numpy.random.RandomState.get_state "numpy.random.RandomState.get_state")

Notes

[`set_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#numpy.random.RandomState.set_state "numpy.random.RandomState.set_state")
 and [`get_state`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.get_state.html#numpy.random.RandomState.get_state "numpy.random.RandomState.get_state")
 are not needed to work with any of the random distributions in NumPy. If the internal state is manually altered, the user should know exactly what he/she is doing.

For backwards compatibility, the form (str, array of 624 uints, int) is also accepted although it is missing some information about the cached Gaussian value: `state = ('MT19937', keys, pos)`.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.set_state.html#id1)\
\]

M. Matsumoto and T. Nishimura, “Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator,” _ACM Trans. on Modeling and Computer Simulation_, Vol. 8, No. 1, pp. 3-30, Jan. 1998.

On this page