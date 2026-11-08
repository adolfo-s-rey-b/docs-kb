*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#mdn-search)
    

CSS animation triggers
======================

The **CSS animation triggers** module provides functionality to trigger standard time-based [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 when a specific timeline trigger occurs.

**Scroll-triggered animations** allow you to control when a regular time-based animation starts, pauses, or stops based on when a trigger activates or deactivates, without using JavaScript. This could include when a scrolling element enters or leaves a [timeline range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets)
.

These ranges normally come from [view progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
, enabling, for example, an animation to start when an element enters a scrollport and pause when it leaves the scrollport. Properties let you change the timeline range and control the active and activation ranges. Triggers can specify different actions when entering versus exiting the timeline range, allowing control over animation playback.

The animation triggers module also defines **event triggers**. When supported, these will activate timeline-based animations when specific DOM events occur.

[Animation triggers in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#animation_triggers_in_action)

----------------------------------------------------------------------------------------------------------------------------------------

This example demonstrates [scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
. Scroll the box up and down — the appearance of the "bouncer" text will trigger the ball's animation, and its disappearance will trigger the same animation in reverse. Scroll further, and the same process will repeat when the "another bouncer" text appears and then disappears from the scrollport.

    <section>
      <div>
        <p>scroll down</p>
        <p id="trigger">bouncer</p>
        <p>keep scrolling</p>
        <p>keep scrolling</p>
        <p>keep scrolling</p>
        <p id="trigger2">another bouncer</p>
        <p>scroll up</p>
      </div>
    </section>
    
    <span id="ball"><span></span></span>
    

    #ball,
    #ball span {
      animation:
        move-right 2s 1 ease-out both,
        move-right 2s 1 ease-out forwards;
      animation-trigger:
        --t play-forwards play-backwards,
        --t2 play-forwards play-backwards;
    }
    #ball span {
      animation-name: bounce, bounce;
    }
    
    #trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    #trigger2 {
      timeline-trigger-name: --t2;
      timeline-trigger-source: view();
    }
    
    html {
      font-family: sans-serif;
      font-size: 1.3rem;
    }
    
    * {
      box-sizing: border-box;
    }
    
    @layer scroller {
      section {
        border: solid;
        width: 200px;
        height: 250px;
        margin-top: 50px;
        overflow: scroll;
      }
      p {
        text-align: center;
        font-size: 1.5rem;
        margin: 100% 0;
      }
      #trigger,
      #trigger2 {
        padding: 0;
        color: red;
      }
    }
    
    @layer animation-setup {
      #ball {
        position: fixed;
        top: 96vh;
      }
      #ball span {
        background: red;
        border-radius: 50%;
        height: 5vw;
        display: block;
        aspect-ratio: 1/1;
      }
    
      @keyframes move-right {
        from {
          transform: translateX(0);
        }
        to {
          transform: translateX(90vw);
        }
      }
    
      @keyframes bounce {
        9%,
        24%,
        35%,
        44%,
        51%,
        58%,
        63%,
        68%,
        72%,
        76%,
        100% {
          transform: translateY(0);
          animation-timing-function: ease-out;
        }
        0%,
        17%,
        30%,
        40%,
        48%,
        55%,
        61%,
        66%,
        70%,
        74% {
          animation-timing-function: ease-in;
        }
        0% {
          transform: translateY(-96vh);
        }
        17% {
          transform: translateY(-57.6vh);
        }
        30% {
          transform: translateY(-34.56vh);
        }
        40% {
          transform: translateY(-20.74vh);
        }
        48% {
          transform: translateY(-12.44vh);
        }
        55% {
          transform: translateY(-7.46vh);
        }
        61% {
          transform: translateY(-4.48vh);
        }
        66% {
          transform: translateY(-2.69vh);
        }
        70% {
          transform: translateY(-1.61vh);
        }
        74% {
          transform: translateY(-0.97vh);
        }
      }
    }
    

    @supports not (timeline-trigger-source: view()) {
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
    

We defined the animation triggers by specifying a [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 and [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 on the "bouncer" elements. The ball has a bouncing [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 set on it twice. It also has an [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property set: this references the names of both triggers and the actions to perform when the animations are activated and deactivated. Activation and deactivation are caused by the "bouncer" elements coming into and out of view.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#reference)

--------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#properties)

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand
*   [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     shorthand
    *   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
        
    *   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
        
*   [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     shorthand
    *   [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
        
    *   [`timeline-trigger-active-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
        
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    
*   [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    
*   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    

The CSS animation triggers module also introduces the `event-trigger`, `event-trigger-name`, and `event-trigger-source` properties. Currently, no browsers support these features.

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#data_types_and_values)

*   [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#guides)

--------------------------------------------------------------------------------------------

[Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)

An introduction to implementing CSS scroll-triggered animations.

[Timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)

The [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 data type: Understanding the various timeline range names.

[Understanding timeline insets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets)

Understanding the animation attachment range syntax used to inset scroll-driven and scroll-triggered animations.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#related_concepts)

----------------------------------------------------------------------------------------------------------------

*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
    *   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
        
    *   [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
         at-rule
    *   [`<keyframe-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
        
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
    *   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
         shorthand
        *   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
            
        *   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
            
    *   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
         shorthand
        *   [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
            
        *   [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
            
    *   [`timeline-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
        
    *   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
         shorthand
        *   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
            
        *   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
            
        *   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
            

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers](https://drafts.csswg.org/animation-triggers-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers#see_also)

------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [Using scroll driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [CSS scroll-triggered animations are coming!](https://developer.chrome.com/blog/scroll-triggered-animations "External link (opens in new tab)")
     on developer.chrome.com (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/animation_triggers/index.md?plain=1 "Folder: en-us/web/css/guides/animation_triggers (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimation_triggers&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fanimation_triggers%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimation_triggers%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fanimation_triggers%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")