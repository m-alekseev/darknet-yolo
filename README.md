# Linux custom object detection using Darknet Yolo

### Prerequisites and Installation:

Before we start you need to install the following packages: [OpenCV](https://opencv.org/), [CUDA](https://developer.nvidia.com/cuda-downloads) (if you want GPU computation) and [Darknet](https://pjreddie.com/darknet/install/).

For this project I've used [MIT Traffic Data Set](http://www.ee.cuhk.edu.hk/~xgwang/MITtraffic.html). They provide a set of videos recorded by stationary camera and 2 matlab files with manually labelled pedestrians that are available by the [link](http://www.ee.cuhk.edu.hk/~xgwang/MIT_traffic_ground_truth_data.tar.gz).

To futher work we need to extract frames from videos, it's possible by using [ffmpeg](https://www.ffmpeg.org/). If you're using Arch Linux you can install it with pacman
```
pacman -S ffmpeg
```
Then go to the folder with downloaded videos and extract frames of them. Use the next command:
```
ffmpeg -i mv2_001.avi mv2_001_$04d.png
```
where:
- -i means the input file
- mv2_001_$04d.png - the output frame name, $04d means that a numeration of the frame starts from 0001 and so on

Name the output files in that way because frame names are related with ground truth data that we've got earlier. Repeat this command for each video you have, changing names of input and output files.

I've got almost 166k frames but we have labeled only each 200th frame. That's why we needed to name our frames as I said above. I've used a python script to select labeled files and move them to a separate folder. *python script link*

Before starting the script make sure you have created folders for the train and test data, while execution it will ask you to select a groud truth data file, a folder with images and a folder to save.

If you're too lazy to do it, I've prepared the ready to use data. HERE SHOULD BE A LINK!



