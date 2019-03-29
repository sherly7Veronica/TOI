STAKEHOLDER
-----------

views
+++++

.. automodule:: stakeholder.views

**RegisterView**

.. autoclass:: RegisterView
   :members:
   :undoc-members:
   :inherited-members: generics.CreateAPIView
   :show-inheritance:

**StakeholderPricingPlanRetrieveView**

.. autoclass:: StakeholderPricingPlanRetrieveView
   :members:
   :undoc-members:
   :inherited-members: APIView

**LoginView**

.. autoclass:: LoginView
   :members:
   :undoc-members:
   :inherited-members:

**GuestStakeholderView**

.. autoclass:: GuestStakeholderView
   :members:
   :undoc-members:
   :inherited-members:

**GuestStakeholderRUDView**

.. autoclass::  GuestStakeholderRUDView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderTypeView**

.. autoclass:: StakeholderTypeView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderRegStatusUpdateView**

.. autoclass:: StakeholderRegStatusUpdateView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderUpdateView**

.. autoclass:: StakeholderUpdateView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderRetrieveView**

.. autoclass:: StakeholderRetrieveView
   :members:
   :undoc-members:
   :inherited-members:

**BusinessEntityAutocompleteView**

.. autoclass:: BusinessEntityAutocompleteView
   :members:
   :undoc-members:
   :inherited-members:

**SendOTPView**

.. autoclass:: SendOTPView
   :members:
   :undoc-members:
   :inherited-members:

**SendOTPEwayBillView**

.. autoclass:: SendOTPEwayBillView
   :members:
   :undoc-members:
   :inherited-members:

**VerifyOTPView**

.. autoclass:: VerifyOTPView
   :members:
   :undoc-members:
   :inherited-members:

**RetryOTPView**

.. autoclass:: RetryOTPView
   :members:
   :undoc-members:
   :inherited-members:

**VerifyEmailView**

.. autoclass:: VerifyEmailView
   :members:
   :undoc-members:
   :inherited-members:

**EWayBillGSTView**

.. autoclass:: EWayBillGSTView
   :members:
   :undoc-members:
   :inherited-members:

**inttra_auth_check**

.. autoclass:: inttra_auth_check
   :members:
   :undoc-members:
   :inherited-members:

**itekseal_auth_check**

.. autoclass:: itekseal_auth_check
   :members:
   :undoc-members:
   :inherited-members:

**odex_auth_check**

.. autoclass:: odex_auth_check
   :members:
   :undoc-members:
   :inherited-members:

**GuestStakeholderListView**

.. autoclass:: GuestStakeholderListView
   :members:
   :undoc-members:
   :inherited-members:

**ChangePasswordRequestView**

.. autoclass:: ChangePasswordRequestView
   :members:
   :undoc-members:
   :inherited-members:

**ChangeStakeholderPasswordView**

.. autoclass:: ChangeStakeholderPasswordView
   :members:
   :undoc-members:
   :inherited-members:

**ChangeUserPasswordView**

.. autoclass:: ChangeUserPasswordView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderInfoRetrieveAPIView**

.. autoclass:: StakeholderInfoRetrieveAPIView
   :members:
   :undoc-members:
   :inherited-members:

**EmailVerifyView**

.. autoclass:: EmailVerifyView
   :members:
   :undoc-members:
   :inherited-members:


models
++++++

.. automodule:: stakeholder.models

**Stakeholder**

.. autoclass:: Stakeholder
   :members:
   :inherited-members:

**GuestStakeholder**

.. autoclass:: GuestStakeholder
   :members:
   :inherited-members: DateBaseModel

**BusinessEntity**

.. autoclass:: BusinessEntity
   :members:
   :inherited-members: DateBaseModel

**StakeholderInfo**

.. autoclass:: StakeholderInfo
   :members:
   :inherited-members: DateBaseModel

**Session**

.. autoclass:: Session
   :members:
   :inherited-members: DateBaseModel

**EmailVerifyToken**

.. autoclass:: EmailVerifyToken
   :members:
   :inherited-members: DateBaseModel


serializer
+++++++++++

.. automodule:: stakeholder.serializers

**StakeholderRegisterSerializer**

.. autoclass:: StakeholderRegisterSerializer
   :members:
   :inherited-members:

**StakeholderRegStatusSerializer**

.. autoclass:: StakeholderRegStatusSerializer
   :members:
   :inherited-members:

**ChildStakeholderSerializer**

.. autoclass:: ChildStakeholderSerializer
   :members:
   :inherited-members:

**GuestStakeholderSerializer**

