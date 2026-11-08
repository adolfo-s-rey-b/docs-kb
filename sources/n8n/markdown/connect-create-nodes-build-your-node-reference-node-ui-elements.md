For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements.md)
.

n8n provides a set of predefined UI components (based on a JSON file) that allows users to input all sorts of data types. The following UI elements are available in n8n.

String[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#string)

-----------------------------------------------------------------------------------------------------

Basic configuration:

Copy

    {
    	displayName: Name, // The value the user sees in the UI
    	name: name, // The name used to reference the element UI within the code
    	type: string,
    	required: true, // Whether the field is required or not
    	default: 'n8n',
    	description: 'The name of the user',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-2e5130ae379e975465b3ba728ecd99d216afd913%252Fstring.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b88b5229ddb1a925729c338767ae3b62&sv=3)

String field example: a Name input with Fixed/Expression toggle and the value n8n typed in

String field for inputting passwords:

Copy

    {
    	displayName: 'Password',
    	name: 'password',
    	type: 'string',
    	required: true,
    	typeOptions: {
    		password: true,
    	},
    	default: '',
    	description: `User's password`,
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-806be839d128a6c3db7e14b7f4aad6b22bb690dd%252Fpassword.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94f8b3c2eb17b990a7691428e5e42a8d&sv=3)

Password field example: a Password input showing masked dots instead of the typed value

String field with more than one row:

Copy

    {
    	displayName: 'Description',
    	name: 'description',
    	type: 'string',
    	required: true,
    	typeOptions: {
    		rows: 4,
    	},
    	default: '',
    	description: 'Description',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-78e0d914f544d7256ed9fadbd3ff019024460da4%252Fmultiple-rows.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1af9391c7559c0cda223d25ef0237793&sv=3)

Multi-row string field example: a Description textarea spanning several lines of text

### Support drag and drop for data keys[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#support-drag-and-drop-for-data-keys)

Users can drag and drop data values to map them to fields. Dragging and dropping creates an expression to load the data value. n8n supports this automatically.

You need to add an extra configuration option to support dragging and dropping data keys:

*   `requiresDataPath: 'single'`: for fields that require a single string.
    
*   `requiresDataPath: 'multiple'`: for fields that can accept a comma-separated list of string.
    

The [Compare Datasets node code](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/CompareDatasets/CompareDatasets.node.ts)
 has examples.

Number[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#number)

-----------------------------------------------------------------------------------------------------

Number field with decimal points:

Copy

    {
    	displayName: 'Amount',
    	name: 'amount',
    	type: 'number',
    	required: true,
    	typeOptions: {
    		maxValue: 10,
    		minValue: 0,
    		numberPrecision: 2,
    	},
    	default: 10.00,
    	description: 'Your current amount',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-e7076525714e815d4b8346261b643b89aee67736%252Fdecimal.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=26dc04d2a2bdc2a5ae06bf967044c564&sv=3)

Decimal number field example: an Amount input showing the value 10.00

Collection[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#collection)

-------------------------------------------------------------------------------------------------------------

Use the `collection` type when you need to display optional fields.

Copy

    {
    	displayName: 'Filters',
    	name: 'filters',
    	type: 'collection',
    	placeholder: 'Add Field',
    	default: {},
    	options: [\
    		{\
    			displayName: 'Type',\
    			name: 'type',\
    			type: 'options',\
    			options: [\
    				{\
    					name: 'Automated',\
    					value: 'automated',\
    				},\
    				{\
    					name: 'Past',\
    					value: 'past',\
    				},\
    				{\
    					name: 'Upcoming',\
    					value: 'upcoming',\
    				},\
    			],\
    			default: '',\
    		},\
    	],
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-8adcf2d9e4745535104d9a7727812e29638a3c69%252Fcollection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b5539d20f5f9a2abe7b105c78189abda&sv=3)

Collection field example: a Filters group with an optional Type dropdown open, listing Automated, Past, and Upcoming

DateTime[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#datetime)

---------------------------------------------------------------------------------------------------------

The `dateTime` type provides a date picker.

Copy

    {
    	displayName: 'Modified Since',
    	name: 'modified_since',
    	type: 'dateTime',
    	default: '',
    	description: 'The date and time when the file was last modified',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-cb8d40982e8fe6b122ca8237bf4e017892f431fe%252Fdatetime.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e6e898a99e3702c7db21fb04a26346c&sv=3)

DateTime field example: a date input opening a calendar picker to choose a date and time

Boolean[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#boolean)

-------------------------------------------------------------------------------------------------------

The `boolean` type adds a toggle for entering true or false.

Copy

    {
    	displayName: 'Wait for Image',
    	name: 'waitForImage',
    	type: 'boolean',
    	default: true, // Initial state of the toggle
    	description: 'Whether to wait for the image or not',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-4e147a271bec679ab3145296dc658c4ba2cb74ac%252Fboolean.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=75cfca7441fa9b583b40bb5098e562ed&sv=3)

Boolean field example: a Wait for Image toggle switched on

Color[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#color)

---------------------------------------------------------------------------------------------------

The `color` type provides a color selector.

Copy

    {
    	displayName: 'Background Color',
    	name: 'backgroundColor',
    	type: 'color',
    	default: '', // Initially selected color
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-0e695590140c5fe9e94bbdfaff969c3a86bb7939%252Fcolor.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=24152304a14902e0becc7d372e908d89&sv=3)

Color field example: a Background Color input with its picker swatch expanded

Options[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#options)

-------------------------------------------------------------------------------------------------------

The `options` type adds an options list. Users can select a single value.

Copy

    {
    	displayName: 'Resource',
    	name: 'resource',
    	type: 'options',
    	options: [\
    		{\
    			name: 'Image',\
    			value: 'image',\
    		},\
    		{\
    			name: 'Template',\
    			value: 'template',\
    		},\
    	],
    	default: 'image', // The initially selected option
    	description: 'Resource to consume',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-28af49c0af9b787c99fb75300c0250b2c0ba32cc%252Foptions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5068968633a274bb2258322dab98fa7a&sv=3)

Options field example: a Resource dropdown open showing single-select choices Image and Template

Multi-options[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#multi-options)

-------------------------------------------------------------------------------------------------------------------

The `multiOptions` type adds an options list. Users can select more than one value.

Copy

    {
    	displayName: 'Events',
    	name: 'events',
    	type: 'multiOptions',
    	options: [\
    		{\
    			name: 'Plan Created',\
    			value: 'planCreated',\
    		},\
    		{\
    			name: 'Plan Deleted',\
    			value: 'planDeleted',\
    		},\
    	],
    	default: [], // Initially selected options
    	description: 'The events to be monitored',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-64d7cf6e47080563224b8405731cff5ca6672191%252Fmultioptions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=20d322edd0bafdc91fbb1c38787d2acd&sv=3)

Multi-options field example: an Events field with Plan Created and Plan Deleted both selected as removable tags

Filter[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#filter)

-----------------------------------------------------------------------------------------------------

Use this component to evaluate, match, or filter incoming data.

This is the code from n8n's own If node. It shows a filter component working with a [collection](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#collection)
 component where users can configure the filter's behavior.

Copy

    {
    	displayName: 'Conditions',
    	name: 'conditions',
    	placeholder: 'Add Condition',
    	type: 'filter',
    	default: {},
    	typeOptions: {
    		filter: {
    			// Use the user options (below) to determine filter behavior
    			caseSensitive: '={{!$parameter.options.ignoreCase}}',
    			typeValidation: '={{$parameter.options.looseTypeValidation ? "loose" : "strict"}}',
    		},
    	},
    },
    {
    displayName: 'Options',
    name: 'options',
    type: 'collection',
    placeholder: 'Add option',
    default: {},
    options: [\
    	{\
    		displayName: 'Ignore Case',\
    		description: 'Whether to ignore letter case when evaluating conditions',\
    		name: 'ignoreCase',\
    		type: 'boolean',\
    		default: true,\
    	},\
    	{\
    		displayName: 'Less Strict Type Validation',\
    		description: 'Whether to try casting value types based on the selected operator',\
    		name: 'looseTypeValidation',\
    		type: 'boolean',\
    		default: true,\
    	},\
    ],
    },

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-afc841b7b202ccc7d77bdebf64286c2b3b8e0e83%252Ffilter.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e343a56686d8b5d99e2b9eb12656ef31&sv=3)

Filter field example: a Conditions builder with two rules joined by OR, using ends with and contains operators

Assignment collection (drag and drop)[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#assignment-collection-drag-and-drop)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the drag and drop component when you want users to pre-fill name and value parameters with a single drag interaction.

Copy

    {
    	displayName: 'Fields to Set',
    	name: 'assignments',
    	type: 'assignmentCollection',
    	default: {},
    },

You can see an example in n8n's [Edit Fields (Set) node](https://github.com/n8n-io/n8n/tree/0faeab1228e26d69a2a93bdb2f89523cca1e4036/packages/nodes-base/nodes/Set/v2)
:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-8e0ced88d29ade1704b527beada433d82058453b%252Fdrag-drop-fixed-toggle.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8567dc4827a5c56f475fdaf7a9f6cde3&sv=3)

A gif showing the drag and drop action, as well as changing a field to fixed

Fixed collection[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#fixed-collection)

-------------------------------------------------------------------------------------------------------------------------

Use the `fixedCollection` type to group fields that are semantically related.

Copy

    {
    	displayName: 'Metadata',
    	name: 'metadataUi',
    	placeholder: 'Add Metadata',
    	type: 'fixedCollection',
    	default: '',
    	typeOptions: {
    		multipleValues: true,
    	},
    	description: '',
    	options: [\
    		{\
    			name: 'metadataValues',\
    			displayName: 'Metadata',\
    			values: [\
    				{\
    					displayName: 'Name',\
    					name: 'name',\
    					type: 'string',\
    					default: 'Name of the metadata key to add.',\
    				},\
    				{\
    					displayName: 'Value',\
    					name: 'value',\
    					type: 'string',\
    					default: '',\
    					description: 'Value to set for the metadata key.',\
    				},\
    			],\
    		},\
    	],
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-b890580ace771e777e16b2bb178315f85ca303f5%252Ffixed-collection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b4dd04597cca8b8a5c117ea8f088eb9d&sv=3)

Fixed collection example: a Metadata group with two repeated Name/Value field pairs and an Add Metadata button

Resource locator[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#resource-locator)

-------------------------------------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-57620ce269232bcf7909d4eba25becf85b15e2ac%252Fresource-locator.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=09fab55465754929426742c4b85bcfc9&sv=3)

Resource locator field example: a Card field with its mode dropdown open, offering By ID, By URL, and From list

The resource locator element helps users find a specific resource in an external service, such as a card or label in Trello.

The following options are available:

*   ID
    
*   URL
    
*   List: allows users to select or search from a prepopulated list. This option requires more coding, as you must populate the list, and handle searching if you choose to support it.
    

You can choose which types to include.

Example:

Copy

    {
    	displayName: 'Card',
    	name: 'cardID',
    	type: 'resourceLocator',
    	default: '',
    	description: 'Get a card',
    	modes: [\
    		{\
    			displayName: 'ID',\
    			name: 'id',\
    			type: 'string',\
    			hint: 'Enter an ID',\
    			validation: [\
    				{\
    					type: 'regex',\
    					properties: {\
    						regex: '^[0-9]',\
    						errorMessage: 'The ID must start with a number',\
    					},\
    				},\
    			],\
    			placeholder: '12example',\
    			// How to use the ID in API call\
    			url: '=http://api-base-url.com/?id={{$value}}',\
    		},\
    		{\
    			displayName: 'URL',\
    			name: 'url',\
    			type: 'string',\
    			hint: 'Enter a URL',\
    			validation: [\
    				{\
    					type: 'regex',\
    					properties: {\
    						regex: '^http',\
    						errorMessage: 'Invalid URL',\
    					},\
    				},\
    			],\
    			placeholder: 'https://example.com/card/12example/',\
    			// How to get the ID from the URL\
    			extractValue: {\
    				type: 'regex',\
    				regex: 'example.com/card/([0-9]*.*)/',\
    			},\
    		},\
    		{\
    			displayName: 'List',\
    			name: 'list',\
    			type: 'list',\
    			typeOptions: {\
    				// You must always provide a search method\
    				// Write this method within the methods object in your base file\
    				// The method must populate the list, and handle searching if searchable: true\
    				searchListMethod: 'searchMethod',\
    				// If you want users to be able to search the list\
    				searchable: true,\
    				// Set to true if you want to force users to search\
    				// When true, users can't browse the list\
    				// Or false if users can browse a list\
    				searchFilterRequired: true,\
    			},\
    		},\
    	],
    	displayOptions: {
    		// the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			],
    		},
    	},
    },

Refer to the following for live examples:

*   Refer to [`CardDescription.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Trello/CardDescription.ts)
     and [`Trello.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Trello/Trello.node.ts)
     in n8n's Trello node for an example of a list with search that includes `searchFilterRequired: true`.
    
*   Refer to [`GoogleDrive.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Drive/GoogleDrive.node.ts)
     for an example where users can browse the list or search.
    

Resource mapper[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#resource-mapper)

-----------------------------------------------------------------------------------------------------------------------

If your node performs insert, update, or upsert operations, you need to send data from the node in a format supported by the service you're integrating with. A common pattern is to use a Set node before the node that sends data, to convert the data to match the schema of the service you're connecting to. The resource mapper UI component provides a way to get data into the required format directly within the node, rather than using a Set node. The resource mapper component can also validate input data against the schema provided in the node, and cast input data into the expected type.

**Mapping and matching**

Mapping is the process of setting the input data to use as values when updating row(s). Matching is the process of using column names to identify the row(s) to update.

Copy

    {
    	displayName: 'Columns',
    	name: 'columns', // The name used to reference the element UI within the code
    	type: 'resourceMapper', // The UI element type
    	default: {
    		// mappingMode can be defined in the component (mappingMode: 'defineBelow')
    		// or you can attempt automatic mapping (mappingMode: 'autoMapInputData')
    		mappingMode: 'defineBelow',
    		// Important: always set default value to null
    		value: null,
    	},
    	required: true,
    	// See "Resource mapper type options interface" below for the full typeOptions specification
    	typeOptions: {
    		resourceMapper: {
    			resourceMapperMethod: 'getMappingColumns',
    			mode: 'update',
    			fieldWords: {
    				singular: 'column',
    				plural: 'columns',
    			},
    			addAllFields: true, 
    			multiKeyMatch: true,
    			supportAutoMap: true,
    			matchingFieldsLabels: {
    				title: 'Custom matching columns title',
    				description: 'Help text for custom matching columns',
    				hint: 'Below-field hint for custom matching columns',
    			},
    		},
    	},
    },

Refer to the [Postgres node (version 2)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Postgres/v2)
 for a live example using a database schema.

Refer to the [Google Sheets node (version 2)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Sheet/v2)
 for a live example using a schema-less service.

### Resource mapper type options interface[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#resource-mapper-type-options-interface)

The `typeOptions` section must implement the following interface:

Copy

    export interface ResourceMapperTypeOptions {
    	// The name of the method where you fetch the schema
    	// Refer to the Resource mapper method section for more detail
    	resourceMapperMethod: string;
    	// Choose the mode for your operation
    	// Supported modes: add, update, upsert
    	mode: 'add' | 'update' | 'upsert';
    	// Specify labels for fields in the UI
    	fieldWords?: { singular: string; plural: string };
    	// Whether n8n should display a UI input for every field when node first added to workflow
    	// Default is true
    	addAllFields?: boolean;
    	// Specify a message to show if no fields are fetched from the service 
    	// (the call is successful but the response is empty)
    	noFieldsError?: string;
    	// Whether to support multi-key column matching
    	// multiKeyMatch is for update and upsert only
    	// Default is false
    	// If true, the node displays a multi-select dropdown for the matching column selector
    	multiKeyMatch?: boolean;
    	// Whether to support automatic mapping
    	// If false, n8n hides the mapping mode selector field and sets mappingMode to defineBelow
    	supportAutoMap?: boolean;
    	// Custom labels for the matching columns selector
    	matchingFieldsLabels?: {
    		title?: string;
    		description?: string;
    		hint?: string;
    	};
    }

### Resource mapper method[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#resource-mapper-method)

This method contains your node-specific logic for fetching the data schema. Every node must implement its own logic for fetching the schema, and setting up each UI field according to the schema.

It must return a value that implements the `ResourceMapperFields` interface:

Copy

    interface ResourceMapperField {
    	// Field ID as in the service
    	id: string;
    	// Field label
    	displayName: string;
    	// Whether n8n should pre-select the field as a matching field
    	// A matching field is a column used to identify the rows to modify
    	defaultMatch: boolean;
    	// Whether the field can be used as a matching field
    	canBeUsedToMatch?: boolean;
    	// Whether the field is required by the schema
    	required: boolean;
    	// Whether to display the field in the UI
    	// If false, can't be used for matching or mapping
    	display: boolean;
    	// The data type for the field
    	// These correspond to UI element types
    	// Supported types: string, number, dateTime, boolean, time, array, object, options
    	type?: FieldType;
    	// Added at runtime if the field is removed from mapping by the user
    	removed?: boolean;
    	// Specify options for enumerated types
    	options?: INodePropertyOptions[];
    }

Refer to the [Postgres resource mapping method](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Postgres/v2/methods/resourceMapping.ts)
 and [Google Sheets resource mapping method](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Sheet/v2/methods/resourceMapping.ts)
 for live examples.

JSON[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#json)

-------------------------------------------------------------------------------------------------

Copy

    {
    	displayName: 'Content (JSON)',
    	name: 'content',
    	type: 'json',
    	default: '',
    	description: '',
    	displayOptions: { // the resources and operations to display this element with
    		show: {
    			resource: [\
    				// comma-separated list of resource names\
    			],
    			operation: [\
    				// comma-separated list of operation names\
    			]
    		}
    	},
    }

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-2b70f47ebb80360103b8af70026ebc5363400389%252Fjson.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ea92f12786a5fcf614bd33c6e5b12247&sv=3)

JSON field example: a Content (JSON) code editor with syntax-highlighted keys and values

HTML[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#html)

-------------------------------------------------------------------------------------------------

The HTML editor allows users to create HTML templates in their workflows. The editor supports standard HTML, CSS in `<style>` tags, and expressions wrapped in `{{}}`. Users can add `<script>` tags to pull in additional JavaScript. n8n doesn't run this JavaScript during workflow execution.

Copy

    {
    	displayName: 'HTML Template', // The value the user sees in the UI
    	name: 'html', // The name used to reference the element UI within the code
    	type: 'string',
    	typeOptions: {
    		editor: 'htmlEditor',
    	},
    	default: placeholder, // Loads n8n's placeholder HTML template
    	noDataExpression: true, // Prevent using an expression for the field
    	description: 'HTML template to render',
    },

Refer to [`Html.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Html/Html.node.ts)
 for a live example.

Notice[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#notice)

-----------------------------------------------------------------------------------------------------

Display a yellow box with a hint or extra info. Refer to [Node UI design](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design)
 for guidance on writing good hints and info text.

Copy

    {
      displayName: 'Your text here',
      name: 'notice',
      type: 'notice',
      default: '',
    },

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-c95b16eec0fd56beb155a468387b7ceec6ec7d23%252Fnotice.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b5d9e60d96ca067859f886e93e9b8009&sv=3)

Notice field example: a pale yellow info box displaying placeholder text

Hints[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#hints)

---------------------------------------------------------------------------------------------------

There are two types of hints: parameter hints and node hints:

*   Parameter hints are small lines of text below a user input field.
    
*   Node hints are a more powerful and flexible option than [Notice](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#notice)
    . Use them to display longer hints, in the input panel, output panel, or node details view.
    

### Add a parameter hint[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#add-a-parameter-hint)

Add the `hint` parameter to a UI element:

Copy

    {
    	displayName: 'URL',
    	name: 'url',
    	type: 'string',
    	hint: 'Enter a URL',
    	...
    }

### Add a node hint[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#add-a-node-hint)

Define the node's hints in the `hints` property within the node `description`:

Copy

    description: INodeTypeDescription = {
    	...
    	hints: [\
    		{\
    			// The hint message. You can use HTML.\
    			message: "This node has many input items. Consider enabling <b>Execute Once</b> in the node\'s settings.",\
    			// Choose from: info, warning, danger. The default is 'info'.\
    			// Changes the color. info (grey), warning (yellow), danger (red)\
    			type: 'info',\
    			// Choose from: inputPane, outputPane, ndv. By default n8n displays the hint in both the input and output panels.\
    			location: 'outputPane',\
    			// Choose from: always, beforeExecution, afterExecution. The default is 'always'\
    			whenToDisplay: 'beforeExecution',\
    			// Optional. An expression. If it resolves to true, n8n displays the message. Defaults to true.\
    			displayCondition: '={{ $parameter["operation"] === "select" && $input.all().length > 1 }}'\
    		}\
    	]
    	...
    }

### Add a dynamic hint to a programmatic-style node[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#add-a-dynamic-hint-to-a-programmatic-style-node)

In programmatic-style nodes you can create a dynamic message that includes information from the node execution. As it relies on the node output data, you can't display this type of hint until after execution.

Copy

    if (operation === 'select' && items.length > 1 && !node.executeOnce) {
        // Expects two parameters: NodeExecutionData and an array of hints
    	return new NodeExecutionOutput(
    		[returnData],
    		[\
    			{\
    				message: `This node ran ${items.length} times, once for each input item. To run for the first item only, enable <b>Execute once</b> in the node settings.`,\
    				location: 'outputPane',\
    			},\
    		],
    	);
    }
    return [returnData];

For a live example of a dynamic hint in a programmatic-style node, view the [Split Out node code](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Transform/SplitOut/SplitOut.node.ts#L266)
.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Node building reference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference)
    

[PreviousReference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference)
[NextCode standards](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/code-standards)

Last updated 10 days ago

Was this helpful?