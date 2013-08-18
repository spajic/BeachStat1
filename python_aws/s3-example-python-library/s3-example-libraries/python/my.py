import S3

AWS_ACCESS_KEY_ID = 'AKIAI7R3ZZAEQ2GBDHUA'
AWS_SECRET_ACCESS_KEY = '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'

# for subdomains (bucket.s3.amazonaws.com),
# the bucket name must be lowercase since DNS is case-insensitive
# BUCKET_NAME = "%s-test-bucket" % AWS_ACCESS_KEY_ID.lower();
BUCKET_NAME = "spajic"

conn = S3.AWSAuthConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
response = conn.list_bucket(BUCKET_NAME)
print response.entries[0].key
print response.entries[1].key
print response.entries[2].key

text = 'this is a test'
key = 'example.txt'
response = conn.put(BUCKET_NAME, key, text)