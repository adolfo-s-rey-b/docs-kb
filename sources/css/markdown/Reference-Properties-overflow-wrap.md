*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#mdn-search)
    

`overflow-wrap` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-wrap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property applies to text, setting whether the browser should insert line breaks within an otherwise unbreakable string to prevent text from overflowing its line box.

**Note:** The property was originally a nonstandard and unprefixed Microsoft extension called `word-wrap`, and was implemented by most browsers with the same name. It has since been renamed to `overflow-wrap`, with `word-wrap` being an alias.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#try_it)

-----------------------------------------------------------------------------------------------------

**Note:** In contrast to [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
, `overflow-wrap` will only create a break if an entire word cannot be placed on its own line without overflowing.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#syntax)

-----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#normal)

Lines may only break at normal word break points (such as a space between two words).

[`anywhere`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#anywhere)

To prevent overflow, an otherwise unbreakable string of characters — like a long word or URL — may be broken at any point if there are no otherwise-acceptable break points in the line. No hyphenation character is inserted at the break point. Soft wrap opportunities introduced by the word break are considered when calculating min-content intrinsic sizes.

[`break-word`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#break-word)

The same as the `anywhere` value, with normally unbreakable words allowed to be broken at arbitrary points if there are no otherwise acceptable break points in the line, but soft wrap opportunities introduced by the word break are NOT considered when calculating min-content intrinsic sizes.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | text elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

overflow-wrap =   
  normal      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  break-word  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  anywhere      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#examples)

---------------------------------------------------------------------------------------------------------

### [Comparing overflow-wrap, word-break, and hyphens](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#comparing_overflow-wrap_word-break_and_hyphens)

This example compares the results of `overflow-wrap`, `word-break`, and `hyphens` when breaking up a long word.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# overflow-wrap-property](https://drafts.csswg.org/css-text/#overflow-wrap-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap#see_also)

---------------------------------------------------------------------------------------------------------

*   [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    
*   [Guide to wrapping and breaking text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-wrap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-wrap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-wrap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-wrap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-wrap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-wrap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")