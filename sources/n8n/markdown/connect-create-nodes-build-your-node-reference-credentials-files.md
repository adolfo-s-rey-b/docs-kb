For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files.md)
.

The credentials file defines the authorization methods for the node. The settings in this file affect what n8n displays in the **Credentials** modal, and must reflect the authentication requirements of the service you're connecting to.

In the credentials file, you can use all the [n8n UI elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements)
. n8n encrypts the data that's stored using credentials using an encryption key.

Structure of the credentials file[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#structure-of-the-credentials-file)

------------------------------------------------------------------------------------------------------------------------------------------------------------

The credentials file follows this basic structure:

1.  Import statements
    
2.  Create a class for the credentials
    
3.  Within the class, define the properties that control authentication for the node.
    

### Outline structure[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#outline-structure)

Copy

    import {
    	IAuthenticateGeneric,
    	ICredentialTestRequest,
    	ICredentialType,
    	INodeProperties,
    } from 'n8n-workflow';
    
    export class ExampleNode implements ICredentialType {
    	name = 'exampleNodeApi';
    	displayName = 'Example Node API';
    	documentationUrl = '';
    	properties: INodeProperties[] = [\
    		{\
    			displayName: 'API Key',\
    			name: 'apiKey',\
    			type: 'string',\
    			default: '',\
    		},\
    	];
    	authenticate: IAuthenticateGeneric = {
    		type: 'generic',
    		properties: {
        		// Can be body, header, qs or auth
    			qs: {
            		// Use the value from `apiKey` above
    				'api_key': '={{$credentials.apiKey}}'
    			}
    
    		},
    	};
    	test: ICredentialTestRequest = {
    		request: {
    			baseURL: '={{$credentials?.domain}}',
    			url: '/bearer',
    		},
    	};
    }

Parameters[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#parameters)

--------------------------------------------------------------------------------------------------------------

### `name`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#name)

String. The internal name of the object. Used to reference it from other places in the node.

### `displayName`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#displayname)

String. The name n8n uses in the GUI.

### `documentationUrl`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#documentationurl)

String. URL to your credentials documentation.

### `properties`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#properties)

Each object contains:

*   `displayName`: the name n8n uses in the GUI.
    
*   `name`: the internal name of the object. Used to reference it from other places in the node.
    
*   `type`: the data type expected, such as `string`.
    
*   `default`: the URL that n8n should use to test credentials.
    

### `authenticate`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#authenticate)

*   `authenticate`: Object. Contains objects that tell n8n how to inject the authentication data as part of the API request.
    

#### `type`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#type)

String. If you're using an authentication method that sends data in the header, body, or query string, set this to `'generic'`.

#### `properties`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#properties-1)

Object. Defines the authentication methods. Options are:

*   `body`: Object. Sends authentication data in the request body. Can contain nested objects.
    

Copy

    authenticate: IAuthenticateGeneric = {
    	type: 'generic',
    	properties: {
    		body: {
    			username: '={{$credentials.username}}',
    			password: '={{$credentials.password}}',
    		},
    	},
    };

*   `header`: Object. Send authentication data in the request header.
    

Copy

    authenticate: IAuthenticateGeneric = {
    	type: 'generic',
    	properties: {
    		header: {
    			Authorization: '=Bearer {{$credentials.authToken}}',
    		},
    	},
    };

*   `qs`: Object. Stands for "query string." Send authentication data in the request query string.
    

Copy

    authenticate: IAuthenticateGeneric = {
    	type: 'generic',
    	properties: {
    		qs: {
    			token: '={{$credentials.token}}',
    		},
    	},
    };

*   `auth`: Object. Used for Basic Auth. Requires `username` and `password` as the key names.
    

Copy

    authenticate: IAuthenticateGeneric = {
    	type: 'generic',
    	properties: {
    		auth: {
    			username: '={{$credentials.username}}',
    			password: '={{$credentials.password}}',
    		},
    	},
    };

### `test`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#test)

Provide a `request` object containing a URL and authentication type that n8n can use to test the credential.

Copy

    test: ICredentialTestRequest = {
    		request: {
    			baseURL: '={{$credentials?.domain}}',
    			url: '/bearer',
    		},
    	};

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files#related-resources)

----------------------------------------------------------------------------------------------------------------------------

*   [Node building reference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference)
    

[PreviousCodex files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files)
[NextHTTP request helpers](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers)

Last updated 10 days ago

Was this helpful?