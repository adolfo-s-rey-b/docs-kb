For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data.md)
.

[JMESPath](https://jmespath.org/)
 is a query language for JSON that you can use to extract and transform elements from a JSON document. For full details of how to use JMESPath, refer to the [JMESPath documentation](https://jmespath.org/tutorial.html)
.

The `jmespath()` method[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#the-jmespath-method)

----------------------------------------------------------------------------------------------------------------------------------

n8n provides a custom method, `jmespath()`. Use this method to perform a search on a JSON object using the JMESPath query language.

The basic syntax is:

Copy

    $jmespath(object, searchString)

**JavaScript only**

The Python Code node doesn't provide `$jmespath()`. To get the same results in Python, use standard Python instead. Each example below includes a Python version.

To help understand what the method does, here is the equivalent longer JavaScript:

Copy

    var jmespath = require('jmespath');
    jmespath.search(object, searchString);

**Expressions must be single-line**

The longer code example doesn't work in Expressions, as they must be single-line.

`object` is a JSON object, such as the output of a previous node. `searchString` is an expression written in the JMESPath query language. The [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification)
 provides a list of supported expressions, while their [Tutorial](https://jmespath.org/tutorial.html)
 and [Examples](https://jmespath.org/examples.html)
 provide interactive examples.

**Search parameter order**

The examples in the [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification)
 follow the pattern `search(searchString, object)`. The [JMESPath JavaScript library](https://github.com/jmespath/jmespath.js/)
, which n8n uses, supports `search(object, searchString)` instead. This means that when using examples from the JMESPath documentation, you may need to change the order of the search function parameters.

Common tasks[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#common-tasks)

----------------------------------------------------------------------------------------------------------------

This section provides examples for some common operations. More examples, and detailed guidance, are available in [JMESPath's own documentation](https://jmespath.org/tutorial.html)
.

When trying out these examples, you need to set the Code node **Mode** to **Run Once for Each Item**.

### Apply a JMESPath expression to a collection of elements with projections[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#apply-a-jmespath-expression-to-a-collection-of-elements-with-projections)

From the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections)
:

> Projections are one of the key features of JMESPath. Use it to apply an expression to a collection of elements. JMESPath supports five kinds of projections:
> 
> *   List Projections
>     
> *   Slice Projections
>     
> *   Object Projections
>     
> *   Flatten Projections
>     
> *   Filter Projections
>     

The following example shows basic usage of list, slice, and object projections. Refer to the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections)
 for detailed explanations of each projection type, and more examples.

Given this JSON from a webhook node:

Copy

    [\
      {\
        "headers": {\
          "host": "n8n.instance.address",\
          ...\
        },\
        "params": {},\
        "query": {},\
        "body": {\
          "people": [\
            {\
              "first": "James",\
              "last": "Green"\
            },\
            {\
              "first": "Jacob",\
              "last": "Jones"\
            },\
            {\
              "first": "Jayden",\
              "last": "Smith"\
            }\
          ],\
          "dogs": {\
            "Fido": {\
              "color": "brown",\
              "age": 7\
            },\
            "Spot": {\
              "color": "black and white",\
              "age": 5\
            }\
          }\
        }\
      }\
    ]
    

Retrieve a [list](https://jmespath.org/tutorial.html#list-and-slice-projections)
 of all the people's first names:

Expressions (JavaScript)

Code node (JavaScript)

Code node (Python)

Copy

    {{$jmespath($json.body.people, "[*].first" )}}
    // Returns ["James", "Jacob", "Jayden"]

Copy

    let firstNames = $jmespath($json.body.people, "[*].first" )
    return {firstNames};
    /* Returns:
    [\
    	{\
    		"firstNames": [\
    			"James",\
    			"Jacob",\
    			"Jayden"\
    		]\
    	}\
    ]
    */

Copy

    people = _item["json"]["body"]["people"]
    first_names = [person["first"] for person in people]
    return {"firstNames": first_names}
    """
    Returns:
    [\
     	{\
    		"firstNames": [\
    			"James",\
    			"Jacob",\
    			"Jayden"\
    		]\
    	}\
    ]
    """

Get a [slice](https://jmespath.org/tutorial.html#list-and-slice-projections)
 of the first names:

Expressions (JavaScript)

Code node (JavaScript)

Code node (Python)

Copy

    {{$jmespath($json.body.people, "[:2].first")}}
    // Returns ["James", "Jacob"]

Copy

    let firstTwoNames = $jmespath($json.body.people, "[:2].first");
    return {firstTwoNames};
    /* Returns:
    [\
    	{\
    		"firstNames": [\
    			"James",\
    			"Jacob",\
    			"Jayden"\
    		]\
    	}\
    ]
    */

Copy

    people = _item["json"]["body"]["people"]
    first_two_names = [person["first"] for person in people[:2]]
    return {"firstTwoNames": first_two_names}
    """
    Returns:
    [\
    	{\
    		"firstTwoNames": [\
    		"James",\
    		"Jacob"\
    		]\
    	}\
    ]
    """

Get a list of the dogs' ages using [object projections](https://jmespath.org/tutorial.html#object-projections)
:

Expressions (JavaScript)

Code node (JavaScript)

Code node (Python)

Copy

    {{$jmespath($json.body.dogs, "*.age")}}
    // Returns [7,5]

Copy

    let dogsAges = $jmespath($json.body.dogs, "*.age");
    return {dogsAges};
    /* Returns:
    [\
    	{\
    		"dogsAges": [\
    			7,\
    			5\
    		]\
    	}\
    ]
    */

Copy

    dogs = _item["json"]["body"]["dogs"]
    dogs_ages = [dog["age"] for dog in dogs.values()]
    return {"dogsAges": dogs_ages}
    """
    Returns:
    [\
    	{\
    		"dogsAges": [\
    			7,\
    			5\
    		]\
    	}\
    ]
    """

### Select multiple elements and create a new list or object[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#select-multiple-elements-and-create-a-new-list-or-object)

Use [Multiselect](https://jmespath.org/tutorial.html#multiselect)
 to select elements from a JSON object and combine them into a new list or object.

Given this JSON from a webhook node:

Copy

    [\
      {\
        "headers": {\
          "host": "n8n.instance.address",\
          ...\
        },\
        "params": {},\
        "query": {},\
        "body": {\
          "people": [\
            {\
              "first": "James",\
              "last": "Green"\
            },\
            {\
              "first": "Jacob",\
              "last": "Jones"\
            },\
            {\
              "first": "Jayden",\
              "last": "Smith"\
            }\
          ],\
          "dogs": {\
            "Fido": {\
              "color": "brown",\
              "age": 7\
            },\
            "Spot": {\
              "color": "black and white",\
              "age": 5\
            }\
          }\
        }\
      }\
    ]
    

Use multiselect list to get the first and last names and create new lists containing both names:

Expressions (JavaScript)

Code node (JavaScript)

Code node (Python)

Copy

    {{$jmespath($json.body.people, "[].[first, last]")}}
    // Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]

Copy

    let newList = $jmespath($json.body.people, "[].[first, last]");
    return {newList};
    /* Returns:
    [\
    	{\
    		"newList": [\
    			[\
    				"James",\
    				"Green"\
    			],\
    			[\
    				"Jacob",\
    				"Jones"\
    			],\
    			[\
    				"Jayden",\
    				"Smith"\
    			]\
    		]\
    	}\
    ]
    */

Copy

    people = _item["json"]["body"]["people"]
    new_list = [[person["first"], person["last"]] for person in people]
    return {"newList": new_list}
    """
    Returns:
    [\
    	{\
    		"newList": [\
    			[\
    				"James",\
    				"Green"\
    			],\
    			[\
    				"Jacob",\
    				"Jones"\
    			],\
    			[\
    				"Jayden",\
    				"Smith"\
    			]\
    		]\
    	}\
    ]
    """

### An alternative to arrow functions in expressions[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#an-alternative-to-arrow-functions-in-expressions)

For example, generate some input data by returning the below code from the Code node:

Copy

    return[\
      {\
        "json": {      \
          "num_categories": "0",\
          "num_products": "45",\
          "category_id": 5529735,\
          "parent_id": 1407340,\
          "pos_enabled": 1,\
          "pos_favorite": 0,\
          "name": "HP",\
          "description": "",\
          "image": ""\
        }\
      },\
      {\
        "json": {\
          "num_categories": "0",\
          "num_products": "86",\
          "category_id": 5529740,\
          "parent_id": 1407340,\
          "pos_enabled": 1,\
          "pos_favorite": 0,\
          "name": "Lenovo",\
          "description": "",\
          "image": ""\
        }\
      }  \
    ]

You could do a search like "find the item with the name Lenovo and tell me their category ID."

Copy

    {{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}

Related resources[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data#related-resources)

--------------------------------------------------------------------------------------------------------------------------

*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Work with files and images](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images)
    
*   [Work with dates and times](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times)
    

[PreviousWork with dates and times](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times)
[NextData tables](https://docs.n8n.io/build/work-with-data/data-tables)

Last updated 10 days ago

Was this helpful?