*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#mdn-search)
    

`text-decoration` CSS property
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-decoration`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the appearance of decorative lines on text. It is a shorthand for [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
, [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
, [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
, and the newer [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
 property.

Text decorations are drawn across descendant text elements. This means that if an element specifies a text decoration, then a child element can't remove the decoration. For example, in the markup `<p>This text has <em>some emphasized words</em> in it.</p>`, the style rule `p { text-decoration: underline; }` would cause the entire paragraph to be underlined. The style rule `em { text-decoration: none; }` would not cause any change; the entire paragraph would still be underlined. However, the rule `em { text-decoration: overline; }` would cause a second decoration to appear on "some emphasized words".

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#try_it)

-------------------------------------------------------------------------------------------------------

    text-decoration: underline;
    

    text-decoration: underline dotted;
    

    text-decoration: underline dotted red;
    

    text-decoration: green wavy underline;
    

    text-decoration: underline overline #ff3028;
    

    <section id="default-example">
      <p>
        I'd far rather be
        <span class="transition-all" id="example-element">happy than right</span>
        any day.
      </p>
    </section>
    

    p {
      font: 1.5em sans-serif;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    
*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    
*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#syntax)

-------------------------------------------------------------------------------------------------------

css

    text-decoration: underline;
    text-decoration: overline red;
    text-decoration: none;
    
    /* Global values */
    text-decoration: inherit;
    text-decoration: initial;
    text-decoration: revert;
    text-decoration: revert-layer;
    text-decoration: unset;
    

The `text-decoration` property is specified as one or more space-separated values representing the various longhand text-decoration properties.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#values)

[`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)

Sets the kind of decoration used, such as `underline` or `line-through`.

[`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)

Sets the color of the decoration.

[`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)

Sets the style of the line used for the decoration, such as `solid`, `wavy`, or `dashed`.

[`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)

Sets the thickness of the line used for the decoration.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)<br>    : `currentcolor`<br>*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)<br>    : `solid`<br>*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)<br>    : `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)<br>    : as specified<br>*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)<br>    : as specified<br>*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)<br>    : computed color<br>*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.")<br>    <br>*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)<br>    : discrete<br>*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)<br>    : discrete<br>*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

text-decoration =   
  [<'text-decoration-line'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
       [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'text-decoration-thickness'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'text-decoration-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
      [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'text-decoration-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
        
  
[<text-decoration-line>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
 =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 underline [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 overline [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 line-through [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 blink [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  spelling-error                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  grammar-error                                         
  
[<text-decoration-thickness>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
 =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  from-font            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <line-width>           
  
[<text-decoration-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
 =   
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  wavy      
  
[<text-decoration-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
 =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#examples)

-----------------------------------------------------------------------------------------------------------

### [Demonstration of text-decoration values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#demonstration_of_text-decoration_values)

css

    .under {
      text-decoration: underline red;
    }
    
    .over {
      text-decoration: wavy overline lime;
    }
    
    .line {
      text-decoration: line-through;
    }
    
    .plain {
      text-decoration: none;
    }
    
    .underover {
      text-decoration: dashed underline overline;
    }
    
    .thick {
      text-decoration: solid underline purple 4px;
    }
    
    .blink {
      text-decoration: blink;
    }
    

html

    <p class="under">This text has a line underneath it.</p>
    <p class="over">This text has a line over it.</p>
    <p class="line">This text has a line going through it.</p>
    <p>
      This <a class="plain" href="#">link will not be underlined</a>, as links
      generally are by default. Be careful when removing the text decoration on
      anchors since users often depend on the underline to denote hyperlinks.
    </p>
    <p class="underover">This text has lines above <em>and</em> below it.</p>
    <p class="thick">
      This text has a really thick purple underline in supporting browsers.
    </p>
    <p class="blink">
      This text might blink for you, depending on the browser you use.
    </p>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 4  <br>\# text-decoration-property](https://drafts.csswg.org/css-text-decor-4/#text-decoration-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# TextDecorationProperties](https://w3c.github.io/svgwg/svg2-draft/text.html#TextDecorationProperties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration#see_also)

-----------------------------------------------------------------------------------------------------------

*   The individual text-decoration properties are [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    , and [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    .
*   The [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
    , [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    , and [`text-underline-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
     properties also affect text-decoration, but are not included in the shorthand.
*   The [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     property controls the appearance of items in HTML [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
     lists.
*   SVG [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/text-decoration)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")