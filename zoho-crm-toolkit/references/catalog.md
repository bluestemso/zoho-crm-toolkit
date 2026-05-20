# Zoho CRM Endpoint Catalog

## Available Apis

### Available Apis

- `getavailableapis`: List available REST APIs
  Returns the list of available REST API endpoints, grouped by module and feature, that the current user can access in this tenant.
  `GET /__apis`
  Scopes: ZohoCRM.apis.READ

## Appointment Preference

### Appointment Preference

- `getappointmentpreference`: Retrieve Appointment Preferences
  Fetches the existing configuration for appointment preferences, including rules for deal creation, job sheet visibility, and mark as complete configurations.
  `GET /settings/appointment_preferences`
  Scopes: ZohoCRM.org.READ
- `updateappointmentpreference`: Update Appointment Preferences
  Updates one appointment preferences in Zoho CRM. This endpoint allows configuring how appointments are handled, including deal creation.
  `PUT /settings/appointment_preferences`
  Scopes: ZohoCRM.org.UPDATE

## Appointments API

### Appointments API

- `deleteid`: DELETE /Appointments__s/id
  appointment module record delete by id
  `DELETE /Appointments__s/{appointmentId}`
  Scopes: ZohoCRM.modules.appointments.DELETE
- `deleteappointmentss`: DELETE /Appointments__s/{ids}
  appointment module record delete
  `DELETE /Appointments__s`
  Scopes: ZohoCRM.modules.appointments.DELETE
- `getappointmentss`: GET /Appointments__s
  appointment records get
  `GET /Appointments__s`
  Scopes: ZohoCRM.modules.appointments.READ
- `getappointmentbyid`: GET /Appointments__s/{appointmentId}
  appointment mode record get by id
  `GET /Appointments__s/{appointmentId}`
  Scopes: ZohoCRM.modules.appointments.READ
- `postappointmentss`: POST /Appointments__s
  appointment module records creation
  `POST /Appointments__s`
  Scopes: ZohoCRM.modules.appointments.CREATE
- `putappointmentss`: PUT /Appointments__s
  appointment module records update
  `PUT /Appointments__s`
  Scopes: ZohoCRM.modules.appointments.UPDATE
- `updateappointmentbyid`: PUT /Appointments__s/{id}
  appointment module records update by appointment id
  `PUT /Appointments__s/{appointmentId}`
  Scopes: ZohoCRM.modules.appointments.UPDATE

## Assignment rules

### Assignment rules

- `getassignmentrules`: GET /settings/automation/assignment_rules
  To get all assignment rules
  `GET /settings/automation/assignment_rules`
  Scopes: ZohoCRM.settings.assignment_rules.READ
- `getassignmentrulebyid`: GET /settings/automation/assignment_rules/1234567890
  To get details of given assignment rule
  `GET /settings/automation/assignment_rules/{id}`
  Scopes: ZohoCRM.settings.assignment_rules.READ

## Zoho CRM Associate Email API

### Zoho CRM Associate Email API

- `associateemail`: Associate Email
  Associates emails to a specific record in a module.
  `POST /{module}/{recordId}/actions/associate_email`
  Scopes: ZohoCRM.modules.emails.CREATE

## Attachments

### Attachments

- `deleteattachment`: Delete Link Attachment
  Delete a link attachment associated with a specific record in a module.
  `DELETE /{moduleApiName}/{recordId}/Attachments/{id}`
  Scopes: ZohoCRM.modules.attachments.DELETE, ZohoCRM.modules.attachments.ALL
- `getattachmentbyid`: Download a specific attachment file
  Download the file content of a specific attachment by its ID. This endpoint returns the actual file (image, PDF, document, etc.). For link attachments, an error is returned as they cannot be downloaded.
  `GET /{moduleApiName}/{recordId}/Attachments/{id}`
  Scopes: ZohoCRM.modules.attachments.READ
- `getattachments`: Retrieve all attachments associated with a specific record
  Retrieve all attachments associated with a specific record.
  `GET /{moduleApiName}/{recordId}/Attachments`
  Scopes: ZohoCRM.modules.attachments.READ, ZohoCRM.modules.attachments.ALL
- `uploadattachment`: Upload an attachment
  Upload an attachment by providing either a file or a valid URL. Maximum request body size: 100MB.
  `POST /{moduleApiName}/{recordId}/Attachments`
  Scopes: ZohoCRM.modules.attachments.CREATE, ZohoCRM.modules.attachments.ALL

## Audit Log Export

### Audit Log Export

- `createauditlogexport`: Create an Audit Log Export job
  Creates a new export job for audit logs based on the specified criteria.
  `POST /settings/audit_log_export`
  Scopes: ZohoCRM.settings.audit_logs.CREATE
- `getauditlogexports`: Get Exported AuditLogs
  Retrieves a list of audit log export jobs along with their details.
  `GET /settings/audit_log_export`
  Scopes: ZohoCRM.settings.audit_logs.READ
- `getauditlogexportsbyid`: Get Exported AuditLogs
  Retrieves the details of a specific audit log export job by its ID.
  `GET /settings/audit_log_export/{id}`
  Scopes: ZohoCRM.settings.audit_logs.READ

## Bulk Read

### Bulk Read

- `createbulkreadjob`: Createbulkreadjob
  Createbulkreadjob
  `POST /read`
  Scopes: ZohoCRM.bulk.READ, ZohoCRM.modules.ALL
- `downloadresult`: Downloadresult
  Downloadresult
  `GET /read/{jobId}/result`
  Scopes: ZohoCRM.bulk.READ, ZohoCRM.modules.ALL
- `getbulkreadjobdetails`: Getbulkreadjobdetails
  Getbulkreadjobdetails
  `GET /read/{jobId}`
  Scopes: ZohoCRM.bulk.READ, ZohoCRM.modules.ALL

## Bulk Write

### Bulk Write

- `createbulkwritejob`: Create Bulk Write Job
  Creates a new bulk write job to insert or update records in bulk
  `POST /write`
  Scopes: ZohoCRM.bulk.CREATE
- `getjobdetails`: Get Bulk Write Job Details
  To upload a CSV file in ZIP format for bulk write API. The response contains the file_id. Use this ID while making the bulk write request.
  `GET /write/{jobId}`
  Scopes: ZohoCRM.bulk.CREATE

## Business Hours

### Business Hours

- `createbusinesshours`: Create business hours configuration
  Creates a new business hours configuration specifying working days, hours, and timezone for the organization.
  `POST /settings/business_hours`
  Scopes: ZohoCRM.settings.business_hours.CREATE
- `getbusinesshours`: Retrieve business hours configuration
  Retrieves the current business hours configuration including working days, hours, and timezone.
  `GET /settings/business_hours`
  Scopes: ZohoCRM.settings.business_hours.READ
- `updatebusinesshours`: Update business hours configuration
  Updates the existing business hours configuration with new working days, hours, or timezone settings.
  `PUT /settings/business_hours`
  Scopes: ZohoCRM.settings.business_hours.UPDATE

## Cadences

### Cadences

- `getcadences`: GET - Get all cadences
  Get all cadences
  `GET /settings/automation/cadences`
  Scopes: ZohoCRM.settings.cadences.READ

## Cadence Execution

### Cadence Execution

- `postenrolincadences`: Enroll records into cadences
  API to enroll records into manual cadence
  `POST /{module}/actions/enrol_in_cadences`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `postunenrolfromcadences`: Unenroll records from cadences
  Un-Enroll records from the cadences
  `POST /{module}/actions/unenrol_from_cadences`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE

## Call Preferences

### Call Preferences

- `getcallpreferences`: To get the Call preferences of the user
  This will return the user preferred Call preference details that is used to display the from number / to number field in CRM
  `GET /settings/call_preferences`
  Scopes: ZohoCRM.settings.modules.read
- `updatecallpreferences`: Updating Call preference
  This will update the user's Call preference
  `PUT /settings/call_preferences`
  Scopes: ZohoCRM.settings.modules.update

## Cancel Meetings

### Cancel Meetings

- `cancelmeetings`: Cancel Meeting
  To post the cancelMeeting mail
  `POST /Events/{event}/actions/cancel`
  Scopes: ZohoCRM.Modules.Events.update

## Change Owner

### Change Owner

- `singleupdate`: Change owner for a single record
  Updates the owner of a specific record in the module
  `POST /{module}/{record}/actions/change_owner`
  Scopes: ZohoCRM.change_owner.CREATE
- `bulkchangeowner`: Change owner for multiple records
  Updates the owner of multiple records in the module
  `POST /{module}/actions/change_owner`
  Scopes: ZohoCRM.change_owner.CREATE

## Composite Requests

### Composite Requests

- `composite`: To process multiple requests in a single API call
  This API allows clients to bundle multiple API requests into a single HTTP request
  `POST /__composite_requests`
  Scopes: ZohoCRM.composite_requests.CUSTOM

## Contact Roles

### Contact Roles

- `createroles`: Create Contact Roles
  Creates one or more contact roles.
  `POST /contacts/roles`
  Scopes: ZohoCRM.modules.contacts.WRITE
- `deleteroles`: Delete Contact Roles
  Deletes one or more contact roles by their IDs.
  `DELETE /contacts/roles`
  Scopes: ZohoCRM.modules.contacts.DELETE
- `deleterole`: Delete Role
  Deletes a specific contact role by ID.
  `DELETE /contacts/roles/{role}`
  Scopes: ZohoCRM.modules.contacts.DELETE
- `getcontactroles`: Get Contact Roles
  Retrieves a list of contact roles
  `GET /contacts/roles`
  Scopes: ZohoCRM.modules.contacts.READ
- `getrole`: Get Role
  Retrieves a specific contact role by its ID
  `GET /contacts/roles/{role}`
  Scopes: ZohoCRM.modules.contacts.READ
- `updateroles`: Update Contact Roles
  Updates one or more contact roles.
  `PUT /contacts/roles`
  Scopes: ZohoCRM.modules.contacts.UPDATE
- `updaterole`: Update Role
  Updates a specific contact role by its ID.
  `PUT /contacts/roles/{role}`
  Scopes: ZohoCRM.modules.contacts.UPDATE

## Zoho CRM Lead Conversion Options API

### Zoho CRM Lead Conversion Options API

- `getleadconversionoptions`: Get Lead Conversion Options
  Retrieves available conversion options for a lead including matching contacts, accounts, field mappings, and layout preferences. This endpoint helps determine what conversion paths are available before performing the actual lead conversion.
  `GET /Leads/{leadId}/__conversion_options`
  Scopes: ZohoCRM.modules.leads.READ

## Zoho CRM Lead Conversion API

### Zoho CRM Lead Conversion API

- `convertlead`: Convert a Lead
  Converts a Lead record into Contact, Account, and/or Deal records. Allows configuration of conversion behavior including overwrite settings, notifications, owner assignment, and tag carryover.
  `POST /Leads/{leadId}/actions/convert`
  Scopes: ZohoCRM.modules.leads.CREATE

## Coql

### Coql

- `executecoqlquery`: Execute COQL query
  Executes a COQL select query to fetch records data.
  `POST /coql`
  Scopes: ZohoCRM.modules.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Leads.READ

## Currencies

### Currencies

- `createcurrencies`: Create currencies
  Creates one or more new currencies for the organization.
  `POST /org/currencies`
  Scopes: ZohoCRM.settings.currencies.CREATE
- `enablecurrency`: Enable multi-currency
  Enable multi-currency for the organization and set the base currency.
  `POST /org/currencies/actions/enable`
  Scopes: ZohoCRM.settings.currencies.CREATE
- `getcurrencybyid`: Get currency by ID
  Retrieves details of a specific currency via its unique currency ID.
  `GET /org/currencies/{currency}`
  Scopes: ZohoCRM.settings.currencies.READ
- `getcurrencies`: List currencies
  Retrieves all added currencies in the organization.
  `GET /org/currencies`
  Scopes: ZohoCRM.settings.currencies.READ
- `updatebasecurrency`: Update base currency
  Update existing base currency details.
  `PUT /org/currencies/actions/enable`
  Scopes: ZohoCRM.settings.currencies.UPDATE
- `updatecurrencies`: Update currencies
  Updates one or more currencies other than the base currency.
  `PUT /org/currencies`
  Scopes: ZohoCRM.settings.currencies.UPDATE
- `updatecurrencybyid`: Update currency by ID
  Update a specific currency by its unique ID.
  `PUT /org/currencies/{currency}`
  Scopes: ZohoCRM.settings.currencies.UPDATE

## Custom Views

### Custom Views

- `changesort`: Change Sort Order
  Change the sort order of a custom view
  `PUT /settings/custom_views/actions/change_sort`
  Scopes: ZohoCRM.settings.custom_views.UPDATE
- `changesortbyid`: Change Sort Order
  Change the sort order of a custom view
  `PUT /settings/custom_views/{id}/actions/change_sort`
  Scopes: ZohoCRM.settings.custom_views.UPDATE
