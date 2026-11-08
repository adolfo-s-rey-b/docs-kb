*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#mdn-search)
    

`border-style` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the line style for all four sides of an element's border.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#try_it)

----------------------------------------------------------------------------------------------------

    border-style: none;
    

    border-style: dotted;
    

    border-style: inset;
    

    border-style: dashed solid;
    

    border-style: dashed double none;
    

    border-style: dashed groove none dotted;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: #eeeeee;
      color: black;
      border: 0.75em solid;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    
    body {
      background-color: white;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    
*   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    
*   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    
*   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    border-style: none;
    border-style: hidden;
    border-style: dotted;
    border-style: dashed;
    border-style: solid;
    border-style: double;
    border-style: groove;
    border-style: ridge;
    border-style: inset;
    border-style: outset;
    
    /* top and bottom | left and right */
    border-style: dotted solid;
    
    /* top | left and right | bottom */
    border-style: hidden double dashed;
    
    /* top | right | bottom | left */
    border-style: none solid dotted dashed;
    
    /* Global values */
    border-style: inherit;
    border-style: initial;
    border-style: revert;
    border-style: revert-layer;
    border-style: unset;
    

The `border-style` property may be specified using one, two, three, or four values.

*   When **one** value is specified, it applies the same style to **all four sides**.
*   When **two** values are specified, the first style applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first style applies to the **top**, the second to the **left and right**, the third to the **bottom**.
*   When **four** values are specified, the styles apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

Each value is a keyword chosen from the list below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#values)

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#line-style)

Describes the style of the border. It can have the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#none)

Like the `hidden` keyword, displays no border. Unless a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 is set, the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of the same side's [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 will be `0`, even if the specified value is something else. In the case of table cell and border collapsing, the `none` value has the _lowest_ priority: if any other conflicting border is set, it will be displayed.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#hidden)

Like the `none` keyword, displays no border. Unless a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 is set, the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of the same side's [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 will be `0`, even if the specified value is something else. In the case of table cell and border collapsing, the `hidden` value has the _highest_ priority: if any other conflicting border is set, it won't be displayed.

[`dotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#dotted)

Displays a series of rounded dots. The spacing of the dots is not defined by the specification and is implementation-specific. The radius of the dots is half the computed value of the same side's [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
.

[`dashed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#dashed)

Displays a series of short square-ended dashes or line segments. The exact size and length of the segments are not defined by the specification and are implementation-specific.

[`solid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#solid)

Displays a single, straight, solid line.

[`double`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#double)

Displays two straight lines that add up to the pixel size defined by [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
.

[`groove`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#groove)

Displays a border with a carved appearance. It is the opposite of `ridge`.

[`ridge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#ridge)

Displays a border with an extruded appearance. It is the opposite of `groove`.

[`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#inset)

Displays a border that makes the element appear embedded. It is the opposite of `outset`. When applied to a table cell with [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 set to `collapsed`, this value behaves like `ridge`.

[`outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#outset)

Displays a border that makes the element appear embossed. It is the opposite of `inset`. When applied to a table cell with [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 set to `collapsed`, this value behaves like `groove`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)<br>    : `none`<br>*   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)<br>    : `none`<br>*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>    : `none`<br>*   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)<br>    : `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)<br>    : as specified<br>*   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)<br>    : as specified<br>*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>    : as specified<br>*   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#formal_syntax)

------------------------------------------------------------------------------------------------------------------

border-style =   
  [<'border-top-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-top-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
 =   
  <line-style>    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#examples)

--------------------------------------------------------------------------------------------------------

### [All property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#all_property_values)

Here is an example of all the property values.

#### HTML

html

    <pre class="b1">none</pre>
    <pre class="b2">hidden</pre>
    <pre class="b3">dotted</pre>
    <pre class="b4">dashed</pre>
    <pre class="b5">solid</pre>
    <pre class="b6">double</pre>
    <pre class="b7">groove</pre>
    <pre class="b8">ridge</pre>
    <pre class="b9">inset</pre>
    <pre class="b10">outset</pre>
    

#### CSS

css

    pre {
      height: 80px;
      width: 120px;
      margin: 20px;
      padding: 20px;
      display: inline-block;
      background-color: palegreen;
      border-width: 5px;
      box-sizing: border-box;
    }
    
    /* border-style example classes */
    .b1 {
      border-style: none;
    }
    
    .b2 {
      border-style: hidden;
    }
    
    .b3 {
      border-style: dotted;
    }
    
    .b4 {
      border-style: dashed;
    }
    
    .b5 {
      border-style: solid;
    }
    
    .b6 {
      border-style: double;
    }
    
    .b7 {
      border-style: groove;
    }
    
    .b8 {
      border-style: ridge;
    }
    
    .b9 {
      border-style: inset;
    }
    
    .b10 {
      border-style: outset;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-style](https://drafts.csswg.org/css-backgrounds/#border-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style#see_also)

--------------------------------------------------------------------------------------------------------

*   The border-related shorthand CSS properties: [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")