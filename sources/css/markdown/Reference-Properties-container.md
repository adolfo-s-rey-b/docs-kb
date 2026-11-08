*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#mdn-search)
    

`container` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **container** [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property establishes the element as a query container and specifies the name and type of the [containment context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#naming_containment_contexts)
 used in a [container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
    
*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#values)

[`<container-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#container-name)

A case-sensitive name for the containment context. More details on the syntax are covered in the [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 property page.

[`<container-type>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#container-type)

The type of containment context. More details on the syntax are covered in the [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
 property page.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)<br>    : `none`<br>*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)<br>    : `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | as each of the properties of the shorthand:  <br><br>*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)<br>    : no<br>*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)<br>    : no |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)<br>    : `none` or an ordered list of identifiers<br>*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)<br>    : Not animatable<br>*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#formal_syntax)

---------------------------------------------------------------------------------------------------------------

container =   
  [<'container-name'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<'container-type'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<container-name>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
[<container-type>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
 =   
  normal                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 size [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-size [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 scroll-state [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#examples)

-----------------------------------------------------------------------------------------------------

### [Establishing inline size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#establishing_inline_size_containment)

Given the following HTML example which is a card component with an image, a title, and some text:

The explicit way to create a container context is to declare a `container-type` with an optional `container-name`:

The `container` shorthand is intended to make this definable in a single declaration:

You can then target that container by name using the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Conditional Rules Module Level 5  <br>\# container-shorthand](https://drafts.csswg.org/css-conditional-5/#container-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container#see_also)

-----------------------------------------------------------------------------------------------------

*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
    
*   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
     at-rule
*   CSS [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
     property
*   CSS [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
     property
*   CSS [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
     property
*   CSS [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/container/index.md?plain=1 "Folder: en-us/web/css/reference/properties/container (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ce88199869b63f8da3bbeafd899400f7579cce9%0A*+Document+last+modified%3A+2026-06-08T16%3A09%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")