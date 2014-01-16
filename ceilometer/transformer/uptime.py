# -*- encoding: utf-8 -*-
#
# Copyright © 2013 Red Hat, Inc
#
# Author: Eoghan Glynn <eglynn@redhat.com>
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

from ceilometer import sample
from ceilometer.openstack.common.gettextutils import _
from ceilometer.openstack.common import log
from ceilometer.openstack.common import timeutils
from ceilometer import transformer

LOG = log.getLogger(__name__)


import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address='/dev/log')
my_logger.addHandler(handler)


class UptimeTransformer(transformer.TransformerBase):
    """Transformer to create uptime.
    """

    def __init__(self, source={}, target={}, **kwargs):
        """Initialize transformer with configured parameters.

        :param source: dict containing source sample unit
        :param target: dict containing target sample name, type,
                       unit and scaling factor (a missing value
                       connotes no change)
        """
        self.source = source
        self.target = target
        self.cache_prev = {}
        self.cache_uptime = {}
        self.uptime = 0.0
        super(UptimeTransformer, self).__init__(**kwargs)

    def _package(self, s, uptime):
        """Package the appropriate sample fields.
        """
        return sample.Sample(
            name=self.target.get('name', s.name),
            unit=self.target.get('unit', s.unit),
            type=self.target.get('type', s.type),
            volume=uptime,
            user_id=s.user_id,
            project_id=s.project_id,
            resource_id=s.resource_id,
            timestamp=s.timestamp,
            resource_metadata=s.resource_metadata
        )

    def handle_sample(self, context, s):
        """Handle a sample."""
        my_logger.critical("******************************************* HERE? ***********************************************")
        my_logger.critical('THIS TRANSFORMER IS: %s' % str(self))
        my_logger.critical('THIS resource_id IS: %s' % s.resource_id)
        key = s.resource_id
        prev = self.cache_prev.get(key)
        timestamp = timeutils.parse_isotime(s.timestamp)
        self.cache_prev[key] = (s.volume, timestamp)
        my_logger.critical('ALL uptime: %s' % self.cache_uptime)

        if prev:
            prev_timestamp = prev[1]

            if s.volume in self.target.get('active'):
                difference = timeutils.delta_seconds(prev_timestamp, timestamp)
                try:
                    self.cache_uptime[key] = (self.cache_uptime[key] +
                                              difference)
                except KeyError:
                    # no uptime for this key yet!
                    self.cache_uptime[key] = difference

            try:
                s = self._package(s, self.cache_uptime[key])
            except KeyError:
                my_logger.critical("Transformer KEYERROR!!")
                s = None

        else:
            LOG.warn(_('dropping sample with no predecessor: %s') %
                     (s,))

        return s
