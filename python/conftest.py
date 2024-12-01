import pytest
import numpy as np
import operators
import waveforms


@pytest.fixture
def new_history():
    last_value = 3
    return operators.history(last_value)


@pytest.fixture
def new_buffer():
    buffer_data = np.array([ [0.01, 0.02, 0.03], [0.04, 0.05, 0.06] ])
    num_out_chans = 2
    return operators.peek(buffer_data, num_out_chans)


@pytest.fixture
def phasor_list():
    phase = 0
    fs = 41000
    time = np.arange(0, 225, 1)
    return [
        waveforms.phasor(60, phase, fs, time),
        waveforms.phasor(600, phase, fs, time),
        waveforms.phasor(6000, phase, fs, time),
        waveforms.phasor(60000, phase, fs, time)
    ]
