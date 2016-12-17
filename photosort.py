import os
import time
import PIL.Image
import PIL.ExifTags

root = "C:\Users\haynt\Desktop\Ema"
PICTYPE = (".jpg")
MOVTYPE = (".mov")

# TODO: is this the most efficient way?

def get_exif(filename):
    ret = {}
    i = PIL.Image.open(filename)
    info = i._getexif()
    for tag, value in info.items():
        decoded = PIL.ExifTags.TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

# TODO: Create test cases for get_min_date
# Find initial date of photo, return date in YYYY-MM format
def get_min_date(exif_data):
    # TODO: put photo/movie check here
    y, m = "", ""
    dates = [v for k, v in exif_data.items() if type(k) is str and "Date" in k]
    if not dates:
        # TODO: fix no dates, use time.strftime
        pass
    for date in dates:
        exif_date, exif_time = date.split(" ")
        temp_y, temp_m, _ = exif_date.split(":")
        if y == "" or m == "":
            y, m = temp_y, temp_m
        elif int(y) <= int(temp_y):
            if int(m) < int(temp_m):
                y, m = temp_y, temp_m
    print "\tDates: {0}".format(dates)
    print "\t{0}".format("-".join((y, m)))
    return "-".join((y, m))

# Check if file or folder parameter exists, return bool
def exists(path):
    return os.path.exists(path)


if __name__ == "__main__":
    # Print every file and folder in the root directory
    for folderName, subfolders, filenames in os.walk(root):
        print "The current folder is: {0}".format(folderName)

        for subfolder in subfolders:
            print "SUBFOLDER OF {0}: {1}".format(folderName, subfolder)

        for filename in filenames:
            print "FILE INSIDE {0}: {1}".format(folderName, filename)

            if filename.lower().endswith(PICTYPE):
                exif_data = get_exif(os.path.join(folderName, filename))
                date = get_min_date(exif_data)
                # TODO: if date is not a folder, create folder
                print "\tPath: {0}".format(exists(os.path.join(root, date)))
                # TODO: if photo name exists in folder, rename photo with next sequential number
                # TODO: move photo to folder

            elif filename.lower().endswith(MOVTYPE):  # TODO: handle pictures AND movies simultaneously
                print "\t{0}".format(os.path.join(folderName,filename))
                secs = os.path.getmtime((os.path.join(folderName, filename)))  # TODO: get_exif may be where to test for pic or movie
                print "\t\tDate: {0}".format(time.ctime(secs))
                print "\t\tFormatted: {0}".format(time.strftime("%Y-%m", time.gmtime(secs)))
                date = time.strftime("%Y-%m", time.gmtime(secs))
                # TODO: if date is not a folder, create folder
                print "\t\tPath: {0}".format(exists(os.path.join(root, date)))
                # TODO: if movie name exists in folder, rename photo with next sequential number
                # TODO: move movie to folder

            else:
                print "\tDid not process: {0}".format(filename)