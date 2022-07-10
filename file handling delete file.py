import os
if os.path.exists("C:/Users/tharun/OneDrive/Desktop/DEMO.txt"):
    os.remove("C:/Users/tharun/OneDrive/Desktop/DEMO.txt")
else:
    print("file does not exist")

os.rmdir("C:/Users/tharun/OneDrive/Desktop/DEMO")