import json

def loadData():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saveDataHelper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def listAllVideos(videos):
    print("\n")
    print("=" * 70)   
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("=" * 70)

def addVideo(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    saveDataHelper(videos)

def updateVideo(videos):
    listAllVideos(videos)
    index = int(input("Enter the video number that you want to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time': time}
        saveDataHelper(videos)
    else:
        print("Invalid index selected")

def deleteVideo(videos):
    listAllVideos(videos)
    index = int(input("Enter the video number that you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        saveDataHelper(videos)
    else:
        print("Invalid video index selected")

def main():    
    videos = loadData()

    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                listAllVideos(videos)
            case "2":
                addVideo(videos)
            case "3":
                updateVideo(videos)
            case "4":
                deleteVideo(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()