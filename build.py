#!/usr/bin/env python3

import parlai.core.build_data as build_data
import os


def build(opt):
    dpath = os.path.join(opt['datapath'], 'viot')
    version = '1.3'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        fname = 'data.txt'
        url = 'https://raw.githubusercontent.com/MANASLU8/VoiceIoT/master/dataset/parlai/' + fname
        build_data.download(url, dpath, fname)
        #build_data.untar(dpath, fname)

        # Mark the data as built.
        build_data.mark_done(dpath, version_string=version)
