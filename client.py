import requests
from config import SERVER

from drinker import user_register, user_drink, get_token,init 


if __name__ == "__main__":
		
	token = get_token()
	
	init()
	request_body = {'dispenserToken' : token}
	while(True):
		mode = int(input())
		if mode == 0:
			userid = user_register()
			#userid=userid.decode('utf-8')
			print("userid: ",userid)
			
			url = SERVER + '/drinker/' + str(userid)
			print(url, request_body)
			res = requests.post(url, data = request_body)
			print(res.text)
		elif mode == 1:		
			userid = user_drink()
			url = SERVER + '/drinker/' + str(userid)
			print(url, request_body)
			res = requests.patch(url, data = request_body)


