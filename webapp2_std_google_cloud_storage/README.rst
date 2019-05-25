GAE Standard - webapp2, google-cloud-storage
====================================

How to run - python37
---------------------

.. code-block:: bash

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/webapp2_std_google_cloud_storage
    dev_appserver.py app37.yaml dev_appserver.py py37.yaml \
        --env_var CLOUD_BUCKET_NAME=<bucket_on_cloud_storage> \
        --env_var GOOGLE_APPLICATION_CREDENTIALS=<service_account_json_path>
    # open browser with http://localhost:8080/


References
----------

* https://cloud.google.com/storage/docs/uploading-objects
