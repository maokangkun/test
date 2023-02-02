API
===

.. autosummary::
   :toctree: generated

   lumache

.. contents:: Table of contents
   :local:
   :backlinks: none
   :depth: 3


Retrieve Book Titles by Author
------------------------------

.. http:get:: /libapi/author/(author_name)
   :noindex:
   
     Retrieves a list of books written by a specified author.
	 
   :query string:  author_name (*required*) -- The name the of the particular author
   
   :requestheader Authorization: `token`
   
.. important::
   The author name must be in URL encoded format.

**Example Request**

.. sourcecode:: bash
  
   curl -s -H "Authorization: e52858e3-529a-40da-99d2-3bffd80a7a9b" curl -X GET https://fictionallibrary.com/libapi/author/Crichton%20Michael 

**Example Response**

.. sourcecode:: json

   {
      "count": 17,
      "results": [
         {
             "author": "Crichton, Michael",
             "title": "The Andromeda Strain",
             "publisher": "Vintage", 
             "latest_publication_date": "January 24, 2017",
             "language": "en",
             "isbn10": "1101974494",
             "isbn13": "9781101974490"
         },
         {
             "author": "Crichton, Michael",
             "title": "Jurassic Park",
             "publisher": "Vintage", 
             "latest_publication_date": "May 14, 2012",
             "language": "en",
             "isbn10": "1501216902",
             "isbn13": "9781501216909"
         },
         {
             "author": "..."
         },
      ]
   }

Builds listing
------------------------------

.. http:get:: /api/v3/projects/(str:project_slug)/builds/

    Retrieve list of all the builds on this project.

    **Example request**:

    .. tabs::

        .. code-tab:: bash

            $ curl -H "Authorization: Token <token>" https://readthedocs.org/api/v3/projects/pip/builds/

        .. code-tab:: python

            import requests
            URL = 'https://readthedocs.org/api/v3/projects/pip/builds/'
            TOKEN = '<token>'
            HEADERS = {'Authorization': f'token {TOKEN}'}
            response = requests.get(URL, headers=HEADERS)
            print(response.json())

    **Example response**:

    .. sourcecode:: json

        {
            "count": 15,
            "next": "/api/v3/projects/pip/builds?limit=10&offset=10",
            "previous": null,
            "results": ["BUILD"]
        }

    :query string commit: commit hash to filter the builds returned by commit
    :query boolean running: filter the builds that are currently building/running


.. warning::
   Failing to dot your **i**s and cross your **t**s, makes the words you write difficult to read.

