import os
import shutil
import imageio
import time


# Folder creation ------------------------------------------------------------------------------------------------
def create_folder(path):
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
        print("The new directory is created!")
        time.sleep(2)

    # Wait until it's created
    while True:
        if os.path.isdir(path):
            break
        time.sleep(1)


def create_label_folders(directory_save_eyes, labels):
    for label in labels:
        create_folder(directory_save_eyes + '/' + label)


# Extensions ------------------------------------------------------------------------------------------------
def check_extension_file(name, extensions):
    for ext in extensions:
        if ext in name:
            return True
    return False


def filter_extensions(lst, extensions):
    return [name for name in lst if check_extension_file(name, extensions)]


def filter_images(lst):
    images_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.CR2')
    return filter_extensions(lst, images_extensions)


def filter_faces(data, flt='closed_eyes'):
    return list(data[data[flt] > 0].file_name)


# Move files ------------------------------------------------------------------------------------------------
def move_files(files_list, path_directory, path_to_save):
    create_folder(path_to_save)
    for file_name in files_list:
        try:
            shutil.move(path_directory + '/' + file_name, path_to_save + '/' + file_name)
        except:
            print("Picture ", file_name, " not found.")


def move_file(file_name, path_directory, path_to_save):
    create_folder(path_to_save)
    try:
        shutil.move(path_directory + '/' + file_name, path_to_save + '/' + file_name)
    except:
        print("Picture ", file_name, " not found.")


def move_folder(path_directory, path_to_save):
    create_folder(path_to_save)
    try:
        shutil.move(path_directory, path_to_save)
    except:
        print("Error path not found:", path_directory)


# Copy files --------------------------------------------------------------------------------------
def copy_files(files_list, path_directory, path_to_save):
    create_folder(path_to_save)
    print(path_directory)
    for file_name in files_list:
        try:
            shutil.copy(path_directory + '/' + file_name, path_to_save + '/' + path_directory.split('/')[-2][-3:]+'_'+file_name)
        except:

            print("Picture ", path_directory+'/'+file_name, " not found.")


def copy_file(file_name, path_directory, path_to_save):
    create_folder(path_to_save)
    try:
        shutil.copy(path_directory + '/' + file_name, path_to_save + '/' + file_name)
    except:
        print("Picture ", file_name, " not found.")


# Save files ------------------------------------------------------------------------------------------------
def save_image(image, image_name, path_directory):
    create_folder(path_directory)
    imageio.imwrite(path_directory + '/' + image_name + '.jpg', image)


# Train-Test split ------------------------------------------------------------------------------------------------
def train_test_split(path='output/eyes', labels=('open', 'closed'), train_test_ratio=0.2):
    for label in labels:
        files_list = os.listdir(path + '/' + label)
        test_len = round(len(files_list) * train_test_ratio)
        move_files(files_list[:test_len], path + '/' + label, path + "/new_dataset/test/" + label)
        move_files(files_list[test_len:], path + '/' + label, path + "/new_dataset/train/" + label)


# Time measuring ----------------------------------------------------------------------------------------------
def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time
