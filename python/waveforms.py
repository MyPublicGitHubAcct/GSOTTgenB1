""" https://docs.cycling74.com/userguide/gen/gen~_operators/ """

import numpy as np


class phasor:
    """
    A non-bandlimited sawtooth-waveform signal generator with a range of 0 to 1
    which can be used as LFO audio signal or a sample-accurate timing/control
    signal.
    """
    def __init__(self, frequency, phase, samplerate, time=1):
        self.ph = phase
        self.inc = (np.pi * frequency) / samplerate
        self.time = time

    def get_next_sample(self) -> float:
        out = self.ph / (2 * np.pi)
        self.ph += self.inc

        if(self.ph > (2 * np.pi)):
            self.ph -= (2 * np.pi)
        if(self.ph < 0):
            self.ph = 0
        return out

    def get_block_of_samples(self):
        out = []
        for i in self.time:
            out.append(self.get_next_sample())

        return out

