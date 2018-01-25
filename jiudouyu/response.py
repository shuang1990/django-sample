CODE_SUCCESS = 200
CODE_ERROR = 500

def call_error(msg='', code=CODE_ERROR, data=None):
    result = {
        'status': False,
        'code': code,
        'msg': msg,
        'data': data
    }
    return result

def call_success(data=None, msg=''):
    result = {
        'status': True,
        'code': CODE_SUCCESS,
        'msg': msg if msg else '成功',
        'data': data
    }
    return result