- `getcustomviews`: Get All Custom Views
  Get all custom views of a module
  `GET /settings/custom_views`
  Scopes: ZohoCRM.settings.custom_views.READ
- `getcustomviewbyid`: Get Custom View By Id
  Get a specific custom view of a module using custom view ID
  `GET /settings/custom_views/{id}`
  Scopes: ZohoCRM.settings.custom_views.READ

## Data Sharing

### Data Sharing

- `getdatasharing`: Get Data Sharing
  Get the data sharing settings configured.API exposed to customers
  `GET /settings/data_sharing`
  Scopes: ZohoCRM.settings.data_sharing.READ, ZohoCRM.settings.data_sharing.ALL
- `updatedatasharing`: Update Data Sharing
  Update the data sharing settings configured.API exposed to customers
  `PUT /settings/data_sharing`
  Scopes: ZohoCRM.settings.data_sharing.UPDATE, ZohoCRM.settings.data_sharing.ALL

## Deal Contact Roles

### Deal Contact Roles

- `upsertcontactrolerelations`: Add Or Update Contact Role Relations
  Add contact roles to a deal or update existing contact role relations in bulk
  `PUT /{module}/{dealId}/Contact_Roles`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW
- `associatecontactroletodeal`: Associate Contact Role To Deal
  Assign or update a contact role for a specific contact on a deal.
  `PUT /{module}/{dealId}/Contact_Roles/{contactId}`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW
- `deletecontactrolerelation`: Delete Contact Role Relation
  Remove a specific contact-deal relation using the contact identifier in the path.
  `DELETE /{module}/{dealId}/Contact_Roles/{contactId}`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW
- `deletecontactrolerelations`: Delete Contact Role Relations
  Remove one or more contact role associations from a deal using their relation IDs
  `DELETE /{module}/{dealId}/Contact_Roles`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW
- `getassociatedcontactroles`: Get Associated Contact Roles
  Retrieve contact roles associated with a deal
  `GET /{module}/{dealId}/Contact_Roles`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW
- `getdealcontactroleforcontact`: Get Contact Role For Contact
  Retrieve the contact role relation for a specific contact associated with a deal.
  `GET /{module}/{dealId}/Contact_Roles/{contactId}`
  Scopes: ZohoCRM.modules.CONTACTS.VIEW, ZohoCRM.modules.DEALS.VIEW

## Deal Link Emails

### Deal Link Emails

- `getrecordactionssingle`: Link Email to Record
  Links an email to a specified record in CRM.
  `POST /Contacts/{contactId}/Emails/{messageId}/actions/link_record`
  Scopes: ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE
- `linkemailstodeals`: Link Emails to Deals
  Links the emails to the specified deals in CRM.
  `POST /Contacts/{contactId}/Emails/actions/link_record`
  Scopes: ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE, ZohoCRM.modules.contacts.CREATE
- `getrecordactions2single`: Unlink Email from Record
  Unlinks an email from a specified record in CRM.
  `DELETE /Contacts/{contactId}/Emails/{messageId}/actions/link_record`
  Scopes: ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE
- `getrecordactions`: Unlink Emails from Records
  Unlinks the emails from the specified records in CRM.
  `DELETE /Contacts/{contactId}/Emails/actions/link_record`
  Scopes: ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE

## Download Email Attachments

### Download Email Attachments

- `downloademailattachments`: Get Download Attachments Details
  Fetches the binary content of an email attachment for a specific record.
  `GET /{module}/{recordId}/Emails/actions/download_attachments`
  Scopes: ZohoCRM.modules.emails.READ, ZohoCRM.modules.leads.READ

## Download Inline Images

### Download Inline Images

- `getdownloadinlineimages`: Download inline images embedded in an email related to a record
  Download inline images embedded in an email related to a record.
  `GET /{module}/{recordId}/Emails/actions/download_inline_images`
  Scopes: ZohoCRM.modules.emails.READ, ZohoCRM.modules.leads.all, ZohoCRM.modules.contacts.all

## Duplicate Check Preference

### Duplicate Check Preference

- `createduplicatecheckpreference`: Create Duplicate Check Preference
  Create Duplicate Check Preference
  `POST /settings/duplicate_check_preference`
  Scopes: ZohoCRM.settings.duplicate_check_preference.CREATE
- `deleteduplicatecheckpreference`: Delete Duplicate Check Preference
  Delete the duplicate check preference for a module in Zoho CRM.
  `DELETE /settings/duplicate_check_preference`
  Scopes: ZohoCRM.settings.duplicate_check_preference.DELETE
- `getduplicatecheckpreference`: Get Duplicate Check Preference
  Get Duplicate Check Preference
  `GET /settings/duplicate_check_preference`
  Scopes: ZohoCRM.settings.duplicate_check_preference.READ
- `updateduplicatecheckpreference`: Update Duplicate Check Preference
  Update Duplicate Check Preference API is used to update duplicate check settings for a specific module in the CRM system. It allows users to define how duplicate records are identified and managed based on field mappings between the current module and a mapped module, such as Contacts. This API helps maintain data integrity by preventing the creation of duplicate records during data entry or import processes.
  `PUT /settings/duplicate_check_preference`
  Scopes: ZohoCRM.settings.duplicate_check_preference.UPDATE

## Email Drafts

### Email Drafts

- `createemaildrafts`: Create email drafts for a record
  Creates one or more email drafts associated with the specified record in the given module.
  `POST /{module}/{record}/__email_drafts`
  Scopes: ZohoCRM.modules.leads.CREATE, ZohoCRM.modules.accounts.CREATE, ZohoCRM.modules.contacts.CREATE
- `deleteemaildrafts`: Delete an email draft
  Deletes the specified email draft for the given record.
  `DELETE /{module}/{record}/__email_drafts/{draft}`
  Scopes: ZohoCRM.modules.leads.DELETE, ZohoCRM.modules.accounts.DELETE, ZohoCRM.modules.contacts.DELETE
- `getemaildraft`: Get email draft
  Retrieves the specified email draft for the given record in the module.
  `GET /{module}/{record}/__email_drafts/{draft}`
  Scopes: ZohoCRM.modules.leads.READ, ZohoCRM.modules.accounts.READ, ZohoCRM.modules.contacts.READ
- `getemaildrafts`: Get email drafts for a record
  Retrieves the list of email drafts associated with the specified record in the given module.
  `GET /{module}/{record}/__email_drafts`
  Scopes: ZohoCRM.modules.leads.READ, ZohoCRM.modules.accounts.READ, ZohoCRM.modules.contacts.READ
- `updateemaildrafts`: Update email draft
  Updates the specified email draft for the given record in the module.
  `PUT /{module}/{record}/__email_drafts/{draft}`
  Scopes: ZohoCRM.modules.leads.UPDATE, ZohoCRM.modules.accounts.UPDATE, ZohoCRM.modules.contacts.UPDATE

## Email Templates

### Email Templates

- `gettemplates`: Retrieve email templates list
  Fetches a paginated list of email templates with support for filtering, sorting, and pagination. Use page/per_page for pagination (default per_page=20, max=100), sort_by and sort_order for sorting, and filters parameter for advanced filtering.
  `GET /settings/email_templates`
  Scopes: ZohoCRM.templates.email.READ

## Get Email Shared Details

### Get Email Shared Details

- `getemailsharingdetail`: Get Email Shared Details
  To get the details of the users and the type with whom you can share the record's emails.
  `GET /{moduleApiName}/{id}/__emails_sharing_details`
  Scopes: ZohoCRM.modules.ALL, ZohoCRM.modules.emails.READ

## Features

### Features

- `getfeaturedetails`: Get Feature Details
  To get the available feature details for the current edition
  `GET /__features`
  Scopes: ZohoCRM.features.READ
- `getfeaturesepcificdetails`: Get Specific Feature Details
  To get the available feature specific details for the current edition
  `GET /__features/{feature}`
  Scopes: ZohoCRM.features.READ

## Fetch Full Data

### Fetch Full Data

- `fetchfulldataforsinglerecord`: Fetch full data for a single record
  Fetches the full content of rich text fields for a specific record. If the 'fields' parameter is not provided, all rich text fields in the module will be fetched.
  `GET /{moduleApiName}/{id}/actions/fetch_full_data`
  Scopes: ZohoCRM.modules.READ
- `fetchfulldataformultiplerecords`: Fetch full data for multiple records
  Fetches the full content of rich text fields for multiple records. The 'fields' parameter is mandatory and supports a maximum of 8 rich text fields.
  `GET /{moduleApiName}/actions/fetch_full_data`
  Scopes: ZohoCRM.modules.READ

## Field Updates

### Field Updates

- `postfieldupdates`: To create a field update action
  To create a field update action in the Automation module. This action modifies field values when triggered by workflows, blueprints, or approval processes.
  `POST /settings/automation/field_updates`
  Scopes: ZohoCRM.settings.automation_actions.CREATE
- `deletefieldupdatebyid`: To delete a fieldupdate action
  To delete a field update action.
  `DELETE /settings/automation/field_updates/{id}`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `deletefieldupdates`: To delete multiple field update actions
  To delete multiple field update actions configured
  `DELETE /settings/automation/field_updates`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `getfieldupdatebyid`: To retrieve a field update action by fieldUpdate ID
  Retrieves the details of the field-update action for the specified fieldUpdate ID.
  `GET /settings/automation/field_updates/{id}`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `getfieldupdates`: To retrieve all field updates
  Retrieve all available field updates
  `GET /settings/automation/field_updates`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `putfieldupdatebyid`: To update an existing field update action
  To update an existing field update action.
  `PUT /settings/automation/field_updates/{id}`
  Scopes: ZohoCRM.settings.automation_actions.UPDATE

## Fields API

### Fields API

- `postfields`: Create Fields
  To create custom fields in a module in your Zoho CRM account.
  `POST /settings/fields`
  Scopes: ZohoCRM.settings.fields.CREATE
- `deletecustomfield`: Delete Custom Field
  Delete a custom field from a module. Field must not be used in workflows, approvals, scoring rules, or other configurations. Only one field can be deleted per request.
  `DELETE /settings/fields/{fieldId}`
  Scopes: ZohoCRM.settings.fields.DELETE
- `getfieldswithid`: Get Field by ID
  Retrieve metadata of a specific custom field in a module using the field ID.
  `GET /settings/fields/{fieldId}`
  Scopes: ZohoCRM.settings.fields.READ
- `getfields`: Get Fields
  Retrieve all fields metadata for modules. Examples and schemas derived from provided sample and schema files.
  `GET /settings/fields`
  Scopes: ZohoCRM.settings.fields.READ
- `putfieldswithid`: Update Field by ID
  Update a Custom Field with related to specific module of Zoho CRM Account
  `PATCH /settings/fields/{fieldId}`
  Scopes: ZohoCRM.settings.fields.UPDATE
- `patchfields`: Update Fields
  To update custom fields in your Zoho CRM account.
  `PATCH /settings/fields`
  Scopes: ZohoCRM.settings.fields.UPDATE

## Files

### Files

- `getfile`: Retrieves a file from ZFS
  Retrieves the binary content of a file stored in Zoho File System (ZFS) using its unique file ID. The file ID is provided as a required query parameter 'id'. If the file exists, the API returns the file's binary data along with appropriate headers indicating the MIME type and content disposition for download. If the file ID does not correspond to any file in ZFS, a 204 No Content response is returned. This endpoint is used to download files that have been previously uploaded to ZFS and associated with Zoho CRM records.
  `GET /files`
  Scopes: ZohoCRM.files.READ
- `uploadfiles`: Uploads a file to ZFS
  Uploads a file to Zoho File System (ZFS) and returns the file metadata including the file ID which can be used to associate the file with records in Zoho CRM. The file is uploaded using multipart/form-data with a required 'file' field containing the binary data of the file to be uploaded. The response includes the file ID, name, status, and other details. Can upload 10 files in a single request by repeating the 'file' field. Maximum file size is 20 MB.
  `POST /files`
  Scopes: ZohoCRM.files.CREATE

## Find And Merge

### Find And Merge

- `getmergejobstatus`: Get Merge Job Status
  Retrieves the status of merge jobs for finding and tracking record merge operations in Zoho CRM modules.
  `GET /{module}/{masterRecordId}/actions/merge`
  Scopes: ZohoCRM.modules.read
- `mergerecords`: Merge Records
  Merges duplicate records in Zoho CRM modules with field mapping and validation. Supports synchronous and asynchronous merge operations.
  `POST /{module}/{masterRecordId}/actions/merge`
  Scopes: ZohoCRM.modules.CREATE

## Fiscal Year

### Fiscal Year

- `getfiscalyear`: GET /settings/fiscal_year
  API DOC : https://learn.zoho.in/portal/zohocorp/manual/v3-apis-1/article/custom-fiscal-year-support
  `GET /settings/fiscal_year`
  Scopes: ZohoCRM.settings.fiscal_year.READ
