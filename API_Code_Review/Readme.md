# API_Report
## Author: Jiahao Zhao
##Code Author: Liyi Cao https://github.com/caoliyi/EC500

Data Path:
Data will be stored in the same directory with the API python file.

API Calls:
API calls with one function that generates pics, videos and a text file which contains Google Vision API labels.

## Error Handling: 
1. Users without any pictures uploaded.
Nothing happened, the program terminates itself. There was no video generated, giving an error: [image2 @ 0x7fbb09803400] Could not open file : *.png
2. Non-exist user.
Got error: tweepy.error.TweepError: [{'code': 34, 'message': 'Sorry, that page does not exist.'}]

## Performance:
1. It orks properly, successfully converting all images into a mp4 file.
2. The labels.txt also gives correct anwsers from Google Cloud Vision.

## main call:
  I think the main call is synchronous. Step 1: get pics; Step 2: generates a video; step 3: uses Google API to give labels.

## Test Web:
![alt text](https://github.com/caoliyi/EC500/blob/master/test.png)
