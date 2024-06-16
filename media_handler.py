# # import instaloader
# #
# #
# # ig = instaloader.Instaloader()
# # ig.login("anandshaurya011@gmail.com", "78708161Sha")
# #
# # from instaloader import Instaloader, Profile
# #
# # PROFILE = "hustledusan"       # profile to download from
# # X_percentage = 10    # percentage of posts that should be downloaded
# #
# # L = Instaloader()
# #
# # profile = Profile.from_username(L.context, PROFILE)
# # posts_sorted_by_likes = sorted(profile.get_posts(),
# #                                key=lambda p: p.likes + p.comments,
# #                                reverse=True)

# from instabot import Bot
import instaloader
import os
# import os
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])

USERNAME = 'anandshaurya011@gmail.com'
PASSWORD = '78708161Sha'
global login_id, im
# bot = Bot()
# SESSION_FILENAME = 'SESSION'
# L.load_session_from_file(username=USERNAME, filename=SESSION_FILENAME)
PROFILE = "boys_things._"
DIR = "{target}"
Name = "{date:%Y-%m-%d %H-%M-%S} {mediaid}_{owner_id}"
ig = instaloader.Instaloader(dirname_pattern=DIR, filename_pattern=Name)


def intro():
    print("-----------------------------------------------------------------")
    print("||||                  Welcome To InstaBot                    ||||")
    print("-----------------------------------------------------------------")
    print("                                      Created By:- Anand Shaurya.")


def main_option():
    print("Choose an option-")
    print("1. Download/Add posts via instagram profile.")
    print("2. Start posting on IG/ seslf content")
    print("3. Automate a page to auto post contents")
    print("4. Contact for a new feature you want ")
    print("5. About the Author/ Work with the Author")
    print("6. Exit")


def automation_option():
    print("1. Add Profiles to copy content:")
    print("2. Set the No. of post you want in a day on your page")
    print("3. List of profile")
    print("4. Delete profiles")
    print("5. Reset")
    print("6. Main menu")


def rename_files_by_date(directory):
    """
    Renames video files and their corresponding text files in the given directory based on their date part in the filename.

    Args:
    - directory (str): The directory containing the files to be renamed.
    """
    try:
        # Get list of file names in the directory
        file_names = os.listdir(directory)

        # Sort file names by date part
        sorted_file_names = sorted(file_names, key=lambda x: x.split("_")[0])

        # Initialize counter
        counter = 1

        # Iterate through sorted file names
        for file_name in sorted_file_names:
            # Check if the file is a video file
            if file_name.lower().endswith('.mp4'):
                # Construct new file names
                new_video_name = f"{counter}.mp4"
                new_txt_name = f"{counter}.txt"

                # Rename video file
                old_video_path = os.path.join(directory, file_name)
                new_video_path = os.path.join(directory, new_video_name)
                os.rename(old_video_path, new_video_path)
                print(f"Renamed '{old_video_path}' to '{new_video_path}'")

                # Rename corresponding text file
                old_txt_name = f"{os.path.splitext(file_name)[0]}.txt"
                old_txt_path = os.path.join(directory, old_txt_name)
                new_txt_path = os.path.join(directory, new_txt_name)
                if os.path.exists(old_txt_path):
                    os.rename(old_txt_path, new_txt_path)
                    print(f"Renamed '{old_txt_path}' to '{new_txt_path}'")

                # Increment counter
                counter += 1

        return "done"
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage:


def add_profile_in_database_for_download_media():
    ss = input("enter profile")
    profiles = []
    profiles.append(ss)

    try:
        f = open(f"{login_id}.txt", "x")
        f.close()
    except Exception as e:
        print(e)
        print("please login first")
        login()
    with open(f'{login_id}.txt', "a") as file:
        file.write(profiles)

    print("Content appended successfully!")




