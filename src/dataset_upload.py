from minio import Minio
from minio.error import *
import os
import subprocess
import eyed3

minioClient = Minio('localhost:9000', 'VRXQF0XU7TCJ8AFNBHFW', 'Re+mqlWU8bcP0aAKCKH9d+RX1TZuTYC+XwH8aKLJ', secure=False)
os.chdir('/run/media/mike/66FC9B63FC9B2C75/Users/Mike/PycharmProjects/MoodifyCNN/venv/resources/fma_small/fma_small/')
try:
    for child_dir in os.listdir('.'):
        minioClient.make_bucket(child_dir, location="eu-central-1")
        for file in os.listdir(child_dir):
            path = child_dir + '/' + file
            audiofile = eyed3.load(path);
            minioClient.fput_object(child_dir, audiofile, path, 'audio/mpeg')
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise
# else:
#     # Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
#     try:
#         minioClient.fput_object('cats', 'KAT', '/home/mike/Downloads/KAT.jpeg', 'image/jpeg')
#     except ResponseError as err:
#         print(err)
