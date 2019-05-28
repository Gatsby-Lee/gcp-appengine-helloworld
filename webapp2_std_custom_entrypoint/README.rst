GAE Standard - webapp2, custom entrypoint
====================================

Why do I need to use custom entrypoint?
---------------------------------------

* ref: https://cloud.google.com/appengine/docs/standard/python3/runtime#application_startup

My reason is to use app in subdirectory rather in root.


How to run - python37
---------------------

.. code-block:: bash

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/webapp2_std_custom_entrypoint
    dev_appserver.py py37.yaml --env_var GOOGLE_APPLICATION_CREDENTIALS=<service_account_json_path>
    # open browser with http://localhost:8080/
    # Try
    http://localhost:8080/



References
----------

* https://cloud.google.com/appengine/docs/standard/python3/runtime#application_startup
