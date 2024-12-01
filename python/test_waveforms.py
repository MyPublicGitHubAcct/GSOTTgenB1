import waveforms
import pytest
import numpy as np

"""
Tests for waveforms.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_waveforms.py
"""

class TestPhasor:

    def test_phasor_60Hz(self, frequency, phase, samplerate, buffer):
        res = waveforms.phasor(0, 1)
        assert res == 0.05

    def test_phasor_600Hz(self, frequency, phase, samplerate, buffer):
        res = waveforms.phasor(1, 1)
        assert res == 0.05

    def test_phasor_6000Hz(self, frequency, phase, samplerate, buffer):
        res = waveforms.phasor(1, 1)
        assert res == 0.05

    def test_phasor_60000Hz(self, frequency, phase, samplerate, buffer):
        res = waveforms.phasor(1, 1)
        assert res == 0.05
