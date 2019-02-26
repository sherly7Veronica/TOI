HUBS
++++

views
-----
.. automodule:: hubs.views

**HubsListCreateAPIView**

.. autoclass:: HubsListCreateAPIView
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

**HubsRetrieveUpdateDestroyAPIView**

.. autoclass:: HubsRetrieveUpdateDestroyAPIView
   :members:
   :undoc-members:
   :inherited-members:

**HubsDynamicValueRUDView**

.. autoclass:: HubsDynamicValueRUDView
   :members:
   :undoc-members:
   :inherited-members:

**HubsAutoCompleteListView**

.. autoclass:: HubsAutoCompleteListView
   :members:
   :undoc-members:
   :inherited-members:

**StakeholderHubListView**

.. autoclass:: StakeholderHubListView
   :members:
   :undoc-members:
   :inherited-members:

**CountryListView**

.. autoclass:: CountryListView
   :members:
   :undoc-members:
   :inherited-members:

**ActiveHubListView**

.. autoclass:: ActiveHubListView
   :members:
   :undoc-members:
   :inherited-members:

**HubsPortAutoCompleteListView**

.. autoclass:: HubsPortAutoCompleteListView
   :members:
   :undoc-members:
   :inherited-members:


models
------

.. automodule:: hubs.models

**Hubs**

.. autoclass:: Hubs
   :members:
   :inherited-members:

serializer
-----------

.. automodule:: hubs.serializer

**HubsSerializer**

.. autoclass:: HubsSerializer
   :members:
   :inherited-members:

**HubsShortSerializer**

.. autoclass:: HubsShortSerializer
   :members:
   :inherited-members:

**HubsNameSerializer**

.. autoclass:: HubsNameSerializer
   :members:
   :inherited-members:

**HubsAutoCompleteSerializer**

.. autoclass:: HubsAutoCompleteSerializer
   :members:
   :inherited-members:

**HubsPostContractSerializer**

.. autoclass:: HubsPostContractSerializer
   :members:
   :inherited-members:

**CitiesLightCountrySerializer**

.. autoclass:: CitiesLightCountrySerializer
   :members:
   :inherited-members:

urls
----

**1.HubsAutoCompleteListView**

.. note:: API: "api/hubs/autocomplete/"

.. note:: Methods: GET

GET: Returns list of all hubs with the corresponding search parameter value.

Example: **search = andheri** displays all the hubs of andheri.

**Response**

.. code-block:: Python

   {
     "id": "75d108bd-0d97-484a-9f4b-************",
     "name": "Andheri East",
     "country": "India",
     "stakeholder": "c7e459fc-95e4-41b6-b6f9-************",
     "type": "Factory"
   }

**2.HubsPortAutoCompleteListView**

.. note:: API: "api/hubs/autocomplete-ports/"

.. note:: Methods: GET

GET: Returns list of all hubs with the corresponding search parameter value.

Example: **search = P** displays all the hubs of andheri.

**Response**

.. code-block:: Python

   {
     "id": "fcca6ae8-377e-4d8f-82e4-************",
     "name": "Ningbo Pt",
     "country": "China",
     "stakeholder": null,
     "type": "Port"
   }

**3.HubsListCreateAPIView**

.. note:: API: "api/hubs/"

.. note:: Methods: GET, POST

GET: Returns list of all hubs.

**Response**

.. code-block:: Python

   {
     "id": <string>,
     "name": <string(64)>,
     "pan": <string(10)>,
     "address_country": <int>,
     "address_lat": <float>,
     "address_lng": <float>,
     "address_line_1": <string(256)>,
     "address_line_11": <string(256)>,
     "address_line_2": <string(256)>,
     "address_line_3": <string(256)>,
     "stakeholder": <string>,
     "dynamic_table": <string>,
     "address_state": <string(256)>,
     "address_zipcode": <string(10)>,
     "gst": <string(15)>
   }

POST: New hub is created with the below given data.

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
    "address_country": 38,
    "name": "test",
    "stakeholder": "",
    "gst": "",
    "address_line_3": ""
   }

**Response**

