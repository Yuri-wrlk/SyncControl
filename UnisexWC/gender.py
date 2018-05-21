from enum import Enum

class Gender(Enum):
    male = 0
    female = 1

    gender_names = {male : 'male', female : 'female'}


def get_gender_name(gender):
    if gender == Gender.male:
        return 'Male'
    elif gender == Gender.female:
        return 'Female'
    else:
        return 'None'
