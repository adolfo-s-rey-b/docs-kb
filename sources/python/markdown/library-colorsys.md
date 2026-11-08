### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/i18n.html "Internationalization")
     |
*   [previous](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Multimedia Services](https://docs.python.org/3/library/mm.html)
     »
*   [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`colorsys` — Conversions between color systems[¶](https://docs.python.org/3/library/colorsys.html#module-colorsys "Link to this heading")

==========================================================================================================================================

**Source code:** [Lib/colorsys.py](https://github.com/python/cpython/tree/3.15/Lib/colorsys.py)

* * *

The `colorsys` module defines bidirectional conversions of color values between colors expressed in the RGB (Red Green Blue) color space used in computer monitors and three other coordinate systems: YIQ, HLS (Hue Lightness Saturation) and HSV (Hue Saturation Value). Coordinates in all of these color spaces are floating-point values. In the YIQ space, the Y coordinate is between 0 and 1, but the I and Q coordinates can be positive or negative. In all other spaces, the coordinates are all between 0 and 1.

See also

More information about color spaces can be found at [https://www.poynton.ca/pdf/ColourFAQ.pdf](https://www.poynton.ca/pdf/ColourFAQ.pdf)
 and [https://www.cambridgeincolour.com/tutorials/color-spaces.htm](https://www.cambridgeincolour.com/tutorials/color-spaces.htm)
.

The `colorsys` module defines the following functions:

colorsys.rgb\_to\_yiq(_r_, _g_, _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_yiq "Link to this definition")

Convert the color from RGB coordinates to YIQ coordinates.

colorsys.yiq\_to\_rgb(_y_, _i_, _q_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.yiq_to_rgb "Link to this definition")

Convert the color from YIQ coordinates to RGB coordinates.

colorsys.rgb\_to\_hls(_r_, _g_, _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_hls "Link to this definition")

Convert the color from RGB coordinates to HLS coordinates.

colorsys.hls\_to\_rgb(_h_, _l_, _s_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.hls_to_rgb "Link to this definition")

Convert the color from HLS coordinates to RGB coordinates.

colorsys.rgb\_to\_hsv(_r_, _g_, _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_hsv "Link to this definition")

Convert the color from RGB coordinates to HSV coordinates.

colorsys.hsv\_to\_rgb(_h_, _s_, _v_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.hsv_to_rgb "Link to this definition")

Convert the color from HSV coordinates to RGB coordinates.

Example:

Copy

\>>> import colorsys
\>>> colorsys.rgb\_to\_hsv(0.2, 0.4, 0.4)
(0.5, 0.5, 0.4)
\>>> colorsys.hsv\_to\_rgb(0.5, 0.5, 0.4)
(0.2, 0.4, 0.4)

#### Previous topic

[`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html "previous chapter")

#### Next topic

[Internationalization](https://docs.python.org/3/library/i18n.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=colorsys+%E2%80%94+Conversions+between+color+systems&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcolorsys.html&pagesource=library%2Fcolorsys.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/colorsys.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/i18n.html "Internationalization")
     |
*   [previous](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Multimedia Services](https://docs.python.org/3/library/mm.html)
     »
*   [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)
    
*    
    
    |
*   Theme Auto Light Dark |