import webbrowser 
import time
url = "https://www.youtube.com/watch?v=qA8YkYZBS-U"
i = 1000
while i>= 0:
    print(i)
    if i == 0:
        webbrowser.open(url,new=1)
    i -= 1
    time.sleep(0.0000000000000001)
