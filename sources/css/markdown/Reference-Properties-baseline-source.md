*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#mdn-search)
    

`baseline-source` CSS property
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/192)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`baseline-source`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines which [baseline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
 to use when inline-level boxes have multiple possible baselines, such as multi-line [inline blocks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout)
 or inline [flex containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts#the_flex_container)
. The values allow for choosing between aligning to the box's first baseline, last baseline, or letting the browser decide automatically based on the box type.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    baseline-source: auto;
    baseline-source: first;
    baseline-source: last;
    
    /* Global values */
    baseline-source: inherit;
    baseline-source: initial;
    baseline-source: revert;
    baseline-source: revert-layer;
    baseline-source: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#auto)

Specifies [`last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#last_baseline)
 alignment for inline-block, [`first baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#first_baseline)
 alignment for everything else.

[`first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#first)

Specifies `first baseline` alignment.

[`last`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#last)

Specifies `last baseline` alignment.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | inline-level boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

baseline-source =   
  auto   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  first  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  last     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#examples)

-----------------------------------------------------------------------------------------------------------

### [Baseline selection in inline flex containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#baseline_selection_in_inline_flex_containers)

This example demonstrates using the `baseline-source` property to control the baseline alignment of inline flex containers.

#### HTML

Our HTML includes several [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 elements, which are generic inline containers for phrasing content. Three of the `<span>` elements contain nested `<span>` children.

html

    <span>Baseline ___</span>
    
    <span class="box first">
      <span>First</span>
      <span>A</span>
      <span>B</span>
      <span>C</span>
    </span>
    
    <span class="box auto">
      <span>Auto</span>
      <span>A</span>
      <span>B</span>
      <span>C</span>
    </span>
    
    <span class="box last">
      <span>A</span>
      <span>B</span>
      <span>C</span>
      <span>Last</span>
    </span>
    

#### CSS

    body {
      font-family: sans-serif;
    }
    
    .box {
      border: 2px solid #888888;
      width: 50px;
    }
    
    span {
      padding: 0.4rem;
    }
    

We define all the boxes to be inline flex containers. We set the `.first` box to use the first baseline, the `.auto` box uses the default baseline (which is `first` for inline flex containers), and the `.last` box uses the last baseline.

css

    .box {
      display: inline-flex;
      flex-direction: column;
    }
    
    .first {
      baseline-source: first;
    }
    
    .auto {
      baseline-source: auto;
    }
    
    .last {
      baseline-source: last;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# baseline-source](https://drafts.csswg.org/css-inline/#baseline-source) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
     property
*   [CSS box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/baseline-source/index.md?plain=1 "Folder: en-us/web/css/reference/properties/baseline-source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbaseline-source&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbaseline-source%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbaseline-source%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbaseline-source%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")