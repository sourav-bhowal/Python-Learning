import sqlite3

# connecting the DB
conn = sqlite3.connect("youtube_videos.db")
# defining the cursor
cursor = conn.cursor()
# defining schema of the db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS youtube_videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_videos():
    print("*" * 80)
    cursor.execute("SELECT * FROM youtube_videos")
    for row in cursor.fetchall():   # fetch all is used to fetch all videos from the database
        print(row)
    print("*" * 80)

def add_new_video(name, time):
    cursor.execute("INSERT INTO youtube_videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(videoID, new_name, new_time):
    cursor.execute("UPDATE youtube_videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, videoID))
    conn.commit()


def delete_video(videoID):
    cursor.execute("DELETE FROM youtube_videos WHERE id = ?", (videoID, ))
    conn.commit()


def main():
    while True:
        print("\n YouTube Manager with DB | Choose a option from below: ")
        print("1. List all youtube videos. ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                list_all_videos()    
            case 2:
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_new_video(name, time)
            case 3:
                videoId = int(input("Enter the videoId:"))
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_video(videoId, name, time)
            case 4:
                videoId = int(input("Enter the videoId:"))
                delete_video(videoId)
            case 5:
                break
            case _: # default
                print("Invalid option chosen.")
    conn.close()    # closing the connection to the DB


if __name__ == "__main__":
    main()