import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)

def my_ls(directory: Path, level: int = 0):
    if not directory.exists():
        print(Fore.RED + "Path not found")
        return

    if not directory.is_dir():
        print(Fore.RED + "Not a directory!")
        return


    for item in directory.iterdir():
        tab = ' ' * (level * 4) 

        if item.is_dir():
           
            print(Fore.BLUE + f"{tab}{item.name}/")
            
            my_ls(item, level + 1)
        else:

            print(Fore.GREEN + f"{tab}{item.name}")

def main():
  
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python my_ls.py /path/to/dir")
        return

    dir_path = Path(sys.argv[1])

    my_ls(dir_path,0)

if __name__ == "__main__":
    main()
