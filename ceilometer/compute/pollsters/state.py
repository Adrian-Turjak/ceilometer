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

from ceilometer.compute import plugin
from ceilometer.compute.pollsters import util
from ceilometer.openstack.common import log
from ceilometer import sample
LOG = log.getLogger(__name__)

from ceilometer import vm_states


class StatePollster(plugin.ComputePollster):

    def get_samples(self, manager, cache, instance):

        # made lowercase as status value is full caps
        state = vm_states.states[instance.status.lower()]

        yield util.make_sample_from_instance(
            instance,
            name='state',
            type=sample.TYPE_GAUGE,
            unit='state',
            volume=state,
        )
