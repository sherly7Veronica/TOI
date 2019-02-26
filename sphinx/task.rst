TASK
-----

views
+++++

.. automodule:: task.views

**AbstractTaskWithPenaltiesListCreateAPIView**

.. autoclass:: AbstractTaskWithPenaltiesListCreateAPIView
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

**TasksForBookingListView**

.. autoclass:: TasksForBookingListView
   :members:
   :undoc-members:
   :inherited-members:

**TaskLCAPIView**

.. autoclass:: TaskLCAPIView
   :members:
   :undoc-members:
   :inherited-members:

**TaskCompletedApiView**

.. autoclass:: TaskCompletedApiView
   :members:
   :undoc-members:
   :inherited-members:

**TaskListCreateAPIView**

.. autoclass:: TaskListCreateAPIView
   :members:
   :undoc-members:
   :inherited-members:

**TaskRetrieveUpdateDestroyAPIView**

.. autoclass:: TaskRetrieveUpdateDestroyAPIView
   :members:
   :undoc-members:
   :inherited-members:

**ActiveApiView**

.. autoclass:: ActiveApiView
   :members:
   :undoc-members:
   :inherited-members:

**AllTaskCPBookingApiView**

.. autoclass:: AllTaskCPBookingApiView
   :members:
   :undoc-members:
   :inherited-members:

**AllTaskBookingApiView**

.. autoclass:: AllTaskBookingApiView
   :members:
   :undoc-members:
   :inherited-members:

**AbstractTaskListCreateAPIView**

.. autoclass:: AbstractTaskListCreateAPIView
   :members:
   :undoc-members:
   :inherited-members:

**AbstractTaskRetrieveUpdateDestroyAPIView**

.. autoclass:: AbstractTaskRetrieveUpdateDestroyAPIView
   :members:
   :undoc-members:
   :inherited-members:

**FormElementsLCView**

.. autoclass:: FormElementsLCView
   :members:
   :undoc-members:
   :inherited-members:

**FormElementsRUDView**

.. autoclass:: FormElementsRUDView
   :members:
   :undoc-members:
   :inherited-members:

**TaskDataOptionsRetreiveView**

.. autoclass:: TaskDataOptionsRetreiveView
   :members:
   :undoc-members:
   :inherited-members:

**FormElementValueCView**

.. autoclass:: FormElementValueCView
   :members:
   :undoc-members:
   :inherited-members:

**FormElementValueRUDView**

.. autoclass:: FormElementValueRUDView
   :members:
   :undoc-members:
   :inherited-members:

**FormRetrieveView**

.. autoclass:: FormRetrieveView
   :members:
   :undoc-members:
   :inherited-members:

**TaskVariableAllRUDView**

.. autoclass:: TaskVariableAllRUDView
   :members:
   :undoc-members:
   :inherited-members:

**TaskVariableRUDView**

.. autoclass:: TaskVariableRUDView
   :members:
   :undoc-members:
   :inherited-members:

**MarkCompletedView**

.. autoclass:: MarkCompletedView
   :members:
   :undoc-members:
   :inherited-members:

**ShipperLogTaskListView**

.. autoclass:: ShipperLogTaskListView
   :members:
   :undoc-members:
   :inherited-members:

**VendorLogTaskListView**

.. autoclass:: VendorLogTaskListView
   :members:
   :undoc-members:
   :inherited-members:

models
++++++

.. automodule:: task.models

**FormData**

.. autoclass:: FormData
   :members:
   :inherited-members:

**TaskBaseModel**

.. autoclass:: TaskBaseModel
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**AbstractTask**

.. autoclass:: AbstractTask
   :members:
   :inherited-members: TaskBaseModel
   :show-inheritance:

**Task**

.. autoclass:: Task
   :members:
   :inherited-members: TaskBaseModel
   :show-inheritance:

**Form**

.. autoclass:: Form
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**FormElement**

.. autoclass:: FormElement
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**FileFormElementValue**

.. autoclass:: FileFormElementValue
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**FormElementValue**

.. autoclass:: FormElementValue
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**TaskVariable**

.. autoclass:: TaskVariable
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**TaskAcknowledgement**

.. autoclass:: TaskAcknowledgement
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**TaskFormData**

.. autoclass:: TaskFormData
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**FileUploads**

