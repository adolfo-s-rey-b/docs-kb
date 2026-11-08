*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#mdn-search)
    

`shape()` CSS function
======================

Baseline 2026

Newly available

Since February 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`shape()`** [CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is used to define a shape for the [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
, [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
, and [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 properties. It combines an initial starting point with a series of shape commands that define the path of the shape. The `shape()` function is a member of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 data type.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* <fill-rule> */
    clip-path: shape(nonzero from 0 0, line to 10px 10px);
    
    /* <move-command>, <line-command>, and close */
    offset-path: shape(from 10px 10px, move by 10px 5px, line by 20px 40%, close);
    
    /* <hvline-command> */
    offset-path: shape(from 10px 10px, hline by 50px, vline to 5rem);
    
    /* <curve-command> */
    offset-path: shape(
      from 10px 10px,
      curve to 80px 80px with 160px 1px / 20% 16px
    );
    
    /* <smooth-command> */
    offset-path: shape(from 10px 10px, smooth to 100px 50pt);
    
    /* <arc-command> */
    offset-path: shape(
      from 5% 0.5rem,
      arc to 80px 1pt of 10% ccw large rotate 25deg
    );
    
    /* Using a CSS math function */
    offset-path: shape(
      from 5px -5%,
      hline to 50px,
      vline by calc(0% + 160px),
      hline by 70.5px,
      close,
      vline by 60px
    );
    
    clip-path: shape(
      evenodd from 10px 10px,
      curve to 60px 20% with 40px 0,
      smooth to 90px 0,
      curve by -20px 60% with 10% 40px / 20% 20px,
      smooth by -40% -10px with -10px 70px,
      close
    );
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#parameters)

[`<fill-rule>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 Optional

Specifies how overlapping regions of a shape should be filled. The possible values include:

*   `nonzero`: A point is considered inside the shape if a ray drawn from the point crosses more left-to-right than right-to-left path segments, resulting in a non-zero count. This is the default value when `<fill-rule>` is omitted.
    
*   `evenodd`: A point is considered to be inside the shape if a ray drawn from the point crosses an odd number of path segments. This means that for each time the ray enters the shape, it has not exited an equal number of times, indicating an odd count of entries without corresponding exits.
    

**Warning:** `<fill-rule>` is not supported in [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 and using it invalidates the property.

[`from <coordinate-pair>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#from_coordinate-pair)

Defines the starting point of the first `<shape-command>` as a pair of coordinates that are measured from the top-left corner of the [reference box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)
. The coordinates are specified as space-separated `<x> <y>` [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values representing the left offset and top offset, respectively. Percentage values are relative to the width and height of the element's reference box, respectively. Add a comma after this parameter.

[`<shape-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#shape-command)

Specifies a list of one or more comma-separated commands that define the shape, using syntax similar to [SVG path commands](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#path_commands)
. Commands include `<move-command>`, `<line-command>`, `<hv-line-command>`, `<curve-command>`, `<smooth-command>`, `<arc-command>`, and `close`. Each command's starting point is the previous command's ending point, with the first point of the shape defined by the [`from <coordinate-pair>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#from_coordinate-pair)
 parameter.

#### Shape commands

The syntax of most shape commands is a keyword that provides a directive, such as `move` or `line`, followed by the `by` or `to` keyword, and a set of coordinates.

*   `by`: Indicates that the `<coordinate-pair>` is relative to the command's starting point (a "relative" value).
*   `to`: Indicates that the `<coordinate-pair>` is relative to the top-left corner of the reference box (an "absolute" value).

**Note:** If a coordinate in a `<coordinate-pair>` is specified as a percentage, the value is calculated relative to the respective width or height of the reference box.

The following `<shape-command>`s can be specified:

[`<move-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#move-command)

Specified as `move [by | to] <coordinate-pair>`. This command adds a [MoveTo command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#moveto_path_commands)
 to the list of shape commands. It draws nothing; instead, it specifies the starting position for the next command. The `by` or `to` keyword specifies whether the `<coordinate-pair>` point is relative or absolute, respectively. If the `<move-command>` follows the `close` command, it identifies the starting point of the next shape or subpath.

[`<line-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#line-command)

Specified as `line [by | to] <coordinate-pair>`. This command adds a [LineTo command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#lineto_path_commands)
 to the list of shape commands. It draws a straight line from the command's starting point to its ending point. The `by` or `to` keyword specifies whether the ending point specified by `<coordinate-pair>` is relative or absolute, respectively.

[`<hv-line-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#hv-line-command)

Specified as `[hline | vline] [by | to] <length-percentage>`. This command adds a horizontal (`hline`) or vertical (`vline`) [LineTo command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#lineto_path_commands)
 to the list of shape commands. With `hline`, a horizontal line is drawn from the command's starting point `to` or `by` the `x` position defined by `<length-percentage>`. With `vline`, a vertical line is drawn from the command's starting point `to` or `by` the `y` position defined by `<length-percentage>`. The `by` or `to` keyword determines the relative or absolute ending point, respectively. This command is equivalent to `<line-command>` with one coordinate value set by the single `<length-percentage>` and the other coordinate value remaining unchanged from its starting command.

[`<curve-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#curve-command)

Specified as `curve [by | to] <end-point> with <control-point> [/ <control-point>]`. This command adds a [Bézier curve command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#cubic_b%C3%A9zier_curve)
 to the list of shape commands. The `by` or `to` keyword determines whether the ending point of the curve, specified by the `<end-point>`, is relative or absolute.

The `with` keyword specifies the control points of the Bézier curve as follows.

*   If only a single `<control-point>` is provided, the command draws a [quadratic Bézier curve](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#quadratic_b%C3%A9zier_curve)
    , which is defined by three points (the start point, control point, and end point).
*   If two `<control-point>` values are provided, the command draws a cubic Bézier curve, which is defined by four points (the start point, two control points, and the end point).

Valid values for `<end-point>` include:

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 keywords or a `<coordinate-value-pair>`

Can be used if the curve end point is absolute (specified using `to`).

[`<coordinate-value-pair>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#coordinate-value-pair)

Can be used if the curve end point is relative (specified using `by`).

Valid values for `<control-point>` include:

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)

Specifies a position keyword. This value is valid only when the curve end point is absolute (specified using `to`).

[`<coordinate-value-pair>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#coordinate-value-pair_2)

Specifies a pair of [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values that define coordinates.

[`<relative-control-point>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#relative-control-point)

Defines a `<coordinate-value-pair>` followed by the `from` keyword and one of the following keywords:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#start)

Indicates that the control point is relative to the start point of the current command.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#end)

Indicates that the control point is relative to the end point of the current command.

[`origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#origin)

Indicates that the control point is relative to the top-left (origin) point of the container the shape is being drawn inside.

**Note:** If the `<relative-control-point>` keywords are not specified, making the `<control-point>` a regular `<coordinate-value-pair>`, the coordinates are relative to the start of the curve. In other words, `start` is the default setting.

[`<smooth-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#smooth-command)

Specified as `smooth [by | to] <end-point> [with <control-point>]`. This command adds a smooth [Bézier curve command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#cubic_b%C3%A9zier_curve)
 to the list of shape commands. The `by` or `to` keyword determines whether the ending point of the curve, specified by the `<end-point>`, is relative or absolute.

The `with` keyword specifies an optional control point for the Bézier curve:

*   If `with <control-point>` is omitted, the command draws a smooth quadratic Bézier curve, which uses the previous control point and the current endpoint to define the curve.
*   If the optional `with` keyword is included, it specifies a control points of the curve through `<control-point>`, drawing a smooth cubic Bézier curve defined by the previous control point, the current control point, and the current endpoint.

Smooth curves ensure a continuous transition from the shape, while quadratic curves do not. Smooth quadratic curves maintain a seamless transition using a single control point, whereas smooth cubic curves provide a more refined transition using two control points.

Valid values for the `<end-point>` and `<control-point>` components are the same as those for [`<curve-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#curve-command)
.

[`<arc-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#arc-command)

Specified as `arc [by | to] <coordinate-pair> of <length-percentage> [<length-percentage>] [<arc-sweep> | <arc-size> | rotate <angle>]`. This command adds an [elliptical arc curve command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#elliptical_arc_curve)
 to the list of shape commands. It draws an elliptical arc between a starting point and an ending point. The `by` or `to` keyword determines whether the ending point of the curve, specified by the first `<coordinate-pair>`, is relative or absolute, respectively.

The elliptical arc curve command defines two possible ellipses, which intersect both the starting and ending points, and each can be traced clockwise or counterclockwise, resulting in four possible arcs depending on the arc size, direction, and angle. The `of` keyword specifies the size of the ellipse from which the arc is taken: the first `<length-percentage>` provides the horizontal radius of the ellipse, and the second `<length-percentage>` provides the vertical radius.

Specify the following parameters to choose which of the four arcs to use:

*   `<arc-sweep>`: Indicates whether the desired arc is the one traced around the ellipse clockwise (`cw`) or counterclockwise (`ccw`). If omitted, this defaults to `ccw`.
*   `<arc-size>`: Indicates whether the desired arc is the larger (`large`) or smaller (`small`) of the two arcs. If omitted, this defaults to `small`.
*   `<angle>`: Specifies the angle, in degrees, by which to rotate the ellipse relative to the x-axis. A positive angle rotates the ellipse clockwise, and a negative angle rotates it counterclockwise. If omitted, this defaults to `0deg`.

Special situations are handled as follows:

*   If only one `<length-percentage>` is provided, the same value is used for both the horizontal and vertical radii, effectively creating a circle. In this case, `<arc-size>` and `<angle>` have no effect.
*   If either radius is zero, the command is equivalent to a `<line-command>` to the ending point.
*   If either radius is negative, its absolute value is used instead.
*   If the horizontal and vertical radii don't describe an ellipse large enough to intersect both the starting point and ending points (after rotation by the specified `<angle>`), the radii are scaled up uniformly until the ellipse is just large enough to intersect both points.
*   If the starting and ending points of the arc lie on exactly opposite sides of the ellipse, there is only one possible ellipse and two possible arcs. In this case, `<arc-sweep>` specifies the arc to choose, and `<arc-size>` has no effect.

[`close`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#close)

Adds a [ClosePath command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#closepath)
 to the list of shape commands, drawing a straight line from the current position (end of the last command) to the first point in the path defined in the `from <coordinate-pair>` parameter. To close the shape without drawing a line, include a `<move-command>` with the originating coordinates before the close command. If the `close` command is immediately followed by a `<move-command>`, it defines the starting point of the next shape or subpath.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#description)

---------------------------------------------------------------------------------------------------------------

The `shape()` function allows you to define complex shapes. It is similar to the [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 shape function in several ways:

*   The `<fill-rule>` parameter in the `shape()` function works exactly like the same parameter in the `path()` function.
*   The `shape()` function requires specifying one or more `<shape-command>`s, where each command uses an underlying [path command](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#path_commands)
    , such as [MoveTo](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#moveto_path_commands)
    , [LineTo](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#lineto_path_commands)
    , and [ClosePath](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#closepath)
    .

However, `shape()` offers several advantages over using `path()`:

*   `shape()` uses standard CSS syntax, making it easier to create and modify shapes directly in your stylesheet. In comparison, `path()` uses the [SVG path](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
     syntax, which is less intuitive for those not familiar with SVG.
*   `shape()` supports a variety of CSS units, including percentages, `rem`, and `em`. `path()`, on the other hand, defines shapes as a single string and limits units to `px`.
*   `shape()` also allows the use of CSS math functions, like [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    , [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    , and [`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
    , providing more versatility when defining shapes.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

<shape()> =   
  shape( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 from <position> , <shape-command>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<fill-rule>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    
  
[<position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 =   
  <position-one>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-two>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-four>    
  
<shape-command> =   
  <move-command>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <line-command>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  close                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <horizontal-line-command>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <vertical-line-command>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <curve-command>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <smooth-command>           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <arc-command>                
  
<position-one> =   
  left                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-start              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-end                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y-start              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y-end                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-start          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-end            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
<position-two> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
                           
  
<position-four> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
            
  
<move-command> =   
  move <command-end-point>    
  
<line-command> =   
  line <command-end-point>    
  
<horizontal-line-command> =   
  hline [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 by <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<vertical-line-command> =   
  vline [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 by <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<curve-command> =   
  curve [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to <position> with <control-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 by <coordinate-pair> with <relative-control-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <relative-control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<smooth-command> =   
  smooth [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to <position> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 with <control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 by <coordinate-pair> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 with <relative-control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<arc-command> =   
  arc <command-end-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 of <length-percentage>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 <arc-sweep>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 <arc-size>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 rotate [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
<command-end-point> =   
  to <position>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  by <coordinate-pair>    
  
<control-point> =   
  <position>                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <relative-control-point>    
  
<coordinate-pair> =   
  <length-percentage>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<relative-control-point> =   
  <coordinate-pair> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 origin [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<arc-sweep> =   
  cw   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ccw    
  
<arc-size> =   
  large  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  small    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#examples)

---------------------------------------------------------------------------------------------------------

### [Using `shape()` to define a path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#using_shape_to_define_a_path)

This example demonstrates how the `shape()` function can be used in the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property to define the shape of the path an element can follow.

The first shape, `shape1`, follows a cubic Bézier curved path defined by the `curve to` command. Next, the `close` command draws a straight line from the curve's end point back to the initial point defined in the `from` command. Finally, `shape1` moves to its new position at `0px 150px` and then proceeds along a horizontal line.

The second shape, `shape2`, initially follows a horizontal line, then moves back to its starting position at `50px 90px`. Next, it follows a vertical line before closing the path back to the initial point.

Both shapes start with their original colors and gradually transition to `hotpink` by the end of the `move` animation, reverting to their initial color as the animation restarts. This cyclic color change provides you a visual cue about the animation's progression and restart.

    <div class="container">
      Using <code>&lt;curve-command&gt;</code>
      <div class="shape shape1">>></div>
    </div>
    
    <div class="container">
      Using <code>&lt;move-command&gt;</code> and
      <code>&lt;hvline-command&gt;</code>
      <div class="shape shape2">>></div>
    </div>
    

    body {
      align-items: center;
      justify-content: center;
      display: flex;
    }
    
    .container {
      position: relative;
      display: inline-block;
      width: 250px;
      height: 250px;
      border: 2px dotted green;
      margin: 20px;
    }
    
    @supports not (offset-path: shape(from 0 0, move to 0 0)) {
      body::after {
        content: "Your browser doesn't support the `shape()` function yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    .shape {
      width: 50px;
      height: 50px;
      background: #2bc4a2;
      position: absolute;
      text-align: center;
      line-height: 50px;
      animation: move 6s infinite linear;
    }
    
    .shape1 {
      offset-path: shape(
        from 30% 60px,
        curve to 180px 180px with 90px 190px,
        close,
        move by 0px 150px,
        hline by 40%
      );
    }
    
    .shape2 {
      offset-path: shape(
        from 50px 90px,
        hline to 8em,
        move to 50px 90px,
        vline by 20%,
        close
      );
    }
    
    @keyframes move {
      0% {
        offset-distance: 0%;
      }
      100% {
        offset-distance: 100%;
        background-color: hotpink;
      }
    }
    

#### Result

### [Using `shape()` to define the visible part of an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#using_shape_to_define_the_visible_part_of_an_element)

This example demonstrates how the `shape()` function can be used in the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property to create different shapes for the clipping region. The first shape (`shape1`) uses a triangle defined by straight lines. The second shape (`shape2`) includes curves and smooth transitions; it also illustrates the use of the `<move-command>` after the `close` command, which adds a rectangular shape to the clipping region.

    <div class="container">
      <div class="shape shape1"></div>
    </div>
    
    <div class="container">
      <div class="shape shape2"></div>
    </div>
    

    body {
      align-items: center;
      justify-content: center;
      display: flex;
    }
    
    .container {
      position: relative;
      display: inline-block;
      width: 200px;
      height: 200px;
      margin: 20px;
      background-color: lightgray;
    }
    
    @supports not (clip-path: shape(from 0 0, move to 0 0)) {
      body::after {
        content: "Your browser doesn't support the `shape()` function yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    .shape {
      width: 100%;
      height: 100%;
      background: #2bc4a2;
      position: absolute;
      text-align: center;
      line-height: 50px;
    }
    
    /* Triangular clipping region */
    .shape1 {
      clip-path: shape(from 0% 0%, line to 100% 0%, line to 50% 100%, close);
    }
    
    /* A Heart clipping region using curve and arc transitions
       and a box using hline and vline transitions */
    .shape2 {
      clip-path: shape(
        from 20px 70px,
        arc to 100px 70px of 1% cw,
        arc to 180px 70px of 1% cw,
        curve to 100px 190px with 180px 130px,
        curve to 20px 70px with 20px 130px,
        close,
        move to 150px 150px,
        hline by 40px,
        vline by 40px,
        hline by -40px,
        close
      );
    }
    

#### Result

### [Using `shape()` to draw curves with relative control points](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#using_shape_to_draw_curves_with_relative_control_points)

Like previous examples, this example also uses [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 to create different shapes for the clipping regions of the elements. The shapes are specified using a combination of [`<curve-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#curve-command)
 and [`<smooth-command>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#smooth-command)
, and the control points are specified using [`<relative-control-point>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#relative-control-point)
 values.

The first shape (`shape1`) draws two cubic Bézier curves.

*   The first curve starts from the center of the left edge of the box and is drawn to a point `200px` along the x-axis — the center of the box's right edge. It uses one control point relative to the start of the curve and one control point relative to the origin (top-left of the box).
*   The second curve starts from the center right of the box and is drawn `-200px` along the x-axis — the center of the box's left edge. It uses one control point relative to the origin and one control point relative to the start of the curve.

    <div class="container">
      <div id="shape1"></div>
      <div id="shape2"></div>
      <div id="shape3"></div>
    </div>
    

    .container {
      display: flex;
      justify-content: center;
      gap: 20px;
    }
    
    @supports not (
      clip-path: shape(
          from center left,
          curve by 200px 0 with 50% -50% from start / 50% 0 from origin,
          curve by -200px 0 with 50% 100% from origin / -50% 50% from start,
          close
        )
    ) {
      body::after {
        content: "Your browser doesn't support `shape()` relative control points.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    #shape1 {
      width: 200px;
      height: 200px;
      background: green;
      clip-path: shape(
        from center left,
        curve by 200px 0 with 50% -50% from start / 50% 0 from origin,
        curve by -200px 0 with 50% 100% from origin / -50% 50% from start,
        close
      );
    }
    

The second shape (`shape2`) draws one quadratic Bézier curve and one cubic Bézier curve.

*   The first curve starts from the center of the left edge of the box and is drawn to an absolute point `200px` from the origin along the x-axis and `100px` from the origin along the y-axis. It uses one control point relative to the start of the curve.
*   The second curve starts from the previous curve's end point and is drawn to the center left of the box. It uses one control point relative to the start of the curve and one control point relative to the end.

css

    #shape2 {
      width: 200px;
      height: 200px;
      background: purple;
      clip-path: shape(
        from center left,
        curve to 200px 100px with 50% -80% from start,
        curve to center left with 0% 70% from start / 20% 0% from end,
        close
      );
    }
    

The third shape (`shape3`) draws one quadratic Bézier curve and one cubic Bézier curve using a `smooth` command.

*   The first curve starts from the center of the left edge of the box and is drawn to a point `200px` along the x-axis. It uses one control point relative to the start of the curve.
*   The second curve starts from the previous curve's end point and is drawn to the center of the box. It uses one control point relative to the start of the curve (the last control point of the previous curve) and one control point relative to the origin.

css

    #shape3 {
      width: 200px;
      height: 200px;
      background: orangered;
      clip-path: shape(
        from center left,
        curve by 200px 0px with 50% -80% from start,
        smooth to center with 50% 100% from origin,
        close
      );
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 2  <br>\# shape-function](https://drafts.csswg.org/css-shapes-2/#shape-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape#see_also)

---------------------------------------------------------------------------------------------------------

*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
*   [Overview of shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
     guide
*   [Basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/shape/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fshape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fshape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fshape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fshape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")