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


from test_library import run_playbook_test


def test_testing_localhost():
    run_playbook_test("tests/stack-confs/stack-test-conf.yml",
                      "tests/target-playbooks/stack-test-playbook.yml")


def test_testing_ec2():
    run_playbook_test("tests/stack-confs/stack-test-ec2-conf.yml",
                      "tests/target-playbooks/stack-test-ec2-playbook.yml")
