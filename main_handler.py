import os
import time
import requests
import automation_ 
import instaloader
import media_handler


# endpoint = "https://dbcd-2405-201-a408-920b-4c53-960b-f284-5a73.ngrok-free.app/"
access_token = "EAAWpHbZARwdgBO7vaoUDZC8QdZBVGL09llKhqyjQosEfcFjKXxWbl8WfsynRRwdVcqZBE91ZC53PYq7qj7Tq1xpLZAbcDCJuEdcYaxQkHAxshb9Pd0tnk7Bn6DgKwRAoqXELtgw75mByEpF4nDubYWRIhZBvZCGxsWNW3MdqGeaZA4fz5LIZBNuqdOpBb5Qy7zPlQNl3G5ErDm"
ig_user_id = "17841444514168066"


def get_time():
    from datetime import datetime

    # Get the current date and time
    current_time = datetime.now()

    hr = formatted_time = current_time.strftime("%H")
    minu = formatted_time = current_time.strftime("%M")
    sec = formatted_time = current_time.strftime("%S")

    # hr = int(hr) + 5
    # minu = int(minu) + 30



    # if hr >= 23:
    #     hr = hr-24
    # if minu >= 60:
    #     minu = minu-60

    print(f"{hr}:{minu}:{sec}")
    return hr, minu, sec



def get_caption(url):

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the text content from the response
            text_content = response.text
            print("Text content from the URL:")
            print(text_content)
            return text_content
        else:
            print(f"Failed to retrieve text content. Status code: {response.status_code}")
        
    except Exception as e:
        print(f"An error occurred: {e}")


def download_recent_videos(profile_username, num_videos):
    # Create an Instaloader instance
    ig = instaloader.Instaloader()

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(ig.context, profile_username)

        # Get the recent posts (videos) of the profile
        recent_posts = profile.get_posts()

        # Download the last 'num_videos' videos
        for index, post in enumerate(recent_posts):
            if index >= num_videos:
                break
            # Download the video post
            ig.download_post(post, target=profile_username)
    except Exception as e:
        print(f"An error occurred: {e}")



profile_list = list()

while True:
    media_handler.intro()
    media_handler.main_option()
    option = int(input())
    if option == 1:
        profile = input('enter profile ID to grab all media')
        profile_list.append(profile)
        try:
            media_handler.all_media_download(profile)
            media_handler.rename_files_by_date(f"{profile}")
            media_handler.del_unwanted_file_in_the_directory(f"{profile}")

        except Exception as e:
            print(e)
            continue

    elif option == 2:
        profile = input('enter profile ID to grab all media')
        profile_list.append(profile)
        no_of_post = int(input("enter the number fo post you want to grab"))
        try:
            download_recent_videos(profile, no_of_post)
            media_handler.del_unwanted_file_in_the_directory(f"{profile}")
            media_handler.rename_files_by_date(f"{profile}")
        except Exception as e:
            print(e)

    elif option == 3:
        endpoint = input("Enter endpoint")
        times = int(input('Enter how many reels you want to post in a day'))
        hr = 18/times
        hr = hr*60
        hr = hr*60
        print("ok in every", hr," sec I'll make a post")
        profiles = input("Enter profile")
        reels_list = os.listdir(profiles)
        print(reels_list)
        video_url = ''
        starts = int(input("start from ? which no. of video"))
        for which_p,i in enumerate(reels_list, start=starts):
            i1 = f"{which_p}.mp4"
            h,m,s = get_time()
            h = int(h)
            print(h)
            # break
            if True:#h >6 and h<1:
                if "mp4" in i1:
                    am = i1.find('.')
                    txt_file = i1[:am]
                    # txt_file = txt_file + ".txt"
                    txt_file = f"{which_p}.txt"
                    print(txt_file)
                    caption_url = f"{endpoint}{profiles}/{txt_file}"
                    print(caption_url)
                    caption = get_caption(caption_url)



                    video_url = f"{endpoint}{profiles}/{i1}"
                    results = automation_.post_video(video_url, caption, access_token, ig_user_id)
                    
                    if not results:
                        print("Failed to upload media")
                        continue
                    
                    time.sleep(5)
                    ig_container_id = results.get('id')
                    if not ig_container_id:
                        print("No container ID found")
                        continue

                    while True:
                        status =automation_.status_code(ig_container_id, access_token)
                        if status is None:
                            break
                        time.sleep(1)
                        if status == 'FINISHED':
                            print("Uploading Video")
                            automation_.publish_video(results, access_token, ig_user_id)
                            print("Successfully uploaded")
                            break
                        else:
                            print(f"Current status: {status}")
                            time.sleep(2)
                    print("next post after", hr)
                    time.sleep(int(hr))
                    # time.sleep(60)
            else:
                print(f"its {h}:{m}:{s}")
                print("Will post next content, from 9AM")
                print("next post in ", hr)
                time.sleep(hr)