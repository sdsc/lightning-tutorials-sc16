* install miniconda for ARM (reply YES to the `PATH` modifications in `.bashrc`):

        wget http://repo.continuum.io/miniconda/Miniconda3-3.16.0-Linux-armv7l.sh
        bash Miniconda3-3.16.0-Linux-armv7l.sh 

* restart the terminal
* install conda packages

        conda install h5py pandas numpy tornado ipython jinja2 traitlets pyzmq scikit-learn

* create a conda environment named `py`

        conda create -n py --clone root

* activate the environment

        source activate py

* install pip packages

        pip install dask[array] jupyter matplotlib

## Facedetection with OpenCV

    sudo apt-get install python-opencv libopencv-photo2.4
