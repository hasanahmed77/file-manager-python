import pathlib, os, shutil

print("RUNNING")

source_path = pathlib.Path.home()/'Downloads/'

# New folder directories
images_path = pathlib.Path.home()/'Downloads/Images'
docs_path = pathlib.Path.home()/'Downloads/Docs'
zip_path = pathlib.Path.home()/'Downloads/Zip'
dmg_path = pathlib.Path.home()/'Downloads/Dmg'
app_path = pathlib.Path.home()/'Downloads/Apps'

#extensions
image_extensions = ('jpg', 'jpeg', 'png')
doc_extensions = ('docx', 'pdf', 'pkpass')
zip_extension = 'zip'
dmg_extension = 'dmg'
app_extension = 'app'

def file_mover(destination_path, extensions):
    source_path= pathlib.Path.home()/'Downloads/'
    
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print('Folder created succesfully')
    else:
        print('Folder already exists')

    for file_name in os.listdir(source_path):
        if file_name.lower() == extensions:
            pass
        elif file_name.lower().endswith(extensions):
            print(file_name)
            source_file_path = os.path.join(source_path, file_name)
            destination_file_path = os.path.join(destination_path, file_name)

            shutil.move(source_file_path, destination_file_path)
            print('file moved!', extensions)


file_mover(images_path, image_extensions)
file_mover(docs_path, doc_extensions)
file_mover(zip_path, zip_extension)
file_mover(dmg_path, dmg_extension)
file_mover(app_path, app_extension)

# Terminal command:
# fswatch -0 /Users/mustakimahmedhasan/Downloads | xargs -0 -n 1 -I {} python3 /Users/mustakimahmedhasan/Workspace/Programming/Python/file-management-system/script.py