.. autoclass:: FileUploads
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

**TaskFiles**

.. autoclass:: TaskFiles
   :members:
   :inherited-members: DateBaseModel
   :show-inheritance:

serializer
+++++++++++

.. automodule:: task.serializer

**AbstractTaskWithPenaltiesSerializer**

.. autoclass:: AbstractTaskWithPenaltiesSerializer
   :members:
   :inherited-members:

**FileUploadSerializer**

.. autoclass:: FileUploadSerializer
   :members:
   :inherited-members:

**TaskFileUploadSerializer**

.. autoclass:: TaskFileUploadSerializer
   :members:
   :inherited-members:

**TaskSerializer**

.. autoclass:: TaskSerializer
   :members:
   :inherited-members:

**TaskGantChartSerializer**

.. autoclass:: TaskGantChartSerializer
   :members:
   :inherited-members:

**FormElementsSerializer**

.. autoclass:: FormElementsSerializer
   :members:
   :inherited-members:

**FormElementsRetrieveSerializer**

.. autoclass:: FormElementsRetrieveSerializer
   :members:
   :inherited-members:

**FormElementsListSerializer**

.. autoclass:: FormElementsListSerializer
   :members:
   :inherited-members:

**FormSerializer**

.. autoclass:: FormSerializer
   :members:
   :inherited-members:

**FormRetrieveSerializer**

.. autoclass:: FormRetrieveSerializer
   :members:
   :inherited-members:

**FormElementValueDataSerializer**

.. autoclass:: FormElementValueDataSerializer
   :members:
   :inherited-members:

**AbstractTaskSerializer**

.. autoclass:: AbstractTaskSerializer
   :members:
   :inherited-members:

**TaskDataSerializer**

.. autoclass:: TaskDataSerializer
   :members:
   :inherited-members:

**TaskVariableSerializerModel**

.. autoclass:: TaskVariableSerializerModel
   :members:
   :inherited-members:

urls
++++

**1.AbstractTaskListCreateAPIView**

.. note:: API: "api/tasks/abstracttask/"

.. note:: Method: GET, POST

GET:

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Enter Vehicle Details",
      "task_description": "Enter Vehicle Details",
      "task_type": 1,
      "task_category": 0,
      "task_for": "transporter",
      "expiry": 360,
      "escalate_at": 180,
      "dependency_tasks": [],
      "trigger_tasks_on_completion": [
        <string>,
        <string>
      ],
      "mode_type": <string>,
      "hub_type": <string>,
      "is_incoming": false,
      "notify_stakeholders": "client,forwarder",
      "secondary_stakeholders": "",
      "notification_msg_short": "Enter Vehicle Details for booking ID: {booking} Before Session ends on {date}",
      "notification_msg_long": "Enter Vehicle Details for booking ID: {booking} Before Session ends on {date}",
      "notification_msg_title": "hey",
      "is_display_field": false,
      "display_name": null,
      "form": {
        "id": <string>,
        "name": "Update Driver Number and Vehicle Number",
        "description": "Update Driver Number and Vehicle Number"
      },
      "trigger_tasks_on": 0,
      "initiator_task": false,
      "estimated_completion_at": 1080
    }
    so on...

POST:

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

    {
    "notification_msg_title": <string>,
    "notification_msg_long": <string>,
    "task_for": <string>,
    "task_type": <int>,
    "task_description": <string>,
    "notification_msg_short": <string>,
    "notify_stakeholders": <string>,
    "task_name": <string>,
    "estimated_completion_at": <int>
    }

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "task_name": "test",
     "task_description": "test",
     "task_type": 0,
     "task_category": 0,
     "task_for": "shipper",
     "expiry": null,
     "escalate_at": null,
     "dependency_tasks": [],
     "trigger_tasks_on_completion": [],
     "mode_type": null,
     "hub_type": null,
     "is_incoming": null,
     "notify_stakeholders": "test",
     "secondary_stakeholders": "",
     "notification_msg_short": "test",
     "notification_msg_long": "test",
     "notification_msg_title": "test",
     "is_display_field": false,
     "display_name": null,
     "form": null,
     "trigger_tasks_on": 0,
     "initiator_task": null,
     "estimated_completion_at": 77
   }

