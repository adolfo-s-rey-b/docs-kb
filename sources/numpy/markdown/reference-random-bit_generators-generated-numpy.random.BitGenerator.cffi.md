[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.cffi.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.random.BitGenerator.cffi[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.cffi.html#numpy-random-bitgenerator-cffi "Link to this heading")

====================================================================================================================================================================================================

attribute

random.BitGenerator.cffi[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.cffi.html#numpy.random.BitGenerator.cffi "Link to this definition")

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