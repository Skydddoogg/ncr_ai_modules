import os
from modules.ResourceFaceRecognition import config
import face_recognition
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def get_all_image_path_from_db():

    if not os.path.isdir(config.db_path):
        os.mkdir(config.db_path)

    all_image_path = [f for f in os.listdir(config.db_path) if os.path.isfile(os.path.join(config.db_path, f)) and '.jpg' in f]

    return all_image_path

def encode_images(list_image_path):

    known_face_encodings = []
    known_face_names = []

    # Encode the fetched images
    for image_name in list_image_path:
        image = face_recognition.load_image_file(os.path.join(config.db_path, image_name))
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(image_name.split('.')[0])

    return known_face_encodings, known_face_names

def display_bbox_in_image(image, face_locations, face_names):

    font_size = 46
    # font = ImageFont.truetype("THSarabunNew.ttf", font_size)
    font = ImageFont.load_default()

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)


        # Draw a label with a name below the face
        draw.rectangle(((left, bottom - font_size), (right, bottom)), fill=(0, 0, 255))
        draw.text((left + 6, bottom - font_size), name, font = font)
        image = np.array(img_pil)

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', image)