- `updatefiscalyear`: PUT /settings/fiscal_year
  Only Admins can update Fiscal YearAPI DOC : https://learn.zoho.in/portal/zohocorp/manual/v3-apis-1/article/custom-fiscal-year-support
  `PUT /settings/fiscal_year`
  Scopes: ZohoCRM.settings.fiscal_year.UPDATE

## From Addresses

### From Addresses

- `getaddresses`: Get From Addresses
  Get the list of email addresses that you can send emails from.
  `GET /settings/emails/actions/from_addresses`
  Scopes: ZohoCRM.settings.emails.READ

## Related Records Count

### Related Records Count

- `getrelatedrecordscount`: Get Related Records Count
  Retrieves the count of related records for a specific parent record. Supports filtering by various criteria including approval status, conversion status, and custom field filters. This operation is useful for analytics and UI display purposes where you need to show counts without fetching the actual related records.
  `POST /{moduleApiName}/{recordId}/actions/get_related_records_count`
  Scopes: ZohoCRM.modules.READ

## Global Picklists

### Global Picklists

- `createglobalpicklist`: Create a new global picklist
  Creates a new global picklist with the specified display label, API name, description, and picklist values. The actual_label, customizable, modified_by, created_by, and presence properties are generated by the backend. In pick_list_values, only display_value and type are considered.
  `POST /settings/global_picklists`
  Scopes: ZohoCRM.settings.global_picklist.CREATE
- `deleteglobalpicklist`: Delete a global picklist by id
  Deletes a single global picklist identified by the path parameter \{id\}. This request is asynchronous: a 202 Accepted indicates deletion has been scheduled and the response contains a job_id in details. There is no status-check endpoint. A 400 Bad Request is returned for invalid id, deletion already scheduled, conversion in progress, association limits, or system-defined restrictions. When an error refers to a position in a multi-resource request/path, details.resource_path_index is provided.
  `DELETE /settings/global_picklists/{id}`
  Scopes: ZohoCRM.settings.global_picklist.DELETE
- `getsingleglobalpicklists`: Get a single global picklist by id
  Fetches the global picklist for given id along with their pick_list_values. used_in_modules, and associated_fields_count can be included in the response based on the 'include' query parameter. A 204 is returned when no global picklists exist.
  `GET /settings/global_picklists/{id}`
  Scopes: ZohoCRM.settings.global_picklist.READ
- `getbulkglobalpicklists`: Get all global picklists
  Fetches the list of global picklists available in the organization along with their details. pick_list_values, used_in_modules, and associated_fields_count can be included in the response based on the 'include' query parameter. A 204 is returned when no global picklists exist.
  `GET /settings/global_picklists`
  Scopes: ZohoCRM.settings.global_picklist.READ
- `getpicklistvaluesassociations`: Get picklist value associations
  To the list of features like blueprints, workflows create, workflow convert, workflow task, ABM, etc in which a particular picklist value is used.
  `GET /settings/global_picklists/{id}/actions/pick_list_values_associations`
  Scopes: ZohoCRM.settings.global_picklist.ALL
- `getreplacedvalues`: Get picklist values which is in replace scheduler
  Retrieves picklist values that are currently being replaced through a replace scheduler for the given global picklist ID.
  `GET /settings/global_picklists/{id}/actions/replaced_values`
  Scopes: ZohoCRM.settings.global_picklist.READ
- `replacepicklistvalues`: Replace picklist values for a global picklist
  Schedules or executes replacement of picklist values for the specified global picklist. You can specify either `id`, `display_value`, or both for `old_value` and `new_value`. If both are provided, the system validates them for consistency. The `from` (old) value can be non-existent in the current picklist, but the `to` (new) value must be in the **used** state of the picklist option.
  `POST /settings/global_picklists/{id}/actions/replace_picklist_values`
  Scopes: ZohoCRM.settings.global_picklist.ALL
- `getglobalpicklistfieldassociations`: To get the fields associated with a global picklist
  Retrieves associations of picklist values with modules, fields, and layouts for a given global picklist ID.
  `GET /settings/global_picklists/{id}/actions/associations`
  Scopes: ZohoCRM.settings.global_picklist.READ
- `updateglobalpicklistbyid`: Update a global picklist by id
  Updates an existing global picklist identified by the path parameter \{id\}. You can update display_label, api_name, description, pick_list_values_sorted_lexically, and pick_list_values. Backend-generated properties (actual_label, customizable, modified_by, created_by, presence) cannot be updated. For pick_list_values, you can add new values, update existing values (using id), move values between used/unused (one at a time), or delete values (one at a time using _delete: true). Bulk operations for moving to unused or deletion are not allowed.
  `PATCH /settings/global_picklists/{id}`
  Scopes: ZohoCRM.settings.global_picklist.UPDATE

## Zoho CRM Holidays API

### Holidays

- `createholidays`: Create holidays
  Creates one or more holidays with specified names, dates, types, and associated shift hours. Each holiday must have a unique name and date combination. Business holidays apply to all users, while shift holidays require a valid shift_hour association.
  `POST /settings/holidays`
  Scopes: ZohoCRM.settings.business_hours.CREATE
- `deleteholiday`: Delete a specific holiday
  Permanently deletes a specific holiday identified by its ID. This operation is irreversible. Ensure the holiday ID is valid before deletion to avoid errors.
  `DELETE /settings/holidays/{holidayId}`
  Scopes: ZohoCRM.settings.business_hours.DELETE
- `getholiday`: Retrieve a specific holiday
  Retrieves complete details of a specific holiday by its unique identifier, including its name, date, type, associated shift hour (if applicable), and year.
  `GET /settings/holidays/{holidayId}`
  Scopes: ZohoCRM.settings.business_hours.READ
- `getholidays`: Retrieve holidays
  Retrieves a list of holidays filtered by year, type (business or shift), and shift ID. Business holidays apply organization-wide, while shift holidays are specific to configured shifts. Returns paginated results with metadata.
  `GET /settings/holidays`
  Scopes: ZohoCRM.settings.business_hours.READ
- `updateholiday`: Update a specific holiday
  Updates a specific holiday identified by its ID. You can modify the holiday's name (max 80 characters, no special characters: #, %, ^, &, *) or date (must be within current or next financial year). Provide only the fields you want to update.
  `PUT /settings/holidays/{holidayId}`
  Scopes: ZohoCRM.settings.business_hours.UPDATE
- `updateholidays`: Update holidays (bulk)
  Updates one or more existing holidays by their IDs with new names, dates, or shift hour associations.
  `PUT /settings/holidays`
  Scopes: ZohoCRM.settings.business_hours.UPDATE

## Inventory Convert

### Inventory Convert

- `convertinventory`: Convert an inventory record
  Converts the record into another inventory module type depending on the parent module:Quotes -> Sales Orders, Invoices :Sales Orders -> Invoices.
  `POST /{moduleApiName}/{id}/actions/convert`
  Scopes: ZohoCRM.modules.Quotes.CREATE, ZohoCRM.modules.SalesOrders.CREATE

## Inventory Templates

### Inventory Templates

- `gettemplates-2`: Retrieve inventory templates list
  Retrieve a paginated list of inventory templates with support for sorting, filtering, and category selection. Use page/per_page for pagination (default: 20 per page, max: 200). Supports sorting by any field and filtering via JSON-stringified filter expressions.
  `GET /settings/inventory_templates`
  Scopes: ZohoCRM.templates.inventory.READ

## Layouts API

### Layouts API

- `deletelayout`: Delete a custom layout
  Deletes a custom layout from a module in Zoho CRM. When deleting a layout that has associated records, you must specify a `transfer_to` layout ID to transfer those records. If the layout has an associated pipeline, you must also provide `pipeline` and `stage` parameters. The `transfer_to` parameter is only optional when the layout is deactivated and has no records associated with it. Note: The standard layout cannot be deleted.
  `DELETE /settings/layouts/{id}`
  Scopes: ZohoCRM.settings.layouts.DELETE
- `getlayoutbyid`: Get a specific layout metadata by ID
  Retrieves comprehensive details of a specific layout by its unique identifier for a specified module in your Zoho CRM account. Returns layout configuration including sections, fields, profiles, and permissions.

**Important Notes:**
- The `profiles` array will be `null` if the user does not have "Module Customization" permission in their profile.
- For Deals module: When the pipeline feature is enabled, multiple layouts exist per pipeline. Each pipeline can have its own set of layouts.
- The `mode` parameter supports different values based on module type. Common modes include `business_card` and `quick_create`.
- Score and Visit Summary sections are system-generated and read-only.

**Prerequisite:** The Layout ID can be obtained from the Get All Layouts API.
  `GET /settings/layouts/{id}`
  Scopes: ZohoCRM.settings.layouts.READ
- `getlayouts`: Get all layouts metadata for a module
  Retrieves comprehensive details of all layouts associated with a specified module in your Zoho CRM account. Returns layout configuration including sections, fields, profiles, and permissions in a single response without pagination.

**Important Notes:**
- The `profiles` array will be `null` if the user does not have "Module Customization" permission in their profile.
- For Deals module: When the pipeline feature is enabled, multiple layouts exist per pipeline. Each pipeline can have its own set of layouts.
- The `mode` parameter supports different values based on module type. Common modes include `business_card` and `quick_create`.
- Score and Visit Summary sections are system-generated and read-only.
- All layouts for the module are returned in a single response; pagination is not supported.
  `GET /settings/layouts`
  Scopes: ZohoCRM.settings.layouts.READ

### Layouts

- `updatelayout`: Update a Layout
  Update a custom layout in Zoho CRM. You can rename the layout, add/remove profile permissions, enable/disable business card, create/update/delete sections, and add/update/delete/move fields within sections. Limits: Maximum 5 sections per request and maximum 5 fields total across all sections per request.
  `PATCH /settings/layouts/{id}`
  Scopes: ZohoCRM.settings.layouts.UPDATE

## Layout Activate and Deactivate API

### Layout Activate and Deactivate API

- `layoutactivate`: Activate layout with profile associations
  Activates a single deactivated layout, making it available for use within the specified module. Optionally allows adding or removing profile associations during activation. Only one layout can be activated per request. This operation is idempotent - attempting to activate an already active layout returns an error (ALREADY_ACTIVATED).
  `POST /settings/layouts/{id}/actions/activate`
  Scopes: ZohoCRM.settings.layouts.CREATE
- `layoutdeactivate`: Deactivate layout with configuration transfer
  Deactivates an active layout and transfers its configuration (profile associations, permissions, field mappings) to another active layout within the same module. At least one active layout must remain in the module. This operation is idempotent - attempting to deactivate an already deactivated layout returns an error (ALREADY_DEACTIVATED).
  `DELETE /settings/layouts/{id}/actions/activate`
  Scopes: ZohoCRM.settings.layouts.DELETE

## Locking Information

### Locking Information

- `removelockfromlockedrecord`: Remove Lock from Locked Records
  Use the Remove Lock from Locked Records API to remove locks from locked records in different modules.
  `DELETE /{moduleName}/{recordId}/Locking_Information__s/{lockId}`
  Scopes: ZohoCRM.settings.modules.DELETE
- `lockrecord`: To lock a record of a module
  Use the Lock Record API to lock records in different modules.
  `POST /{moduleName}/{recordId}/Locking_Information__s`
  Scopes: ZohoCRM.settings.modules.CREATE
- `getrecordlockinginformationoftherecord`: To retrieve the locking information details of locked records
  Use the Get Record Locking Information API to retrieve the locking information details of locked records in different modules.
  `GET /{moduleName}/{recordId}/Locking_Information__s`
  Scopes: ZohoCRM.settings.modules.READ
- `updatereasonoflockedrecord`: To update the locking reason of a locked record
  Use the Update Record Locking Infromation API to modify locking information of locked records in different modules.
  `PUT /{moduleName}/{recordId}/Locking_Information__s/{lockId}`
  Scopes: ZohoCRM.settings.modules.ALL

## Mail Merge

### Mail Merge

- `postdownloadmailmerge`: POST /{module_API_name}/{recordId}/actions/download_mail_merge
  Use the download mail merge API to download the merged document created using your mail merge template.
  `POST /{moduleApiName}/{recordId}/actions/download_mail_merge`
  Scopes: ZohoCRM.settings.mailmerge.CREATE,ZohoWriter.documentEditor.ALL,ZohoWriter.merge.ALL
- `postsendmailmerge`: POST /{module_API_name}/{recordId}/actions/send_mail_merge
  Send mail merge API to use a mail merge template and send emails to users. You can also attach files either as inline images or separate attachments with the email through the API.
  `POST /{moduleApiName}/{recordId}/actions/send_mail_merge`
  Scopes: ZohoCRM.settings.mailmerge.CREATE,ZohoWriter.documentEditor.ALL,ZohoWriter.merge.ALL,ZohoCRM.settings.emails.ALL
