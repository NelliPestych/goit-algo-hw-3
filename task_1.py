import os
import shutil
import argparse

def copy_files(src, dst):
    try:
        os.makedirs(dst, exist_ok=True)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            if os.path.isdir(s):
                copy_files(s, dst)
            else:
                ext = os.path.splitext(item)[1].lstrip('.').lower()
                target_dir = os.path.join(dst, ext)
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(s, target_dir)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy files and sort by extension.')
    parser.add_argument('source', type=str, help='Source directory')
    parser.add_argument('destination', nargs='?', default='dist', type=str, help='Destination directory')
    args = parser.parse_args()

    copy_files(args.source, args.destination)