**2.AbstractTaskWithPenaltiesListCreateAPIView**

.. note:: API: "api/tasks/abstracttask/penalties/"

.. note:: Method: GET, POST

GET:

**Response**

.. code-block:: Python

   {
     "task_for": "transporter",
     "expiry": 360,
     "escalate_at": 180,
     "mode_type": <string>,
     "hub_type": <string>,
     "is_incoming": false,
     "penalties": [],
     "estimated_completion_at": 1080
   },
   {
     "task_for": "transporter",
     "expiry": 720,
     "escalate_at": 360,
     "mode_type": <string>,
     "hub_type": <string>,
     "is_incoming": false,
     "penalties": [
       {
         "id": <string>,
         "penalty": 500,
         "tax": <string>,
         "description": "Delay for Gate In",
         "penalty_type": 2,
         "penalty_currency": "INR",
         "tax_currency": "INR"
       },
       {
         "id": <string>,
         "penalty": 939,
         "tax": "0f4461d3-6d78-4c35-bf04-10e9a1c40c2a",
         "description": "Delay",
         "penalty_type": 1,
         "penalty_currency": "INR",
         "tax_currency": "INR"
       }
     "estimated_completion_at": 1440
   }
   so on...

POST:

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
       "estimated_completion_at": <int>,
       "task_for": <string>
   }

**Response**

.. code-block:: Python

**3.AbstractTaskRetrieveUpdateDestroyAPIView**

.. note:: API: "api/tasks/abstracttask/(?P<pk>[^/]+)/"

.. note:: Method: GET, PUT, PATCH, DELETE

GET:

**Response**

.. code-block:: Python

   {
       "id": <string>,
       "task_name": <string>,
       "task_description": <string>,
       "task_type": 0,
       "task_category": 0,
       "task_for": "shipper",
       "expiry": null,
       "escalate_at": null,
       "dependency_tasks": [],
       "trigger_tasks_on_completion": [],
       "mode_type": null,
       "hub_type": null,
       "is_incoming": null,
       "notify_stakeholders": <string>,
       "secondary_stakeholders": <string>,
       "notification_msg_short": <string>,
       "notification_msg_long": <string>,
       "notification_msg_title": <string>,
       "is_display_field": false,
       "display_name": null,
       "form": null,
       "trigger_tasks_on": 0,
       "initiator_task": null,
       "estimated_completion_at": 77
   }


PUT:

.. note:: These fields are mandatory.

**Request**

.. code-block:: Python

    {
    "notification_msg_title": <string>,
    "notification_msg_long": <string>,
    "task_for": <string>,
    "task_type": <int>,
    "task_description": <string>,
    "notification_msg_short": <string>,
    "notify_stakeholders": <string>,
    "task_name": <string>,
    "estimated_completion_at": <int>
    }


**Response**

.. code-block:: Python

   {
       "id": <string>,
       "task_name": <string>,
       "task_description": <string>,
       "task_type": 0,
       "task_category": 0,
       "task_for": "shipper",
       "expiry": null,
       "escalate_at": null,
       "dependency_tasks": [],
       "trigger_tasks_on_completion": [],
       "mode_type": null,
       "hub_type": null,
       "is_incoming": null,
       "notify_stakeholders": <string>,
       "secondary_stakeholders": <string>,
       "notification_msg_short": <string>,
       "notification_msg_long": <string>,
       "notification_msg_title": <string>,
       "is_display_field": false,
       "display_name": null,
       "form": null,
       "trigger_tasks_on": 0,
       "initiator_task": null,
       "estimated_completion_at": 77
   }

PATCH:

**Request**

.. code-block:: Python

   {
       "notification_msg_title": "latest"
   }

**Response**

.. code-block:: Python

   {
       "id": <string>,
       "task_name": <string>,
       "task_description": <string>,
       "task_type": 0,
       "task_category": 0,
       "task_for": "shipper",
       "expiry": null,
       "escalate_at": null,
       "dependency_tasks": [],
       "trigger_tasks_on_completion": [],
       "mode_type": null,
       "hub_type": null,
       "is_incoming": null,
       "notify_stakeholders": <string>,
       "secondary_stakeholders": <string>,
       "notification_msg_short": <string>,
       "notification_msg_long": <string>,
       "notification_msg_title": "latest",       <---- updated
       "is_display_field": false,
       "display_name": null,
       "form": null,
       "trigger_tasks_on": 0,
       "initiator_task": null,
       "estimated_completion_at": 77
   }

