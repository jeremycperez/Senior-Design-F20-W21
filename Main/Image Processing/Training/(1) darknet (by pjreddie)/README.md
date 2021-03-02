* [Part 1: Training YOLOv3-Tiny Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(1)%20darknet%20(by%20pjreddie)) **<-- you are here**<br>
* [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb)<br>
* [Part 3: Converting .pb to TFLite](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(3)%20.pb%20to%20TFLite)<br>
* [Part 4: Test TFLite Model](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(4)%20Test%20TFLite%20Model)<br>
* [Part 5: Make TFLite Model EdgeTPU Compatible](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(5)%20Compile%20on%20EdgeTPU)<br>
* [Part 6: Run EdgeTPU Object Detection](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(6)%20Test%20Edge-compatible%20TFlite%20Model)<br>


# Part 1: Training YOLOv3-Tiny Model
## **<span style="color:red">Current Issues</span>**
Unable to get OpenCV working with Darknet and CUDA

## Prerequisites
* Ubuntu (I used Kubuntu)
* A CUDA-capable GPU
* CUDA 11.2
* OpenCV
* Darknet
# Part 1.1: Getting CUDA 11.2 to work in Ubuntu 20.04 or 20.10
## Download CUDA
  Link to [CUDA](https://developer.nvidia.com/cuda-downloads) download page<br>
  Steps
* OS - Linux
* Arch - x86_64
* Distro - Ubuntu
* Ver - 20.04
* Install type - runfile (local)<br>
<p>$ <code>wget https://developer.download.nvidia.com/compute/cuda/11.2.1/local_installers/cuda_11.2.1_460.32.03_linux.run</code>

<p><br>

## Blacklist Nouveau
in /ect/modprobe.d, create a .conf file (i.e. nouveau_blacklist.conf) that contains the following content:
* blacklist nouveau
* options nouveau modeset=0
<p>Then open the console and run:<br>
<p>$ <code>sudo update-initramfs -u</code><br>
$ <code>sudo reboot</code>

<p><br>

## Disable Secure Boot
In the console:
<p>$ <code>sudo apt install mokutil</code><br>
$ <code>sudo mokutil --disable-validation</code><br>
create a password (write it down for the next step)<br>
<p>$ <code>sudo reboot</code><br>
<p>Click "Change Secure Boot state"<br>
<p>You will have to end the character it requests in your password (index starts at 1)<br>

    Example password: abcdefgh<br>
    ENTER PASS WORD CHARACTER 2: 
    Answer: "b"      
    Disable Secure Boot



## Install CUDA 11.2
<p>$ <code>sudo init 3</code>
<p>enter username and password when prompted. 
<p>$ <code>sudo sh cuda_11.2.1_460.32.03_linux.run</code>
<p>$ <code>export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}</code>
<p>$ <code>export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}</code>
<p>$ <code>sudo init 5</code>

<p><br>

## Verify Installation
<p>$ <code>cd ~</code>
<p>$ <code>cd /usr/local/cuda-11.2/samples/4_Finance/BlackScholes</code>
<p>$ <code>make</code>
<p>$ <code>./BlackScholes</code>
<p>If you get a warning that says "...Permission Denied," try:
<p>$ <code>cd ~</code>
<p>$ <code>cd /usr/local/cuda-11.2/samples/4_Finance/BlackScholes</code>
<p>$ <code>sudo make -k</code>
<p>$ <code>./BlackScholes</code>
<p>If the installed correctly, you should see "Test Passed"

<p><br>

# Part 1.2: Installing Darknet (*see [Darknet Install](https://pjreddie.com/darknet/install/)*)

## In the console:
$ <code>cd ~</code><br>
$ <code>git clone https://github.com/pjreddie/darknet.git</code><br>

<p><br>

Access the darknet directory, open the <code>Makefile</code>, and make the foillowing changes:
* <code>GPU=1</code><br>
  * *if CUDA is installed*
* <code>OPENCV=1</code><br>
  * *if OpenCV is installed*

Move the files on this page to their repective destination (i.e. copy/paste contents of "data" to . . /darknet/data)
## In the console:
$ <code>cd darknet</code><br>
$ <code>make</code><br>

<p>Begin training the model:<br>

$ <code>./darknet detector train data/obj.data cfg/yolov3-tiny-ver2.cfg darknet53.conv.74</code><br>

The weights will be saved to . . /darknet/backup

<p><br>
<p><br>

## **Next -->** [Part 2: Converting YOLO Weights to .pb](https://github.com/jeremycperez/Senior-Design-F20-W21/tree/master/Main/Image%20Processing/Training/(2)%20YOLOv3-Tiny%20to%20.pb)<br>