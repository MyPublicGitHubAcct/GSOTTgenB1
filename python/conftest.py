import pytest
import numpy as np
import operators

@pytest.fixture
def new_history():
    last_value = 3
    return operators.history(last_value)


@pytest.fixture
def new_buffer():
    buffer_data = np.array([ [0.01, 0.02, 0.03], [0.04, 0.05, 0.06] ])
    num_out_chans = 2
    return operators.peek(buffer_data, num_out_chans)