- `postsignmailmerge`: POST /{module_API_name}/{recordId}/actions/sign_mail_merge
  To send a mail merge document for signing and approval.To use this API, you must initially access&nbsp;the Merge and Sign dialogue&nbsp;from the Writer UI once. Please note that you need to do this only once.
  `POST /{moduleApiName}/{recordId}/actions/sign_mail_merge`
  Scopes: ZohoCRM.settings.mailmerge.CREATE,ZohoWriter.documentEditor.ALL,ZohoWriter.merge.ALL,ZohoSign.documents.ALL

## Map Dependency

### Map Dependency

- `createmapdependency`: Create a new field dependency for a layout
  Creates a new field dependency mapping between parent and child fields in a specific layout. The dependency defines how child field values are controlled based on parent field selections.
  `POST /settings/layouts/{layoutId}/map_dependency`
  Scopes: ZohoCRM.settings.map_dependency.create
- `deletemapdependency`: Delete a field dependency
  Deletes an existing field dependency from a specific layout. This operation permanently removes the dependency mapping between parent and child fields.
  `DELETE /settings/layouts/{layoutId}/map_dependency/{dependencyId}`
  Scopes: ZohoCRM.settings.map_dependency.delete
- `getmapdependencybyid`: Retrieve a specific field dependency by ID
  Retrieves detailed information about a specific field dependency including parent and child field relationships with picklist value mappings.
  `GET /settings/layouts/{layoutId}/map_dependency/{dependencyId}`
  Scopes: ZohoCRM.settings.map_dependency.read
- `getmapdependency`: Retrieve field dependencies for a layout
  Retrieves the list of field dependencies for a specific layout in a module. The response includes parent and child field relationships and its additional metadata.
  `GET /settings/layouts/{layoutId}/map_dependency`
  Scopes: ZohoCRM.settings.map_dependency.read
- `updatemapdependency`: Update an existing field dependency
  Updates the picklist value mappings for an existing field dependency. Use "_delete": null to remove specific mappings.
  `PUT /settings/layouts/{layoutId}/map_dependency/{dependencyId}`
  Scopes: ZohoCRM.settings.map_dependency.update

## Mass Change Owner

### Mass Change Owner

- `checkstatus`: Check mass change owner job status
  Check the status of a mass change owner job using the job ID
  `GET /{module}/actions/mass_change_owner`
  Scopes: ZohoCRM.change_owner.READ
- `masschangeowner`: Mass change owner of records
  Mass change the owner of records in a module based on a custom view
  `POST /{module}/actions/mass_change_owner`
  Scopes: ZohoCRM.change_owner.CREATE

## Mass Convert

### Mass Convert

- `getjobstatus`: Get mass convert job status
  Retrieve the status and counts of a previously scheduled mass convert job using job_id query parameter.
  `GET /Leads/actions/mass_convert`
  Scopes: ZohoCRM.mass_convert.leads.READ
- `massconvert`: Mass convert leads
  Start a scheduled mass-convert job that converts multiple leads into other modules (Deals/Contacts/Accounts) according to provided options. Max 50 lead IDs per request.
  `POST /Leads/actions/mass_convert`
  Scopes: ZohoCRM.mass_convert.leads.CREATE

## Mass Delete Api

### Mass Delete Api

- `massdelete`: Mass delete with record ids and custom view id
  Mass delete records with record ids or custom view id
  `POST /{module}/actions/mass_delete`
  Scopes: ZohoCRM.mass_delete.DELETE
- `getmassdeletejobstatus`: Retrieve mass delete job status
  Get the status and results of a previously scheduled mass delete operation by job ID.
  `GET /{module}/actions/mass_delete`
  Scopes: ZohoCRM.mass_delete.READ

## Mass Delete Tags

### Mass Delete Tags

- `getstatus`: Get status of mass delete job
  Retrieve the status of a scheduled mass delete job using its job_id
  `GET /settings/tags/actions/mass_delete`
  Scopes: ZohoCRM.settings.tags.READ
- `createmassdeletetags`: Schedule mass delete tags job
  Schedules a job to delete multiple tags across modules in Zoho CRM.
  `POST /settings/tags/actions/mass_delete`
  Scopes: ZohoCRM.settings.tags.DELETE

## Mass Update API

### Mass Update API

- `idsupdate`: Mass Update API
  Enables users to update a specific field value across multiple records within a CRM module.
  `POST /{module}/actions/mass_update`
  Scopes: ZohoCRM.mass_update.UPDATE, ZohoCRM.mass_update.Leads.UPDATE
- `getmassupdatestatus`: Retrieve the status of a mass update job
  Retrieves the current status and progress metrics of an asynchronous mass update job initiated via POST /crm/v8/\{module\}/actions/mass_update. Returns record counts and current job state.
  `GET /{module}/actions/mass_update`
  Scopes: ZohoCRM.mass_update.READ, ZohoCRM.mass_update.Leads.READ

## Search Records

### Search

- `searchrecords`: Search Records by Criteria, Word, Email, or Phone
  Searches records matching your criteria within a CRM module. Supports criteria queries, email/phone/word searches. At least one search parameter required. Max 2,000 records, 15 criteria conditions. Newly created records may have indexing delays.
  `GET /{module}/search`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoSearch.securesearch.READ, ZohoCRM.modules.Contacts.READ

## Modules

### Modules

- `createmodules`: Create a custom CRM module
  Creates a single custom module in the CRM. Requires the Crm_Implied_Customize_Zoho_CRM permission. This operation is not idempotent; submitting the same api_name multiple times will result in validation errors. Only one module can be created per request; batch creation is not supported.
  `POST /settings/modules`
  Scopes: ZohoCRM.settings.modules.CREATE
- `getmodulebyapiname`: Get module metadata by API name
  Retrieves complete metadata for a specific CRM module identified by its API name. Returns comprehensive configuration including fields, layouts, profiles, related lists, custom views, and module capabilities.
  `GET /settings/modules/{moduleIdentifier}`
  Scopes: ZohoCRM.settings.modules.READ
- `getmodules`: Retrieve CRM module metadata
  Fetches metadata for CRM modules including configuration, capabilities, and structural information. Supports filtering by feature name to retrieve modules associated with specific features, or by status (e.g., `system_hidden`) to return modules matching that status. When both `status` and `feature_name` are provided, modules must satisfy both criteria (AND logic). Expected latency: ~60ms.
  `GET /settings/modules`
  Scopes: ZohoCRM.settings.modules.READ
- `updatemodules`: Update CRM modules
  Updates existing modules in the CRM. Allows modification of module labels and profile assignments. This operation is idempotent; the same request can be safely repeated. Supports batch updates - multiple modules can be updated in a single request. Returns 200 when all modules update successfully, or 207 Multi-Status when some succeed and others fail.
  `PUT /settings/modules`
  Scopes: ZohoCRM.settings.modules.UPDATE
- `updatemodulebyapiname`: Update module labels and profiles
  Partially updates a module's display labels (singular and plural) and associated profile permissions. This operation only modifies the specified fields without affecting other module configuration. The operation is idempotent - calling it multiple times with the same payload produces the same result.
  `PUT /settings/modules/{moduleIdentifier}`
  Scopes: ZohoCRM.settings.modules.UPDATE

## Notes

### Notes

- `createnotesmodule`: Create Notes
  Creates one or more note records.
  `POST /Notes`
  Scopes: ZohoCRM.modules.notes.CREATE
- `deletenotesmodule`: Delete Notes
  Permanently deletes one or more notes using comma-separated note IDs.
  `DELETE /Notes`
  Scopes: ZohoCRM.modules.notes.DELETE
- `deletenotebyid`: Delete a Specific Note
  Permanently deletes a specific note by its ID.
  `DELETE /Notes/{id}`
  Scopes: ZohoCRM.modules.notes.DELETE
- `getnotesmodule`: Get Notes
  Retrieves a list of notes.
  `GET /Notes`
  Scopes: ZohoCRM.modules.notes.READ
- `getnotebyid`: Get a Specific Note
  Retrieves details of a specific note by its ID.
  `GET /Notes/{id}`
  Scopes: ZohoCRM.modules.notes.READ
- `updatenotesmodule`: Update Notes
  Updates one or more existing note records. Either note content or note title must be provided (at least one is mandatory) for each note.
  `PUT /Notes`
  Scopes: ZohoCRM.modules.notes.UPDATE
- `updatenotebyid`: Update a Specific Note
  Updates a specific note by its ID. Either note content or note title must be provided (at least one is mandatory).
  `PUT /Notes/{id}`
  Scopes: ZohoCRM.modules.notes.UPDATE

## Notifications

### Notifications

- `createnotifications`: Create notification channels
  Create one or more notification channels.
  `POST /actions/watch`
  Scopes: ZohoCRM.notifications.CREATE, ZohoCRM.notifications.ALL
- `disablenotifications`: Disable notification channels
  Disable one or more notification channels identified by the channel_ids query parameter.
  `DELETE /actions/watch`
  Scopes: ZohoCRM.notifications.DELETE, ZohoCRM.notifications.ALL
- `getnotifications`: List active notification channels
  Get a list of all active notification channels for the user.
  `GET /actions/watch`
  Scopes: ZohoCRM.notifications.READ
- `updatenotificationdetails`: Update full notification details
  Replace all details of an existing notification channel, overwriting its previous configuration.
  `PUT /actions/watch`
  Scopes: ZohoCRM.notifications.UPDATE, ZohoCRM.notifications.ALL
- `updatenotificationinfo`: Update specific notification information
  Partially update selected properties of a notification channel (URL, events, expiry, conditions, token).
  `PATCH /actions/watch`
  Scopes: ZohoCRM.notifications.UPDATE, ZohoCRM.notifications.ALL

## Org

### Org

- `getorganization`: Get Organization data
  To get the Company Details
  `GET /org`
  Scopes: ZohoCRM.org.READ

## Org Photo

### Org Photo

- `delete`: Delete Organization Photo
  Delete the organization photo
  `DELETE /org/photo`
  Scopes: ZohoCRM.org.DELETE
- `getorgphoto`: Get Org Photo
  Retrieve the organization photo
  `GET /org/photo`
  Scopes: ZohoCRM.org.READ
- `uploadorganizationphoto`: Upload Organization Photo
  Upload a photo for the organization
  `POST /org/photo`
  Scopes: ZohoCRM.org.CREATE

## Pick List Values

### Pick List Values

- `getpicklistvalues`: Retrieve pick list values for a field
  Returns the available pick list values for a specified field in a module, including display values (with translations if enabled), reference values, layout associations, and metadata. Returns 204 if the field exists but is not a pick list type. Does not support pagination.
  `GET /settings/fields/{fieldId}/pick_list_values`
  Scopes: ZohoCRM.settings.fields.READ

## Pipeline

### Pipeline

- `createpipeline`: Create Pipeline
  Create a new pipeline for a given layout
  `POST /settings/pipeline`
  Scopes: ZohoCRM.settings.pipeline.CREATE
- `getpipeline`: Get Pipeline
  Get particular pipeline by ID
  `GET /settings/pipeline/{id}`
  Scopes: ZohoCRM.settings.pipeline.READ
- `getpipelines`: Get Pipelines
  Get pipelines for a given layout
  `GET /settings/pipeline`
  Scopes: ZohoCRM.settings.pipeline.READ
- `transferanddeletepipelines`: Transfer and Delete Pipelines
  Transfer and delete pipelines
  `POST /settings/pipeline/actions/transfer`
  Scopes: ZohoCRM.settings.pipeline.CREATE
- `updateordeletepipelinepatch`: UpdateOrDelete Pipeline
  Update/Delete an pipeline
  `PATCH /settings/pipeline`
  Scopes: ZohoCRM.settings.pipeline.UPDATE
- `updateordeletepipelineput`: UpdateOrDelete Pipeline
  Update/Delete an pipeline
  `PUT /settings/pipeline`
  Scopes: ZohoCRM.settings.pipeline.UPDATE
- `updateordeletepipelinepatchurl`: UpdateOrDelete Pipeline
  Update/Delete an pipeline
  `PATCH /settings/pipeline/{id}`
  Scopes: ZohoCRM.settings.pipeline.UPDATE
- `updateordeletepipelineputurl`: UpdateOrDelete Pipeline
  Update/Delete an pipeline
  `PUT /settings/pipeline/{id}`
  Scopes: ZohoCRM.settings.pipeline.UPDATE

## Portal User Type

### Portal User Type

- `createportalusertype`: Create portal user type
  Create one or more portal user types for the specified portal. Request body must include a user_type array with one or more user type objects.
  `POST /settings/portals/{portal}/user_type`
  Scopes: ZohoCRM.settings.clientportal.CREATE
- `deleteportalusertype`: Delete portal user type
  Delete the specified portal user type.
  `DELETE /settings/portals/{portal}/user_type/{userTypeId}`
  Scopes: ZohoCRM.settings.clientportal.DELETE
- `getportalusertype`: Get portal user type
  Retrieve details for the specified portal user type.
  `GET /settings/portals/{portal}/user_type/{userTypeId}`
  Scopes: ZohoCRM.settings.clientportal.READ
