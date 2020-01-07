# -*- coding:utf-8 -*-

import os
import yaml                                                                     # pip install pyyaml
import  pymongo

cfg_path = os.path.realpath(os.path.dirname(__file__)) + "/cfg.yml"

cfg = {}

try:
    with open(cfg_path, 'r') as f:
        cfg = yaml.load(f)
except:
    pass

class conf:


    class mongo:

        host, port = cfg.get("mongo", ("127.0.0.1", 27017))


if __name__ == '__main__':
    print(conf.mysql.host)
