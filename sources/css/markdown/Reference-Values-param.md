*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#mdn-search)
    

`param()` CSS function
======================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#browser_compatibility)
 carefully before using this in production.

The **`param()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is used to set link parameters. It can be used in the [`link-parameters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters)
 CSS property, in the URL fragment of an external resource, or in the [`<url-modifier>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function#url-modifier)
 of the `url()` CSS function.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#syntax)

-----------------------------------------------------------------------------------------

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#values)

-----------------------------------------------------------------------------------------

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

A `<dashed-ident>` is a user-defined variable that is used as an identifier in the [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
 CSS function to update the value.

[`<declaration_value>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#declaration_value)

A `<declaration_value>` is the value of the attribute being updated. If the `<declaration-value>` is omitted, it represents an empty value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#formal_syntax)

-------------------------------------------------------------------------------------------------------

<param()> =   
  param( <param-spec> , <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<param-spec> =   
  color                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  accent-color                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 <css-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<css-type> =   
  <syntax-component>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <type()>              
  
<syntax-component> =   
  <syntax-single-component> <syntax-multiplier>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '<' transform-list '>'                            
  
[<type()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 =   
  type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 )    
  
<syntax-single-component> =   
  '<' <syntax-type-name> '>'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
                       
  
<syntax-multiplier> =   
  '#'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '+'    
  
<syntax-type-name> =   
  angle               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  custom-ident        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  image               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  integer             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length-percentage   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  number              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  percentage          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  resolution          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  string              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  time                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  url                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  transform-function    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#examples)

---------------------------------------------------------------------------------------------

All of the following examples use the same SVG file, which has attributes set with [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
 CSS function.

### [Using `link-parameters` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#using_link-parameters_property)

In this example the SVG attributes are updated with the [`link-parameters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters)
 CSS property and `param()` function.

### [Passing `param()` into URL modifier](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#passing_param_into_url_modifier)

In this example the SVG attributes are updated by passing the `param()` function into the URL fragment of the [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#src)
 attribute of the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 HTML element.

### [Using `param()` with `background-image` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#using_param_with_background-image_property)

In this example the SVG attributes are updated by passing the `param()` function into the [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 data type of the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 CSS property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Linked Parameters Module Level 1  <br>\# funcdef-param](https://drafts.csswg.org/css-link-params-1/#funcdef-param) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param#see_also)

---------------------------------------------------------------------------------------------

*   [`link-parameters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters)
    
*   [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/param/index.md?plain=1 "Folder: en-us/web/css/reference/values/param (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fparam&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fparam%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fparam%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fparam%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5738cef418354ffa76a451281312fec98a7aad63%0A*+Document+last+modified%3A+2026-10-28T19%3A17%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")