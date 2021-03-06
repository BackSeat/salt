'''
Tests for the rabbitmq state
'''
import os
import integration


class RabbitUserTestCase(integration.ModuleCase):
    '''
    Validate the rabbitmq user states.
    '''
    def setUp(self):
        super(RabbitUserTestCase, self).setUp()
        rabbit_installed = self.run_function('cmd.has_exec', ['rabbitmqctl'])

        if not rabbit_installed:
            self.skipTest('rabbitmq-server not installed')
        if os.geteuid() != 0:
            self.skipTest('You must be root to run this test')

    def test_present(self):
        '''
        rabbitmq_user.present null_name
        '''
        ret = self.run_state(
            'rabbitmq_user.present', name='null_name', test=True)

        self.assertTrue(ret)
        self.assertFalse(self.state_result(ret))

    def absent(self):
        '''
        rabbitmq_user.absent null_name
        '''
        ret = self.run_state(
            'rabbitmq_user.absent', name='null_name', test=True)

        self.assertTrue(ret)
        self.assertFalse(self.state_result(ret))
