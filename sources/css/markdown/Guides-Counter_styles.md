*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#mdn-search)
    

CSS counter styles
==================

The **CSS counter styles** module lets you define your own counter styles to manage the appearance of [markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 in lists and counters in [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
. It also enables you to extend native browser list styles with your own customizations.

While we think of counters as numbers, they are actually strings with components that can be incremented. The counter styles module defines the `@counter-style` rule with ten descriptors, which enable developers to precisely define how counters are converted into strings. This module enables defining which characters to use for the counter bullets, the prefix to put before the counter and postfix that comes after, along with how to handle negative values. The descriptors can also set a range to limit the values a counter style can handle, while also providing fallback styles for when the counter value falls outside the defined range or otherwise can't render the counter value. The module also enables defining how the counter is read out loud by speech synthesizers.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#reference)

----------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#properties)

No properties are defined in this module

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#functions)

*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#data_types)

*   [`<counter-style-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter-style-name)
    
*   [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols#values)
    
*   [`<symbols-type>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols#syntax)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#at-rules_and_descriptors)

*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
    *   [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
        
    *   [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
        
    *   [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
        
    *   [`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
        
    *   [`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
        
    *   [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
        
    *   [`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
        
    *   [`pad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
        
    *   [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
        
    *   [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
        

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#interfaces)

*   [`CSSCounterStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSCounterStyleRule)
     interface

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#guides)

----------------------------------------------------------------------------------------

[Using CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)

Describes how to use counters to number any HTML element or to perform complex counting.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#related_concepts)

------------------------------------------------------------------------------------------------------------

[CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
 module:

*   [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
     property
*   [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
     property
*   [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
     property
*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
     property
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     shorthand property
*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
     function
*   [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
     function

[CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
 module:

*   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
     pseudo-element
*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
     pseudo-element
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
     pseudo-element

[CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
 module:

*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
     property

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3](https://drafts.csswg.org/css-counter-styles/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#see_also)

--------------------------------------------------------------------------------------------

*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
     module
*   [Ready-made counter styles](https://w3c.github.io/predefined-counter-styles/#builtins "External link (opens in new tab)")
     via W3C (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/counter_styles/index.md?plain=1 "Folder: en-us/web/css/guides/counter_styles (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCounter_styles&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcounter_styles%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCounter_styles%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcounter_styles%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")