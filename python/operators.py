""" https://docs.cycling74.com/userguide/gen/gen~_operators/ """

import numpy as np

def switch(reset: bool, new_value) -> float:
    """ 
    Parameters:
        reset: If true (not 0) is received, the function outputs new_value. A 0 value will cause the 
               function to output 0.
        new_value: A value received. Example: This can come from an addition to a history object.
    Returns: A float, either 0 or new_value.
    """
    if reset:
        return 0
    else:
        return new_value


def phasewrap(angle):
    """
    Parameters:
        angle: The input value
    Returns: The input wrapped to the range -pi to +pi
    """
    angle = np.fmod(angle + np.pi, 2 * np.pi)
    if (angle < 0):
        angle += 2 * np.pi

    return angle - np.pi


class peek:
    """
    Read values from a data/buffer object. The first argument should be a name of a data or buffer object in 
    the gen patcher. The second argument specifies the number of output channels. The first inlet specifes a 
    sample index to read (no interpolation); indices out of range return zero. The last inlet specifies a 
    channel offset (default 0).
    """
    def __init__(self, buffer, num_out_chans):
        self.buffer = buffer

        if num_out_chans > len(buffer):
            self.num_out_chans = len(buffer)
        else:
            self.num_out_chans = num_out_chans

    def get_buffer(self):
        return self.buffer

    def get_sample(self, chan: int, idx: int) -> float:   
        return self.buffer[chan][idx]


class history:
    """
    The history operator allows feedback in the gen patcher through the insertion of a single-sample delay. 
    The first argument is an optional name for the history operator, which allows it to also be set externally 
    (in the same way as the param operator). The second argument specifies an initial value of stored history 
    (defaults to zero).
    """
    def __init__(self, last_value):
        self.last_value = last_value

    def get_last_value(self, new_value):  
        out = self.last_value
        self.last_value = new_value
        return out


