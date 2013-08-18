import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAI7R3ZZAEQ2GBDHUA'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET = 'spajic'

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
b = conn.create_bucket(BUCKET)
k = Key(b)
k.key = 'beach_all_inclusive.html'
k.set_contents_from_filename('C:/Users/1/Dropbox/Beach/Graphics/beach_all_inclusive.html')
k.set_acl('public-read')
