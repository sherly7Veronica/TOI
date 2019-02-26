QUOTES
------

views
+++++

.. automodule:: quote.views

**QuoteCreateView**

.. autoclass:: QuoteCreateView
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

**QuoteListView**

.. autoclass:: QuoteListView
   :members:
   :undoc-members:
   :inherited-members:

**QuoteRUDView**

.. autoclass:: QuoteRUDView
   :members:
   :undoc-members:
   :inherited-members:

**RouteSelectionUpdateView**

.. autoclass:: RouteSelectionUpdateView
   :members:
   :undoc-members:
   :inherited-members:

**QuoteSelectedRouteLegsView**

.. autoclass:: QuoteSelectedRouteLegsView
   :members:
   :undoc-members:
   :inherited-members:

**QuoteLegListCreateView**

.. autoclass:: QuoteLegListCreateView
   :members:
   :undoc-members:
   :inherited-members:

**QuoteRatesListView**

.. autoclass:: QuoteRatesListView
   :members:
   :undoc-members:
   :inherited-members:

**VendorQuoteRequirementListView**

.. autoclass:: VendorQuoteRequirementListView
   :members:
   :undoc-members:
   :inherited-members:

**VendorDashboard**

.. autoclass:: VendorDashboard
   :members:
   :undoc-members:
   :inherited-members:

**QuoteRetrieveUpdateDestroyAPIView**

.. autoclass:: QuoteRetrieveUpdateDestroyAPIView
   :members:
   :undoc-members:
   :inherited-members:

**AllQuoteListView**

.. autoclass:: AllQuoteListView
   :members:
   :undoc-members:
   :inherited-members:

models
++++++

.. automodule:: quote.models

**Quote**

.. autoclass:: Quote
   :members:
   :inherited-members:

**Leg**

.. autoclass:: Leg
   :members:
   :inherited-members:

serializer
+++++++++++

.. automodule:: quote.serializers

**LegsSerializer**

.. autoclass:: LegsSerializer
   :members:
   :inherited-members:

**RouteSelectionLegSerializer**

.. autoclass:: RouteSelectionLegSerializer
   :members:
   :inherited-members:

**RouteSelectionQuoteSerializer**

.. autoclass:: RouteSelectionQuoteSerializer
   :members:
   :inherited-members:

**QuoteSerializer**

.. autoclass:: QuoteSerializer
   :members:
   :inherited-members:

**QuoteListSerializer**

.. autoclass:: QuoteListSerializer
   :members:
   :inherited-members:

**QuoteDetailSerializer**

.. autoclass:: QuoteDetailSerializer
   :members:
   :inherited-members:

**QuoteUnConfirmedBookingDetailSerializer**

.. autoclass:: QuoteUnConfirmedBookingDetailSerializer
   :members:
   :inherited-members:

**QuoteSelectedRouteLegsSerializer**

.. autoclass:: QuoteSelectedRouteLegsSerializer
   :members:
   :inherited-members:

**LegWithNoOfContainersSerializer**

.. autoclass:: LegWithNoOfContainersSerializer
   :members:
   :inherited-members:

**QuoteRatesSerializer**

.. autoclass:: QuoteRatesSerializer
   :members:
   :inherited-members:

**VendorQuoteRequirementListSerializer**

.. autoclass:: VendorQuoteRequirementListSerializer
   :members:
   :inherited-members:

urls
++++

**1.ExcelQuoteAPIView** +++++++++++++++pending

.. note:: API: "api/quote/quote-excel/"

.. note:: Methods: POST

POST: Creates a new quote.


**Response**

.. code-block:: Python

**2.ExcelQuoteRequestView**   ++++++++++++++ pending

.. note:: API: "api/quote/excel-request/"

.. note:: Methods: POST

POST: Creates a new quote.

**Response**

.. code-block:: Python


**3.QuoteCreateView**

.. note:: API: "api/quote/"

.. note:: Methods: POST

POST: New quote is created with the below given data.

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
      "source": <string>,
      "no_of_containers": <int>,
      "destination": <string>,
      "for_date": <timestamp>
   }

**Response**

