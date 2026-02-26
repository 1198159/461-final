The repository should be setup in a way that should run *I think*

make sure to run "conda activate nepmap" to get into the correct environment

Note that not all the examples work but some do.

Our custom input is the video **resource\test.mp4** It is a random video of Alex running down stairs and has no particular significance.

our custom output is in a file **logs\castle\render_only\ro_project_vid_rgb.gif**

*I also felt nice and put both files in the **sample** directory for easier access :)*

**Here are all the steps required that it took to get this working**

The first problems we had were the packages (nerfacc...). THis was solved by importing them. Also we had to make a local copy of nerfacc to recompile it.

We had a CUDA mismatch. We had to rebuild the project around this new version. Upon rebuilding the project, we had issues with the code itself. All changes are documented in the files with a
 #NEW CODE ADDED FOR 461
comment.

One of the issues caused by the new code is that it only worked for square videos. As a result, we made the script *resize_square.py*. If you wanted to run your own stuff, you would need to edit this file and run it

This was what enabled us to actually validate the projection mapping.

We did not get around to getting the text projection to work. It is cool, and if we had time, we would have done it. 

The Liscense should be already included as per the original repository

And finally, in the name of disclosure, Claude Sonnet 4.5 and ChatGPT 4.0 were used tremendously for debugging and writing code necessary to get this project working. 