.. autoclass:: GuestStakeholderSerializer
   :members:
   :inherited-members:

**StakeholderUpdateSerializer**

.. autoclass:: StakeholderUpdateSerializer
   :members:
   :inherited-members:

**BusinessEntitySerializer**

.. autoclass:: BusinessEntitySerializer
   :members:
   :inherited-members:

**ChildStakeholderListSerializer**

.. autoclass:: ChildStakeholderListSerializer
   :members:
   :inherited-members:

**StakeholderFullSerializer**

.. autoclass:: StakeholderFullSerializer
   :members:
   :inherited-members:

**StakeholderShortSerializer**

.. autoclass:: StakeholderShortSerializer
   :members:
   :inherited-members:

**StakeholderChangePasswordSerializer**

.. autoclass:: StakeholderChangePasswordSerializer
   :members:
   :inherited-members:

**StakeholderInfoSerializer**

.. autoclass:: StakeholderInfoSerializer
   :members:
   :inherited-members:

**StakeholderDetailSerializer**

.. autoclass:: StakeholderDetailSerializer
   :members:
   :inherited-members:


urls
++++

**1.StakeholderTypeView**

.. note:: API: "api/stakeholder/types/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "results": [
       {
         "id": <string>,
         "table_name": "Surveyor"
       },
       {
         "id": <string>,
         "table_name": "Forwarder"
       },
       {
         "id": <string>,
         "table_name": "Forwarder1"
       },
       {
         "id": <string>,
         "table_name": "Guest4"
       },
       {
         "id": <string>,
         "table_name": "Guest3"
       },
       {
         "id": <string>,
         "table_name": "Guest2"
       },
       {
         "id": <string>,
         "table_name": "Guest1"
       },
       {
         "id": <string>,
         "table_name": "guest"
       },

       {
         "id": <string>,
         "table_name": "Camelport Marketing"
       },
       {
         "id": <string>,
         "table_name": "Camelport Operations"
       }
     ]
   }


**2.RegisterView**

.. note:: API: "api/stakeholder/register/"

.. note:: Method: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
   "password1": <string(32)>,
   "password2": <string(32)>,
   "user": {
   "name": <string(128)>,
   "email": <string(128)>
   },
   "executive_first_name": <string(32)>
   }

**Response**

.. code-block:: Python

   {
    "id":  <string> ,
    "user": {
        "name": <string>,
        "email": <string>
    },
    "executive_first_name": "test1",
    "executive_last_name": null,
    "phone": null,
    "mobile": null,
    "company_name": null,
    "entity_type": null,
    "pan_number": null,
    "iec_code": null,
    "company_address_line_1": null,
    "company_address_line_2": null,
    "company_address_line_3": null,
    "city": null,
    "state": null,
    "country": null,
    "zipcode": null,
    "designation": null,
    "dynamic_table": "Shipper",
    "reg_status": 0,
    "is_enabled": false,
    "razor_pay": null,
    "razor_account_number": null,
    "razor_ifsc_code": null,
    "quickbooks_customer": null,
    "helpscout_id": <int>
   }

**3.StakeholderUpdateView**

.. note:: API: "api/stakeholder/update/"

.. note:: Methods: PUT, PATCH

PUT:

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "executive_first_name": <string>
   }

**Request**

.. code-block:: Python

   {
    "executive_first_name": "Monica"
   }

**Response**

.. code-block:: Python

   {
    "id": "c7e459fc-95e4-41b6-b6f9-************",
    "executive_first_name": "Monica",                     <----- executive_first_name changed
    "executive_last_name": "K",
    "phone": null,
    "mobile": "***********",
    "dynamic_table": "58718e97-cc50-4c8a-8ab4-************",
    "company_name": "CamelPort",
    "entity_type": null,
    "pan_number": null,
    "iec_code": null,
    "company_address_line_1": null,
    "company_address_line_2": null,
    "company_address_line_3": null,
    "city": null,
    "state": null,
    "country": null,
    "zipcode": null,
    "designation": null,
    "reg_status": 1,
    "is_enabled": false
   }

Before:

.. code-block:: Python

   {
    "id": "c7e459fc-95e4-41b6-b6f9-************",
    "executive_first_name": "Veronica",                <----- initial executive_first_name
    "executive_last_name": "K",
    "phone": null,
    "mobile": "***********",
    "dynamic_table": "58718e97-cc50-4c8a-8ab4-************",
    "company_name": "CamelPort",
    "entity_type": null,
    "pan_number": null,
    "iec_code": null,
    "company_address_line_1": null,
    "company_address_line_2": null,
    "company_address_line_3": null,
    "city": null,
    "state": null,
    "country": null,
    "zipcode": null,
    "designation": null,
    "reg_status": 1,
    "is_enabled": false
   }