DELETE:

**Response**

.. code-block:: Python

   {
    "detail": "Not found."
   }

**4.TaskListCreateAPIView**

.. note:: API: "api/tasks/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-05T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": "9faad55c-5bd9-4545-9ccf-************",
         "user": {
           "name": null,
           "email": <string>
         },
         "executive_first_name": "Transporter",
         "executive_last_name": "Camelport",
         "company_name": "Camelport Transporter",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       },
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 0,
     "task_category": 3,
     "is_active": false,
     "completed_at": null,
     "booking": {
       "id": "affbd05d-8ea1-4ef3-bf46-************",
       "quote": "f9b5ca5d-fb7a-4bdf-9982-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-******",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "76b1ea89-eb2d-45f2-ae6e-************",
       "e629a3c8-9dfe-46ad-b10b-************",
       "43c77e9c-13fa-4e5f-b463-************"
     ],
     "abstract_task": "44f59912-927c-4cab-9a5a-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   }
   {
     "id": "37fcda8e-184b-4ae9-961d-************",
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-05T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": "9faad55c-5bd9-4545-9ccf-************",
         "user": {
           "name": null,
           "email": <string>
         },
         "executive_first_name": "Transporter",
         "executive_last_name": "Camelport",
         "company_name": "Camelport Transporter",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       },
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 0,
     "task_category": 3,
     "is_active": false,
     "completed_at": null,
     "booking": {
       "id": "affbd05d-8ea1-4ef3-bf46-************",
       "quote": "f9b5ca5d-fb7a-4bdf-9982-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-******",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "76b1ea89-eb2d-45f2-ae6e-************",
       "e629a3c8-9dfe-46ad-b10b-************",
       "43c77e9c-13fa-4e5f-b463-************"
     ],
     "abstract_task": "44f59912-927c-4cab-9a5a-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   }
   {
     "id": "37fcda8e-184b-4ae9-961d-************",
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-05T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": "9faad55c-5bd9-4545-9ccf-************",
         "user": {
           "name": null,
           "email": <string>
         },
         "executive_first_name": "Transporter",
         "executive_last_name": "Camelport",
         "company_name": "Camelport Transporter",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       },
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 0,
     "task_category": 3,
     "is_active": false,
     "completed_at": null,
     "booking": {
       "id": "affbd05d-8ea1-4ef3-bf46-************",
       "quote": "f9b5ca5d-fb7a-4bdf-9982-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-******",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "76b1ea89-eb2d-45f2-ae6e-************",
       "e629a3c8-9dfe-46ad-b10b-************",
       "43c77e9c-13fa-4e5f-b463-************"
     ],
     "abstract_task": "44f59912-927c-4cab-9a5a-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   }

   so on...


**5.TaskCompletedApiView**

