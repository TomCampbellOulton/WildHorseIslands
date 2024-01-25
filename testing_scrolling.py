from ahkunwrapped import Script

ahk = Script('''
F1::
    while GetKeyState("F1", "P") ; while holding down F1
    {
        SendInput, {WheelDown}   ; send this command to the active window
        Sleep, 1000              ; every second (1000 ms)
    }
return
''')
