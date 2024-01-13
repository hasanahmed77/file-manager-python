import pathlib, os, shutil


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


print("RUNNING")

source_path = pathlib.Path.home()/'Downloads/'
addresses = [
    { 'path': f"{source_path}/Images", 'extension': ('jpg', 'jpeg', 'png') },
    { 'path': f"{source_path}/Docs", 'extension': ('docx', 'pdf', 'pkpass') },
    { 'path': f"{source_path}/Zip", 'extension': 'zip' },
    { 'path': f"{source_path}/Dmg", 'extension': 'dmg' },
    { 'path': f"{source_path}/Apps", 'extension': 'app' },
]

for address in addresses:
    file_mover(address['path'], address['extension'])