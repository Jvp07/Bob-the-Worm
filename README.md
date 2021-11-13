# Bob The Almost Worm
## Disclaimer:
This repository and every script included in it is for educational and testing purposes only. The owner nor any contributor is not responsible for your actions.

## Overview:
This is a work in progress worm-like program. This can be used to scan targeted networks for online machines and open ports. Once machines with open ports are found, this program will bruteforce an SSH connection using provided username and password text files. If successful, the program will download a file from a local web server.

## Screenshots of the running program:
![1](https://user-images.githubusercontent.com/19824320/140623024-13d289c0-6be2-4fb2-ae36-ec4d7734148f.PNG)
![2](https://user-images.githubusercontent.com/19824320/140623025-67c9b1c7-76a2-4c6c-bfcd-fbf5b56c2b9a.PNG)


## Requirements:
```
pip install -r requirements.txt
```
Must download both main.py and hello.py to run the program.

## Executing the file:
```
python3 main.py
```

### Note when running the program:
This program requires a local cache of IP's to be built prior to succesfully running. You may need to run this once or twice before it can succesfully run. 

#### Authors:
Jose Vega
Sheena Talosig