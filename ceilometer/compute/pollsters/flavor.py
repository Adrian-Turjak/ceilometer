from ceilometer.compute import plugin
from ceilometer.compute.pollsters import util
# from ceilometer.compute.virt import inspector as virt_inspector
from ceilometer.openstack.common.gettextutils import _  # noqa
from ceilometer import sample


class FlavorPollster(plugin.ComputePollster):

    def get_samples(self, manager, cache, instance):

        yield util.make_sample_from_instance(
            instance,
            name='flavor',
            type=sample.TYPE_GAUGE,
            unit='flavor.id',
            volume=instance.flavor['id'],
        )
