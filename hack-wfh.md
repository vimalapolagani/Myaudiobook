```python
pip install autogui
```

    Collecting autogui
      Downloading autogui-0.1.8.tar.gz (696 kB)
    Collecting pythonnet
      Downloading pythonnet-3.0.0.post1-py3-none-any.whl (279 kB)
    Collecting clr-loader<0.3.0,>=0.2.2
      Downloading clr_loader-0.2.3-py3-none-any.whl (50 kB)
    Requirement already satisfied: cffi>=1.13 in c:\users\vimala\anaconda3\lib\site-packages (from clr-loader<0.3.0,>=0.2.2->pythonnet->autogui) (1.14.6)
    Requirement already satisfied: pycparser in c:\users\vimala\anaconda3\lib\site-packages (from cffi>=1.13->clr-loader<0.3.0,>=0.2.2->pythonnet->autogui) (2.20)
    Building wheels for collected packages: autogui
      Building wheel for autogui (setup.py): started
      Building wheel for autogui (setup.py): finished with status 'done'
      Created wheel for autogui: filename=autogui-0.1.8-py3-none-any.whl size=470158 sha256=ad19d396903764b99fa3259a847d7254245cacec99c64bc80530358385701979
      Stored in directory: c:\users\vimala\appdata\local\pip\cache\wheels\5e\e6\2b\5302a8b38c64e21850aa73dd95f4e1b6e0267bcc15321d00c2
    Successfully built autogui
    Installing collected packages: clr-loader, pythonnet, autogui
    Successfully installed autogui-0.1.8 clr-loader-0.2.3 pythonnet-3.0.0.post1
    Note: you may need to restart the kernel to use updated packages.
    


```python
import pyautogui
import time
pyautogui.FAILSAFE=False
while True:
    time.sleep(15)
    for i in range(0,100):
        pyautogui.moveTo(0,i*5)
    for i in range(0,3):
        pyautogui.press('shift')
```


```python

```
