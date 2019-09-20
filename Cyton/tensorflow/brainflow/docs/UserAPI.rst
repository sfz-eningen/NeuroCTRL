User API
=========

There is no separated classes for each BCI board, instead there is only one BoardShim class, you need to pass BrainFlow's board id to BoardShim constructor to choose a board.
Using this design you are able to switch boards via single integer value and that's all.
To request information like sampling rate for speciffic board we recommend to use BoardInfoGetter class.
All bindings throw BrainFlowException with exit code and error message if smth goes wrong, to check all possible exit codes and their description check brainflow.exit_codes files

All bindings have pretty similar API, only important difference - java and matlab bindings currently have no signal processing methods. Here we will add only Python API Reference, for other languages it's almost the same

Python API Reference
---------------------

brainflow.board\_shim
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: brainflow.board_shim
   :members:
   :noindex:
   :show-inheritance:

brainflow.exit\_codes
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: brainflow.exit_codes
   :members:
   :undoc-members:
   :noindex:
   :show-inheritance:

brainflow.preprocess
~~~~~~~~~~~~~~~~~~~~~

.. automodule:: brainflow.preprocess
   :members:
   :undoc-members:
   :noindex:
   :show-inheritance:
