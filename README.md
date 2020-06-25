# NCR-AI Modules

## วิธีการติดตั้งบน Windows
1. ดาวน์โหลดโฟลเดอร์ modules ไปวางไว้ในโฟลเดอร์ Work Space ของเรา (ในตัวอย่างนี้โฟลเดอร์ Work Space มีชื่อว่า `test`)
2. ติดตั้ง Miniconda
    * ดูการวิธีการติดตั้งได้ที่ https://docs.conda.io/en/latest/miniconda.html
    * เมื่อติดตั้งเสร็จแล้วให้เปิด Anaconda Prompt (insert image)
    * ตรวจสอบการติดตั้งโดยการรันคำสั่ง `conda` แล้วผลลัพธ์ควรเป็นไปตามรูปด้านล่าง (insert image)
3. สร้าง Environment สำหรับการจัดเก็บ Library (ในกรณีที่ต้องการใช้ Environment ที่มีอยู่แล้วให้ข้ามไปทำข้อ 4. เลย)(insert image)
    * รันคำสั่ง `conda create -n *ชื่อ Environment* python=3.5` เช่น `conda create -n ai_module_env python=3.5`
4. เข้าไปในโฟลเดอร์ Work Spac ของเรา และ เปิดใช้งาน Environment ที่สร้าง (insert image)
    * รันคำสั่ง `conda activate *ชื่อ Environment*` เช่น `conda activate ai_module_env`
5. ติดตั้ง Library ที่จำเป็นต่อการใช้งาน AI Module ลงใน Environment ที่สร้าง
    * รันคำสั่ง `conda install -c menpo dlib`
    * รันคำสั่ง `conda install -c akode face_recognition_models`
    * รันคำสั่ง `conda install -c conda-forge opencv`
    * รันคำสั่ง `conda install -c conda-forge speechrecognition`
    * รันคำสั่ง `pip install gTTS`
    * รันคำสั่ง `pip install playsound`
    * รันคำสั่ง `conda install pyaudio`
## วิธีการติดตั้งบน Raspberry Pi 3

## ตัวอย่างการใช้งานเบื้องต้น
1. เข้าไปในโฟลเดอร์ Work Space ของเรา และสร้างไฟล์ Script ที่มีชื่อว่า `test_module.py`
2. เขียนโค้ดเพื่อใช้งาน AI Module ลงไปในไฟล์ที่สร้าง โดยแต่ละ Module จะมีการใช้งานที่ต่างกันดังนี้
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
3. เปิดใช้งาน Environment (ถ้าเปิดใช้งานอยู่แล้ว ไม่ต้องรันคำสั่งอีกรอบ)
   * รันคำสั่ง `conda activate *ชื่อ Environment*`
4. รันโปรแกรม (insert image)
   * รันคำสั่ง `python test_module.py`
