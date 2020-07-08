import face_recognition
import cv2
import numpy as np
import os
from modules.ResourceFaceRecognition import utils, config
from modules import TextToSpeech, SpeechRecognition
from modules import global_utils

def play():

    # The original code of this function can be found here: https://github.com/ageitgey/face_recognition

    print("Face Recognition (FR) is started")

    # Fetch images from face database
    images = utils.get_all_image_path_from_db()

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Encode images
    known_face_encodings, known_face_names = utils.encode_images(images)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    unknown_c = 0
    unknown_images = []

    while True:

        if unknown_c == 100:
            unknown_c = 0
            temp_stop = True
        else:
            temp_stop = False

        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        unknown_locations = []

        # Only process every other frame of video to save time
        if process_this_frame:

            # Find all the faces and face encodings in the current frame of video
            # -CPU-
            face_locations = face_recognition.face_locations(rgb_small_frame)

            # -GPU-
            # face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=0, model="cnn")

            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            idx = 0
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                if len(face_distances) != 0:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                if name == 'Unknown':
                    top, right, bottom, left = face_locations[idx][0], face_locations[idx][1], face_locations[idx][2], face_locations[idx][3]
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    crop_face = frame[top - config.crop_pad:bottom + config.crop_pad, left - config.crop_pad:right + config.crop_pad]
                    unknown_images.append(crop_face)
                    # cv2.imshow('Unknown', crop_face)
                    if temp_stop:
                        global_utils.show_module_log("FR - Speak your name!")
                        TextToSpeech.play("What is your name?", repeat=False)
                        while True:
                            name_for_unknown = SpeechRecognition.play(return_value = True)
                            if name_for_unknown != '0':
                                global_utils.show_module_log("FR - Now i know you! Nice to meet you.")
                                TextToSpeech.play("Nice to meet you " + name_for_unknown, repeat=False)
                                break
                            else:
                                global_utils.show_module_log("FR - Try again!")
                                TextToSpeech.play("Say your name again", repeat=False)
                        name_for_unknown = name_for_unknown
                        cv2.imwrite(os.path.join(config.db_path, name_for_unknown + '.jpg'), crop_face)
                        images = utils.get_all_image_path_from_db()
                        known_face_encodings, known_face_names = utils.encode_images(images)
                        # cv2.destroyWindow('Unknown')

                face_names.append(name)
                idx += 1

        if len(unknown_images) != 0:
            unknown_c += 2
        else:
            if unknown_c != 0:
                unknown_c -= 1
                cv2.destroyWindow('Unknown')

        process_this_frame = not process_this_frame

        utils.display_bbox_in_image(frame, face_locations, face_names)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()