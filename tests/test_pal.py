from agents.pal import PAL
import replay_buffer
from test_dqn_like import _TestDQNLike


class TestPAL(_TestDQNLike):

    def make_agent(self, gpu, q_func, opt):
        rbuf = replay_buffer.ReplayBuffer(10 ** 5)
        return PAL(q_func, opt, rbuf, gpu=gpu, gamma=0.9, epsilon=0.2,
                   replay_start_size=100, target_update_frequency=100)