class NetworkException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Response Status is not 200')
