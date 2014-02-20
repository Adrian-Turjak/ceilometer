# -*- encoding: utf-8 -*-
#
# Copyright © 2014 Catalyst IT
#
# Author: Adrian Turjak <adriant@catalyst.net.nz>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from ceilometer.compute import manager
from ceilometer.compute.pollsters import state as pollsters_state
from ceilometer.tests.compute.pollsters import base


class TestStatePollster(base.TestPollsterBase):

    def setUp(self):
        super(TestStatePollster, self).setUp()

    @mock.patch('ceilometer.pipeline.setup_pipeline', mock.MagicMock())
    def test_get_samples_instance(self):
        mgr = manager.AgentManager()
        pollster = pollsters_state.StatePollster()
        samples = list(pollster.get_samples(mgr, {}, self.instance))
        self.assertEqual(len(samples), 1)
        self.assertEqual(samples[0].name, 'state')
        self.assertEqual(samples[0].volume, 1)
        self.assertEqual(samples[0].unit, 'state')
