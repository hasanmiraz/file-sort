import os
import shutil

if __name__=='__main__':

    # path of the target folder
    path = input("enter the input path: ")+"\\"
    dest = input("enter the output path: ")+"\\"

    # check if the path exists
    if os.path.exists(path):
        count_dirs = 0
        count_files = 0
        list_of_folders = []
        dict_of_files = {}
        set_of_extensions = set()
        
        # get all the file names in the directory
        files = os.listdir(path)

        # print(files)
        for file in files:
            # for directories
            if os.path.isdir(path+file):
                count_dirs+=1
                list_of_folders.append(file)
            
            # for files
            else:
                count_files+=1
                _, file_extension = os.path.splitext(path+file)
                file_extension = file_extension.replace(".","")
                
                if file_extension not in set_of_extensions:
                    set_of_extensions.add(file_extension)
                    dict_of_files.update({file_extension:[]})
                
                dict_of_files[file_extension].append(file)
                

        # creating directories
        for extention in set_of_extensions:
            if not os.path.exists(dest+str(extention)):
                os.makedirs(dest+str(extention))

        # moving files
        for key, values in dict_of_files.items():
            for value in values:
                shutil.move(path+value, dest+key+"\\"+value)


        print(f"dir  = {count_dirs}")
        print(f"files  = {count_files}")


    else:
        print("invalid directory")