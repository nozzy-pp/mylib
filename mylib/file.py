import os, platform, shutil

def remove(path: str, empty_only: bool=False) -> bool:
    """
    Remove a file or directory at the given path.

    Args:
        path (str): Path to the file or directory to remove.
        empty_only (bool, optional): If True, only remove empty directories. 
        If False, remove non-empty directories as well. Defaults to False.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        OSError: If empty_only is True and the directory is not empty.
        Exception: For other unexpected errors.

    Returns:
        bool: True if the file or directory was successfully removed.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist.")
    
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
    # If the directory is not empty, use shutil.rmtree
    except OSError as e:
        if not empty_only:
            shutil.rmtree(path)
        else:
            raise e
        
    except Exception as e:
        raise e
    
    return True
