[Skip to main content](https://pandas.pydata.org/docs/user_guide/cookbook.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Cookbook[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook "Link to this heading")

=====================================================================================================

This is a repository for _short and sweet_ examples and links for useful pandas recipes.

Simplified, condensed, new-user friendly, in-line examples have been inserted where possible to augment the Stack-Overflow and GitHub links. Many of the links contain expanded information, above what the in-line examples offer.

pandas (pd) and NumPy (np) are the only two abbreviated imported modules. The rest are kept explicitly imported for newer users.

Idioms[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#idioms "Link to this heading")

-------------------------------------------------------------------------------------------------

These are some neat pandas `idioms`

[if-then/if-then-else on one column, and assignment to another one or more columns:](https://stackoverflow.com/questions/17128302/python-pandas-idiom-for-if-then-else)

In \[1\]: df \= pd.DataFrame(
   ...:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ...: )
   ...: 

In \[2\]: df
Out\[2\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

Copy to clipboard

### If-then…[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#if-then "Link to this heading")

An if-then on one column

In \[3\]: df.loc\[df.AAA \>= 5, "BBB"\] \= \-1

In \[4\]: df
Out\[4\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   -1   50
2    6   -1  -30
3    7   -1  -50

Copy to clipboard

An if-then with assignment to 2 columns:

In \[5\]: df.loc\[df.AAA \>= 5, \["BBB", "CCC"\]\] \= 555

In \[6\]: df
Out\[6\]: 
   AAA  BBB  CCC
0    4   10  100
1    5  555  555
2    6  555  555
3    7  555  555

Copy to clipboard

Add another line with different logic, to do the -else

In \[7\]: df.loc\[df.AAA < 5, \["BBB", "CCC"\]\] \= 2000

In \[8\]: df
Out\[8\]: 
   AAA   BBB   CCC
0    4  2000  2000
1    5   555   555
2    6   555   555
3    7   555   555

Copy to clipboard

Or use pandas where after you’ve set up a mask

In \[9\]: df\_mask \= pd.DataFrame(
   ...:    {"AAA": \[True\] \* 4, "BBB": \[False\] \* 4, "CCC": \[True, False\] \* 2}
   ...: )
   ...: 

In \[10\]: df.where(df\_mask, \-1000)
Out\[10\]: 
   AAA   BBB   CCC
0    4 -1000  2000
1    5 -1000 -1000
2    6 -1000   555
3    7 -1000 -1000

Copy to clipboard

[if-then-else using NumPy’s where()](https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column)

In \[11\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[12\]: df
Out\[12\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[13\]: df\["logic"\] \= np.where(df\["AAA"\] \> 5, "high", "low")

In \[14\]: df
Out\[14\]: 
   AAA  BBB  CCC logic
0    4   10  100   low
1    5   20   50   low
2    6   30  -30  high
3    7   40  -50  high

Copy to clipboard

### Splitting[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#splitting "Link to this heading")

[Split a frame with a boolean criterion](https://stackoverflow.com/questions/14957116/how-to-split-a-dataframe-according-to-a-boolean-criterion)

In \[15\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[16\]: df
Out\[16\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[17\]: df\[df.AAA <= 5\]
Out\[17\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50

In \[18\]: df\[df.AAA \> 5\]
Out\[18\]: 
   AAA  BBB  CCC
2    6   30  -30
3    7   40  -50

Copy to clipboard

### Building criteria[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#building-criteria "Link to this heading")

[Select with multi-column criteria](https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe)

In \[19\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[20\]: df
Out\[20\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

Copy to clipboard

…and (without assignment returns a Series)

In \[21\]: df.loc\[(df\["BBB"\] < 25) & (df\["CCC"\] \>= \-40), "AAA"\]
Out\[21\]: 
0    4
1    5
Name: AAA, dtype: int64

Copy to clipboard

…or (without assignment returns a Series)

In \[22\]: df.loc\[(df\["BBB"\] \> 25) | (df\["CCC"\] \>= \-40), "AAA"\]
Out\[22\]: 
0    4
1    5
2    6
3    7
Name: AAA, dtype: int64

Copy to clipboard

…or (with assignment modifies the DataFrame.)

In \[23\]: df.loc\[(df\["BBB"\] \> 25) | (df\["CCC"\] \>= 75), "AAA"\] \= 999

In \[24\]: df
Out\[24\]: 
   AAA  BBB  CCC
0  999   10  100
1    5   20   50
2  999   30  -30
3  999   40  -50

Copy to clipboard

[Select rows with data closest to certain value using argsort](https://stackoverflow.com/questions/17758023/return-rows-in-a-dataframe-closest-to-a-user-defined-number)

In \[25\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[26\]: df
Out\[26\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[27\]: aValue \= 43.0

In \[28\]: df.loc\[(df.CCC \- aValue).abs().argsort()\]
Out\[28\]: 
   AAA  BBB  CCC
1    5   20   50
0    4   10  100
2    6   30  -30
3    7   40  -50

Copy to clipboard

[Dynamically reduce a list of criteria using a binary operators](https://stackoverflow.com/questions/21058254/pandas-boolean-operation-in-a-python-list/21058331)

In \[29\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[30\]: df
Out\[30\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[31\]: Crit1 \= df.AAA <= 5.5

In \[32\]: Crit2 \= df.BBB \== 10.0

In \[33\]: Crit3 \= df.CCC \> \-40.0

Copy to clipboard

One could hard code:

In \[34\]: AllCrit \= Crit1 & Crit2 & Crit3

Copy to clipboard

…Or it can be done with a list of dynamically built criteria

In \[35\]: import functools

In \[36\]: CritList \= \[Crit1, Crit2, Crit3\]

In \[37\]: AllCrit \= functools.reduce(lambda x, y: x & y, CritList)

In \[38\]: df\[AllCrit\]
Out\[38\]: 
   AAA  BBB  CCC
0    4   10  100

Copy to clipboard

### Repeating rows or columns[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#repeating-rows-or-columns "Link to this heading")

Unlike [`Series.repeat()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas.Series.repeat "pandas.Series.repeat")
, `DataFrame` has no `repeat` method. The same result can be achieved by repeating the row (or column) labels and passing them to [`DataFrame.reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")
. This requires the labels on the repeated axis to be unique [GH 42943](https://github.com/pandas-dev/pandas/issues/42943)

In \[39\]: df \= pd.DataFrame({"AAA": \[1, 2\], "BBB": \[3, 4\]})

In \[40\]: df.reindex(df.index.repeat(2))
Out\[40\]: 
   AAA  BBB
0    1    3
0    1    3
1    2    4
1    2    4

In \[41\]: df.reindex(df.index.repeat(2)).reset\_index(drop\=True)
Out\[41\]: 
   AAA  BBB
0    1    3
1    1    3
2    2    4
3    2    4

In \[42\]: df.reindex(columns\=df.columns.repeat(\[1, 2\]))
Out\[42\]: 
   AAA  BBB  BBB
0    1    3    3
1    2    4    4

Copy to clipboard

Repeating positions with [`DataFrame.iloc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")
 instead works whether or not the labels are unique:

In \[43\]: df.iloc\[np.repeat(np.arange(len(df)), 2)\]
Out\[43\]: 
   AAA  BBB
0    1    3
0    1    3
1    2    4
1    2    4

Copy to clipboard

### Expanding ranges into rows[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#expanding-ranges-into-rows "Link to this heading")

Given columns of `start` and `stop` values, expand each row into one row per value in `range(start, stop)`. Applying `range` row-wise and calling [`Series.explode()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas.Series.explode "pandas.Series.explode")
 is simple but slow for large inputs; a vectorized construction with [`numpy.repeat()`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "(in NumPy v2.5)")
 is much faster, especially when there are many rows to expand [GH 39630](https://github.com/pandas-dev/pandas/issues/39630)

In \[44\]: df \= pd.DataFrame({"start": \[10, 27, 30\], "stop": \[15, 31, 31\]})

In \[45\]: start \= df\["start"\].to\_numpy()

In \[46\]: stop \= df\["stop"\].to\_numpy()

In \[47\]: counts \= stop \- start

In \[48\]: offsets \= np.arange(counts.sum()) \- np.repeat(counts.cumsum() \- counts, counts)

In \[49\]: pd.Series(np.repeat(start, counts) + offsets, index\=df.index.repeat(counts))
Out\[49\]: 
0    10
0    11
0    12
0    13
0    14
1    27
1    28
1    29
1    30
2    30
dtype: int64

Copy to clipboard

Selection[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#selection "Link to this heading")

-------------------------------------------------------------------------------------------------------

### DataFrames[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#dataframes "Link to this heading")

The [indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
 docs.

[Using both row labels and value conditionals](https://stackoverflow.com/questions/14725068/pandas-using-row-labels-in-boolean-indexing)

In \[50\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[51\]: df
Out\[51\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[52\]: df\[(df.AAA <= 6) & (df.index.isin(\[0, 2, 4\]))\]
Out\[52\]: 
   AAA  BBB  CCC
0    4   10  100
2    6   30  -30

Copy to clipboard

Use loc for label-oriented slicing and iloc positional slicing [GH 2904](https://github.com/pandas-dev/pandas/issues/2904)

In \[53\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]},
   ....:    index\=\["foo", "bar", "boo", "kar"\],
   ....: )
   ....: 

Copy to clipboard

There are 2 explicit slicing methods, with a third general case

1.  Positional-oriented (Python slicing style : exclusive of end)
    
2.  Label-oriented (Non-Python slicing style : inclusive of end)
    
3.  General (Either slicing style : depends on if the slice contains labels or positions)
    

In \[54\]: df.loc\["bar":"kar"\]  \# Label
Out\[54\]: 
     AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

\# Generic
In \[55\]: df\[0:3\]
Out\[55\]: 
     AAA  BBB  CCC
foo    4   10  100
bar    5   20   50
boo    6   30  -30

In \[56\]: df\["bar":"kar"\]
Out\[56\]: 
     AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

Copy to clipboard

Ambiguity arises when an index consists of integers with a non-zero start or non-unit increment.

In \[57\]: data \= {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}

In \[58\]: df2 \= pd.DataFrame(data\=data, index\=\[1, 2, 3, 4\])  \# Note index starts at 1.

In \[59\]: df2.iloc\[1:3\]  \# Position-oriented
Out\[59\]: 
   AAA  BBB  CCC
2    5   20   50
3    6   30  -30

In \[60\]: df2.loc\[1:3\]  \# Label-oriented
Out\[60\]: 
   AAA  BBB  CCC
1    4   10  100
2    5   20   50
3    6   30  -30

Copy to clipboard

[Using inverse operator (~) to take the complement of a mask](https://stackoverflow.com/q/14986510)

In \[61\]: df \= pd.DataFrame(
   ....:    {"AAA": \[4, 5, 6, 7\], "BBB": \[10, 20, 30, 40\], "CCC": \[100, 50, \-30, \-50\]}
   ....: )
   ....: 

In \[62\]: df
Out\[62\]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In \[63\]: df\[~((df.AAA <= 6) & (df.index.isin(\[0, 2, 4\])))\]
Out\[63\]: 
   AAA  BBB  CCC
1    5   20   50
3    7   40  -50

Copy to clipboard

[How to randomly extract n contiguous rows in a pandas DataFrame?](https://stackoverflow.com/questions/67349588/how-to-randomly-extract-n-contiguous-rows-in-a-pandas-dataframe)

In \[64\]: df \= pd.DataFrame({
   ....:    'A': range(10),
   ....:    'B': range(10),
   ....:    'C': range(10)
   ....: })
   ....: 

In \[65\]: window\_size \= 5

In \[66\]: start\_idx \= np.random.randint(0, len(df) \- window\_size + 1)

In \[67\]: df.iloc\[start\_idx:start\_idx+window\_size\]
Out\[67\]: 
   A  B  C
1  1  1  1
2  2  2  2
3  3  3  3
4  4  4  4
5  5  5  5

Copy to clipboard

### New columns[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#new-columns "Link to this heading")

[Efficiently and dynamically creating new columns using DataFrame.map (previously named applymap)](https://stackoverflow.com/questions/16575868/efficiently-creating-additional-columns-in-a-pandas-dataframe-using-map)

In \[68\]: df \= pd.DataFrame({"AAA": \[1, 2, 1, 3\], "BBB": \[1, 1, 2, 2\], "CCC": \[2, 1, 3, 1\]})

In \[69\]: df
Out\[69\]: 
   AAA  BBB  CCC
0    1    1    2
1    2    1    1
2    1    2    3
3    3    2    1

In \[70\]: source\_cols \= df.columns  \# Or some subset would work too

In \[71\]: new\_cols \= \[str(x) + "\_cat" for x in source\_cols\]

In \[72\]: categories \= {1: "Alpha", 2: "Beta", 3: "Charlie"}

In \[73\]: df\[new\_cols\] \= df\[source\_cols\].map(categories.get)

In \[74\]: df
Out\[74\]: 
   AAA  BBB  CCC  AAA\_cat BBB\_cat  CCC\_cat
0    1    1    2    Alpha   Alpha     Beta
1    2    1    1     Beta   Alpha    Alpha
2    1    2    3    Alpha    Beta  Charlie
3    3    2    1  Charlie    Beta    Alpha

Copy to clipboard

[Keep other columns when using min() with groupby](https://stackoverflow.com/q/23394476)

In \[75\]: df \= pd.DataFrame(
   ....:    {"AAA": \[1, 1, 1, 2, 2, 2, 3, 3\], "BBB": \[2, 1, 3, 4, 5, 1, 2, 3\]}
   ....: )
   ....: 

In \[76\]: df
Out\[76\]: 
   AAA  BBB
0    1    2
1    1    1
2    1    3
3    2    4
4    2    5
5    2    1
6    3    2
7    3    3

Copy to clipboard

Method 1 : idxmin() to get the index of the minimums

In \[77\]: df.loc\[df.groupby("AAA")\["BBB"\].idxmin()\]
Out\[77\]: 
   AAA  BBB
1    1    1
5    2    1
6    3    2

Copy to clipboard

Method 2 : sort then take first of each

In \[78\]: df.sort\_values(by\="BBB").groupby("AAA", as\_index\=False).first()
Out\[78\]: 
   AAA  BBB
0    1    1
1    2    1
2    3    2

Copy to clipboard

Notice the same results, with the exception of the index.

Multiindexing[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#multiindexing "Link to this heading")

---------------------------------------------------------------------------------------------------------------

The [multindexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-hierarchical)
 docs.

[Creating a MultiIndex from a labeled frame](https://stackoverflow.com/questions/14916358/reshaping-dataframes-in-pandas-based-on-column-labels)

In \[79\]: df \= pd.DataFrame(
   ....:    {
   ....:        "row": \[0, 1, 2\],
   ....:        "One\_X": \[1.1, 1.1, 1.1\],
   ....:        "One\_Y": \[1.2, 1.2, 1.2\],
   ....:        "Two\_X": \[1.11, 1.11, 1.11\],
   ....:        "Two\_Y": \[1.22, 1.22, 1.22\],
   ....:    }
   ....: )
   ....: 

In \[80\]: df
Out\[80\]: 
   row  One\_X  One\_Y  Two\_X  Two\_Y
0    0    1.1    1.2   1.11   1.22
1    1    1.1    1.2   1.11   1.22
2    2    1.1    1.2   1.11   1.22

\# As Labelled Index
In \[81\]: df \= df.set\_index("row")

In \[82\]: df
Out\[82\]: 
     One\_X  One\_Y  Two\_X  Two\_Y
row                            
0      1.1    1.2   1.11   1.22
1      1.1    1.2   1.11   1.22
2      1.1    1.2   1.11   1.22

\# With Hierarchical Columns
In \[83\]: df.columns \= pd.MultiIndex.from\_tuples(\[tuple(c.split("\_")) for c in df.columns\])

In \[84\]: df
Out\[84\]: 
     One        Two      
       X    Y     X     Y
row                      
0    1.1  1.2  1.11  1.22
1    1.1  1.2  1.11  1.22
2    1.1  1.2  1.11  1.22

\# Now stack & Reset
In \[85\]: df \= df.stack(0).reset\_index(1)

In \[86\]: df
Out\[86\]: 
    level\_1     X     Y
row                    
0       One  1.10  1.20
0       Two  1.11  1.22
1       One  1.10  1.20
1       Two  1.11  1.22
2       One  1.10  1.20
2       Two  1.11  1.22

\# And fix the labels (Notice the label 'level\_1' got added automatically)
In \[87\]: df.columns \= \["Sample", "All\_X", "All\_Y"\]

In \[88\]: df
Out\[88\]: 
    Sample  All\_X  All\_Y
row                     
0      One   1.10   1.20
0      Two   1.11   1.22
1      One   1.10   1.20
1      Two   1.11   1.22
2      One   1.10   1.20
2      Two   1.11   1.22

Copy to clipboard

### Arithmetic[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#arithmetic "Link to this heading")

[Performing arithmetic with a MultiIndex that needs broadcasting](https://stackoverflow.com/questions/19501510/divide-entire-pandas-multiindex-dataframe-by-dataframe-variable/19502176#19502176)

In \[89\]: cols \= pd.MultiIndex.from\_tuples(
   ....:    \[(x, y) for x in \["A", "B", "C"\] for y in \["O", "I"\]\]
   ....: )
   ....: 

In \[90\]: df \= pd.DataFrame(np.random.randn(2, 6), index\=\["n", "m"\], columns\=cols)

In \[91\]: df
Out\[91\]: 
          A                   B                   C          
          O         I         O         I         O         I
n  0.952516  0.035680  0.974184  0.719101  0.184765  0.619326
m -1.138680 -0.641576  0.443212 -0.110240 -0.166778  0.501113

In \[92\]: df \= df.div(df\["C"\], level\=1)

In \[93\]: df
Out\[93\]: 
          A                   B              C     
          O         I         O         I    O    I
n  5.155278  0.057611  5.272551  1.161103  1.0  1.0
m  6.827507 -1.280302 -2.657489 -0.219990  1.0  1.0

Copy to clipboard

### Slicing[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#slicing "Link to this heading")

[Slicing a MultiIndex with xs](https://stackoverflow.com/questions/12590131/how-to-slice-multindex-columns-in-pandas-dataframes)

In \[94\]: coords \= \[("AA", "one"), ("AA", "six"), ("BB", "one"), ("BB", "two"), ("BB", "six")\]

In \[95\]: index \= pd.MultiIndex.from\_tuples(coords)

In \[96\]: df \= pd.DataFrame(\[11, 22, 33, 44, 55\], index, \["MyData"\])

In \[97\]: df
Out\[97\]: 
        MyData
AA one      11
   six      22
BB one      33
   two      44
   six      55

Copy to clipboard

To take the cross section of the 1st level and 1st axis the index:

\# Note : level and axis are optional, and default to zero
In \[98\]: df.xs("BB", level\=0, axis\=0)
Out\[98\]: 
     MyData
one      33
two      44
six      55

Copy to clipboard

…and now the 2nd level of the 1st axis.

In \[99\]: df.xs("six", level\=1, axis\=0)
Out\[99\]: 
    MyData
AA      22
BB      55

Copy to clipboard

[Slicing a MultiIndex with xs, method #2](https://stackoverflow.com/questions/14964493/multiindex-based-indexing-in-pandas)

In \[100\]: import itertools

In \[101\]: index \= list(itertools.product(\["Ada", "Quinn", "Violet"\], \["Comp", "Math", "Sci"\]))

In \[102\]: headr \= list(itertools.product(\["Exams", "Labs"\], \["I", "II"\]))

In \[103\]: indx \= pd.MultiIndex.from\_tuples(index, names\=\["Student", "Course"\])

In \[104\]: cols \= pd.MultiIndex.from\_tuples(headr)  \# Notice these are un-named

In \[105\]: data \= \[\[70 + x + y + (x \* y) % 3 for x in range(4)\] for y in range(9)\]

In \[106\]: df \= pd.DataFrame(data, indx, cols)

In \[107\]: df
Out\[107\]: 
               Exams     Labs    
                   I  II    I  II
Student Course                   
Ada     Comp      70  71   72  73
        Math      71  73   75  74
        Sci       72  75   75  75
Quinn   Comp      73  74   75  76
        Math      74  76   78  77
        Sci       75  78   78  78
Violet  Comp      76  77   78  79
        Math      77  79   81  80
        Sci       78  81   81  81

In \[108\]: All \= slice(None)

In \[109\]: df.loc\["Violet"\]
Out\[109\]: 
       Exams     Labs    
           I  II    I  II
Course                   
Comp      76  77   78  79
Math      77  79   81  80
Sci       78  81   81  81

In \[110\]: df.loc\[(All, "Math"), All\]
Out\[110\]: 
               Exams     Labs    
                   I  II    I  II
Student Course                   
Ada     Math      71  73   75  74
Quinn   Math      74  76   78  77
Violet  Math      77  79   81  80

In \[111\]: df.loc\[(slice("Ada", "Quinn"), "Math"), All\]
Out\[111\]: 
               Exams     Labs    
                   I  II    I  II
Student Course                   
Ada     Math      71  73   75  74
Quinn   Math      74  76   78  77

In \[112\]: df.loc\[(All, "Math"), ("Exams")\]
Out\[112\]: 
                 I  II
Student Course        
Ada     Math    71  73
Quinn   Math    74  76
Violet  Math    77  79

In \[113\]: df.loc\[(All, "Math"), (All, "II")\]
Out\[113\]: 
               Exams Labs
                  II   II
Student Course           
Ada     Math      73   74
Quinn   Math      76   77
Violet  Math      79   80

Copy to clipboard

[Setting portions of a MultiIndex with xs](https://stackoverflow.com/questions/19319432/pandas-selecting-a-lower-level-in-a-dataframe-to-do-a-ffill)

### Sorting[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#sorting "Link to this heading")

[Sort by specific column or an ordered list of columns, with a MultiIndex](https://stackoverflow.com/q/14733871)

In \[114\]: df.sort\_values(by\=("Labs", "II"), ascending\=False)
Out\[114\]: 
               Exams     Labs    
                   I  II    I  II
Student Course                   
Violet  Sci       78  81   81  81
        Math      77  79   81  80
        Comp      76  77   78  79
Quinn   Sci       75  78   78  78
        Math      74  76   78  77
        Comp      73  74   75  76
Ada     Sci       72  75   75  75
        Math      71  73   75  74
        Comp      70  71   72  73

Copy to clipboard

Partial selection, the need for sortedness [GH 2995](https://github.com/pandas-dev/pandas/issues/2995)

### Levels[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#levels "Link to this heading")

[Prepending a level to a multiindex](https://stackoverflow.com/questions/14744068/prepend-a-level-to-a-pandas-multiindex)

In \[115\]: df \= pd.DataFrame(
   .....:    {"A": \["a1", "a1", "a2", "a3"\], "B": \["b1", "b2", "b3", "b4"\], "Vals": np.random.randn(4)}
   .....: ).groupby(\["A", "B"\]).sum()
   .....: 

In \[116\]: df
Out\[116\]: 
           Vals
A  B           
a1 b1 -0.355322
   b2 -0.337890
a2 b3  0.580967
a3 b4  0.983801

Copy to clipboard

Prepend a constant label to the existing row MultiIndex using `pd.concat` with the `keys` argument:

In \[117\]: df \= pd.concat(\[df\], keys\=\["Foo"\], names\=\["FirstLevel"\])

In \[118\]: df
Out\[118\]: 
                      Vals
FirstLevel A  B           
Foo        a1 b1 -0.355322
              b2 -0.337890
           a2 b3  0.580967
           a3 b4  0.983801

Copy to clipboard

[Flatten Hierarchical columns](https://stackoverflow.com/q/14507794)

In \[119\]: df \= pd.DataFrame(
   .....:    {
   .....:        "USAF": \["702730"\] \* 4,
   .....:        "WBAN": \[26451\] \* 4,
   .....:        "day": \[1, 2, 3, 4\],
   .....:        "s\_PC": \[1, 0, 1, 3\],
   .....:        "s\_CL": \[0, 0, 10, 0\],
   .....:        "tempf": \[30.92, 32.00, 23.00, 10.04\],
   .....:    }
   .....: )
   .....: 

In \[120\]: df \= df.groupby(\["USAF", "WBAN", "day"\]).agg(
   .....:    {"s\_PC": "sum", "s\_CL": "sum", "tempf": \["max", "min"\]}
   .....: ).reset\_index()
   .....: 

In \[121\]: df
Out\[121\]: 
     USAF   WBAN day s\_PC s\_CL  tempf       
                      sum  sum    max    min
0  702730  26451   1    1    0  30.92  30.92
1  702730  26451   2    0    0  32.00  32.00
2  702730  26451   3    1   10  23.00  23.00
3  702730  26451   4    3    0  10.04  10.04

Copy to clipboard

Use a generator expression to drop the empty-string second levels before joining, so `("USAF", "")` becomes `"USAF"` rather than `"USAF_"`. Columns with a real aggregation label are joined normally, so `("tempf", "max")` becomes `"tempf_max"` and `("s_PC", "sum")` becomes `"s_PC_sum"`:

In \[122\]: df.columns \= \["\_".join(c for c in col if c) for col in df.columns\]

In \[123\]: df
Out\[123\]: 
     USAF   WBAN  day  s\_PC\_sum  s\_CL\_sum  tempf\_max  tempf\_min
0  702730  26451    1         1         0      30.92      30.92
1  702730  26451    2         0         0      32.00      32.00
2  702730  26451    3         1        10      23.00      23.00
3  702730  26451    4         3         0      10.04      10.04

Copy to clipboard

Missing data[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#missing-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The [missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
 docs.

Fill forward a reversed timeseries

In \[124\]: df \= pd.DataFrame(
   .....:    np.random.randn(6, 1),
   .....:    index\=pd.date\_range("2013-08-01", periods\=6, freq\="B"),
   .....:    columns\=list("A"),
   .....: )
   .....: 

In \[125\]: df.loc\[df.index\[3\], "A"\] \= np.nan

In \[126\]: df
Out\[126\]: 
                   A
2013-08-01  0.057802
2013-08-02  0.761948
2013-08-05 -0.712964
2013-08-06       NaN
2013-08-07 -0.974602
2013-08-08  1.047704

In \[127\]: df.bfill()
Out\[127\]: 
                   A
2013-08-01  0.057802
2013-08-02  0.761948
2013-08-05 -0.712964
2013-08-06 -0.974602
2013-08-07 -0.974602
2013-08-08  1.047704

Copy to clipboard

[cumsum reset at NaN values](https://stackoverflow.com/questions/18196811/cumsum-reset-at-nan)

### Replace[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#replace "Link to this heading")

[Using replace with backrefs](https://stackoverflow.com/questions/16818871/extracting-value-and-creating-new-column-out-of-it)

Grouping[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#grouping "Link to this heading")

-----------------------------------------------------------------------------------------------------

The [grouping](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
 docs.

[Basic grouping with apply](https://stackoverflow.com/questions/15322632/python-pandas-df-groupy-agg-column-reference-in-agg)

Unlike agg, apply’s callable is passed a sub-DataFrame which gives you access to all the columns

In \[128\]: df \= pd.DataFrame(
   .....:    {
   .....:        "animal": "cat dog cat fish dog cat cat".split(),
   .....:        "size": list("SSMMMLL"),
   .....:        "weight": \[8, 10, 11, 1, 20, 12, 12\],
   .....:        "adult": \[False\] \* 5 + \[True\] \* 2,
   .....:    }
   .....: )
   .....: 

In \[129\]: df
Out\[129\]: 
  animal size  weight  adult
0    cat    S       8  False
1    dog    S      10  False
2    cat    M      11  False
3   fish    M       1  False
4    dog    M      20  False
5    cat    L      12   True
6    cat    L      12   True

\# List the size of the animals with the highest weight.
In \[130\]: df.groupby("animal").apply(lambda subf: subf\["size"\]\[subf\["weight"\].idxmax()\])
Out\[130\]: 
animal
cat     L
dog     M
fish    M
dtype: str

Copy to clipboard

[Using get\_group](https://stackoverflow.com/questions/14734533/how-to-access-pandas-groupby-dataframe-by-key)

In \[131\]: gb \= df.groupby("animal")

In \[132\]: gb.get\_group("cat")
Out\[132\]: 
  animal size  weight  adult
0    cat    S       8  False
2    cat    M      11  False
5    cat    L      12   True
6    cat    L      12   True

Copy to clipboard

[Apply to different items in a group](https://stackoverflow.com/questions/15262134/apply-different-functions-to-different-items-in-group-object-python-pandas)

In \[133\]: def GrowUp(x):
   .....:    avg\_weight \= sum(x\[x\["size"\] \== "S"\].weight \* 1.5)
   .....:    avg\_weight += sum(x\[x\["size"\] \== "M"\].weight \* 1.25)
   .....:    avg\_weight += sum(x\[x\["size"\] \== "L"\].weight)
   .....:    avg\_weight /= len(x)
   .....:    return pd.Series(\["L", avg\_weight, True\], index\=\["size", "weight", "adult"\])
   .....: 

In \[134\]: expected\_df \= gb.apply(GrowUp)

In \[135\]: expected\_df
Out\[135\]: 
       size   weight  adult
animal                     
cat       L  12.4375   True
dog       L  20.0000   True
fish      L   1.2500   True

Copy to clipboard

[Expanding apply](https://stackoverflow.com/questions/14542145/reductions-down-a-column-in-pandas)

In \[136\]: S \= pd.Series(\[i / 100.0 for i in range(1, 11)\])

In \[137\]: def cum\_ret(x, y):
   .....:    return x \* (1 + y)
   .....: 

In \[138\]: def red(x):
   .....:    return functools.reduce(cum\_ret, x, 1.0)
   .....: 

In \[139\]: S.expanding().apply(red, raw\=True)
Out\[139\]: 
0    1.010000
1    1.030200
2    1.061106
3    1.103550
4    1.158728
5    1.228251
6    1.314229
7    1.419367
8    1.547110
9    1.701821
dtype: float64

Copy to clipboard

[Replacing some values with mean of the rest of a group](https://stackoverflow.com/questions/14760757/replacing-values-with-groupby-means)

In \[140\]: df \= pd.DataFrame({"A": \[1, 1, 2, 2\], "B": \[1, \-1, 1, 2\]})

In \[141\]: gb \= df.groupby("A")

In \[142\]: def replace(g):
   .....:    mask \= g < 0
   .....:    return g.where(~mask, g\[~mask\].mean())
   .....: 

In \[143\]: gb.transform(replace)
Out\[143\]: 
   B
0  1
1  1
2  1
3  2

Copy to clipboard

[Sort groups by aggregated data](https://stackoverflow.com/questions/14941366/pandas-sort-by-group-aggregate-and-column)

In \[144\]: df \= pd.DataFrame(
   .....:    {
   .....:        "code": \["foo", "bar", "baz"\] \* 2,
   .....:        "data": \[0.16, \-0.21, 0.33, 0.45, \-0.59, 0.62\],
   .....:        "flag": \[False, True\] \* 3,
   .....:    }
   .....: )
   .....: 

In \[145\]: code\_groups \= df.groupby("code")

In \[146\]: agg\_n\_sort\_order \= code\_groups\[\["data"\]\].transform("sum").sort\_values(by\="data")

In \[147\]: sorted\_df \= df.loc\[agg\_n\_sort\_order.index\]

In \[148\]: sorted\_df
Out\[148\]: 
  code  data   flag
1  bar -0.21   True
4  bar -0.59  False
3  foo  0.45   True
0  foo  0.16  False
2  baz  0.33  False
5  baz  0.62   True

Copy to clipboard

[Create multiple aggregated columns](https://stackoverflow.com/questions/14897100/create-multiple-columns-in-pandas-aggregation-function)

In \[149\]: rng \= pd.date\_range(start\="2014-10-07", periods\=10, freq\="2min")

In \[150\]: ts \= pd.Series(data\=list(range(10)), index\=rng)

In \[151\]: def MyCust(x):
   .....:    if len(x) \> 2:
   .....:        return x.iloc\[1\] \* 1.234
   .....:    return pd.NaT
   .....: 

In \[152\]: mhc \= {"Mean": "mean", "Max": "max", "Custom": MyCust}

In \[153\]: ts.resample("5min").apply(mhc)
Out\[153\]: 
                     Mean  Max Custom
2014-10-07 00:00:00   1.0    2  1.234
2014-10-07 00:05:00   3.5    4    NaT
2014-10-07 00:10:00   6.0    7  7.404
2014-10-07 00:15:00   8.5    9    NaT

In \[154\]: ts
Out\[154\]: 
2014-10-07 00:00:00    0
2014-10-07 00:02:00    1
2014-10-07 00:04:00    2
2014-10-07 00:06:00    3
2014-10-07 00:08:00    4
2014-10-07 00:10:00    5
2014-10-07 00:12:00    6
2014-10-07 00:14:00    7
2014-10-07 00:16:00    8
2014-10-07 00:18:00    9
Freq: 2min, dtype: int64

Copy to clipboard

[Create a value counts column and reassign back to the DataFrame](https://stackoverflow.com/q/17709270)

In \[155\]: df \= pd.DataFrame(
   .....:    {"Color": "Red Red Red Blue".split(), "Value": \[100, 150, 50, 50\]}
   .....: )
   .....: 

In \[156\]: df
Out\[156\]: 
  Color  Value
0   Red    100
1   Red    150
2   Red     50
3  Blue     50

In \[157\]: df\["Counts"\] \= df.groupby(\["Color"\]).transform(len)

In \[158\]: df
Out\[158\]: 
  Color  Value  Counts
0   Red    100       3
1   Red    150       3
2   Red     50       3
3  Blue     50       1

Copy to clipboard

[Shift groups of the values in a column based on the index](https://stackoverflow.com/q/23198053/190597)

In \[159\]: df \= pd.DataFrame(
   .....:    {"line\_race": \[10, 10, 8, 10, 10, 8\], "beyer": \[99, 102, 103, 103, 88, 100\]},
   .....:    index\=\[\
   .....:        "Last Gunfighter",\
   .....:        "Last Gunfighter",\
   .....:        "Last Gunfighter",\
   .....:        "Paynter",\
   .....:        "Paynter",\
   .....:        "Paynter",\
   .....:    \],
   .....: )
   .....: 

In \[160\]: df
Out\[160\]: 
                 line\_race  beyer
Last Gunfighter         10     99
Last Gunfighter         10    102
Last Gunfighter          8    103
Paynter                 10    103
Paynter                 10     88
Paynter                  8    100

In \[161\]: df\["beyer\_shifted"\] \= df.groupby(level\=0)\["beyer"\].shift(1)

In \[162\]: df
Out\[162\]: 
                 line\_race  beyer  beyer\_shifted
Last Gunfighter         10     99            NaN
Last Gunfighter         10    102           99.0
Last Gunfighter          8    103          102.0
Paynter                 10    103            NaN
Paynter                 10     88          103.0
Paynter                  8    100           88.0

Copy to clipboard

[Select row with maximum value from each group](https://stackoverflow.com/q/26701849/190597)

In \[163\]: df \= pd.DataFrame(
   .....:    {
   .....:        "host": \["other", "other", "that", "this", "this"\],
   .....:        "service": \["mail", "web", "mail", "mail", "web"\],
   .....:        "no": \[1, 2, 1, 2, 1\],
   .....:    }
   .....: ).set\_index(\["host", "service"\])
   .....: 

In \[164\]: mask \= df.groupby(level\=0).agg("idxmax")

In \[165\]: df\_count \= df.loc\[mask\["no"\]\].reset\_index()

In \[166\]: df\_count
Out\[166\]: 
    host service  no
0  other     web   2
1   that    mail   1
2   this    mail   2

Copy to clipboard

[Grouping like Python’s itertools.groupby](https://stackoverflow.com/q/29142487/846892)

In \[167\]: df \= pd.DataFrame(\[0, 1, 0, 1, 1, 1, 0, 1, 1\], columns\=\["A"\])

In \[168\]: df\["A"\].groupby((df\["A"\] != df\["A"\].shift()).cumsum()).groups
Out\[168\]: {1: \[0\], 2: \[1\], 3: \[2\], 4: \[3, 4, 5\], 5: \[6\], 6: \[7, 8\]}

In \[169\]: df\["A"\].groupby((df\["A"\] != df\["A"\].shift()).cumsum()).cumsum()
Out\[169\]: 
0    0
1    1
2    0
3    1
4    2
5    3
6    0
7    1
8    2
Name: A, dtype: int64

Copy to clipboard

### Expanding data[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#expanding-data "Link to this heading")

[Alignment and to-date](https://stackoverflow.com/questions/15489011/python-time-series-alignment-and-to-date-functions)

[Rolling Computation window based on values instead of counts](https://stackoverflow.com/questions/14300768/pandas-rolling-computation-with-window-based-on-values-instead-of-counts)

[Rolling Mean by Time Interval](https://stackoverflow.com/questions/15771472/pandas-rolling-mean-by-time-interval)

### Splitting[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#id2 "Link to this heading")

[Splitting a frame](https://stackoverflow.com/questions/13353233/best-way-to-split-a-dataframe-given-an-edge/15449992#15449992)

Create a list of dataframes, split using a delineation based on logic included in rows.

In \[170\]: df \= pd.DataFrame(
   .....:    data\={
   .....:        "Case": \["A", "A", "A", "B", "A", "A", "B", "A", "A"\],
   .....:        "Data": np.random.randn(9),
   .....:    }
   .....: )
   .....: 

In \[171\]: dfs \= list(
   .....:    zip(
   .....:        \*df.groupby(
   .....:            (1 \* (df\["Case"\] \== "B"))
   .....:            .cumsum()
   .....:            .rolling(window\=3, min\_periods\=1)
   .....:            .median()
   .....:        )
   .....:    )
   .....: )\[\-1\]
   .....: 

In \[172\]: dfs\[0\]
Out\[172\]: 
  Case      Data
0    A -0.717852
1    A -1.053898
2    A -0.019369
3    B  0.758887

In \[173\]: dfs\[1\]
Out\[173\]: 
  Case      Data
4    A  2.340598
5    A  0.219039
6    B -1.235583

In \[174\]: dfs\[2\]
Out\[174\]: 
  Case      Data
7    A  0.031785
8    A  0.701683

Copy to clipboard

### Pivot[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#pivot "Link to this heading")

The [Pivot](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-pivot)
 docs.

[Partial sums and subtotals](https://stackoverflow.com/a/15574875)

In \[175\]: df \= pd.DataFrame(
   .....:    data\={
   .....:        "Province": \["ON", "QC", "BC", "AL", "AL", "MN", "ON"\],
   .....:        "City": \[\
   .....:            "Toronto",\
   .....:            "Montreal",\
   .....:            "Vancouver",\
   .....:            "Calgary",\
   .....:            "Edmonton",\
   .....:            "Winnipeg",\
   .....:            "Windsor",\
   .....:        \],
   .....:        "Sales": \[13, 6, 16, 8, 4, 3, 1\],
   .....:    }
   .....: )
   .....: 

In \[176\]: table \= pd.pivot\_table(
   .....:    df,
   .....:    values\=\["Sales"\],
   .....:    index\=\["Province"\],
   .....:    columns\=\["City"\],
   .....:    aggfunc\="sum",
   .....:    margins\=True,
   .....: )
   .....: 

In \[177\]: table.stack("City")
Out\[177\]: 
                    Sales
Province City            
AL       Calgary      8.0
         Edmonton     4.0
         Montreal     NaN
         Toronto      NaN
         Vancouver    NaN
...                   ...
All      Toronto     13.0
         Vancouver   16.0
         Windsor      1.0
         Winnipeg     3.0
         All         51.0

\[48 rows x 1 columns\]

Copy to clipboard

[Frequency table like plyr in R](https://stackoverflow.com/questions/15589354/frequency-tables-in-pandas-like-plyr-in-r)

In \[178\]: grades \= \[48, 99, 75, 80, 42, 80, 72, 68, 36, 78\]

In \[179\]: df \= pd.DataFrame(
   .....:    {
   .....:        "ID": \["x%d" % r for r in range(10)\],
   .....:        "Gender": \["F", "M", "F", "M", "F", "M", "F", "M", "M", "M"\],
   .....:        "ExamYear": \[\
   .....:            "2007",\
   .....:            "2007",\
   .....:            "2007",\
   .....:            "2008",\
   .....:            "2008",\
   .....:            "2008",\
   .....:            "2008",\
   .....:            "2009",\
   .....:            "2009",\
   .....:            "2009",\
   .....:        \],
   .....:        "Class": \[\
   .....:            "algebra",\
   .....:            "stats",\
   .....:            "bio",\
   .....:            "algebra",\
   .....:            "algebra",\
   .....:            "stats",\
   .....:            "stats",\
   .....:            "algebra",\
   .....:            "bio",\
   .....:            "bio",\
   .....:        \],
   .....:        "Participated": \[\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "no",\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "yes",\
   .....:            "yes",\
   .....:        \],
   .....:        "Passed": \["yes" if x \> 50 else "no" for x in grades\],
   .....:        "Employed": \[\
   .....:            True,\
   .....:            True,\
   .....:            True,\
   .....:            False,\
   .....:            False,\
   .....:            False,\
   .....:            False,\
   .....:            True,\
   .....:            True,\
   .....:            False,\
   .....:        \],
   .....:        "Grade": grades,
   .....:    }
   .....: )
   .....: 

In \[180\]: df.groupby("ExamYear").agg(
   .....:    {
   .....:        "Participated": lambda x: x.value\_counts()\["yes"\],
   .....:        "Passed": lambda x: sum(x \== "yes"),
   .....:        "Employed": lambda x: sum(x),
   .....:        "Grade": lambda x: sum(x) / len(x),
   .....:    }
   .....: )
   .....: 
Out\[180\]: 
          Participated  Passed  Employed      Grade
ExamYear                                           
2007                 3       2         3  74.000000
2008                 3       3         0  68.500000
2009                 3       2         2  60.666667

Copy to clipboard

[Plot pandas DataFrame with year over year data](https://stackoverflow.com/questions/30379789/plot-pandas-data-frame-with-year-over-year-data)

To create year and month cross tabulation:

In \[181\]: df \= pd.DataFrame(
   .....:    {"value": np.random.randn(36)},
   .....:    index\=pd.date\_range("2011-01-01", freq\="ME", periods\=36),
   .....: )
   .....: 

In \[182\]: pd.pivot\_table(
   .....:    df, index\=df.index.month, columns\=df.index.year, values\="value", aggfunc\="sum"
   .....: )
   .....: 
Out\[182\]: 
        2011      2012      2013
1  -1.557016  0.109001  1.171652
2  -0.636986 -0.533294  1.387952
3  -1.238610  0.243981  0.009025
4   0.179286 -1.037831  0.613766
5  -1.002278 -1.150016 -0.031653
6   0.654052 -0.871461  0.543156
7   1.150663 -0.687693 -0.983195
8  -1.269741  1.921056 -1.247823
9   1.053999 -0.121113  1.710348
10  0.651981 -0.258742 -0.466489
11  0.280668 -0.706329 -0.590065
12  0.642481  0.402547 -0.245043

Copy to clipboard

### Apply[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#apply "Link to this heading")

[Rolling apply to organize - Turning embedded lists into a MultiIndex frame](https://stackoverflow.com/questions/17349981/converting-pandas-dataframe-with-categorical-values-into-binary-values)

In \[183\]: df \= pd.DataFrame(
   .....:    data\={
   .....:        "A": \[\[2, 4, 8, 16\], \[100, 200\], \[10, 20, 30\]\],
   .....:        "B": \[\["a", "b", "c"\], \["jj", "kk"\], \["ccc"\]\],
   .....:    },
   .....:    index\=\["I", "II", "III"\],
   .....: )
   .....: 

In \[184\]: def SeriesFromSubList(aList):
   .....:    return pd.Series(aList)
   .....: 

In \[185\]: df\_orgz \= pd.concat(
   .....:    {ind: row.apply(SeriesFromSubList) for ind, row in df.iterrows()}
   .....: )
   .....: 

In \[186\]: df\_orgz
Out\[186\]: 
         0     1     2     3
I   A    2     4     8  16.0
    B    a     b     c   NaN
II  A  100   200   NaN   NaN
    B   jj    kk   NaN   NaN
III A   10  20.0  30.0   NaN
    B  ccc   NaN   NaN   NaN

Copy to clipboard

[Rolling apply with a DataFrame returning a Series](https://stackoverflow.com/questions/19121854/using-rolling-apply-on-a-dataframe-object)

Rolling Apply to multiple columns where function calculates a Series before a Scalar from the Series is returned

In \[187\]: df \= pd.DataFrame(
   .....:    data\=np.random.randn(2000, 2) / 10000,
   .....:    index\=pd.date\_range("2001-01-01", periods\=2000),
   .....:    columns\=\["A", "B"\],
   .....: )
   .....: 

In \[188\]: df
Out\[188\]: 
                   A         B
2001-01-01 -0.000055  0.000094
2001-01-02 -0.000019 -0.000077
2001-01-03  0.000018  0.000007
2001-01-04 -0.000015 -0.000055
2001-01-05  0.000153 -0.000160
...              ...       ...
2006-06-19  0.000061 -0.000188
2006-06-20 -0.000005 -0.000152
2006-06-21  0.000083 -0.000141
2006-06-22  0.000222  0.000099
2006-06-23 -0.000001 -0.000118

\[2000 rows x 2 columns\]

In \[189\]: def gm(df, const):
   .....:    v \= ((((df\["A"\] + df\["B"\]) + 1).cumprod()) \- 1) \* const
   .....:    return v.iloc\[\-1\]
   .....: 

In \[190\]: s \= pd.Series(
   .....:    {
   .....:        df.index\[i\]: gm(df.iloc\[i: min(i + 51, len(df) \- 1)\], 5)
   .....:        for i in range(len(df) \- 50)
   .....:    }
   .....: )
   .....: 

In \[191\]: s
Out\[191\]: 
2001-01-01    0.002351
2001-01-02    0.000715
2001-01-03    0.000781
2001-01-04    0.000600
2001-01-05    0.000553
                ...   
2006-04-30    0.002038
2006-05-01   -0.000297
2006-05-02   -0.001285
2006-05-03   -0.000136
2006-05-04    0.000555
Length: 1950, dtype: float64

Copy to clipboard

[Rolling apply with a DataFrame returning a Scalar](https://stackoverflow.com/questions/21040766/python-pandas-rolling-apply-two-column-input-into-function/21045831#21045831)

Rolling Apply to multiple columns where function returns a Scalar (Volume Weighted Average Price)

In \[192\]: rng \= pd.date\_range(start\="2014-01-01", periods\=100)

In \[193\]: df \= pd.DataFrame(
   .....:    {
   .....:        "Open": np.random.randn(len(rng)),
   .....:        "Close": np.random.randn(len(rng)),
   .....:        "Volume": np.random.randint(100, 2000, len(rng)),
   .....:    },
   .....:    index\=rng,
   .....: )
   .....: 

In \[194\]: df
Out\[194\]: 
                Open     Close  Volume
2014-01-01  0.033486 -0.696814    1584
2014-01-02 -0.814911  0.757498    1646
2014-01-03  0.914505 -0.050488    1834
2014-01-04  1.341414  0.334399     714
2014-01-05 -0.147454  0.267882    1209
...              ...       ...     ...
2014-04-06 -1.003720  1.057274     820
2014-04-07 -1.267996 -0.758783    1720
2014-04-08  0.014528  0.120241     484
2014-04-09  0.705241 -0.277638    1675
2014-04-10 -0.281064  0.371639     835

\[100 rows x 3 columns\]

In \[195\]: def vwap(bars):
   .....:    return (bars.Close \* bars.Volume).sum() / bars.Volume.sum()
   .....: 

In \[196\]: window \= 5

In \[197\]: s \= pd.concat(
   .....:    \[\
   .....:        (pd.Series(vwap(df.iloc\[i: i + window\]), index\=\[df.index\[i + window\]\]))\
   .....:        for i in range(len(df) \- window)\
   .....:    \]
   .....: )
   .....: 

In \[198\]: s.round(2)
Out\[198\]: 
2014-01-06    0.09
2014-01-07    0.37
2014-01-08    0.12
2014-01-09    0.10
2014-01-10    0.14
              ... 
2014-04-06    0.06
2014-04-07    0.05
2014-04-08   -0.55
2014-04-09   -0.49
2014-04-10   -0.21
Length: 95, dtype: float64

Copy to clipboard

Timeseries[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#timeseries "Link to this heading")

---------------------------------------------------------------------------------------------------------

### Time-distance weighted rolling aggregations[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#time-distance-weighted-rolling-aggregations "Link to this heading")

A decay-weighted aggregation can be applied inside a time-based rolling window. The weight depends on how far each observation is from the most recent timestamp in the window. This is useful when more recent values should contribute more to rolling statistics than older ones, particularly where observations are not evenly spaced in time.

This approach relies on `rolling.apply` and recomputes weights for each window, so it may be slow for large datasets.

df \= pd.DataFrame(
    {
        "timestamp": \[\
            "2024-01-01 01:00",\
            "2024-01-01 02:00",\
            "2024-01-01 05:00",\
            "2024-01-01 05:00",\
            "2024-01-01 07:00",\
            "2024-01-01 08:00",\
        \],
        "value": \[12, 13, 20, 26, 24, 27\],
    }
)

df\["timestamp"\] \= pd.to\_datetime(df\["timestamp"\])
df \= df.set\_index("timestamp")

def decay\_weighted\_mean(values, alpha\=0.1):
    timestamps \= values.index
    age\_hours \= (timestamps.max() \- timestamps).total\_seconds() / 3600
    weights \= np.exp(\-alpha \* age\_hours)
    return (weights \* values).sum() / weights.sum()

result \= (
    df\["value"\]
    .rolling("7h")
    .apply(decay\_weighted\_mean)
)

Copy to clipboard

[Between times](https://stackoverflow.com/questions/14539992/pandas-drop-rows-outside-of-time-range)

[Using indexer between time](https://stackoverflow.com/questions/17559885/pandas-dataframe-mask-based-on-index)

[Constructing a datetime range that excludes weekends and includes only certain times](https://stackoverflow.com/a/24014440)

[Vectorized Lookup](https://stackoverflow.com/questions/13893227/vectorized-look-up-of-values-in-pandas-dataframe)

[Aggregation and plotting time series](https://nipunbatra.github.io/blog/posts/2013-05-01-aggregation-timeseries.html)

Turn a matrix with hours in columns and days in rows into a continuous row sequence in the form of a time series. [How to rearrange a Python pandas DataFrame?](https://stackoverflow.com/questions/15432659/how-to-rearrange-a-python-pandas-dataframe)

[Dealing with duplicates when reindexing a timeseries to a specified frequency](https://stackoverflow.com/questions/22244383/pandas-df-refill-adding-two-columns-of-different-shape)

Calculate the first day of the month for each entry in a DatetimeIndex

In \[199\]: dates \= pd.date\_range("2000-01-01", periods\=5)

In \[200\]: dates.to\_period(freq\="M").to\_timestamp()
Out\[200\]: 
DatetimeIndex(\['2000-01-01', '2000-01-01', '2000-01-01', '2000-01-01',\
               '2000-01-01'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Split rows describing events with a start and stop time into multiple rows, so that each row falls within a single interval of a fixed frequency. Extra columns are replicated for each piece, and the original row label identifies which event each piece came from [GH 34836](https://github.com/pandas-dev/pandas/issues/34836)

In \[201\]: df \= pd.DataFrame(
   .....:    {
   .....:        "start": pd.to\_datetime(\["2020-06-01 08:06", "2020-06-01 21:10"\]),
   .....:        "stop": pd.to\_datetime(\["2020-06-01 09:14", "2020-06-02 01:30"\]),
   .....:        "foo": \["bar", "baz"\],
   .....:    }
   .....: )
   .....: 

In \[202\]: freq \= "30min"

In \[203\]: def split\_event(start, stop, freq):
   .....:    edges \= pd.date\_range(start.floor(freq), stop.ceil(freq), freq\=freq)
   .....:    cuts \= \[start, \*edges\[(edges \> start) & (edges < stop)\], stop\]
   .....:    return list(zip(cuts\[:\-1\], cuts\[1:\]))
   .....: 

In \[204\]: result \= df.assign(
   .....:    pieces\=\[split\_event(start, stop, freq) for start, stop in zip(df\["start"\], df\["stop"\])\]
   .....: ).explode("pieces")
   .....: 

In \[205\]: result\[\["start", "stop"\]\] \= pd.DataFrame(result\["pieces"\].tolist(), index\=result.index)

In \[206\]: result.drop(columns\="pieces")
Out\[206\]: 
                start                stop  foo
0 2020-06-01 08:06:00 2020-06-01 08:30:00  bar
0 2020-06-01 08:30:00 2020-06-01 09:00:00  bar
0 2020-06-01 09:00:00 2020-06-01 09:14:00  bar
1 2020-06-01 21:10:00 2020-06-01 21:30:00  baz
1 2020-06-01 21:30:00 2020-06-01 22:00:00  baz
1 2020-06-01 22:00:00 2020-06-01 22:30:00  baz
1 2020-06-01 22:30:00 2020-06-01 23:00:00  baz
1 2020-06-01 23:00:00 2020-06-01 23:30:00  baz
1 2020-06-01 23:30:00 2020-06-02 00:00:00  baz
1 2020-06-02 00:00:00 2020-06-02 00:30:00  baz
1 2020-06-02 00:30:00 2020-06-02 01:00:00  baz
1 2020-06-02 01:00:00 2020-06-02 01:30:00  baz

Copy to clipboard

### Resampling[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#resampling "Link to this heading")

The [Resample](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-resampling)
 docs.

[Using Grouper instead of TimeGrouper for time grouping of values](https://stackoverflow.com/questions/15297053/how-can-i-divide-single-values-of-a-dataframe-by-monthly-averages)

[Time grouping with some missing values](https://stackoverflow.com/questions/33637312/pandas-grouper-by-frequency-with-completeness-requirement)

Valid frequency arguments to Grouper [Timeseries](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)

[Grouping using a MultiIndex](https://stackoverflow.com/questions/41483763/pandas-timegrouper-on-multiindex)

Using TimeGrouper and another grouping to create subgroups, then apply a custom function [GH 3791](https://github.com/pandas-dev/pandas/issues/3791)

[Resampling with custom periods](https://stackoverflow.com/questions/15408156/resampling-with-custom-periods)

[Resample intraday frame without adding new days](https://stackoverflow.com/questions/14898574/resample-intraday-pandas-dataframe-without-add-new-days)

[Resample minute data](https://stackoverflow.com/questions/14861023/resampling-minute-data)

[Resample with groupby](https://stackoverflow.com/q/18677271/564538)

Merge[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#merge "Link to this heading")

-----------------------------------------------------------------------------------------------

The [Join](https://pandas.pydata.org/docs/user_guide/merging.html#merging-join)
 docs.

[Concatenate two dataframes with overlapping index (emulate R rbind)](https://stackoverflow.com/questions/14988480/pandas-version-of-rbind)

In \[207\]: rng \= pd.date\_range("2000-01-01", periods\=6)

In \[208\]: df1 \= pd.DataFrame(np.random.randn(6, 3), index\=rng, columns\=\["A", "B", "C"\])

In \[209\]: df2 \= df1.copy()

Copy to clipboard

Depending on df construction, `ignore_index` may be needed

In \[210\]: df \= pd.concat(\[df1, df2\], ignore\_index\=True)

In \[211\]: df
Out\[211\]: 
           A         B         C
0   0.005581 -0.141065  0.328092
1   0.021672 -0.352088 -0.444963
2  -0.057350  0.890862  0.279513
3   0.852785 -0.853224  1.682849
4  -0.889863  0.463793 -1.533246
5   1.406591 -1.175524 -1.905383
6   0.005581 -0.141065  0.328092
7   0.021672 -0.352088 -0.444963
8  -0.057350  0.890862  0.279513
9   0.852785 -0.853224  1.682849
10 -0.889863  0.463793 -1.533246
11  1.406591 -1.175524 -1.905383

Copy to clipboard

Self Join of a DataFrame [GH 2996](https://github.com/pandas-dev/pandas/issues/2996)

In \[212\]: df \= pd.DataFrame(
   .....:    data\={
   .....:        "Area": \["A"\] \* 5 + \["C"\] \* 2,
   .....:        "Bins": \[110\] \* 2 + \[160\] \* 3 + \[40\] \* 2,
   .....:        "Test\_0": \[0, 1, 0, 1, 2, 0, 1\],
   .....:        "Data": np.random.randn(7),
   .....:    }
   .....: )
   .....: 

In \[213\]: df
Out\[213\]: 
  Area  Bins  Test\_0      Data
0    A   110       0 -0.197435
1    A   110       1 -0.831425
2    A   160       0 -0.138160
3    A   160       1  1.663817
4    A   160       2 -0.368981
5    C    40       0  1.058936
6    C    40       1  0.258897

In \[214\]: df\["Test\_1"\] \= df\["Test\_0"\] \- 1

In \[215\]: pd.merge(
   .....:    df,
   .....:    df,
   .....:    left\_on\=\["Bins", "Area", "Test\_0"\],
   .....:    right\_on\=\["Bins", "Area", "Test\_1"\],
   .....:    suffixes\=("\_L", "\_R"),
   .....: )
   .....: 
Out\[215\]: 
  Area  Bins  Test\_0\_L    Data\_L  Test\_1\_L  Test\_0\_R    Data\_R  Test\_1\_R
0    A   110         0 -0.197435        -1         1 -0.831425         0
1    A   160         0 -0.138160        -1         1  1.663817         0
2    A   160         1  1.663817         0         2 -0.368981         1
3    C    40         0  1.058936        -1         1  0.258897         0

Copy to clipboard

[How to set the index and join](https://stackoverflow.com/questions/14341805/pandas-merge-pd-merge-how-to-set-the-index-and-join)

[KDB like asof join](https://stackoverflow.com/questions/12322289/kdb-like-asof-join-for-timeseries-data-in-pandas/12336039#12336039)

[Join with a criteria based on the values](https://stackoverflow.com/questions/15581829/how-to-perform-an-inner-or-outer-join-of-dataframes-with-pandas-on-non-simplisti)

[Using searchsorted to merge based on values inside a range](https://stackoverflow.com/questions/25125626/pandas-merge-with-logic/2512764)

Plotting[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#plotting "Link to this heading")

-----------------------------------------------------------------------------------------------------

The [Plotting](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization)
 docs.

[Make Matplotlib look like R](https://stackoverflow.com/questions/14349055/making-matplotlib-graphs-look-like-r-by-default)

[Setting x-axis major and minor labels](https://stackoverflow.com/questions/12945971/pandas-timeseries-plot-setting-x-axis-major-and-minor-ticks-and-labels)

[Plotting multiple charts in an IPython Jupyter notebook](https://stackoverflow.com/questions/16392921/make-more-than-one-chart-in-same-ipython-notebook-cell)

[Creating a multi-line plot](https://stackoverflow.com/questions/16568964/make-a-multiline-plot-from-csv-file-in-matplotlib)

[Plotting a heatmap](https://stackoverflow.com/questions/17050202/plot-timeseries-of-histograms-in-python)

[Annotate a time-series plot](https://stackoverflow.com/questions/11067368/annotate-time-series-plot-in-matplotlib)

[Annotate a time-series plot #2](https://stackoverflow.com/questions/17891493/annotating-points-from-a-pandas-dataframe-in-matplotlib-plot)

[Generate Embedded plots in excel files using Pandas, Vincent and xlsxwriter](https://pandas-xlsxwriter-charts.readthedocs.io/)

[Boxplot for each quartile of a stratifying variable](https://stackoverflow.com/questions/23232989/boxplot-stratified-by-column-in-python-pandas)

In \[216\]: df \= pd.DataFrame(
   .....:    {
   .....:        "stratifying\_var": np.random.uniform(0, 100, 20),
   .....:        "price": np.random.normal(100, 5, 20),
   .....:    }
   .....: )
   .....: 

In \[217\]: df\["quartiles"\] \= pd.qcut(
   .....:    df\["stratifying\_var"\], 4, labels\=\["0-25%", "25-50%", "50-75%", "75-100%"\]
   .....: )
   .....: 

In \[218\]: df.boxplot(column\="price", by\="quartiles")
Out\[218\]: <Axes: title={'center': 'price'}, xlabel='quartiles'>

Copy to clipboard

![../_images/quartile_boxplot.png](https://pandas.pydata.org/docs/_images/quartile_boxplot.png)

Data in/out[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#data-in-out "Link to this heading")

-----------------------------------------------------------------------------------------------------------

[Performance comparison of SQL vs HDF5](https://stackoverflow.com/q/16628329)

### CSV[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#csv "Link to this heading")

The [CSV](https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table)
 docs

[read\_csv in action](https://www.datacamp.com/tutorial/pandas-read-csv)

[appending to a csv](https://stackoverflow.com/questions/17134942/pandas-dataframe-output-end-of-csv)

[Reading a csv chunk-by-chunk](https://stackoverflow.com/questions/11622652/large-persistent-dataframe-in-pandas/12193309#12193309)

Reading only rows matching a condition, chunk-by-chunk, so that only `chunksize` rows of the file are read at a time rather than the whole file [GH 32072](https://github.com/pandas-dev/pandas/issues/32072)

In \[219\]: from io import StringIO

In \[220\]: data \= "col\_1,col\_2\\n940,45\\n1040,52\\n1530,46\\n753,43\\n890,32\\n"

In \[221\]: pd.concat(
   .....:    (chunk.query("col\_1 >= 1000") for chunk in pd.read\_csv(StringIO(data), chunksize\=2)),
   .....:    ignore\_index\=True,
   .....: )
   .....: 
Out\[221\]: 
   col\_1  col\_2
0   1040     52
1   1530     46

Copy to clipboard

[Reading the first few lines of a frame](https://stackoverflow.com/questions/15008970/way-to-read-first-few-lines-for-pandas-dataframe)

Reading a file that is compressed but not by `gzip/bz2` (the native compressed formats which `read_csv` understands). This example shows a `WinZipped` file, but is a general application of opening the file within a context manager and using that handle to read. [See here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)

[Inferring dtypes from a file](https://stackoverflow.com/questions/15555005/get-inferred-dataframe-types-iteratively-using-chunksize)

Dealing with bad lines [GH 2886](https://github.com/pandas-dev/pandas/issues/2886)

Fields containing the `read_csv` comment character are truncated when read back unless they are quoted; write with `quoting=csv.QUOTE_NONNUMERIC` to quote all strings. Note that only the default C engine honors the quoting when reading; `engine="python"` strips the comment regardless [GH 27637](https://github.com/pandas-dev/pandas/issues/27637)

In \[222\]: import csv

In \[223\]: from io import StringIO

In \[224\]: df \= pd.DataFrame({"strings": \["a#b", "plain"\], "value": \[1, 2\]})

In \[225\]: out \= df.to\_csv(index\=False, quoting\=csv.QUOTE\_NONNUMERIC)

In \[226\]: print(out)
"strings","value"
"a#b",1
"plain",2

In \[227\]: pd.read\_csv(StringIO(out), comment\="#")
Out\[227\]: 
  strings  value
0     a#b      1
1   plain      2

Copy to clipboard

[Write a multi-row index CSV without writing duplicates](https://stackoverflow.com/questions/17349574/pandas-write-multiindex-rows-with-to-csv)

#### Reading multiple files to create a single DataFrame[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#reading-multiple-files-to-create-a-single-dataframe "Link to this heading")

The best way to combine multiple files into a single DataFrame is to read the individual frames one by one, put all of the individual frames into a list, and then combine the frames in the list using `pd.concat()`:

In \[228\]: for i in range(3):
   .....:    data \= pd.DataFrame(np.random.randn(10, 4))
   .....:    data.to\_csv("file\_{}.csv".format(i))
   .....: 

In \[229\]: files \= \["file\_0.csv", "file\_1.csv", "file\_2.csv"\]

In \[230\]: result \= pd.concat(\[pd.read\_csv(f) for f in files\], ignore\_index\=True)

Copy to clipboard

You can use the same approach to read all files matching a pattern. Here is an example using `glob`:

In \[231\]: import glob

In \[232\]: import os

In \[233\]: files \= glob.glob("file\_\*.csv")

In \[234\]: result \= pd.concat(\[pd.read\_csv(f) for f in files\], ignore\_index\=True)

Copy to clipboard

Finally, this strategy will work with the other `pd.read_*(...)` functions described in the [io docs](https://pandas.pydata.org/docs/user_guide/io.html#io)
.

#### Parsing date components in multi-columns[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#parsing-date-components-in-multi-columns "Link to this heading")

Parsing date components in multi-columns is faster with a format

In \[235\]: i \= pd.date\_range("20000101", periods\=10000)

In \[236\]: df \= pd.DataFrame({"year": i.year, "month": i.month, "day": i.day})

In \[237\]: df.head()
Out\[237\]: 
   year  month  day
0  2000      1    1
1  2000      1    2
2  2000      1    3
3  2000      1    4
4  2000      1    5

In \[238\]: %timeit pd.to\_datetime((df.year \* 10000 + df.month \* 100 + df.day).astype(str), format='%Y%m%d')
   .....: ds \= df.apply(lambda x: "%04d%02d%02d" % (x\["year"\], x\["month"\], x\["day"\]), axis\=1)
   .....: ds.head()
   .....: %timeit pd.to\_datetime(ds)
   .....: 
3.6 ms +- 347 us per loop (mean +- std. dev. of 7 runs, 100 loops each)
1.95 ms +- 3.84 us per loop (mean +- std. dev. of 7 runs, 1,000 loops each)

Copy to clipboard

#### Skip row between header and data[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#skip-row-between-header-and-data "Link to this heading")

In \[239\]: data \= """;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: ;;;;
   .....: date;Param1;Param2;Param4;Param5
   .....:    ;m²;°C;m²;m
   .....: ;;;;
   .....: 01.01.1990 00:00;1;1;2;3
   .....: 01.01.1990 01:00;5;3;4;5
   .....: 01.01.1990 02:00;9;5;6;7
   .....: 01.01.1990 03:00;13;7;8;9
   .....: 01.01.1990 04:00;17;9;10;11
   .....: 01.01.1990 05:00;21;11;12;13
   .....: """
   .....: 

Copy to clipboard

##### Option 1: pass rows explicitly to skip rows[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#option-1-pass-rows-explicitly-to-skip-rows "Link to this heading")

In \[240\]: from io import StringIO

In \[241\]: pd.read\_csv(
   .....:    StringIO(data),
   .....:    sep\=";",
   .....:    skiprows\=\[11, 12\],
   .....:    index\_col\=0,
   .....:    parse\_dates\=True,
   .....:    header\=10,
   .....: )
   .....: 
Out\[241\]: 
                     Param1  Param2  Param4  Param5
date                                               
1990-01-01 00:00:00       1       1       2       3
1990-01-01 01:00:00       5       3       4       5
1990-01-01 02:00:00       9       5       6       7
1990-01-01 03:00:00      13       7       8       9
1990-01-01 04:00:00      17       9      10      11
1990-01-01 05:00:00      21      11      12      13

Copy to clipboard

##### Option 2: read column names and then data[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#option-2-read-column-names-and-then-data "Link to this heading")

In \[242\]: pd.read\_csv(StringIO(data), sep\=";", header\=10, nrows\=10).columns
Out\[242\]: Index(\['date', 'Param1', 'Param2', 'Param4', 'Param5'\], dtype='str')

In \[243\]: columns \= pd.read\_csv(StringIO(data), sep\=";", header\=10, nrows\=10).columns

In \[244\]: pd.read\_csv(
   .....:    StringIO(data), sep\=";", index\_col\=0, header\=12, parse\_dates\=True, names\=columns
   .....: )
   .....: 
Out\[244\]: 
                     Param1  Param2  Param4  Param5
date                                               
1990-01-01 00:00:00       1       1       2       3
1990-01-01 01:00:00       5       3       4       5
1990-01-01 02:00:00       9       5       6       7
1990-01-01 03:00:00      13       7       8       9
1990-01-01 04:00:00      17       9      10      11
1990-01-01 05:00:00      21      11      12      13

Copy to clipboard

### SQL[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#sql "Link to this heading")

The [SQL](https://pandas.pydata.org/docs/user_guide/io.html#io-sql)
 docs

[Reading from databases with SQL](https://stackoverflow.com/questions/10065051/python-pandas-and-databases-like-mysql)

### Excel[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#excel "Link to this heading")

The [Excel](https://pandas.pydata.org/docs/user_guide/io.html#io-excel)
 docs

[Reading from a filelike handle](https://stackoverflow.com/questions/15588713/sheets-of-excel-workbook-from-a-url-into-a-pandas-dataframe)

[Modifying formatting in XlsxWriter output](https://pbpython.com/improve-pandas-excel-output.html)

Loading only visible sheets [GH 19842#issuecomment-892150745](https://github.com/pandas-dev/pandas/issues/19842#issuecomment-892150745)

### HTML[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#html "Link to this heading")

[Reading HTML tables from a server that cannot handle the default request header](https://stackoverflow.com/a/18939272/564538)

### HDFStore[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#hdfstore "Link to this heading")

The [HDFStores](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5)
 docs

[Simple queries with a Timestamp Index](https://stackoverflow.com/questions/13926089/selecting-columns-from-pandas-hdfstore-table)

Managing heterogeneous data using a linked multiple table hierarchy [GH 3032](https://github.com/pandas-dev/pandas/issues/3032)

[Merging on-disk tables with millions of rows](https://stackoverflow.com/questions/14614512/merging-two-tables-with-millions-of-rows-in-python/14617925#14617925)

[Avoiding inconsistencies when writing to a store from multiple processes/threads](https://stackoverflow.com/a/29014295/2858145)

De-duplicating a large store by chunks, essentially a recursive reduction operation. Shows a function for taking in data from csv file and creating a store by chunks, with date parsing as well. [See here](https://stackoverflow.com/questions/16110252/need-to-compare-very-large-files-around-1-5gb-in-python/16110391#16110391)

[Creating a store chunk-by-chunk from a csv file](https://stackoverflow.com/questions/20428355/appending-column-to-frame-of-hdf-file-in-pandas/20428786#20428786)

[Appending to a store, while creating a unique index](https://stackoverflow.com/questions/16997048/how-does-one-append-large-amounts-of-data-to-a-pandas-hdfstore-and-get-a-natural/16999397#16999397)

[Large Data work flows](https://stackoverflow.com/q/14262433)

[Reading in a sequence of files, then providing a global unique index to a store while appending](https://stackoverflow.com/questions/16997048/how-does-one-append-large-amounts-of-data-to-a-pandas-hdfstore-and-get-a-natural)

[Groupby on an HDFStore with low group density](https://stackoverflow.com/questions/15798209/pandas-group-by-query-on-large-data-in-hdfstore)

[Groupby on an HDFStore with high group density](https://stackoverflow.com/questions/25459982/trouble-with-grouby-on-millions-of-keys-on-a-chunked-file-in-python-pandas/25471765#25471765)

[Hierarchical queries on an HDFStore](https://stackoverflow.com/questions/22777284/improve-query-performance-from-a-large-hdfstore-table-with-pandas/22820780#22820780)

[Counting with an HDFStore](https://stackoverflow.com/questions/20497897/converting-dict-of-dicts-into-pandas-dataframe-memory-issues)

[Troubleshoot HDFStore exceptions](https://stackoverflow.com/questions/15488809/how-to-trouble-shoot-hdfstore-exception-cannot-find-the-correct-atom-type)

[Setting min\_itemsize with strings](https://stackoverflow.com/questions/15988871/hdfstore-appendstring-dataframe-fails-when-string-column-contents-are-longer)

[Using ptrepack to create a completely-sorted-index on a store](https://stackoverflow.com/questions/17893370/ptrepack-sortby-needs-full-index)

Storing Attributes to a group node

In \[245\]: df \= pd.DataFrame(np.random.randn(8, 3))

In \[246\]: store \= pd.HDFStore("test.h5")

In \[247\]: store\["df"\] \= df

\# you can store an arbitrary Python object via pickle
In \[248\]: store.get\_storer("df").attrs.my\_attribute \= {"A": 10}

In \[249\]: store.get\_storer("df").attrs.my\_attribute
Out\[249\]: {'A': 10}

Copy to clipboard

You can create or load an HDFStore in-memory by passing the `driver` parameter to PyTables. Changes are only written to disk when the HDFStore is closed.

In \[250\]: store \= pd.HDFStore("test.h5", "w", driver\="H5FD\_CORE")

In \[251\]: df \= pd.DataFrame(np.random.randn(8, 3))

In \[252\]: store\["test"\] \= df

\# only after closing the store, data is written to disk:
In \[253\]: store.close()

Copy to clipboard

### Binary files[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#binary-files "Link to this heading")

pandas readily accepts NumPy record arrays, if you need to read in a binary file consisting of an array of C structs. For example, given this C program in a file called `main.c` compiled with `gcc main.c -std=gnu99` on a 64-bit machine,

#include <stdio.h>
#include <stdint.h>

typedef struct \_Data
{
    int32\_t count;
    double avg;
    float scale;
} Data;

int main(int argc, const char \*argv\[\])
{
    size\_t n \= 10;
    Data d\[n\];

    for (int i \= 0; i < n; ++i)
    {
        d\[i\].count \= i;
        d\[i\].avg \= i + 1.0;
        d\[i\].scale \= (float) i + 2.0f;
    }

    FILE \*file \= fopen("binary.dat", "wb");
    fwrite(&d, sizeof(Data), n, file);
    fclose(file);

    return 0;
}

Copy to clipboard

the following Python code will read the binary file `'binary.dat'` into a pandas `DataFrame`, where each element of the struct corresponds to a column in the frame:

names \= "count", "avg", "scale"

\# note that the offsets are larger than the size of the type because of
\# struct padding
offsets \= 0, 8, 16
formats \= "i4", "f8", "f4"
dt \= np.dtype({"names": names, "offsets": offsets, "formats": formats}, align\=True)
df \= pd.DataFrame(np.fromfile("binary.dat", dt))

Copy to clipboard

Note

The offsets of the structure elements may be different depending on the architecture of the machine on which the file was created. Using a raw binary file format like this for general data storage is not recommended, as it is not cross platform. We recommended either HDF5 or parquet, both of which are supported by pandas’ IO facilities.

Computation[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#computation "Link to this heading")

-----------------------------------------------------------------------------------------------------------

[Numerical integration (sample-based) of a time series](https://nbviewer.ipython.org/gist/metakermit/5720498)

### Correlation[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#correlation "Link to this heading")

Often it’s useful to obtain the lower (or upper) triangular form of a correlation matrix calculated from [`DataFrame.corr()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")
. This can be achieved by passing a boolean mask to `where` as follows:

In \[254\]: df \= pd.DataFrame(np.random.random(size\=(100, 5)))

In \[255\]: corr\_mat \= df.corr()

In \[256\]: mask \= np.tril(np.ones\_like(corr\_mat, dtype\=np.bool\_), k\=-1)

In \[257\]: corr\_mat.where(mask)
Out\[257\]: 
          0         1         2         3   4
0       NaN       NaN       NaN       NaN NaN
1 -0.092049       NaN       NaN       NaN NaN
2  0.095091 -0.019222       NaN       NaN NaN
3  0.061613  0.061839  0.010327       NaN NaN
4 -0.065716  0.116280  0.075950 -0.063626 NaN

Copy to clipboard

To list each pair only once, sorted by correlation strength, stack the masked matrix into a Series and sort by absolute value [GH 24728](https://github.com/pandas-dev/pandas/issues/24728)

In \[258\]: pairs \= corr\_mat.where(mask).stack().dropna()

In \[259\]: pairs.sort\_values(key\=abs, ascending\=False)
Out\[259\]: 
4  1    0.116280
2  0    0.095091
1  0   -0.092049
4  2    0.075950
   0   -0.065716
   3   -0.063626
3  1    0.061839
   0    0.061613
2  1   -0.019222
3  2    0.010327
dtype: float64

Copy to clipboard

The `method` argument within `DataFrame.corr` can accept a callable in addition to the named correlation types. Here we compute the [distance correlation](https://en.wikipedia.org/wiki/Distance_correlation)
 matrix for a `DataFrame` object.

In \[260\]: def distcorr(x, y):
   .....:    n \= len(x)
   .....:    a \= np.zeros(shape\=(n, n))
   .....:    b \= np.zeros(shape\=(n, n))
   .....:    for i in range(n):
   .....:        for j in range(i + 1, n):
   .....:            a\[i, j\] \= abs(x\[i\] \- x\[j\])
   .....:            b\[i, j\] \= abs(y\[i\] \- y\[j\])
   .....:    a += a.T
   .....:    b += b.T
   .....:    a\_bar \= np.vstack(\[np.nanmean(a, axis\=0)\] \* n)
   .....:    b\_bar \= np.vstack(\[np.nanmean(b, axis\=0)\] \* n)
   .....:    A \= a \- a\_bar \- a\_bar.T + np.full(shape\=(n, n), fill\_value\=a\_bar.mean())
   .....:    B \= b \- b\_bar \- b\_bar.T + np.full(shape\=(n, n), fill\_value\=b\_bar.mean())
   .....:    cov\_ab \= np.sqrt(np.nansum(A \* B)) / n
   .....:    std\_a \= np.sqrt(np.sqrt(np.nansum(A \*\* 2)) / n)
   .....:    std\_b \= np.sqrt(np.sqrt(np.nansum(B \*\* 2)) / n)
   .....:    return cov\_ab / std\_a / std\_b
   .....: 

In \[261\]: df \= pd.DataFrame(np.random.normal(size\=(100, 3)))

In \[262\]: df.corr(method\=distcorr)
Out\[262\]: 
          0         1         2
0  1.000000  0.132965  0.152845
1  0.132965  1.000000  0.217007
2  0.152845  0.217007  1.000000

Copy to clipboard

Timedeltas[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#timedeltas "Link to this heading")

---------------------------------------------------------------------------------------------------------

The [Timedeltas](https://pandas.pydata.org/docs/user_guide/timedeltas.html#timedeltas-timedeltas)
 docs.

[Using timedeltas](https://github.com/pandas-dev/pandas/pull/2899)

In \[263\]: import datetime

In \[264\]: s \= pd.Series(pd.date\_range("2012-1-1", periods\=3, freq\="D"))

In \[265\]: s \- s.max()
Out\[265\]: 
0   -2 days
1   -1 days
2    0 days
dtype: timedelta64\[us\]

In \[266\]: s.max() \- s
Out\[266\]: 
0   2 days
1   1 days
2   0 days
dtype: timedelta64\[us\]

In \[267\]: s \- datetime.datetime(2011, 1, 1, 3, 5)
Out\[267\]: 
0   364 days 20:55:00
1   365 days 20:55:00
2   366 days 20:55:00
dtype: timedelta64\[us\]

In \[268\]: s + datetime.timedelta(minutes\=5)
Out\[268\]: 
0   2012-01-01 00:05:00
1   2012-01-02 00:05:00
2   2012-01-03 00:05:00
dtype: datetime64\[us\]

In \[269\]: datetime.datetime(2011, 1, 1, 3, 5) \- s
Out\[269\]: 
0   -365 days +03:05:00
1   -366 days +03:05:00
2   -367 days +03:05:00
dtype: timedelta64\[us\]

In \[270\]: datetime.timedelta(minutes\=5) + s
Out\[270\]: 
0   2012-01-01 00:05:00
1   2012-01-02 00:05:00
2   2012-01-03 00:05:00
dtype: datetime64\[us\]

Copy to clipboard

[Adding and subtracting deltas and dates](https://stackoverflow.com/questions/16385785/add-days-to-dates-in-dataframe)

In \[271\]: deltas \= pd.Series(\[datetime.timedelta(days\=i) for i in range(3)\])

In \[272\]: df \= pd.DataFrame({"A": s, "B": deltas})

In \[273\]: df
Out\[273\]: 
           A      B
0 2012-01-01 0 days
1 2012-01-02 1 days
2 2012-01-03 2 days

In \[274\]: df\["New Dates"\] \= df\["A"\] + df\["B"\]

In \[275\]: df\["Delta"\] \= df\["A"\] \- df\["New Dates"\]

In \[276\]: df
Out\[276\]: 
           A      B  New Dates   Delta
0 2012-01-01 0 days 2012-01-01  0 days
1 2012-01-02 1 days 2012-01-03 -1 days
2 2012-01-03 2 days 2012-01-05 -2 days

In \[277\]: df.dtypes
Out\[277\]: 
A             datetime64\[us\]
B            timedelta64\[us\]
New Dates     datetime64\[us\]
Delta        timedelta64\[us\]
dtype: object

Copy to clipboard

[Another example](https://stackoverflow.com/questions/15683588/iterating-through-a-pandas-dataframe)

Values can be set to NaT using np.nan, similar to datetime

In \[278\]: y \= s \- s.shift()

In \[279\]: y
Out\[279\]: 
0      NaT
1   1 days
2   1 days
dtype: timedelta64\[us\]

In \[280\]: y\[1\] \= np.nan

In \[281\]: y
Out\[281\]: 
0      NaT
1      NaT
2   1 days
dtype: timedelta64\[us\]

Copy to clipboard

Creating example data[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#creating-example-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

To create a dataframe from every combination of some given values, like R’s `expand.grid()` function, we can create a dict where the keys are column names and the values are lists of the data values:

In \[282\]: def expand\_grid(data\_dict):
   .....:    rows \= itertools.product(\*data\_dict.values())
   .....:    return pd.DataFrame.from\_records(rows, columns\=data\_dict.keys())
   .....: 

In \[283\]: df \= expand\_grid(
   .....:    {"height": \[60, 70\], "weight": \[100, 140, 180\], "sex": \["Male", "Female"\]}
   .....: )
   .....: 

In \[284\]: df
Out\[284\]: 
    height  weight     sex
0       60     100    Male
1       60     100  Female
2       60     140    Male
3       60     140  Female
4       60     180    Male
5       60     180  Female
6       70     100    Male
7       70     100  Female
8       70     140    Male
9       70     140  Female
10      70     180    Male
11      70     180  Female

Copy to clipboard

Constant Series[#](https://pandas.pydata.org/docs/user_guide/cookbook.html#constant-series "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

To assess if a series has a constant value, we can check if `series.nunique() <= 1`. However, a more performant approach, that does not count all unique values first, is:

In \[285\]: v \= s.to\_numpy()

In \[286\]: is\_constant \= v.shape\[0\] \== 0 or (s\[0\] \== s).all()

Copy to clipboard

This approach assumes that the series does not contain missing values. For the case that we would drop NA values, we can simply remove those values first:

In \[287\]: v \= s.dropna().to\_numpy()

In \[288\]: is\_constant \= v.shape\[0\] \== 0 or (s\[0\] \== s).all()

Copy to clipboard

If missing values are considered distinct from any other value, then one could use:

In \[289\]: v \= s.to\_numpy()

In \[290\]: is\_constant \= v.shape\[0\] \== 0 or (s\[0\] \== s).all() or not pd.notna(v).any()

Copy to clipboard

(Note that this example does not disambiguate between `np.nan`, `pd.NA` and `None`)

On this page