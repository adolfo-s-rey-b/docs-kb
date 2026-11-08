[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.reorder_levels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.reorder_levels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.reorder_levels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.reorder_levels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.reorder_levels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.reorder_levels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.reorder_levels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.reorder_levels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.reorder_levels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.reorder_levels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.reorder_levels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.reorder_levels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.reorder\_levels[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas-dataframe-reorder-levels "Link to this heading")

==============================================================================================================================================================================

DataFrame.reorder\_levels(_order_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L10054-L10114)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "Link to this definition")

Rearrange index or column levels using input `order`.

May not drop or duplicate levels.

Parameters:

**order**list of int or list of str

List representing new level order. Reference level by number (position) or by key (label).

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Where to reorder levels.

Returns:

DataFrame

DataFrame with indices or columns with reordered levels.

See also

[`DataFrame.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "pandas.DataFrame.swaplevel")

Swap levels i and j in a MultiIndex.

Examples

\>>> data \= {
...     "class": \["Mammals", "Mammals", "Reptiles"\],
...     "diet": \["Omnivore", "Carnivore", "Carnivore"\],
...     "species": \["Humans", "Dogs", "Snakes"\],
... }
\>>> df \= pd.DataFrame(data, columns\=\["class", "diet", "species"\])
\>>> df \= df.set\_index(\["class", "diet"\])
\>>> df
                                  species
class      diet
Mammals    Omnivore                Humans
           Carnivore                 Dogs
Reptiles   Carnivore               Snakes

Copy to clipboard

Let’s reorder the levels of the index:

\>>> df.reorder\_levels(\["diet", "class"\])
                                  species
diet      class
Omnivore  Mammals                  Humans
Carnivore Mammals                    Dogs
          Reptiles                 Snakes

Copy to clipboard

On this page