import re


def getDPI():
    # Specify the path to your file
    file_path = "/home/matija/.Xresources"

    # Define the pattern to match the line
    pattern = r"Xft\.dpi:\s+(\d+)"

    # Open the file and search for the pattern
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                dpi = int(match.group(1))
                break  # Stop searching once a match is found

    return dpi


dpi = getDPI()
