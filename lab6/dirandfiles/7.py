import os
def copy(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


source_file = r'C:\Users\Asus\Desktop\PP2-2025\lab6\dirandfiles\source.txt'
destination_file = r'C:\Users\Asus\Desktop\PP2-2025\lab6\dirandfiles\destination.txt'

copy(source_file, destination_file)