- `getportalusertypes`: List portal user types
  Retrieve all user types for the specified portal.
  `GET /settings/portals/{portal}/user_type`
  Scopes: ZohoCRM.settings.clientportal.READ
- `updateportalusertype`: Update portal user type
  Update the specified portal user type. Request body must include user_type array with items containing the fields to update.
  `PUT /settings/portals/{portal}/user_type/{userTypeId}`
  Scopes: ZohoCRM.settings.clientportal.UPDATE

## Portal Users

### Portal Users

- `changeportalusersstatus`: Change status of portal users
  Changing portal users status.
  `POST /settings/portals/{portal}/user_type/{userType}/users/{recordId}/actions/change_status`
  Scopes: ZohoCRM.settings.clientportal.UPDATE
- `changeportalusersstatusbulk`: Change status of portal users in bulk
  Changing portal users status in bulk.
  `POST /settings/portals/{portal}/user_type/{userType}/users/actions/change_status`
  Scopes: ZohoCRM.settings.clientportal.UPDATE
- `inviteusers`: Invite portal users
  Send invitations to portal users for a specific module.
  `POST /{module}/actions/portal_invite`
  Scopes: ZohoCRM.settings.clientportal.CREATE
- `getscheduledinviteusersinfo`: Invite portal users
  Send invitations to portal users for a specific module.
  `GET /{module}/actions/portal_invite`
  Scopes: ZohoCRM.settings.clientportal.READ
- `singleinviteuser`: Invite portal users
  Send invitations to portal users for a specific module.
  `POST /{module}/{recordId}/actions/portal_invite`
  Scopes: ZohoCRM.settings.clientportal.CREATE
- `getportalusers`: List portal users
  Retrieve users of a specific portal filtered by user type.
  `GET /settings/portals/{portal}/user_type/{userType}/users`
  Scopes: ZohoCRM.settings.clientportal.READ
- `transferportalusers`: Transfer portal users from one user group to another
  Transferring portal user from one user group to another user group within the same portal.
  `POST /settings/portals/{portal}/user_type/{userType}/users/action/transfer`
  Scopes: ZohoCRM.settings.clientportal.UPDATE
- `deleteportalusers`: delete portal users
  Retrieve users of a specific portal filtered by user type.
  `DELETE /settings/portals/{portal}/user_type/{userType}/users`
  Scopes: ZohoCRM.settings.clientportal.DELETE

## Portals

### Portals

- `createportal`: Create portals
  Create portals for the organization to provide access for end customer.
  `POST /settings/portals`
  Scopes: ZohoCRM.settings.clientportal.CREATE
- `deleteportal`: Delete portal
  Delete portal settings for the specified portal identifier.
  `DELETE /settings/portals/{portal}`
  Scopes: ZohoCRM.settings.clientportal.DELETE
- `getportal`: Get portal details
  Retrieve details for a specific portal by its identifier.
  `GET /settings/portals/{portal}`
  Scopes: ZohoCRM.settings.clientportal.READ
- `getportals`: Get portals
  Retrieve a details of portals data.
  `GET /settings/portals`
  Scopes: ZohoCRM.settings.clientportal.READ
- `updateportal`: Update portal
  Update portal settings for the specified portal identifier.
  `PUT /settings/portals/{portal}`
  Scopes: ZohoCRM.settings.clientportal.UPDATE

## Profiles API

### Profiles API

- `cloneprofile`: Clone a CRM profile
  Creates a clone of the specified profile.

**Scopes:**
* ZohoCRM.settings.profiles.all
* ZohoCRM.settings.profiles.read
  `POST /settings/profiles/{id}/actions/clone`
  Scopes: ZohoCRM.settings.profiles.CREATE
- `deleteprofile`: Delete a CRM profile
  Deletes an existing CRM profile by ID.

**Scopes:**
* ZohoCRM.settings.profiles.all
* ZohoCRM.settings.profiles.delete
  `DELETE /settings/profiles/{id}`
  Scopes: ZohoCRM.settings.profiles.DELETE
- `getprofile`: Get a CRM profile
  Retrieves the details of a specific CRM profile by ID.

**Scopes:**
* ZohoCRM.settings.profiles.all
* ZohoCRM.settings.profiles.read
  `GET /settings/profiles/{id}`
  Scopes: ZohoCRM.settings.profiles.READ
- `getprofiles`: List CRM profiles
  Retrieves the list of CRM profiles with metadata.

**Scopes:**
* ZohoCRM.settings.profiles.all
* ZohoCRM.settings.profiles.read
  `GET /settings/profiles`
  Scopes: ZohoCRM.settings.profiles.READ
- `updateprofile`: Update a CRM profile
  Updates an existing CRM profile by ID.

**Scopes:**
* ZohoCRM.settings.profiles.all
* ZohoCRM.settings.profiles.read
  `PUT /settings/profiles/{id}`
  Scopes: ZohoCRM.settings.profiles.UPDATE

## Records

### Records

- `createrecords`: Create a Record in a specific module
  Create a Record in a specific module
  `POST /{module}`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `deleterecord`: Delete a single record by ID
  Permanently deletes a specific record from the module using its unique record ID.
  `DELETE /{module}/{recordID}`
  Scopes: ZohoCRM.modules.Leads.DELETE, ZohoCRM.modules.Contacts.DELETE, ZohoCRM.modules.Accounts.DELETE
- `deleterecords`: Delete multiple records from a module
  Permanently deletes one or more records from the specified module using comma-separated record IDs. Returns per-item results for bulk operations.
  `DELETE /{module}`
  Scopes: ZohoCRM.modules.Leads.DELETE, ZohoCRM.modules.Contacts.DELETE, ZohoCRM.modules.Accounts.DELETE
- `getrecord`: Get Record for a specific module with RecordId
  To get the details of a specific record with its unique record ID.
  `GET /{module}/{recordID}`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ
- `getrecords`: Get Records for a specific module
  To get the list of available records from a module
  `GET /{module}`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ
- `getdeletedrecords`: Get deleted records from a module
  Retrieve the deleted records for the module. This endpoint can retrieve both permanently deleted records and temporarily deleted records from the recycle bin.
  `GET /{module}/deleted`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ
- `clonerecord`: To clone a record in a module
  To clone a record in a module.
  `POST /{module}/{recordID}/actions/clone`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `upsertrecords`: To insert a new or update an existing record based on duplicate check field
  The Upsert API allows you to insert a new record or update an existing one based on duplicate check field values.
  `POST /{module}/upsert`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `updaterecords`: To update existing entities or records in a specified module
  To update existing entities or records in a specified module.
  `PUT /{module}`
  Scopes: ZohoCRM.modules.Leads.UPDATE, ZohoCRM.modules.Contacts.UPDATE, ZohoCRM.modules.Accounts.UPDATE
- `updaterecord`: To update existing entities or records in a specified module with the recordID
  To update existing entities or records in a specified module with the recordID
  `PUT /{module}/{recordID}`
  Scopes: ZohoCRM.modules.Leads.UPDATE, ZohoCRM.modules.Contacts.UPDATE, ZohoCRM.modules.Accounts.UPDATE

## Module Record Count

### Records

- `getcount`: Get Record Count in a Module
  Fetches the total number of records in a specified module.
The count can be filtered using `cvid` (Custom View ID) or one of the search parameters (`criteria`, `phone`, `email`, `word`).

**Important Constraint (Zoho Documentation):**
You can only include **either** `cvid` **or** one of the search parameters (`criteria`, `phone`, `email`, `word`) in a single request. Combining `cvid` with any search parameter will result in an `AMBIGUITY_DURING_PROCESSING` error (HTTP 400).
  `GET /{moduleApiName}/actions/count`
  Scopes: ZohoCRM.modules.ALL, ZohoSearch.securesearch.READ, ZohoCRM.modules.Leads.READ

## Record Locking Configuration

### Record Locking Configuration

- `createrecordlockingconfiguration`: Create Record Locking Configuration
  To add record locking configuration for different modules.
  `POST /settings/record_locking_configurations`
  Scopes: ZohoCRM.settings.record_locking_configurations.CREATE
- `deleterecordlockingconfiguration`: Delete Record Locking Configuration
  To delete the record locking configuration for different modules.
  `DELETE /settings/record_locking_configurations`
  Scopes: ZohoCRM.settings.record_locking_configurations.DELETE
- `deleterecordlockingconfigurationpassingidinurl`: Delete Record Locking Configuration by ID
  To delete the record locking configuration for different modules,pass the configuration ID through the URL.
  `DELETE /settings/record_locking_configurations/{id}`
  Scopes: ZohoCRM.settings.record_locking_configurations.DELETE
- `getrecordlockingconfiguration`: Get Record Locking Configuration Details
  To retrieve the record locking configuration for different modules.
  `GET /settings/record_locking_configurations`
  Scopes: ZohoCRM.settings.record_locking_configurations.READ
- `getrecordlockingconfigurationpassingidinurl`: Get Record Locking Configuration by ID
  To retrieve the record locking configuration for different modules,pass the configuration ID through the URL
  `GET /settings/record_locking_configurations/{id}`
  Scopes: ZohoCRM.settings.record_locking_configurations.READ
- `updaterecordlockingconfiguration`: Update Record Locking Configuration
  To update the record locking configuration for different modules.
  `PUT /settings/record_locking_configurations`
  Scopes: ZohoCRM.settings.record_locking_configurations.UPDATE
- `updaterecordlockingconfigurationpassingidinurl`: Update Record Locking Configuration by ID
  To update the record locking configuration for different modules, pass the configuration ID through the URL
  `PUT /settings/record_locking_configurations/{id}`
  Scopes: ZohoCRM.settings.record_locking_configurations.UPDATE

## Record Photo

### Record Photo

- `deletephoto`: Delete a photo
  Delete a photo for a record
  `DELETE /{module}/{record}/photo`
  Scopes: ZohoCRM.modules.DELETE
- `getphoto`: Get a photo
  Retrieve a photo for a record
  `GET /{module}/{record}/photo`
  Scopes: ZohoCRM.modules.READ
- `uploadphoto`: Upload a photo
  Upload a photo for a record
  `POST /{module}/{record}/photo`
  Scopes: ZohoCRM.modules.CREATE

## Record Level Sharing Of Emails

### Record Level Sharing Of Emails

- `sharebulkemails`: Share Emails in Bulk
  To share emails of multiple records with other users in your organization
  `POST /{moduleApiName}/actions/share_emails`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `shareemails`: Share Emails of a record
  To share emails of specific record with other users in your organization
  `POST /{moduleApiName}/{id}/actions/share_emails`
  Scopes: ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE
- `unsharebulkemails`: Unshare Emails in Bulk
  To unshare emails of multiple records with other users in your organization
  `POST /{moduleApiName}/actions/unshare_emails`
  Scopes: ZohoCRM.modules.Leads.DELETE, ZohoCRM.modules.Contacts.DELETE, ZohoCRM.modules.Accounts.DELETE
- `unshareemails`: Unshare Emails of a record
  To unshare emails of specific record with other users in your organization
  `POST /{moduleApiName}/{id}/actions/unshare_emails`
  Scopes: ZohoCRM.modules.Leads.DELETE, ZohoCRM.modules.Contacts.DELETE, ZohoCRM.modules.Accounts.DELETE

## Recycle Bin

### Recycle Bin

- `deleterecyclebinrecord`: Delete a recycle bin record
  Permanently deletes the recycle-bin record identified by `record_id`. This is irreversible.
  `DELETE /settings/recycle_bin/{recordId}`
  Scopes: ZohoCRM.settings.recycle_bin.DELETE
- `deleterecyclebinrecords`: Delete multiple recycle bin records
  Permanently deletes matching recycle-bin records. This is a destructive operation and may partially succeed for some items; check 207 responses for per-item results.
  `DELETE /settings/recycle_bin`
  Scopes: ZohoCRM.settings.recycle_bin.DELETE
- `emptyrecyclebin`: Empty the recycle bin
  Permanently deletes all records from the Recycle Bin. This action is irreversible, as deleted records cannot be restored after this operation. When the number of records in the Recycle Bin exceeds 1000 (including child records), the deletion will be scheduled as a background job (202 status). If the count is 1000 or fewer, the records are deleted immediately (200 status). Only users with the Admin profile can empty the Recycle Bin.
  `POST /settings/recycle_bin/actions/empty`
  Scopes: ZohoCRM.settings.recycle_bin.UPDATE
- `getrecyclebinrecord`: Get a recycle bin record
  Returns a single recycle-bin record identified by the path parameter `record_id`. The record_id in the URL takes precedence over any filters or ids given in query parameters.
  `GET /settings/recycle_bin/{recordId}`
  Scopes: ZohoCRM.settings.recycle_bin.READ
