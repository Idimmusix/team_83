from PIL import Image
from PIL.ExifTags import TAGS

#get image or video
# imagename = "FB_IMG_1645054248977.jpg"
imagename = "The_Mighty_Surpriser complete-2.png"
# imagename = "image.png"

#read the image data using PIL
image = Image.open(imagename)

# def generate_exif_dict(filepath):
#     """
#     Generate a dictionary of dictionaries.
#     The outer dictionary keys are the names
#     of individual items, eg Make, Model etc.
#     The outer dictionary values are themselves
#     dictionaries with the following keys:
#         tag: the numeric code for the item names
#         raw: the data as stored in the image, often
#         in a non-human-readable format
#         processed: the raw data if it is human-readable,
#         or a processed version if not.
#     """
#     try:
#         image = Image.open(filepath) #read image
#         exif_data_PIL = image._getexif()
        
        
#extract image basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1),
}

for label,value in info_dict.items():
    print(f"{label}: {value}")
    
# extract EXIF data
exifdata = image.getexif().items()
print(f"{exifdata}")

exif = {}
# iterating over all EXIF data fields
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes 
#     if isinstance(data, bytes):
#         data = data.decode()
#     print(f"{tag:25}: {data}")

# #extarcting all the metadata as key and value pairs and converting them from numerical value to string values
#     if tag in TAGS:
#         exif[TAGS[tag]] = value

# #checking if image is copyrighted      
# try:
#     if 'Copyright' in exif:
#         print("Image is Copyrighted, by ", exif['Copyright'])
# except KeyError:
#     pass