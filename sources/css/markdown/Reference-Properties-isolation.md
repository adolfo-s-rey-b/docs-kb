*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#mdn-search)
    

`isolation` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`isolation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property determines whether an element must create a new [stacking context](https://developer.mozilla.org/en-US/docs/Glossary/Stacking_context)
.

This property is especially helpful when used in conjunction with [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
 and [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#try_it)

-------------------------------------------------------------------------------------------------

    isolation: auto;
    

    isolation: isolate;
    

    <section class="default-example" id="default-example">
      <div class="background-container">
        <div id="example-element">
          <img src="/shared-assets/images/examples/firefox-logo.svg" />
          <p><code>mix-blend-mode: multiply;</code></p>
        </div>
      </div>
    </section>
    

    .background-container {
      background-color: #f4f460;
      width: 250px;
    }
    
    #example-element {
      border: 1px solid black;
      margin: 2em;
    }
    
    #example-element * {
      mix-blend-mode: multiply;
      color: #8245a3;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    isolation: auto;
    isolation: isolate;
    
    /* Global values */
    isolation: inherit;
    isolation: initial;
    isolation: revert;
    isolation: revert-layer;
    isolation: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#auto)

A new stacking context is created only if one of the properties applied to the element requires it.

[`isolate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#isolate)

A new stacking context must be created.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | All elements. In SVG, it applies to container elements, graphics elements, and graphics referencing elements. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#formal_syntax)

---------------------------------------------------------------------------------------------------------------

isolation =   
  <isolation-mode>    
  
<isolation-mode> =   
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  isolate    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#examples)

-----------------------------------------------------------------------------------------------------

### [Forcing a new stacking context for an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#forcing_a_new_stacking_context_for_an_element)

#### HTML

html

    <div class="big-square">
      <div class="isolation-auto">
        <div class="small-square">auto</div>
      </div>
      <div class="isolation-isolate">
        <div class="small-square">isolate</div>
      </div>
    </div>
    

#### CSS

css

    .isolation-auto {
      isolation: auto;
    }
    
    .isolation-isolate {
      isolation: isolate;
    }
    
    .big-square {
      background-color: lime;
      width: 200px;
      height: 210px;
    }
    
    .small-square {
      background-color: lime;
      width: 100px;
      height: 100px;
      border: 1px solid black;
      padding: 2px;
      mix-blend-mode: difference;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compositing and Blending Module Level 2  <br>\# isolation](https://drafts.csswg.org/compositing/#isolation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation#see_also)

-----------------------------------------------------------------------------------------------------

*   [`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
    
*   [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    , [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/isolation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/isolation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fisolation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fisolation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fisolation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fisolation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")