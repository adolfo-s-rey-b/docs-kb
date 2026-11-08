*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#mdn-search)
    

`outline-style` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`outline-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the style of an element's outline. An outline is a line that is drawn around an element, outside the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
.

It is often more convenient to use the shorthand property [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 when defining the appearance of an outline.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#try_it)

-----------------------------------------------------------------------------------------------------

    outline-style: none;
    

    outline-style: dotted;
    

    outline-style: solid;
    

    outline-style: groove;
    

    outline-style: inset;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with an outline around it.
      </div>
    </section>
    

    #example-element {
      outline: 0.75em solid;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    outline-style: auto;
    outline-style: none;
    outline-style: dotted;
    outline-style: dashed;
    outline-style: solid;
    outline-style: double;
    outline-style: groove;
    outline-style: ridge;
    outline-style: inset;
    outline-style: outset;
    
    /* Global values */
    outline-style: inherit;
    outline-style: initial;
    outline-style: revert;
    outline-style: revert-layer;
    outline-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#values)

This property is specified as one of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#auto)

Permits the user agent to render a custom outline style.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#none)

No outline is used.

[`dotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#dotted)

The outline is a series of dots.

[`dashed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#dashed)

The outline is a series of short line segments.

[`solid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#solid)

The outline is a single line.

[`double`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#double)

The outline is two single lines. The [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
 is the sum of the two lines and the space between them.

[`groove`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#groove)

The outline looks as though it were carved into the page.

[`ridge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#ridge)

The opposite of `groove`: the outline looks as though it were extruded from the page.

[`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#inset)

The outline makes the box look as though it were embedded in the page.

[`outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#outset)

The opposite of `inset`: the outline makes the box look as though it were coming out of the page.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

outline-style =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <outline-line-style>    
  
<outline-line-style> =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#examples)

---------------------------------------------------------------------------------------------------------

### [Setting outline style to auto](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#setting_outline_style_to_auto)

The `auto` value indicates a custom outline style, described in [the specification](https://drafts.csswg.org/css-ui/#outline-style "External link (opens in new tab)")
 as "typically a style \[that\] is either a user interface default for the platform, or perhaps a style that is richer than can be described in detail in CSS, e.g., a rounded edge outline with semi-translucent outer pixels that appears to glow".

#### HTML

html

    <div>
      <p class="auto">Outline Demo</p>
    </div>
    

#### CSS

css

    .auto {
      outline-style: auto; /* same result as "outline: auto" */
    }
    
    /* To make the Demo clearer */
    * {
      outline-width: 10px;
      padding: 15px;
    }
    

#### Result

### [Setting outline style to dashed and dotted](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#setting_outline_style_to_dashed_and_dotted)

#### HTML

html

    <div>
      <div class="dotted">
        <p class="dashed">Outline Demo</p>
      </div>
    </div>
    

#### CSS

css

    .dotted {
      outline-style: dotted; /* same result as "outline: dotted" */
    }
    .dashed {
      outline-style: dashed;
    }
    
    /* To make the Demo clearer */
    * {
      outline-width: 10px;
      padding: 15px;
    }
    

#### Result

### [Setting outline style to solid and double](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#setting_outline_style_to_solid_and_double)

#### HTML

html

    <div>
      <div class="solid">
        <p class="double">Outline Demo</p>
      </div>
    </div>
    

#### CSS

css

    .solid {
      outline-style: solid;
    }
    .double {
      outline-style: double;
    }
    
    /* To make the Demo clearer */
    * {
      outline-width: 10px;
      padding: 15px;
    }
    

#### Result

### [Setting outline style to groove and ridge](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#setting_outline_style_to_groove_and_ridge)

#### HTML

html

    <div>
      <div class="groove">
        <p class="ridge">Outline Demo</p>
      </div>
    </div>
    

#### CSS

css

    .groove {
      outline-style: groove;
    }
    .ridge {
      outline-style: ridge;
    }
    
    /* To make the Demo clearer */
    * {
      outline-width: 10px;
      padding: 15px;
    }
    

#### Result

### [Setting outline style to inset and outset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#setting_outline_style_to_inset_and_outset)

#### HTML

html

    <div>
      <div class="inset">
        <p class="outset">Outline Demo</p>
      </div>
    </div>
    

#### CSS

css

    .inset {
      outline-style: inset;
    }
    .outset {
      outline-style: outset;
    }
    
    /* To make the Demo clearer */
    * {
      outline-width: 10px;
      padding: 15px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# outline-style](https://drafts.csswg.org/css-ui/#outline-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style#see_also)

---------------------------------------------------------------------------------------------------------

*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/outline-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/outline-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")