import pathlib
import os

# NEW: Add validation so that the fallback is more graceful and interpretable
def rel2abspath(relative_path):
    if not relative_path:
        raise ValueError("relative_path is None. Did you forget to set USER_DB_PATH?")
    return str((pathlib.Path().resolve() / relative_path).resolve())

def create_folders(path: str):
    if not path.endswith('\\'):
        folder_path = os.path.dirname(path)
    else:
        folder_path = path
    os.makedirs(folder_path, exist_ok=True)
