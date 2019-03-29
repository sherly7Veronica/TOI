ASSETS
------

views
+++++

.. automodule:: assets.views


**AssetsListCreateAPIView**

.. autoclass:: AssetsListCreateAPIView
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

**AssetsRetrieveUpdateDestroyAPIView**

.. autoclass:: AssetsRetrieveUpdateDestroyAPIView
   :members:
   :undoc-members:
   :inherited-members:

**AssetsDynamicValueRetrieveUpdateDestroyView**

.. autoclass:: AssetsDynamicValueRetrieveUpdateDestroyView
   :members:
   :undoc-members:
   :inherited-members:

**AssetsListAPIView**

.. autoclass:: AssetsListAPIView
   :members:
   :undoc-members:
   :inherited-members:

**TrackingRetrieveAPIView**

.. autoclass:: TrackingRetrieveAPIView
   :members:
   :undoc-members:
   :inherited-members:

**MarineTrackingView**

.. autoclass:: MarineTrackingView
   :members:
   :undoc-members:
   :inherited-members:

models
++++++

.. automodule:: assets.models

**Assets**

.. autoclass:: Assets
   :members:
   :inherited-members:

**MyEavConfigClass**

.. autoclass:: MyEavConfigClass
   :members:
   :inherited-members:

**ContainerTracking**

.. autoclass:: ContainerTracking
   :members:
   :inherited-members:

**TrackingEvent**

.. autoclass:: TrackingEvent
   :members:
   :inherited-members:

**FreightCarrier**

.. autoclass:: FreightCarrier
   :members:
   :inherited-members:

serializer
+++++++++++

.. automodule:: assets.serializer

**AssetsSerializer**

.. autoclass:: AssetsSerializer
   :members:
   :inherited-members:

**AssetsPostContractSerializer**

.. autoclass:: AssetsPostContractSerializer
   :members:
   :inherited-members:

**AssetsListSerializer**

.. autoclass:: AssetsListSerializer
   :members:
   :inherited-members:

**TrackingEventSerializer**

.. autoclass:: TrackingEventSerializer
   :members:
   :inherited-members:

**TrackingSerializer**

.. autoclass:: TrackingSerializer
   :members:
   :inherited-members:

urls
++++

**1.AssetsListCreateAPIView**

.. note:: API: "api/assets/"

.. note:: Methods: GET, POST

GET: Returns list of all assets.

POST: New asset is created with the below given data.

**Request**

.. code-block:: Python

   {
    "identifier": <string>
   }

.. note:: This field is mandatory.


**Response**

.. code-block:: Python

 {
  "id": <string>,
  "identifier": <string>,
  "length": <string>,
  "length_unit": <int>,
  "width": <string>,
  "width_unit": <int>,
  "height": <string>,
  "height_unit": <int>,
  "weight": <string>,
  "weight_unit": <int>,
  "is_dimension_constant": <boolean>,
  "is_weight_constant": <boolean>,
  "dynamic_table": <string>
   }


**2.AssetsRetrieveUpdateDestroyAPIView**

.. note:: API: "api/assets/(?P<pk>[^/]+)/"

.. note:: Methods: GET, PUT, PATCH, DELETE.

GET: Returns details of the given id.

PUT: Updates the data of the particular id with the below given data.

**Request**

.. code-block:: Python

   {
    "identifier": "40' GP"
   }

.. note:: This field is mandatory.

**Response**

.. code-block:: Python

 {
  "id": <string>,
  "identifier": "40' GP",
  "length": <string>,
  "length_unit": <int>,
  "width": <string>,
  "width_unit": <int>,
  "height": <string>,
  "height_unit": <int>,
  "weight": <string>,
  "weight_unit": <int>,
  "is_dimension_constant": <boolean>,
  "is_weight_constant": <boolean>,
  "dynamic_table": <string>
   }

.. note:: The identifier updated from 20' HC to 40'GP as shown below.

Before:

.. code-block:: Python

 {
  "id": <string>,
  "identifier": "20' HC",
  "length": <string>,
  "length_unit": <int>,
  "width": <string>,
  "width_unit": <int>,
  "height": <string>,
  "height_unit": <int>,
  "weight": <string>,
  "weight_unit": <int>,
  "is_dimension_constant": <boolean>,
  "is_weight_constant": <boolean>,
  "dynamic_table": <string>
   }

After:

.. code-block:: Python

 {
  "id": <string>,
  "identifier": "40' GP",
  "length": <string>,
  "length_unit": <int>,
  "width": <string>,
  "width_unit": <int>,
  "height": <string>,
  "height_unit": <int>,
  "weight": <string>,
  "weight_unit": <int>,
  "is_dimension_constant": <boolean>,
  "is_weight_constant": <boolean>,
  "dynamic_table": <string>
   }

PATCH: Modifies the existing data.

DELETE: Destroys the given id.

**3.AssetsDynamicValueRetrieveUpdateDestroyView**

.. note:: API: "api/assets/assetsDynamicRUD/(?P<pk>[^/]+)/"

.. note:: Methods: GET, PUT, PATCH, DELETE.

GET: Returns list of all assets.

PUT: Asset is updated with the below given data.

**Request**

.. code-block:: Python

   {
    "identifier": "20' HT"
   }

.. note:: This field is mandatory.


**Response**

.. code-block:: Python

 {
  "id": <string>,
  "identifier": "20' HT",
  "length": <string>,
  "length_unit": <int>,
  "width": <string>,
  "width_unit": <int>,
  "height": <string>,
  "height_unit": <int>,
  "weight": <string>,
  "weight_unit": <int>,
  "is_dimension_constant": <boolean>,
  "is_weight_constant": <boolean>,
  "dynamic_table": <string>
   }

PATCH: Modifies the existing data.

DELETE: Destroys the given id.

**4.AssetsListAPIView**

.. note:: API: "api/assets/fulllist/"

.. note:: Method: GET

GET: Returns the full list of all assets.

**Response**

.. code-block:: Python

   [
    {
     "id": <string>,
     "identifier": <string>,
     "length": <string>,
     "length_unit": <int>,
     "width": <string>,
     "width_unit": <int>,
     "height": <string>,
     "height_unit": <int>,
     "weight": <string>,
     "weight_unit": <int>,
     "is_dimension_constant": <boolean>,
     "is_weight_constant": <boolean>,
     "dynamic_table": <string>
      },

    {
     "id": <string>,
     "identifier": <string>,
     "length": <string>,
     "length_unit": <int>,
     "width": <string>,
     "width_unit": <int>,
     "height": <string>,
     "height_unit": <int>,
     "weight": <string>,
     "weight_unit": <int>,
     "is_dimension_constant": <boolean>,
     "is_weight_constant": <boolean>,
     "dynamic_table": <string>
      }
      ]

so on..

**5.TrackingRetrieveAPIView**

.. note:: API: "api/assets/container-no/(?P<container_no>[^/]+)/"

.. note:: Method: GET

**Response**

.. code-block:: Python

   {
     "container_no": "CAIU7237212",
     "tracking_events": [
       {
         "time": "2018-07-26T00:30:00Z",
         "details": <string>,
         "particulars": <string>,
         "css_selector": <int>
       },
       {
         "time": "2018-08-11T14:30:00Z",
         "details": <string>,
         "particulars": <string>,
         "css_selector": <int>
       },
       {
         "time": "2018-09-05T20:30:00Z",
         "details": <string>,
         "particulars": <string>,
         "css_selector": <int>
       }
     ]
   }

**6.MarineTrackingView**

.. note:: API: "api/assets/marine-tracking/"

.. note:: Method: POST

