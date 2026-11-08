For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md)
.

The Compare Datasets node helps you compare data from two input streams.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#node-parameters)

----------------------------------------------------------------------------------------------------------------------

1.  Decide which fields to compare. In **Input A Field**, enter the name of the field you want to use from input stream A. In **Input B Field**, enter the name of the field you want to use from input stream B.
    
2.  **Optional**: You can compare by multiple fields. Select **Add Fields to Match** to set up more comparisons.
    
3.  Choose how to handle differences between the datasets. In **When There Are Differences**, select one of the following:
    
    *   **Use Input A Version** to treat input stream A as the source of truth.
        
    *   **Use Input B Version** to treat input stream B as the source of truth.
        
    *   **Use a Mix of Versions** to use different inputs for different fields.
        
        *   Use **Prefer** to select either **Input A Version** or **Input B Version** as the main source of truth.
            
        *   Enter input fields that are exceptions to **For Everything Except** to pull from the other input source. To add multiple input fields, enter a comma-separated list.
            
        
    *   **Include Both Versions** to include both input streams in the output, which may make the structure more complex.
        
    
4.  Decide whether to use **Fuzzy Compare**. When turned on, the comparison will tolerate small type differences when comparing fields. For example, the number 3 and the string `3` are treated as the same with **Fuzzy Compare** turned on, but wouldn't be treated the same with it turned off.
    

Understand item comparison[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#understand-item-comparison)

--------------------------------------------------------------------------------------------------------------------------------------------

Item comparison is a two stage process:

1.  n8n checks if the values of the fields you selected to compare match across both inputs.
    
2.  If the fields to compare match, n8n then compares all fields within the items, to determine if the items are the same or different.
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#node-options)

----------------------------------------------------------------------------------------------------------------

Use the node **Options** to refine your comparison or tweak comparison behavior.

### Fields to Skip Comparing[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#fields-to-skip-comparing)

Enter field names that you want to ignore in the comparison.

For example, if you compare the two datasets below using `person.language` as the **Fields to Match**, n8n returns them as different. If you add `person.name` to **Fields to Skip Comparing**, n8n returns them as matching.

Copy

    	// Input 1
    	[\
    		{\
    			"person":\
    			{\
    				"name":	"Stefan",\
    				"language":	"de"\
    			}\
    		},\
    		{\
    			"person":\
    			{\
    				"name":	"Jim",\
    				"language":	"en"\
    			}\
    		},\
    		{\
    			"person":\
    			{\
    				"name":	"Hans",\
    				"language":	"de"\
    			}\
    		}\
    	]
    	// Input 2
    		[\
    		{\
    			"person":\
    			{\
    				"name":	"Sara",\
    				"language":	"de"\
    			}\
    		},\
    		{\
    			"person":\
    			{\
    				"name":	"Jane",\
    				"language":	"en"\
    			}\
    		},\
    		{\
    			"person":\
    			{\
    				"name":	"Harriet",\
    				"language":	"de"\
    			}\
    		}\
    	]

### Disable Dot Notation[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#disable-dot-notation)

Whether to disallow referencing child fields using `parent.child` in the field name (turned on) or allow it (turned off, default).

### Multiple Matches[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#multiple-matches)

Choose how to handle duplicate data. The default is **Include All Matches**. You can choose **Include First Match Only**.

For example, given these two datasets:

Copy

    	// Input 1
    	[\
    		{\
    			"fruit": {\
    				"type": "apple",\
    				"color": "red"\
    			}\
    		},\
    				{\
    			"fruit": {\
    				"type": "apple",\
    				"color": "red"\
    			}\
    		},\
    				{\
    			"fruit": {\
    				"type": "banana",\
    				"color": "yellow"\
    			}\
    		}\
    	]
    	// Input 2
    	[\
    		{\
    			"fruit": {\
    				"type": "apple",\
    				"color": "red"\
    			}\
    		},\
    				{\
    			"fruit": {\
    				"type": "apple",\
    				"color": "red"\
    			}\
    		},\
    				{\
    			"fruit": {\
    				"type": "banana",\
    				"color": "yellow"\
    			}\
    		}\
    	]

n8n returns three items in the **Same Branch** tab. The data is the same in both branches.

If you select **Include First Match Only**, n8n returns two items, in the **Same Branch** tab. The data is the same in both branches, but n8n only returns the first occurrence of the matching "apple" items.

Understand the output[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#understand-the-output)

----------------------------------------------------------------------------------------------------------------------------------

There are four output options:

*   **In A only Branch**: Contains data that occurs only in the first input.
    
*   **Same Branch**: Contains data that's the same in both inputs.
    
*   **Different Branch**: Contains data that's different between inputs.
    
*   **In B only Branch**: Contains data that occurs only in the second output.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------

[Browse Compare Datasets integration templates](https://n8n.io/integrations/compare-datasets)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues)
[NextCompression](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression)

Last updated 10 days ago

Was this helpful?