"""
Steps

# 1. get a list of .md files (glob)
# 2. within that list, parse each file,
    * grab a url/ element if it exists in the front matter
    * see if there is a folder called filename_files
    * if there is, copy all images in that folder to the location static/figs/first-part-of-url

    * parse the markdown file itself, find each instance of
     <img src="4-python-packages_files
     replace the path to the image to be the location of the folder that you copied above
     static/figs/first-part-of-url

     so below would become

    <img src="4-python-packages_files/figure-markdown_strict/cell-3-output-1.png"

    <img src="figs/first-part-of-url/filename/cell-3-output-1.png"


# LOOP

# get the first file name, remove .md and get the path to that file location
# that path is where the images will live

# Get the URL element url:  if it exists from the front matter
# the final image path should be the first element in the frontmatter url.

# create a method that parses through the markdown file and finds <img src> pattern




# find images in the directory if they exist - the directory with the images should be named
# filename_files
#  Make a copy of the images in a directory called: static/images/url-path/images-here

"""


import os
import re
from glob import glob
import yaml
import shutil
import sys

from typing import List, Dict, Any


def get_md_files(a_dir: str) -> List[str]:
    """
    Get a list of Markdown (.md) files in a directory and its subdirectories, excluding files starting with an underscore.

    Args:
        a_dir (str): The directory to search for Markdown files.

    Returns:
        List[str]: A list of Markdown file paths.
    """
    all_files = glob(os.path.join(a_dir, "**/*.md"), recursive=True)
    filtered = [file for file in all_files if not os.path.basename(file).startswith('_')]

    print(f"Found {len(filtered)} files")
    return filtered


def parse_md_file(file_path: str) -> Dict[str, Any]:
    """
    Parse a Markdown file, extract and parse its front matter.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        Dict[str, Any]: A dictionary containing the front matter.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find front matter and parse it
    front_matter = {}
    if content.startswith("---"):
        front_matter_end = content[3:].find("---") + 3
        front_matter_yaml = content[3:front_matter_end]
        try:
            front_matter = yaml.safe_load(front_matter_yaml)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {file_path}: {e}")

    return front_matter


def copy_images(file_path: str, front_matter: Dict[str, Any]) -> None:
    """
    Copy images from the '_files' folder to a specified location based on the
    'url' in front matter.

    Args:
        file_path (str): The path to the Markdown file.
        front_matter (Dict[str, Any]): The front matter of the Markdown file.
    """
    if "url" in front_matter:
        url_parts = front_matter["url"].split("/")
        if len(url_parts) > 0:
            # Create path to new directory where images live
            filename = os.path.basename(file_path).split('.')[0]
            url_folder = os.path.join("figs", *url_parts[:-1], filename)

            # Create path to where quarto saves figures
            source_folder = os.path.join(
                os.path.dirname(file_path),
                f"{filename}_files",
            )
            # Copy images from the quarto default path to the static dir
            if os.path.exists(source_folder) and os.path.isdir(source_folder):
                os.makedirs(url_folder, exist_ok=True)

                for root, dirs, files in os.walk(source_folder):
                    for file in files:
                        source_file = os.path.join(root, file)
                        destination_file = os.path.join(url_folder, file)
                        shutil.copy2(source_file, destination_file)
                print(f"Copied images from {source_folder} to {url_folder}")
            return url_folder



def update_markdown_images(markdown_file_path, new_image_path):
    try:
        # Read the markdown file
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Regex that matches url with figure-markdown_strict in it
        img_pattern = r'<img([^>]*)src="([^"]+/figure-markdown_strict/[^"]+)"([^>]*)>'

        # Find all matching <img> elements
        img_matches = list(re.finditer(img_pattern, markdown_content))

        # Iterate over matches and update them
        if img_matches:
            print("there are matches in", markdown_file_path, "file")
            for img_match in img_matches:
                # This is the entire figure element
                img_tag = img_match.group(0)
                # This is the existing image path to be updated
                img_src = img_match.group(2)

                # Get image name
                image_name = img_src.split('/')[-1]

                # Create the new image path for website
                new_path = "/" + new_image_path + "/" + image_name

                # Modify the src attribute to include the new image path
                updated_img_tag = img_tag.replace(f'src="{img_src}"',
                                                  f'src="{new_path}"')

                # Replace <img src=" with {{< image src="
                # replace />  with >}}
                # replace alt= with caption=
                # # replace data-fig-alt= with alt=
                # Replace the old <img> tag with the updated one
                # Your dictionary of replacements
                replacements = {
                    "<img src=": "{{< image src=",
                    "/>": ">}}",
                    " alt=": " caption=",
                    "data-fig-alt=": "alt=",
                }
                for old_str, new_str in replacements.items():
                    updated_img_tag = updated_img_tag.replace(old_str, new_str)

                # Update the markdown
                markdown_content = markdown_content.replace(img_tag, updated_img_tag)

            # Write the updated content back to the file
            with open(markdown_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"Updated images in {markdown_file_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    #dir_path = sys.argv[1]
    print("cwd is", os.getcwd())

    lessons_md = os.path.join("content", "english", "lessons")
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <directory>")
    #     sys.exit(1)

    md_files = get_md_files(lessons_md)

    for md_file in md_files:
        front_matter = parse_md_file(md_file)
        path = copy_images(md_file, front_matter)
        update_markdown_images(md_file, path)


if __name__ == "__main__":
    main()
