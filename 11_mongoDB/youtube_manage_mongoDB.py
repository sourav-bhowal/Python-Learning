from pymongo import MongoClient
from bson import ObjectId


# connecting to MongoServer
try:
    client = MongoClient("mongodb+srv://souravbhowal15:sourav2003@backend1.kmkr3ik.mongodb.net/")  
# Not a good idea to include id and password in code files
except:
    raise Exception("Cannot connect to MongoServer") 


# creating a DB
db = client["ytmanager"] 
# creating a collection   
video_collection = db["videos"] 


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, Time: {video["time"]}")


def create_video(name, time):
    video_collection.insert_one(
        {"name": name, "time": time}
    )


def update_video(new_name, new_time, videoId):
    video_collection.update_one(
        {
            "_id": ObjectId(videoId),   # we need to import and use ObjectId from bson because we r getting string as _id from input
        }, 
        {
           "$set": {"name": new_name, "time": new_time}
        }
    )


def delete_video(videoId):
    video_collection.delete_one({"_id": ObjectId(videoId)})


def main():
    while True:
        print("\n Youtube Manager App | Mongo DB ")
        print("1. List all videos.")
        print("2. Create a new video.")
        print("3. Update a video.")
        print("4. Delete a video.")
        print("5. Exit.")
        choice = input("Please enter the choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            create_video(name, time)

        elif choice == "3":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            videoId = input("Enter the videoId: ")
            update_video(name, time, videoId)

        elif choice == "4":
            videoId = input("Enter the videoId: ")
            delete_video( videoId)

        elif choice == "5":
            break

        else: 
            print("Please enter the correct choice.")
        

if __name__ == "__main__":
    main()