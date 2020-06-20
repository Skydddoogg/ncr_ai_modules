# NCR-AI Modules

## วิธีการติดตั้ง
1. ดาวน์โหลดโฟลเดอร์ modules, ไฟล์ environment.yml และ ไฟล์ setup.sh ไปวางไว้ในโฟลเดอร์ Work Space ของเรา
2. ติดตั้ง Miniconda
    * ดูการวิธีการติดตั้งได้ที่ https://docs.conda.io/en/latest/miniconda.html
3. สร้าง Environment และติดตั้ง Package ที่จำเป็นต่อการใช้งาน AI Module
    * รันคำสั่ง `chmod +x setup.sh`
    * รันคำสั่ง `./setup.sh`

## วิธีการใช้งาน
การที่จะสามารถใช้งาน AI Module ได้นั้น จำเป็นจะต้องเปิดใช้งาน Environment ที่สร้างมาก่อน
* รันคำสั่ง `conda activate ncr_ai_module_env`

### Face Recognition
```python
from modules import FaceRecognition

FaceRecognition.play()
```
### Speech-To-Text
```python
from modules import SpeechRecognition

SpeechRecognition.play()
```
### Text-To-Speech
```python
from modules import TextToSpeech

TextToSpeech.play(self_input=True)
```
