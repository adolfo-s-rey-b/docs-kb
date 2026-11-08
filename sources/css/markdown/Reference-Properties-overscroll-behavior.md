*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#mdn-search)
    

`overscroll-behavior` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/567)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overscroll-behavior`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls what happens when scrolling reaches the edge of a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#try_it)

-----------------------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`overscroll-behavior-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-x)
    
*   [`overscroll-behavior-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#syntax)

-----------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#values)

The `overscroll-behavior` property is specified as one or two keywords chosen from the list of values below.

Two keywords specifies the `overscroll-behavior` value on the `x` and `y` axes respectively. If only one value is specified, both x and y are assumed to have the same value.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#auto)

Allows the default behavior at a scroll boundary. Scrolling may continue in another scroll container.

[`chain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#chain)

Allows scrolling to continue outside the scroll container, but prevents overscroll "bounce" effects.

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#contain)

Prevents scrolling from continuing outside the scroll container. "Bounce" effects may still occur.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#none)

Prevents scrolling from continuing outside the scroll container and also prevents overscroll "bounce" effects.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#description)

---------------------------------------------------------------------------------------------------------------------

By default, mobile browsers tend to provide a "bounce" effect or even a page refresh when the top or bottom of a page (or other scroll area) is reached. You may also have noticed that when you have a dialog box with scrolling content at the top of a page that also has scrolling content, once the dialog box's [scroll boundary](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_boundary)
 is reached, the underlying page will then start to scroll — this is called [scroll chaining](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_chaining)
.

In some cases, these behaviors are not desirable. You can use `overscroll-behavior` to get rid of unwanted scroll chaining and the browser's "pull to refresh"-type behavior.

Note that this property applies only to [scroll containers](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. In particular, since an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 is not a scroll container, setting this property on an iframe has no effect. To control scroll chaining from an iframe, set `overscroll-behavior` on both the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 and the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 elements of the iframe's document.

A [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 that has no scrollable overflow, such as an element with `overflow: hidden`, is always considered to be at its [scroll boundary](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_boundary)
. So setting a non-default `overscroll-behavior` such as `contain` or `none` on it will prevent scroll chaining to ancestor scroll containers. This can be used to prevent background scrolling while a dialog or overlay is open.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | non-replaced block-level elements and non-replaced inline-block elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`overscroll-behavior-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-x)<br>    : as specified<br>*   [`overscroll-behavior-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

overscroll-behavior =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 contain [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 chain [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#examples)

---------------------------------------------------------------------------------------------------------------

### [`overscroll-behavior` on `<dialog>` elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#overscroll-behavior_on_dialog_elements)

In this example there are 4 buttons that launch a dialog, each dialog has a different `overscroll-behavior` value. There is also a `<div>` that forces the content to be larger than the container so that the scroll effect of the page can be seen.

#### HTML

#### CSS

#### Result

Click one of the buttons to see that behavior applied to the dialog that appears, when you scroll within the dialog:

*   `auto`: if you overscroll the dialog you will see the content "bounce" and if you then continue to scroll you will see the background scroll too.
*   `contain`: if you overscroll the dialog you will see the content "bounce" and if you then continue to scroll you will see the background does not scroll.
*   `chain`: if you overscroll the dialog you will see that the content does not "bounce" and if you then continue to scroll you will see the background scroll too.
*   `none`: if you overscroll the dialog you will see that the content does not "bounce" and if you then continue to scroll you will see the background does not scroll.

An alternate example of controlling scroll of "chat" window can be seen on the [`overscroll-behavior-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y#preventing_an_underlying_element_from_scrolling)
 property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overscroll Behavior Module Level 1  <br>\# overscroll-behavior-properties](https://drafts.csswg.org/css-overscroll/#overscroll-behavior-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior#see_also)

---------------------------------------------------------------------------------------------------------------

*   [CSS overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overscroll_behavior)
     module
*   [CSS scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring)
     module
*   [Take control of your scroll: customizing pull-to-refresh and overflow effects](https://developer.chrome.com/blog/overscroll-behavior "External link (opens in new tab)")
     on developer.chrome.com (2017)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 13, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overscroll-behavior/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overscroll-behavior (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverscroll-behavior&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverscroll-behavior%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverscroll-behavior%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverscroll-behavior%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F151d527b2d48812d732cb4f3fdffa0737682e684%0A*+Document+last+modified%3A+2026-10-13T13%3A35%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")