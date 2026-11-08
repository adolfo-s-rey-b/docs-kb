*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#mdn-search)
    

`random()` CSS function
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/514)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`random()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 generates a random value within a specified range, optionally limiting the possible values to step size intervals between those limits. It can be used when specifying a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, or [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 within a property value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#try_it)

------------------------------------------------------------------------------------------

    <div class="box"></div>
    

    .box {
      rotate: random(property-scoped, 0deg, 360deg);
      width: random(property-scoped, 50px, 300px);
      background-color: hsl(random(property-scoped, 0, 360) 50% 50%);
      height: random(property-scoped, 50px, 300px);
    }
    
    @supports not (order: random(1, 2)) {
      body::before {
        content: "Your browser doesn't support the random() function.";
      }
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#syntax)

------------------------------------------------------------------------------------------

css

    /* Basic usage */
    random(0, 100)
    random(10px, 500px)
    random(0deg, 360deg)
    
    /* With step interval */
    random(0, 100, 10)
    random(0rad, 1turn, 30deg)
    
    /* With <random-key> */
    random(auto, 0, 360)
    random(element-scoped, 0s, 5s)
    random(property-scoped, 0s, 5s)
    random(property-index-scoped, 0s, 5s)
    random(--unique-base, 400px, 100px)
    random(fixed 0.5, 1em, 40vw)
    random(--unique-base property-scoped, 100dpi, 300dpi)
    
    /* With <random-key> and step interval */
    random(property-scoped, 0deg, 360deg, 45deg)
    random(--my-base, 1em, 3rem, 2px)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#parameters)

The `random(seed, min, max, step)` function accepts two to four comma-separated expressions as its parameters.

[`<random-key>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#random-key)

Controls which `random()` functions in the document will share a random base value, or _seed_, and which will get distinct values. Specified as one of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#auto)

The `auto` value is the default and is what is applied if the `<random-key>` is excluded. This random function generates independent random values. The random cache name, and thus the result, varies across every `random()` instance in a multi-component value, across different properties, and across different elements. This is equivalent to specifying `element-scoped property-index-scoped`.

