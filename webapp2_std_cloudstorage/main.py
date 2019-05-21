import os
import time

import cloudstorage
import webapp2

from google.appengine.api import app_identity


def get_bucket_path():
    bucket_name = os.environ.get(
            'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    return '/%s' % bucket_name

class ListObjects(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('!!! googlecloudstorageclient doesn NOT support python3\n')
        self.response.write('# cloudstorage\n')
        self.response.write('# webapp2 - {}\n'.format(webapp2.__version__))

        bucket = get_bucket_path()
        self.response.write('List result in bucket={}:\n'.format(bucket))
        # max_keys is used to limit the number of key
        stats = cloudstorage.listbucket(bucket + '/', max_keys=10)
        self.response.write('Start ------------------------\n')
        for stat in stats:
            self.response.write(repr(stat))
            self.response.write('\n')
        self.response.write('END ------------------------\n')

class CreateObject(webapp2.RequestHandler):
    def get(self):

        write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)

        bucket = get_bucket_path()
        filename = os.path.join(bucket, '{}.txt'.format(int(time.time())))
        gcs_file = cloudstorage.open(filename,
                            'w',
                            content_type='text/plain',
                            retry_params=write_retry_params)
        gcs_file.write('abcde\n')
        gcs_file.close()
        self.redirect('/')

class DeleteObject(webapp2.RequestHandler):
    def get(self):

        fname = self.request.get('q')
        print(fname)
        write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
        bucket = get_bucket_path()
        filename = os.path.join(bucket, '{}.txt'.format(fname))
        try:
            cloudstorage.delete(filename, retry_params=write_retry_params)
        except cloudstorage.NotFoundError:
            pass

        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', ListObjects),
    ('/create', CreateObject),
    ('/delete', DeleteObject),
], debug=True)
