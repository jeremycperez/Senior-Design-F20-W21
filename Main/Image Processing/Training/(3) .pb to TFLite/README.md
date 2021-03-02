* [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(1)%20darknet%20(by%20pjreddie))<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb)<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite) **<-- you are here**<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model)<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU)<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>

# Part 3: Converting .pb to TFLite

## **<span style="color:red">Current Issues</span>**
To be capable of running on the Coral Edge TPU, the TFLite model has to be quantized to UINT8 or INT8. It currently does not appear to quantize post-training; <span style="color:red">therefore it will not be able to be compiled for our application at this time.</span> It appears to convert with FLOAT values. 

## Prerequisites
* YOLOv3-tiny Frozen Graph (.pb file)
* Python 3.5.9
* Tensorflow 1.15

## In Ubuntu Console:
$ <code>tflite_convert --graph_def_file=/home/tensorflow-yolo-v3/yolov3-tiny-cube.pb --output_file=[[~CHOOSE DIRECTORY TO SAVE FILE~]]/yolov3-tiny.tflite --input_format=TENSORFLOW_GRAPHDEF --output_format=TFLITE --input_shape=1,416,416,3 --input_array=inputs --output_array=output_boxes --inference_type=QUANTIZED_UINT8 --input_data_type=FLOAT --optimization[tf.lite.Optimization.DEFAULT] --post_training_quantization</code><br>
<p><br>
<p><br>

## **Next -->** [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model)