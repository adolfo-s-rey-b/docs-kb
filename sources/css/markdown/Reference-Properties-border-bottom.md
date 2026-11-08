*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#mdn-search)
    

`border-bottom` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-bottom`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets an element's bottom [border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
. It sets the values of [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
, [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
 and [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#try_it)

-----------------------------------------------------------------------------------------------------

    border-bottom: solid;
    

    border-bottom: dashed red;
    

    border-bottom: 1rem solid;
    

    border-bottom: thick double #32a1ce;
    

    border-bottom: 4mm ridge rgb(211 220 50 / 0.6);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: #eeeeee;
      color: darkmagenta;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    
*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    
*   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#syntax)

-----------------------------------------------------------------------------------------------------

css

    border-bottom: 1px;
    border-bottom: 2px dotted;
    border-bottom: medium dashed blue;
    
    /* Global values */
    border-bottom: inherit;
    border-bottom: initial;
    border-bottom: revert;
    border-bottom: revert-layer;
    border-bottom: unset;
    

The three values of the shorthand property can be specified in any order, and one or two of them may be omitted.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#values)

[`<br-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#br-width)

See [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
.

[`<br-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#br-style)

See [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

See [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#description)

---------------------------------------------------------------------------------------------------------------

As with all shorthand properties, `border-bottom` always sets the values of all of the properties that it can set, even if they are not specified. It sets those that are not specified to their default values. Consider the following code:

css

    border-bottom-style: dotted;
    border-bottom: thick green;
    

It is actually the same as this one:

css

    border-bottom-style: dotted;
    border-bottom: none thick green;
    

The value of [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
 given before `border-bottom` is ignored. Since the default value of [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
 is `none`, not specifying the `border-style` part results in no border.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>    : `medium`<br>*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>    : `none`<br>*   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>    : `currentcolor` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>    : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>    , snapped as a line width<br>*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>    : as specified<br>*   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>    : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>    : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>    <br>*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>    : discrete<br>*   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

border-bottom =   
  <line-width>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <line-style>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
         
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#examples)

---------------------------------------------------------------------------------------------------------

### [Applying a bottom border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#applying_a_bottom_border)

#### HTML

html

    <div>This box has a border on the bottom side.</div>
    

#### CSS

css

    div {
      border-bottom: 4px dashed blue;
      background-color: gold;
      height: 100px;
      width: 100px;
      font-weight: bold;
      text-align: center;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-shorthands](https://drafts.csswg.org/css-backgrounds/#border-shorthands) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom#see_also)

---------------------------------------------------------------------------------------------------------

*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-bottom/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-bottom (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")