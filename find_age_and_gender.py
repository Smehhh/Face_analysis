from age_and_gender import *
from PIL import Image, ImageDraw, ImageFont

data = AgeAndGender()
data.load_shape_predictor('models/shape_predictor_5_face_landmarks.dat')
data.load_dnn_gender_classifier('models/dnn_gender_classifier_v1.dat')
data.load_dnn_age_predictor('models/dnn_age_predictor_v1.dat')



def get_age_and_gender(photo):
    img = Image.open(photo).convert("RGB")
    result = data.predict(img)
    for info in result:
        gender = info['gender']['value']
        age = info['age']['value']
        gender_percent = int(info['gender']['confidence'])
        age_percent = int(info['age']['confidence'])
        print("age is " + str(age) + " sure on " + str(age_percent) + " %")
        print(f"{gender} (~{gender_percent}%)")
    return ([age, gender])


