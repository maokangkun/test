Usage
=====

.. _installation:

Installation
------------

To use openCDS, you can simply install it from PyPI with the following command:

.. code-block:: console

   (.venv) $ pip install openCDS

If you use Anaconda or Miniconda, you can install openCDS through the following command:

.. code-block:: console
   
   (.venv) $ conda install -c openCDS openCDS

Quick Start
----------------

.. code-block:: console

   (.venv) $ openCDS config --dbtype mysql --host <host> --port 3306 -u <user> -p <pwd>
   (.venv) $ openCDS -h
   (.venv) $ openCDS query --id <xxx> --his --html

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.


For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

