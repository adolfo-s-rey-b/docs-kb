*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#mdn-search)
    

`animation` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property applies an animation between styles. It is a shorthand for [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
, [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
, [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
, [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
, [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
, [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
, [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
, [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
, and [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#try_it)

-------------------------------------------------------------------------------------------------

    animation: 3s ease-in 1s infinite reverse both running slide-in;
    

    animation: 3s linear 1s infinite running slide-in;
    

    animation: 3s linear 1s infinite alternate slide-in;
    

    animation: 0.5s linear 1s infinite alternate slide-in;
    

    <section class="flex-column" id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      background-color: #1766aa;
      margin: 20px;
      border: 5px solid #333333;
      width: 150px;
      height: 150px;
      border-radius: 50%;
    }
    
    @keyframes slide-in {
      from {
        margin-left: -20%;
      }
      to {
        margin-left: 100%;
      }
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    
*   [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    
*   [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    
*   [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    
*   [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    
*   [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    
*   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    
*   [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    
*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    

### [Reset-only sub-properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#reset-only_sub-properties)

This property resets the following CSS properties to their initial values:

*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    
*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   `animation-delay-end`
*   [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    
*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Duration | easing-function | delay |
    iteration-count | direction | fill-mode | play-state | name */
    animation: 3s ease-in 1s 2 reverse both paused slide-in;
    
    /* Duration | easing-function | delay | name */
    animation: 3s linear 1s slide-in;
    
    /* Duration | name */
    animation: 3s slide-in;
    
    /* Multiple animations */
    animation:
      3s linear slide-in,
      3s ease-out 5s slide-out;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#values)

This property is specified as a comma-separated list of `<animation>` values, with each value being a space-separated list of the following values:

[`<keyframes-name>` or `none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#keyframes-name)

The name of a [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rules that specifies the animation to apply to an element. The initial value for [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 is `none`.

[`<animation-duration>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#animation-duration)

Determines the length of time that an animation takes to complete one cycle. The value must be one of those available in [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
. The initial value is `0s`.

[`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#easing-function)

Determines the type of transition. The value must be one of those available in [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
. The initial value is `ease`.

[`<animation-delay>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#animation-delay)

Determines the amount of time to wait from applying the animation to an element before beginning to perform the animation. The value must be one of those available in [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
. The initial value is `0s`.

[`<single-animation-direction>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#single-animation-direction)

The direction in which the animation is played. The value must be one of those available in [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
. The initial value for [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
 is `normal`.

[`<single-animation-iteration-count>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#single-animation-iteration-count)

The number of times the animation is played. The value must be one of those available in [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
. The initial value for [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
 is `1`.

[`<single-animation-fill-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#single-animation-fill-mode)

Determines how styles should be applied to the animation's target before and after its execution. The value must be one of those available in [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
. The initial value for [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 is `none`.

[`<single-animation-play-state>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#single-animation-play-state)

Determines whether the animation is playing or not. The value must be one of those available in [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
. The initial value for [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
 is `running`.

[`<single-animation-timeline>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#single-animation-timeline)

Determines the timeline used to control the progress of the animation. The value must be one of those available in [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
. The initial value is `auto`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#description)

-----------------------------------------------------------------------------------------------------------

The `animation` property is specified as one or more single animations, separated by commas. Each `animation` within the comma-separated list of animations sets the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
, [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
, [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
, [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
, [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
, [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
, [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
, [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
, and [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
. If any of the components are not included in an `animation` declaration, the component value is set to the component's initial value.

**Note:** The `animation` shorthand property resets the [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
, [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
 and [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 properties to their initial values; `normal`, `normal` and `none`, respectively. These reset-only sub-properties cannot be set in the `animation` shorthand, and including them invalidates the entire declaration. Because the `animation` declaration sets each of these properties to their initial values, they must either be declared after any `animation` shorthand declarations or with greater [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

### [animation-name](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#animation-name)

The `<animation-name>` component of each animation is the name for the animation, which may be `none`, a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, or a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
. The initial value of `animation-name` is `none`, meaning if no `animation-name` value is declared in the `animation` shorthand property, no animation is applied to any of the properties.

The order of other values within an animation definition is important for distinguishing an [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 value from other values. If a value in the `animation` shorthand can be parsed as a value for an animation property other than `animation-name`, then the value will be applied to that property first and not to `animation-name`. For this reason, the recommended practice is to specify a value for `animation-name` as the last value in a list of values when using the `animation` shorthand; this holds true even when you specify multiple, comma-separated animations using the `animation` shorthand.

### [Time values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#time_values)

Each animation can include zero, one, or two occurrences of the [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 value. The order of time values within each animation definition is important: the first value that can be parsed as a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 is assigned to the [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
, and the second one is assigned to [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
.

When no `animation-duration` value is specified in the `animation` shorthand property, the duration defaults to `0s`. In this case, the animation will still occur (the [`animationStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event)
 and [`animationEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event)
 events will be fired), but no animation will be visible to the user.

### [animation-timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#animation-timeline)

If no `<animation-timeline>` is included in the `animation` shorthand, the shorthand declaration will reset any previously-declared `animation-timeline` values to `auto`, which sets the timeline to the default [`documentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
.

If an `<animation-timeline>` value is included, but the user-agent doesn't support `<animation-timeline>` values within the shorthand, the entire `animation` declaration is invalid and ignored. For this reason, when creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, you need to declare the `animation-timeline` property after declaring any `animation` shorthand for it to take effect.

Alternatively, the `<animation-timeline>` can be set within the `animation` shorthand within a CSS [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 block, such as:

css

    @supports (animation: view()) {
      /* CSS for browsers supporting <animation-timeline> within `animation` shorthand */
    }
    

### [animation-fill-mode and new stacking contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#animation-fill-mode_and_new_stacking_contexts)

In the case of the `animation-fill-mode` [forwards](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#forwards)
 value, animated properties behave as if included in a set [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
 property value. If a new stacking context is created during the animation, the target element retains the stacking context after the animation has finished.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#accessibility)

---------------------------------------------------------------------------------------------------------------

Blinking and flashing animation can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD). Additionally, certain kinds of motion can be a trigger for vestibular disorders, epilepsy, and migraine and scotopic sensitivity.

Consider providing a mechanism for pausing or disabling animation as well as using the [reduced motion `@media` query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 to create a complementary experience for users who have expressed a preference for reduced animated experiences.

*   [Designing Safer Web Animation For Motion Sensitivity](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/ "External link (opens in new tab)")
     via A List Apart (2015)
*   [An Introduction to the Reduced Motion Media Query](https://css-tricks.com/introduction-reduced-motion-media-query/ "External link (opens in new tab)")
     via CSS-Tricks (2017)
*   [Responsive Design for Motion](https://webkit.org/blog/7551/responsive-design-for-motion/ "External link (opens in new tab)")
     via WebKit (2017)
*   [Understanding WCAG, Guideline 2.2 — Enough Time: Provide users enough time to read and use content](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.2_%e2%80%94_enough_time_provide_users_enough_time_to_read_and_use_content)
    
*   [Understanding WCAG Success Criterion 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide "External link (opens in new tab)")
     via W3C (2026)

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)<br>    : `none`<br>*   [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)<br>    : `0s`<br>*   [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)<br>    : `ease`<br>*   [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)<br>    : `0s`<br>*   [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)<br>    : `1`<br>*   [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)<br>    : `normal`<br>*   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)<br>    : `none`<br>*   [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)<br>    : `running`<br>*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)<br>    : `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)<br>    : as specified<br>*   [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)<br>    : as specified<br>*   [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)<br>    : as specified<br>*   [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)<br>    : as specified<br>*   [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)<br>    : as specified<br>*   [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)<br>    : as specified<br>*   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)<br>    : as specified<br>*   [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)<br>    : as specified<br>*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)<br>    : a list, each item either a case-sensitive CSS identifier or the keywords `none`, `auto` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#formal_syntax)

---------------------------------------------------------------------------------------------------------------

animation =   
  <single-animation>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation> =   
  [<'animation-duration'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
              [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <easing-function>                   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <'animation-delay-start'>           [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <single-animation-iteration-count>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <single-animation-direction>        [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <single-animation-fill-mode>        [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <single-animation-play-state>       [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <keyframes-name> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
         [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <single-animation-timeline>           
  
[<animation-duration>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<time \[0s,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<easing-function>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 =   
  <linear-easing-function>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier-easing-function>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <step-easing-function>            
  
<animation-delay-start> =   
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-iteration-count> =   
  infinite        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
  
<single-animation-direction> =   
  normal             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  reverse            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alternate          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alternate-reverse    
  
<single-animation-fill-mode> =   
  none       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  forwards   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  backwards  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both         
  
<single-animation-play-state> =   
  running  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  paused     
  
<keyframes-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
          
  
<single-animation-timeline> =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scroll()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <view()>          
  
<linear-easing-function> =   
  linear      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <linear()>    
  
<cubic-bezier-easing-function> =   
  ease              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-out          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in-out       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier()>    
  
<step-easing-function> =   
  step-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  step-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <steps()>     
  
[<scroll()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 =   
  scroll( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <scroller> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <axis> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<view()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 =   
  view( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <axis> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'view-timeline-inset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<linear()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
 =   
  linear( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[{0,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cubic-bezier()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
 =   
  cubic-bezier( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,1\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<steps()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
 =   
  steps( <integer> , <step-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<scroller> =   
  root     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nearest  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self       
  
[<axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         
  
[<view-timeline-inset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<step-position> =   
  jump-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-none   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-both   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#examples)

-----------------------------------------------------------------------------------------------------

**Note:** Animating [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 properties is discouraged as it leads to layout reflow and repaints. Animating any box model property is inherently CPU-intensive; consider animating the [transform](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 property instead.

### [Basic usage: a sunrise](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#basic_usage_a_sunrise)

In this example, we demonstrate basic usage of the `animation` shorthand by animating a yellow sun across a light blue sky. The sun rises to the center of the viewport and then falls out of sight.

#### HTML

We include a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element to represent our sun.

html

    <div class="sun"></div>
    

#### CSS

We start by creating the sun and the sky. The sky is the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 of the HTML document. We hide any content that is outside the viewport, which in our case will be any part of the sun below the horizon, by setting the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to hidden. We also use the [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 property to center the sun in the background. We make the sun yellow, declare its [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 to be the height of the viewport (`100vh`), and set its width to equal its height by setting the [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 to `1`. We turn the square `<div>` into a circle using the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 property.

css

    :root {
      overflow: hidden;
      background-color: lightblue;
      display: flex;
      justify-content: center;
    }
    
    .sun {
      background-color: yellow;
      border-radius: 50%;
      height: 100vh;
      aspect-ratio: 1;
      animation: 4s linear 0s infinite alternate sunrise;
    }
    

Next, we define some animation [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 that will push the element on which they are applied down past the viewport and then return the element to its default position using [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
:

css

    @keyframes sunrise {
      from {
        transform: translateY(110vh);
      }
      to {
        transform: translateY(0);
      }
    }
    

The last step is to apply the animation! We use the `animation` shorthand property to apply the `sunrise` keyframe animation to the `.sun` `<div>`. The animation is set to play for infinite iterations, with each one lasting 4 seconds; the animation direction alternates with each iteration:

css

    .sun {
      animation: 4s linear 0s infinite alternate sunrise;
    }
    

#### Results

### [Applying multiple animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#applying_multiple_animations)

This example demonstrates applying multiple animations to a single element. Expanding on the previous example, with a sun that rises and falls on a light blue background, here we will gradually rotate the sun through a rainbow of colors. The timing of the sun's position and color are independent.

    <div class="sun"></div>
    

    :root {
      overflow: hidden;
      background-color: lightblue;
      display: flex;
      justify-content: center;
    }
    
    .sun {
      background-color: yellow;
      border-radius: 50%;
      height: 100vh;
      aspect-ratio: 1 / 1;
    }
    
    @keyframes sunrise {
      from {
        transform: translateY(110vh);
      }
      to {
        transform: translateY(0);
      }
    }
    

We include the same HTML and CSS as in the previous example, and add a second set of animation `@keyframes` to apply a [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 that rotates the hue through all possible values using the [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
 filter function:

css

    @keyframes psychedelic {
      from {
        filter: hue-rotate(0deg);
      }
      to {
        filter: hue-rotate(360deg);
      }
    }
    

We then apply the two animations to our sun. Multiple animations are separated by commas, and each animation's parameters are set independently:

css

    .sun {
      animation:
        4s linear 0s infinite alternate sunrise,
        24s linear 0s infinite psychedelic;
    }
    

#### Results

### [Cascading multiple animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#cascading_multiple_animations)

This example demonstrates what happens when multiple animations define values for the same property. This example expands upon the [basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#basic_usage_a_sunrise)
 example, with two animations applied that both set a [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 value.

    <div class="sun"></div>
    

    :root {
      overflow: hidden;
      background-color: lightblue;
      display: flex;
      justify-content: center;
    }
    
    .sun {
      background-color: yellow;
      border-radius: 50%;
      height: 100vh;
      aspect-ratio: 1 / 1;
    }
    

We use the same HTML and CSS as in the first example, including the original `sunrise` animation, and a second animation named `bounce`. The two animations declare values for the same property:

css

    @keyframes sunrise {
      from {
        transform: translateY(110vh);
      }
      to {
        transform: translateY(0);
      }
    }
    
    @keyframes bounce {
      from {
        transform: translateX(-50vw);
      }
      to {
        transform: translateX(50vw);
      }
    }
    

We apply both animations to the sun. When two animations apply different values to the same property, animations declared later in the cascade override previously-declared animations. In this case, the `transform` value on the `bounce` animation "wins" the [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#css_animations_and_the_cascade)
, and overrides the transform set by `sunrise`, so the sun will only move horizontally.

css

    .sun {
      animation:
        4s linear 0s infinite alternate sunrise,
        4s linear 0s infinite alternate bounce;
    }
    

#### Results

The sun bounces between the left- and right-hand sides of the viewport. The sun remains in the viewport even though the `sunrise` animation is defined. The `sunrise` animation's transform property is overridden by the bounce animation.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation](https://drafts.csswg.org/css-animations/#animation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation#see_also)

-----------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4aba58b4ad2745a73054f60b6d649d8e29b7b44d%0A*+Document+last+modified%3A+2026-10-05T11%3A36%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")