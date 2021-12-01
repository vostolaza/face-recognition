import heapq
import json
import linecache
import math
import os
import sys
import collections
from itertools import chain

import face_recognition
import numpy as np
import pandas as pd
from rtree import index

CHUNKSIZE = 5


def knnRTree(k, image):
    p = index.Property()
    p.dimension = 128  # D
    p.buffering_capacity = 3  # M
    p.dat_extension = 'dat'
    p.idx_extension = 'idx'
    idx = index.Index(f"RTree", properties=p)

    picture = face_recognition.load_image_file(image)
    vector = face_recognition.face_encodings(picture)
    q = tuple(vector[0])

    if not len(q):
        return []

    lres = list(idx.nearest(coordinates=q, num_results=k))
    res = []
    for x in lres:
        line = json.loads(linecache.getline(
            f"Sequential.json", x+1))
        res.append(line[0])
    return res


def RangeRTree(r, image):

    p = index.Property()
    p.dimension = 128  # D
    p.buffering_capacity = 3  # M
    p.dat_extension = 'dat'
    p.idx_extension = 'idx'
    idx = index.Index(f"RTree", properties=p)

    picture = face_recognition.load_image_file(image)
    vector = face_recognition.face_encodings(picture)

    q = vector[0]

    bounds = []
    bounds.extend([i - r for i in q])
    bounds.extend([i + r for i in q])

    lres = [n.id for n in idx.intersection(bounds, objects=True)]

    res = []
    for x in lres:
        line = json.loads(linecache.getline(
            f"Sequential.json", x+1))
        res.append(line[0])
    return res
