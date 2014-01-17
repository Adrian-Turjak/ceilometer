from ceilometer.compute import plugin
from ceilometer.compute.pollsters import util
# from ceilometer.compute.virt import inspector as virt_inspector
from ceilometer.openstack.common.gettextutils import _  # noqa
from ceilometer.openstack.common import log
from ceilometer import sample
LOG = log.getLogger(__name__)

from ceilometer.vm_states import states


class StatePollster(plugin.ComputePollster):

    def get_samples(self, manager, cache, instance):

        # made lowercase as status value is full caps
        state = states[instance.status.lower()]

        yield util.make_sample_from_instance(
            instance,
            name='state',
            type=sample.TYPE_GAUGE,
            unit='state',
            volume=state,
        )
