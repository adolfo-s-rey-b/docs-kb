*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#mdn-search)
    

`scrollbar-width` CSS property
==============================

Baseline 2024

Newly available

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scrollbar-width`** property allows the author to set the desired thickness of an element's scrollbars when they are shown.

The purpose of the `scrollbar-width` is to optimize the space occupied by the scrollbar on a page or element; the purpose is not related to scrollbar aesthetics. The `scrollbar-width` predefined keyword values indicate to the user agent whether a normal or smaller scrollbar should be rendered. Avoid using `none`, as hiding a scrollbar negatively impacts [accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#accessibility)
.

**Note:** For elements that are scrollable only via programmatic means and not by direct user interaction, use the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property with a value of `hidden` rather than `scrollbar-width: none`.

**Note:** Browsers ignore the non-standard [`::-webkit-scrollbar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar)
 family of pseudo-elements on any element whose _computed_ `scrollbar-width` value is anything other than `auto`. Unlike [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
, `scrollbar-width` is not inherited, so an ancestor's value doesn't affect its descendants. Setting `scrollbar-width: auto` on an element restores its `::-webkit-scrollbar-*` styling. See [Adding a fallback for scrollbar styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#adding_a_fallback_for_scrollbar_styles)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#syntax)

-------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#auto)

The default scrollbar width for the platform.

[`thin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#thin)

A thin scrollbar width variant on platforms that provide that option, or a thinner scrollbar than the default platform scrollbar width.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#none)

No scrollbar shown, however the element will still be scrollable.

**Note:** User Agents must apply any `scrollbar-width` value set on the root element to the viewport.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#accessibility)

---------------------------------------------------------------------------------------------------------------------

Use this property with caution — setting `scrollbar-width` to `thin` or `none` can make content hard or impossible to scroll if the author does not provide an alternative scrolling mechanism. While swiping gestures or mouse wheels can enable scrolling on such content, some devices have no scroll alternative.

WCAG criterion 2.1.1 (Keyboard) has been in place for a long time to advise on basic keyboard accessibility, and this should include scrolling of content areas. And introduced in WCAG 2.1, criterion 2.5.5 (Target Size) advises that touch targets should be at least 44px in width and height (although the problem is compounded on high-resolution screens; thorough testing is advised).

*   [MDN Understanding WCAG, Guideline 2.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.1_%E2%80%94_keyboard_accessible_make_all_functionality_available_from_a_keyboard)
    
*   [MDN Understanding WCAG, Guideline 2.5 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.5_input_modalities_make_it_easier_for_users_to_operate_functionality_through_various_inputs_beyond_keyboard)
    
*   [Understanding Success Criterion 2.1.1 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/keyboard "External link (opens in new tab)")
    
*   [Understanding Success Criterion 2.5.5 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | scrolling boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

scrollbar-width =   
  auto  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#examples)

-----------------------------------------------------------------------------------------------------------

### [Sizing overflow scrollbars](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#sizing_overflow_scrollbars)

#### CSS

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scrollbars Styling Module Level 1  <br>\# scrollbar-width](https://drafts.csswg.org/css-scrollbars/#scrollbar-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width#see_also)

-----------------------------------------------------------------------------------------------------------

*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scrollbars styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`scrollbar-gutter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
    
*   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scrollbar-width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scrollbar-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e2dfb27a085911dd64aa4798d4a1071660c2397%0A*+Document+last+modified%3A+2026-08-26T06%3A42%3A20.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")