PATCH: The PATCH method is used to apply partial modifications to a resource.

.. note:: No mandatory fields in this method.


**4.StakeholderRetrieveView**

.. note:: API: "api/stakeholder/retrieve/"

.. note:: Methods: GET

GET: Returns data of stakeholder.

**Response**

.. code-block:: Python

   {
    "id": "c7e459fc-95e4-41b6-b6f9-************",
    "user": {
        "name": <string>,
        "email": <string>
    },
    "executive_first_name": "Monica",
    "executive_last_name": "K",
    "phone": null,
    "mobile": "***********",
    "dynamic_table": "58718e97-cc50-4c8a-8ab4-************",
    "company_name": "CamelPort",
    "entity_type": null,
    "pan_number": null,
    "iec_code": null,
    "company_address_line_1": null,
    "company_address_line_2": null,
    "company_address_line_3": null,
    "city": null,
    "state": null,
    "country": null,
    "zipcode": null,
    "designation": null,
    "reg_status": 1,
    "quickbooks_customer": "115",
    "razor_pay": "va_AV7gAr806xpLAf",
    "helpscout_id": 195115971,
    "is_enabled": false
   }


**5.LoginView**

.. note:: API: "api/stakeholder/login/"

.. note:: Methods: POST

POST: Creates a new instance.

.. note:: These fields are mandatory.

**Request**

.. code-block:: Python

   {
     "password": <string>
     "email": <string>
   }

**Response**

.. code-block:: Python

   {
       "id": "ad0b3dc5-b121-43ea-9ed2-************",
       "user": {
           "name": null,
           "email": <string>
       },
       "executive_first_name": <string>,
       "executive_last_name": <string>,
       "phone": null,
       "mobile": <string>,
       "dynamic_table": "Shipper",
       "company_name": "abcd",
       "entity_type": null,
       "pan_number": null,
       "iec_code": null,
       "company_address_line_1": null,
       "company_address_line_2": null,
       "company_address_line_3": null,
       "city": null,
       "state": null,
       "country": null,
       "zipcode": null,
       "designation": null,
       "reg_status": 1,
       "quickbooks_customer": "810",
       "razor_pay": "va_B5Ruo2rc8LWWhb",
       "helpscout_id": 209353122,
       "is_enabled": false,
       "token": {
           "key": "706c1a35f8067eb44164cfffc***************"
       },
       "razor_account_number": "111222**********",
       "razor_ifsc_code": "RAZR0000001"
   }

**6.LoginView(admin)**

.. note:: API: "api/stakeholder/admin-login/"

.. note:: Method: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
     "password": <string>
     "email": <string>
   }

**7.GuestStakeholderView**

.. note:: API: "api/stakeholder/guest/"

.. note:: Methods: POST

POST: Creates a new instance.

**Request**

.. note:: These fields are mandatory.


.. code-block:: Python

   {
    "child_stakeholder": {
        "password1": "test",
        "password2": "test",
        "role": 1,
        "executive_first_name": "test",
        "user": {
            "email": "test@gmail.com"
        }
    }
   }

**Response**

.. code-block:: Python

   {
    "id": "f4869313-eb39-4b2e-a416-************",
    "child_stakeholder": {
        "executive_first_name": "test",
        "executive_last_name": null,
        "user": {
            "name": null,
            "email": "test@gmail.com"
        },
        "is_enabled": false
    }
   }

**8.GuestStakeholderListView**

.. note:: API: "api/stakeholder/guest-list/"

.. note:: Methods: GET

**Response**

.. code-block:: Python

    {
        "id": <string>,
        "user": {
            "name": <string>,
            "email": <string>
        },
        "executive_first_name": <string>,
        "executive_last_name": <string>,
        "phone": <string>,
        "mobile": <string>,
        "dynamic_table": <string>,
        "company_name": <string>,
        "entity_type": <int>,
        "pan_number": <string>,
        "iec_code": <string>,
        "company_address_line_1": <string>,
        "company_address_line_2": <string>,
        "company_address_line_3": <string>,
        "city": <string>,
        "state": <string>,
        "country": <string>,
        "zipcode": <int>,
        "designation": <int>,
        "reg_status": <int>,
        "quickbooks_customer": <string>,
        "razor_pay": <string>,
        "helpscout_id": <int>,
        "is_enabled": <boolean>
    }