.. note:: API: "api/tasks/completed/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "id": "59d98561-500e-4d72-80f9-************",
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-22T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       },
       {
         "id": "576d5fbe-cbf5-4c41-8b39-************",
         "user": {
           "name": null,
           "email": <string>
         },
         "executive_first_name": <string>,
         "executive_last_name": "k",
         "company_name": "abc",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 100,
     "task_category": 3,
     "is_active": false,
     "completed_at": "2019-01-18T12:07:06.355902Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-4BFBUJ",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "4c70499a-0bbf-47bc-a2b6-55ab24d0c47e",
       "1436e5b6-1535-410c-995c-28d84783b79a",
       "bd2942e7-4b7d-4655-885d-edc3ee223830"
     ],
     "abstract_task": "44f59912-927c-4cab-9a5a-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": "fd90559b-7882-46e1-8278-************",
     "task_name": "Enter Custom Agent Details",
     "task_description": "Enter Custom Agent Details",
     "dependency_tasks": [],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-18T12:08:53.789940Z",
     "expiry": 864,
     "escalation": 432,
     "notify_stakeholders": [],
     "secondary_stakeholders": [],
     "task_type": 1,
     "completed_percentage": 100,
     "task_category": 0,
     "is_active": false,
     "completed_at": "2019-01-18T12:09:39.498835Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-4BFBUJ",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "2a73d819-5da1-4d09-be76-************",
       "e051d455-d6ba-40af-bdc7-************"
     ],
     "abstract_task": "f3d90d78-7aa5-411d-ada3-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": "2a73d819-5da1-4d09-be76-************",
     "task_name": "Depart From Factory",
     "task_description": "Depart From Factory",
     "dependency_tasks": [
       "e051d455-d6ba-40af-bdc7-************",
       "76ff1791-ddc8-4a4d-ba36-************"
     ],
     "task_for": {
       "id": "576d5fbe-cbf5-4c41-8b39-************",
       "user": {
         "name": null,
         "email": <string>
       },
       "executive_first_name": <string>,
       "executive_last_name": "k",
       "company_name": "abc",
       "is_enabled": false,
       "stakeholder_type": "Trucker"
     },
     "triggered_at": "2019-01-18T12:08:53.775679Z",
     "expiry": 1007,
     "escalation": 720,
     "notify_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 3,
     "completed_percentage": 100,
     "task_category": 2,
     "is_active": false,
     "completed_at": "2019-01-18T12:09:04.484814Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-4BFBUJ",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "9ed7f9d2-7aba-4078-b774-************"
     ],
     "abstract_task": "a990d3e1-0bcf-4d9e-93a0-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": "e051d455-d6ba-40af-bdc7-************",
     "task_name": "Upload BL (draft)",
     "task_description": "Upload Bill",
     "dependency_tasks": [
       "76ff1791-ddc8-4a4d-ba36-************"
     ],
     "task_for": {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
         "name": "veronica",
         "email": <string>
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-18T12:09:39.565642Z",
     "expiry": 864,
     "escalation": 432,
     "notify_stakeholders": [],
     "secondary_stakeholders": [],
     "task_type": 1,
     "completed_percentage": 100,
     "task_category": 0,
     "is_active": false,
     "completed_at": "2019-01-18T12:10:01.409255Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-4BFBUJ",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [],
     "abstract_task": "8faf928d-bf69-483f-af99-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": "1436e5b6-1535-410c-995c-************",
     "task_name": "Enter Container Details",
     "task_description": "Enter Container Details",
     "dependency_tasks": [
       "4c70499a-0bbf-47bc-a2b6-************"
     ],
     "task_for": {
       "id": "576d5fbe-cbf5-4c41-8b39-************",
       "user": {
         "name": null,
         "email": <string>
       },
       "executive_first_name": <string>,
       "executive_last_name": "k",
       "company_name": "abc",
       "is_enabled": false,
       "stakeholder_type": "Trucker"
     },
     "triggered_at": "2019-01-18T12:08:07.048022Z",
     "expiry": 720,
     "escalation": 480,
     "notify_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 100,
     "task_category": 0,
     "is_active": false,
     "completed_at": "2019-01-18T12:08:42.830106Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-******",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "76ff1791-ddc8-4a4d-ba36-************",
       "fd90559b-7882-46e1-8278-************"
     ],
     "abstract_task": "ed865b3a-55de-426c-b8a0-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": "76ff1791-ddc8-4a4d-ba36-************",
     "task_name": "Arrival at Factory",
     "task_description": "Arrival at Factory",
     "dependency_tasks": [
       "1436e5b6-1535-410c-995c-************",
       "bd2942e7-4b7d-4655-885d-************"
     ],
     "task_for": {
       "id": "576d5fbe-cbf5-4c41-8b39-************",
       "user": {
         "name": null,
         "email": <string>
       },
       "executive_first_name": <string>,
       "executive_last_name": "k",
       "company_name": "abc",
       "is_enabled": false,
       "stakeholder_type": "Trucker"
     },
     "triggered_at": "2019-01-18T12:08:42.880023Z",
     "expiry": 1002,
     "escalation": 668,
     "notify_stakeholders": [
       {
         "id": "576d5fbe-cbf5-4c41-8b39-************",
         "user": {
           "name": null,
           "email": <string>
         },
         "executive_first_name": <string>,
         "executive_last_name": "k",
         "company_name": "abc",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": "ad0b3dc5-b121-43ea-9ed2-************",
         "user": {
           "name": "veronica",
           "email": <string>
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 3,
     "completed_percentage": 100,
     "task_category": 2,
     "is_active": false,
     "completed_at": "2019-01-18T12:08:53.700686Z",
     "booking": {
       "id": "39fb8580-0f92-49f9-81bb-************",
       "quote": "d6aeb1e5-306c-49ea-b2aa-************",
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-******",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       "2a73d819-5da1-4d09-be76-************",
       "fd90559b-7882-46e1-8278-************",
       "e051d455-d6ba-40af-bdc7-************"
     ],
     "abstract_task": "46632fe8-f58c-4b6d-a851-************",
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   }


**6.TaskLCAPIView**                              -------pending

.. note:: API: "api/tasks/update/(?P<task_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**7.ActiveApiView**

.. note:: API: "api/tasks/active/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": <string>,
       "user": {
         "name": "veronica",
         "email": "sherly7veronica@gmail.com"
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-05T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": <string>,
         "user": {
           "name": null,
           "email": "snehalchile95+t@gmail.com"
         },
         "executive_first_name": "Transporter",
         "executive_last_name": "Camelport",
         "company_name": "Camelport Transporter",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       },
       {
         "id": <string>,
         "user": {
           "name": "veronica",
           "email": "sherly7veronica@gmail.com"
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": <string>,
         "user": {
           "name": "veronica",
           "email": "sherly7veronica@gmail.com"
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 0,
     "task_category": 3,
     "is_active": false,
     "completed_at": null,
     "booking": {
       "id": <string>,
       "quote": <string>,
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-LCQQF7",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       <string>,
       <string>,
       <string>
     ],
     "abstract_task": <string>,
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   },
   {
     "id": <string>,
     "task_name": "Upload Delivery Order",
     "task_description": "Upload Delivery Order",
     "dependency_tasks": [],
     "task_for": {
       "id": <string>,
       "user": {
         "name": "veronica",
         "email": "sherly7veronica@gmail.com"
       },
       "executive_first_name": "veronica",
       "executive_last_name": "sherly",
       "company_name": "abcd",
       "is_enabled": false,
       "stakeholder_type": "Shipper"
     },
     "triggered_at": "2019-01-05T01:30:00Z",
     "expiry": 720,
     "escalation": 360,
     "notify_stakeholders": [
       {
         "id": <string>,
         "user": {
           "name": null,
           "email": "snehalchile95+t@gmail.com"
         },
         "executive_first_name": "Transporter",
         "executive_last_name": "Camelport",
         "company_name": "Camelport Transporter",
         "is_enabled": false,
         "stakeholder_type": "Trucker"
       },
       {
         "id": <string>,
         "user": {
           "name": "veronica",
           "email": "sherly7veronica@gmail.com"
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "secondary_stakeholders": [
       {
         "id": <string>,
         "user": {
           "name": "veronica",
           "email": "sherly7veronica@gmail.com"
         },
         "executive_first_name": "veronica",
         "executive_last_name": "sherly",
         "company_name": "abcd",
         "is_enabled": false,
         "stakeholder_type": "Shipper"
       }
     ],
     "task_type": 1,
     "completed_percentage": 0,
     "task_category": 3,
     "is_active": false,
     "completed_at": null,
     "booking": {
       "id": <string>,
       "quote": <string>,
       "is_cancelled": false,
       "is_completed": false,
       "terminated_at": null,
       "cp_booking_number": "CPQ-LCQQF7",
       "is_confirmed": true
     },
     "event": null,
     "trigger_tasks_on_completion": [
       <string>,
       <string>,
       <string>
     ],
     "abstract_task": <string>,
     "estimated_completion": 4000,
     "partially_completed_at": null,
     "expired_at": null
   }

**8.AllTaskCPBookingApiView**

.. note:: API: "api/tasks/cpbooking-tasks/(?P<cpbooking_id>[^/]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Upload Delivery Order",
      "task_description": "Upload Delivery Order",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Forwarder",
        "executive_last_name": "Logistics",
        "company_name": "Logistic Forwarder",
        "is_enabled": false,
        "stakeholder_type": "Forwarder"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 720,
      "escalation": 360,
      "notify_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Transporter",
          "executive_last_name": "Camelport",
          "company_name": "Camelport Transporter",
          "is_enabled": false,
          "stakeholder_type": "Trucker"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>,
        <string>
      ],
      "abstract_task": <string>,
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    },
    {
      "id": <string>,
      "task_name": "Enter Vehicle Details",
      "task_description": "Enter Vehicle Details",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Transporter",
        "executive_last_name": "Camelport",
        "company_name": "Camelport Transporter",
        "is_enabled": false,
        "stakeholder_type": "Trucker"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 360,
      "escalation": 180,
      "notify_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>
      ],
      "abstract_task": <string>
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    }
    so on...

**9.AllTasksCPBookingApiView**

.. note:: API: "api/tasks/all-cpbooking-tasks/(?P<cpbooking_id>[^/]+)/"

.. note:: Method: POST

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Upload Delivery Order",
      "task_description": "Upload Delivery Order",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Forwarder",
        "executive_last_name": "Logistics",
        "company_name": "Logistic Forwarder",
        "is_enabled": false,
        "stakeholder_type": "Forwarder"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 720,
      "escalation": 360,
      "notify_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Transporter",
          "executive_last_name": "Camelport",
          "company_name": "Camelport Transporter",
          "is_enabled": false,
          "stakeholder_type": "Trucker"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>,
        <string>
      ],
      "abstract_task": <string>,
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    }
    so on...

**10.AllTaskBookingApiView**

.. note:: API: "api/tasks/booking-tasks/(?P<booking_id>[^/]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Upload Delivery Order",
      "task_description": "Upload Delivery Order",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Forwarder",
        "executive_last_name": "Logistics",
        "company_name": "Logistic Forwarder",
        "is_enabled": false,
        "stakeholder_type": "Forwarder"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 720,
      "escalation": 360,
      "notify_stakeholders": [
        {
          "id": <string>,,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Transporter",
          "executive_last_name": "Camelport",
          "company_name": "Camelport Transporter",
          "is_enabled": false,
          "stakeholder_type": "Trucker"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>,
        <string>
      ],
      "abstract_task": <string>,
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    }
    so on...

**11.AllTasksBookingApiView**

.. note:: API: "api/tasks/all-booking-tasks/(?P<booking_id>[^/]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Upload Delivery Order",
      "task_description": "Upload Delivery Order",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Forwarder",
        "executive_last_name": "Logistics",
        "company_name": "Logistic Forwarder",
        "is_enabled": false,
        "stakeholder_type": "Forwarder"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 720,
      "escalation": 360,
      "notify_stakeholders": [
        {
          "id": <string>,,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Transporter",
          "executive_last_name": "Camelport",
          "company_name": "Camelport Transporter",
          "is_enabled": false,
          "stakeholder_type": "Trucker"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>,
        <string>
      ],
      "abstract_task": <string>,
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    }
    so on...

**12.TasksForBookingListView**

.. note:: API: "api/tasks/booking/(?P<booking_id>[^/]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

    {
      "id": <string>,
      "task_name": "Upload Delivery Order",
      "task_description": "Upload Delivery Order",
      "dependency_tasks": [],
      "task_for": {
        "id": <string>,
        "user": {
          "name": null,
          "email": <string>
        },
        "executive_first_name": "Forwarder",
        "executive_last_name": "Logistics",
        "company_name": "Logistic Forwarder",
        "is_enabled": false,
        "stakeholder_type": "Forwarder"
      },
      "triggered_at": "2019-01-26T01:30:00Z",
      "expiry": 720,
      "escalation": 360,
      "notify_stakeholders": [
        {
          "id": <string>,,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Forwarder",
          "executive_last_name": "Logistics",
          "company_name": "Logistic Forwarder",
          "is_enabled": false,
          "stakeholder_type": "Forwarder"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>
          },
          "executive_first_name": "Transporter",
          "executive_last_name": "Camelport",
          "company_name": "Camelport Transporter",
          "is_enabled": false,
          "stakeholder_type": "Trucker"
        },
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "secondary_stakeholders": [
        {
          "id": <string>,
          "user": {
            "name": null,
            "email": <string>,
          },
          "executive_first_name": "New",
          "executive_last_name": "Shipper",
          "company_name": "Camelport Shipper",
          "is_enabled": false,
          "stakeholder_type": "Shipper"
        }
      ],
      "task_type": 1,
      "is_active": false,
      "completed_at": null,
      "booking": {
        "id": <string>,
        "quote": <string>,
        "is_cancelled": false,
        "is_completed": false,
        "terminated_at": null,
        "cp_booking_number": "CPQ-******",
        "is_confirmed": true
      },
      "event": null,
      "trigger_tasks_on_completion": [
        <string>,
        <string>,
        <string>
      ],
      "abstract_task": <string>,
      "estimated_completion": 4000,
      "partially_completed_at": null,
      "completed_percentage": 0,
      "expired_at": null,
      "can_edit": false,
      "can_view": false,
      "is_rejected": false
    }
    so on...

**13.FormElementsLCView**

.. note:: API: "api/tasks/formelement-create/"

.. note:: Method: GET, POST

GET:

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "type": <string>,
     "css_class": <string>,
     "label": <string>,
     "placeholder": null,
     "name": <string>,
     "kwargs": {
       "required": <boolean>,
       "choices": [
         <string>,
         <string>
       ]
     },
     "default": <string>,
     "order": <int>,
     "assign_to_var": null,
     "is_autofill": <boolean>
   }

POST:

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

**Response**

.. code-block:: Python



**14.FormElementsRUDView**

.. note:: API: "api/tasks/formelement-rud/(?P<element_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**15.MarkCompletedView**

.. note:: API: "api/tasks/mark-completed/(?P<task_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**16.TaskDataOptionsRetreiveView**

.. note:: API: "api/tasks/form/(?P<pk>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**17.ShipperLogTaskListView**

.. note:: API: "api/tasks/all-task-log/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "shipment_num": <int>,
     "task_id": <string>,
     "updated_at": "2019-01-18T12:10:01.349538Z",
     "booking_num": <string>,
     "container_num": <string>,
     "task_name": <string>
   }

