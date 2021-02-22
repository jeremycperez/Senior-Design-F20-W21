# Getting CUDA 11.2 to work in Ubuntu 20.04 or 20.10
## Download CUDA
  Link to [CUDA](https://developer.nvidia.com/cuda-downloads) download page<br>
  Steps
* OS - Linux
* Arch - x86_64
* Distro - Ubuntu
* Ver - 20.04
* Install type - runfile (local)<br>
<p>$ <code>wget https://developer.download.nvidia.com/compute/cuda/11.2.1/local_installers/cuda_11.2.1_460.32.03_linux.run</code>
<p><br><p><br>

## Blacklist Nouveau
in /ect/modprobe.d, create a .conf file (i.e. nouveau_blacklist.conf) that containes the following content:
* blacklist nouveau
* options nouveau modeset=0
<p>Then open the console and run:<br>
<p>$ <code>sudo update-initramfs -u</code><br>
$ <code>sudo reboot</code>
<p><br><p><br>

## Disable Secure Boot
In the console:
<p>$ <code>sudo apt install mokutil</code><br>
$ <code>sudo mokutil --disable-validation</code><br>
create a password (write it down for the next step)<br>
<p>$ <code>sudo reboot</code><br>
<p>Click "Change Secure Boot state"<br>
<p>You will have to end the character it requests in your password (index starts at 1)<br>
<p><br>
<p>Example: password: abcdefgh<br>
<p>ENTER PASS WORD CHARACTER 2: <br>
<p>Answer: "b"<br>      
<p>Disable Secure Boot<br>
<p><br><p><br>

## Install CUDA 11.2
<p>$ <code>sudo init 3</code>
<p>enter username and password when prompted. 
<p>$ <code>sudo sh cuda_11.2.1_460.32.03_linux.run</code>
<p>$ <code>export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}</code>
<p>$ <code>export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}</code>
<p>$ <code>sudo init 5</code>
<p><br><p><br>

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