from rest_framework.response import Response
class MyResponse(Response):
    def __init__(self, data_status=200, data_msg='ok', results=None, http_status=None, headers=None, exception=None, **kwargs):
        # data的初始状态：状态码与状态信息
        data = {
            'data': {
                'results': {},
                'meta': {
                    'status': data_status,
                    'msg': data_msg
                }
            }
        }
        if results is not None:
            data['data']['results'] = results
        if kwargs is not None:
            data['data'].update(kwargs)

        super().__init__(data=data, status=http_status, headers=headers, exception=exception)
