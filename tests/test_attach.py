# encoding: utf-8

#
# Copyright © 2015 ATS Advanced Telematic Systems GmbH
#
# This file is part of Docker Launcher.
#
# Docker Launcher is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Docker Launcher is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# Docker Launcher. If not, see <http://www.gnu.org/licenses/>.
#


from launcher.util.stack_config import StackConf
import pytest


@pytest.fixture(scope="function")
def valid_service():
    return {
        'services': [{
            'name': 'test_service',
            'repo': 'test/repo',
            'attach': True
        }]
    }


def test_attach_is_valid(valid_service):
    StackConf(valid_service)

