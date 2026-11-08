*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#mdn-search)
    

`user-select` CSS property
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/59)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`user-select`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls whether the user can select text. This doesn't have any effect on content loaded as part of a browser's user interface (its [chrome](https://developer.mozilla.org/en-US/docs/Glossary/Chrome)
), except in textboxes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#try_it)

---------------------------------------------------------------------------------------------------

    user-select: none;
    

    user-select: text;
    

    user-select: all;
    

    <section id="default-example">
      <p id="example-element">Try to select this text</p>
    </section>
    

    #example-element {
      font-size: 1.5rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    user-select: none;
    user-select: auto;
    user-select: text;
    user-select: all;
    
    /* Global values */
    user-select: inherit;
    user-select: initial;
    user-select: revert;
    user-select: revert-layer;
    user-select: unset;
    

**Note:** `user-select` is not an inherited property, though the initial `auto` value makes it behave like it is inherited most of the time. WebKit/Chromium-based browsers _do_ implement the property as inherited, which violates the behavior described in the spec, and this will bring some issues. Until now, Chromium has chosen to [fix the issues](https://chromium.googlesource.com/chromium/src/+/b01af0b296ecb855aac95c4ed335d188e6eac2de "External link (opens in new tab)")
 to make the final behavior meet the specifications.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#none)

The text of the element and its sub-elements is not selectable. Note that the [`Selection`](https://developer.mozilla.org/en-US/docs/Web/API/Selection)
 object can contain these elements.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#auto)

The used value of `auto` is determined as follows:

*   On the `::before` and `::after` pseudo elements, the used value is `none`
*   If the used value of `user-select` on the parent of this element is `none`, the used value is `none`
*   Otherwise, if the used value of `user-select` on the parent of this element is `all`, the used value is `all`
*   Otherwise, the used value is `text`

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#text)

The text can be selected by the user.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#all)

The content of the element shall be selected atomically: If a selection would contain part of the element, then the selection must contain the entire element including all its descendants. If a double-click or context-click occurred in sub-elements, the highest ancestor with this value will be selected.

**Note:** The [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
 module defines a `contain` value for the `user-select` property to enable selection to start within the element to be contained by the bounds of that element, however, this is not supported in any browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

user-select =   
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  text     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#examples)

-------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#html)

html

    <p>You should be able to select this text.</p>
    <p class="unselectable">Hey, you can't select this text!</p>
    <p class="all">Clicking once will select all of this text.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#css)

css

    .unselectable {
      -webkit-user-select: none; /* Safari */
      user-select: none;
    }
    
    .all {
      -webkit-user-select: all;
      user-select: all;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# content-selection](https://drafts.csswg.org/css-ui/#content-selection) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select#see_also)

-------------------------------------------------------------------------------------------------------

*   [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
     pseudo-element
*   The JavaScript [`Selection`](https://developer.mozilla.org/en-US/docs/Web/API/Selection)
     object

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/user-select/index.md?plain=1 "Folder: en-us/web/css/reference/properties/user-select (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fuser-select&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fuser-select%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fuser-select%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fuser-select%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")