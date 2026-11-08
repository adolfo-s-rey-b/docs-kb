*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#mdn-search)
    

`overflow-inline` CSS property
==============================

Baseline 2025

Newly available

\*

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what shows when content overflows the inline start and end edges of a box. This may be nothing, a scroll bar, or the overflow content.

**Note:** The `overflow-inline` property maps to [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 or [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 depending on the writing mode of the document.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    overflow-inline: visible;
    overflow-inline: hidden;
    overflow-inline: clip;
    overflow-inline: scroll;
    overflow-inline: auto;
    
    /* Global values */
    overflow-inline: inherit;
    overflow-inline: initial;
    overflow-inline: revert;
    overflow-inline: revert-layer;
    overflow-inline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#values)

This property is specified as one of the following [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
 keyword values:

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#visible)

Content is not clipped and may be rendered outside the padding box's inline start and end edges.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#hidden)

Content is clipped if necessary to fit the inline dimension in the padding box. No scrollbars are provided.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#clip)

Overflow content is clipped at the element's overflow clip edge that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#scroll)

Content is clipped if necessary to fit in the padding box in the inline dimension. Browsers display scrollbars whether or not any content is actually clipped. (This prevents scrollbars from appearing or disappearing when the content changes.) Printers may still print overflowing content.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#auto)

Depends on the user agent. If content fits inside the padding box, it looks the same as `visible`, but still establishes a new block-formatting context. Desktop browsers provide scrollbars if content overflows.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br> or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br> is neither `visible` nor clip |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

overflow-inline =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clip     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#examples)

-----------------------------------------------------------------------------------------------------------

### [Setting inline overflow behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#setting_inline_overflow_behavior)

#### HTML

html

    <ul>
      <li>
        <code>overflow-inline: hidden</code> (hides the text outside the box)
        <div id="div1">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-inline: scroll</code> (always adds a scrollbar)
        <div id="div2">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-inline: visible</code> (displays the text outside the box if
        needed)
        <div id="div3">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-inline: auto</code> (equivalent to <code>scroll</code>
        in most browsers)
        <div id="div4">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-inline: clip</code> (hides the text outside the box beyond
        the overflow clip edge)
        <code>clip</code>
        <div id="div5">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    </ul>
    

#### CSS

css

    div {
      border: 1px solid black;
      width: 250px;
      margin-bottom: 12px;
    }
    
    #div1 {
      overflow-inline: hidden;
    }
    #div2 {
      overflow-inline: scroll;
    }
    #div3 {
      overflow-inline: visible;
    }
    #div4 {
      overflow-inline: auto;
    }
    #div5 {
      overflow-inline: clip;
      overflow-clip-margin: 2em;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# overflow-control](https://drafts.csswg.org/css-overflow/#overflow-control) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    , [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    , [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
    , [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
    , [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    , [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    , [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
    
*   [Learn: Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-inline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")