**18.VendorLogTaskListView**

.. note:: API: "api/tasks/vendor-all-task-log/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "shipment_num": <int>,
     "task_id": <string>,
     "updated_at": "2019-01-18T12:10:01.349538Z",
     "booking_num": <string>,
     "container_num": <string>,
     "task_name": <string>
   }

**19.FormElementValueCView**

.. note:: API: "api/tasks/(?P<pk>[^/]+)/data/(?P<s_num>[\d]+)/create/"

.. note:: Method: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python



**Response**

.. code-block:: Python

**20.FormElementValueRUDView**

.. note:: API: "api/tasks/(?P<pk>[^/]+)/data/(?P<s_num>[\d]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**21.TaskVariableAllRUDView**

.. note:: API: "api/tasks/variable/all/(?P<booking_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**22.TaskVariableRUDView**

.. note:: API: "api/tasks/variable/(?P<booking_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**23.TaskRetrieveUpdateDestroyAPIView**

.. note:: API: "api/tasks/variable/(?P<booking_id>[^/]+)/"

.. note:: Method: POST

**Request**

.. code-block:: Python

**Response**

.. code-block:: Python

**24.FormRetrieveView**

.. note:: API: "api/tasks/(?P<pk>[^/]+)/form/retrieve/(?P<s_num>[\d]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "name": <string>,
     "description": <string>,
     "form_elements": [
       {
         "id": <string>,
         "type": <string>,
         "css_class": "<string>,
         "label": <string>,
         "placeholder": <string>,
         "name": <string>,
         "kwargs": {
           "required": <boolean>
         },
         "default": null,
         "order": <int>,
         "assign_to_var": null,
         "is_autofill": <boolean>,
         "value_present": <boolean>
       },
       {
         "id": <string>,
         "type": <string>,
         "css_class": "<string>,
         "label": <string>,
         "placeholder": <string>,
         "name": <string>,
         "kwargs": {
           "required": <boolean>
         },
         "default": null,
         "order": <int>,
         "assign_to_var": null,
         "is_autofill": <boolean>,
         "value_present": <boolean>
       },
       {
         "id": <string>,
         "type": <string>,
         "css_class": "<string>,
         "label": <string>,
         "placeholder": <string>,
         "name": <string>,
         "kwargs": {
           "required": <boolean>
         },
         "default": null,
         "order": <int>,
         "assign_to_var": null,
         "is_autofill": <boolean>,
         "value_present": <boolean>
       }
     ]
   }