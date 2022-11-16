OPTION_TYPES = {
    'C': 'call',
    'P': 'put'
}

def decode_option(encoded_option: str) -> dict:
    response = {}
    response['symbol'] = encoded_option[:-15]
    response['year'] = int(encoded_option[-15:-13]) + 2000
    response['month'] = int(encoded_option[-13:-11])
    response['day'] = int(encoded_option[-11:-9])
    response['option_type'] = OPTION_TYPES[encoded_option[-9:-8]]
    response['price'] = float(encoded_option[-8:]) / 1000
    return response

if __name__ == '__main__':
    print(decode_option('AAPL150416C00031420'))