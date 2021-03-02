* [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(1)%20Darknet%20(by%20pjreddie))<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(2)%20YOLOv3-Tiny%20to%20.pb)<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(3)%20.pb%20to%20TFLite)<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(4)%20Test%20TFLite%20Model)<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(5)%20Compile%20on%20EdgeTPU)<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Object%20Detection/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>

<p><br>
<p><br>

# Objectives
* Create an object detection algorithm that detects cubes.<br>
  * Must be able to run on a Raspberry Pi 4 2GB.
  * Must be able to run on the Coral Edge TPU.
* Must maintain a minimum average framerate of 10 FPS

<p><br>
<p><br>

# Progress
## Object Detection
* A dataset has been created.
* The model has been trained.
* The .weights file has been converted to a .pb file
* **\<ISSUE>** The .pb file can be converted to a .tflite model but is not quantized to run on the Edge TPU
*  **\<ISSUE>** The .tflite file will not run on the Raspberry Pi. Index Error

## Edge TPU
* Tested on sample object detection model and confirmed to be working as intended.
* **\<ISSUE>** Unable to test the TPU on our trained model due to previously stated issues.