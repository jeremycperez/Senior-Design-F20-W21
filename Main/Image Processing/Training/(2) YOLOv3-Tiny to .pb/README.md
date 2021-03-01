# Part 2
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