file = open("youtube.txt", "w")

try: 
    file.write(" Created by me on Youtube")
finally:
    file.close()

################## OR #################################

with open("youtube.txt", "w") as file:  # here errors are handled on their own we dont have to manually write try-catch
    file.write("Created by me on Youtube")  