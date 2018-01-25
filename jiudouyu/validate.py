import re

def is_phone(phone=''):
    phone = phone.strip()
    pattern = r"^(13\d|14[57]|15[012356789]|18\d|17[0135678])\d{8}$"
    if phone == '' or re.compile(pattern).match(phone) == None:
        raise Exception("invalid_phone")


def is_name(name=''):
    name = name.strip()
    pattern = r'''#[a-z\d~!@\#$%^&*()_+{}|\[\]\-=:<>?/"'\\\\]#'''
    if name == '' or re.compile(pattern).match(name) == None:
        raise Exception("invalid_real_name")


def is_idcard(id_card=''):
    id_card = id_card.strip().lower()
    pattern = r"^(\d{15}|\d{17}X|\d{18})$"

    if id_card == '' or re.compile(pattern).match(id_card) == None:
        result = True
    elif len(id_card) == 18:
        result = idcard_checksum18(id_card)
    elif len(id_card) == 15:
        id_card = idcard_15to18(id_card)
        result = idcard_checksum18(id_card)
    else:
        result = False

    if not result:
        raise Exception('invalid_id_card')


def idcard_15to18(id_card):
    if len(id_card) != 15:
        return False
    else:
        #如果身份证顺序码是996 997 998 999，这些是为百岁以上老人的特殊编码
        if id_card[12:15] not in ['996', '997', '999']:
            id_card = id_card[0:6] + '18' + id_card[6:]
        else:
            id_card = id_card[0:6] + '19' + id_card[6:]
    id_card = id_card + idcard_verify_number(id_card)
    return id_card

def idcard_checksum18(id_card):
    if len(id_card) != 18:
        return False

    idcard_base = id_card[0:17]
    if idcard_verify_number(idcard_base) != id_card[17]:
        return False
    else:
        return True


def idcard_verify_number(idcard_base):
    if len(idcard_base) != 17:
        return False

    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    verify_number_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    checksum = 0

    for i in range(len(idcard_base)):
        checksum += int(idcard_base[i]) * factor[i]

    mod = checksum % 11
    return verify_number_list[mod]