- `getrecyclebincounts`: Get recycle bin counts
  Returns the count of items in the recycle bin. Useful for monitoring or quick summaries.
  `GET /settings/recycle_bin/actions/count`
  Scopes: ZohoCRM.settings.recycle_bin.READ
- `getrecyclebinrecords`: List recycle bin records
  Returns paginated recycle-bin entries. Use filters or ids to scope results.
  `GET /settings/recycle_bin`
  Scopes: ZohoCRM.settings.recycle_bin.READ
- `restorerecyclebinrecord`: Restore a recycle bin record
  Restores a single recycle-bin record identified by the path parameter `record_id`.
  `POST /settings/recycle_bin/{recordId}/actions/restore`
  Scopes: ZohoCRM.settings.recycle_bin.UPDATE
- `restorerecyclebinrecords`: Restore multiple recycle bin records
  Restores multiple recycle-bin records based on provided criteria. You can specify records to restore using one of: `ids`, `filters`, or `restore_all_records`. Only one of these fields should be provided; supplying multiple will result in an error. When the number of records to restore (including child records) exceeds 1000, the operation is scheduled as a background job (202 status). For 1000 or fewer records, restoration happens immediately (200/207 status).
  `POST /settings/recycle_bin/actions/restore`
  Scopes: ZohoCRM.settings.recycle_bin.UPDATE

## Related Lists

### Related Lists

- `getrelatedlists`: Retrieve related lists configuration
  Get the configuration of related lists for a specific module and layout
  `GET /settings/related_lists`
  Scopes: ZohoCRM.settings.related_lists.READ

## Related Notes

### Related Notes

- `createnotes`: Create Notes for a Record
  Creates one or more notes associated with a specific parent record. Either note content or note title must be provided (at least one is mandatory).
  `POST /{parentRecordModule}/{parentRecordId}/Notes`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Contacts.READ
- `deletebulknotes`: Delete Note(s) for a Record
  Deletes one or more notes associated with a specific parent record using comma-separated note IDs in the query parameter.
  `DELETE /{parentRecordModule}/{parentRecordId}/Notes`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Contacts.READ
- `deletenotes`: Delete a Specific Note
  Deletes a specific note record associated with a parent record using the note ID in the path.
  `DELETE /{parentRecordModule}/{parentRecordId}/Notes/{noteId}`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Contacts.READ
- `getnotesbyid`: Get a Specific Note
  Retrieves details of a specific note record associated with a parent record in a CRM module.
  `GET /{parentRecordModule}/{parentRecordId}/Notes/{noteId}`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Contacts.READ
- `getnotes`: List Notes for a Record
  Retrieves a paginated list of notes associated with a specific parent record in a CRM module.
  `GET /{parentRecordModule}/{parentRecordId}/Notes`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Contacts.READ
- `updatebulknotes`: Update Multiple Notes for a Record
  Updates one or more notes associated with a specific parent record. Either note content or note title must be provided (at least one is mandatory) for each note.
  `PUT /{parentRecordModule}/{parentRecordId}/Notes`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Contacts.READ
- `updatenotes`: Update a Note
  Updates an existing note associated with a specific parent record. Either note content or note title must be provided (at least one is mandatory).
  `PUT /{parentRecordModule}/{parentRecordId}/Notes/{noteId}`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Contacts.READ

## Zoho CRM Related Records API

### Zoho CRM Related Records API

- `delinkspecificrelatedrecord`: Delink Specific Related Record
  Deletes the association between a parent record and a specific related record. This operation deletes only the relationship link, not the actual record itself.
  `DELETE /{parentRecordModule}/{parentRecord}/{relatedList}/{record}`
  Scopes: ZohoCRM.modules.DELETE
- `getrelatedrecord`: Get Specific Related Record
  Retrieves details of a specific record that is related to a parent record. Returns the record data along with pagination information if applicable.
  `GET /{parentRecordModule}/{parentRecord}/{relatedList}/{record}`
  Scopes: ZohoCRM.modules.READ
- `getdeletedrelatedrecord`: List Deleted Related Records
  Retrieves a list of records that were previously related to a parent record but have since been deleted. Useful for audit trails and data recovery scenarios.
  `GET /{parentRecordModule}/deleted/{parentRecord}/{relatedList}`
  Scopes: ZohoCRM.modules.READ
- `getrelatedrecords`: List Related Records
  Retrieves a paginated list of records from a specific related list of a parent record in a CRM module. Supports filtering by fields and conditional requests using If-Modified-Since header.
  `GET /{parentRecordModule}/{parentRecord}/{relatedList}`
  Scopes: ZohoCRM.modules.READ
- `delinkrelatedrecords`: Remove Related Records by IDs
  Removes relationships between a parent record and multiple records in a specified related list, identified by their IDs in the query parameter. This operation deletes only the relationship links, not the actual records themselves. The target records remain intact in their respective modules.
  `DELETE /{parentRecordModule}/{parentRecord}/{relatedList}`
  Scopes: ZohoCRM.modules.DELETE
- `updaterelatedrecords`: Update Related Records
  Updates multiple related records' specific properties in a specified related list.
  `PUT /{parentRecordModule}/{parentRecord}/{relatedList}`
  Scopes: ZohoCRM.modules.UPDATE
- `updatespecificrelatedrecord`: Update Specific Related Record
  Updates a specific related record's properties.
  `PUT /{parentRecordModule}/{parentRecord}/{relatedList}/{record}`
  Scopes: ZohoCRM.modules.UPDATE

## Roles

### Roles

- `createroles-2`: Create new roles
  Create one or more new CRM roles in the organization
  `POST /settings/roles`
  Scopes: ZohoCRM.settings.roles.CREATE
- `deleterole-2`: Delete role
  Delete an existing CRM role and transfer users to another role
  `DELETE /settings/roles/{role}`
  Scopes: ZohoCRM.settings.roles.DELETE
- `getroles`: Get all roles
  Retrieve a list of all CRM roles in the organization
  `GET /settings/roles`
  Scopes: ZohoCRM.settings.roles.READ
- `getrole-2`: Get specific role
  Retrieve details of a specific CRM role by its identifier
  `GET /settings/roles/{role}`
  Scopes: ZohoCRM.settings.roles.READ
- `updateroles-2`: Update multiple roles
  Update multiple CRM roles in the organization
  `PUT /settings/roles`
  Scopes: ZohoCRM.settings.roles.UPDATE
- `updaterole-2`: Update role
  Update an existing CRM role with new information
  `PUT /settings/roles/{role}`
  Scopes: ZohoCRM.settings.roles.UPDATE

## Scoring Rules

### Scoring Rules

- `deletescoringrules`: DELETE /settings/automation/scoring_rules
  To delete multiple scoring rules
  `DELETE /settings/automation/scoring_rules`
  Scopes: settings.scoring_rules.DELETE
- `deletescoringrulebyid`: DELETE /settings/automation/scoring_rules/{ruleId}
  To delete a single scoring rule
  `DELETE /settings/automation/scoring_rules/{ruleId}`
  Scopes: settings.scoring_rules.DELETE
- `deleteactivate`: DELETE /settings/automation/scoring_rules/{ruleId}/actions/activate
  To deactivate a scoring rule
  `DELETE /settings/automation/scoring_rules/{ruleId}/actions/activate`
  Scopes: settings.scoring_rules.DELETE
- `getscoringrules`: GET /settings/automation/scoring_rules
  Returns the list of scoring rules configured. If params are passed, rules matched the param value will be returned.
  `GET /settings/automation/scoring_rules`
  Scopes: settings.scoring_rules.READ
- `getscoringrulebyid`: GET /settings/automation/scoring_rules/{ruleId}
  Returns the scoring rule details
  `GET /settings/automation/scoring_rules/{ruleId}`
  Scopes: settings.scoring_rules.READ
- `postscoringrules`: POST /settings/automation/scoring_rules
  Configure scoring rules for a module and layout.
  `POST /settings/automation/scoring_rules`
  Scopes: settings.scoring_rules.CREATE
- `postclone`: POST /settings/automation/scoring_rules/{ruleId}/actions/clone
  To clone the scoring rule
  `POST /settings/automation/scoring_rules/{ruleId}/actions/clone`
  Scopes: settings.scoring_rules.CREATE
- `putscoringrules`: PUT /settings/automation/scoring_rules
  Update multiple scoring rules
  `PUT /settings/automation/scoring_rules`
  Scopes: settings.scoring_rules.UPDATE
- `putscoringrulebyid`: PUT /settings/automation/scoring_rules/{ruleId}
  To update a scoring rule name, description, field_rules, touch_point_rules or custom_fields.
  `PUT /settings/automation/scoring_rules/{ruleId}`
  Scopes: settings.scoring_rules.UPDATE
- `putactivate`: PUT /settings/automation/scoring_rules/{ruleId}/actions/activate
  To activate the scoring rule
  `PUT /settings/automation/scoring_rules/{ruleId}/actions/activate`
  Scopes: settings.scoring_rules.UPDATE

## Send Mail

### Send Mail

- `sendmail`: Send an email to a record
  Sends an email using specific templates or custom content to a record in a given module.
  `POST /{moduleName}/{id}/actions/send_mail`
  Scopes: ZohoCRM.send_mail.all.CREATE

## Service Preference

### Service Preference

- `getservicepreference`: Retrieve service preference settings for the organization
  Fetch service preference configuration for the organization.
  `GET /settings/service_preferences`
  Scopes: ZohoCRM.settings.modules.READ
- `updateservicepreference`: Update service preference settings for the organization
  Update the service preference configuration for the organization.
  `PUT /settings/service_preferences`
  Scopes: ZohoCRM.settings.modules.UPDATE

## Services API

### Services API

- `deleteservicess`: DELETE /services_s
  services records delete
  `DELETE /Services__s`
  Scopes: ZohoCRM.modules.services.DELETE
- `deleteservicebyid`: DELETE /services_s/{id}
  services record delete by id
  `DELETE /Services__s/{id}`
  Scopes: ZohoCRM.modules.services.DELETE
- `getservicess`: GET /services_s
  services records get
  `GET /Services__s`
  Scopes: ZohoCRM.modules.services.READ
- `getservicebyid`: GET /services_s/{id}
  services record get by id
  `GET /Services__s/{id}`
  Scopes: ZohoCRM.modules.services.READ
- `postservicess`: POST /services_s
  create services api
  `POST /Services__s`
  Scopes: ZohoCRM.modules.services.CREATE
- `putservicess`: PUT /services_s
  update services api
  `PUT /Services__s`
  Scopes: ZohoCRM.modules.services.UPDATE
- `putservicebyid`: PUT /services_s/{id}
  update services api
  `PUT /Services__s/{id}`
  Scopes: ZohoCRM.modules.services.UPDATE

## Share Records

### Share Records

- `createsharerecords`: Create Share Records
  Create Share Records. API exposed to customers
  `POST /{moduleApiName}/{recordId}/actions/share`
  Scopes: ZohoCRM.share.leads.CREATE, ZohoCRM.share.contacts.CREATE, ZohoCRM.share.accounts.CREATE
- `deletesharerecords`: Delete Share Records
  Delete Share Records. API exposed to customers
  `DELETE /{moduleApiName}/{recordId}/actions/share`
  Scopes: ZohoCRM.share.leads.DELETE, ZohoCRM.share.contacts.DELETE, ZohoCRM.share.accounts.DELETE
- `getsharerecords`: Get Share Records
  Get Share Records. API exposed to customers
  `GET /{moduleApiName}/{recordId}/actions/share`
  Scopes: ZohoCRM.share.leads.READ, ZohoCRM.share.contacts.READ, ZohoCRM.share.accounts.READ
- `updatesharerecords`: Update Share Records
  Update Share Records. API exposed to customers
  `PUT /{moduleApiName}/{recordId}/actions/share`
  Scopes: ZohoCRM.share.leads.UPDATE, ZohoCRM.share.contacts.UPDATE, ZohoCRM.share.accounts.UPDATE

## Shift Hours

### Shift Hours

- `createshifts`: Create new shifts
  Creates one or more new shift hour configurations with timing, break hours, and timezone settings.
  `POST /settings/business_hours/shift_hours`
  Scopes: ZohoCRM.settings.business_hours.CREATE
- `deletesingleshifthour`: Delete a specific shift hour
  Deletes a specific shift hour configuration. This operation cannot be undone.
  `DELETE /settings/business_hours/shift_hours/{shift}`
  Scopes: ZohoCRM.settings.business_hours.DELETE
- `getsingleshifthour`: Retrieve a specific shift hour
  Retrieves detailed information about a specific shift hour configuration including timing, breaks, users, and holidays.
  `GET /settings/business_hours/shift_hours/{shift}`
  Scopes: ZohoCRM.settings.business_hours.READ
- `getshifts`: Retrieve all shift hours
  Retrieves all configured shift hours including shift timing, break hours, users, and holidays for each shift.
  `GET /settings/business_hours/shift_hours`
  Scopes: ZohoCRM.settings.business_hours.READ
