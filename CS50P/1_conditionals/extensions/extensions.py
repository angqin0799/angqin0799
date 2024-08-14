
file_name = str(input("File name: "))

# Get the file extension from the file name
file_extension = file_name.split(".")[-1].lower().strip()

# Check the file extension and print the corresponding media type
if file_extension == "gif":
    print("image/gif")
elif file_extension == "png":
    print("image/png")
elif file_extension == "txt":
    print("text/plain")
elif file_extension in ["jpeg", "jpg"]:
    print("image/jpeg")
elif file_extension == "pdf":
    print("application/pdf")
elif file_extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")

