### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests")
     |
*   [previous](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files")
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
*   [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Cryptographic Services[¶](https://docs.python.org/3/library/crypto.html#cryptographic-services "Link to this heading")

=======================================================================================================================

The modules described in this chapter implement various algorithms of a cryptographic nature. They are available at the discretion of the installation. Here’s an overview:

*   [`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
    *   [Hash algorithms](https://docs.python.org/3/library/hashlib.html#hash-algorithms)
        
    *   [Usage](https://docs.python.org/3/library/hashlib.html#usage)
        
    *   [Constructors](https://docs.python.org/3/library/hashlib.html#constructors)
        
    *   [Attributes](https://docs.python.org/3/library/hashlib.html#attributes)
        
    *   [Hash Objects](https://docs.python.org/3/library/hashlib.html#hash-objects)
        
    *   [SHAKE variable length digests](https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests)
        
    *   [File hashing](https://docs.python.org/3/library/hashlib.html#file-hashing)
        
    *   [Key derivation](https://docs.python.org/3/library/hashlib.html#key-derivation)
        
    *   [BLAKE2](https://docs.python.org/3/library/hashlib.html#blake2)
        *   [Creating hash objects](https://docs.python.org/3/library/hashlib.html#creating-hash-objects)
            
        *   [Constants](https://docs.python.org/3/library/hashlib.html#constants)
            
        *   [Examples](https://docs.python.org/3/library/hashlib.html#examples)
            *   [Simple hashing](https://docs.python.org/3/library/hashlib.html#simple-hashing)
                
            *   [Using different digest sizes](https://docs.python.org/3/library/hashlib.html#using-different-digest-sizes)
                
            *   [Keyed hashing](https://docs.python.org/3/library/hashlib.html#keyed-hashing)
                
            *   [Randomized hashing](https://docs.python.org/3/library/hashlib.html#randomized-hashing)
                
            *   [Personalization](https://docs.python.org/3/library/hashlib.html#personalization)
                
            *   [Tree mode](https://docs.python.org/3/library/hashlib.html#tree-mode)
                
        *   [Credits](https://docs.python.org/3/library/hashlib.html#credits)
            
*   [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
    
*   [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)
    *   [Random numbers](https://docs.python.org/3/library/secrets.html#random-numbers)
        
    *   [Generating tokens](https://docs.python.org/3/library/secrets.html#generating-tokens)
        *   [How many bytes should tokens use?](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use)
            
    *   [Other functions](https://docs.python.org/3/library/secrets.html#other-functions)
        
    *   [Recipes and best practices](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices)
        

#### Previous topic

[`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html "previous chapter")

#### Next topic

[`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Cryptographic+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcrypto.html&pagesource=library%2Fcrypto.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/crypto.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests")
     |
*   [previous](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files")
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
*   [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
    
*    
    
    |
*   Theme Auto Light Dark |