.. code-block:: Python

   {
     "id": "04655a00-ef69-443b-b59c-************",
     "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
     "source": "932c0a37-87a0-47d4-8d1a-************",
     "destination": "0c7cf0d9-083e-4a23-a668-************",
     "asset": null,
     "for_date": "2019-01-31T17:08:00+05:30",
     "for_date_choices": 1,
     "weight": null,
     "no_of_containers": 77,
     "include_cha": true,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "legs": [
       {
         "id": "a2010ae4-7c3d-4bb3-b5ca-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 1,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Sunny Point to Bar <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-24T11:20:00Z",
         "vessel_name": null
       },
       {
         "id": "801df2b1-49ef-4766-afed-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-53c562aff0f3",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-53c562aff0f3",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 2,
         "route_num": 1,
         "start_date": "2019-01-31T11:38:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Bar to Sunny Point <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-30T11:38:00Z",
         "vessel_name": null
       }
     ],
     "num_routes": 1,
     "helpscout_id": 22998****,
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "billing_address": null,
     "quickbooks_id": null,
     "cargo_description": null
   }

**4.QuoteListView**

.. note:: API: "api/quote/list/"

.. note:: Methods: GET

GET: Returns the list of all quotes.

**Response**

.. code-block:: Python

   {
     "count": 2,
     "current_page": 1,
     "num_pages": 1,
     "results": [
       {
         "id": "4a1e8ca3-9b39-4c64-8618-************",
         "stakeholder": {
           "id": "ad0b3dc5-b121-43ea-9ed2-************",
           "user": {
             "name": null,
             "email": "************@gmail.com"
           },
           "executive_first_name": "veronica",
           "executive_last_name": "sherly",
           "phone": null,
           "mobile": "************",
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
           "designation": null
         },
         "source": {
           "id": "673042e6-d147-4923-8cf0-************",
           "name": "Andheri East",
           "pan": null,
           "address_country": 105,
           "address_lat": "19.035882300000000811",
           "address_lng": "72.924652100000002974",
           "address_line_1": "404, SATELLITE GAZEBO, 4th floor",
           "address_line_11": null,
           "address_line_2": "WEST WING ANDHERI GHATKOPAR LINK ROAD",
           "address_line_3": "ANDHERI EAST",
           "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
           "dynamic_table": "96106ae7-4c93-4de3-a7f2-************",
           "address_state": "MAHARASTRA",
           "address_zipcode": "400094"
         },
         "destination": {
           "id": "b28bbf16-6005-4bc4-9e78-************",
           "name": "Nhava Sheva",
           "pan": null,
           "address_country": 105,
           "address_lat": "18.951666666666664440",
           "address_lng": "72.949722222222220580",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": "Maharashtra",
           "address_zipcode": null
         },
         "asset": {
           "id": "d34f8937-189f-4740-8666-************",
           "identifier": "20' GP",
           "length": "20.00",
           "length_unit": 2,
           "width": "8.00",
           "width_unit": 2,
           "height": "8.50",
           "height_unit": 2,
           "weight": "4810.00",
           "weight_unit": 2,
           "is_dimension_constant": false,
           "is_weight_constant": false,
           "dynamic_table": "ab3dd0c5-3389-4c18-b104-************"
         },
         "for_date": "2018-12-30T17:12:57.386724Z",
         "for_date_choices": 1,
         "weight": "2.00",
         "no_of_containers": 1,
         "include_cha": false,
         "is_dock_stuffing": false,
         "stuffing_duration": 1440,
         "helpscout_id": 226*****,
         "selected_route_num": 1,
         "quote_number": "CPQ-******",
         "rate_currency": null,
         "cargo_description": "asdasd",
         "status": 0
       },
       {
         "id": "04655a00-ef69-443b-b59c-************",
         "stakeholder": {
           "id": "ad0b3dc5-b121-43ea-9ed2-************",
           "user": {
             "name": null,
             "email": "************@gmail.com"
           },
           "executive_first_name": "veronica",
           "executive_last_name": "sherly",
           "phone": null,
           "mobile": "************",
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
           "designation": null
         },
         "source": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "destination": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "asset": null,
         "for_date": "2019-01-31T11:38:00Z",
         "for_date_choices": 1,
         "weight": null,
         "no_of_containers": 77,
         "include_cha": true,
         "is_dock_stuffing": false,
         "stuffing_duration": 1440,
         "helpscout_id": 2299*****,
         "selected_route_num": null,
         "quote_number": "CPQ-******",
         "rate_currency": null,
         "cargo_description": null,
         "status": 0
       }
     ],
     "links": {
       "previous": null,
       "next": null
     }
   }

