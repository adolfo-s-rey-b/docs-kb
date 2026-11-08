*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#mdn-search)
    

`round()` CSS function
======================

Baseline 2024

Newly available

Since May 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`round()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 returns a rounded number based on a selected rounding strategy.

Authors should use a [custom CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 (e.g., `--my-property`) for the rounding value, interval, or both; using the `round()` function is redundant if these have known values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#syntax)

-----------------------------------------------------------------------------------------

css

    width: round(var(--width), 50px);
    width: round(up, 101px, var(--interval));
    width: round(down, var(--height), var(--interval));
    margin: round(to-zero, -105px, 10px);
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#parameters)

The `round(<rounding-strategy>, valueToRound, roundingInterval)` function specifies an optional rounding strategy, a value (or mathematical expression) to be rounded and a rounding interval (or mathematical expression). The `valueToRound` is rounded according to the rounding strategy, to the nearest integer multiple of `roundingInterval`.

[`<rounding-strategy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#rounding-strategy)

The rounding strategy. This may be one of the following values:

[`up`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#up)

Round `valueToRound` up to the nearest integer multiple of `roundingInterval` (if the value is negative, it will become "more positive"). This is equivalent to the JavaScript [`Math.ceil()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)
 method.

[`down`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#down)

Round `valueToRound` down to the nearest integer multiple of `roundingInterval` (if the value is negative, it will become "more negative"). This is equivalent to the JavaScript [`Math.floor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)
 method.

[`nearest` (default)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#nearest)

Round `valueToRound` to the nearest integer multiple of `roundingInterval`, which may be either above or below the value. If the `valueToRound` is half way between the rounding targets above and below (neither is "nearest"), it will be rounded up. Equivalent to JavaScript [`Math.round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)
.

[`to-zero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#to-zero)

Round `valueToRound` to the nearest integer multiple of `roundingInterval` closer to/towards zero (a positive number will decrease, while a negative value will become "less negative"). This is equivalent to the JavaScript [`Math.trunc()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/trunc)
 method.

[`valueToRound`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#valuetoround)

The value to be rounded. This must be a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or a mathematical expression that resolves to one of those values.

[`roundingInterval`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#roundinginterval)

The rounding interval. This is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or a mathematical expression that resolves to one of those values. If `valueToRound` is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, `roundingInterval` may be omitted and defaults to `1`. Otherwise, omitting it results in an invalid expression.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#return_value)

The value of `valueToRound`, rounded to the nearest lower or higher integer multiple of `roundingInterval`, depending on the `rounding strategy`.

*   If `roundingInterval` is 0, the result is `NaN`.
    
*   If `valueToRound` and `roundingInterval` are both `infinite`, the result is `NaN`.
    
*   If `valueToRound` is infinite but `roundingInterval` is finite, the result is the same `infinity`.
    
*   If `valueToRound` is finite but `roundingInterval` is infinite, the result depends on the rounding strategy and the sign of `A`:
    
    *   `up` - If `valueToRound` is positive (not zero), return `+∞`. If `valueToRound` is `0⁺`, return `0⁺`. Otherwise, return `0⁻`.
    *   `down` - If `valueToRound` is negative (not zero), return `−∞`. If `valueToRound` is `0⁻`, return `0⁻`. Otherwise, return `0⁺`.
    *   `nearest`, `to-zero` - If `valueToRound` is positive or `0⁺`, return `0⁺`. Otherwise, return `0⁻`.
*   The argument calculations can resolve to [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    , [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
    , or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    , but must have the same type, or else the function is invalid; the result will have the same type as the arguments.
    
*   If `valueToRound` is exactly equal to an integer multiple of `roundingInterval`, `round()` resolves to `valueToRound` exactly (preserving whether `valueToRound` is `0⁻` or `0⁺`, if relevant). Otherwise, there are two integer multiples of `roundingInterval` that are potentially "closest" to `valueToRound`, lower `roundingInterval` which is closer to `−∞` and upper `roundingInterval` which is closer to `+∞`.
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#formal_syntax)

-------------------------------------------------------------------------------------------------------

<round()> =   
  round( <rounding-strategy>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <calc-sum> , <calc-sum>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<rounding-strategy> =   
  nearest     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  up          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  down        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  to-zero     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  line-width    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#examples)

---------------------------------------------------------------------------------------------

### [Round positive values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#round_positive_values)

This example demonstrates how the `round()` function's rounding strategies work for positive values.

Of the five boxes below, the `round()` function is used to set the height of the last four. The value to be rounded is between 100 px and 125 px in each case, and the rounding value is 25px in all cases. The height of the boxes is therefore either rounded up to 125 px or down to 100 px.

#### HTML

The HTML defines 5 `div` elements that will be rendered as boxes by the CSS. The elements contain text indicating the rounding strategy, initial value, and expected final height of the box (in parentheses).

html

    <div class="box box-1">height: 100px</div>
    <div class="box box-2">up 101px (125px)</div>
    <div class="box box-3">down 122px (100px)</div>
    <div class="box box-4">to-zero 120px (100px)</div>
    <div class="box box-5">nearest 117px (125px)</div>
    

#### CSS

    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 50px;
    }
    

The CSS that is applied to all boxes is shown below. Note that we apply a [custom CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 named `--rounding-interval`, that we will use for the rounding interval.

css

    div.box {
      width: 100px;
      height: 100px;
      background: lightblue;
      --rounding-interval: 25px;
    }
    

The first `div` from the left isn't targeted with specific CSS rules, so it will have a default height of 100px. The CSS for `div` two, three, and four is shown below, which round, up, down, and to-zero, respectively.

css

    div.box-2 {
      height: round(up, 101px, var(--rounding-interval));
    }
    div.box-3 {
      height: round(down, 122px, var(--rounding-interval));
    }
    div.box-4 {
      height: round(to-zero, 120px, var(--rounding-interval));
    }
    

Notice how above we indicate the rounding interval using `var()` and the custom CSS property `--rounding-interval`.

The last box is set without specifying a rounding strategy, and hence defaults to `nearest`. In this case, the nearest interval to 117 px is 125px, so it will round up. Just for contrast, here we specified hardcoded values for both the rounding value and interval. While this is allowed, you wouldn't do this normally because there is no point rounding a number when you already know what the result must be.

css

    div.box-5 {
      height: round(117px, 25px);
    }
    

#### Result

If the browser supports the CSS `round()` function, you should see five columns with heights that are rounded as indicated by their contained text.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# funcdef-round](https://drafts.csswg.org/css-values/#funcdef-round) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round#see_also)

---------------------------------------------------------------------------------------------

*   [`mod()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)
    
*   [`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/round/index.md?plain=1 "Folder: en-us/web/css/reference/values/round (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fround&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fround%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fround%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fround%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa23122d0e86fb376234614beb5b350b217068054%0A*+Document+last+modified%3A+2026-09-10T17%3A10%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")