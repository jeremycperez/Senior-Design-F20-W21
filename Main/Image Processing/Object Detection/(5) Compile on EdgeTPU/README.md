 * [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(1)%20darknet%20(by%20pjreddie))<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb)<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model)<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU) **<-- you are here**<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>

# Part 5: Make TFLite Model EdgeTPU Compatible

## **<span style="color:red">Current Issues</span>**
Problems with running tflite model (see Current Issues in [Part 3](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)).

## On the Raspberry Pi (*see [Edge TPU Compiler](https://coral.ai/docs/edgetpu/compiler/#system-requirements)*):
$ <code>curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -</code><br>
$ <code>echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list</code><br>
$ <code>sudo apt-get update</code><br>
$ <code>sudo apt-get install edgetpu-compiler</code><br>
<p><br>
(uncertain if the below command works)<br>
$ <code>edgetpu_compiler /home/tflite/yolo_model/detect.tflite -o /home/tflite/yolo_model/</code>

<p><br>
<p><br>

## **Next -->** [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>
