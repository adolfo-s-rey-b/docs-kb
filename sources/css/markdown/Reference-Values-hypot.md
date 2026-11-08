*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#mdn-search)
    

`hypot()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hypot()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is an exponential function that returns the [square root](https://en.wikipedia.org/wiki/Square_root "External link (opens in new tab)")
 of the sum of squares of its parameters.

While [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
 and [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
 only work on unitless numbers, `hypot()` accepts values with units, but they all must have the same [type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#syntax)

-----------------------------------------------------------------------------------------

css

    /* A <number> value */
    width: hypot(2em); /* 2em */
    width: hypot(3em, 4em); /* 5em */
    width: hypot(30px, 40px); /* 50px */
    width: hypot(48px, 64px); /* 80px */
    width: hypot(3px, 4px, 5px); /* 7.0710678118654755px */
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#parameters)

The `hypot(x [, ...]#)` function accepts one or more comma-separated calculations as its parameters.

[`x`, `x2`, ..., `xN`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#x)

A calculation that resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#return_value)

Returns a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 (based on the inputs), which is the square root of the sum of squares of its parameters.

*   If any of the inputs is `infinite`, the result is `+∞`.
*   If a single parameter is provided, the result is the absolute value of its input. `hypot(2em)` and `hypot(-2em)` both resolve to `2em`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#formal_syntax)

-------------------------------------------------------------------------------------------------------

<hypot()> =   
  hypot( <calc-sum>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#examples)

---------------------------------------------------------------------------------------------

### [Sizes based on hypot function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#sizes_based_on_hypot_function)

This example shows how you can use the `hypot()` function to calculate sizes.

#### HTML

html

    <div class="boxes">
      <div class="box">100px</div>
      <div class="box one">100px</div>
      <div class="box two">141.42px</div>
      <div class="box three">250px</div>
    </div>
    

#### CSS

Here we are using [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 to define the sizes to be used. First we declare the first size (`--size-0`) which is then used to calculate the other sizes.

*   `--size-1` is calculated with the hypotenuse of `--size-0` (100px). This takes the square value and, as there is no other value, returns the square root of the value, which results in 100px.
*   `--size-2` is calculated with the hypotenuse of `--size-0` (100px), twice. This takes the square of the value (100px \* 100px = 10000px2) and adds it to the square of `--size-0` again (10000px2 + 10000px2 = 20000px2) and returns the square root of the sum (√(20000px2)), which results in 141.42px.
*   `--size-3` is calculated with the hypotenuse `--size-0` \* 1.5 (150px) and `--size-0` \* 2 (200px). The result is the square root of the sum of their squares: The values are squared (22500px2 and 40000px2) and added together (62500px2), with the sum square-rooted (√(62500px2)) being 250px.

css

    :root {
      --size-0: 100px;
      --size-1: hypot(var(--size-0)); /*  100px */
      --size-2: hypot(var(--size-0), var(--size-0)); /*  141.42px */
      --size-3: hypot(
        calc(var(--size-0) * 1.5),
        calc(var(--size-0) * 2)
      ); /*  250px */
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

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# exponent-funcs](https://drafts.csswg.org/css-values/#exponent-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot#see_also)

---------------------------------------------------------------------------------------------

*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    
*   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/hypot/index.md?plain=1 "Folder: en-us/web/css/reference/values/hypot (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhypot&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhypot%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhypot%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhypot%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")