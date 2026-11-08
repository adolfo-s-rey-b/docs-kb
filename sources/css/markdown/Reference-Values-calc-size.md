*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#mdn-search)
    

`calc-size()` CSS function
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/252)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#browser_compatibility)
 carefully before using this in production.

The **`calc-size()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 allows you to perform calculations on [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 values such as `auto`, [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
, and [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
; this is not supported by the regular [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function.

`calc-size()` return values can also be [interpolated](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
, enabling size keyword values to be used in [animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 and [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
. In effect, including `calc-size()` in a property value automatically applies [`interpolate-size: allow-keywords`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
 to the selection.

Note however that `interpolate-size` is inherited, therefore applying it to an element enables interpolation of intrinsic size keywords for every property applied to that element and its children. As a result, `interpolate-size` is the preferred solution for enabling intrinsic size animations. You should only use `calc-size()` to enable intrinsic size animations if they also require calculations.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#syntax)

---------------------------------------------------------------------------------------------

css

    /* Pass a value through calc-size() */
    calc-size(auto, size)
    calc-size(fit-content, size)
    
    /* Perform a calculation */
    calc-size(min-content, size + 100px)
    calc-size(fit-content, size / 2)
    
    /* Calculation including a function */
    calc-size(auto, round(up, size, 50px))
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#parameters)

The `calc-size()` function's syntax is as follows:

calc-size(<calc-size-basis>, <calc-sum>)

The parameters are:

[`<calc-size-basis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#calc-size-basis)

The value (most commonly an intrinsic size) that you want to perform a calculation on.

