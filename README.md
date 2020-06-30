# NCR-AI Modules

## วิธีการติดตั้งบน Windows
1. ติดตั้ง Miniconda
    * ดูการวิธีการติดตั้งได้ที่ https://docs.conda.io/en/latest/miniconda.html
    * เมื่อติดตั้งเสร็จแล้วให้เปิด Anaconda Prompt
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/2.png)
    * ตรวจสอบการติดตั้งโดยการรันคำสั่ง `conda` แล้วผลลัพธ์ควรเป็นไปตามรูปด้านล่าง
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/3.PNG)
2. สร้าง Environment สำหรับการจัดเก็บ Package โดยแนะนำว่าใน Environment ต้องใช้ Python 3.5 (ในกรณีที่ต้องการใช้ Environment ที่มีอยู่แล้วให้ข้ามไปทำข้อ 4. เลย)
    * รันคำสั่ง `conda create -n *ชื่อ Environment* python=3.5` เช่น `conda create -n ai_module_env python=3.5`
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/4.PNG)
3. เปิดใช้งาน Environment ที่สร้าง
    * รันคำสั่ง `conda activate *ชื่อ Environment*` เช่น `conda activate ai_module_env`
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/5.PNG)
4. ติดตั้ง Package ที่จำเป็นต่อการใช้งาน AI Module ลงใน Environment ที่สร้าง
    * รันคำสั่ง `conda install -c menpo dlib`
    * รันคำสั่ง `conda install -c akode face_recognition_models`
    * รันคำสั่ง `conda install -c conda-forge opencv`
    * รันคำสั่ง `conda install -c conda-forge speechrecognition`
    * รันคำสั่ง `pip install gTTS`
    * รันคำสั่ง `pip install playsound`
    * รันคำสั่ง `conda install pyaudio`

## วิธีการติดตั้งบน Raspberry Pi 3
1. ติดตั้ง Virtualenv
   * รันคำสั่ง `pip install virtualenv`
   * เมื่อติดตั้งเสร็จแล้วให้ตรวจสอบโดยการรันคำสั่ง `virtualenv` แล้วผลลัพธ์ควรเป็นไปตามรูปด้านล่าง
   ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/pi_1.PNG)
2. สร้างโฟลเดอร์ Work Space ของเรา โดยในตัวอย่างนี้มีชื่อว่า `test_pi`
![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/pi_2.PNG)
3. เข้าไปในโฟลเดอร์ Work Space และ สร้าง Environment สำหรับการจัดเก็บ Package (ในกรณีที่ต้องการใช้ Environment ที่มีอยู่แล้วให้ข้ามไปทำข้อ 4. เลย)
   * รันคำสั่ง `virtualenv *ชื่อ Environment*` เช่น `virtualenv ai_module_env`
   ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/pi_3.PNG)
4. เปิดใช้งาน Enviroment ที่สร้าง เพื่อติดตั้ง Package ที่จำเป็นลงไป
   * รันคำสั่ง `source *ชื่อ Environment*/bin/activate` เช่น `source ai_module_env/bin/activate` แล้วผลลัพธ์ควรเป็นดังรูปด้านล่าง
   ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/pi_4.PNG)
5. ติดตั้ง Package ที่จำเป็นต่อการใช้งาน AI Module ลงใน Environment ที่สร้าง
   * 5.1 OpenCV
      * รันคำสั่ง `sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100 libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 libatlas-base-dev libjasper-dev`
      * รันคำสั่ง `pip install opencv-contrib-python==4.1.0.25`
   * 5.2 PiCamera
      * รันคำสั่ง `pip install "picamera[array]"`
   * 5.3 Pygame
      * รันคำสั่ง `pip install pygame`
   * 5.4 Google Text-to-Speech
      * รันคำสั่ง `pip install gTTS`
   * 5.5 Speech Recognition
      * รันคำสั่ง `pip install SpeechRecognition`
   * 5.6 Dlib
      * รันคำสั่ง `sudo apt-get update`
      * รันคำสั่ง `sudo apt-get upgrade`
      * รันคำสั่ง `sudo apt-get install build-essential cmake gfortran git wget curl graphicsmagick libgraphicsmagick1-dev libatlas-dev libavcodec-dev libavformat-dev libboost-all-dev libgtk2.0-dev libjpeg-dev liblapack-dev libswscale-dev pkg-config python3-dev python3-numpy python3-pip zip`
      * รันคำสั่ง `sudo apt-get clean`
      * รันคำสั่ง `sudo nano /etc/dphys-swapfile`
      * เปลี่ยน `CONF_SWAPSIZE=100` เป็น `CONF_SWAPSIZE=1024` และออกจาก nano โดย Ctrl + X --> Y --> กด Enter
      * รันคำสั่ง `sudo /etc/init.d/dphys-swapfile restart`
      * รันคำสั่ง `mkdir -p dlib`
      * รันคำสั่ง `git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/`
      * รันคำสั่ง `sudo chown -R pi:pi dlib/`
      * รันคำสั่ง `cd ./dlib`
      * รันคำสั่ง `python setup.py install --compiler-flags "-mfpu=neon"` ในขึ้นตอนนี้จะใช้เวลานานมาก...
   * 5.7 Face Recognition
      * รันคำสั่ง `pip install face_recognition`
      * รันคำสั่ง `sudo nano /etc/dphys-swapfile`
      * เปลี่ยน `CONF_SWAPSIZE=1024` เป็น `CONF_SWAPSIZE=100` และออกจาก nano โดย Ctrl + X --> Y --> กด Enter
      * รันคำสั่ง `sudo /etc/init.d/dphys-swapfile restart`
      * รันคำสั่ง `sudo apt-get install --no-install-recommends xserver-xorg xinit raspberrypi-ui-mods`
   * 5.7 PyAudio
      * รันคำสั่ง `pip install pyaudio`

## ตัวอย่างการใช้งานเบื้องต้น
1. ดาวน์โหลดโฟลเดอร์ modules ไปวางไว้ในโฟลเดอร์ Work Space ของเรา
2. เข้าไปในโฟลเดอร์ Work Space ของเรา และสร้างไฟล์ Script ที่มีชื่อว่า `test_module.py`
3. เขียนโค้ดเพื่อใช้งาน AI Module ลงไปในไฟล์ที่สร้าง โดยแต่ละ Module จะมีการใช้งานที่ต่างกันดังนี้
   * Face Recognition
      ```python
      from modules import FaceRecognition

      FaceRecognition.play()
      ```
   * Speech-To-Text
      ```python
      from modules import SpeechRecognition

      SpeechRecognition.play()
      ```
   * Text-To-Speech
      ```python
      from modules import TextToSpeech

      TextToSpeech.play(self_input=True)
      ```
4. เปิดใช้งาน Environment (ถ้าเปิดใช้งานอยู่แล้ว ไม่ต้องรันคำสั่งอีกรอบ)
5. รันโปรแกรม
   * รันคำสั่ง `python test_module.py`
