class NetworkException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Response Status is not 200')


class ParameterNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Parameter is not found to process this request')
