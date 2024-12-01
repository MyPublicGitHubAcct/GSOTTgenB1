""" https://docs.cycling74.com/userguide/gen/gen~_operators/ """

import numpy as np
from scipy import signal


class phasor:
    """
    A non-bandlimited sawtooth-waveform signal generator which can be
    used as LFO audio signal or a sample-accurate timing/control signal.
    """
    def __init__(self, frequency, phase, time, buffer):
        self.f = frequency
        self.ph = phase
        self.t = time
        self.buf = buffer
        self.phase_increment = 0

    def get_buffer(self):
        return self.buf

    def get_sample(self, chan: int, idx: int) -> float:
        return signal.sawtooth(2 * np.pi * f * t)
