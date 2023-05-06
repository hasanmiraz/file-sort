import os
if __name__=='__main__':
    # path of the target folder
    path = ".\\test"

    # check if the path exists
    if os.path.exists(path):
        count_dirs = 0
        count_files = 0
        list_of_folders = []
        set_of_extensions = set()
        
        # get all the file names in the directory
        files = os.listdir(path)

        # print(files)
        for file in files:
            # for directories
            if os.path.isdir(path+"\\"+file):
                count_dirs+=1
                list_of_folders.append(file)
            
            # for files
            else:
                count_files+=1
                _, file_extension = os.path.splitext(path+"\\"+file)
                # print(f"filename = {_}, extention = {file_extension}")
                set_of_extensions.add(file_extension)

        print(f"dir  = {list_of_folders}")
        print(f"set  = {set_of_extensions}")


    else:
        print("invalid directory")