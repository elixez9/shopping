from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('787830567A4F6161557458537276564367347545484A644B3936757757755048393259323974685949324D3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما{code}:',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
