# EMOTION RECOGNITION JUKE BOX

A Respository created for emotion recognition and play music based on emotion recognized.

# Major Features!

  - Emotion Recognition
  - Music Player

# Sub Features!

 - Opening the camera.
 - Choosing the image
 - Creating Playlist
 - View the playlist
 - Login Provision
 - Forgot Password Provision

### Tech

EMOTION RECOGNITION JUKE BOX uses a number of languages and plugins to work properly:

* Django
* Material Design Bootstrap
* Javascript Face API
* Tensorflow
* Opencv
* sqlite3

### Installation

Clone the repository
Install the required dependencies start the server.
specify the local path for static assets like songs and images as per your need and based on operating system wheverer required.

Create a Superuser
```sh
$python manage.py createsuperuser
```
this will ask you few details fill those and create a super user.

Migrate the tables so as to create a sqlite database
```sh
$python manage.py makemigrations
```
```sh
$python manage.py migrate
```

Start the django server by executing below command.
```sh
$python manage.py runserver or $ python3 manage.py runserver
```

Navigate to 
```sh
127.0.0.1:8000/admin
```
and create a user account so as to login to the project.

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

### For detecting emotion continuously and live replace the below piece of code in scripts.js inside static/js folder.

```js
setTimeout(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions().withAgeAndGender()
    const resizedDetections = await faceapi.resizeResults(detections, displaySize)
    let detectedResult = detections[0].expressions
    console.log(detectedResult)
    maximunProb = Object.keys(detectedResult).reduce((a, b) => detectedResult[a] > detectedResult[b] ? a : b);
    $('.capturing__image_block').hide()
    const audio = new Audio('/media/alone/Seagate Backup Plus Drive/Aishwarya/static/assets/js/songs/' + maximunProb + '/' + maximunProb + '.mp3')
    audio.play()
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
}, 5000)
```
By

```js
setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = await faceapi.resizeResults(detections, displaySize)
    let detectedResult = detections[0].expressions
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    }, 100)
```


### Screenshots

![Screenshot from 2020-09-22 20-58-50](https://user-images.githubusercontent.com/38497682/93903824-c8e85a80-fd16-11ea-903f-c89be5cf13bc.png)
![Screenshot from 2020-09-22 20-59-04](https://user-images.githubusercontent.com/38497682/93903877-d1d92c00-fd16-11ea-8188-1754df46d938.png)
![Screenshot from 2020-09-22 20-59-08](https://user-images.githubusercontent.com/38497682/93903887-d43b8600-fd16-11ea-9658-1f86590c4c7c.png)
![Screenshot from 2020-09-22 20-59-17](https://user-images.githubusercontent.com/38497682/93903903-d7367680-fd16-11ea-92f2-afbf7b2b0137.png)
![Screenshot from 2020-09-22 20-59-26](https://user-images.githubusercontent.com/38497682/93903918-dbfb2a80-fd16-11ea-926d-1582640baf54.png)
![Screenshot from 2020-09-22 21-00-11](https://user-images.githubusercontent.com/38497682/93903925-df8eb180-fd16-11ea-88ca-7aee179eb417.png)
![Screenshot from 2020-09-22 21-01-05](https://user-images.githubusercontent.com/38497682/93903942-e289a200-fd16-11ea-8100-9cd78e31a85b.png)
