import os

# Create folders for each file type

os.makedirs("Images", exist_ok=True)
os.makedirs("Text_Files", exist_ok=True)
os.makedirs("Audio_Files", exist_ok=True)
os.makedirs("Video_Files", exist_ok=True)
os.makedirs("PDF_Files", exist_ok=True)
os.makedirs("Compressed_Files", exist_ok=True)
os.makedirs("Executable_Files", exist_ok=True)
os.makedirs("Unknown_Files", exist_ok=True)

files = os.listdir()

for file in files:

    if os.path.isfile(file):

        file_name, file_extension = os.path.splitext(file)

        if file_extension == ".jpg" or file_extension == ".png":
            print(file, "is an image file.")

        elif file_extension == ".txt" or file_extension == ".docx":
            print(file, "is a text file.")

        elif file_extension == ".mp3" or file_extension == ".wav":
            print(file, "is an audio file.")

        elif file_extension == ".mp4" or file_extension == ".mkv":
            print(file, "is a video file.")

        elif file_extension == ".pdf":
            print(file, "is a pdf file.")

        elif file_extension == ".zip" or file_extension == ".rar":
            print(file, "is a compressed file.")

        elif file_extension == ".exe":
            print(file, "is an executable file.")

        else:
            print(file, "is of unknown file type.")