""" https://docs.cycling74.com/userguide/gen/gen~_operators/ """

def switch(reset: bool, new_value) -> float:
    """ 
    Parameters:
        reset: If false (or 0) is received, the function outputs 0. Any other value will cause
               the function to output new_value.
        new_value: A value received. Example: This can come from an addition to a history object.
    Returns: A float, either 0 or new_value.
    """
    if reset:
        return new_value
    else:
        return 0


class peek:
    """
    Read values from a data/buffer object. The first argument should be a name of a data or buffer object in 
    the gen patcher. The second argument specifies the number of output channels. The first inlet specifes a 
    sample index to read (no interpolation); indices out of range return zero. The last inlet specifies a 
    channel offset (default 0).

    (buffer_name, channels, sample_number, channel_offset=0)
    """
    def __init__(self, buffer_name, num_out_chans):
        self.buffer_name = buffer_name
        self.num_out_chans = num_out_chans

    def get_sample(idx: int, chan: int):
        return buffer_name[chan][idx]


class history:
    """
    The history operator allows feedback in the gen patcher through the insertion of a single-sample delay. 
    The first argument is an optional name for the history operator, which allows it to also be set externally 
    (in the same way as the param operator). The second argument specifies an initial value of stored history 
    (defaults to zero).
    """
    def __init__(self, last_value=0):
        self.last_value = last_value

    def get_last_value(self, new_value):  
        out = last_value
        last_value = new_value
        return out



