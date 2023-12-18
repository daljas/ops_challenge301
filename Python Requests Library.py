import requests

def translate_status_code(code):
    status_codes = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Request Entity Too Large',
        414: 'Request-URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
    }
    return status_codes.get(code, 'Unknown Status Code')

def send_request(url, method):
    try:
        response = requests.request(method, url)
        print('\nResponse Headers:')
        for header, value in response.headers.items():
            print(f'{header}: {value}')

        print('\nStatus Code:', response.status_code)
        print('Status:', translate_status_code(response.status_code))
        print('\nResponse Content:')
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Prompt user for destination URL
    url = input('Enter destination URL: ')

    # Prompt user for HTTP Method
    http_method = input('Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ').upper()

    # Confirm before proceeding
    confirmation = input(f'\nSending {http_method} request to {url}. Do you want to proceed? (yes/no): ')
    if confirmation.lower() != 'yes':
        print('Operation cancelled.')
        exit()

    # Perform the request and print response information
    send_request(url, http_method)
