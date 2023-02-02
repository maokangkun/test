API
===

.. autosummary::
   :toctree: generated


Builds listing
++++++++++++++

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