.. code-block:: Python

   {
     "id": "3f38aa69-eea4-457d-bc2a-************",
     "name": "",
     "pan": null,
     "address_country": 38,
     "address_lat": "37.994287600000000000",
     "address_lng": "-122.303601000000000000",
     "address_line_1": null,
     "address_line_11": null,
     "address_line_2": null,
     "address_line_3": "",
     "stakeholder": "c7e459fc-95e4-41b6-b6f9-************",
     "dynamic_table": "24fe6492-e1ce-4201-a4fa-************",
     "address_state": null,
     "address_zipcode": null,
     "gst": ""
   }

**4.HubsDynamicValueRUDView**

.. note:: API: "api/hubs/"

.. note:: Methods: GET, PUT, PATCH, DELETE

GET: Returns list of all hubs.

**Response**

.. code-block:: Python


POST: New hub is created with the below given data.

**Request**

.. code-block:: Python


.. note:: All fields are mandatory.


**Response**

.. code-block:: Python


**5.StakeholderHubListView**

.. note:: API: "api/hubs/factories/"

.. note:: Methods: GET

GET: Returns list of all hubs.

**Response**

.. code-block:: Python

    {
     "id": <string>,
     "name": <string(64)>,
     "pan": <string(10)>,
     "address_country": <int>,
     "address_lat": <float>,
     "address_lng": <float>,
     "address_line_1": <string(256)>,
     "address_line_11": <string(256)>,
     "address_line_2": <string(256)>,
     "address_line_3": <string(256)>,
     "stakeholder": <string>,
     "dynamic_table": <string>,
     "address_state": <string(256)>,
     "address_zipcode": <string(10)>,
     "gst": <string(15)>
    }
    so on....

**6.CountryListView**

.. note:: API: "api/hubs/countries/"

.. note:: Methods: GET

GET: Returns list of all countries.

**Response**

.. code-block:: Python

   {
     "id": <int>,
     "name": "Afghanistan",
     "mobile_country_code": "++93"
   }

**7.ActiveHubListView**

.. note:: API: "api/hubs/active/"

.. note:: Methods: GET

GET: Returns list of all active hubs.

.. code-block:: Python

   {
     "id": <string>,
     "name": <string(64)>,
     "pan": <string(10)>,
     "address_country": <int>,
     "address_lat": <float>,
     "address_lng": <float>,
     "address_line_1": <string(256)>,
     "address_line_11": <string(256)>,
     "address_line_2": <string(256)>,
     "address_line_3": <string(256)>,
     "stakeholder": <string>,
     "dynamic_table": <string>,
     "address_state": <string(256)>,
     "address_zipcode": <string(10)>,
     "gst": <string(15)>
   }

**8.HubsRetrieveUpdateDestroyAPIView**

.. note:: API: "api/hubs/(?P<pk>[^/]+)/"

.. note:: Methods: GET, PUT, PATCH, DELETE.

GET: Returns list of all hubs.

PUT: Updates the data of the particular id with the below given data.

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
      "address_country": "6",
      "name": "India",
      "stakeholder": <string>,
      "gst": "dcba"
   }


**Response**

.. note:: 1. The address_country updated from **38** to **6**.
          2. The name updated from **Albania** to **India**.
          3. The stakeholder updated from **id** to **null** as we did not specify any data.
          4. The gst updated from **abcd** to **dcba** as shown below.

Before:

.. code-block:: Python

  {
     "id": <string>,
     "name": "Albania",
     "pan": <string(10)>,
     "address_country": 38,
     "address_lat": <float>,
     "address_lng": <float>,
     "address_line_1": <string(256)>,
     "address_line_11": <string(256)>,
     "address_line_2": <string(256)>,
     "address_line_3": <string(256)>,
     "stakeholder": "a4590179-498c-4146-960c-************",
     "dynamic_table": <string>,
     "address_state": <string(256)>,
     "address_zipcode": <string(10)>,
     "gst": "abcd"
   }

After:

.. code-block:: Python

 {
     "id": <string>,
     "name": "India",
     "pan": <string(10)>,
     "address_country": 6,
     "address_lat": <float>,
     "address_lng": <float>,
     "address_line_1": <string(256)>,
     "address_line_11": <string(256)>,
     "address_line_2": <string(256)>,
     "address_line_3": <string(256)>,
     "stakeholder": null,
     "dynamic_table": <string>,
     "address_state": <string(256)>,
     "address_zipcode": <string(10)>,
     "gst": "dcba"
   }

PATCH: Modifies the existing data.

DELETE: Destroys the given id.