def login():

    print("Dont worry we can't see your logins/ We are trusted")
    login_id = input("Please enter your insta username/email")
    password = input("Please enter your insta password")
    try:
        ig.login(login_id, password)
        print('Successfully log_in.')
        profile = instaloader.Profile.from_username(ig.context, 'login_id')
        profile_name = profile.full_name
        print("Welcome", profile_name)
    except Exception as e:
        print(e, "\n please enter a valid Email/password")
        login()


def all_media_download(PROFILE):
    """
    :type PROFILE: str
    """
    # PROFILE = input("Enter the profile username")
    # login()
    print("Downloading Posts")



    try:
        profile = instaloader.Profile.from_username(ig.context, PROFILE)
        for post in profile.get_posts():
            ig.download_post(post, target=profile.username)
            filename = profile.username + '/' + ig.format_filename(post, target=profile.username, )
        # print("pppp", filename)
    except Exception as e:
        login()
        profile = instaloader.Profile.from_username(ig.context, PROFILE)
        for post in profile.get_posts():
            ig.download_post(post, target=profile.username)
            filename = profile.username + '/' + ig.format_filename(post, target=profile.username, )
            # print("pppp", filename)



def del_unwanted_file_in_the_directory(dir_name):
    dir_list = os.listdir(dir_name)
    for file_name in dir_list:
        if file_name.endswith('.jpg') or file_name.endswith('.xz'):
            file_path = os.path.join(dir_name, file_name)
            os.remove(file_path)
            print(f"Removed '{file_path}'")
        else:
            print(f"Ignored '{os.path.join(dir_name, file_name)}'")


def post(video_path, caption):
    # bot.login(username=login_id, password=PASSWORD)
    bot.upload_video(video_path, caption=caption)


def upload():
    nt = int(input("Enter number of post in a day"))
    interval = 24/nt


def upload_videos(directory):
    """
    Uploads video files and their corresponding caption text files from the given directory to Instagram using Instabot.

    Args:
    - directory (str): The directory containing the video files and corresponding caption text files.
    """
    bot.login(username='anandshaurya011@gmail.com', password='78708161Sha', use_cookie=True)  # Replace with your Instagram username and password

    try:
        # Get list of file names in the directory
        file_names = os.listdir(directory)

        for file_name in file_names:
            if file_name.lower().endswith('.jpg'):
                video_path = os.path.join(directory, file_name)
                caption_path = os.path.join(directory, f"{os.path.splitext(file_name)[0]}.txt")

                # Read caption from text file
                if os.path.exists(caption_path):
                    with open(caption_path, 'r') as f:
                        caption = f.read().strip()
                else:
                    caption = ""

                # Upload video with caption
                bot.upload_video(video_path, caption=caption)
                print(f"Uploaded '{file_name}' with caption: {caption}")

    except Exception as e:
        print(f"An error occurred during upload: {e}")

#
# while True:
#     intro()
#     main_option()
#     option = input("Enter number as option:- ")
#     if option == "1":
#         im = input("Enter the profile username")
#         all_media_download(im)
#         del_unwanted_file_in_the_directory(im)
#         rename_files_by_date(im)
#     elif option == "2":
#         upload_videos('aishwaryasingh_21')
#     elif option == "3":
#         while True:
#             intro()
#             automation_option()
#             option = input("select option")
#             if option == '1':
#                 add_profile_in_database_for_download_media()
#             if option == '2':
#                 iteration = input("Enter the number of post in a day:- ")
#             if option == '3':
#                 pass
#             if option == '4':
#                 pass
#             if option == '5':
#                 pass
#             if option == '6':
#                 # intro()
#                 break
#
#     elif option == "4":
#         im = input("Enter the DIR")
#         while True:
#             try:
#                 del_unwanted_file_in_the_directory(im)
#                 l = rename_files_by_date(im)
#                 if l== "done":
#                     break
#             except Exception as e:
#                 print(e)
#     elif option == "5":
#         pass
#     elif option == "6":
#         break
#     else:
#         print("Enter a valid option")
#
