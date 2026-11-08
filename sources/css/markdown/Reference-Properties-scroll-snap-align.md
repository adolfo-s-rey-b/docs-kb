*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#mdn-search)
    

`scroll-snap-align` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-snap-align`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the box's snap position as an alignment of its [snap area](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_area)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#try_it)

---------------------------------------------------------------------------------------------------------

    scroll-snap-align: start;
    

    scroll-snap-align: end;
    

    scroll-snap-align: center;
    

    <section class="default-example" id="default-example">
      <div id="example-parent">
        <div>1</div>
        <div id="example-element">2</div>
        <div>3</div>
      </div>
      <div class="info">Scroll »</div>
    </section>
    

    .default-example {
      flex-wrap: wrap;
    }
    
    .default-example .info {
      width: 100%;
      padding: 0.5em 0;
      font-size: 90%;
    }
    
    #example-parent {
      text-align: left;
      width: 250px;
      height: 250px;
      overflow-x: scroll;
      display: flex;
      box-sizing: border-box;
      border: 1px solid black;
      scroll-snap-type: x mandatory;
    }
    
    #example-parent > div {
      flex: 0 0 66%;
      width: 250px;
      background-color: rebeccapurple;
      color: white;
      font-size: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    #example-parent > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Single keyword value */
    scroll-snap-align: none;
    scroll-snap-align: center;
    scroll-snap-align: start;
    scroll-snap-align: end;
    
    /* Two keyword values */
    scroll-snap-align: start end;
    scroll-snap-align: end center;
    scroll-snap-align: center start;
    
    /* Global values */
    scroll-snap-align: inherit;
    scroll-snap-align: initial;
    scroll-snap-align: revert;
    scroll-snap-align: revert-layer;
    scroll-snap-align: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#values)

This property is specified as one or two of the following keyword values, space-separated:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#none)

The box does not define a snap position in that axis.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#start)

The start alignment of this box's scroll [snap area](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_area)
, within the scroll container's [snapport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snapport)
 is a snap position in this axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#end)

The end alignment of this box's scroll snap area, within the scroll container's snapport is a snap position in this axis.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#center)

The center alignment of this box's scroll snap area, within the scroll container's snapport is a snap position in this axis.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#description)

-------------------------------------------------------------------------------------------------------------------

The `scroll-snap-align` property specifies the box's snap position as an alignment of its [snap area](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_area)
 (as the [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
) within its snap container's snap port (as the [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
).

One or two values can be specified for the `scroll-snap-align` property. If one value is set, it is applied to both the block and inline axes. If two values are set, the first value controls the block axis and the second value controls the inline axis.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

scroll-snap-align =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# scroll-snap-align](https://drafts.csswg.org/css-scroll-snap/#scroll-snap-align) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
    
*   [`scroll-initial-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target)
    
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-snap-align/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-snap-align (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-align&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-align%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-align%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-align%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6354422058e438a2599e4eab71eaec8eb40850fa%0A*+Document+last+modified%3A+2026-09-14T09%3A57%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")