**9.StakeholderRegStatusUpdateView**

.. note:: API: "api/stakeholder/reg-status/"

.. note:: Methods: PUT, PATCH

**Request**

.. code-block:: Python

  {
    "reg_status": 1,
    "is_enabled": false
  }


**Response**

.. code-block:: Python

   {
       "reg_status": 1,         <---- value changed
       "is_enabled": false
   }

Before:

.. code-block:: Python

  {
       "reg_status": 2,         <---- initial value is 2
       "is_enabled": false
   }

**10.BusinessEntityAutocompleteView**     ++++++++++pending

.. note:: API: "api/stakeholder/business-entity/autocomplete/"

.. note:: Methods: GET

**Response**

.. code-block:: Python


**11.SendOTPView**

.. note:: API: "api/stakeholder/send-otp/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "mobile": <string>
   }

**Response**

.. code-block:: Python

   {
       "message": "396171723347313936313830",
       "type": "success"
   }

**12.SendOTPEwayBillView**

.. note:: API: "api/stakeholder/send-otp/ewaybill/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "mobile": <string>
   }

**Response**

.. code-block:: Python

   {
       "message": "396171733059353239353737",
       "type": "success"
   }

**13.VerifyOTPView**

.. note:: API: "api/stakeholder/verify-otp/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "mobile": <string>
   }

**Response**

.. code-block:: Python

   {
       "message": "396171733059353239353737",
       "type": "success"
   }

**14.RetryOTPView**

.. note:: API: "api/stakeholder/retry-otp/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "mobile": <string>
   }

**Response**

.. code-block:: Python

   {
       "message": "otp_sent_successfully",
       "type": "success"
   }

**15.VerifyEmailView**

.. note:: API: "api/stakeholder/email-verify/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
     "email": <string>
   }

**Response**

.. code-block:: Python

   {
       "message": "Email verified successfully",
       "verified": true
   }

**16.Check_Is_EnabledView**

.. note:: API: "api/stakeholder/check_is_enabled/"

.. note:: Methods: GET

**Response**

.. code-block:: Python

   {
       "pricing_plan": 2
   }

**17.EWayBillGSTView**

.. note:: API: "api/stakeholder/ewaybill-gst/(?P<gst>[\w]+)/"

.. note:: Methods: GET

**Response**

.. code-block:: Python

   {
       "addrBnm": "",
       "addrBno": <string>,
       "__type": <string>,
       "CommonEnroll": "",
       "addrSt": <string>,
       "txpType": "",
       "cnOffCode": null,
       "tradeName": <string>,
       "gstin": <string>,
       "email": <string>,
       "addrPncd": "492099",
       "status": <string>,
       "addrLoc": <string>,
       "noOfAddlPlaces": null,
       "stOffCode": null,
       "addrFlno": "",
       "regType": null,
       "addrDst": null,
       "mobileNo": null,
       "stateCode": "22",
       "legalName": null,
       "tinNo": null,
       "addrStjd": null
   }

**18.inttra_auth_check**     +++++++++++pending

.. note:: API: "api/stakeholder/inttra/"

.. note:: Methods: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

**Response**

.. code-block:: Python

**19.itekseal_auth_check**                   ------pending (request)

.. note:: API: "api/stakeholder/itekseal/"

.. note:: Methods: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

**Response**

.. code-block:: Python

   {
       "ExceptionMessage": "Object reference not set to an instance of an object.",
       "StackTrace": "   at RSeal.BLL.BLL_Login.Auth_Post_ProcessLogin(Auth_Post_Login_Req req)\r\n   at RSeal.Controllers.AuthController.Post_Auth_Login(Auth_Post_Login_Req req)\r\n   at lambda_method(Closure , Object , Object[] )\r\n   at System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ActionExecutor.<>c__DisplayClass10.<GetExecutor>b__9(Object instance, Object[] methodParameters)\r\n   at System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ExecuteAsync(HttpControllerContext controllerContext, IDictionary`2 arguments, CancellationToken cancellationToken)\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Controllers.ApiControllerActionInvoker.<InvokeActionAsyncCore>d__0.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Controllers.ActionFilterResult.<ExecuteAsync>d__2.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Dispatcher.HttpControllerDispatcher.<SendAsync>d__1.MoveNext()",
       "Message": "An error has occurred.",
       "ExceptionType": "System.NullReferenceException"
   }

**20.odex_auth_check**                 ----------pending

.. note:: API: "api/stakeholder/odex/"

.. note:: Methods: POST

**Response**

.. code-block:: Python

**21.StakeholderZendeskView**              ------pending