[`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)

An expression that defines the calculation to be performed on the `<calc-size-basis>`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#return_value)

Returns a value equal to the `<calc-size-basis>` modified by the `<calc-sum>` expression. As the `<calc-size-basis>` value is an intrinsic size value, the return value is a modified intrinsic size value that behaves like the intrinsic size value input into the function.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#description)

-------------------------------------------------------------------------------------------------------

Certain browser layout algorithms have special behaviors for intrinsic sizing keywords. The `calc-size()` function is explicitly defined to represent an intrinsic size rather than a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, thereby enforcing correctness. `calc-size()` enables calculations to be performed on intrinsic size values in a safe, well-defined manner.

### [Valid values for the first argument (`<calc-size-basis>`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#valid_values_for_the_first_argument_calc-size-basis)

The first `calc-size()` argument can be one of the following intrinsic values:

*   `auto`
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
    
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    
*   `content` (for containers sized using [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    ).

There are also a few special values that this argument can take:

*   A nested `calc-size()` value. This isn't something you'd be likely to do very often, but it is available ensuring using a [CSS variable](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
     as the `<calc-size-basis>` will always work, provided the variable is a valid value for the property `calc-size()` is being set on. So for example, this will work:
    
    css
    
        section {
          height: calc-size(calc-size(max-content, size), size + 2rem);
        }
        
    
    As will this:
    
    css
    
        :root {
          --intrinsic-size: calc-size(max-content, size);
        }
        
        section {
          height: calc-size(var(--intrinsic-size), size + 2rem);
        }
        
    
*   Another `<calc-sum>`, with the same restrictions as the `<calc-sum>` specified for the second argument, except that the `size` keyword cannot be included. You likely will not do this, as you are no longer doing a calculation on an intrinsic size value, but if a custom property value is a `<calc-sum>`, the function will still work. For example, this will work directly or if you use a custom property with a value of `300px + 2rem`:
    
    css
    
        section {
          height: calc-size(300px + 2rem, size / 2);
        }
        
    
*   The keyword `any`, which represents an unspecified definite size. In this case, the `size` keyword cannot be included in the second argument, and the `calc-size()` returns the result of the second argument calculation. For example:
    
    css
    
        section {
          height: calc-size(any, 300px * 1.5); /* Returns 450px */
        }
        
    

Mixing different intrinsic sizes together in the same calculation doesn't work. For example, `max-content - min-content` doesn't make sense. `calc-size()` only allows a single intrinsic size value in each calculation, avoiding this problem.

### [Valid values for the second argument (`<calc-sum>`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#valid_values_for_the_second_argument_calc-sum)

The second `calc-size()` argument is a [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 expression.

In this expression:

*   The keyword `size` represents the `<calc-size-basis>` specified as the first argument.
*   Operands can include `size`, and any value types that make sense in the context.
*   The `+`, `-`, `*`, and `/` operators can be included.
*   Other mathematical functions can be included such as [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    , [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    , or even a nested `calc-size()`.
*   The overall expression must match [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    , and resolve to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    .

### [Enabling animation of intrinsic size values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#enabling_animation_of_intrinsic_size_values)

`calc-size()` return values can be interpolated, enabling animations between a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 value and a `calc-size()` intrinsic size return value.

**Note:** You should avoid animating box model properties if possible, to cut down on layout events and mitigate the resulting impact on performance (see [Critical rendering path > Layout](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path#layout)
).

For example, you could use a [transition](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 to animate a container `width` between `0` and `auto` like so:

css

    section {
      width: 0;
      transition: width ease 1s;
    }
    
    section:hover,
    section:focus {
      width: calc-size(auto, size);
    }
    

In the above case, we are not calculating anything — we are putting `auto` into `calc-size()` and returning it unchanged. The [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
 property makes animations like the above simpler to implement in most cases, especially when there are multiple animations to consider. It is inherited and therefore only needs to be declared once on an ancestor property, meaning we could have transitioned between `0` and `auto` without using `calc-size()`.

The `calc-size()` function should only be used to enable intrinsic size animations if they also require calculations. For example, in the following case we are animating the `width` _and_ applying a calculation to the intrinsic size end state:

css

    section {
      width: 0;
      transition: width ease 1s;
    }
    
    section:hover,
    section:focus {
      width: calc-size(auto, size + 2rem);
    }
    

One case in which `calc-size()` is useful is when you want to animate between an intrinsic size and a modified version of the same intrinsic size. This is not possible with `interpolate-size` and `calc()`. For example, the following [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 definition animates a container `width` between `fit-content` and 70% of the `fit-content`.

css

    @keyframes narrower {
      from {
        width: fit-content;
      }
    
      to {
        width: calc-size(fit-content, size * 0.7);
      }
    }
    

**Note:** Note that `calc-size()` does not enable animating between two different intrinsic size values.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#formal_syntax)

-----------------------------------------------------------------------------------------------------------

<calc-size()> =   
  calc-size( <calc-size-basis> , <calc-sum> )    
  
<calc-size-basis> =   
  <size-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-sum>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<calc-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  any               
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#examples)

-------------------------------------------------------------------------------------------------

### [Basic `calc-size` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#basic_calc-size_usage)

This example shows basic dimension sizing of a container using `calc-size()`

#### HTML

The HTML contains a single [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element that contains some child content.

html

    <section>
      <h2>Favorite quote</h2>
    
      <p>
        Fashion is something so ugly it has to be changed every fifteen minutes.
      </p>
    </section>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    section {
      font-family: "Helvetica", "Arial", sans-serif;
      border: 1px solid black;
    }
    
    h2 {
      margin: 0;
      font-weight: normal;
      font-size: 1.1rem;
      text-align: center;
      letter-spacing: 1px;
    }
    
    p {
      font-size: 0.8rem;
    }
    

In the CSS, we use [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 to center the child elements inside the `<section>`, and set the `width` and `height` of the `<section>` to `calc-size()` functions. The `width` is set equal to `fit-content` plus `6rem`. The `height` is set to `auto` multiplied by two.

css

    section {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    
      width: calc-size(fit-content, size + 6rem);
      height: calc-size(auto, size * 2);
    }
    

The rest of the CSS has been hidden for brevity.

#### Result

We've created some horizontal and vertical space for the text to be centered in, without the use of padding.

### [Basic `calc-size` animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#basic_calc-size_animations)

This example demonstrates how to use `calc-size()` to animate between a specific size and an intrinsic size. The demo features a character badge/"name tag", which can be hovered or focused to reveal information about the character. The reveal is handled by a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 transition between a set length and `max-content`.

#### HTML

The HTML contains a single [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element with [`tabindex="0"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
 set on it so it can receive keyboard focus. The `<section>` contains [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
 and [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 elements, each with their own child content.

html

    <section tabindex="0">
      <header>
        <h2>Chris Mills</h2>
      </header>
      <main>
        <p>Chris is the silent phantom of MDN.</p>
        <ul>
          <li><strong>Height</strong>: 3.03m</li>
          <li><strong>Weight</strong>: 160kg</li>
          <li><strong>Tech Fu</strong>: 7</li>
          <li><strong>Bad Jokes</strong>: 9</li>
        </ul>
      </main>
    </section>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    section {
      font-family: "Helvetica", "Arial", sans-serif;
      width: 175px;
      border-radius: 5px;
      background: #eeeeee;
      box-shadow:
        inset 1px 1px 4px rgb(255 255 255 / 0.5),
        inset -1px -1px 4px rgb(0 0 0 / 0.5);
    }
    
    header {
      padding: 10px;
      border-bottom: 2px solid #cccccc;
    }
    
    main {
      padding: 0.7rem;
    }
    
    h2 {
      margin: 0;
      font-weight: normal;
      font-size: 1.1rem;
      text-align: center;
      letter-spacing: 1px;
    }
    
    p,
    li {
      font-size: 0.8rem;
      line-height: 1.5;
    }
    
    p {
      margin-top: 0;
    }
    

In the CSS, we set the `<section>`'s [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 to `2.5rem` and [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to `hidden` so only the `<header>` is shown by default, then specify a `transition` that animates the `<section>` `height` over 1 second during state changes. Finally, we set the `<section>` `height` to a `calc-size()` function call on [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 and [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
. The function return value is the equivalent of `max-content` + `2rem`.

css

    section {
      height: 2.5rem;
      overflow: hidden;
      transition: height ease 1s;
    }
    
    section:hover,
    section:focus {
      height: calc-size(max-content, size + 2rem);
    }
    

The rest of the CSS has been hidden for brevity.

#### Result

Try hovering over the `<section>` or focusing it via the keyboard — it will animate to its full height + 2rem, revealing all the content with 2rems of extra space at the bottom.

### [Adjusting reading width based on `fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#adjusting_reading_width_based_on_fit-content)

This example shows a container with text inside it, and a button that can be clicked to make the container width narrower or wider depending on reading preference.

#### HTML

The HTML contains a single [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element containing child text content, plus a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 to change the `<section>` width.

html

    <section class="easy-reader">
      <h2>Easy reader</h2>
    
      <p>
        Eius velit aperiam ipsa. Deleniti eum excepturi ut magni maxime maxime
        beatae. Dicta aperiam est laudantium ut illum facere qui officiis. Sunt
        deleniti quam id. Quis sunt voluptatem praesentium minima dolorum autem
        consequatur velit.
      </p>
    
      <p>
        Vitae ab incidunt velit aspernatur deleniti distinctio rerum. Et natus sed
        et quos mollitia quia quod. Quae officia ex ea. Ducimus ut voluptatem et et
        debitis. Quidem provident laboriosam exercitationem similique deleniti.
        Temporibus vel veniam mollitia magni unde a nostrum.
      </p>
    
      <button class="width-adjust">Narrower</button>
    </section>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    body {
      width: 600px;
      margin: 0 auto;
    }
    
    section {
      margin-top: 20px;
      font-family: "Helvetica", "Arial", sans-serif;
      background: #eeeeee;
      border: 2px solid #cccccc;
      padding: 0 20px;
      position: relative;
    }
    
    p,
    li {
      font-size: 0.8rem;
      line-height: 1.5;
    }
    
    button {
      position: absolute;
      top: 2px;
      right: 2px;
    }
    

In the CSS, we set the `<section>`'s [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 to a default of [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
. We then define two sets of [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
, `narrower`, which animates from `fit-content` to 70% of `fit-content` (calculated using `calc-size()`), and `wider`, which animates the same values but in the opposite direction. Finally, we attach those animations to two classes — `.narrower` and `.wider`. Each animation is defined to last one second and to keep the final state applied once finished.

css

    section {
      width: fit-content;
    }
    
    @keyframes narrower {
      from {
        width: fit-content;
      }
    
      to {
        width: calc-size(fit-content, size * 0.7);
      }
    }
    
    @keyframes wider {
      from {
        width: calc-size(fit-content, size * 0.7);
      }
    
      to {
        width: fit-content;
      }
    }
    
    .narrower {
      animation: narrower 1s ease forwards;
    }
    
    .wider {
      animation: wider 1s ease forwards;
    }
    

The rest of the CSS has been hidden for brevity.

#### JavaScript

The JavaScript provides a narrower/wider toggle that applies the relevant class to the `<section>` when the button is clicked:

js

    const widthAdjustBtn = document.querySelector(".width-adjust");
    const easyReader = document.querySelector(".easy-reader");
    
    widthAdjustBtn.addEventListener("click", () => {
      if (easyReader.classList.length === 1) {
        easyReader.classList.add("narrower");
        widthAdjustBtn.textContent = "Wider";
      } else if (easyReader.classList.contains("wider")) {
        easyReader.classList.replace("wider", "narrower");
        widthAdjustBtn.textContent = "Wider";
      } else if (easyReader.classList.contains("narrower")) {
        easyReader.classList.replace("narrower", "wider");
        widthAdjustBtn.textContent = "Narrower";
      }
    });
    

#### Result

Try clicking the `<button>` a few times to adjust the `<section>` between the wide and narrow reading width, achieved by manipulating the `width` based on the `fit-content` value.

### [Using a function inside the `calc-size()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#using_a_function_inside_the_calc-size_function)

As mentioned earlier, it is possible to use another function inside `calc-size()`. This example sets [`field-sizing: content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)
 on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements to make them as wide as the entered content, and then uses a [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
 function inside `calc-size()` to ensure that the `<input>`s are at least a minimum size, and only start to grow when the entered text becomes wider than that size — by being set to `fit-content` plus `20px`.

#### HTML

The HTML contains a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element containing three textual `<input>` types. Each `<input>` has a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 associated with it to make the form accessible, and a [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)
 applied to stop entered values getting long enough to break the form layout.

html

    <form>
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" maxlength="48" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" maxlength="48" />
      </div>
      <div>
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" maxlength="60" />
      </div>
    </form>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    body {
      width: 600px;
      margin: 0 auto;
    }
    
    form {
      margin-top: 20px;
      padding: 20px;
      font-family: "Helvetica", "Arial", sans-serif;
      background: #eeeeee;
      border: 2px solid #cccccc;
    }
    
    div {
      display: flex;
      align-items: center;
    }
    
    div:not(div:last-child) {
      margin-bottom: 20px;
    }
    

In the CSS, we set the `width` of the `<label>` elements to `100px`. We set `field-sizing: content` on the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements to make them as wide as the entered content — by default they would no width because nothing would be entered into them. To counteract this, we set their `width` values to `calc-size(fit-content, max(100px, size + 20px))`. This means that they are a minimum of `100px` wide, even with no value entered. When an entered value becomes wider than `100px`, their `width` changes to `fit-content` plus `20px`, which means they start to grow with the content size but keep a `20px` gap on the right-hand side.

css

    label {
      width: 100px;
    }
    
    input {
      field-sizing: content;
      width: calc-size(fit-content, max(100px, size + 20px));
    }
    

The rest of the CSS has been hidden for brevity.

#### Result

Try entering some text inside the form inputs, and see how they grow when the values start to become as wide as the minimum width enforced by the `max()` function.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# calc-size](https://drafts.csswg.org/css-sizing-4/#calc-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size#see_also)

-------------------------------------------------------------------------------------------------

*   [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
    
*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    
*   [Animate to height: auto; (and other intrinsic sizing keywords) in CSS](https://developer.chrome.com/docs/css-ui/animate-to-height-auto "External link (opens in new tab)")
     on developer.chrome.com (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/calc-size/index.md?plain=1 "Folder: en-us/web/css/reference/values/calc-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")