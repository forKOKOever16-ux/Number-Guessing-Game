# To start, we need to install the two libraries:
# The qrcode library: This library lets us perform all of our QR code related operations.
# The pillow library: This library helps us process and save images.
#  We just need to import qrcode, because pillow is implicitly imported.

import qrcode

website_link = "https://youtu.be/ZYaZ6Odbx_Y?si=EYkoYp6FuI_UXjWx"

#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be.
qr = qrcode.QRCode(version = 1 , box_size = 5 , border = 5)



# the data (specifically, the link we specified before) is added to the QR code, using .add_data().
qr.add_data(website_link)
# The QR code is then generated using .make():
qr.make()


# Finally, we save this created QR code in an img pillow object using qr.make_image():
img = qr.make_image(fill_color = 'black', back_color = 'white')
# Setting the line color fill_color to black.
# Setting the background color back_color to white.

# Finally, we have to store and save the file, using pillow's save() command.
img.save('youtube_qr.png')