.. note:: API: "api/stakeholder/zendesk/(?P<zendesk_id>[\d]+)/"

.. note:: Methods: GET

**Response**

.. code-block:: Python


**22.GuestStakeholderRUDView**

.. note:: API: "api/stakeholder/(?P<pk>[^/]+)/guest-rud/"

.. note:: Methods: GET, PUT, PATCH, DELETE

GET:

**Response**

.. code-block:: Python

   {
       "id": <string>,
       "user": {
           "name": <string>,
           "email": <string>
       },
       "executive_first_name": <string>,
       "executive_last_name": <string>,
       "phone": <string>,
       "mobile": <string>,
       "dynamic_table": <string>,
       "company_name": <string>,
       "entity_type": <int>,
       "pan_number": <string>,
       "iec_code": <string>,
       "company_address_line_1": <string>,
       "company_address_line_2": <string>,
       "company_address_line_3": <string>,
       "city": <string>,
       "state": <string>,
       "country": <string>,
       "zipcode": <int>,
       "designation": <int>,
       "reg_status": <int>,
       "quickbooks_customer": <string>,
       "razor_pay": <string>,
       "helpscout_id": <int>,
       "is_enabled": <boolean>
   }

PUT:

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

**Response**

.. code-block:: Python

PATCH:

**Request**

.. code-block:: Python

   {
       "executive_first_name": "test123"
   }

**Response**

BEFORE:

.. code-block:: Python

   {
       "id": "09c7a583-eb5f-402c-93b2-************",
       "user": {
           "name": null,
           "email": <string>
       },
       "executive_first_name": "test1",                   <---- initial value is test1
       "executive_last_name": null,
       "phone": null,
       "mobile": null,
       "dynamic_table": "e69974d9-67bf-4147-8968-************",
       "company_name": "abcd",
       "entity_type": null,
       "pan_number": null,
       "iec_code": null,
       "company_address_line_1": null,
       "company_address_line_2": null,
       "company_address_line_3": null,
       "city": null,
       "state": null,
       "country": null,
       "zipcode": null,
       "designation": null,
       "reg_status": 1,
       "quickbooks_customer": null,
       "razor_pay": null,
       "helpscout_id": null,
       "is_enabled": false
   }


AFTER:

.. code-block:: Python

   {
       "id": "09c7a583-eb5f-402c-93b2-************",
       "user": {
           "name": null,
           "email": <string>
       },
       "executive_first_name": "test123",                  <----- Updated to test123
       "executive_last_name": null,
       "phone": null,
       "mobile": null,
       "dynamic_table": "e69974d9-67bf-4147-8968-************",
       "company_name": "abcd",
       "entity_type": null,
       "pan_number": null,
       "iec_code": null,
       "company_address_line_1": null,
       "company_address_line_2": null,
       "company_address_line_3": null,
       "city": null,
       "state": null,
       "country": null,
       "zipcode": null,
       "designation": null,
       "reg_status": 1,
       "quickbooks_customer": null,
       "razor_pay": null,
       "helpscout_id": null,
       "is_enabled": false
   }

DELETE: Destroys the given ID.

**23.ChangePasswordRequestView**

.. note:: API: "api/stakeholder/password/forgot/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory.

.. code-block:: Python

   {
       "email": <string>
   }

**Response**

.. code-block:: Python

   {
       "status": "success"
   }

**24.ChangeStakeholderPasswordView**

.. note:: API: "api/stakeholder/password/reset/(?P<token>[a-zA-Z0-9_]*)/"

.. note:: Methods: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
    "password1": "old",
    "password2": "new"
   }

**Response**

.. code-block:: Python

   {
       "status": "success"
   }

**25.ChangeUserPasswordView**

.. note:: API: "api/stakeholder/userpassword/reset/"

.. note:: Methods: POST

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
    "password1": "old",
    "password2": "new"
   }

**Response**

.. code-block:: Python

   {
       "status": "success"
   }

**26.StakeholderInfoRetrieveAPIView**

.. note:: API: "api/stakeholder/info/"

.. note:: Methods: GET

**Response**

.. code-block:: Python

   {
       "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
       "rating": "0.00",
       "age_of_company_years": null,
       "house_bl": false,
       "response_time_hr": null
   }

**27.EmailVerifyView**

.. note:: API: "api/stakeholder/email-verification/"

.. note:: Methods: POST

**Request**

.. note:: This field is mandatory

.. code-block:: Python

   {
       "token": <string>
   }

**Response**

.. code-block:: Python

   {
       "status": "success"
   }
