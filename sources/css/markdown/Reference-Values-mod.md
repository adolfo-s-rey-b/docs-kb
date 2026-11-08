*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#mdn-search)
    

`mod()` CSS function
====================

Baseline 2024

Newly available

Since May 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mod()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 returns a modulus left over when the first parameter is divided by the second parameter, similar to the JavaScript [remainder operator (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
. The modulus is the value left over when one operand, the dividend, is divided by a second operand, the divisor. It always takes the sign of the divisor.

The calculation is `a - (Math.floor(a / b) * b)`. For example, the CSS `mod(21, -4)` function returns the remainder of `-3`. The full calculation is `21 - (Math.floor(21 / -4) * -4)`. When dividing `21` by `-4`, the result is `-5.25`. This is floored to `-6`. Multiplying `-6` by `-4` is `24`. Subtracting this `24` from the original `21`, the remainder is -3.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#syntax)

---------------------------------------------------------------------------------------

css

    /* Unitless <number> */
    line-height: mod(7, 2); /* 1 */
    line-height: mod(14, 5); /* 4 */
    line-height: mod(3.5, 2); /* 1.5 */
    
    /* Unit based <percentage> and <dimension> */
    margin: mod(15%, 2%); /* 1% */
    margin: mod(18px, 4px); /* 2px */
    margin: mod(19rem, 5rem); /* 4rem */
    margin: mod(29vmin, 6vmin); /* 5vmin */
    margin: mod(1000px, 29rem); /* 72px - if root font-size is 16px */
    
    /* Negative/positive values */
    rotate: mod(100deg, 30deg); /* 10deg */
    rotate: mod(135deg, -90deg); /* -45deg */
    rotate: mod(-70deg, 20deg); /* 10deg */
    rotate: mod(-70deg, -15deg); /* -10deg */
    
    /* Calculations */
    scale: mod(10 * 2, 1.7); /* 1.3 */
    rotate: mod(10turn, 18turn / 3); /* 4turn */
    transition-duration: mod(20s / 2, 3000ms * 2); /* 4s */
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#parameters)

The `mod(dividend, divisor)` function accepts two comma-separated values as its parameters. Both parameters must have the same type, [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [dimension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, for the function to be valid. While the units in the two parameters don't need to be the same, they do need of the same dimension type, such as [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, or [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
 to be valid.

[`dividend`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#dividend)

A calculation that resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the dividend.

[`divisor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#divisor)

A calculation that resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the divisor.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#return_value)

Returns a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 (corresponds to the parameters' type) representing the modulus, that is, the operation left over.

*   If `divisor` is `0`, the result is `NaN`.
*   If `dividend` is `infinite`, the result is `NaN`.
*   If `divisor` is positive the result is positive (`0⁺`), and if `divisor` is negative the result is negative (`0⁻`).

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#formal_syntax)

-----------------------------------------------------------------------------------------------------

<mod()> =   
  mod( <calc-sum> , <calc-sum> )    
  
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

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# funcdef-mod](https://drafts.csswg.org/css-values/#funcdef-mod) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod#see_also)

-------------------------------------------------------------------------------------------

*   [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    
*   [`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/mod/index.md?plain=1 "Folder: en-us/web/css/reference/values/mod (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fmod&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fmod%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fmod%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fmod%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")