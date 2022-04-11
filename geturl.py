from krakenio import Client

api = Client('c7b0b157e26ec1d04d2c5b47ed1368b6', '518702c6396672227c6228be527146921e46868a')

data = {
    'wait': True
}

result = api.upload('/img1.jpg', data);

if result.get('success'):
    print (result.get('kraked_url'))
else:
    print( result.get('message'))