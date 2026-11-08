*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#mdn-search)
    

`<filter-function>` CSS type
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<filter-function>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a graphical effect that can change the appearance of an input image. It is used in the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#syntax)

---------------------------------------------------------------------------------------------------

The `<filter-function>` data type is specified using one of the filter functions listed below. Each function requires an argument which, if invalid, results in no filter being applied.

[`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)

Blurs the image.

[`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)

Makes the image brighter or darker.

[`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)

Increases or decreases the image's contrast.

[`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)

Applies a drop shadow behind the image.

[`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)

Converts the image to grayscale.

[`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)

Changes the overall hue of the image.

[`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)

Inverts the colors of the image.

[`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)

Makes the image transparent.

[`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)

Super-saturates or desaturates the input image.

[`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)

Converts the image to sepia.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<filter-function> =   
  <blur()>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <brightness()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <contrast()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <drop-shadow()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <grayscale()>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <hue-rotate()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <invert()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <opacity()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <sepia()>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <saturate()>       
  
[<blur()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
 =   
  blur( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<brightness()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
 =   
  brightness( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<contrast()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
 =   
  contrast( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<drop-shadow()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
 =   
  drop-shadow( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[{2,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<grayscale()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
 =   
  grayscale( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<hue-rotate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
 =   
  hue-rotate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<invert()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
 =   
  invert( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<opacity()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
 =   
  opacity( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<sepia()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
 =   
  sepia( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<saturate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
 =   
  saturate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#examples)

-------------------------------------------------------------------------------------------------------

### [Filter function comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#filter_function_comparison)

This example provides a graphic, a select menu to allow you to choose between the different types of filter function, and a slider to allow you to vary the values used inside the filter function. Updating the controls updates the filter effect in real time, allowing you to investigate the effects of different filters.

The dropdown selects the function name, and the slider sets the parameter value for that function. For `drop-shadow`, the value is used for both the horizontal and vertical offsets, and the radius is set to half the value.

    <div></div>
    <ul>
      <li>
        <label for="filter-select">Choose a filter function:</label>
        <select id="filter-select">
          <option selected>blur</option>
          <option>brightness</option>
          <option>contrast</option>
          <option>drop-shadow</option>
          <option>grayscale</option>
          <option>hue-rotate</option>
          <option>invert</option>
          <option>opacity</option>
          <option>saturate</option>
          <option>sepia</option>
        </select>
      </li>
      <li><input type="range" /><output></output></li>
      <li>
        <p>Current value: <code></code></p>
      </li>
    </ul>
    

    div {
      width: 100%;
      height: 512px;
      background-image: url("https://mdn.github.io/shared-assets/images/examples/fx-nightly-512.png");
      background-repeat: no-repeat;
      background-position: center center;
    }
    
    li {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }
    
    input {
      width: 60%;
    }
    
    output {
      width: 5%;
      text-align: center;
    }
    
    select {
      width: 40%;
      margin-left: 2px;
    }
    

    const selectElem = document.querySelector("select");
    const divElem = document.querySelector("div");
    const slider = document.querySelector("input");
    const output = document.querySelector("output");
    const curValue = document.querySelector("p code");
    
    selectElem.addEventListener("change", () => {
      setSlider(selectElem.value);
      setDiv(selectElem.value);
    });
    
    slider.addEventListener("input", () => {
      setDiv(selectElem.value);
    });
    
    function setSlider(filter) {
      switch (filter) {
        case "blur":
          slider.value = 0;
          slider.min = 0;
          slider.max = 30;
          slider.step = 1;
          slider.setAttribute("data-unit", "px");
          break;
        case "brightness":
        case "contrast":
        case "saturate":
          slider.value = 1;
          slider.min = 0;
          slider.max = 4;
          slider.step = 0.05;
          slider.setAttribute("data-unit", "");
          break;
        case "drop-shadow":
          slider.value = 0;
          slider.min = -20;
          slider.max = 40;
          slider.step = 1;
          slider.setAttribute("data-unit", "px");
          break;
        case "opacity":
          slider.value = 1;
          slider.min = 0;
          slider.max = 1;
          slider.step = 0.01;
          slider.setAttribute("data-unit", "");
          break;
        case "grayscale":
        case "invert":
        case "sepia":
          slider.value = 0;
          slider.min = 0;
          slider.max = 1;
          slider.step = 0.01;
          slider.setAttribute("data-unit", "");
          break;
        case "hue-rotate":
          slider.value = 0;
          slider.min = 0;
          slider.max = 360;
          slider.step = 1;
          slider.setAttribute("data-unit", "deg");
          break;
        default:
          console.error("Unknown filter set");
      }
    }
    
    function setDiv(filter) {
      const unit = slider.getAttribute("data-unit");
      const offset = `${Math.round(slider.value)}${unit}`;
      const radius = `${Math.round(Math.abs(slider.value / 2))}${unit}`;
      divElem.style.filter =
        filter === "drop-shadow"
          ? `${selectElem.value}(${offset} ${offset} ${radius})`
          : `${selectElem.value}(${slider.value}${unit})`;
    
      updateOutput();
      updateCurValue();
    }
    
    function updateOutput() {
      output.textContent = slider.value;
    }
    
    function updateCurValue() {
      curValue.textContent = `filter: ${divElem.style.filter}`;
    }
    
    setSlider(selectElem.value);
    setDiv(selectElem.value);
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# typedef-filter-function](https://drafts.csswg.org/filter-effects/#typedef-filter-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function#see_also)

-------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")