[`element-scoped`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#element-scoped)

Adds an element-specific identifier to the random cache name, so if applied over multiple properties (e.g., `width` and `height`) both properties use the same value, but each element (e.g., `<div>`) gets a different random values.

[`property-scoped`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#property-scoped)

Adds the property name to the random cache name, so if applied over multiple properties (e.g., `width` and `height`) both properties gets a different random value, but each element (e.g., `<div>`) uses the same random values.

[`property-index-scoped`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#property-index-scoped)

Adds the property name and the index of the `random()` function among all random functions used in the same property value to the random cache name, so multiple instances in the same declaration each get different random values.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

A custom name for the random cache key (e.g., `--my-random-key`). When used alone, the same random base value is shared across all elements and properties that use the same identifier. When combined with a `*-scoped` keyword, the sharing behavior is determined by the keyword.

[`fixed <number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#fixed_number)

Bypasses the random cache name and uses the `<number>` — between `0` and `1`, inclusive of 0, exclusive of 1 — as the seed's value.

[`<calc-sum>, <calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#calc-sum_calc-sum)

Specified as `<number>`, `<dimension>`, or `<percentage>` values, or calculations resolving to one of these types, defining the minimum and maximum values, respectively. Both values must be resolvable to the same [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
. If the maximum is less than the minimum, the function will return the first `<calc-sum>` value.

[`<calc-sum>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#calc-sum)

Specifies the step interval. If present and of the same data type as the minimum and maximum `<calc-sum>` values, it defines the return value to be the minimum value or at increments of the step value from the minimum value, up to the maximum value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#return_value)

Returns a random `<number>`, `<dimension>`, or `<percentage>` between the minimum and maximum range values, inclusive, in the same type as the `<calc-sum>` parameters.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#description)

----------------------------------------------------------------------------------------------------

The `random(SEED, MIN, MAX, STEP)` function specifies the minimum and maximum values and optional step increments, starting at the minimum value. The function generates a random result within the range specified. The seed, an [optional `<random-key>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#random-key)
 parameter, enables sharing or varying random base values across different properties and elements.

The minimum, maximum and step values specified must be of the same data type for the function to be valid. While the units in the two to three `<calc-sum>` parameters don't need to be the same, they do need to be of the same data type, such as [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, or [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
, to be valid.

### [Random base value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#random_base_value)

The random base value works like a [seed for randomness](https://developer.mozilla.org/en-US/docs/Glossary/RNG)
. It's a starting number that is used to generate the final random result. When two `random()` functions share the same base value, their results vary together in a predictable pattern. When they have different base values, their results are completely independent of each other.

The optional first `<random-key>` parameter controls how the random base value is shared. It can be `auto`, a scope keyword (`element-scoped`, `property-scoped`, or `property-index-scoped`), a custom [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
, `fixed <number>`, or a `<dashed-ident>` paired with a scope keyword.

#### Scope keywords

Used on their own, the scope keywords control sharing without a custom name:

*   `property-scoped` shares a base value across all elements, per property.
*   `element-scoped` gives each element its own base value, per property.
*   `property-index-scoped` works like `property-scoped`, but also separates `random()` calls by position within a shorthand.

The `property-scoped` keyword makes `.a`, `.b`, and `.c` identical rectangles, since every element gets the same `width` value and the same `height` value:

css

    .a,
    .b,
    .c {
      width: random(property-scoped, 10px, 200px);
      height: random(property-scoped, 10px, 200px);
    }
    

The `element-scoped` values would give each element its own independently sized `width` value and `height` value.

The `property-index-scoped` keyword is useful in shorthands, where each position needs its own shared value:

css

    .a,
    .b,
    .c {
      margin: random(property-index-scoped, 5px, 40px)
        random(property-index-scoped, 5px, 40px)
        random(property-index-scoped, 5px, 40px)
        random(property-index-scoped, 5px, 40px);
    }
    

All three elements get the same top margin, the same right margin, and so on, but the four margin values differ from each other.

#### Custom names

A `<dashed-ident>` (e.g., `--custom-name`) used alone shares its base value globally: any `random()` call anywhere in the document with the same identifier gets the same result. This makes `.a`, `.b`, and `.c` identical squares, since every `width` and `height` resolves to the same value:

css

    .a,
    .b,
    .c {
      width: random(--custom-name, 10px, 200px);
      height: random(--custom-name, 10px, 200px);
    }
    

Pair a `<dashed-ident>` with a scope keyword to narrow that sharing. `property-scoped` keeps it global across elements but separates it by property:

css

    .a,
    .b,
    .c {
      width: random(--custom-name property-scoped, 10px, 200px);
      height: random(--custom-name property-scoped, 10px, 200px);
    }
    

`element-scoped` instead keeps `width` and `height` linked within each element, but gives each element its own value, so `.a`, `.b`, and `.c` become squares of different sizes:

css

    .a,
    .b,
    .c {
      width: random(--custom-name element-shared, 10px, 200px);
      height: random(--custom-name element-shared, 10px, 200px);
    }
    

#### Automatic behavior

When the first parameter is omitted, or explicitly set to `auto`, an ident is auto-generated from the property name and position. This behavior can cause some unexpected random base value sharing.

css

    .foo {
      width: random(100px, 200px);
    }
    .foo:hover {
      width: random(100px, 200px);
    }
    .bar {
      margin: random(1px, 100px) random(1px, 100px);
    }
    .bar:hover {
      margin: random(1px, 100px) random(1px, 100px) random(1px, 100px)
        random(1px, 100px);
    }
    

When the `<random-key>` defaults or is explicitly set to `auto`, the user agent auto-generates a seed name, or _generated value sharing identifier_, following consistent rules based on property name and order. Because of this, `random()` functions can end up with the same seed name and, therefore, the same random base value. In this example, the generated value sharing identifier for the `random()` function in the `width` property value is the same for `.foo` as for `.foo:hover`, so the value won't change between states. Similarly, the first two `random()` functions in both `margin` declarations have the same generated value sharing identifier, meaning the first two values in the `margin` shorthand will be unchanged when hovered; on hover, `bar`'s top and right margins will remain the same, but the bottom and left margins will get independent random values. To get an independent value for each `random()` function, provide a unique [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
.

### [Custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#custom_properties)

As with all CSS functions, when a `random()` function is included within a custom property value, the value remains a function; behaving like a text replacement mechanism, not storing a single return value.

css

    --random-size: random(1px, 100px);
    

In this example, the `--random-size` custom property does not "store" the randomly generated result. When `var(--random-size)` is parsed it is effectively replaced with `random(1px, 100px)`, meaning each use creates a new `random()` function call with its own base value depending on the context in which its used.

This is not true in the case of using `random()` when registering a custom property with [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
. Registered custom properties compute random values and store them.

In this example, as `--defaultSize` is registered, `.a`, `.b`, and `.c` will be squares of equal size, but their colors will be random, as `--random-angle` was not registered:

css

    @property --defaultSize {
      syntax: "<length> | <percentage>";
      inherits: true;
      initial-value: random(100px, 200px);
    }
    :root {
      --random-angle: random(0deg, 360deg);
    }
    .a,
    .b,
    .c {
      background-color: hsl(var(--random-angle) 100% 50%);
      height: var(--defaultSize);
      width: var(--defaultSize);
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#accessibility)

--------------------------------------------------------------------------------------------------------

Because `random()` can generate an unknown value within a range, you don't have full control over what you get. This can lead to inaccessible results. For example, if you use `random()` to generate text color, you could end up with a value that has low contrast with its background. It is important to be mindful of the context in which `random()` is used, ensuring your results are always accessible.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#formal_syntax)

--------------------------------------------------------------------------------------------------------

<random()> =   
  random( <random-key>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <calc-sum> , <calc-sum> , <calc-sum>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<random-key> =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <random-cache-key>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed [<number \[0,1\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<random-cache-key> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
                                      [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  element-scoped                                      [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 property-scoped [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 property-index-scoped [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <random-ua-ident> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<random-ua-ident> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#examples)

----------------------------------------------------------------------------------------------

### [Basic Usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#basic_usage)

In this example, we'll generate random colors for some circular badges to demonstrate the basic usage of the `random()` function.

#### HTML

We include five badges, one using the `desaturated` class and two using the `unique` class.

html

    <div class="badge"></div>
    <div class="badge"></div>
    <div class="badge desaturated"></div>
    <div class="badge unique"></div>
    <div class="badge unique"></div>
    

#### CSS

We render the five badges as circles. We use the `random()` function within an [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 color function to define the [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 of the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
. We set `property-scoped` to share the random base value between the default `badge` and the `desaturated` one, so it is a less saturated version of the same [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
. We then override the `unique` badges to have a truly random `hue` by letting the base value sharing parameter default to `auto`.

css

    .badge {
      display: inline-block;
      width: 5em;
      aspect-ratio: 1/1;
      border-radius: 50%;
      background: hsl(random(property-scoped, 0, 360) 50% 50%);
    }
    .badge.desaturated {
      background: hsl(random(property-scoped, 0, 360) 10% 50%);
    }
    .badge.unique {
      background: hsl(random(0, 360) 50% 50%);
    }
    

    @supports not (order: random(1, 2)) {
      body::before {
        content: "Your browser doesn't support the random() function.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

### [Random value sharing between properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#random_value_sharing_between_properties)

In this example, we create a starry backdrop to demonstrate combining a `<dashed-ident>` with `element-scoped` to share a random base value between properties within each individual element, without sharing it across elements.

#### HTML

We include five particles, all sharing the same class name.

html

    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    

#### CSS

Every particle has the same styles. We use the `random()` function for the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 values to randomly size and position each particle. We pair a `<dashed-ident>` with `element-scoped` for `height` and `width`, so each particle is a circle (its height matches its width) but sized independently of the others. `top` and `left` are left at the default `auto`, so each axis is positioned independently.

css

    body {
      background: black;
    }
    
    .particle {
      border-radius: 50%;
      background: white;
      position: fixed;
      width: random(--particle-size element-scoped, 0.25em, 1em);
      height: random(--particle-size element-scoped, 0.25em, 1em);
      top: random(0%, 100%);
      left: random(0%, 100%);
      animation: move 1s alternate-reverse infinite;
    }
    

    @supports not (order: random(1, 2)) {
      body::before {
        content: "Your browser doesn't support the random() function.";
        color: white;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 5  <br>\# random](https://drafts.csswg.org/css-values-5/#random) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random#see_also)

----------------------------------------------------------------------------------------------

*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [CSS units and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [`Math.random()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
    
*   [Rolling the Dice with CSS random()](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/ "External link (opens in new tab)")
     via webkit.org (2025)
*   [CSS Almanac: random()](https://css-tricks.com/almanac/functions/r/random/ "External link (opens in new tab)")
     via CSS-Tricks.com

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/random/index.md?plain=1 "Folder: en-us/web/css/reference/values/random (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frandom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frandom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frandom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frandom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F74b73e8310d2ecfecd3e4a2aa21e5b54f43d7387%0A*+Document+last+modified%3A+2026-10-09T04%3A07%3A43.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")