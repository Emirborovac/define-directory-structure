import os

def print_dir_structure(start_path, indent=""):
    """
    Recursively prints the directory structure starting from `start_path`.

    :param start_path: Root directory to start printing from.
    :param indent: Current indentation level for the structure.
    """
    items = sorted(os.listdir(start_path))
    for i, item in enumerate(items):
        item_path = os.path.join(start_path, item)
        is_last = (i == len(items) - 1)
        if os.path.isdir(item_path):
            connector = "└── " if is_last else "├── "
            print(f"{indent}{connector}{item}/")
            print_dir_structure(item_path, indent + ("    " if is_last else "│   "))
        else:
            connector = "└── " if is_last else "├── "
            print(f"{indent}{connector}{item}")

# Example usage
root_directory = r""  # Use a raw string
print_dir_structure(root_directory)
