import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from datetime import datetime
from tzlocal import get_localzone

window_name = "iTunes"

date = datetime.now()
localdate = date.astimezone(get_localzone()).strftime("%Y-%m-%d %H-%M-%S")
filename = "./output/" + window_name + " " + localdate + ".avi"

fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0
record_seconds = 5
w = gw.getWindowsWithTitle(window_name)[0]
w.activate()
out = cv2.VideoWriter(filename, fourcc, fps, tuple(w.size))

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()