- `updatesingleshifthour`: Update a specific shift hour
  Updates a specific shift hour configuration with new timing, break hours, or timezone settings.
  `PUT /settings/business_hours/shift_hours/{shift}`
  Scopes: ZohoCRM.settings.business_hours.CREATE
- `updateshifthours`: Update multiple shift hours
  Updates one or more existing shift hour configurations with new timing, break hours, or timezone settings.
  `PUT /settings/business_hours/shift_hours`
  Scopes: ZohoCRM.settings.business_hours.UPDATE

## Tags CRUD API

### Tags CRUD API

- `deletetags`: DELETE /settings/tags/{id}
  This endpoint is used to delete Tags
  `DELETE /settings/tags/{id}`
  Scopes: ZohoCRM.settings.tags.DELETE
- `posttags`: POST /settings/tags
  This endpoint is used to create tags
  `POST /settings/tags`
  Scopes: ZohoCRM.settings.tags.CREATE
- `puttags`: PUT /settings/tags
  Put API with Tag id in request body
  `PUT /settings/tags`
  Scopes: ZohoCRM.settings.tags.UPDATE
- `puttagswithid`: PUT /settings/tags/{id}
  This endpoint is used to update the tag details
  `PUT /settings/tags/{id}`
  Scopes: ZohoCRM.settings.tags.UPDATE
- `gettags`: this endpoint is used to get tags from a module
  to get tags from a module
  `GET /settings/tags`
  Scopes: ZohoCRM.settings.tags.READ

## Tag Actions API

### Tag Actions API

- `getrecordscount`: GET /settings/tags/{id}/actions/records_count
  This endpoint is used to get the number of records associated to the tag.
  `GET /settings/tags/{id}/actions/records_count`
  Scopes: ZohoCRM.settings.tags.all
- `postmerge`: POST /settings/tags/{id}/actions/merge
  This endpoint is used to merge two tags
  `POST /settings/tags/{id}/actions/merge`
  Scopes: ZohoCRM.settings.tags.all
- `postaddtags`: POST /{module}/actions/add_tags
  This endpoint is used to associate tags to records
  `POST /{module}/actions/add_tags`
  Scopes: ZohoCRM.settings.tags.all
- `postremovetags`: POST /{module}/actions/remove_tags
  This endpoint is used to remove tags from records
  `POST /{module}/actions/remove_tags`
  Scopes: ZohoCRM.settings.tags.all
- `postaddtagswithid`: POST /{module}/{id}/actions/add_tags
  This endpoint is used to add tags to record
  `POST /{module}/{id}/actions/add_tags`
  Scopes: ZohoCRM.settings.tags.all
- `postremovetagswithid`: POST /{module}/{id}/actions/remove_tags
  This endpoint is used to dissociate tags from records
  `POST /{module}/{id}/actions/remove_tags`
  Scopes: ZohoCRM.settings.tags.all

## Territories

### Territories

- `asssignterritoriestorecord`: Asssign Territories To Record
  Auto-generated description for operation `Asssign Territories To Record`.
  `POST /{module}/{record}/actions/assign_territories`
  Scopes: ZohoCRM.modules.UPDATE
- `asssignterritoriestorecords`: Asssign Territories To Records
  Auto-generated description for operation `Asssign Territories To Records`.
  `POST /{module}/actions/assign_territories`
  Scopes: ZohoCRM.modules.UPDATE
- `createterritories`: Create Territories
  Auto-generated description for operation `Create Territories`.
  `POST /settings/territories`
  Scopes: ZohoCRM.settings.territories.CREATE
- `deleteterritories`: Delete Territories
  Auto-generated description for operation `Delete Territories`.
  `DELETE /settings/territories`
  Scopes: ZohoCRM.settings.territories.DELETE
- `deleteterritorybyid`: Delete Territory By Id
  Auto-generated description for operation `Update Territory`.
  `DELETE /settings/territories/{id}`
  Scopes: ZohoCRM.settings.territories.DELETE
- `getassociateduserscount`: Get Associated Users Count
  Auto-generated description for operation `Get Associated Users Count`.
  `GET /settings/territories/actions/associated_users_count`
  Scopes: ZohoCRM.settings.territories.READ
- `getchildterritoriesbyid`: Get Child Territories By Id
  Auto-generated description for operation `Get Child Territories By Id`.
  `GET /settings/territories/{id}/__child_territories`
  Scopes: ZohoCRM.settings.territories.READ
- `getterritory`: Get Territory
   `Get Territory By Id`
  `GET /settings/territories/{id}`
  Scopes: ZohoCRM.settings.territories.READ
- `getallterritories`: Get all territories
  Retrieves a list of territories.
  `GET /settings/territories`
  Scopes: ZohoCRM.settings.territories.READ
- `removeterritoriestorecord`: Remove Territories To Record
  Auto-generated description for operation `Remove Territories To Record`.
  `POST /{module}/{record}/actions/remove_territories`
  Scopes: ZohoCRM.modules.UPDATE
- `removeterritoriestorecords`: Remove Territories To Records
  Auto-generated description for operation `Remove Territories To Records`.
  `POST /{module}/actions/remove_territories`
  Scopes: ZohoCRM.modules.UPDATE
- `transferanddeleteterritories`: Transfer And Delete Territories
  Auto-generated description for operation `Transfer And Delete Territories`.
  `POST /settings/territories/actions/transfer_and_delete`
  Scopes: ZohoCRM.settings.territories.DELETE
- `transferanddeleteterritorybyid`: Transfer And Delete Territory By Id
  Auto-generated description for operation `Transfer And Delete Territory By Id`.
  `POST /settings/territories/{id}/actions/transfer_and_delete`
  Scopes: ZohoCRM.settings.territories.DELETE
- `updateterritory`: Update Territory
  Auto-generated description for operation `Update Territory`.
  `PUT /settings/territories`
  Scopes: ZohoCRM.settings.territories.UPDATE
- `updateterritorybyid`: Update Territory
  Auto-generated description for operation `Update Territory`.
  `PUT /settings/territories/{id}`
  Scopes: ZohoCRM.settings.territories.UPDATE

## Territory Users

### Territory Users

- `associateusertospecificterritory`: Add specific user
  Add a specific user to a territory.
  `PUT /settings/territories/{territory}/users/{user}`
  Scopes: ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL
- `associateuserstoterritory`: Add users
  Add users to a territory.
  `PUT /settings/territories/{territory}/users`
  Scopes: ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL
- `getuserdetailsfromterritory`: Get user details
  Return a specific user in a territory.
  `GET /settings/territories/{territory}/users/{user}`
  Scopes: ZohoCRM.users.READ, ZohoCRM.settings.territories.READ, ZohoCRM.users.ALL
- `getterritoryusers`: List territory users
  Return users for a territory.
  `GET /settings/territories/{territory}/users`
  Scopes: ZohoCRM.users.READ, ZohoCRM.settings.territories.READ, ZohoCRM.users.ALL
- `deassociateuserfromspecificterritory`: Remove user
  Remove a specific user from a territory.
  `DELETE /settings/territories/{territory}/users/{user}`
  Scopes: ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL
- `deassociateusersfromterritories`: Remove users
  Remove users from a territory.
  `DELETE /settings/territories/{territory}/users`
  Scopes: ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL

## Timelines

### Timelines

- `gettimelines`: Get Timelines
  Get Timelines
  `GET /{module}/{recordId}/__timeline`
  Scopes: ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ

## Unblock Email

### Unblock Email

- `unblockemailbymodule`: Unblock bulk emails in a module
  Unblock emails for multiple records in a module.
  `POST /{module}/actions/unblock_email`
  Scopes: ZohoCRM.settings.emails.CREATE
- `unblockemailbyid`: Unblock single email
  Unblock email for a single record in a module.
  `POST /{module}/{id}/actions/unblock_email`
  Scopes: ZohoCRM.settings.emails.CREATE

## unsubscribe_links

### unsubscribe_links

- `delete111111000000115722`: DELETE /settings/unsubscribe_links/111111000000115722
  To delete an unsubscribe link.
  `DELETE /settings/unsubscribe_links/{id}`
  Scopes: ZohoCRM.settings.unsubscribe.DELETE
- `getassociations`: GET /settings/unsubscribe_link/actions/associations
  To obtain information regarding the associations of unsubscribe links configured in your account.
  `GET /settings/unsubscribe_link/actions/associations`
  Scopes: ZohoCRM.settings.unsubscribe.READ
- `getunsubscribelinks`: GET /settings/unsubscribe_links
  To get all unsubscribe links
  `GET /settings/unsubscribe_links`
  Scopes: ZohoCRM.settings.unsubscribe.READ
- `get111111000000115718`: GET /settings/unsubscribe_links/111111000000115718
  To get unsubscribe link by id
  `GET /settings/unsubscribe_links/{id}`
  Scopes: ZohoCRM.settings.unsubscribe.READ
- `postunsubscribelinks`: POST /settings/unsubscribe_links
  To create an unsubscribe link
  `POST /settings/unsubscribe_links`
  Scopes: ZohoCRM.settings.unsubscribe.CREATE
- `putunsubscribelinks`: PUT /settings/unsubscribe_links
  To update an unsubscribe link.
  `PUT /settings/unsubscribe_links`
  Scopes: ZohoCRM.settings.unsubscribe.UPDATE
- `put111111000000115722`: PUT /settings/unsubscribe_links/111111000000115722
  To update an unsubscribe link.
  `PUT /settings/unsubscribe_links/{id}`
  Scopes: ZohoCRM.settings.unsubscribe.UPDATE

## Upload

### Upload

- `uploadfile`: Upload a file to CRM
  Allows uploading a file to the CRM system using multipart/form-data.
  `POST /upload`
  Scopes: ZohoFiles.files.ALL

## User Groups

### User Groups

- `creategroup`: Create Group
  Create a new user group in your organization.
  `POST /settings/user_groups`
  Scopes: ZohoCRM.settings.user_groups.CREATE
- `deletegroup`: Delete Group
  Delete an existing user group from your organization.
  `DELETE /settings/user_groups/{group}`
  Scopes: ZohoCRM.settings.user_groups.DELETE
- `getassociatedgroupsforuser`: Get Associated Groups for User
  Get the list of user groups associated with the specified user.
  `GET /users/{user}/actions/associated_groups`
  Scopes: ZohoCRM.settings.user_groups.READ
- `getassociateduserscount-2`: Get Associated Users Count
  Get the count of users associated with user groups based on the provided filters.
  `GET /settings/user_groups/actions/associated_users_count`
  Scopes: ZohoCRM.settings.user_groups.READ
- `getgroup`: Get Group
  Get details of the specified user group.
  `GET /settings/user_groups/{group}`
  Scopes: ZohoCRM.settings.user_groups.READ
- `getassociations-2`: Get Group associations
  You can associate a user group with sharing rules, workflows, assignment rules, approval and review processes, and email notification criteria. Use this API to find out where a user group is associated.
  `GET /settings/user_groups/{group}/actions/associations`
  Scopes: ZohoCRM.settings.user_groups.READ
- `getgroups`: Get Groups
  Get the list of user groups available in your organization.
  `GET /settings/user_groups`
  Scopes: ZohoCRM.settings.user_groups.ALL
- `getsources`: Get Sources
  Get the list of members for the specified user group.
  `GET /settings/user_groups/{group}/sources`
  Scopes: ZohoCRM.settings.user_groups.READ
- `getsourcescount`: Get Sources Count
  Get the count of sources (territories, roles, groups, and users) for the specified user group.
  `GET /settings/user_groups/{group}/actions/sources_count`
  Scopes: ZohoCRM.settings.user_groups.READ
- `updategroup`: Update Group
  Update an existing user group in your organization.
  `PUT /settings/user_groups/{group}`
  Scopes: ZohoCRM.settings.user_groups.UPDATE

## Users API

### Users API

- `createuser`: Create User
  Create a new user in the organization. API exposed to customers
  `POST /users`
  Scopes: ZohoCRM.users.CREATE
- `deleteuser`: Delete a User
  Delete a user by ID. API exposed to customers
  `DELETE /users/{user}`
  Scopes: ZohoCRM.users.DELETE
- `getsingleuser`: Get user
  To get a single user based on the provided user ID.
  `GET /users/{user}`
  Scopes: ZohoCRM.users.READ
- `getusers`: Get users
  To get all users based on the provided parameters.
  `GET /users`
  Scopes: ZohoCRM.users.READ
- `updateuser`: Update User
  Update multiple users. API exposed to customers
  `PUT /users`
  Scopes: ZohoCRM.users.UPDATE
- `updatesingleuser`: Update User
  Update single user by ID. API exposed to customers
  `PUT /users/{user}`
  Scopes: ZohoCRM.users.UPDATE

## Users Territories

### Users Territories

- `associateterritoriestouser`: Associate Territories to User
  Associate Territories to a User
  `PUT /users/{user}/territories`
  Scopes: ZohoCRM.settings.territories.UPDATE, ZohoCRM.users.UPDATE
