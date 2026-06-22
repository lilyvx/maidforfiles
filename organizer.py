import os;
import shutil;


SOURCE_DIR = r"C:/Users/User/Downloads"
BASE_DEST_DIR = r"C:/Users/User/Documents"

    #routing table
ROUTING_TABLE = {
    "Cloud Computing" : ["UECS3223", "Cloud Computing", "Elastic Beanstalk"],
}

all_files = os.listdir(SOURCE_DIR) #list directory from our constant directory
print("Here are all the files found inside your Downloads Folder:")
print(all_files)

for stuff in all_files:

    full_item_path = os.path.join(SOURCE_DIR, stuff) #join the path to the file
    
    if os.path.isdir(full_item_path): #see if its a directory
        continue #skip if it's a directory
    for folder_name, keyword_list in ROUTING_TABLE.items():
        
        for keyword in keyword_list:
            if keyword in stuff:
                print(f"*MATCH FOUND*: File '{stuff}' matches keyword '{keyword}'")

                # All of this code is now properly nested inside the IF match gate
                destination_path = os.path.join(BASE_DEST_DIR, folder_name) 

                if os.path.exists(destination_path): 
                    print(f"Destination folder '{folder_name}' already exists. Moving file '{stuff}' to it.")
                else:
                    os.mkdir(destination_path)
                    print(f"Destination Folder '{folder_name}' created. Moving file '{stuff}' to it.")
                    
                try:        
                    shutil.move(full_item_path, destination_path)
                    file_was_moved = True # Mark that this file is finished
                except Exception as error:
                    print(f"*ERROR*: Error moving file '{stuff}': {error}")
                
                break



#Decomposition of the code:
#scan for files in source directory (Downloads)
#check if the file is a directory, if so skip it. check by joining the source directory path with the file name and checking if it is a directory
#find the course name and keyword list from the routing table
#match found, move the file to the appropriate directory by joining base directory (Documents) to the folder name
