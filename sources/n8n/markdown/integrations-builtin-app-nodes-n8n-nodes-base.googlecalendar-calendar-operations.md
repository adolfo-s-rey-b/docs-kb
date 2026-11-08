For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md)
.

Use this operation to check availability in a calendar in Google Calendar. Refer to [Google Calendar](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar)
 for more information on the Google Calendar node itself.

Availability[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations#availability)

----------------------------------------------------------------------------------------------------------------------------------

Use this operation to check if a time-slot is available in a calendar.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Google Calendar credentials](https://docs.n8n.io/integrations/builtin/credentials/google)
    .
    
*   **Resource**: Select **Calendar**.
    
*   **Operation**: Select **Availability**.
    
*   **Calendar**: Choose a calendar you want to check against. Select **From list** to choose the title from the dropdown list or **By ID** to enter a calendar ID.
    
*   **Start Time**: The start time for the time-slot you want to check. By default, uses an expression evaluating to the current time (`{{ $now }}`).
    
*   **End Time**: The end time for the time-slot you want to check. By default, uses an expression evaluating to an hour from now (`{{ $now.plus(1, 'hour') }}`).
    

### Options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations#options)

*   **Output Format**: Select the format for the availability information:
    
    *   **Availability**: Returns if there are already events overlapping with the given time slot or not.
        
    *   **Booked Slots**: Returns the booked slots.
        
    *   **RAW**: Returns the RAW data from the API.
        
    
*   **Timezone**: The timezone used in the response. By default, uses the n8n timezone.
    

Refer to the [Freebusy: query | Google Calendar](https://developers.google.com/calendar/api/v3/reference/freebusy/query)
 API documentation for more information.

[PreviousGoogle Calendar](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar)
[NextEvent operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations)

Last updated 10 days ago

Was this helpful?