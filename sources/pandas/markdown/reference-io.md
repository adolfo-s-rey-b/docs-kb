[Skip to main content](https://pandas.pydata.org/docs/reference/io.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Input/output[#](https://pandas.pydata.org/docs/reference/io.html#input-output "Link to this heading")

======================================================================================================

Note

For an overview, see [IO tools (text, CSV, HDF5, …)](https://pandas.pydata.org/docs/user_guide/io.html#io)
.

Pickling[#](https://pandas.pydata.org/docs/reference/io.html#pickling "Link to this heading")

----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#pandas.read_pickle "pandas.read_pickle")<br>(filepath\_or\_buffer\[, ...\]) | Load pickled pandas object (or any object) from file and return unpickled object. |
| [`DataFrame.to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle "pandas.DataFrame.to_pickle")<br>(path, \*\[, compression, ...\]) | Pickle (serialize) object to file. |

Flat file[#](https://pandas.pydata.org/docs/reference/io.html#flat-file "Link to this heading")

------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table "pandas.read_table")<br>(filepath\_or\_buffer, \*\[, sep, ...\]) | Read general delimited file into DataFrame. |
| [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")<br>(filepath\_or\_buffer, \*\[, sep, ...\]) | Read a comma-separated values (csv) file into DataFrame. |
| [`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")<br>(\[path\_or\_buf, sep, na\_rep, ...\]) | Write object to a comma-separated values (csv) file. |
| [`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")<br>(filepath\_or\_buffer, \*\[, colspecs, ...\]) | Read a table of fixed-width formatted lines into DataFrame. |

|     |     |
| --- | --- |
| [`TextFileReader`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.html#pandas.io.parsers.TextFileReader "pandas.io.parsers.TextFileReader")<br>(f\[, engine\]) | Iterator over chunks of a delimited text file. |
| [`TextFileReader.read`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")<br>(\[nrows\]) | Read rows from the file into a `DataFrame`. |
| [`TextFileReader.get_chunk`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "pandas.io.parsers.TextFileReader.get_chunk")<br>(\[size\]) | Read the next chunk of rows from the file. |
| [`TextFileReader.close`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html#pandas.io.parsers.TextFileReader.close "pandas.io.parsers.TextFileReader.close")<br>() | Close the underlying file handle and parser engine. |

Clipboard[#](https://pandas.pydata.org/docs/reference/io.html#clipboard "Link to this heading")

------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#pandas.read_clipboard "pandas.read_clipboard")<br>(\[sep, dtype\_backend\]) | Read text from clipboard and pass to [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")<br>. |
| [`DataFrame.to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard "pandas.DataFrame.to_clipboard")<br>(\*\[, excel, sep\]) | Copy object to the system clipboard. |

Excel[#](https://pandas.pydata.org/docs/reference/io.html#excel "Link to this heading")

----------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")<br>(io\[, sheet\_name, header, names, ...\]) | Read an Excel file into a `DataFrame`. |
| [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")<br>(excel\_writer, \*\[, ...\]) | Write object to an Excel sheet. |
| [`ExcelFile`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html#pandas.ExcelFile "pandas.ExcelFile")<br>(path\_or\_buffer\[, engine, ...\]) | Class for parsing tabular Excel sheets into DataFrame objects. |
| [`ExcelFile.book`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html#pandas.ExcelFile.book "pandas.ExcelFile.book") | Gets the Excel workbook. |
| [`ExcelFile.sheet_names`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html#pandas.ExcelFile.sheet_names "pandas.ExcelFile.sheet_names") | Names of the sheets in the document. |
| [`ExcelFile.parse`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#pandas.ExcelFile.parse "pandas.ExcelFile.parse")<br>(\[sheet\_name, header, names, ...\]) | (DEPRECATED) Parse specified sheet(s) into a DataFrame. |

|     |     |
| --- | --- |
| [`Styler.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html#pandas.io.formats.style.Styler.to_excel "pandas.io.formats.style.Styler.to_excel")<br>(excel\_writer\[, sheet\_name, ...\]) | Write Styler to an Excel sheet. |

|     |     |
| --- | --- |
| [`ExcelWriter`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter "pandas.ExcelWriter")<br>(path\[, engine, date\_format, ...\]) | Class for writing DataFrame objects into excel sheets. |

JSON[#](https://pandas.pydata.org/docs/reference/io.html#json "Link to this heading")

--------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_json`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")<br>(path\_or\_buf, \*\[, orient, typ, ...\]) | Convert a JSON string to pandas object. |
| [`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#pandas.json_normalize "pandas.json_normalize")<br>(data\[, record\_path, meta, ...\]) | Normalize semi-structured JSON data into a flat table. |
| [`DataFrame.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")<br>(\[path\_or\_buf, orient, ...\]) | Convert the object to a JSON string. |

|     |     |
| --- | --- |
| [`build_table_schema`](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html#pandas.io.json.build_table_schema "pandas.io.json.build_table_schema")<br>(data\[, index, ...\]) | Create a Table schema from `data`. |

|     |     |
| --- | --- |
| [`JsonReader`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.JsonReader.html#pandas.api.typing.JsonReader "pandas.api.typing.JsonReader")<br>(filepath\_or\_buffer, orient, typ, ...) | JsonReader provides an interface for reading in a JSON file. |

HTML[#](https://pandas.pydata.org/docs/reference/io.html#html "Link to this heading")

--------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#pandas.read_html "pandas.read_html")<br>(io, \*\[, match, flavor, header, ...\]) | Read HTML tables into a `list` of `DataFrame` objects. |
| [`DataFrame.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")<br>(\[buf, columns, col\_space, ...\]) | Render a DataFrame as an HTML table. |

|     |     |
| --- | --- |
| [`Styler.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#pandas.io.formats.style.Styler.to_html "pandas.io.formats.style.Styler.to_html")<br>(\[buf, table\_uuid, ...\]) | Write Styler to a file, buffer or string in HTML-CSS format. |

XML[#](https://pandas.pydata.org/docs/reference/io.html#xml "Link to this heading")

------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_xml`](https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html#pandas.read_xml "pandas.read_xml")<br>(path\_or\_buffer, \*\[, xpath, ...\]) | Read XML document into a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")<br> object. |
| [`DataFrame.to_xml`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html#pandas.DataFrame.to_xml "pandas.DataFrame.to_xml")<br>(\[path\_or\_buffer, index, ...\]) | Render a DataFrame to an XML document. |

Latex[#](https://pandas.pydata.org/docs/reference/io.html#latex "Link to this heading")

----------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas.DataFrame.to_latex "pandas.DataFrame.to_latex")<br>(\[buf, columns, header, ...\]) | Render object to a LaTeX tabular, longtable, or nested table. |

|     |     |
| --- | --- |
| [`Styler.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html#pandas.io.formats.style.Styler.to_latex "pandas.io.formats.style.Styler.to_latex")<br>(\[buf, column\_format, ...\]) | Write Styler to a file, buffer or string in LaTeX format. |

HDFStore: PyTables (HDF5)[#](https://pandas.pydata.org/docs/reference/io.html#hdfstore-pytables-hdf5 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "pandas.read_hdf")<br>(path\_or\_buf\[, key, mode, errors, ...\]) | Read from the store, close it if we opened it. |
| [`HDFStore.put`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#pandas.HDFStore.put "pandas.HDFStore.put")<br>(key, value\[, format, index, ...\]) | Store object in HDFStore. |
| [`HDFStore.append`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")<br>(key, value\[, format, axes, ...\]) | Append to Table in file. |
| [`HDFStore.append_to_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#pandas.HDFStore.append_to_multiple "pandas.HDFStore.append_to_multiple")<br>(d, value, selector) | Append to multiple tables. |
| [`HDFStore.get`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html#pandas.HDFStore.get "pandas.HDFStore.get")<br>(key) | Retrieve pandas object stored in file. |
| [`HDFStore.select`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "pandas.HDFStore.select")<br>(key\[, where, start, stop, ...\]) | Retrieve pandas object stored in file, optionally based on where criteria. |
| [`HDFStore.select_as_coordinates`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#pandas.HDFStore.select_as_coordinates "pandas.HDFStore.select_as_coordinates")<br>(key\[, where, ...\]) | Return the selection as an Index. |
| [`HDFStore.select_as_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas.HDFStore.select_as_multiple "pandas.HDFStore.select_as_multiple")<br>(keys\[, where, ...\]) | Retrieve pandas objects from multiple tables. |
| [`HDFStore.select_column`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_column.html#pandas.HDFStore.select_column "pandas.HDFStore.select_column")<br>(key, column\[, start, ...\]) | Return a single column from the table. |
| [`HDFStore.remove`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.remove.html#pandas.HDFStore.remove "pandas.HDFStore.remove")<br>(key\[, where, start, stop\]) | Remove pandas object partially by specifying the where condition. |
| [`HDFStore.create_table_index`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.create_table_index.html#pandas.HDFStore.create_table_index "pandas.HDFStore.create_table_index")<br>(key\[, columns, ...\]) | Create a pytables index on the table. |
| [`HDFStore.copy`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.copy.html#pandas.HDFStore.copy "pandas.HDFStore.copy")<br>(file\[, mode, propindexes, ...\]) | Copy the existing store to a new file, updating in place. |
| [`HDFStore.flush`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.flush.html#pandas.HDFStore.flush "pandas.HDFStore.flush")<br>(\[fsync\]) | Force all buffered modifications to be written to disk. |
| [`HDFStore.info`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "pandas.HDFStore.info")<br>() | Print detailed information on the store. |
| [`HDFStore.is_open`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.is_open.html#pandas.HDFStore.is_open "pandas.HDFStore.is_open") | Return a boolean indicating whether the file is open. |
| [`HDFStore.keys`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.keys.html#pandas.HDFStore.keys "pandas.HDFStore.keys")<br>(\[include\]) | Return a list of keys corresponding to objects stored in HDFStore. |
| [`HDFStore.groups`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.groups.html#pandas.HDFStore.groups "pandas.HDFStore.groups")<br>() | Return a list of all the top-level nodes. |
| [`HDFStore.get_storer`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "pandas.HDFStore.get_storer")<br>(key) | Return the storer object for a key. |
| [`HDFStore.walk`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.walk.html#pandas.HDFStore.walk "pandas.HDFStore.walk")<br>(\[where\]) | Walk the pytables group hierarchy for pandas objects. |

Warning

One can store a subclass of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 to HDF5, but the type of the subclass is lost upon storing.

Feather[#](https://pandas.pydata.org/docs/reference/io.html#feather "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_feather`](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "pandas.read_feather")<br>(path\[, columns, use\_threads, ...\]) | Load a feather-format object from the file path. |
| [`DataFrame.to_feather`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas.DataFrame.to_feather "pandas.DataFrame.to_feather")<br>(path, \*\*kwargs) | Write a DataFrame to the binary Feather format. |

Parquet[#](https://pandas.pydata.org/docs/reference/io.html#parquet "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")<br>(path\[, engine, columns, ...\]) | Load a parquet object from the file path, returning a DataFrame. |
| [`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")<br>(\[path, engine, ...\]) | Write a DataFrame to the binary parquet format. |

Iceberg[#](https://pandas.pydata.org/docs/reference/io.html#iceberg "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_iceberg`](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html#pandas.read_iceberg "pandas.read_iceberg")<br>(table\_identifier\[, ...\]) | Read an Apache Iceberg table into a pandas DataFrame. |
| [`DataFrame.to_iceberg`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_iceberg.html#pandas.DataFrame.to_iceberg "pandas.DataFrame.to_iceberg")<br>(table\_identifier\[, ...\]) | Write a DataFrame to an Apache Iceberg table. |

Warning

`read_iceberg` is experimental and may change without warning.

ORC[#](https://pandas.pydata.org/docs/reference/io.html#orc "Link to this heading")

------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_orc`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")<br>(path\[, columns, dtype\_backend, ...\]) | Load an ORC object from the file path, returning a DataFrame. |
| [`DataFrame.to_orc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "pandas.DataFrame.to_orc")<br>(\[path, engine, index, ...\]) | Write a DataFrame to the Optimized Row Columnar (ORC) format. |

SAS[#](https://pandas.pydata.org/docs/reference/io.html#sas "Link to this heading")

------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_sas`](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "pandas.read_sas")<br>(filepath\_or\_buffer, \*\[, format, ...\]) | Read SAS files stored as either XPORT or SAS7BDAT format files. |

SPSS[#](https://pandas.pydata.org/docs/reference/io.html#spss "Link to this heading")

--------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_spss`](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas.read_spss "pandas.read_spss")<br>(path\[, usecols, ...\]) | Load an SPSS file from the file path, returning a DataFrame. |

SQL[#](https://pandas.pydata.org/docs/reference/io.html#sql "Link to this heading")

------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_sql_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table "pandas.read_sql_table")<br>(table\_name, con\[, schema, ...\]) | Read SQL database table into a DataFrame. |
| [`read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas.read_sql_query "pandas.read_sql_query")<br>(sql, con\[, index\_col, ...\]) | Read SQL query into a DataFrame. |
| [`read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "pandas.read_sql")<br>(sql, con\[, index\_col, ...\]) | Read SQL query or database table into a DataFrame. |
| [`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")<br>(name, con, \*\[, schema, ...\]) | Write records stored in a DataFrame to a SQL database. |

STATA[#](https://pandas.pydata.org/docs/reference/io.html#stata "Link to this heading")

----------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`read_stata`](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html#pandas.read_stata "pandas.read_stata")<br>(filepath\_or\_buffer, \*\[, ...\]) | Read Stata file into DataFrame. |
| [`DataFrame.to_stata`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas.DataFrame.to_stata "pandas.DataFrame.to_stata")<br>(path, \*\[, convert\_dates, ...\]) | Export DataFrame object to Stata dta format. |

|     |     |
| --- | --- |
| [`StataReader.data_label`](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html#pandas.io.stata.StataReader.data_label "pandas.io.stata.StataReader.data_label") | Return data label of Stata file. |
| [`StataReader.value_labels`](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html#pandas.io.stata.StataReader.value_labels "pandas.io.stata.StataReader.value_labels")<br>() | Return a nested dict mapping each value label name to its values and labels. |
| [`StataReader.variable_labels`](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html#pandas.io.stata.StataReader.variable_labels "pandas.io.stata.StataReader.variable_labels")<br>() | Return a dict associating each variable name with corresponding label. |
| [`StataWriter.write_file`](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html#pandas.io.stata.StataWriter.write_file "pandas.io.stata.StataWriter.write_file")<br>() | Export DataFrame object to Stata dta format. |

On this page