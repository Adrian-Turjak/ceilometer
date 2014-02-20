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
