^!q::  ; Press Ctrl + Alt + Q to trigger the scroll
    StartTime := A_TickCount
    while (A_TickCount - StartTime < 8)
    {
        Send {WheelDown}
        Sleep 10  ; Adjust the sleep duration (in milliseconds) if needed
    }
return
