*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#mdn-search)
    

`inset-inline-start` CSS property
=================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inset-inline-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the logical inline start inset of an element, which maps to a physical offset depending on the element's writing mode, directionality, and text orientation. It corresponds to the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
, or [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 property depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

This [inset property](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 has no effect on non-positioned elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#try_it)

----------------------------------------------------------------------------------------------------------

    writing-mode: horizontal-tb;
    

    writing-mode: vertical-rl;
    

    writing-mode: horizontal-tb;
    direction: rtl;
    

    writing-mode: vertical-lr;
    

    <section id="default-example">
      <div class="example-container" id="example-element">
        <div id="abspos">
          I am absolutely positioned with inset-inline-start: 50px
        </div>
        <p>
          As much mud in the streets as if the waters had but newly retired from the
          face of the earth, and it would not be wonderful to meet a Megalosaurus,
          forty feet long or so, waddling like an elephantine lizard up Holborn
          Hill.
        </p>
      </div>
    </section>
    

    #example-element {
      border: 0.75em solid;
      padding: 0.75em;
      position: relative;
      width: 100%;
      min-height: 200px;
      unicode-bidi: bidi-override;
    }
    
    #abspos {
      background-color: yellow;
      color: black;
      border: 3px solid red;
      position: absolute;
      inset-inline-start: 50px;
      inline-size: 140px;
      min-block-size: 80px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    inset-inline-start: 3px;
    inset-inline-start: 2.4em;
    inset-inline-start: calc(anchor(--my-anchor 50%) + 10px);
    inset-inline-start: anchor-size(width);
    
    /* <percentage>s of the width or height of the containing block */
    inset-inline-start: 10%;
    
    /* Keyword value */
    inset-inline-start: auto;
    
    /* Global values */
    inset-inline-start: inherit;
    inset-inline-start: initial;
    inset-inline-start: revert;
    inset-inline-start: revert-layer;
    inset-inline-start: unset;
    

The shorthand for `inset-inline-start` and [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
 is [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#values)

The `inset-inline-start` property takes the same values as the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | logical-width of containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | same as box offsets: [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)<br>, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)<br>, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)<br>, [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)<br> properties except that directions are logical |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

inset-inline-start =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#examples)

--------------------------------------------------------------------------------------------------------------

### [Setting inline start offset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#setting_inline_start_offset)

#### HTML

html

    <div>
      <p class="exampleText">Example text</p>
    </div>
    

#### CSS

css

    div {
      background-color: yellow;
      width: 120px;
      height: 120px;
    }
    
    .exampleText {
      writing-mode: vertical-lr;
      position: relative;
      inset-inline-start: 20px;
      background-color: #c8c800;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# propdef-inset-inline-start](https://drafts.csswg.org/css-logical/#propdef-inset-inline-start) |
| [CSS Positioned Layout Module Level 3  <br>\# propdef-inset-inline-start](https://drafts.csswg.org/css-position/#propdef-inset-inline-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start#see_also)

--------------------------------------------------------------------------------------------------------------

*   The properties which defines other insets: [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
    , [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
    , and [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
    
*   The mapped physical properties: [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    , [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    , [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    , and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/inset-inline-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/inset-inline-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finset-inline-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finset-inline-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finset-inline-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finset-inline-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")