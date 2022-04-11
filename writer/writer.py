import multiprocessing as mp
from functools import partial

import boto3
import numpy as np


s3 = boto3.client(
    's3',
    region_name='eu-west-1',
    endpoint_url='http://localhost:4572'
)
archive = np.load(s3.get_object('some_key'))


def _something(**kwargs):
    return np.array([1, 2, 3])


def do(archive):  # pass the previously loaded archive, and not the s3 object into the function
    pool = mp.pool()
    sub_process = partial(_something, slack=0.1)
    parts = np.array_split(archive, 1)
    target_parts = np.array([1])

    out = pool.starmap(sub_process, [x for x in zip(parts, target_parts)])

    pool.close()
    pool.join()
