import os



def find_files_path():
    extensions_to_encrpt = ('.css','.html',".js",".json",".php",".txt");

    # grab all files
    selected_files_path = []
    for root, dirs,files in os.walk("./"):
        for file in files:
            if file.endswith(extensions_to_encrpt):
                selected_files_path.append (os.path.join(root, file))


    return selected_files_path;
        
