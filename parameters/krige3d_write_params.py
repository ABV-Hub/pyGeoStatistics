# -*- coding: utf-8 -*-
"""
Created on Tue Nov 2016
"""
__author__ = "yuhao"

import os
import json

PARAMS = {
    'datafl': 'testData/test.gslib',
    'icolx': 0,
    'icoly': 1,
    'icolz': 2,
    'icolvr': 3,
    'icolsec': 4,

    'tmin': -1.0e21,
    'tmax': 1.0e21,

    'option': 0,
    'jackfl': 'jackfl.dat',
    'jicolx': 0,
    'jicoly': 1,
    'jicolz': 2,
    'jicolvr': 3,
    'jicolsec': 4,

    'idbg': 3,
    'dbgfl': 'kt3d.dbg',
    'outfl': 'out.dat',

    'nx': 98,
    'xmn': 100,
    'xsiz': 200,
    'ny': 79,
    'ymn': 100,
    'ysiz': 200,
    'nz': 1,
    'zmn': 0,
    'zsiz': 200,

    'nxdis': 1,
    'nydis': 1,
    'nzdis': 1,

    'ndmin': 1,
    'ndmax': 30,

    'noct': 0,
    'radius_hmax': 4000,
    'radius_hmin': 4000,
    'radius_vert': 0,
    'sang1' : 0,
    'sang2' : 0,
    'sang3' : 0,

    'ikrige': 0,
    'skmean': 14.69588,

    'idrift': [False, False, False, False, False, False, False, False, False],
    'itrend': False,
    'secfl': 'secfl.dat',
    'iseccol': 3,

    'nst': 1,
    'c0': 0.05,
    'it': [1],
    'cc': [0.65],
    'ang1': [0],
    'ang2': [0],
    'ang3': [0],
    'aa_hmax': [3715.9],
    'aa_hmin': [3715.9],
    'aa_vert': [3715.9],
}

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
PARAM_DIR = os.path.join(PARENT_DIR, 'testData')

with open(os.path.join(PARAM_DIR, 'test_krige3d.par'), 'w') as fout:
    fout.write(json.dumps(PARAMS, sort_keys=True, indent=4))
