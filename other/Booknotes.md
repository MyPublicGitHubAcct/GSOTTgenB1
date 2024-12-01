# Book notes

From _Generating Sound & Organizing Time_ by Wakefield and Taylor.

Other sources:

- https://docs.cycling74.com/userguide/gen/_gen_overview/
- https://docs.cycling74.com/userguide/gen/gen~_operators/
- https://cycling74.com/tutorials/gen-video-tutorial-series

## Python environment

Note: _pysound_ is not available yet, so _sounddevice_ and _soundfile_ are used to read and write files. They are not available through homebrew, so a virtual environment should be installed in the user's home directory.


```python
sudo python3 -m venv venv/
source venv/bin/activate
sudo python3 -m pip install numpy scipy matplotlib soundfile sounddevice jupyterlab pytest
deactivate
```

To load Jupyter lab:

```python
jupyter lab
```

