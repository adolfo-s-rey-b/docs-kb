*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#mdn-search)
    

`log()` CSS function
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`log()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is an exponential function that returns the logarithm of a number.

[Logarithm](https://en.wikipedia.org/wiki/Logarithm "External link (opens in new tab)")
 is the inverse of exponentiation. It is the number that a fixed base has to be raised to in order to yield the number passed as the first parameter.

In CSS, when a single parameter is passed, the natural logarithm `e`, or approximately `2.7182818`, is used, though the base can be set to any value with an optional second parameter.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#syntax)

---------------------------------------------------------------------------------------

css

    /* A <number> value */
    width: calc(100px * log(7.389)); /* 200px */
    width: calc(100px * log(8, 2)); /* 300px */
    width: calc(100px * log(625, 5)); /* 400px */
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#parameters)

The `log(value [, base]?)` function accepts two comma-separated values as its parameters.

[`value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#value)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 greater than or equal to 0. Representing the value to be taken the log of.

[`base`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#base)

Optional. A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 greater than or equal to 0. Representing the base of the logarithm. If not defined, the default logarithmic base `e` is used.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#return_value)

The logarithm of `value`, when `base` is defined.

The natural logarithm (base `e`) of `value`, when `base` is not defined.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#formal_syntax)

-----------------------------------------------------------------------------------------------------

<log()> =   
  log( <calc-sum> , <calc-sum>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#examples)

-------------------------------------------------------------------------------------------

### [Using the `log()` function on a logarithmic scale](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#using_the_log_function_on_a_logarithmic_scale)

This example illustrates how the `log()` function can be used to visualize data values by using a [logarithmic scale](https://en.wikipedia.org/wiki/Logarithmic_scale "External link (opens in new tab)")
. The width of each bar in this example is relative to its data value on a logarithmic scale with base 10. On each element, its value is assigned to a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 named `--value`, which is then used by the `.bar` class to calculate its width.

#### HTML

html

    <div class="bar" style="--value: 50">50</div>
    <div class="bar" style="--value: 100">100</div>
    <div class="bar" style="--value: 500">500</div>
    <div class="bar" style="--value: 10000">10,000</div>
    <div class="bar" style="--value: 2000000">2,000,000</div>
    

#### CSS

css

    .bar {
      width: calc(log(var(--value), 10) * 2em);
    }
    

    .bar {
      height: 2em;
      background-color: tomato;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0.25em 0;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# exponent-funcs](https://drafts.csswg.org/css-values/#exponent-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log#see_also)

-------------------------------------------------------------------------------------------

*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
    
*   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/log/index.md?plain=1 "Folder: en-us/web/css/reference/values/log (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flog&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flog%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flog%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flog%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")