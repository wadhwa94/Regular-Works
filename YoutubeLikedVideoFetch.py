import urllib3
import facebook
import requests
import ast
import json

api_key = "____________________________";
response_playlistID = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=UCuaQuGfEQS1pSVpf_I-Hj5w&key=" + api_key) 
# print (response_playlistID.text)
response_playlistID_jsonData = json.loads(response_playlistID.text)
# print (response_playlistID_jsonData)
# print(len(response_playlistID_jsonData))

# print(response_playlistID_jsonData.keys())
# print (len(response_playlistID_jsonData['items']))
# print (len(response_playlistID_jsonData['items'][0]))

# print (response_playlistID_jsonData['items'][0].keys())

# print (response_playlistID_jsonData['items'][0]['contentDetails'])
# print (response_playlistID_jsonData['items'][0]['contentDetails']['relatedPlaylists']['likes'])

playlistId = response_playlistID_jsonData['items'][0]['contentDetails']['relatedPlaylists']['likes']

responseVideosID = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId="+  playlistId  + "&key=" + api_key) 
responseVideosID_jsonData = json.loads(responseVideosID.text)
print ("Jatin Wadhwa")
# print (len(responseVideosID_jsonData))
# print (responseVideosID_jsonData.keys())
print (int(responseVideosID_jsonData['pageInfo']['totalResults']))
if int(responseVideosID_jsonData['pageInfo']['totalResults']) > 0:
		print (len(responseVideosID_jsonData['items']))
		# for i in range(0,len(responseVideosID_jsonData['items'])):
		for i in range(0,1):
			print (responseVideosID_jsonData['items'][i]['snippet']['resourceId']['videoId'])
			responseVideoContent = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + responseVideosID_jsonData['items'][i]['snippet']['resourceId']['videoId'] + " &key=" + api_key)
			responseVideosContent_jsonData = json.loads(responseVideoContent.text)
			print (responseVideosContent_jsonData['items'][0]['snippet']['categoryId'])

			responseVideoCategoryContent = requests.get("https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id="+ responseVideosContent_jsonData['items'][0]['snippet']['categoryId'] +"&key=" + api_key)
			responseVideoCategoryContent_jsonData = json.loads(responseVideoCategoryContent.text)
			
 
		# print (responseVideosID_jsonData['items'][0].keys())
		# for x in range(0,2):

		print ("Videos Fetched")
		#fetch all the videos from here
		# while()
		# https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken=CKwCEAA&playlistId=LLuaQuGfEQS1pSVpf_I-Hj5w&key={YOUR_API_KEY}
		while 'nextPageToken' in responseVideosID_jsonData:
		   pageToken = responseVideosID_jsonData['nextPageToken'] 
		   responseVideosID = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken="+ pageToken+"&playlistId="+  playlistId  + "&key=" + api_key) 
		   responseVideosID_jsonData = json.loads(responseVideosID.text)
		   # print (responseVideosID_jsonData.keys())
		   print('nextPageToken' in responseVideosID_jsonData)
		   print ("Videos Fetched")
		   #fetch videos


# #r = requests.get("https://graph.facebook.com/me/friends?access_token=" + token)
# # print (ast.literal_eval(r.text))
# list_dict = ast.literal_eval(r.text)
# print (list_dict.keys())
# user_id = list_dict["id"]
# # print (r.text)
# # print (r.status_code)

# events = graph.request('/'+ '100001265210378' + '?fields=id,name,gender,about')
# print (events)


# # r = requests.get("https://graph.facebook.com/" + user_id + "/gender?access_token=" + token)
# # print (r.text)
# # print (r.status_code)


# # print (type(events))
# # print (len(events))
