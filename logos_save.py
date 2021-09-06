import requests
import os
import pathlib
import click
import csv
import shutil
from pyfiglet import Figlet

MY_DIR = pathlib.Path().absolute()
FILE_DICT = "files_dictionary.csv"


#base_url = "https://internal-api.mercadopago.com/single-player/entities-api/entities/5985_movistar/image"
base_url = "https://internal-api.mercadopago.com/single-player/entities-api/entities/%s/image"

# load de_para into images_name -> 'image_name': 'entity_name'
def load_images_dict(file_dict):
    images_name = {}
    with open(file_dict, "r") as csvfile:
        dictreader = csv.DictReader(csvfile)
        for row in dictreader:
            images_name[row['image_name']] = row['entity_name']
    return images_name

# save images_name into entities-api
def save_into_entities(image_list):
    for image in image_list:
        # payload={'image': '@'+ image}
        files = {'image': open(image_list[image], 'rb')}
        url = base_url % image
        print(url)
        print(image_list[image])
        response = requests.request("PUT", url, files=files)
        print(response.status_code)

def load_images_path(directory, file_dict):
    if not os.path.isdir(directory):
        print("Not valid dir")
        return

    images_dictonary = load_images_dict(file_dict)
    subfolders= [f.path for f in os.scandir(directory) if f.is_dir()]
    for k in subfolders:
        print(k)
    images_path = {}
    for folder in subfolders:
        path = os.path.basename(folder)
        word = has_word(path, images_dictonary)
        if word != "":
            name = word.split(".")[0]
            images_path[images_dictonary[word]] = folder + '/' + name + "@3x.png"
    return images_path

def format_names(images_dict, alternative):
    formated_dict = {}
    if (alternative):
        os.makedirs("formated_image_name/alternative", exist_ok=True)
    else:
        os.makedirs("formated_image_name/default", exist_ok=True)
    for entity_name, image in images_dict.items():
        if (alternative):
            dst = shutil.copyfile(image, "formated_image_name/alternative/%s_alternative.png" % entity_name)
        else:
            dst = shutil.copyfile(image, "formated_image_name/default/%s.png" % entity_name)
        formated_dict[entity_name] = dst
    return formated_dict

# return the word if has one match and empty if not
def has_word(word, list_word):
    for k in list_word:
        if word.lower() == k.lower():
            return k
    return ""

def run(dir, file_dict, alternative, upload):
    image_list = load_images_path(dir, file_dict)
    for k in image_list:
        print(k)
    formated_dict = format_names(image_list, alternative)
    if (upload):
        save_into_entities(formated_dict)

def create_list_folder(directory):
    list_folder = []
    subfolders= [f.path for f in os.scandir(directory) if f.is_dir()]
    for folder in subfolders:
        list_folder.append(os.path.basename(folder))
    print(list_folder)
    return list_folder

def generate_csv_dictionary(list_folder, fill_entity_name):
    with open(FILE_DICT, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["image_name", "entity_name"])
        writer.writeheader()
        for folder in list_folder:
            if fill_entity_name:
                entity_name = folder.split(".imageset")[0]
                writer.writerow({"image_name": folder, "entity_name": entity_name})
            else:
                writer.writerow({"image_name": folder})

@click.group()
def cli():
    pass

@cli.command()
@click.option("--dir", default=MY_DIR, help="Search directory for squared img, default is current")
@click.option("--dir_alternative", default=MY_DIR, help="Search directory for circle img, default is current")
@click.option("--file_dict", default=FILE_DICT, help="A dictionary of files name to entity name")
@click.option("--upload", help="Upload images to entities-api", default=False)
def create_imgs(dir, file_dict, dir_alternative, upload):
    click.echo("Single Player image uploader CLI")
    # run(dir, file_dict, False, upload)
    run(dir_alternative, file_dict, True, upload)

@cli.command()
@click.option("--dir", default=MY_DIR, help="Search directory, default is current")
@click.option("--fill_entity_name", help="Try to fill entity name automatically", default=False)
def create_dictionary(dir, fill_entity_name):
    list_folder = create_list_folder(dir)
    # list_folder += create_list_folder(dir_alternative)
    generate_csv_dictionary(list_folder, fill_entity_name)


if __name__ == "__main__":
    f = Figlet(font='slant')
    print (f.renderText('Super Single Player Img Uploader Pro Inc Utopia'))
    cli()