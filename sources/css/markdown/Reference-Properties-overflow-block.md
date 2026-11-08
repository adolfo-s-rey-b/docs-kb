*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#mdn-search)
    

`overflow-block` CSS property
=============================

Baseline 2025

Newly available

\*

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-block`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what shows when content overflows the block start and block end edges of a box. This may be nothing, a scroll bar, or the overflow content.

**Note:** The `overflow-block` property maps to [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 or [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 depending on the writing mode of the document.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    overflow-block: visible;
    overflow-block: hidden;
    overflow-block: clip;
    overflow-block: scroll;
    overflow-block: auto;
    
    /* Global values */
    overflow-block: inherit;
    overflow-block: initial;
    overflow-block: revert;
    overflow-block: revert-layer;
    overflow-block: unset;
    

The `overflow-block` property is specified as a single [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
 keyword value:

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#values)

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#visible)

Content is not clipped and may be rendered outside the padding box's block start and block end edges.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#hidden)

Content is clipped if necessary to fit the block dimension in the padding box. No scrollbars are provided.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#clip)

Overflow content is clipped at the element's overflow clip edge that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#scroll)

Content is clipped if necessary to fit in the block dimension in the padding box. Browsers display scrollbars whether or not any content is actually clipped. (This prevents scrollbars from appearing or disappearing when the content changes.) Printers may still print overflowing content.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#auto)

Depends on the user agent. If content fits inside the padding box, it looks the same as `visible`, but still establishes a new block-formatting context.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br> or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br> is neither `visible` nor clip |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

overflow-block =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clip     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#examples)

----------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#html)

html

    <ul>
      <li>
        <code>overflow-block: hidden</code> (hides the text outside the box)
        <div id="hidden">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-block: scroll</code> (always adds a scrollbar)
        <div id="scroll">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-block: clip</code> (hides the text outside the box beyond the
        overflow clip edge)
        <div id="clip">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-block: visible</code> (displays the text outside the box if
        needed)
        <div id="visible">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-block: auto</code> (on most browsers, equivalent to
        <code>scroll</code>)
        <div id="auto">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    </ul>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#css)

css

    div {
      border: 1px solid black;
      width: 250px;
      height: 100px;
      margin-bottom: 120px;
    }
    
    #hidden {
      overflow-block: hidden;
    }
    #scroll {
      overflow-block: scroll;
    }
    #clip {
      overflow-block: clip;
    }
    #visible {
      overflow-block: visible;
    }
    #auto {
      overflow-block: auto;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# overflow-control](https://drafts.csswg.org/css-overflow/#overflow-control) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block#see_also)

----------------------------------------------------------------------------------------------------------

*   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    , [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    , [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    , [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    , [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    , [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    , [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scrollbars style](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
    
*   [Learn: Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-block/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-block (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-block&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-block%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-block%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-block%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")