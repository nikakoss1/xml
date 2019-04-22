import os

#/Users/nikakoss/MEGA/projects/clients/slideshop/src/tb/pptx/utils/list_dir.py


def main():
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))



if __name__ == '__main__':
    main()