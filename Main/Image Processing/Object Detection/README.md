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