<link rel="icon" href="http://icons.iconarchive.com/icons/papirus-team/papirus-apps/512/python-icon.png">

# TODO
## Libs/User Interface
### Libraries ([master/Cyton/basic_libs](./Cyton/basic_libs))
 - **Timeline to FFT** **([master/Cyton/basic_libs/fft.py](./Cyton/basic_libs/fft.py))**
 - **FFT/TL to Bands** **([more](https://de.wikipedia.org/wiki/Elektroenzephalografie))** **([master/Cyton/basic_libs/fft.py](./basic_libs/fft.py))**
 
   | Band Name   | Frequency Lower | Frequency Higher |
   |-------------|----------------:|-----------------:|
   | **Delta**   |          0.1 Hz |           < 4 Hz |
   | **Theta**   |            4 Hz |           < 8 Hz |
   | **Alpha**   |            8 Hz |          < 13 Hz |
   | **Beta**    |           13 Hz |          < 30 Hz |
   | **Gamma**   |           30 Hz |          > 30 Hz |

 - **Generate Sample of EEG Data** **([master/Cyton/basic_libs/collect.py](./Cyton/basic_libs/collect.py))**
 - **Generate TensorFlow Array** **([master/Cyton/basic_libs/conv_tf.py](./Cyton/basic_libs/conv_tf.py))**
 - **Sample Saver** **([master/Cyton/basic_libs/sample_tool.py](./Cyton/basic_libs/sample_tool.py))**
 - **Sample Loader** **([master/Cyton/basic_libs/sample_tool.py](./Cyton/basic_libs/sample_tool.py))**
 - **Cyton input to usable EEG data** **([master/Cyton/basic_libs/conv_in.py](./Cyton/basic_libs/sample_tool.py))**

### UI ([master/Cyton/graphics](./Cyton/graphics))
 - **Display Container** **([master/Cyton/graphics/main_ui.py](./Cyton/graphics/main_ui.py))**

## Tensorflow ([master/Cyton/tensorflow](./Cyton/tensorflow))
 - **Install**
   - *Add into Repo as Lib*
 - **Base Script**
   - *Set up settings*
 - **Loader**
   - Loader for new samples
 - **Recognizer**

## Links
[Main Page](https://sfz-eningen.github.io/NeuroCTRL/)
