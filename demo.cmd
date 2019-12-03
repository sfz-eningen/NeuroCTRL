@ECHO OFF
REM ---------------------------------------------
REM Demo to show functionality of the ESARToolkit
REM ---------------------------------------------

CD  .\Cyton\
:init
SET /P init="Initialized UDP-Stream on 127.0.0.1:12345?   [PRESS ENTER TO CONTINUE]>"

C:/Users/%USERNAME%/AppData/Local/Programs/Python/Python37-32/python.exe ./demo.py
EXIT