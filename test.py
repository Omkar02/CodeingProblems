import __main__ as main
from TimerLogger import CodeTimeLogging

fileName = main.__file__
fileName = fileName.split('\\')[-1]


CodeTimeLogging(Flag='S', filename=fileName)
# this
