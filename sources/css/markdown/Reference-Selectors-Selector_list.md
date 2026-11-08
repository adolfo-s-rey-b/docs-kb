*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#mdn-search)
    

Selector list
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The CSS **selector list** (`,`) selects all the matching nodes. A selector list is a comma-separated list of selectors.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#description)

--------------------------------------------------------------------------------------------------------------

When multiple selectors share the same declarations, they can be grouped together into a comma-separated list. Selector lists can also be passed as parameters to some functional CSS pseudo-classes. White space may appear before and/or after the comma.

The following three declarations are equivalent:

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#examples)

--------------------------------------------------------------------------------------------------------

When applying the same styles to elements matching different criteria, grouping the selectors in a comma-separated list can improve consistency while reducing the size of style sheets.

### [Single line grouping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#single_line_grouping)

This example shows grouping selectors in a single line using a comma-separated list.

### [Multi line grouping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#multi_line_grouping)

This example shows grouping selectors in multiple lines using a comma-separated list.

[Valid and invalid selector lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#valid_and_invalid_selector_lists)

--------------------------------------------------------------------------------------------------------------------------------------------------------

An invalid selector represents, and therefore matches, nothing. When a selector list contains an invalid selector, the entire style block is ignored, except for the [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 and [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
 pseudo-classes that accept [forgiving selector lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#forgiving_selector_list)
.

### [Invalid selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#invalid_selector_list)

A downside to using a selector list is that a single unsupported selector in the selector list invalidates the entire rule.

Consider the following two CSS rule sets:

They are not equivalent. In the first rule set, styles will be applied on the `h1` and `h3` elements, but the `h2:invalid-pseudo` rule will not be parsed. In the second rule set, because one selector in the list is invalid, the entire rule will not be parsed. Because of this, no style will be applied to the `h1` and `h3` elements as when any selector in a list of selectors in invalid, the entire style block will be ignored.

### [Forgiving selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#forgiving_selector_list)

A way to remedy the [invalid selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#invalid_selector_list)
 problem is to use the [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 or the [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
 pseudo-class, which accept a forgiving selector list. Each selector in a forgiving selector list is parsed individually. So any invalid selectors in the list are ignored and the valid ones are used.

Carrying on from the previous example, the following two CSS rule sets are now equivalent:

The difference between the two is that the specificity of `:is()` is its most specific argument, whereas the `:where()` selector and the forgiving selector list parameter do not add any specificity weight.

### [Relative selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#relative_selector_list)

A relative selector list is a comma-separated selector list parsed as [relative selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#relative_selector)
, which begin with an explicit or implied combinator.

In the above example, the italic style will be applied to any `h2` heading that is immediately followed by `<p>` or `<ul class="red">`. Note that pseudo-elements and the `:has()` selector are not valid within the [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
 relative selector list.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# grouping](https://drafts.csswg.org/selectors/#grouping) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#see_also)

--------------------------------------------------------------------------------------------------------

*   The [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
     and [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
     pseudo-classes accept forgiving selector lists.
*   The [`:not()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)
     pseudo-class accepts a regular selector list
*   The [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
     pseudo-class accepts a relative selector list.
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [Selectors and combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selectors_and_combinators)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/selector_list/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/selector_list (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FSelector_list&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fselector_list%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FSelector_list%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fselector_list%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")