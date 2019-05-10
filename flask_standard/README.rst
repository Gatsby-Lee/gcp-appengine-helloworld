GAE - Flask Standard
====================


.. code-block::

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/flask_standard
    dev_appserver.py app.yaml
    # open browser with http://localhost:8080/
    ## --- Deploying
    gcloud app deploy
    gcloud app browse
