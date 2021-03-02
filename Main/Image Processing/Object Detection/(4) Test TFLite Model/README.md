* [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(1)%20darknet%20(by%20pjreddie))<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb)<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model) **<-- you are here**<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU)<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>

# Part 4: Test TFLite Model

## **<span style="color:red">Current Issues</span>**
When running <code>python TFLite_detection_webcam.py --modeldir=yolo_model</code>, there is an "out of index" error; the script will not run. Possibly an issue from [Part 3](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite) (see Current Issues). 

## Follow this guide to install the Raspberry Pi dependencies for this section:
* Edje Electronics [Youtube Video](https://www.youtube.com/watch?v=aimSGOAUI8Y&ab_channel=EdjeElectronics)
* Edje Electronics [Github](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi#part-1---how-to-train-convert-and-run-custom-tensorflow-lite-object-detection-models-on-windows-10)

## After following the video's instructions:
Create a folder in the <code>tflite</code> directory named <code>yolo_model</code> containing the folowing contents:
* <code>labelmap.txt</code> containing the word <code>cube</code>
* The <code>yolov3-tiny.tflite</code> file created in [Part 3](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite).  
  * Rename the .tflite file to <code>detect.tflite</code>

if you do not have the virtual environment active already, open the console and enter the following:<br>
$ <code>cd ~</code><br>
$ <code>cd tflite</code><br>
$ <code>source /bin/activate</code><br>

To run the YOLOv3-tiny tflite model:<br>
$ <code>python TFLite_detection_webcam.py --modeldir=yolo_model </code>

You should see a video stream. Test it on the cubes.

<p><br>
<p><br>

## **Next -->** [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU)