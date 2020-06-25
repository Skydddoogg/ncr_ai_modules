# NCR-AI Modules

## วิธีการติดตั้งบน Windows
1. ติดตั้ง Miniconda
    * ดูการวิธีการติดตั้งได้ที่ https://docs.conda.io/en/latest/miniconda.html
    * เมื่อติดตั้งเสร็จแล้วให้เปิด Anaconda Prompt
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/2.png)
    * ตรวจสอบการติดตั้งโดยการรันคำสั่ง `conda` แล้วผลลัพธ์ควรเป็นไปตามรูปด้านล่าง
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/3.PNG)
2. สร้าง Environment สำหรับการจัดเก็บ Library (ในกรณีที่ต้องการใช้ Environment ที่มีอยู่แล้วให้ข้ามไปทำข้อ 4. เลย)
    * รันคำสั่ง `conda create -n *ชื่อ Environment* python=3.5` เช่น `conda create -n ai_module_env python=3.5`
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/4.PNG)
3. เข้าไปในโฟลเดอร์ Work Spac ของเรา และ เปิดใช้งาน Environment ที่สร้าง
    * รันคำสั่ง `conda activate *ชื่อ Environment*` เช่น `conda activate ai_module_env`
    ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/5.PNG)
4. ติดตั้ง Library ที่จำเป็นต่อการใช้งาน AI Module ลงใน Environment ที่สร้าง
    * รันคำสั่ง `conda install -c menpo dlib`
    * รันคำสั่ง `conda install -c akode face_recognition_models`
    * รันคำสั่ง `conda install -c conda-forge opencv`
    * รันคำสั่ง `conda install -c conda-forge speechrecognition`
    * รันคำสั่ง `pip install gTTS`
    * รันคำสั่ง `pip install playsound`
    * รันคำสั่ง `conda install pyaudio`
## วิธีการติดตั้งบน Raspberry Pi 3

## ตัวอย่างการใช้งานเบื้องต้น
1. ดาวน์โหลดโฟลเดอร์ modules ไปวางไว้ในโฟลเดอร์ Work Space ของเรา (ในตัวอย่างนี้โฟลเดอร์ Work Space มีชื่อว่า `test`)
![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/1.PNG)
2. เข้าไปในโฟลเดอร์ Work Space ของเรา และสร้างไฟล์ Script ที่มีชื่อว่า `test_module.py`
![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/ex1.PNG)
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
   * รันคำสั่ง `conda activate *ชื่อ Environment*`
5. รันโปรแกรม (insert image)
   * รันคำสั่ง `python test_module.py`
   ![](https://github.com/Skydddoogg/ncr_ai_modules/blob/master/images/ex2.PNG)
