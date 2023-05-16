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
                set_of_extensions.add(file_extension.replace(".",""))

        # creating directories
        for extention in set_of_extensions:
            if not os.path.exists(path+"\\result\\"+str(extention)):
                os.makedirs(path+"\\result\\"+str(extention))



        print(f"dir  = {count_dirs}")
        print(f"set  = {count_files}")


    else:
        print("invalid directory")