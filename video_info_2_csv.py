import pandas as pd
import json


def read_file(filename):
    video_info = []
    with open(filename, 'r')as f:
        l = f.readline()
        while l != '':
            try:
                video_info.append(json.loads(l[:-1]))
                l = f.readline()
            except:
                pass
    return video_info


vi = read_file('bilibiliVideo.json')
for i in range(5):
    print(vi[i])
