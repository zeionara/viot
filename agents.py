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
        super().__init__(opt, shared)
        opt = copy.deepcopy(opt)

        opt['datafile'] = _path(opt, '')
        if shared is None:
             self._setup_data(opt['datafile'])