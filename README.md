# Linux custom object detection using Darknet Yolo

## Prerequisites and Installation:

Before we start you need to install the following packages: [OpenCV](https://opencv.org/), [CUDA](https://developer.nvidia.com/cuda-downloads) (if you want GPU computation) and [Darknet](https://pjreddie.com/darknet/install/).

### Preparing a dataset
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

I've got almost 166k frames but we have labeled only each 200th frame. That's why we needed to name our frames as I said above. I've used a python script to select labeled files and move them to a separate folder. Here is a [script](process_data.py).

Before starting the script make sure you have created folders for the train and test data, while execution it will ask you to select a groud truth data file, a folder with images and a folder to save.

If you're too lazy to do it, I've prepared the ready to use [dataset](https://drive.google.com/file/d/0B-2U0T71FkkZNmpUdUNXRXlxUVE/view?usp=sharing).

After we finished with the dataset preparation, we should put it into darknet/data folder.

### Creating configuration files
We have to create it so darknet will know what files to train. We're going to create the following files:
- ground_truth.data
- train.list
- test.list
- names.list

So, let's start with ground_truth.data
```
classes = 1
train = data/pedestrian_ground_truth/train.list
valid = data/pedestrian_ground_truth/test.list
names = data/pedestrian_ground_truth/names.list
# you need to create darknet/backup dir to store your trained weights
backup = backup 
```
We're going to try train our network to find only persons, so we have only one class. train.list contains of paths to images that we'll use to train hence test.list contains of paths to test images.

Let's create the train.list, the easiest way to do it is to use a command (make sure that you're in folder with train and test folders) `find /test -name \*.png > test.list`

As a result you'll get something similar with this ![screen1]()

Repeat this step for test images.

Create the names.list. One category on one string since we have only one it contains one string.
```
Person
```
Last step before we start train our network is to create the .cfg file. To make simplier I copied yolo-voc.cfg and made the next changes:
- Comment line 3 and 4 and uncomment line 5 and 6, because we're going to use it for train, when you'll be testing it change it back. So `batch = 64` means that we will use 64 images on each training step. `subdivisions = 8` means that the batch will be divided by 8 to decrease VRAM requirements. If you have a powerful GPU you can decrease it.
- line 8 and 9: `height = 608` and `width = 608` these parameters are responsible for network-resolution. You can use any value multiple of 32.
- line 237: You can find out amount of filters by `filters = (classes + 5) * 5`, so `filters = 30`
- line 244: Change the number `classes = 1`

To start training we also need a set of convulutional weights. We can get it from the [official site](https://pjreddie.com/media/files/darknet19_448.conv.23).

## Training




