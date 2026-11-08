[Skip to content](https://ggplot2.tidyverse.org/reference/draw_key.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Key glyphs for legends
======================

Source: [`R/legend-draw.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/legend-draw.R)

`draw_key.Rd`

Each geom has an associated function that draws the key when the geom needs to be displayed in a legend. These functions are called `draw_key_*()`, where `*` stands for the name of the respective key glyph. The key glyphs can be customized for individual geoms by providing a geom with the `key_glyph` argument (see `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) ` or examples below.)

Usage[](https://ggplot2.tidyverse.org/reference/draw_key.html#ref-usage)

-------------------------------------------------------------------------

    draw_key_point(data, params, size)
    
    draw_key_abline(data, params, size)
    
    draw_key_rect(data, params, size)
    
    draw_key_polygon(data, params, size)
    
    draw_key_blank(data, params, size)
    
    draw_key_boxplot(data, params, size)
    
    draw_key_crossbar(data, params, size)
    
    draw_key_path(data, params, size)
    
    draw_key_vpath(data, params, size)
    
    draw_key_dotplot(data, params, size)
    
    draw_key_linerange(data, params, size)
    
    draw_key_pointrange(data, params, size)
    
    draw_key_smooth(data, params, size)
    
    draw_key_text(data, params, size)
    
    draw_key_label(data, params, size)
    
    draw_key_vline(data, params, size)
    
    draw_key_timeseries(data, params, size)

Arguments[](https://ggplot2.tidyverse.org/reference/draw_key.html#arguments)

-----------------------------------------------------------------------------

data[](https://ggplot2.tidyverse.org/reference/draw_key.html#arg-data)

A single row data frame containing the scaled aesthetics to display in this key

params[](https://ggplot2.tidyverse.org/reference/draw_key.html#arg-params)

A list of additional parameters supplied to the geom.

size[](https://ggplot2.tidyverse.org/reference/draw_key.html#arg-size)

Width and height of key in mm.

Value[](https://ggplot2.tidyverse.org/reference/draw_key.html#value)

---------------------------------------------------------------------

A grid grob.

Examples[](https://ggplot2.tidyverse.org/reference/draw_key.html#ref-examples)

-------------------------------------------------------------------------------

    p <- ggplot(economics, aes(date, psavert, color = "savings rate"))
    # key glyphs can be specified by their name
    p + geom_line(key_glyph = "timeseries")
    
    
    # key glyphs can be specified via their drawing function
    p + geom_line(key_glyph = draw_key_rect)