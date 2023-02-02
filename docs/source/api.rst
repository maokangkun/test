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
            ...
         ]
      }


患者所有数据
----------

.. http:get:: /api/patient/(str:patient_sn)

   根据患者ID返回患者所有数据。

   :query string patient_sn: 患者id
   :requestheader Authorization: `token`

   .. important::
      The author name must be in URL encoded format.

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/patient/(str:patient_sn)

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/patient/(str:patient_sn)'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      {
         "id": "患者id",
         "info": {
            "name": "患者姓名",
            "gender": "性别",
            "age": "年龄",
            "患者基本信息等": null
         },
         "records": [
            "患者所有检查记录数据"
         ]
      }

