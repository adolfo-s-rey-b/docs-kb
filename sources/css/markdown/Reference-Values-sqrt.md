*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#mdn-search)
    

`sqrt()` CSS function
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sqrt()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is an exponential function that returns the [square root](https://en.wikipedia.org/wiki/Square_root "External link (opens in new tab)")
 of a number.

The function `pow(x, 0.5)` is equivalent to `sqrt(x)`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#syntax)

----------------------------------------------------------------------------------------

css

    /* A <number> value */
    width: calc(100px * sqrt(9)); /*  300px */
    width: calc(100px * sqrt(25)); /*  500px */
    width: calc(100px * sqrt(100)); /* 1000px */
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#parameters)

The `sqrt(x)` function accepts only one value as its parameter.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#x)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 greater than or equal to 0.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#return_value)

Returns a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 which is the square root of `x`.

*   if `x` is `+∞`, the result is `+∞`.
*   If `x` is `0⁻`, the result is `0⁻`.
*   If `x` is less than `0`, the result is `NaN`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#formal_syntax)

------------------------------------------------------------------------------------------------------

<sqrt()> =   
  sqrt( <calc-sum> )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#examples)

--------------------------------------------------------------------------------------------

### [Scale sizes based on square root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#scale_sizes_based_on_square_root)

This example shows how you can use the `sqrt()` function to calculate sizes.

#### HTML

html

    <div class="boxes">
      <div class="box">50px</div>
      <div class="box one">100px</div>
      <div class="box two">150px</div>
      <div class="box three">200px</div>
    </div>
    

#### CSS

Here we are using [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 to define the sizes to be used. First, we declare the first size (`--size-0`), which is then used to calculate the other sizes.

*   `--size-1` is calculated by multiplying the value of `--size-0` (50px) by the square root of 4 (2), which results in 100px.
*   `--size-2` is calculated by multiplying the value of `--size-0` (50px) by the square root of 9 (3), which results in 150px.
*   `--size-3` is calculated by multiplying the value of `--size-0` (50px) by the square root of 16 (4), which results in 200px.

css

    :root {
      --size-0: 50px;
      --size-1: calc(var(--size-0) * sqrt(4)); /*  100px */
      --size-2: calc(var(--size-0) * sqrt(9)); /*  150px */
      --size-3: calc(var(--size-0) * sqrt(16)); /*  200px */
    }
    

    .boxes {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
    }
    
    .box {
      width: var(--size-0);
      height: var(--size-0);
      background-color: tomato;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

The sizes are then applied as the `width` and `height` values of the selectors.

css

    .one {
      width: var(--size-1);
      height: var(--size-1);
    }
    .two {
      width: var(--size-2);
      height: var(--size-2);
    }
    .three {
      width: var(--size-3);
      height: var(--size-3);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# exponent-funcs](https://drafts.csswg.org/css-values/#exponent-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt#see_also)

--------------------------------------------------------------------------------------------

*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
    
*   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    
*   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/sqrt/index.md?plain=1 "Folder: en-us/web/css/reference/values/sqrt (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsqrt&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsqrt%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsqrt%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsqrt%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")