GAE Standard - webapp2
======================

webapp2 python3 comparability
-----------------------------

webapp2 2.x doesn't support python3 yet.

webapp2. 3.x DOES support python3. This is currently under beta.

https://pypi.org/project/webapp2/#history



Local Dev - python3.7
---------------------

.. code-block:: bash

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/webapp2_standard
    dev_appserver.py app37.yaml
    # open browser with http://localhost:8080/


Deploying - python3.7
---------------------

.. code-block:: bash

    cd /home/web/gcp-appengine-helloworld
    python3.7 -m venv .venv
    cd /home/web/gcp-appengine-helloworld/webapp2_standard
    # .venv is in .gcloudignore, so it won't be uploaded to GCS
    ../.venv/bin/pip install -t lib -r requirements.txt
    gcloud app deploy app37.yaml
    gcloud app browse
