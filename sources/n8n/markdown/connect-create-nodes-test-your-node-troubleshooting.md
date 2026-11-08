For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting.md)
.

Credentials[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#credentials)

---------------------------------------------------------------------------------------------------

### Error message: 'Credentials of type "\*" aren't known'[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#error-message-credentials-of-type-arent-known)

Check that the name in the credentials array matches the name used in the property name of the credentials' class. For example, this credential class sets `name` to `friendGridApi`:

Copy

    export class FriendGridApi implements ICredentialType {
    	name = 'friendGridApi';
    	displayName = 'FriendGrid API';
    	documentationUrl = 'friendGrid';
    	properties = [\
    		{\
    			displayName: 'API Key',\
    			name: 'apiKey',\
    			type: 'string' as NodePropertyTypes,\
    			default: '',\
    		},\
    	];
    }

The node's `credentials` array must reference that same `name` value:

Copy

    credentials: [\
    	{\
    		name: 'friendGridApi',\
    		required: true,\
    	},\
    ],

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-41945b2238327b3872534227d57b19790cf4a842%252Ftroubleshooting-credentials-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f4f09ec6d3c2083a9821dcdbe7d81521&sv=3)

Code examples with arrows linking the credential class's name property to the matching name field in the node's credentials array

Editor UI[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#editor-ui)

-----------------------------------------------------------------------------------------------

### Error message: 'There was a problem loading init data: API-Server can not be reached. It's probably down'[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#error-message-there-was-a-problem-loading-init-data-api-server-can-not-be-reached-its-probably-down)

*   Check that the names of the node file, node folder, and class match the path added to `packages/nodes-base/package.json`.
    
*   Check that the names used in the `displayOptions` property are names used by UI elements in the node.
    

### Node icon doesn't show up in the Add Node menu and the Editor UI[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#node-icon-doesnt-show-up-in-the-add-node-menu-and-the-editor-ui)

*   Check that the icon is in the same folder as the node.
    
*   Check that it's either in PNG or SVG format.
    
*   When the `icon` property references the icon file, check that it includes the logo extension (`.png` or `.svg`) and that it prefixes it with `file:`. For example, `file:friendGrid.png` or `file:friendGrid.svg`.
    

### Node icon doesn't fit[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#node-icon-doesnt-fit)

*   If you use an SVG file, make sure the canvas size is square. Refer to [GIMP's guide to resizing the canvas](https://docs.gimp.org/2.10/en/gimp-image-resize.html)
     to change the canvas size of an SVG file.
    
*   If you use a PNG file, make sure that it's 60x60 pixels.
    

### Node doesn't show up in the Add Node menu[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#node-doesnt-show-up-in-the-add-node-menu)

Check that you registered the node in the `package.json` file in your project.

### Changes to the description properties don't show in the UI on refreshing[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#changes-to-the-description-properties-dont-show-in-the-ui-on-refreshing)

Every time you change the description properties, you have to stop the current `n8n-node dev` process (`ctrl` + `c`) and run it again.

### Linter incorrectly warning about file name case[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#linter-incorrectly-warning-about-file-name-case)

The node linter has rules for file names, including what case they should be. Windows users may encounter an issue when renaming files that causes the linter to continue giving warnings, even after you rename the files. This is due to a [known Windows issue](https://answers.microsoft.com/en-us/windows/forum/all/file-renaming-when-changing-case-doesnt-work/aa15ff7c-dd2d-4ed3-bcce-799ca90d4e58)
 with changing case when renaming files.

Related resources[](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting#related-resources)

---------------------------------------------------------------------------------------------------------------

*   [Test your node](https://docs.n8n.io/connect/create-nodes/test-your-node)
    
*   [Run your node locally](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally)
    
*   [Node linter](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter)
    

[PreviousNode linter](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter)
[NextDeploy your node](https://docs.n8n.io/connect/create-nodes/deploy-your-node)

Last updated 10 days ago

Was this helpful?