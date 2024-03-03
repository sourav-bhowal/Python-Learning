import json

youtube_file = "youtube.txt"

def load_data():
    try:
        with open(youtube_file, "r") as file:
            return json.load(file) # using json to load the data from the above file and converting it to json
    except FileNotFoundError:
        return [] # return an empty list
    

def save_data_helper(videos):
    with open(youtube_file, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video["name"]} | Duration: {video["time"]}")
    print("*" * 50)


def add_new_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index: "))

    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")


def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose a option from below: ")
        print("1. List all youtube videos. ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                list_all_videos(videos)    
            case 2:
                add_new_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _: # default
                print("Invalid option chosen.")


if __name__ == "__main__":  # if "name" i.e. "__name__" of the fn is "main" i.e "__main__" then only run the main() fn.
    main() 

