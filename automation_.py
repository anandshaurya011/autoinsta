# import time
# import json
# import requests

# def post_video(video_url, caption, access_token, ig_user_id):
    
#     post_url = "https://graph.facebook.com/v20.0/{}/media".format(ig_user_id)
#     payload = {
#         'media_type':'REELS',
#         'video_url' : video_url,
#         'caption' : caption,
#         'access_token': access_token
#     }
#     r = requests.post(post_url, data=payload)
#     print(r.text)
#     print("media has been uploaded")
#     results = json.loads(r.text)
#     return results

# def status_code(ig_container_id, access_token):
#     graph_url = "https://graph.facebook.com/v20.0/"
#     url = graph_url + ig_container_id
#     param = {}
#     param['access_token'] = access_token
#     param['fields'] = 'status_code'
#     response = requests.get(url, params=param)
#     response = response.json()
#     print(response)
#     return response['status_code']

# def publish_video(results, access_token, ig_user_id):
#     if 'id' in results:
#         creation_id = results['id']
#         second_url = "https://graph.facebook.com/v20.0/{}/media_publish".format(ig_user_id)
#         second_payload = {
#             'creation_id': creation_id,
#             'access_token': access_token
#         }
#         r = requests.post(second_url, data=second_payload)
#         print(r.text)
#         print("successfully published")

# access_token = "EAAWpHbZARwdgBO7vaoUDZC8QdZBVGL09llKhqyjQosEfcFjKXxWbl8WfsynRRwdVcqZBE91ZC53PYq7qj7Tq1xpLZAbcDCJuEdcYaxQkHAxshb9Pd0tnk7Bn6DgKwRAoqXELtgw75mByEpF4nDubYWRIhZBvZCGxsWNW3MdqGeaZA4fz5LIZBNuqdOpBb5Qy7zPlQNl3G5ErDm"
# ig_user_id = "17841444514168066"
# # video_url = "https://youtube.com/shorts/c1Bs0dk4fP4?si=0Y0tnluLYrNGEaiY"
# caption = "posted by graph api"

# count = int(input("enter how many times you want to post"))
# for i in range(count):
#     video_url = input("Enter the url of the content")
#     results = post_video(video_url, caption, access_token, ig_user_id)
#     time.sleep(5)
#     ig_container_id = results['id']
#     status = status_code(ig_container_id, access_token)

#     while True:
#         status = status_code(ig_container_id, access_token)
#         time.sleep(1)
#         if status == 'FINISHED':
#             break
#         else:
#             print(status)
#             time.sleep(2)
#             continue

#     if status == 'FINISHED':
#         print("Uploading Video")
#         publish_video(results, access_token, ig_user_id)
#         print("Successfully uploaded")
#     else:
#         print("Failed")





import time
import json
import requests

def post_video(video_url, caption, access_token, ig_user_id):
    post_url = f"https://graph.facebook.com/v20.0/{ig_user_id}/media"
    payload = {
        'media_type': 'REELS',
        'video_url': video_url,
        'caption': caption,
        'access_token': access_token
    }
    r = requests.post(post_url, data=payload)
    response = r.json()
    
    if r.status_code != 200:
        print(f"Error uploading media: {response}")
        return None
    
    print("Media has been uploaded")
    return response

def status_code(ig_container_id, access_token):
    graph_url = "https://graph.facebook.com/v20.0/"
    url = f"{graph_url}{ig_container_id}"
    params = {
        'access_token': access_token,
        'fields': 'status_code'
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    
    if 'error' in response_data:
        print(f"Error fetching status: {response_data}")
        return None
    
    return response_data['status_code']

def publish_video(results, access_token, ig_user_id):
    if 'id' in results:
        creation_id = results['id']
        second_url = f"https://graph.facebook.com/v20.0/{ig_user_id}/media_publish"
        second_payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }
        r = requests.post(second_url, data=second_payload)
        response = r.json()
        
        if r.status_code != 200:
            print(f"Error publishing video: {response}")
            return None
        
        print("Successfully published")
        return response

access_token = "EAAWpHbZARwdgBO7vaoUDZC8QdZBVGL09llKhqyjQosEfcFjKXxWbl8WfsynRRwdVcqZBE91ZC53PYq7qj7Tq1xpLZAbcDCJuEdcYaxQkHAxshb9Pd0tnk7Bn6DgKwRAoqXELtgw75mByEpF4nDubYWRIhZBvZCGxsWNW3MdqGeaZA4fz5LIZBNuqdOpBb5Qy7zPlQNl3G5ErDm"
ig_user_id = "17841444514168066"
caption = "posted by graph api"

if "__name__" == "__main__":

    count = int(input("Enter how many times you want to post: "))
    for i in range(count):
        video_url = input("Enter the URL of the content: ")
        results = post_video(video_url, caption, access_token, ig_user_id)
        
        if not results:
            print("Failed to upload media")
            continue
        
        time.sleep(5)
        ig_container_id = results.get('id')
        if not ig_container_id:
            print("No container ID found")
            continue

        while True:
            status = status_code(ig_container_id, access_token)
            if status is None:
                break
            time.sleep(1)
            if status == 'FINISHED':
                print("Uploading Video")
                publish_video(results, access_token, ig_user_id)
                print("Successfully uploaded")
                break
            else:
                print(f"Current status: {status}")
                time.sleep(2)
