import os, argparse, pdb, glob, shutil

def run(args):
    try:
        if not os.path.exists(args.input_folder):
            print("\n[WARNING] Input Folder specified does not exist!!")
            return
        if not os.path.exists(args.output_folder):
            op = input("\n[WARNING] Output folder does not exist. Do you want to create this folder? [y/N]\n")
            if op == 'y' or op == 'Y' or op == 'yes':
                os.mkdir(args.output_folder)
            else:
                print("Exiting script...")
                return
        os.chdir(args.input_folder)
        print(f"Input Folder: {os.getcwd()}")
        username_dict = {}
        for pic_filename in os.listdir():
            username = pic_filename.split('-')[0]
            if username not in username_dict:
                username_dict[username] = 1
            else:
                username_dict[username] += 1
        for username, pictures_count in username_dict.items():
            if pictures_count > 9:
                print(f"Moving {pictures_count} pictures to {args.output_folder}\{username}") 
                os.mkdir(f"{args.output_folder}\\{username}")
                for filename in glob.glob(f"{username}*"):
                    print(f"\t{filename}")
                    shutil.copy2(f"{args.input_folder}\\{filename}", f"{args.output_folder}\\{username}")
    except TypeError:
        print("Please add input/output folder")
    #print(f"Output Folder: {args.output_folder}")
    finally:
        print("\nExiting Script...")

if __name__ == "__main__":
    param_parser = argparse.ArgumentParser(prog="Twitter Scraper Sorter",
                                     description= "A simple script that sorts tweets, pictures and video from a specified folder into several folders by username",
                                     epilog= "Use at your own risk :)")
    param_parser.add_argument('-i', '--input_folder')
    param_parser.add_argument('-o', '--output_folder')
    args = param_parser.parse_args()
    run(args)