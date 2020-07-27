# Invisible-mat
Using this we can become invisible by segmenting the background image with the sequence of images that is being captured by the webcam and overlapping it in the required positions.

In this we mainly used the libraries:-
  1)Numpy
  2)Opencv
  
Initially we capture the background image and save it.
Later we use the image color segmentation to differentiate the required color using which we wan to become invisible and mask the portion of that color in the image.Then we overlap the background image in the areas of the mask so as to create an illusion of invisibility.
