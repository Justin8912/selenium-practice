Selenium Practice
--
The purpose of this repo is to test out selenium for use in automating a small but tedious part of Robin's job. 

There is a section in her job which requires her to manually change the seat count in all sections during registration 
which includes clicking on a set of buttons hundreds of times. This seems like it can be automated. However, due to 
the important nature of this work, there are a couple of guidelines that need to be followed:

1. The modifications need made by the script need to be clear and ideally should be stored in an external file 
2. There should be a way to exclude sections based on time and the unique number of the section 
3. We should be able to see the changes that are being made by the script 

Running tests
--
There is a test `my-app` react app that is being used to render what the basic display looks like on Robin's side. 

In order to test the selenium app, you must follow these steps:
1. Open one terminal to run the react app and wait until it is fully loaded
2. Open another terminal to run the selenium script

After running the test a directory should populate called `changes-made` with the time that the file was run 
as the name of the file. This will hold all the record for everything that was changed.