[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

User Interface Helpers[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#user-interface-helpers "Link to this heading")

===============================================================================================================================================

JupyterLab comes with helpers to show or request simple information from a user. Those speed up development and ensure a common look and feel.

Dialogs[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#dialogs "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

### Generic Dialog[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#generic-dialog "Link to this heading")

To display a generic dialog, use [`showDialog`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.showDialog.html)
 function from `@jupyterlab/apputils`.

The options available are:

showDialog({
  title: 'Dialog title', // Can be text or a react element
  body: 'Dialog body', // Can be text, a widget or a react element
  host: document.body, // Parent element for rendering the dialog
  buttons: \[\
    // List of buttons\
    {\
      label: 'my button', // Button label\
      caption: 'my button title', // Button title\
      className: 'my-button', // Additional button CSS class\
      accept: true, // Whether this button will discard or accept the dialog\
      displayType: 'default' // applies 'default' or 'warn' styles\
    }\
  \],
  checkbox: {
    // Optional checkbox in the dialog footer
    label: 'check me', // Checkbox label
    caption: "check me I'magic", // Checkbox title
    className: 'my-checkbox', // Additional checkbox CSS class
    checked: true // Default checkbox state
  },
  defaultButton: 0, // Index of the default button
  focusNodeSelector: '.my-input', // Selector for focussing an input element when dialog opens
  hasClose: false, // Whether to display a close button or not
  renderer: undefined // To define customized dialog structure
});

Copy to clipboard

Note

If no options are specified, the dialog will only contain _OK_ and _Cancel_ buttons.

### Dialog Button Helpers and Defaults[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#dialog-button-helpers-and-defaults "Link to this heading")

Use the [`Dialog`](https://jupyterlab.readthedocs.io/en/stable/api/modules/apputils.Dialog.html)
 helpers from [`apputils`](https://jupyterlab.readthedocs.io/en/stable/api/modules/apputils.html)
 to get consistent labels, styling and behavior:

*   [`okButton`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.Dialog.okButton.html)
    : creates an accept button (`accept: true`) with a default localized `Ok` label.
    
*   [`cancelButton`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.Dialog.cancelButton.html)
    : creates a reject button (`accept: false`) with a default localized `Cancel` label.
    
*   [`warnButton`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.Dialog.warnButton.html)
    : creates a warning-styled button (`displayType: 'warn'`); acceptance and label still follow [`createButton`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.Dialog.createButton.html)
    .
    
*   [`createButton`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.Dialog.createButton.html)
    : generic helper; if `accept` is omitted it defaults to `true`, and the default label is `Ok` for accept buttons and `Cancel` otherwise.
    

You only need to provide `label` when you want custom text.

### Message Dialogs[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#message-dialogs "Link to this heading")

Helper functions to show a message to the user are available in the [`apputils`](https://jupyterlab.readthedocs.io/en/stable/api/modules/apputils.html)
 package. These dialogs return a `Promise` resolving when the user dismisses the dialog.

There is one helper:

*   [`showErrorMessage`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.showErrorMessage.html)
     : show an error message dialog.
    

### Input Dialogs[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#input-dialogs "Link to this heading")

Helper functions to request a single input from the user are available in the `apputils` package within the [`InputDialog`](https://jupyterlab.readthedocs.io/en/stable/api/modules/apputils.InputDialog.html)
 namespace. There are four helpers:

*   [`getBoolean`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.InputDialog.getBoolean.html)
     : request a boolean through a checkbox.
    
*   [`getItem`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.InputDialog.getItem.html)
     : request a item from a list; the list may be editable.
    
*   [`getNumber`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.InputDialog.getNumber.html)
     : request a number; if the user input is not a valid number, NaN is returned.
    
*   [`getText`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.InputDialog.getText.html)
     : request a short text.
    
*   [`getPassword`](https://jupyterlab.readthedocs.io/en/stable/api/functions/apputils.InputDialog.getPassword.html)
     : request a short password.
    

All dialogs are built on the standard [`Dialog`](https://jupyterlab.readthedocs.io/en/stable/api/modules/apputils.Dialog.html)
 namespace using the [`Dialog`](https://jupyterlab.readthedocs.io/en/stable/api/classes/apputils.Dialog-1.html)
 class. Therefore the helper functions each return a `Promise` resolving in a [`IResult`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.Dialog.IResult.html)
 object.

// Request a boolean
InputDialog.getBoolean({ title: 'Check or not?' }).then(value \=> {
  console.log('boolean ' + value.value);
});

// Request a choice from a list
InputDialog.getItem({
  title: 'Pick a choice',
  items: \['1', '2'\]
}).then(value \=> {
  console.log('item ' + value.value);
});

// Request a choice from a list or specify your own choice
InputDialog.getItem({
  title: 'Pick a choice or write your own',
  items: \['1', '2'\],
  editable: true
}).then(value \=> {
  console.log('editable item ' + value.value);
});

// Request a number
InputDialog.getNumber({ title: 'How much?' }).then(value \=> {
  console.log('number ' + value.value);
});

// Request a text
InputDialog.getText({ title: 'Provide a text' }).then(value \=> {
  console.log('text ' + value.value);
});

// Request a text
InputDialog.getPassword({ title: 'Input password' }).then(value \=> {
  console.log('A password was input');
});

Copy to clipboard

Note

Try these helpers in a browser playground:

1.  Click **Load Interactive Example**.
    
2.  In the playground editor toolbar (or command palette), run `Load Current File As Extension`.
    
3.  Use the **UI Helpers Playground** panel buttons to preview dialogs, notifications, and file dialogs.
    

Interactive dialogs + notifications example.

Load Interactive Example[JupyterLab](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/index.html?hide=all#plugin=1.g.H4sIAAAAAAAAA71Y64_bNhL_V6ZGUcmArHpz7R2g1Okluwm6hz4WlwT90A0Qrji2maVIlaS8Nrb-3ws-bFMPO04uuE-yyZnfPDgv8nG0QqWZFKPiIhvdM0FHxWjOOI4y9_mVVDgqRkxQXOdGj7KRlo0q3VpVS2XgEf7T1BuD6pWSwrwUNOsu3PBmwQRsYa5kBcm_P_htTu6-JXXNWUkMkyJ5eituxQ70VgBcMcLlIrM_ry9lVRFBbwhHY9CviboxEc0vhInnCsnvjC7QuKVfpWHzgO8W9FI-eJZbcUSfxjCu28rAK8YxSILrK5yThhu79kLJB41q0DTrvTu_30HzCh6YeFMxIb99cMtBdCmFNlA7zxXDDv1hJRl9BjPvLEYLSBo2WSKvUekJxUoWnj9xppPGyNeGKFOAUY13ocI_G6ZQF_BH18NDdr7zQKVhK2KwgNT-BSB13VMx81u1RysGDxCAehEBvhiSaQnHMHvmrQTwjqHuMAImzPqWewLrywMTswFzgsftt1lEFEAnOGOyNoCsURyi5wSEDZeJ13pimQZgJKeoPglo7lj6UDdEID-BYWkmtSXy0XjgVo3wGsAMiN6IEtL4dADIA2EmyrN0vwNgmOFYQPL2Gn7y4uAKK5lkB5I7STcFJG-WTIdDBqYdnPDpQgQwYVC5KESgsmwqFMa5HnBNqppj3kJsjJHChrhXKC-JKJG_cMvpOAtlJpf3YekROLlDXkDyWjaCalhISRPYjt_tQLfj4NFt3zuuKh1zTqBC3XBH43wV1bF8geYNrs2Q035fEufXhlMwS2yFJmiy-TFpqbf7w-aQeoG590ROyhJrA998ExTJV4Q3OIZIZlw3cybmMo1JM3h01eSSS40F_GM6nR5cArA96psYFmZd57SE6qYsUevURwLTQCAstQ13MWHdQWWpwQZvnmSxKR1FzznC30LO6tORPniYh1y3Z7lHig-0IoIsbLVrV7-8khR5HnZ7eh4_yY-c3PvXyLE0SOHrx_gUc45iYZZbYAarVI_z9y2_HfUcnHfWv3Uq1v_gxZdrpg0TiyumsDRSbf5v3vTK6eDAG2KWGmattMkrUqfWg9Yo-81rYpYHMTuMCrUmC4RZ7OEWcDgPmM1mcBFTAfwIh0P0Jb2Arx9b3H9M323ft7mKHpfuseUfJBNpkkEy3r5_eiqMggGfmvscDbhGUnTmsx_85xn8BaLhHGbu04mjUiEx-Ly0avjqbMvGTlgo09ooJhb7ik8cdRHi7EbJimkMs9JfYL-eclzAT29--dnDvuRou8hAZN7txO46Te6VChxp4gmSgw9COJlNjba3hv3eNq7NpRTGSfWmdEm02XDMa0IpEzZ_kmn-ncIKpvm_vldY9SA9_Z1UFJUlv6jXoCVnFFZEpZPJh3riNyel5FI9GZ9E-C-hrLHhnvyzXh-jJOX9Qtkuaen2UjjZyMZ4KRfHpJSN0tLpWUvX0Xt0hNKXKxTmZ6YNClRpUnJW3idZt4aAO9bdWecKteQrTH0kpONxXhJTLlNUygp81i5z9pglx9ztepo4fTu54KkSO7aESIM5YRypaztxanzXSY123Tz8VGgaJYLNR5oSCt0odFOb65tHkyk2zlY4l3q21X_lfuVMXzFdS420VeeCDo4mzuV2KpT7cBX4EG4x6cGQ3ZBtlDyRLnWUKY62nQkHnZK3Gm1n17gb4cBIqBWuGD6E2VBnrWlAZ2AHWjsB7wjypCPNB19FlL2S2pyC6S6hYJrExliFciEp9hPxopV-LVpS1yjo5ZJxmjqJ8TDmXeTjRp9wEmWryE2BPqhBma452Vg1ForR5AiZ3XuDVc2JwUvJm8oJTBTWSExq43QyZyaDiomKrNMnT6b1OoOLuRqPj0KS2lehXfXpksW290t3mrxeyocwbifZ4Sox7pv6MaTn-h5eSQV2WPZQbor-DCSnU5ziHi5e-QxUO_24KUa37O1Mlp8N7Lp5Hzkat8adsBsO0CA1pq1DkbEp3i4y6eO-AkTlK9SVwWvk_gYZk7r7TO4anuWJ7oI3nGx8NxnmKbnU5I7brmpfMLoVNK5ehwJK6jov_U1X244Sbr1p6wUhmnx3d7_OHbWAVvDuqHGNZWPfN_bBHOSPP6pA_Bpxjvx2yA8p4FLgbPkDTxvnqOESYzOsQJw0Z-sx-EJyjiYDOTakVCfnPk2v_pPL-Zq1k_SoapGIT9ItfsM5W6lDioHjH9CrN1v5puVfJ2EWzyJpPN3YceMrT5Uz_dwYUi47Y4Y3SC-Rc2tN6qkzSCrC4gl6f4_osISHxxeb6x1vzmj_8nHwX3h-tMKu7S3XVjDnsKL3DJZBSQwupLLPT2_to-61HUrnpMSdI5ND3TsB3CksXwi1XS2-EOhgCfhC2EfS-kuiDyXnufhegrs22ABTqI1USHOzRJF2UmBPtU_FkCy9PNw_Kvkf21vhGxGu3dN_eKIIz_pPR9u_AeCczDB-GQAA "Open full JupyterLab view in a new tab")
 [Notebook v7](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/tree/index.html?hide=all#plugin=1.g.H4sIAAAAAAAAA71Y64_bNhL_V6ZGUcmArHpz7R2g1Okluwm6hz4WlwT90A0Qrji2maVIlaS8Nrb-3ws-bFMPO04uuE-yyZnfPDgv8nG0QqWZFKPiIhvdM0FHxWjOOI4y9_mVVDgqRkxQXOdGj7KRlo0q3VpVS2XgEf7T1BuD6pWSwrwUNOsu3PBmwQRsYa5kBcm_P_htTu6-JXXNWUkMkyJ5eituxQ70VgBcMcLlIrM_ry9lVRFBbwhHY9CviboxEc0vhInnCsnvjC7QuKVfpWHzgO8W9FI-eJZbcUSfxjCu28rAK8YxSILrK5yThhu79kLJB41q0DTrvTu_30HzCh6YeFMxIb99cMtBdCmFNlA7zxXDDv1hJRl9BjPvLEYLSBo2WSKvUekJxUoWnj9xppPGyNeGKFOAUY13ocI_G6ZQF_BH18NDdr7zQKVhK2KwgNT-BSB13VMx81u1RysGDxCAehEBvhiSaQnHMHvmrQTwjqHuMAImzPqWewLrywMTswFzgsftt1lEFEAnOGOyNoCsURyi5wSEDZeJ13pimQZgJKeoPglo7lj6UDdEID-BYWkmtSXy0XjgVo3wGsAMiN6IEtL4dADIA2EmyrN0vwNgmOFYQPL2Gn7y4uAKK5lkB5I7STcFJG-WTIdDBqYdnPDpQgQwYVC5KESgsmwqFMa5HnBNqppj3kJsjJHChrhXKC-JKJG_cMvpOAtlJpf3YekROLlDXkDyWjaCalhISRPYjt_tQLfj4NFt3zuuKh1zTqBC3XBH43wV1bF8geYNrs2Q035fEufXhlMwS2yFJmiy-TFpqbf7w-aQeoG590ROyhJrA998ExTJV4Q3OIZIZlw3cybmMo1JM3h01eSSS40F_GM6nR5cArA96psYFmZd57SE6qYsUevURwLTQCAstQ13MWHdQWWpwQZvnmSxKR1FzznC30LO6tORPniYh1y3Z7lHig-0IoIsbLVrV7-8khR5HnZ7eh4_yY-c3PvXyLE0SOHrx_gUc45iYZZbYAarVI_z9y2_HfUcnHfWv3Uq1v_gxZdrpg0TiyumsDRSbf5v3vTK6eDAG2KWGmattMkrUqfWg9Yo-81rYpYHMTuMCrUmC4RZ7OEWcDgPmM1mcBFTAfwIh0P0Jb2Arx9b3H9M323ft7mKHpfuseUfJBNpkkEy3r5_eiqMggGfmvscDbhGUnTmsx_85xn8BaLhHGbu04mjUiEx-Ly0avjqbMvGTlgo09ooJhb7ik8cdRHi7EbJimkMs9JfYL-eclzAT29--dnDvuRou8hAZN7txO46Te6VChxp4gmSgw9COJlNjba3hv3eNq7NpRTGSfWmdEm02XDMa0IpEzZ_kmn-ncIKpvm_vldY9SA9_Z1UFJUlv6jXoCVnFFZEpZPJh3riNyel5FI9GZ9E-C-hrLHhnvyzXh-jJOX9Qtkuaen2UjjZyMZ4KRfHpJSN0tLpWUvX0Xt0hNKXKxTmZ6YNClRpUnJW3idZt4aAO9bdWecKteQrTH0kpONxXhJTLlNUygp81i5z9pglx9ztepo4fTu54KkSO7aESIM5YRypaztxanzXSY123Tz8VGgaJYLNR5oSCt0odFOb65tHkyk2zlY4l3q21X_lfuVMXzFdS420VeeCDo4mzuV2KpT7cBX4EG4x6cGQ3ZBtlDyRLnWUKY62nQkHnZK3Gm1n17gb4cBIqBWuGD6E2VBnrWlAZ2AHWjsB7wjypCPNB19FlL2S2pyC6S6hYJrExliFciEp9hPxopV-LVpS1yjo5ZJxmjqJ8TDmXeTjRp9wEmWryE2BPqhBma452Vg1ForR5AiZ3XuDVc2JwUvJm8oJTBTWSExq43QyZyaDiomKrNMnT6b1OoOLuRqPj0KS2lehXfXpksW290t3mrxeyocwbifZ4Sox7pv6MaTn-h5eSQV2WPZQbor-DCSnU5ziHi5e-QxUO_24KUa37O1Mlp8N7Lp5Hzkat8adsBsO0CA1pq1DkbEp3i4y6eO-AkTlK9SVwWvk_gYZk7r7TO4anuWJ7oI3nGx8NxnmKbnU5I7brmpfMLoVNK5ehwJK6jov_U1X244Sbr1p6wUhmnx3d7_OHbWAVvDuqHGNZWPfN_bBHOSPP6pA_Bpxjvx2yA8p4FLgbPkDTxvnqOESYzOsQJw0Z-sx-EJyjiYDOTakVCfnPk2v_pPL-Zq1k_SoapGIT9ItfsM5W6lDioHjH9CrN1v5puVfJ2EWzyJpPN3YceMrT5Uz_dwYUi47Y4Y3SC-Rc2tN6qkzSCrC4gl6f4_osISHxxeb6x1vzmj_8nHwX3h-tMKu7S3XVjDnsKL3DJZBSQwupLLPT2_to-61HUrnpMSdI5ND3TsB3CksXwi1XS2-EOhgCfhC2EfS-kuiDyXnufhegrs22ABTqI1USHOzRJF2UmBPtU_FkCy9PNw_Kvkf21vhGxGu3dN_eKIIz_pPR9u_AeCczDB-GQAA "Open lightweight Notebook v7 view in a new tab")

### File Dialogs[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#file-dialogs "Link to this heading")

Two helper functions to ask a user to open a file or a folder are available in the [`filebrowser`](https://jupyterlab.readthedocs.io/en/stable/api/modules/filebrowser.html)
 package under the namespace [`FileDialog`](https://jupyterlab.readthedocs.io/en/stable/api/modules/filebrowser.FileDialog.html)
.

Here is an example to request a file.

const dialog \= FileDialog.getOpenFiles({
  manager, // IDocumentManager
  filter: model \=> model.type \== 'notebook' // optional (model: Contents.IModel) => boolean
});

const result \= await dialog;

if (result.button.accept) {
  let files \= result.value;
}

Copy to clipboard

And for a folder.

const dialog \= FileDialog.getExistingDirectory({
  manager // IDocumentManager
});

const result \= await dialog;

if (result.button.accept) {
  let folders \= result.value;
}

Copy to clipboard

Note

The document manager can be obtained in a plugin by requesting [`IDefaultFileBrowser`](https://jupyterlab.readthedocs.io/en/stable/api/variables/filebrowser.IDefaultFileBrowser-1.html)
 token. The `manager` will be accessed through `defaultBrowser.model.manager`.

Notifications[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#notifications "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

JupyterLab has a notifications manager that can add, update or dismiss notifications. That feature is provided by the `@jupyterlab/apputils` package.

Warning

It is a good practice to limit the number of notifications sent to respect the user’s focus. Therefore by default, the notification won’t be displayed to the user. But the status bar will indicate that a new notification arrived. So the user can click on the indicator to see all notifications.

Try adding a button `Do not show me again` for recurrent notifications to allow users to quickly filter notifications that matters for them.

A notification is described by the following element:

{
  /\*\*
   \* Notification message
   \*
   \* ### Notes
   \* Message can only be plain text with a maximum length of 140 characters.
   \*/
  message: string;
  /\*\*
   \* Notification type
   \*/
  type?:  'info' | 'in-progress' | 'success' | 'warning' | 'error' | 'default';
  /\*\*
   \* Notification options
   \*/
  options?: {
    /\*\*
     \* Autoclosing behavior - false (not closing automatically)
     \* or number (time in milliseconds before hiding the notification)
     \*
     \* Set to zero if you want the notification to be retained in the notification
     \* center but not displayed as toast. This is the default behavior.
     \*/
    autoClose?: number | false;
    /\*\*
     \* List of associated actions
     \*/
    actions?: Array<IAction\>;
    /\*\*
     \* Data associated with a notification
     \*/
    data?: T;
  };
}

Copy to clipboard

At creation, a notification will receive an unique identifier.

Actions can be linked to a notification but the interface depends on how the notification is handled.

There are two ways of interacting with notifications: through an API or through commands. The only difference is that actions linked to a notification can have an arbitrary callback when using the API. But only a command can be set as an action when using the command call for creating a notification.

### Using the API[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#using-the-api "Link to this heading")

To create notification, you need to provide a message and you can use the following helpers to set the type automatically (or use `notify` to set the type manually):

/\*\*
 \* Helper function to emit an error notification.
 \*/
Notification.error(message: string, options?: IOptions): string;

/\*\*
 \* Helper function to emit an info notification.
 \*/
Notification.info(message: string, options?: IOptions): string;

/\*\*
 \* Helper function to emit a success notification.
 \*/
Notification.success(message: string, options?: IOptions): string;

/\*\*
 \* Helper function to emit a warning notification.
 \*/
Notification.warning(message: string, options?: IOptions): string;

/\*\*
 \* Helper function to emit a in-progress notification. Then
 \* it will update it with a error or success notification
 \* depending on the promise resolution.
 \*/
Notification.promise(
  promise: Promise,
  {
    pending: { message: string, options?: IOptions },
    /\*\*
     \* If not set \`options.data\` will be set to the promise result.
     \*/
    success: { message: (result, data) \=> string, options?: IOptions },
    /\*\*
     \* If not set \`options.data\` will be set to the promise rejection error.
     \*/
    error: { message: (reason, data) \=> string, options?: IOptions }
  }
): string;

/\*\*
 \* Helper function to emit a notification.
 \*/
Notification.emit(
  message: string,
  type: 'info' | 'in-progress' | 'success' | 'warning' | 'error' | 'default' \= 'default',
  options?: IOptions
): string;

Copy to clipboard

When using the API, an action is defined by:

{
  /\*\*
   \* The action label.
   \*
   \* This should be a short description.
   \*/
  label: string;
  /\*\*
   \* Callback function to trigger
   \*
   \* ### Notes
   \* By default execution of the callback will close the toast
   \* and dismiss the notification. You can prevent this by calling
   \* \`event.preventDefault()\` in the callback.
   \*/
  callback: (event: MouseEvent) \=> void;
  /\*\*
   \* The action caption.
   \*
   \* This can be a longer description of the action.
   \*/
  caption?: string;
  /\*\*
   \* The action display type.
   \*
   \* This will be used to modify the action button style.
   \*/
  displayType?: 'default' | 'accent' | 'warn' | 'link';
}

Copy to clipboard

You can update a notification using:

Notification.update({
  id: string;
  message: string;
  type?:  'info' | 'in-progress' | 'success' | 'warning' | 'error' | 'default';
  autoClose?: number | false;
  actions?: Array<IAction\>;
  data?: ReadonlyJsonValue;
}): boolean;

Copy to clipboard

Note

Once updated the notification will be moved at the begin of the notification stack.

And you can dismiss a notification (if you provide an `id`) or all notifications using:

Notification.dismiss(id?: string): void;

Copy to clipboard

Note

Dismissing a notification will remove it from the list of notifications without knowing if the user has seen it or not. Therefore it is recommended to not dismiss a notification.

### Using commands[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html#using-commands "Link to this heading")

There are three commands available.

`'apputils:notify'` to create a notification:

commands.execute('apputils:notify', {
   message: string;
   type?: 'info' | 'in-progress' | 'success' | 'warning' | 'error' | 'default';
   options?: {
     autoClose?: number | false;
     actions?: Array<IAction\>;
     data?: T;
   };
});

Copy to clipboard

The result is the notification unique identifier.

An action is defined by:

{
  /\*\*
   \* The action label.
   \*
   \* This should be a short description.
   \*/
  label: string;
  /\*\*
   \* Callback command id to trigger
   \*/
  commandId: string;
  /\*\*
   \* Command arguments
   \*/
  args?: ReadonlyJsonObject;
  /\*\*
   \* The action caption.
   \*
   \* This can be a longer description of the action.
   \*/
  caption?: string;
  /\*\*
   \* The action display type.
   \*
   \* This will be used to modify the action button style.
   \*/
  displayType?: 'default' | 'accent' | 'warn' | 'link';
}

Copy to clipboard

`'apputils:update-notification'` to update a notification:

commands.execute('apputils:update-notification', {
  id: string;
  message: string;
  type?: 'info' | 'in-progress' | 'success' | 'warning' | 'error' | 'default';
  autoClose?: number | false;
  actions?: Array<IAction\>;
  data?: T;
});

Copy to clipboard

The result is a boolean indicating if the update was successful. In particular, updating an absent notification will fail.

`'apputils:dismiss-notification'` to dismiss a notification:

commands.execute('apputils:dismiss-notification', {
  id: string;
});

Copy to clipboard

Note

Dismissing a notification will remove it from the list of notifications without knowing if the user has seen it or not. Therefore it is recommended to not dismiss a notification.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/ui_helpers.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/ui_helpers.md.txt)