- `getterritoriesofuser`: Get Territories of User
  Get Territories Assigned to a User
  `GET /users/{user}/territories`
  Scopes: ZohoCRM.settings.territories.READ, ZohoCRM.users.READ
- `getspecificterritoryofuser`: Get specific Territory of User
  Get specific territory of a user
  `GET /users/{user}/territories/{territory}`
  Scopes: ZohoCRM.settings.territories.READ, ZohoCRM.users.READ
- `removeterritoriesfromuser`: Remove Territories from User
  Remove Territories from a User
  `DELETE /users/{user}/territories`
  Scopes: ZohoCRM.settings.territories.DELETE, ZohoCRM.users.DELETE
- `removespecificterritoriesfromuser`: Remove Territory from User
  Remove Territory from a User
  `DELETE /users/{user}/territories/{territory}`
  Scopes: ZohoCRM.settings.territories.DELETE, ZohoCRM.users.DELETE

## Users Transfer

### Users Transfer

- `gettransferstatus`: Get Transfer Status
  Retrieve the status of a user transfer operation using the job ID
  `GET /users/actions/transfer_and_delete`
  Scopes: ZohoCRM.users.DELETE, ZohoCRM.users.READ
- `gettransferapistatus`: Get Transfer Status
  Retrieve the status of a user transfer operation using the job ID
  `GET /users/actions/transfer`
  Scopes: ZohoCRM.change_owner.READ
- `getvalidatebeforetransferstatus`: Get Transfer Status
  Retrieve the status of a user transfer operation using the job ID
  `GET /users/{userId}/actions/validate_before_transfer`
  Scopes: ZohoCRM.change_owner.READ
- `usertransfer`: Transfer User
  Transfer user records, assignments, and criteria to another user
  `POST /users/{userId}/actions/transfer_and_delete`
  Scopes: ZohoCRM.users.CREATE
- `usertransferwithoutid`: Transfer User
  Transfer user records, assignments, and criteria to another user
  `POST /users/actions/transfer_and_delete`
  Scopes: ZohoCRM.users.CREATE
- `usertransferapi`: Transfer User
  Transfer user records, assignments, and criteria to another user
  `POST /users/{userId}/actions/transfer`
  Scopes: ZohoCRM.change_owner.CREATE

## Variable Groups

### Variable Groups

- `getvariablegroups`: GET /settings/variable_groups
  To get the list variable groups created in crm org
  `GET /settings/variable_groups`
  Scopes: ZohoCRM.settings.variable_groups.READ
- `getvariablegroupbyid`: GET variable_groups by {id}
  To get the particular variable group
  `GET /settings/variable_groups/{id}`
  Scopes: ZohoCRM.settings.variable_groups.READ
- `putvariablegroupbyid`: PUT by variable_groups by id
  Update variable group details
  `PUT /settings/variable_groups/{id}`
  Scopes: ZohoCRM.settings.variable_groups.UPDATE
- `putvariablegroups`: PUT variable_groups
  Update variable group details
  `PUT /settings/variable_groups`
  Scopes: ZohoCRM.settings.variable_groups.UPDATE

## Variables

### Variables

- `deletevariables`: DELETE /settings/variables
  Delete all
  `DELETE /settings/variables`
  Scopes: ZohoCRM.settings.variables.DELETE
- `deletevariablebyid`: DELETE /settings/variables/1234567890
  used to delete particular variables
  `DELETE /settings/variables/{id}`
  Scopes: ZohoCRM.settings.variables.DELETE
- `getvariables`: GET /settings/variables
  This helps in fetching all the variables
  `GET /settings/variables`
  Scopes: ZohoCRM.settings.variables.READ
- `getvariablebyid`: GET /settings/variables/1234567890
  Get Variables by ID
  `GET /settings/variables/{id}`
  Scopes: ZohoCRM.settings.variables.READ
- `postvariables`: POST /settings/variables
  this creates variables.
  `POST /settings/variables`
  Scopes: ZohoCRM.settings.variables.CREATE
- `putvariables`: PUT /settings/variables
  Updates all variables
  `PUT /settings/variables`
  Scopes: ZohoCRM.settings.variables.UPDATE
- `putvariablebyid`: PUT /settings/variables/1234567890
  updates variables based on id
  `PUT /settings/variables/{id}`
  Scopes: ZohoCRM.settings.variables.UPDATE

## Webhooks

### Webhooks

- `deletewebhooks`: DELETE /settings/automation/webhooks
  To delete one or more webhooks configured in your Zoho CRM account. You can delete up to 10 webhooks in a single API call.
  `DELETE /settings/automation/webhooks`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `deletewebhooksbyid`: DELETE /settings/automation/webhooks/{webhookId}
  To delete one webhooks configured in your Zoho CRM account.
  `DELETE /settings/automation/webhooks/{webhookId}`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `getwebhookfailures`: GET /settings/automation/webhook_failures
  To retrieve detailed information about webhook execution failures in your Zoho CRM organization.
  `GET /settings/automation/webhook_failures`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `getwebhooks`: GET /settings/automation/webhooks
  Retrieve all available&nbsp;webhooks&nbsp;configured in your Zoho CRM account.
  `GET /settings/automation/webhooks`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `getassociatedmodules`: GET /settings/automation/webhooks/actions/associated_modules
  To retrieve the list of modules that are associated with&nbsp;Webhook actions&nbsp;in the current CRM account.
  `GET /settings/automation/webhooks/actions/associated_modules`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `getusagereports`: GET /settings/automation/webhooks/actions/usage_reports
  To retrieve usage statistics for Webhook actions executed in Zoho CRM over the last&nbsp;seven days.&nbsp;
  `GET /settings/automation/webhooks/actions/usage_reports`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `getwebhookbyid`: GET /settings/automation/webhooks/{webhookId}
  Retrieve the&nbsp;webhooks&nbsp;configured in your Zoho CRM account.
  `GET /settings/automation/webhooks/{webhookId}`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `postwebhooks`: POST /settings/automation/webhooks
  Webhooks in Zoho CRM allow you to send real-time data from Zoho CRM to external applications or services when specific events occur such as Record creation, update, or deletion.
  `POST /settings/automation/webhooks`
  Scopes: ZohoCRM.settings.automation_actions.CREATE
- `putwebhooks`: PUT /settings/automation/webhooks
  To update an existing webhook available in your Zoho CRM account.
  `PUT /settings/automation/webhooks`
  Scopes: ZohoCRM.settings.automation_actions.UPDATE
- `putwebhooksbyid`: PUT /settings/automation/webhooks
  To update an existing webhook available in your Zoho CRM account.
  `PUT /settings/automation/webhooks/{webhookId}`
  Scopes: ZohoCRM.settings.automation_actions.UPDATE

## Wizards

### Wizards

- `getallwizards`: Get all wizards with basic details
  This API is used to get all the wizards' basic information available in the CRM account. You can filter the response by providing the module name as a query parameter.
  `GET /settings/wizards`
  Scopes: ZohoCRM.settings.wizards.READ

## Workflow Configurations

### Workflow Configurations

- `getworkflowconfigurations`: To get workflow configuration metadata
  To retrieve the complete configuration metadata details for workflows.This includes the list of available triggers for the module, the actions supported for each trigger, and their limits and properties.&nbsp;
  `GET /workflow_configurations`
  Scopes: ZohoCRM.settings.workflow_rules.READ

## Workflow Rules

### Workflow Rules

- `postworkflowrule`: Configure a Workflow rule
  To configure a Workflow rule
  `POST /settings/automation/workflow_rules`
  Scopes: ZohoCRM.settings.workflow_rules.CREATE
- `deleteworkflowrules`: Delete Multiple Workflow Rules
  Delete Multiple Workflow Rules
  `DELETE /settings/automation/workflow_rules`
  Scopes: ZohoCRM.settings.workflow_rules.DELETE
- `deleteworkflowrulebyid`: Delete Workflow Rule By ID
  Deletes an existing workflow rule by its ID.
  `DELETE /settings/automation/workflow_rules/{id}`
  Scopes: ZohoCRM.settings.workflow_rules.DELETE
- `getworkflowrules`: Get All WorkflowRules
  To retrieve the list of Workflow rules
  `GET /settings/automation/workflow_rules`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `getactionscount`: Get Workflow Rule actions count
  To retrieve the total number of actions configured in the specified Workflow rules, including both instant and scheduled actions. The response includes a count of actions, categorized by action type.
  `GET /settings/automation/workflow_rules/actions/actions_count`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `getmodulespecificactionscount`: Get Workflow Rule actions count for each module
  Get Workflow Rule actions count for each module
  `GET /settings/automation/workflow_rules/actions/module_specific_count`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `getrulescount`: Get Workflow Rules count
  To fetch the limit and usage details of workflow rules and actions in your Zoho CRM account. Use this API to track how many rules and actions are configured and how many more you can create.
  `GET /settings/automation/workflow_rules/actions/rules_count`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `getworkflowrulebyid`: Retrieve a single workflow
  To retrieve the details of a specific Workflow rule in your Zoho CRM account.
  `GET /settings/automation/workflow_rules/{id}`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `putreorder`: To reorder workflow rules
  To update the execution order of Workflow rules in a specific module in Zoho CRM. By default, workflow rules are executed in the order in which they are created.
  `PUT /settings/automation/workflow_rules/actions/reorder`
  Scopes: ZohoCRM.settings.workflow_rules.UPDATE
- `getusage`: To retrieve Workflow Rule usage
  To retrieve the usage report of a specific Workflow Rule in your Zoho CRM organization. It provides a count of how many times the workflow was triggered and the success or failure metrics for each associated action within a specified date range.
  `GET /settings/automation/workflow_rules/{workflowRuleId}/actions/usage`
  Scopes: ZohoCRM.settings.workflow_rules.READ
- `updateworkflowrulebyid`: Update Workflow Rule By ID
  Updates an existing workflow rule with partial data.
  `PUT /settings/automation/workflow_rules/{id}`
  Scopes: ZohoCRM.settings.workflow_rules.UPDATE
- `updateworkflowrule`: Update Workflow Rule For the Given ID in Body
  Updates an existing workflow rule with partial data.
  `PUT /settings/automation/workflow_rules`
  Scopes: ZohoCRM.settings.workflow_rules.UPDATE

## Automation Task

### Automation Task

- `deletetasks`: DELETE /settings/automation/tasks
  To delete automation tasks configured in your Zoho CRM account.
  `DELETE /settings/automation/tasks`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `deletetaskbyid`: DELETE /settings/automation/tasks/{id}
  To delete automation tasks configured in your Zoho CRM account.
  `DELETE /settings/automation/tasks/{id}`
  Scopes: ZohoCRM.settings.automation_actions.DELETE
- `gettasks`: GET /settings/automation/tasks
  To retrieve the list of automation tasks configured in your Zoho CRM organization.
  `GET /settings/automation/tasks`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `gettaskbyid`: GET /settings/automation/tasks/{id}
  To retrieve automation tasks configured in your Zoho CRM organization
  `GET /settings/automation/tasks/{id}`
  Scopes: ZohoCRM.settings.automation_actions.READ
- `posttasks`: POST /settings/automation/tasks
  To create an automation task in your Zoho CRM organization.
  `POST /settings/automation/tasks`
  Scopes: ZohoCRM.settings.automation_actions.CREATE
- `puttasksbyid`: PUT /settings/automation/tasks/123445566
  To update an automation task in your Zoho CRM organization.
  `PUT /settings/automation/tasks/{id}`
  Scopes: ZohoCRM.settings.automation_actions.UPDATE

## Zia Enrichment Configuration API

### Zia Enrichment Configuration API

- `getziaenrichmentconfiguration`: get Zia Enrichment Configuration for a specific module
  get Zia Enrichment Configuration for a specific module
  `GET /settings/zia/data_enrichment`
  Scopes: ZohoCRM.zia.enrichment

## ZIA Organization Enrichment API

### ZIA Organization Enrichment API

- `getziaorgenrichment`: Get Zia Org Enrichment
  Retrieve the Zia Org Enrichment records with pagination and filtering options
  `GET /__zia_org_enrichment`
  Scopes: ZohoCRM.settings.intelligence.READ
- `getorgenrichmentbyid`: Retrieve organization-level enrichment data by enrichment ID
  Fetches the enrichment status and enriched organization data for a specific enrichment job using its unique ID. Returns completed, scheduled, or failed enrichment information along with enriched fields such as name, website, email, address, CEO, revenue, employees, social media, and industries.
  `GET /__zia_org_enrichment/{id}`
  Scopes: ZohoCRM.settings.intelligence.READ
- `submitorgenrichmentrequest`: Trigger organization-level enrichment for a CRM record
  Initiates the ZIA organization enrichment process for a specific CRM record. Accepts module name, record ID, and supported fields (name, email, website).
  `POST /__zia_org_enrichment`
  Scopes: ZohoCRM.settings.intelligence.CREATE
