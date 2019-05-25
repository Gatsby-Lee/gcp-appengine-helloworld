import gzip
import os
import time

import webapp2

import google.api_core.exceptions
import google.cloud.storage


BUCKET_NAME = os.environ.get('CLOUD_BUCKET_NAME')
STORAGE_CLIENT = google.cloud.storage.Client()
# thread-safe?
BUCKET = STORAGE_CLIENT.bucket(BUCKET_NAME)

class ListEnv(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        for k,v in os.environ.items():
            self.response.write('{}: {}\n'.format(k,v))

class ListObjects(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        blobs = BUCKET.list_blobs()
        self.response.write('Start ------------------------\n')
        for b in blobs:
            self.response.write(b)
            self.response.write('\n')
        self.response.write('END ------------------------\n')


class CreateObject(webapp2.RequestHandler):
    def get(self):
        object_key = '{}.txt'.format(int(time.time()))
        content = 'abcde'
        content_compressed = gzip.compress(content.encode('utf-8'))
        blob = BUCKET.blob(object_key)
        blob.content_encoding = 'gzip'
        blob.upload_from_string(content_compressed,
                                content_type='text/plain')
        self.redirect('/')

class DeleteObject(webapp2.RequestHandler):
    def get(self):
        try:
            fname = self.request.get('q')
            object_key = '{}.txt'.format(fname)
            blob = BUCKET.blob(object_key)
            blob.delete()
        except google.api_core.exceptions.NotFound:
            pass
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', ListObjects),
    ('/create', CreateObject),
    ('/delete', DeleteObject),
    ('/env', ListEnv),
], debug=True)
