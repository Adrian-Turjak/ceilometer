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


""""Mapping of Nova VM states to ints for use in metering. """
# It might be better to build a query for this list in
# the NoveClient rather than store it here.
# Or import vm_states and use the names defined there.
states = {'active': 1,
          'building': 2,
          'paused': 3,
          'suspended': 4,
          'stopped': 5,
          'rescued': 6,
          'resized': 7,
          'soft_deleted': 8,
          'deleted': 9,
          'error': 10,
          'shelved': 11,
          'shelved_offloaded': 12}
