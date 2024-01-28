from fastapi import Form, UploadFile


class BuyerCreate:
    def __init__(self, full_name: str = Form(...), display_name: str = Form(...), address: str = Form(...),
                 postal_code: str = Form(...), city: str = Form(...), phone_number: str = Form(...),
                 gender: str = Form(...), date_of_birth: str = Form(...), profile_image: UploadFile = Form(...),
                 email: str = Form(...), password: str = Form(...)):
        self.full_name = full_name
        self.display_name = display_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.phone_number = phone_number
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.profile_image = profile_image
        self.email = email
        self.password = password
