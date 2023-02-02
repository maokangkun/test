API
===

.. contents:: Table of contents
   :local:
   :backlinks: none
   :depth: 3


所有患者列表
----------

.. http:get:: /api/patient_list

   返回所有患者列表。

   :requestheader Authorization: `token`

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/patient_list

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/patient_list'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      {
         "data": [
            {
               "cancer_type": "胃癌",
               "first_diag_age": 73,
               "gender": "女",
               "patient_name": "张三",
               "patient_sn": "xxxxxxxxxxxxxxxx",
               "zyh": "4240897"
            },
         ]
      }


所有患者列表
----------

.. http:get:: /api/v3/projects/(str:project_slug)/builds/

   返回所有患者列表。

   :query string commit: commit hash to filter the builds returned by commit
   :query boolean running: filter the builds that are currently building/running
   :requestheader Authorization: `token`

   .. important::
      The author name must be in URL encoded format.

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" https://readthedocs.org/api/v3/projects/pip/builds/

      .. code-tab:: python

         import requests
         URL = 'https://readthedocs.org/api/v3/projects/pip/builds/'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      {
         "data": []
      }

