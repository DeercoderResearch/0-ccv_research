#!/usr/bin/env python
import Image
# the following are the areas from FULL.jpg detected by detect
crop1 = (678, 85, 678+53, 85+53)
crop2 = (264,122,264+241, 122+241)

# Now we plot these are to verify it
src = Image.open("FULL.jpg")
crop1 = src.crop(crop1)
crop2 = src.crop(crop2)

# save them as .jpg images
crop1.save("crop1.jpg")
crop2.save("crop2.jpg")
