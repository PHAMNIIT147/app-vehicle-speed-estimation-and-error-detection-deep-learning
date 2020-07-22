<p align="center">
  <img src="assets/logo/logo.png" width="200">
</p>
<h1 align="center">VAA Ai Go!</h1>
<h3 align="center">Vehicle Speed Estimation and Error Detection Based on Deep Learning - Internet Of Things</h3>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/github/license/jesusrp98/spacex-go.svg?style=for-the-badge">
  </a>
  <a href="https://github.com/jesusrp98/spacex-go/stargazers">
    <img src="https://img.shields.io/github/stars/jesusrp98/spacex-go.svg?style=for-the-badge">
  </a>
  <a href="https://www.paypal.com/paypalme/my/profile">
    <img src="https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge">
  </a>
  <a href="https://www.patreon.com/jesusrp98">
    <img src="https://img.shields.io/badge/Support-Patreon-orange.svg?style=for-the-badge">
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.chechu.cherry">
    <img src="https://img.shields.io/badge/Google-PlayStore-green.svg?style=for-the-badge">
  </a>
</p> 

### About the project

The purpose of this project is to develop the ultimate SpaceX experience in a variety of platforms. A single experience, from a single codebase.

From the start, SpaceX GO! has been developed to be light-weight, fast and easy to use. It takes all the data from the open-source r/SpaceX REST API, which can be found [here](https://github.com/r-spacex/SpaceX-API).

This project has been built using the [Flutter](https://flutter.io/) framework, which allows to build an app for mobile, desktop & web, from a single codebase.

<p align="center">
  <img src="assets/img/picture.png" width="256" hspace="4">
</p>

## Features



## Download & install



## Built with

- [Flutter](https://flutter.dev/) - Beautiful native apps in record time.
- [Android Studio](https://developer.android.com/studio/index.html/) - Tools for building apps on every type of Android device.
- [Visual Studio Code](https://code.visualstudio.com/) - Code editing. Redefined.

## Authors


## Contributing


## License

This project is licensed under the GNU GPL v3 License - see the [LICENSE.md](LICENSE.md) file for details.

# Reference 
- This project using model build from Factory (Clean Architecture)
## MVC Project
```
- src/
  |_ controllers/
  |  |_ FarmeLabel.py
  |  |   + mouseMoveEvent(event)
  |  |   + setMouseEvent(data)
  |  |   + getMouseCursorPos()
  |  |   + mouseReleaseEvent(event)
  |  |   + mouseRelaseEvent(event)
  |  |   + mousePressEvent(event)
  |  |   + paintEvent(event)
  |  |   + getPonts(event)
  |  |   + createContecMenu()
  |  |    -> processing user actions
  |  |_ ImageProcessingSettingsDialog.py
  |  |   + updateStoreSettingFromDialog()
  |  |   + updateDialogSettingFromStored()
  |  |   + resetAllDialogToDefaults()
  |  |   + smothTypeChange(input)
  |  |   + validateDialog()
  |  |   + resetSmoothDialogDefault()
  |  |   + resetDilateDialogToDefault()
  |  |   + resetErodeDialogToDefault()
  |  |   + resetFlipDialogToDefault()
  |  |   + resetCannyDialogToDefault() 
  |_ model/
  |  |_ core/
  |  |   -> processing call YoloV3 algorithm. The enviroment relationship of object detection
  |  |   + ./
  |  |_ Buffer.py 
  |  |   + add(data, dropFull=False)
  |  |   + get()
  |  |   + clear()
  |  |   + size()
  |  |   + maxSize()
  |  |   + ifFull()
  |  |   + isEmpty()
  |  |_ CaptureThread.py 
  |  |   + run() # by overriding the run() method in a subclass.
  |  |   + stop()
  |  |   + connectToCamera()
  |  |   + disconnectCamera()
  |  |   + isCameraConnected()
  |  |   + getInputSourceWdith()
  |  |   +  getInputSourceHeight()
  |  |   + updateFPS(timeElapsed)
  |  |_ MatToQImage.py
  |  |   + matQImage(data)
  |  |_ ProcessingThread.py
  |  |   + run() # by overriding the run() method in a subclass.
  |  |   + doShowImage(value)
  |  |   + updateFPS(timeEplased)
  |  |   + stop()
  |  |   + updateBoxesBufferMax(imgProcFlags)
  |  |   + updateImageProcessingFlags(imgProcFlags)
  |  |   + updateImageProcessing(imgProcSettings)
  |  |   + setROI(roi)
  |  |   + getCurrentROI()
  |  |_ SharedImageBuffer.py
  |  |   + add(deviceUrl, imageBuffer, sync=False)
  |  |   + getByDeviceUrl(deviceUrl)
  |  |   + removeByDevicesUrl(deviceUrl)
  |  |   + sync(deviceUrl)
  |  |   + wakeAll()
  |  |   + setSyncEnabled(enable)
  |  |   + isSyncEnabledForDeviceUrl(deviceUrl)
  |  |   + getSyncEnbaled()
  |  |   + containsImageBufferForDeviceUrl(deviceUrl)
  |_ views/
  |  | -> UI layers 
```


## SORT

<hr>

A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences.
See an example [video here](https://motchallenge.net/movies/ETH-Linthescher-SORT.mp4).

By Alex Bewley  

### Introduction

SORT is a barebones implementation of a visual multiple object tracking framework based on rudimentary data association and state estimation techniques. It is designed for online tracking applications where only past and current frames are available and the method produces object identities on the fly. While this minimalistic tracker doesn't handle occlusion or re-entering objects its purpose is to serve as a baseline and testbed for the development of future trackers.

SORT was initially described in [this paper](http://arxiv.org/abs/1602.00763). At the time of the initial publication, SORT was ranked the best *open source* multiple object tracker on the [MOT benchmark](https://motchallenge.net/results/2D_MOT_2015/).

**Note:** A significant proportion of SORT's accuracy is attributed to the detections.
For your convenience, this repo also contains *Faster* RCNN detections for the MOT benchmark sequences in the [benchmark format](https://motchallenge.net/instructions/). To run the detector yourself please see the original [*Faster* RCNN project](https://github.com/ShaoqingRen/faster_rcnn) or the python reimplementation of [py-faster-rcnn](https://github.com/rbgirshick/py-faster-rcnn) by Ross Girshick.

**Also see:**
A new and improved version of SORT with a Deep Association Metric implemented in tensorflow is available at [https://github.com/nwojke/deep_sort](https://github.com/nwojke/deep_sort) .

### License

SORT is released under the GPL License (refer to the LICENSE file for details) to promote the open use of the tracker and future improvements. If you require a permissive license contact Alex (alex@bewley.ai).

### Citing SORT

If you find this repo useful in your research, please consider citing:

    @inproceedings{Bewley2016_sort,
      author={Bewley, Alex and Ge, Zongyuan and Ott, Lionel and Ramos, Fabio and Upcroft, Ben},
      booktitle={2016 IEEE International Conference on Image Processing (ICIP)},
      title={Simple online and realtime tracking},
      year={2016},
      pages={3464-3468},
      keywords={Benchmark testing;Complexity theory;Detectors;Kalman filters;Target tracking;Visualization;Computer Vision;Data Association;Detection;Multiple Object Tracking},
      doi={10.1109/ICIP.2016.7533003}
    }


### Dependencies:

To install required dependencies run:
```
$ pip install -r requirements.txt
```


### Demo:

To run the tracker with the provided detections:

```
$ cd path/to/sort
$ python sort.py
```

To display the results you need to:

1. Download the [2D MOT 2015 benchmark dataset](https://motchallenge.net/data/2D_MOT_2015/#download)
0. Create a symbolic link to the dataset
  ```
  $ ln -s /path/to/MOT2015_challenge/data/2DMOT2015 mot_benchmark
  ```
0. Run the demo with the ```--display``` flag
  ```
  $ python sort.py --display
  ```


### Main Results

Using the [MOT challenge devkit](https://motchallenge.net/devkit/) the method produces the following results (as described in the paper).

 Sequence       | Rcll | Prcn |  FAR | GT  MT  PT  ML|   FP    FN  IDs   FM|  MOTA  MOTP MOTAL
--------------- |:----:|:----:|:----:|:-------------:|:-------------------:|:------------------:
 TUD-Campus     | 68.5 | 94.3 | 0.21 |  8   6   2   0|   15   113    6    9|  62.7  73.7  64.1
 ETH-Sunnyday   | 77.5 | 81.9 | 0.90 | 30  11  16   3|  319   418   22   54|  59.1  74.4  60.3
 ETH-Pedcross2  | 51.9 | 90.8 | 0.39 | 133  17  60  56|  330  3014   77  103|  45.4  74.8  46.6
 ADL-Rundle-8   | 44.3 | 75.8 | 1.47 | 28   6  16   6|  959  3781  103  211|  28.6  71.1  30.1
 Venice-2       | 42.5 | 64.8 | 2.75 | 26   7   9  10| 1650  4109   57  106|  18.6  73.4  19.3
 KITTI-17       | 67.1 | 92.3 | 0.26 |  9   1   8   0|   38   225    9   16|  60.2  72.3  61.3
 *Overall*      | 49.5 | 77.5 | 1.24 | 234  48 111  75| 3311 11660  274  499|  34.0  73.3  35.1


### Using SORT in your own project

Below is the gist of how to instantiate and update SORT. See the ['__main__'](https://github.com/abewley/sort/blob/master/sort.py#L239) section of [sort.py](https://github.com/abewley/sort/blob/master/sort.py#L239) for a complete example.
    
    from sort import *
    
    #create instance of SORT
    mot_tracker = Sort() 
    
    # get detections
    ...
    
    # update SORT
    track_bbs_ids = mot_tracker.update(detections)

    # track_bbs_ids is a np array where each row contains a valid bounding box and track_id (last column)
    ...
    
 
