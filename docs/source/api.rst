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


患者所有记录数据
--------------

.. http:get:: /api/patient/(str:patient_sn)

   根据患者ID返回患者所有数据。

   :query string patient_sn: 患者id
   :requestheader Authorization: `token`

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
            "birth_date": "",
            "blood_type_abo": "未查",
            "blood_type_rh": "未查",
            "contact_name": "",
            "contact_relationship": "",
            "contact_telephone": "",
            "create_at": "",
            "credential_no": "",
            "credential_type": "",
            "education": "",
            "ethnic": "",
            "gender": "",
            "hometown": "",
            "marriage": "",
            "medical_org_id": "",
            "medical_org_name": "",
            "nation": "",
            "occupation_category": "",
            "patient_name": "",
            "patient_sn": "",
            "telephone": "",
            "update_at": ""
         },
         "records": [
            {
               "abdominal_surgery_history": 0,
               "ae_symptom": "腹泻",
               "bleeding": 1,
               "cancer_family_history": 0,
               "create_date": "",
               "dept_name": "胃肠外一",
               "doc_sn": "",
               "doc_text": "",
               "doc_type_name": "入院记录",
               "doc_xml": "",
               "is_ulcer": 1,
               "liver_metastasis": "",
               "liver_metastasis_time": "",
               "obstruction": 1,
               "obstruction_degree": 0,
               "other_hospital_records": "",
               "patient_sn": "",
               "visit_sn": ""
            },
         ]
      }

   .. warning::
      records 数组里的记录数据里所含的字段根据不同的记录而不同.

患者决策树数据
------------

.. http:get:: /api/decisiontree/(str:patient_sn)

   根据患者ID返回患者所有的阶段及其每个阶段的决策树数据。

   :query string patient_sn: 患者id
   :requestheader Authorization: `token`

   .. important::
      The author name must be in URL encoded format.

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/decisiontree/(str:patient_sn)

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/decisiontree/(str:patient_sn)'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      {
         "id": "患者id",
         "info": {
         },
         "records": [
         ]
      }


所有记录统计数据
-------------

.. http:get:: /api/records_summary

   返回数据库中所有记录的总结统计数据。

   :requestheader Authorization: `token`

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/records_summary

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/records_summary'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      <html></html>

所有患者统计数据
-------------

.. http:get:: /api/patients_summary

   返回数据库中所有患者相关的总结统计数据。

   :requestheader Authorization: `token`

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/patients_summary

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/patients_summary'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      <html></html>

患者第一次治疗前状态统计数据
------------------------

.. http:get:: /api/patients_status

   返回数据库中所有患者在第一次治疗前的状态统计数据。

   :requestheader Authorization: `token`

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/patients_status

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/patients_status'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      <html></html>

治疗操作相关统计数据
-----------------

.. http:get:: /api/other_variables_statistics

   返回数据库中所有治疗操作相关的总结统计数据。

   :requestheader Authorization: `token`

   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl -H "Authorization: Token <token>" http://<server_address>>/api/other_variables_statistics

      .. code-tab:: python

         import requests
         URL = 'http://<server_address>>/api/other_variables_statistics'
         TOKEN = '<token>'
         HEADERS = {'Authorization': f'Token {TOKEN}'}
         response = requests.get(URL, headers=HEADERS)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      <html></html>
