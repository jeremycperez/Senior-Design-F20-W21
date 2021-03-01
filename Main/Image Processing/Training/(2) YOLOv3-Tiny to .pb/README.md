* [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(1)%20darknet%20(by%20pjreddie))<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb) **<-- you are here**<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model)<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU)<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>

# Part 2: Converting YOLO Weights to .pb
## After training the darknet YOLOv3-tiny model, copy the directory of the weights and class files
  (i.e)
  * /home/darknet/backup/yolov3-tiny-cube_final.weights
  * /home/darknet/data/classes.names
### This part will cover the conversion from .weights to .pb to later be configured into a .tflite file.

## Prerequisites
* YOLOv3-tiny weights and classes
* Python 3.5.9
* Tensorflow 1.15
* [Mystic123/tensorflow-yolo-v3](https://github.com/mystic123/tensorflow-yolo-v3)

## In Ubuntu Console:

$ <code>git clone https://github.com/mystic123/tensorflow-yolo-v3</code><br>
$ <code>cd tensorflow-yolo-v3</code><br>
$ <code>python3.5 convert_weights_pb.py --class_names /home/darknet/data/classes.names --weights_file /home/darknet/backup/yolov3-tiny-cube_final.weights --data_format "NHWC" --tiny</code><br>

The .pb file will be saved to the /home/tensorflow-yolo-v3 directory
<p><br>
<p><br>

## **Next -->** [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)