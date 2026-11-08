[Skip to content](https://ggplot2.tidyverse.org/reference/map_data.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Create a data frame of map data
===============================

Source: [`R/fortify-map.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/fortify-map.R)

`map_data.Rd`

Easily turn data from the maps package into a data frame suitable for plotting with ggplot2.

Usage[](https://ggplot2.tidyverse.org/reference/map_data.html#ref-usage)

-------------------------------------------------------------------------

    map_data(map, region = ".", exact = FALSE, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/map_data.html#arguments)

-----------------------------------------------------------------------------

map[](https://ggplot2.tidyverse.org/reference/map_data.html#arg-map)

name of map provided by the maps package. These include `["county"](https://rdrr.io/pkg/maps/man/county.html) `, `["france"](https://rdrr.io/pkg/maps/man/france.html) `, `["italy"](https://rdrr.io/pkg/maps/man/italy.html) `, `["nz"](https://rdrr.io/pkg/maps/man/nz.html) `, `["state"](https://rdrr.io/pkg/maps/man/state.html) `, `["usa"](https://rdrr.io/pkg/maps/man/usa.html) `, `["world"](https://rdrr.io/pkg/maps/man/world.html) `, or `["world2"](https://rdrr.io/pkg/maps/man/world2.html) `.

region[](https://ggplot2.tidyverse.org/reference/map_data.html#arg-region)

name(s) of subregion(s) to include. Defaults to `.` which includes all subregions. See documentation for `[maps::map()](https://rdrr.io/pkg/maps/man/map.html) ` for more details.

exact[](https://ggplot2.tidyverse.org/reference/map_data.html#arg-exact)

should the `region` be treated as a regular expression (`FALSE`) or as a fixed string (`TRUE`).

...[](https://ggplot2.tidyverse.org/reference/map_data.html#arg--)

all other arguments passed on to `[maps::map()](https://rdrr.io/pkg/maps/man/map.html) `

Examples[](https://ggplot2.tidyverse.org/reference/map_data.html#ref-examples)

-------------------------------------------------------------------------------

    if (require("maps")) {
    states <- map_data("state")
    arrests <- USArrests
    names(arrests) <- tolower(names(arrests))
    arrests$region <- tolower(rownames(USArrests))
    
    choro <- merge(states, arrests, sort = FALSE, by = "region")
    choro <- choro[order(choro$order), ]
    ggplot(choro, aes(long, lat)) +
      geom_polygon(aes(group = group, fill = assault)) +
      coord_map("albers",  lat0 = 45.5, lat1 = 29.5)
    }
    
    
    if (require("maps")) {
    ggplot(choro, aes(long, lat)) +
      geom_polygon(aes(group = group, fill = assault / murder)) +
      coord_map("albers",  lat0 = 45.5, lat1 = 29.5)
    }