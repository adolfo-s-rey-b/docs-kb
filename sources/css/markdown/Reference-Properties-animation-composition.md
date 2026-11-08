*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#mdn-search)
    

`animation-composition` CSS property
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-composition`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the [composite operation](https://developer.mozilla.org/en-US/docs/Glossary/Composite_operation)
 to use when multiple animations affect the same property simultaneously.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Single animation */
    animation-composition: replace;
    animation-composition: add;
    animation-composition: accumulate;
    
    /* Multiple animations */
    animation-composition: replace, add;
    animation-composition: add, accumulate;
    animation-composition: replace, add, accumulate;
    
    /* Global values */
    animation-composition: inherit;
    animation-composition: initial;
    animation-composition: revert;
    animation-composition: revert-layer;
    animation-composition: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#values)

This property is specified as one or more comma-separated keyword values:

[`replace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#replace)

The effect value overrides the underlying value of the property. This is the default value.

[`add`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#add)

The effect value builds on the underlying value of the property. This operation produces an additive effect. For animation types where the addition operation is not commutative, the order of the operands is the underlying value followed by the effect value.

[`accumulate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#accumulate)

The effect and underlying values are combined. For animation types where the addition operation is not commutative, the order of the operands is the underlying value followed by the effect value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#description)

-----------------------------------------------------------------------------------------------------------------------

Each property that is targeted by the [@keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rule is associated with an effect stack. The value of the effect stack is calculated by combining the _underlying value_ of a property in a CSS style rule with the _effect value_ of that property in the keyframe. The `animation-composition` property helps to specify how to combine the underlying value with the effect value.

For example, in the CSS below, `blur(5px)` is the underlying value, and `blur(10px)` is the effect value. The `animation-composition` property specifies the operation to perform to produce the final effect value after compositing the effect of the underlying value and the effect value.

css

    .icon:hover {
      filter: blur(5px);
      animation: 3s infinite pulse;
      animation-composition: add;
    }
    
    @keyframes pulse {
      0% {
        filter: blur(10px);
      }
      100% {
        filter: blur(20px);
      }
    }
    

Consider different values for the `animation-composition` property in the above example. The final effect value in each of those cases will be calculated as explained below:

*   With `replace`, `blur(10px)` will replace `blur(5px)` in the `0%` keyframe. This is the default behavior of the property.
*   With `add`, the composite effect value in the `0%` keyframe will be `blur(5px) blur(10px)`.
*   With `accumulate`, the composite effect value in `0%` keyframe will be `blur(15px)`.

**Note:** A composite operation can also be specified in a keyframe. In that case, the specified composite operation is used for each property first within that keyframe and then on each property in the next keyframe.

### [Multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#multiple_values)

When you specify multiple comma-separated values on an `animation-*` property, they will be applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. If the number of animations and compositions differ, the values listed in the `animation-composition` property will cycle from the first to the last `animation-name`, looping until all the animations have an assigned `animation-composition` value. For more information, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `replace` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

animation-composition =   
  <single-animation-composition>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-composition> =   
  replace     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  add         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  accumulate    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#examples)

-----------------------------------------------------------------------------------------------------------------

### [Understanding the animation-composition values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#understanding_the_animation-composition_values)

The example below shows the effect of different `animation-composition` values side-by-side.

#### HTML

html

    <div class="container">
      replace
      <div id="replace" class="target"></div>
    </div>
    <div class="container">
      add
      <div id="add" class="target"></div>
    </div>
    <div class="container">
      accumulate
      <div id="accumulate" class="target"></div>
    </div>
    

#### CSS

    body {
      display: flex;
      flex-wrap: wrap;
      gap: 3px;
    }
    
    .container {
      flex: 1;
      min-width: 200px;
      height: 200px;
      background: lightblue;
      display: inline-block;
      text-align: center;
    }
    
    .target {
      width: 20px;
      height: 50px;
      background: green;
      border-radius: 10px;
      margin: 20px 0;
    }
    

css

    @keyframes slide {
      50% {
        transform: translateY(30px);
      }
      100% {
        transform: translateX(150px);
      }
    }
    
    .target {
      transform: translateX(30px) rotate(45deg);
      animation: slide 5s linear infinite;
    }
    #replace {
      animation-composition: replace;
    }
    #add {
      animation-composition: add;
    }
    #accumulate {
      animation-composition: accumulate;
    }
    

#### Result

The underlying value for the `transform` property in all cases is `translateX(30px) rotate(45deg)`. The different `animation-composition` values' effects are as follows:

*   With `replace`, the `transform` property in each keyframe entirely replaces the underlying `transform` property set on the animated element. The final effect value for the `transform` property at the `50%` keyframe is `translateY(30px)` (no `rotate` or `translateX`); at the `100%` keyframe, it is `translateX(150px)` (no `rotate` or `translateY`).
    
    The target starts at `transform: translateX(30px) rotate(45deg)` and effectively animates to `transform: translateY(30px)`, then to `transform: translateX(150px)`.
    
*   With `add`, the final effect value at each keyframe is the underlying `transform` value with the effect value placed immediately after it.
    
    Therefore, the target starts at `transform: translateX(30px) rotate(45deg)` and effectively animates first to `transform: translateX(30px) rotate(45deg) translateY(30px)` (which is `30px` "downwards" on the rotated Y-axis), and then to `transform: translateX(30px) rotate(45deg) translateX(150px)`. Since the additive operation is relative to the underlying `transform` and not the previous keyframe, there is no `translateY(30px)` at `100%`, placing the element `150px` along the rotated X-axis from the original position.
    
*   With `accumulate`, the final effect value is the keyframe's effect `transform` combined with the underlying original. At `50%`, `translateY(30px)` combines with the original `translateX(30px)` into a single translation (`translate(30px, 30px)`). At `100%`, the `translateX(150px)` combines with the original `translateX(30px)` to create `translateX(180px)`.
    
    Therefore, the target starts at `transform: translateX(30px) rotate(45deg)` and effectively animates first to `transform: translate(30px, 30px) rotate(45deg)`, and then to `transform: translateX(180px) rotate(45deg)`.
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 2  <br>\# animation-composition](https://drafts.csswg.org/css-animations-2/#animation-composition) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [Composite property of KeyFrameEffect](https://developer.mozilla.org/en-US/docs/Web/API/KeyframeEffect/composite)
    
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-composition/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-composition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-composition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-composition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-composition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-composition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd4dc9d899ebec0e9c22a5bb9229f39f33457d8df%0A*+Document+last+modified%3A+2026-07-24T10%3A26%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")