GAE Standard - webapp2, cloudstorage
====================================

NOTE!!
------

* `GoogleAppEngineCloudStorageClient` doesn't work with python37. `runtime` has to be python27.
* With `GoogleAppEngineCloudStorageClient`  and `dev_appserver.py`, local storage can emulate Cloud Storage. ( no connection to remote cloud storage ).


How to run - python27
---------------------

.. code-block:: bash

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/webapp2_std_cloudstorage
    # assuming this pip is python27
    pip install -t lib -r requirements.txt
    # --storage_path specifies the directory of local storage
    dev_appserver.py app27.yaml --storage_path=/mnt/tmp/dev_appserver
    # open browser with http://localhost:8080/


References
----------

* https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/functions
* https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/app-engine-cloud-storage-sample
* https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/storage/appengine-client/main.py
