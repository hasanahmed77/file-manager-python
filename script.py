import pathlib, os, shutil

source_path = pathlib.Path.home()/'Downloads/'

# New folder directories
images_path = pathlib.Path.home()/'Downloads/Images'
docs_path = pathlib.Path.home()/'Downloads/Docs'
zip_path = pathlib.Path.home()/'Downloads/Zip'
dmg_path = pathlib.Path.home()/'Downloads/Dmg'

#extensions
image_extensions = ('jpg', 'jpeg', 'png')
doc_extensions = ('docx', 'pdf')
zip_extension = 'zip'
dmg_extension = 'dmg'

def file_mover(destination_path, extensions):
    source_path= pathlib.Path.home()/'Downloads/'
    
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print('Folder created succesfully')
    else:
        print('Folder already exists')

    for file_name in os.listdir(source_path):
        if file_name.lower() == extensions:
            break
        elif file_name.lower().endswith(extensions):
            source_file_path = os.path.join(source_path, file_name)
            destination_file_path = os.path.join(destination_path, file_name)

            shutil.move(source_file_path, destination_file_path)
            print('file moved!')

file_mover(images_path, image_extensions)
file_mover(docs_path, doc_extensions)
# file_mover(zip_path, zip_extension)
file_mover(dmg_path, dmg_extension)