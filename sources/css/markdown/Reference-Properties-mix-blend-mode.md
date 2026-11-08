*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#mdn-search)
    

`mix-blend-mode` CSS property
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mix-blend-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how an element's content should blend with its _backdrop_ — the content rendered behind the element within the same [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
.

**Note:** This property blends the element with content _behind_ it in the stacking context. To blend an element's own background layers with each other, use [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
 instead.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#try_it)

------------------------------------------------------------------------------------------------------

    mix-blend-mode: normal;
    

    mix-blend-mode: multiply;
    

    mix-blend-mode: hard-light;
    

    mix-blend-mode: difference;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <img
          id="example-element"
          src="/shared-assets/images/examples/firefox-logo.svg"
          width="200" />
      </div>
    </section>
    

    .example-container {
      background-color: sandybrown;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    mix-blend-mode: normal;
    mix-blend-mode: multiply;
    mix-blend-mode: screen;
    mix-blend-mode: overlay;
    mix-blend-mode: darken;
    mix-blend-mode: lighten;
    mix-blend-mode: color-dodge;
    mix-blend-mode: color-burn;
    mix-blend-mode: hard-light;
    mix-blend-mode: soft-light;
    mix-blend-mode: difference;
    mix-blend-mode: exclusion;
    mix-blend-mode: hue;
    mix-blend-mode: saturation;
    mix-blend-mode: color;
    mix-blend-mode: luminosity;
    mix-blend-mode: plus-darker;
    mix-blend-mode: plus-lighter;
    
    /* Global values */
    mix-blend-mode: inherit;
    mix-blend-mode: initial;
    mix-blend-mode: revert;
    mix-blend-mode: revert-layer;
    mix-blend-mode: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#values)

[`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)

The blending mode that should be applied.

[`plus-darker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#plus-darker)

Blending using the [_plus-darker_ compositing operator](https://drafts.csswg.org/compositing-2/#porterduffcompositingoperators_plus_darker "External link (opens in new tab)")
.

[`plus-lighter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#plus-lighter)

Blending using the [_plus-lighter_ compositing operator](https://drafts.csswg.org/compositing-2/#porterduffcompositingoperators_plus_lighter "External link (opens in new tab)")
. Useful for cross-fade effects (prevents unwanted blinking when two overlaying elements animate their opacity in opposite directions).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

mix-blend-mode =   
  <blend-mode>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  plus-lighter    
  
[<blend-mode>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
 =   
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  darken       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  multiply     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-burn   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lighten      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  screen       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-dodge  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlay      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  soft-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hard-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  difference   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exclusion    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hue          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  saturation   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  luminosity     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#examples)

----------------------------------------------------------------------------------------------------------

### [Effect of different mix-blend-mode values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#effect_of_different_mix-blend-mode_values)

    <div class="grid">
      <div class="col">
        <div class="note">
          Blending in isolation (no blending with the background)
        </div>
        <div class="row isolate">
          <div class="cell">
            normal
            <div class="container normal">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <defs>
                    <linearGradient id="red">
                      <stop offset="0" stop-color="hsl(0 100% 50%)" />
                      <stop offset="100%" stop-color="hsl(0 0% 100%)" />
                    </linearGradient>
                    <linearGradient id="green">
                      <stop offset="0" stop-color="hsl(120 100% 50%)" />
                      <stop offset="100%" stop-color="hsl(120 0% 100%)" />
                    </linearGradient>
                    <linearGradient id="blue">
                      <stop offset="0" stop-color="hsl(240 100% 50%)" />
                      <stop offset="100%" stop-color="hsl(240 0% 100%)" />
                    </linearGradient>
                  </defs>
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            multiply
            <div class="container multiply">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            darken
            <div class="container darken">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            screen
            <div class="container screen">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            lighten
            <div class="container lighten">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            overlay
            <div class="container overlay">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color-dodge
            <div class="container color-dodge">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color-burn
            <div class="container color-burn">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            hard-light
            <div class="container hard-light">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            soft-light
            <div class="container soft-light">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            difference
            <div class="container difference">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            exclusion
            <div class="container exclusion">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            hue
            <div class="container hue">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            saturation
            <div class="container saturation">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color
            <div class="container color">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            luminosity
            <div class="container luminosity">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            plus-darker
            <div class="container plus-darker">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            plus-lighter
            <div class="container plus-lighter">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
        </div>
    
        <div class="note">Blending globally (blend with the background)</div>
        <div class="row">
          <div class="cell">
            normal
            <div class="container normal">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            multiply
            <div class="container multiply">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            darken
            <div class="container darken">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            screen
            <div class="container screen">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            lighten
            <div class="container lighten">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            overlay
            <div class="container overlay">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color-dodge
            <div class="container color-dodge">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color-burn
            <div class="container color-burn">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            hard-light
            <div class="container hard-light">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            soft-light
            <div class="container soft-light">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            difference
            <div class="container difference">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            exclusion
            <div class="container exclusion">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            hue
            <div class="container hue">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            saturation
            <div class="container saturation">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            color
            <div class="container color">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            luminosity
            <div class="container luminosity">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            plus-darker
            <div class="container plus-darker">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
          <div class="cell">
            plus-lighter
            <div class="container plus-lighter">
              <div class="group">
                <div class="item firefox"></div>
                <svg class="item" viewBox="0 0 150 150">
                  <ellipse class="item R" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item G" cx="75" cy="75" rx="25" ry="70"></ellipse>
                  <ellipse class="item B" cx="75" cy="75" rx="25" ry="70"></ellipse>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    

    html,
    body {
      height: 100%;
      box-sizing: border-box;
      background: #eeeeee;
    }
    
    .grid {
      width: 100%;
      display: flex;
      font: 1em monospace;
    }
    
    .row {
      display: flex;
      flex: 1 auto;
      flex-direction: row;
      flex-wrap: wrap;
      height: auto;
    }
    
    .col {
      display: flex;
      flex: 1 auto;
      flex-direction: column;
      height: auto;
    }
    
    .cell {
      margin: 0.5em;
      padding: 0.5em;
      background-color: white;
      overflow: hidden;
      text-align: center;
    }
    
    .note {
      background: #fff3d4;
      padding: 1em;
      margin: 0.5em 0.5em 0;
      font: 0.8em sans-serif;
      text-align: left;
      white-space: nowrap;
    }
    
    .note + .row .cell {
      margin-top: 0;
    }
    
    .container {
      position: relative;
      background:
        linear-gradient(to right, black 0%, transparent 50%, white 100%),
        linear-gradient(to bottom, yellow 0%, magenta 50%, cyan 100%);
      width: 150px;
      height: 150px;
      margin: 0 auto;
    }
    
    .R {
      transform-origin: center;
      transform: rotate(-30deg);
      fill: url("#red");
    }
    
    .G {
      transform-origin: center;
      transform: rotate(90deg);
      fill: url("#green");
    }
    
    .B {
      transform-origin: center;
      transform: rotate(210deg);
      fill: url("#blue");
    }
    
    .isolate .group {
      isolation: isolate;
    }
    
    .normal .item {
      mix-blend-mode: normal;
    }
    .multiply .item {
      mix-blend-mode: multiply;
    }
    .screen .item {
      mix-blend-mode: screen;
    }
    .overlay .item {
      mix-blend-mode: overlay;
    }
    .darken .item {
      mix-blend-mode: darken;
    }
    .lighten .item {
      mix-blend-mode: lighten;
    }
    .color-dodge .item {
      mix-blend-mode: color-dodge;
    }
    .color-burn .item {
      mix-blend-mode: color-burn;
    }
    .hard-light .item {
      mix-blend-mode: hard-light;
    }
    .soft-light .item {
      mix-blend-mode: soft-light;
    }
    .difference .item {
      mix-blend-mode: difference;
    }
    .exclusion .item {
      mix-blend-mode: exclusion;
    }
    .hue .item {
      mix-blend-mode: hue;
    }
    .saturation .item {
      mix-blend-mode: saturation;
    }
    .color .item {
      mix-blend-mode: color;
    }
    .luminosity .item {
      mix-blend-mode: luminosity;
    }
    .plus-darker .item {
      mix-blend-mode: plus-darker;
    }
    .plus-lighter .item {
      mix-blend-mode: plus-lighter;
    }
    

### [Using mix-blend-mode with HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#using_mix-blend-mode_with_html)

#### HTML

html

    <div class="isolate">
      <div class="circle circle-1"></div>
      <div class="circle circle-2"></div>
      <div class="circle circle-3"></div>
    </div>
    

#### CSS

css

    .circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      mix-blend-mode: screen;
      position: absolute;
    }
    
    .circle-1 {
      background: red;
    }
    
    .circle-2 {
      background: lightgreen;
      left: 40px;
    }
    
    .circle-3 {
      background: blue;
      left: 20px;
      top: 40px;
    }
    
    .isolate {
      isolation: isolate; /* Without isolation, the background color will be taken into account */
      position: relative;
    }
    

#### Result

### [Using mix-blend-mode with SVG](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#using_mix-blend-mode_with_svg)

#### SVG

html

    <svg>
      <g class="isolate">
        <circle cx="40" cy="40" r="40" fill="red" />
        <circle cx="80" cy="40" r="40" fill="lightgreen" />
        <circle cx="60" cy="80" r="40" fill="blue" />
      </g>
    </svg>
    

#### CSS

css

    circle {
      mix-blend-mode: screen;
    }
    .isolate {
      isolation: isolate;
    } /* Without isolation, the background color will be taken into account */
    

#### Result

### [Using mix-blend-mode with text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#using_mix-blend-mode_with_text)

This example uses `mix-blend-mode` to blend text color with the background color of its parent element.

#### HTML

html

    <div class="container">
      <p>Mostly Harmless</p>
      <p class="multiply">Mostly Harmless</p>
      <p class="screen">Mostly Harmless</p>
      <p class="hard-light">Mostly Harmless</p>
    </div>
    

#### CSS

css

    @import "https://fonts.googleapis.com/css2?family=Rubik+Moonrocks&display=swap";
    
    .container {
      background-color: blue;
    }
    
    p {
      font:
        4rem "Rubik Moonrocks",
        cursive;
      font-weight: bold;
      color: orange;
      padding: 0.5rem;
      margin: 0;
    }
    
    .multiply {
      mix-blend-mode: multiply;
    }
    
    .screen {
      mix-blend-mode: screen;
    }
    
    .hard-light {
      mix-blend-mode: hard-light;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compositing and Blending Module Level 2  <br>\# mix-blend-mode](https://drafts.csswg.org/compositing/#mix-blend-mode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode#see_also)

----------------------------------------------------------------------------------------------------------

*   [`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
    
*   [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mix-blend-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mix-blend-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmix-blend-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmix-blend-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmix-blend-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmix-blend-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a1539b859a7e1b1daedd1880c610b71debde782%0A*+Document+last+modified%3A+2026-06-08T17%3A17%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")