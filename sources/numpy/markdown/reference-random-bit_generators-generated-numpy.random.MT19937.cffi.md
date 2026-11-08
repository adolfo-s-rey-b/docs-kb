[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.MT19937.cffi[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html#numpy-random-mt19937-cffi "Link to this heading")

=====================================================================================================================================================================================

attribute

random.MT19937.cffi[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.MT19937.cffi.html#numpy.random.MT19937.cffi "Link to this definition")

CFFI interface

Returns:

**interface**namedtuple

Named tuple containing CFFI wrapper

*   state\_address - Memory address of the state struct
    
*   state - pointer to the state struct
    
*   next\_uint64 - function pointer to produce 64 bit integers
    
*   next\_uint32 - function pointer to produce 32 bit integers
    
*   next\_double - function pointer to produce doubles
    
*   bitgen - pointer to the bit generator struct
    

On this page