*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#mdn-search)
    

`@counter-style` CSS at-rule
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@counter-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 lets you extend predefined list styles and define your own counter styles that are not part of the predefined set of styles. The `@counter-style` rule contains [descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#descriptors)
 defining how the counter value is converted into a string representation.

While CSS provides many useful predefined counter styles, the `@counter-style` at-rule offers an open-ended method for creating counters. This at-rule caters to the needs of worldwide typography by allowing authors to define their own counter styles when the predefined styles don't fit their requirements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#syntax)

----------------------------------------------------------------------------------------------------

The `@counter-style` at-rule is identified by a [counter style name](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter_style_name)
, and the style of the named counter can be fine-tuned using a `<declaration-list>` consisting of one or more [descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#descriptors)
 and their values.

### [Counter style name](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter_style_name)

[`<counter-style-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter-style-name)

Provides a name for your counter style. It is specified as a case-sensitive [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 without quotes. The value should not be equal to `none`. Like all custom identifiers, the value of your counter style can't be a [CSS-wide keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)
. Avoid other enumerated CSS property values, including values of [list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#properties)
 and [counter style](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles#properties)
 properties. The name of your counter can't be the case-insensitive [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property values of `decimal`, `disc`, `square`, `circle`, `disclosure-open`, and `disclosure-closed`.

**Note:** The non-overridable counter style names `decimal`, `disc`, `square`, `circle`, `disclosure-open`, and `disclosure-closed` cannot be used as the name of a custom counter. However, they are valid in other contexts where the `<counter-style-name>` data type is expected, such as in `system: extends <counter-style-name>`.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#descriptors)

[`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)

Specifies the algorithm to be used for converting the integer value of a counter to a string representation. If the value is `cyclic`, `numeric`, `alphabetic`, `symbolic`, or `fixed`, the `symbols` descriptor must also be specified. If the value is `additive`, the `additive-symbols` descriptor must also be specified.

[`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)

Specifies the symbols that are to be used for the marker representations. Symbols can contain strings, images, or custom identifiers. This descriptor is required if the `system` descriptor is set to `cyclic`, `numeric`, `alphabetic`, `symbolic`, or `fixed`.

[`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)

Defines the _additive tuples_ for additive systems. While the symbols specified in the `symbols` descriptor are used for constructing marker representation by most algorithms, additive counter systems, such as Roman numerals, consist of a series of weighted symbols. The descriptors is a list of counter symbol along with their non-negative integer weights, listed by weight in descending order. This descriptor is required if the `system` descriptor is set to `additive`.

[`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)

Specifies to symbols to be appended or prepended to the counter representation if the value is negative.

[`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)

Specifies a symbol that should be prepended to the marker representation. Prefixes are added to the representation in the final stage, before any characters added to negative counter values by the `negative` descriptor.

[`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)

Specifies, similar to the prefix descriptor, a symbol that is appended to the marker representation. Suffixes come after the marker representation, including after any characters added to negative counter values by the `negative` descriptor.

[`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)

Defines the range of values over which the counter style is applicable. If a counter style is used to represent a counter value outside of the ranges defined by this descriptor, the counter style will drop back to its `fallback` style.

[`pad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)

Is used when you need the marker representations to be of a minimum length. For example if you want the counters to start at 01 and go through 02, 03, 04, etc., then the `pad` descriptor is to be used. For representations larger than the specified `pad` value, the marker is constructed as normal.

[`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)

Describes how speech synthesizers, such as screen readers, should announce the counter style. For example, the value of the list item marker can be read out as numbers or alphabets for ordered lists or as audio cues for unordered lists, based on the value of this descriptor.

[`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)

Specifies the counter name of the system to fall back to if either the specified system is unable to construct the representation of a counter value or if the counter value is outside the specified `range`. If the fallback counter also fails to represent the value, then that counter's fallback is used, if one is specified. If there are either no fallback counters described or if the chain of fallback systems are unable to represent a counter value, then it will ultimately fall back to the `decimal` style.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#formal_syntax)

------------------------------------------------------------------------------------------------------------------

@counter-style =   
  @counter-style <counter-style-name> { <declaration-list> }    
  
<counter-style-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#examples)

--------------------------------------------------------------------------------------------------------

### [Specifying symbols with counter-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#specifying_symbols_with_counter-style)

The above counter style rule can be applied to lists like this:

The above code produces the following result:

See more examples on the [demo page](https://mdn.github.io/css-examples/counter-style-demo/ "External link (opens in new tab)")
 ([code](https://github.com/mdn/css-examples/tree/main/counter-style-demo "External link (opens in new tab)")
).

### [Ready-made counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#ready-made_counter_styles)

Find a collection of over 100 `counter-style` code snippets in the [Ready-made Counter Styles](https://w3c.github.io/predefined-counter-styles/ "External link (opens in new tab)")
 document. This document provides counters that meet the needs of languages and cultures around the world.

The [Counter styles converter](https://r12a.github.io/app-counters/ "External link (opens in new tab)")
 pulls from this list to test and create copy and paste code for counter styles.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3  <br>\# the-counter-style-rule](https://drafts.csswg.org/css-counter-styles/#the-counter-style-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#see_also)

--------------------------------------------------------------------------------------------------------

*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    
*   [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    , [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
    
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@counter-style/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@counter-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")