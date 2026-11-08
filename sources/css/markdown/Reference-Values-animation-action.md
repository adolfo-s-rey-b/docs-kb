*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#mdn-search)
    

<animation-action>
==================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#browser_compatibility)
 carefully before using this in production.

The **`<animation-action>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 data type represents keyword values that specify how an animation should behave in certain circumstances — for example, how a [triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
 should behave when its trigger is activated and deactivated.

The `<animation-action>` keyword values are used in the following properties:

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#syntax)

----------------------------------------------------------------------------------------------------

The `<animation-action>` enumerated type is specified using one of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#none)

No action is specified for the animation.

[`play`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play_2)

The animation will play, resume (if paused), or restart (if currently finished) in the same direction as its current direction of play.

[`play-forwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-forwards)

As `play`, except that the animation's [`playbackRate`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/playbackRate "playbackRate")
 is adjusted if required (flipping it to positive if negative) so that the animation will play forwards.

[`play-backwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-backwards)

As `play`, except that the animation's `playbackRate` is adjusted if required (flipping it to negative if positive) so that the animation will play in reverse.

[`play-once`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-once_2)

As `play`, except that once the animation has played through all its iterations, it won't be triggered again. Like `play`, if an animation is paused, `play-once` will resume playing it; unlike `play`, it won't replay a finished animation.

[`pause`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#pause)

The animation will pause.

[`replay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#replay)

As `play`, except that the animation is put back to the start.

[`reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#reset)

As `pause`, except that the animation is put back to the start.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#description)

--------------------------------------------------------------------------------------------------------------

The `<animation-action>` type specifies how an animation behaves when certain things happen. For example, when setting an [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 value on an animated element to specify the animation as a triggered animation, the value can include one or two `<animation-action>` values, separated by a space. The first value specifies the animation behavior when its trigger activates, while the optional second value specifies the animation behavior when its trigger deactivates. If you only specify a single value, the animation doesn't change its behavior when its trigger deactivates; it continues with the activation behavior. It has the same effect as setting `none` as the second value.

There are some common patterns to observe:

*   `play-forwards play-backwards` is very common when you want a UI element to "animate in" when it scrolls into view, and then "animate out" again when it scrolls out of view.
*   `play pause` is common for animating an element as it scrolls into view, then pausing the animation as it scrolls out of view.
*   `play-once` is often used on its own, when you want an animation to play only once when it scrolls into view.

The eight `<animation-action>` values provide different animation behaviors. It's important to understand how they behave on their own and the effects that can created by changing trigger activation and deactivation values.

### [Specifying no action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#specifying_no_action)

To specify that no action should occur, use the `none` value.

### [Playing the animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#playing_the_animation)

The `play`, `play-forwards`, `play-backwards`, and `play-once` keyword values all cause the animation to play, but each one specifies a different precise behavior.

#### `play`

Setting `play` will play the animation through all its iterations, as defined by the [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
 property.

If only `play` is set, the animation will play on activation but never deactivate, as a deactivation action is not specified.

css

    animation-trigger: --t play;
    

If `play` is combined with `pause`, `replay` or `reset`, the animation will play on activation, and then `pause`, `replay` or `reset` on deactivation. On subsequent activation, the animation will play again.

css

    animation-trigger: --t play reset;
    

When combining `play` with `play-backwards`, the animation will play on activation, then play backward through all the iterations it previously played forwards through on deactivation:

css

    animation-trigger: --t play play-backwards;
    

While valid, combining `play` with `play-once` is unnecessary, as it behaves the same as `play`. Similarly, combining `play` with `play-forwards` is unnecessary, because `play-forwards` plays the animation in the same direction as `play`, even when [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
 is set to `reverse` or `alternate`.

#### `play-forwards` and `play-backwards`

Setting `play-forwards` and `play-backwards` will play the animation through all its iterations, except that the direction of play will change to forwards or backward, respectively. This is achieved by adjusting the animation's [`playbackRate`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/playbackRate "playbackRate")
; the [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
 value is not affected.

Specifying an activation action of `play-forwards` only has the same effect as specifying `play` only:

css

    animation-trigger: --t play-forwards;
    

Combining `play-forwards` with `play-backwards` causes the animation to play forwards on activation, then play backward through all the iterations it previously played forwards through on deactivation. On subsequent activations, the animation starts playing forwards again.

css

    animation-trigger: --t play-forwards play-backwards;
    

Combining `play-forwards` with `pause`, `replay` or `reset` produces the same effect as `play`: the animation will play on activation, and then `pause`, `replay` or `reset` on deactivation. On subsequent activations, the animation will play again.

css

    animation-trigger: --t play-forwards pause;
    

It doesn't make sense to combine `play-forwards` with `play` or `play-once`, because all of these actions effectively play the animation forwards; doing the same thing on deactivation as on activation has no discernible effect.

Note that using `play-backwards` as an activation action has no effect if the animation is already at the start of its iterations. With the following example, the animation does not play because it is already at the start:

css

    animation-trigger: --t play-backwards;
    

#### `play-once`

Setting `play-once` will play the animation through all its iterations, but only once. If [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
 is set to `infinite`, there is not much difference in effect between `play-once` and `play`/`play-forwards`. However, with `animation-iteration-count` set to a finite number, you will observe the following behavior.

When combining `play-once` with `pause`, the animation will play on activation and then `pause` on deactivation. However, once the animation has played through all its iterations, the animation will not play again on subsequent activations.

css

    animation-trigger: --t play-once pause;
    

If you combine `play-once` with `replay`, the animation will play on activation, then play again from the beginning on deactivation. It won't exceed its iteration count on any playthrough, but it will play again on subsequent deactivations because we reset the animation to the start each time. On subsequent activations, however, the animation will not play again.

css

    animation-trigger: --t play-once replay;
    

If `play-once` is combined with `reset`, the animation plays on activation, then resets to the beginning on deactivation. On subsequent activation, the animation will play again.

css

    animation-trigger: --t play-once reset;
    

If `play-once` is combined with `play-backwards`, the animation plays on activation, then plays backward through all the iterations on deactivation. On subsequent activation, the animation will not play again, but the animation will play backward again on subsequent deactivations.

css

    animation-trigger: --t play-once play-backwards;
    

### [Pausing the animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#pausing_the_animation)

The `pause` value pauses the animation at whatever point it reached in its playback upon activation/deactivation. Using this in combination with other values was discussed earlier, although one case not mentioned was using `pause` as the activation action, for example:

css

    animation-trigger: --t pause play;
    

This has an interesting effect of no playback on activation, but playback on subsequent deactivation: useful if you want an animation to play only when the subject leaves the scrollport.

It doesn't make sense to combine `pause` with `reset` because both effectively pause the animation, except that `reset` puts the animation back to the start. If the animation has not been played, `reset` has no discernible effect.

### [Resetting the animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#resetting_the_animation)

The `replay` and `reset` values are similar to `pause`, except that:

*   `reset` pauses the animation but also puts it back to the start.
*   `replay` puts the animation back to the start and then starts playing it again.

We previously discussed using these values in combination with other values. However, one case was not mentioned: using them as the activation action.

For example:

css

    animation-trigger: --t replay pause;
    

This has an interesting effect: it plays on activation (the same as an action like `play`) and pauses on deactivation. However, on subsequent activation, it will play from the start again, regardless of the previous play state. This is useful if you want an animation to play when the subject enters the scrollport, pause when it leaves the scrollport, but then play from the start on each subsequent entry.

Another interesting example is as follows:

css

    animation-trigger: --t reset play;
    

This has an interesting effect: it doesn't play on activation but plays on deactivation. On subsequent activation, it resets to progress `0`, regardless of the previous play state. This is useful if you want an animation to play when the subject leaves the scrollport, and then reset to the beginning on each subsequent entry.

### [Equivalence with the Web Animations API](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#equivalence_with_the_web_animations_api)

The behavior specified by the various `<animation-action>` keywords is equivalent to calling various methods of the [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
 on the specified animation, as follows:

[`play`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play_3)

Equivalent to calling [`Animation.play()`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/play)
 on the animation.

[`play-forwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-forwards_2)

Equivalent to setting the [`Animation.playbackRate`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/playbackRate)
 of a playing animation to its absolute positive value.

[`play-backwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-backwards_2)

Equivalent to setting the [`Animation.playbackRate`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/playbackRate)
 of a playing animation to its absolute positive value multiplied by `-1`.

[`play-once`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#play-once_3)

Equivalent to calling `Animation.play()` on the animation except that it only plays once.

[`pause`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#pause_2)

Equivalent to calling [`Animation.pause()`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/pause)
 on the animation.

[`replay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#replay_2)

Equivalent to setting the [`Animation.overallProgress`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/overallProgress)
 of a playing animation to `0`.

[`reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#reset_2)

Equivalent to setting the `Animation.overallProgress` of a paused animation to `0`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#formal_syntax)

------------------------------------------------------------------------------------------------------------------

<animation-action> =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pause           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  play            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  play-backwards  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  play-forwards   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  play-once       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  replay          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  reset             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#basic_usage)

This example shows how to create a basic scroll-triggered animation that plays forwards on trigger activation and backward on trigger deactivation.

#### HTML

Our markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one to animate and one to create a trigger, plus some basic text content to scroll the page. We have hidden the text content for brevity.

html

    <div class="animated">I am animated</div>
    
    ...
    
    <div class="trigger">I create the trigger</div>
    
    ...
    

    <div class="animated">I am animated</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger">I create the trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

#### CSS

We give the `.animated` element a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 of `fixed`, positioning it near the top-left of the scrollport so we can see when its animation starts and stops.

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      height: 100px;
      border: 5px solid black;
    }
    
    .animated {
      width: 100px;
      background: orange;
    }
    
    .trigger {
      background: wheat;
    }
    

css

    .animated {
      position: fixed;
      top: 25px;
      left: 25px;
    }
    

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for a `rotate` animation:

css

    @keyframes rotate {
      from {
        rotate: 0deg;
      }
    
      to {
        rotate: 360deg;
      }
    }
    

The `.animated` element has the `rotate` animation applied. We then give it an `animation-trigger` value that references a `timeline-trigger-name` of `--t` with two `<animation-action>` values, `play-forwards` and `play-backwards`. These specify that the animation will play on activation and play in reverse on deactivation.

css

    .animated {
      animation: rotate 1.5s infinite linear both;
      animation-trigger: --t play-forwards play-backwards;
    }
    

The `.trigger` element creates the animated `<div>`'s trigger using a `timeline-trigger` value of `--t view()`. This value includes the identifier referenced in the animated `<div>`'s `animation-trigger` property value (the `timeline-trigger-name`), associating the two together. It also includes:

*   A `timeline-trigger-source` value of [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.
*   A [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     value of [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#contain)
    , which means that the trigger will activate when the `.trigger` element is fully inside the scrollport. Because [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     defaults to `auto`, its value is the same as the activation range; the trigger therefore deactivates when it stops being fully inside the scrollport.

css

    .trigger {
      timeline-trigger: --t view() contain;
    }
    

#### Result

Try scrolling the content up. When the tracked `<div>` fully appears in the scrollport, the animation plays; when it starts to leave the scrollport at either edge, the animation plays in reverse.

### [Comparing the `<animation-action>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#comparing_the_animation-action_values)

This example provides a comparison of the various `<animation-action>` values. By applying the same rotation animation to identical side-by-side elements and varying the `animation-trigger` values, you can compare and contrast the effects of the different actions.

#### HTML

We include a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element containing five [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each with a number inside. We also include text content to make the page scroll, which we've hidden for brevity.

html

    <section>
      <div class="one">1</div>
      <div class="two">2</div>
      <div class="three">3</div>
      <div class="four">4</div>
      <div class="five">5</div>
    </section>
    

    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <section>
      <div class="one">1</div>
      <div class="two">2</div>
      <div class="three">3</div>
      <div class="four">4</div>
      <div class="five">5</div>
    </section>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

#### CSS

We apply the same [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to each `<div>` element—we play the `rotate` animation infinitely, with each iteration lasting two seconds. We also style each `<div>` to be a `50px` diameter colored circle.

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      display: flex;
      justify-content: center;
    }
    
    section {
      display: flex;
      justify-content: space-between;
    }
    

css

    div {
      animation: rotate 2s infinite linear both;
      height: 50px;
      width: 50px;
      border: 5px solid black;
      border-radius: 50%;
      background-color: orange;
    }
    

Next, we set the `<section>` element to create an animation trigger, with a `timeline-trigger` value of `--t view() contain 20% contain 80%`. There is nothing unusual here, except that we've set a [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
 value and defaulted the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 to `contain 20% contain 80%`. This means the trigger activates when the `<section>` element has scrolled around `20%` of the way up the scrollport, and deactivates when it has scrolled around `80%` of the way up the scrollport. This allows you to see the `<animation-action>` effects more clearly than if the activation range covered the entire scrollport.

css

    section {
      timeline-trigger: --t view() contain 20% contain 80%;
    }
    

Next, we set a different [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property value on each `<div>` element. Each one references the `<section>` element's `timeline-trigger-name`, but each one has a different set of `<animation-action>` values applied. The last `<div>` additionally has a new `animation` property value applied, overriding the one we set earlier. It is the same as the original `animation` property, except that the iteration count is set to `1` rather than `infinite`. It is easier to demonstrate the effect of `play-once` when `animation-iteration-count` is not `infinite` (if this were the case, it would play forever, regardless).

css

    .one {
      animation-trigger: --t play-forwards play-backwards;
    }
    
    .two {
      animation-trigger: --t play;
    }
    
    .three {
      animation-trigger: --t play replay;
    }
    
    .four {
      animation-trigger: --t pause play;
    }
    
    .five {
      animation: rotate 2s 1 linear both;
      animation-trigger: --t play-once reset;
    }
    

    @supports not (animation-trigger: --t play-once reset) {
      body::before {
        content: "Your browser does not support scroll-triggered animations.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Scroll down to the point where the `<section>` and `<div>` elements enter the scrollport. Move them through the start and end of the trigger activation range, concentrating on a different `<div>` each time, to visualize the effects of each set of `<animation-action>`s.

The effects are:

1.  The first `<div>` (far left) has `play-forwards play-backwards` set. When the tracked element enters the activation range, the animation plays forward. When it leaves the activation range (at the top or bottom of the scrollport), it starts playing backward.
2.  The second `<div>` has a single `<animation-action>` set — `play`. When the tracked element enters the activation range, the animation starts to play. However, because no deactivation action is set to change its behavior, the animation continues to play forever until the page reloads.
3.  The third `<div>` has `play replay` set. When the tracked element enters the activation range, the animation starts playing forward. When it leaves the activation range, the animation resets to progress `0` and then starts playing again.
4.  The fourth `<div>` has `pause play` set. When the tracked element enters the activation range, the animation continues not to play due to the paused state. However, when it leaves the activation range, the animation starts to play. From then on, the animation pauses when the tracked element is inside the activation range and plays when it is outside it.
5.  The fifth `<div>` (far right, with an iteration count of `1`) has `play-once reset` set. When the tracked element enters the activation range, the animation plays once. When it leaves the activation range, the animation resets to progress `0` and pauses. From then on, the animation plays once whenever the tracked element enters the activation range and resets when it leaves the activation range.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-animation-trigger](https://drafts.csswg.org/animation-triggers-1/#propdef-animation-trigger) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action#see_also)

--------------------------------------------------------------------------------------------------------

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand property
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/animation-action/index.md?plain=1 "Folder: en-us/web/css/reference/values/animation-action (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fanimation-action&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fanimation-action%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fanimation-action%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fanimation-action%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")