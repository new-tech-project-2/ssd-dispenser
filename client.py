import requests
from config import SERVER

from drinker import user_register, user_drink, get_token


if __name__ == "__main__":
		
	token = get_token()
	request_body = {'dispenserToken' : token}
	while(true):
		mode = int(input())
		if mode == 0:
			userid = user_register()
			url = SERVER + '/drinker/' + userid
			print(url, request_body)
			#requests.post(url, data = request_body)
		elif mode == 1:		
			userid = user_register()
                        url = SERVER + '/drinker/' + userid
                        print(url, request_body)
                        #requests.patch(url, data = request_body)


