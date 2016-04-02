# -*- coding: utf-8 -*-

# Copyright (C) 2016, Maximilian Köhl <mail@koehlma.de>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License version 3 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import os

from jaspy import metadata
from jaspy.preprocessor import process


__path__ = os.path.dirname(__file__)
if __path__:
    os.chdir(__path__)


if __name__ == '__main__':
    namespace = {
        'DEBUG': False,
        'DEBUG_INSTRUCTIONS': False,
        'DEBUG_EXCEPTIONS': False,
        'DEBUG_THREADING': False,

        'INCLUDE_BIGINT': True,
        'INCLUDE_ENCODING': False,

        'ENABLE_DEBUGGER': True,
        'ENABLE_THREADING': True,

        'THREADING_LIMIT': 5000,


        'modules': [],

        'metadata': metadata
    }

    if not os.path.exists('build'):
        os.mkdir('build')

    with open('build/jaspy.js', 'w') as output:
        output.write(process('src/__init__.js', namespace))
