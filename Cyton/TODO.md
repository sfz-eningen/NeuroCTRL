# TODO
## Libs/User Interface
### Libraries ([master/basic_libs](./basic_libs))
 - **Timeline to FFT** **([master/basic_libs/fft.py](./basic_libs/fft.py))**
 - **FFT/TL to Bands** **([more](https://de.wikipedia.org/wiki/Elektroenzephalografie))** **([master/basic_libs/fft.py](./basic_libs/fft.py))**
   | Band Name   | Frequency Lower | Frequency Higher |
   |-------------|----------------:|-----------------:|
   | **Delta**   |          0.1 Hz |           < 4 Hz |
   | **Theta**   |            4 Hz |           < 8 Hz |
   | **Alpha**   |            8 Hz |          < 13 Hz |
   | **Beta**    |           13 Hz |          < 30 Hz |
   | **Gamma**   |           30 Hz |          > 30 Hz |

 - **Generate Sample of EEG Data** **([master/basic_libs/collect.py](./basic_libs/collect.py))**
 - **Generate TensorFlow Array** **([master/basic_libs/conv_tf.py](./basic_libs/conv_tf.py))**
 - **Sample Saver** **([master/basic_libs/sample_tool.py](./basic_libs/sample_tool.py))**
 - **Sample Loader** **([master/basic_libs/sample_tool.py](./basic_libs/sample_tool.py))**
 - **Cyton input to usable EEG data** **([master/basic_libs/conv_in.py](./basic_libs/sample_tool.py))**

### UI ([master/graphics](./graphics))
 - **Display Container** **([master/graphics/main_ui.py](./graphics/main_ui.py))**

## Tensorflow ([master/tensorflow](./tensorflow))
 - **Install**
   - *Add into Repo as Lib*
 - **Base Script**
   - *Set up settings*
 - **Loader**
   - Loader for new samples
 - **Recognizer**