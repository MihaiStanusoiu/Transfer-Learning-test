from minio import Minio
from minio.error import *

minioClient = Minio('localhost:9000', '74ZSR29QTTIFINKGNARD', 'kahtZP8zS8NRAe6lF5nJEDlLas91VLyFTBfgkBlL', secure=False)

try:
    minioClient.make_bucket("cats", location="eu-central-1")
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise
else:
    # Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
    try:
        minioClient.fput_object('cats', 'KAT', '/home/mike/Downloads/KAT.jpeg', 'image/jpeg')
    except ResponseError as err:
        print(err)
