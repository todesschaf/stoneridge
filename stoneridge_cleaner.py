#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

import shutil

import stoneridge

@stoneridge.main
def main():
    parser = stoneridge.ArgumentParser()
    parser.parse_arguments()
    shutil.rmtree(stoneridge.workdir)
