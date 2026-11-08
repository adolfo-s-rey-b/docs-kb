*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#mdn-search)
    

`overflow-y` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-y`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what shows when content overflows a block-level element's top and bottom edges. This may be nothing, a scroll bar, or the overflow content. This property may also be set by using the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 shorthand property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#try_it)

--------------------------------------------------------------------------------------------------

    overflow-y: visible;
    

    overflow-y: hidden;
    

    overflow-y: clip;
    

    overflow-y: scroll;
    

    overflow-y: auto;
    

    <section class="default-example" id="default-example">
      <p id="example-element">
        Michaelmas term lately over, and the Lord Chancellor sitting in Lincoln's
        Inn Hall. Implacable November weather. As much mud in the streets as if the
        waters had but newly retired from the face of the earth.
      </p>
    </section>
    

    #example-element {
      width: 15em;
      height: 9em;
      border: medium dotted;
      padding: 0.75em;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    overflow-y: visible;
    overflow-y: hidden;
    overflow-y: clip;
    overflow-y: scroll;
    overflow-y: auto;
    
    /* Global values */
    overflow-y: inherit;
    overflow-y: initial;
    overflow-y: revert;
    overflow-y: revert-layer;
    overflow-y: unset;
    

The `overflow-y` property is specified as a single [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
 keyword value.

If [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 is `hidden`, `scroll`, or `auto` and the `overflow-y` property is `visible` (default), the value will be implicitly computed as `auto`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#values)

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#visible)

Overflow content is not clipped and may be visible outside the element's padding box at the top and bottom edges. The element box is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#hidden)

Overflow content is clipped if necessary to fit vertically in the elements' padding box. No scroll bars are provided.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#clip)

Overflow content is clipped at the element's _overflow clip edge_ that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property. As a result, content overflows the element's padding box by the [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value of `overflow-clip-margin` or by `0px` if not set. The difference between `clip` and `hidden` is that the `clip` keyword also forbids all scrolling, including programmatic scrolling. No new formatting context is created. To establish a formatting context, use `overflow: clip` along with [`display: flow-root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#flow-root)
. The element box is not a scroll container.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#scroll)

Overflow content is clipped if necessary to fit vertically inside the element's padding box. Browsers display scroll bars in the vertical direction whether or not any content is actually clipped. (This prevents scroll bars from appearing or disappearing when the content changes.) Printers may still print overflowing content.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#auto)

Overflow content is clipped at the element's padding box, and overflow content can be scrolled into view. Unlike `scroll`, user agents display scroll bars _only if_ the content is overflowing, hiding scroll bars by default. If content fits inside the element's padding box, it looks the same as with `visible`, but still establishes a new block-formatting context.

**Note:** The keyword value `overlay` is a legacy value alias for `auto`. With `overlay`, the scroll bars are drawn on top of the content instead of taking up space.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br> or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br> is neither `visible` nor clip |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#formal_syntax)

----------------------------------------------------------------------------------------------------------------

overflow-y =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clip     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#examples)

------------------------------------------------------------------------------------------------------

### [Setting overflow-y behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#setting_overflow-y_behavior)

#### HTML

html

    <ul>
      <li>
        <code>overflow-y:hidden</code> — hides the text outside the box
        <div id="div1">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-y:scroll</code> — always adds a scrollbar
        <div id="div2">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-y:visible</code> — displays the text outside the box if
        needed
        <div id="div3">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    
      <li>
        <code>overflow-y:auto</code> — equivalent to <code>scroll</code>
        on most browsers
        <div id="div4">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur.
        </div>
      </li>
    </ul>
    

#### CSS

css

    div {
      border: 1px solid black;
      width: 250px;
      height: 100px;
    }
    
    #div1 {
      overflow-y: hidden;
      margin-bottom: 12px;
    }
    #div2 {
      overflow-y: scroll;
      margin-bottom: 12px;
    }
    #div3 {
      overflow-y: visible;
      margin-bottom: 120px;
    }
    #div4 {
      overflow-y: auto;
      margin-bottom: 120px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# overflow-properties](https://drafts.csswg.org/css-overflow/#overflow-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y#see_also)

------------------------------------------------------------------------------------------------------

*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    , [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [Learn: Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-y/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-y (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-y&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-y%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-y%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-y%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")