#!/usr/bin/env python3

from parlai.core.teachers import ParlAIDialogTeacher
import parlai.core.agents as core_agents
from .build import build
from parlai.core.teachers import DialogTeacher

import copy
import os


def _path(opt, dt=''):
    # Build the data if it doesn't exist.
    build(opt)
    if dt == '':
        dt = opt['datatype'].split(':')[0]
    return os.path.join(
        opt['datapath'],
        'viot',
        'data.txt',
    )


class DefaultTeacher(ParlAIDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)
        data_path = _path(opt)
        opt['datafile'] = data_path
        self.id = 'viot'
        print("Content of datafile:")
        with open(opt["datafile"], "r") as file:
            print(file.read())
        super().__init__(opt, shared)

    def setup_data(self, path):
        return setup_data(path)
