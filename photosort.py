import os
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
    y, m = "", ""
    dates = [v for k, v in exif_data.items() if type(k) is str and "Date" in k]
    for date in dates:
        exif_date, exif_time = date.split(" ")
        temp_y, temp_m, _ = exif_date.split(":")
        if y == "" or m == "":
            y, m = temp_y, temp_m
        elif int(y) <= int(temp_y):
            if int(m) < int(temp_m):
                y, m = temp_y, temp_m
    print dates
    print "-".join((y, m))
    return "-".join((y, m))

# Check if file or folder parameter exists, return bool
def exists(path):
    return os.path.exists(path)


if __name__ == "__main__":
    # Print every file and folder in the root directory
    for dirpath, dirnames, filenames in os.walk(root):
        #print "Dirpath: {0}".format(dirpath)
        for dirname in dirnames:
            print "{0}".format(dirname)
            i = 0
            for filename in filenames:
                if i > 10:
                    break
                if filename.lower().endswith(PICTYPE):
                    print "\t{0}".format(filename)
                    #img = PIL.Image.open(os.path.join(dirpath, filename))
                    exif_data = get_exif(os.path.join(dirpath, filename))
                    date = get_min_date(exif_data)
                    # TODO: if date is not a folder, create folder
                    print exists(os.path.join(root, date))
                    # TODO: if photo/movie name exists in folder, rename photo with next sequential number
                    # TODO: move photo/movie to folder
                i += 1
        break