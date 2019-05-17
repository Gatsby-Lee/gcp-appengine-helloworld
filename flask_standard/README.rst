GAE - Flask Standard
====================

ref: https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env

이상한 경험들
----------

* python27과 python37을 테스팅 하느라고 번갈아 가면서 사용했다. AppEngine이 기대하는 것과 달리 동작하지 않았다.
* AppEngine이 Google Cloud Storage ( GCS ) Image를 Uploading 한다. 아무래도, python27과 python37을 번갈아 가면서 deploying 할 때, GCS Bucket에 Image가 모든 Update 되는 것이 아닌 것 같아 보인다. Diffset만 Upload 되는 것으로 보인다. ( Local에서 Deploying 할때도, uploading 하는 file에 숫자가 다르다.
* 뭔가가 이상할때는, GCS 있는 AppEngine 관련된 bucket을 모두 지워고 다시 시도해 보는 것도 하나의 방법이 되겠다.
* `gcloud app deploy` 할때, `./lib` 폴더에 있는 package들도 같이 deploying 된다. `appengine_config.py`에 정의 되어 있기 때문인 듯 하다.
* `./lib`에 package를 installing 할때 `pip install -t lib -r requirement.txt` 하게 되는데, 이때 사용하는 pip은 python27 또는 python37 각각 맞는 버젼을 사용해야 한다. python37으로 deploying 하면서 pip2.7으로 package를 installing 하면 안 되는듯.


Local Dev
---------

.. code-block:: bash

    cd /home/web
    git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
    cd gcp-appengine-helloworld/flask_standard
    dev_appserver.py app.yaml
    # open browser with http://localhost:8080/


Deploying
---------

.. code-block:: bash

    ## --- Deploying
    pip install -t lib -r requirement.txt
    gcloud app deploy app.yaml
    gcloud app browse


Error Msg ( python3 )
---------------------


(.venv) [/home/web/gcp-appengine-helloworld/flask_standard]$ dev_appserver.py app.yaml
ERROR: Python 3 and later is not compatible with the Google Cloud SDK. Please use Python version 2.7.x.

If you have a compatible Python interpreter installed, you can use it by setting
the CLOUDSDK_PYTHON environment variable to point to it.
