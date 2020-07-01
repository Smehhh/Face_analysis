from PIL import Image, ImageDraw
import face_recognition
import json
import os
from find_age_and_gender import  *
print(face_recognition)


#picture_of_me = face_recognition.load_image_file("me3.jpg")
#my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
#a = list(my_face_encoding)
ls = os.listdir(path="faces")
picture_of_me = face_recognition.load_image_file("200006200512_324204.jpg")
# print(picture_of_me)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
for i in ls:
    unknown_picture = face_recognition.load_image_file("faces/" + i)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    a = list(unknown_face_encoding)

    age_and_gender = get_age_and_gender("faces/" + i)
    to_json = {'face_encoding': a, "result": str(results[0]), "age": str(age_and_gender[0]), "gender": age_and_gender[1]}
    with open("jsons/" + str(i).split(".")[0] +'.json', 'w') as f:
        f.write(json.dumps(to_json))

print(ls)

#to_json = {'face_encoding': a}

#with open('sw_templates.json', 'w') as f:
    #f.write(json.dumps(to_json))
'''
# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("me3.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")

image = face_recognition.load_image_file("200070400740_38887.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

# Show the picture
pil_image.show()
'''