**5.VendorQuoteRequirementListView**

.. note:: API: "api/quote/vendorlist/"

.. note:: Methods: GET

GET: Returns all quotes of the vendor.

**Response**

.. code-block:: Python

   {"result": [ {
     "id": "d157756c-747d-4f2b-8637-************",
     "asset": {
       "id": "f35a6272-ddd9-4442-956d-************",
       "identifier": "40 OT",
       "length": "40.00",
       "length_unit": 2,
       "width": "8.00",
       "width_unit": 2,
       "height": "8.50",
       "height_unit": 2,
       "weight": "8550.00",
       "weight_unit": 2,
       "is_dimension_constant": false,
       "is_weight_constant": false,
       "dynamic_table": "ab3dd0c5-3389-4c18-b104-************"
     },
     "mode": {
       "id": "669d0d02-bb2c-427a-8722-************",
       "name": "Ocean"
     },
     "for_date": "2019-01-18T18:30:00Z",
     "for_date_choices": 1,
     "weight": "5.00",
     "no_of_containers": 5,
     "include_cha": false,
     "is_dock_stuffing": false,
     "stuffing_duration": 2880,
     "grouped_legs": {
       "min_rate_currency": "INR",
       "is_import": null,
       "min_rate_service_provider": "f9b8a8a4-836e-4e72-aba9-************",
       "hub_list": [
         {
           "id": "b28bbf16-6005-4bc4-9e78-************",
           "name": "Nhava Sheva",
           "pan": null,
           "address_country": 105,
           "address_lat": "18.951666666666664440",
           "address_lng": "72.949722222222220580",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": "Maharashtra",
           "address_zipcode": null
         },
         {
           "id": "5e960931-4308-479a-9ba1-************",
           "name": "Colombo",
           "pan": null,
           "address_country": 131,
           "address_lat": "6.916666666666666963",
           "address_lng": "79.849999999999994316",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": null,
           "address_zipcode": null
         }
       ],
       "min_rate": 78940,
       "start_date": "2019-01-22T18:30:00Z",
       "quoted_rate": null
     },
     "quote_number": "CPQ-TS87TR",
     "rate_currency": null,
     "cargo_description": "jhjhjhj"
   }
   -1 {
     "id": "d157756c-747d-4f2b-8637-************",
     "asset": {
       "id": "f35a6272-ddd9-4442-956d-************",
       "identifier": "40 OT",
       "length": "40.00",
       "length_unit": 2,
       "width": "8.00",
       "width_unit": 2,
       "height": "8.50",
       "height_unit": 2,
       "weight": "8550.00",
       "weight_unit": 2,
       "is_dimension_constant": false,
       "is_weight_constant": false,
       "dynamic_table": "ab3dd0c5-3389-4c18-b104-************"
     },
     "mode": {
       "id": "669d0d02-bb2c-427a-8722-************",
       "name": "Ocean"
     },
     "for_date": "2019-01-18T18:30:00Z",
     "for_date_choices": 1,
     "weight": "5.00",
     "no_of_containers": 5,
     "include_cha": false,
     "is_dock_stuffing": false,
     "stuffing_duration": 2880,
     "grouped_legs": {
       "min_rate_currency": "INR",
       "is_import": null,
       "min_rate_service_provider": "f9b8a8a4-836e-4e72-aba9-************",
       "hub_list": [
         {
           "id": "b28bbf16-6005-4bc4-9e78-************",
           "name": "Nhava Sheva",
           "pan": null,
           "address_country": 105,
           "address_lat": "18.951666666666664440",
           "address_lng": "72.949722222222220580",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": "Maharashtra",
           "address_zipcode": null
         },
         {
           "id": "5e960931-4308-479a-9ba1-************",
           "name": "Colombo",
           "pan": null,
           "address_country": 131,
           "address_lat": "6.916666666666666963",
           "address_lng": "79.849999999999994316",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": null,
           "address_zipcode": null
         }
       ],
       "min_rate": 78940,
       "start_date": "2019-01-22T18:30:00Z",
       "quoted_rate": null
     },
     "quote_number": "CPQ-TS87TR",
     "rate_currency": null,
     "cargo_description": "jhjhjhj"
   }
   -2 {
     "id": "d157756c-747d-4f2b-8637-************",
     "asset": {
       "id": "f35a6272-ddd9-4442-956d-************",
       "identifier": "40 OT",
       "length": "40.00",
       "length_unit": 2,
       "width": "8.00",
       "width_unit": 2,
       "height": "8.50",
       "height_unit": 2,
       "weight": "8550.00",
       "weight_unit": 2,
       "is_dimension_constant": false,
       "is_weight_constant": false,
       "dynamic_table": "ab3dd0c5-3389-4c18-b104-************"
     },
     "mode": {
       "id": "669d0d02-bb2c-427a-8722-71126b11c7a3",
       "name": "Ocean"
     },
     "for_date": "2019-01-18T18:30:00Z",
     "for_date_choices": 1,
     "weight": "5.00",
     "no_of_containers": 5,
     "include_cha": false,
     "is_dock_stuffing": false,
     "stuffing_duration": 2880,
     "grouped_legs": {
       "min_rate_currency": "INR",
       "is_import": null,
       "min_rate_service_provider": "f9b8a8a4-836e-4e72-aba9-************",
       "hub_list": [
         {
           "id": "b28bbf16-6005-4bc4-9e78-************",
           "name": "Nhava Sheva",
           "pan": null,
           "address_country": 105,
           "address_lat": "18.951666666666664440",
           "address_lng": "72.949722222222220580",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": "Maharashtra",
           "address_zipcode": null
         },
         {
           "id": "5e960931-4308-479a-9ba1-************",
           "name": "Colombo",
           "pan": null,
           "address_country": 131,
           "address_lat": "6.916666666666666963",
           "address_lng": "79.849999999999994316",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "a4590179-498c-4146-960c-************",
           "address_state": null,
           "address_zipcode": null
         }
       ],
       "min_rate": 78940,
       "start_date": "2019-01-22T18:30:00Z",
       "quoted_rate": null
     },
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "cargo_description": "jhjhjhj"
   ]
   }

   so on ...

**6.QuoteRetrieveUpdateDestroyAPIView**

.. note:: API: "api/quote/(?P<pk>[^/]+)/quote-retupdatedel/"

.. note:: Methods: GET, PUT, PATCH, DELETE

GET: Returns list of all quotes.

PUT: Quote of the particular id is updated with the below given data.

.. note:: These fields are mandatory.

.. code-block:: Python

   {
   "source": <string>,
   "no_of_containers": <int>,
   "destination": <string>,
   "for_date": <timestamp>
   }

**Request**

.. code-block:: Python

   {
    "source": <string>,
    "no_of_containers": <int>,
    "destination": <string>,
    "for_date": <timestamp>,
    "weight": 30
   }


**Response**

.. code-block:: Python

   {
     "id": "04655a00-ef69-443b-b59c-************",
     "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
     "source": "932c0a37-87a0-47d4-8d1a-************",
     "destination": "0c7cf0d9-083e-4a23-a668-************",
     "asset": null,
     "for_date": "2019-01-24T11:20:00Z",
     "for_date_choices": 1,
     "weight": "30.00",
     "no_of_containers": 88,
     "include_cha": true,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "legs": [
       {
         "id": "a2010ae4-7c3d-4bb3-b5ca-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 1,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 1440,
         "rate": 143201,
         "delay": 0,
         "description_text": "Sunny Point to Bar <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-24T11:20:00Z",
         "vessel_name": null
       },
       {
         "id": "801df2b1-49ef-4766-afed-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 2,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 1440,
         "rate": 143201,
         "delay": 0,
         "description_text": "Bar to Sunny Point <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-30T11:38:00Z",
         "vessel_name": null
       }
     ],
     "num_routes": 1,
     "helpscout_id": *********,
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "billing_address": null,
     "quickbooks_id": null,
     "cargo_description": null
   }

Before

.. note:: The weight has been changed from **null** to **30**.

.. code-block:: Python

   {
     "id": "04655a00-ef69-443b-b59c-************",
     "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
     "source": "932c0a37-87a0-47d4-8d1a-************",
     "destination": "0c7cf0d9-083e-4a23-a668-************",
     "asset": null,
     "for_date": "2019-01-24T11:20:00Z",
     "for_date_choices": 1,
     "weight": null,                         <---- weight is null
     "no_of_containers": 88,
     "include_cha": true,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "legs": [
       {
         "id": "a2010ae4-7c3d-4bb3-b5ca-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 1,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 1440,
         "rate": 143201,
         "delay": 0,
         "description_text": "Sunny Point to Bar <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-24T11:20:00Z",
         "vessel_name": null
       },
       {
         "id": "801df2b1-49ef-4766-afed-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 2,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 1440,
         "rate": 143201,
         "delay": 0,
         "description_text": "Bar to Sunny Point <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-30T11:38:00Z",
         "vessel_name": null
       }
     ],
     "num_routes": 1,
     "helpscout_id": *********,
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "billing_address": null,
     "quickbooks_id": null,
     "cargo_description": null
   }

**8.RouteSelectionUpdateView**   +++++++++++++++=pending

.. note:: API: "api/quote/(?P<pk>[^/]+)/select-route/"

.. note:: Methods: PUT, PATCH

PUT: Updates the data of the particular id with the below given data.

**Request**

.. code-block:: Python


.. note:: This field is mandatory.


**Response**

.. code-block:: Python


PATCH: Modifies the existing data.

**9.QuoteSelectedRouteLegsView**

.. note:: API: "api/quote/(?P<pk>[^/]+)/selected-route/"

.. note:: Methods: GET

GET: Returns the data of the given id.

**Response**

.. code-block:: Python

   {
     "id": "04655a00-ef69-443b-b59c-************",
     "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
     "source": "932c0a37-87a0-47d4-8d1a-************",
     "destination": "0c7cf0d9-083e-4a23-a668-************",
     "asset": null,
     "for_date": "2019-01-31T17:08:00+05:30",
     "for_date_choices": 1,
     "weight": null,
     "no_of_containers": 88,
     "include_cha": true,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "legs": [
       {
         "id": "a2010ae4-7c3d-4bb3-b5ca-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 1,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Sunny Point to Bar <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-24T11:20:00Z",
         "vessel_name": null
       },
       {
         "id": "801df2b1-49ef-4766-afed-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 2,
         "route_num": 1,
         "start_date": "2019-01-31T11:38:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Bar to Sunny Point <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-30T11:38:00Z",
         "vessel_name": null
       }
     ],
     "num_routes": 1,
     "helpscout_id": 229******,
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "billing_address": null,
     "quickbooks_id": null,
     "cargo_description": null
   }

**10.QuoteRatesListView**

.. note:: API: "api/quote/(?P<pk>[^/]+)/rates/"

.. note:: Methods: GET

GET: Returns the data of the given id.

**Response**

.. code-block:: Python

   {
     "id": "9c61a9a3-142e-4b01-bd85-540509ec743a",
     "stakeholder": "fa9c60a8-1cf0-4b68-a55f-c0192386e494",
     "source": "b28bbf16-6005-4bc4-9e78-6216156e3852",
     "destination": "5d0743fb-95ab-482f-9ff9-85133cb0212f",
     "asset": {
       "id": "d34f8937-189f-4740-8666-2cbd595abe2f",
       "identifier": "20' GP",
       "length": "20.00",
       "length_unit": 2,
       "width": "8.00",
       "width_unit": 2,
       "height": "8.50",
       "height_unit": 2,
       "weight": "4810.00",
       "weight_unit": 2,
       "is_dimension_constant": false,
       "is_weight_constant": false,
       "dynamic_table": "ab3dd0c5-3389-4c18-b104-1d491bec7f57"
     },
     "for_date": "2019-01-02T18:30:00Z",
     "for_date_choices": 1,
     "weight": "4.00",
     "no_of_containers": 1,
     "include_cha": false,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "rate_legs": [
       {
         "legs": [
           {
             "id": "01d34ad0-c232-44e3-b231-44ce1a34767f",
             "mode": {
               "id": "669d0d02-bb2c-427a-8722-71126b11c7a3",
               "is_tracking_enabled": false,
               "tracking_method": 7,
               "dynamic_table": {
                 "id": "5abf419f-a5ae-4c42-a149-c1dd751b86ed",
                 "table_name": "Ocean"
               }
             },
             "fromHub": {
               "id": "b28bbf16-6005-4bc4-9e78-6216156e3852",
               "name": "Nhava Sheva",
               "pan": null,
               "address_country": 105,
               "address_lat": "18.951666666666664440",
               "address_lng": "72.949722222222220580",
               "address_line_1": null,
               "address_line_11": null,
               "address_line_2": null,
               "address_line_3": null,
               "stakeholder": null,
               "dynamic_table": "a4590179-498c-4146-960c-f15f813428c2",
               "address_state": "Maharashtra",
               "address_zipcode": null
             },
             "toHub": {
               "id": "5d0743fb-95ab-482f-9ff9-85133cb0212f",
               "name": "Jebel Ali",
               "pan": null,
               "address_country": 2,
               "address_lat": "24.995833333333333570",
               "address_lng": "55.059444444444444855",
               "address_line_1": null,
               "address_line_11": null,
               "address_line_2": null,
               "address_line_3": null,
               "stakeholder": null,
               "dynamic_table": "a4590179-498c-4146-960c-f15f813428c2",
               "address_state": null,
               "address_zipcode": null
             },
             "leg_num": 1,
             "route_num": 7,
             "start_date": "2019-01-02T18:30:00Z",
             "duration": 10080,
             "rate": 10000,
             "delay": 0,
             "description_text": "Nhava Sheva to Jebel Ali <br /><b>Gate In Cutoff</b>: 01/01/2019<br/><b>Vessel Date</b>: 03/01/2019<br/><b>Vessel</b>: HYUNDAI FORCE - BERMUDA",
             "is_import": null,
             "rate_currency": null,
             "is_active": false,
             "arrival_date": "2018-12-30T18:30:00Z",
             "vessel_name": "HYUNDAI FORCE - BERMUDA"
           }
         ],
         "rates": [
           {
             "id": "38d68d7b-c1ec-4e35-96cf-3975450dc802",
             "is_return": false,
             "provider_rate": 419,
             "provided_rate": 419,
             "tax": "4d1e7975-8c0c-4f03-91c9-afae63a936af",
             "mode": "669d0d02-bb2c-427a-8722-71126b11c7a3",
             "asset": "d34f8937-189f-4740-8666-2cbd595abe2f",
             "weight": "4.00",
             "num_assets": 1,
             "used_assets": 0,
             "rate_for_date": "2019-01-02T18:30:00Z",
             "rate_type": 0,
             "service_provider": {
               "id": "c7e459fc-95e4-41b6-b6f9-32089c9f517c",
               "executive_first_name": "Rajan",
               "executive_last_name": "Gupta",
               "company_name": "CamelPort",
               "user": {
                 "name": null,
                 "email": "pranali06patil+for@gmail.com"
               },
               "is_enabled": false,
               "info": {
                 "stakeholder": "c7e459fc-95e4-41b6-b6f9-32089c9f517c",
                 "rating": "0.00",
                 "age_of_company_years": null,
                 "house_bl": false,
                 "response_time_hr": null
               }
             },
             "for_stakeholder": null,
             "rate_expiry_date": "2019-01-09T18:30:00Z",
             "hub_list": [
               {
                 "id": "c5a43654-a983-4cb3-b130-46725874da36",
                 "hub": {
                   "id": "b28bbf16-6005-4bc4-9e78-6216156e3852",
                   "name": "Nhava Sheva",
                   "pan": null,
                   "address_country": 105,
                   "address_lat": "18.951666666666664440",
                   "address_lng": "72.949722222222220580",
                   "address_line_1": null,
                   "address_line_11": null,
                   "address_line_2": null,
                   "address_line_3": null,
                   "stakeholder": null,
                   "dynamic_table": "a4590179-498c-4146-960c-f15f813428c2",
                   "address_state": "Maharashtra",
                   "address_zipcode": null
                 },
                 "leg_num": 1
               },
               {
                 "id": "b5bdd8a5-142b-4e65-96d0-f29e1c7fd857",
                 "hub": {
                   "id": "5d0743fb-95ab-482f-9ff9-85133cb0212f",
                   "name": "Jebel Ali",
                   "pan": null,
                   "address_country": 2,
                   "address_lat": "24.995833333333333570",
                   "address_lng": "55.059444444444444855",
                   "address_line_1": null,
                   "address_line_11": null,
                   "address_line_2": null,
                   "address_line_3": null,
                   "stakeholder": null,
                   "dynamic_table": "a4590179-498c-4146-960c-f15f813428c2",
                   "address_state": null,
                   "address_zipcode": null
                 },
                 "leg_num": 2
               }
             ],
             "tax_currency": null,
             "provider_rate_currency": "INR",
             "provided_rate_currency": "INR",
             "charges": [],
             "penalties": [],
             "total_charge": "0.00",
             "is_cancelled": false
           }
         ],
         "mode": "Ocean"
       }
     ],
     "quote_number": "CPQ-NH3FY3",
     "rate_currency": null,
     "cargo_description": "fddsfg"
   }

**11.QuoteRUDView**

.. note:: API: "api/quote/(?P<pk>[^/]+)/"

.. note:: Methods: GET, PUT, PATCH, DELETE

GET: Returns list of all quotes.

PUT: New quote is created with the below given data.

**Request**

.. note:: These fields are mandatory.

.. code-block:: Python

   {
      "source": <string>,
      "no_of_containers": 88,
      "destination": <string>,
      "for_date": <timestamp>
   }


**Response**

.. code-block:: Python

   {
     "id": "04655a00-ef69-443b-b59c-************",
     "stakeholder": "ad0b3dc5-b121-43ea-9ed2-************",
     "source": "932c0a37-87a0-47d4-8d1a-************",
     "destination": "0c7cf0d9-083e-4a23-a668-************",
     "asset": null,
     "for_date": "2019-01-31T17:08:00+05:30",
     "for_date_choices": 1,
     "weight": null,
     "no_of_containers": 88,
     "include_cha": true,
     "is_dock_stuffing": false,
     "stuffing_duration": 1440,
     "legs": [
       {
         "id": "a2010ae4-7c3d-4bb3-b5ca-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 1,
         "route_num": 1,
         "start_date": "2019-01-24T11:20:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Sunny Point to Bar <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-24T11:20:00Z",
         "vessel_name": null
       },
       {
         "id": "801df2b1-49ef-4766-afed-************",
         "mode": {
           "id": "ee664a2f-d8a2-4d93-a524-************",
           "is_tracking_enabled": false,
           "tracking_method": 6,
           "dynamic_table": {
             "id": "51e739be-fa8a-43c0-b355-************",
             "table_name": "Road"
           }
         },
         "fromHub": {
           "id": "932c0a37-87a0-47d4-8d1a-************",
           "name": "Bar",
           "pan": null,
           "address_country": 234,
           "address_lat": "36.747852000000000000",
           "address_lng": "-95.976223000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "toHub": {
           "id": "0c7cf0d9-083e-4a23-a668-************",
           "name": "Sunny Point",
           "pan": null,
           "address_country": 234,
           "address_lat": "35.578569000000000000",
           "address_lng": "-82.588904000000000000",
           "address_line_1": null,
           "address_line_11": null,
           "address_line_2": null,
           "address_line_3": null,
           "stakeholder": null,
           "dynamic_table": "8dfe60e5-0b55-4d14-9ce7-************",
           "address_state": null,
           "address_zipcode": null
         },
         "leg_num": 2,
         "route_num": 1,
         "start_date": "2019-01-31T11:38:00Z",
         "duration": 8658,
         "rate": 143201,
         "delay": 0,
         "description_text": "Bar to Sunny Point <br />on: TRAILER",
         "is_import": false,
         "rate_currency": null,
         "is_active": false,
         "arrival_date": "2019-01-30T11:38:00Z",
         "vessel_name": null
       }
     ],
     "num_routes": 1,
     "helpscout_id": 229******,
     "quote_number": "CPQ-******",
     "rate_currency": null,
     "billing_address": null,
     "quickbooks_id": null,
     "cargo_description": null
   }

PATCH: Modifies the existing data.

DELETE: Destroys the given id.



