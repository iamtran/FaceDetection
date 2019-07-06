 
When App receive an image, it sends this image to facedetection to recognize the face and make a square mark
around the face.

FaceDetectionApp has two parts:
1. sytem setup : automatically start application after boot up using crontab.
	crontab-setup	: setup crontab
	start_FaceDetectionApp	command run by crontab.
2. Core application :	FaceDetection

	Dockerfile-flask	: Docker related files.
	docker-compose.yml : containers for docker compose.
	requirements.txt : Docker related files.
	
	app.py	: Heart of app engine.
	facedetection.py	First commit FaceDetection	8 days ago
	OpenCV/data/haarcascades : computer vision model to recognize faces
	conf.d : configuration file nginx
	static : content images for testing.
	templates : HTML files for application interfac
