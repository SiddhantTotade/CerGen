<div align="center" >
  <img src="https://github.com/SiddhantTotade/certificate-generator-and-sender/blob/main/app_images/CerGen.png" />
</div>

# About the project
CerGen is a web application which generates the certificates for the participants and send it to their corrosponding email. This application has the ability of generating the certificates of the participants who are participated in the event/contest. Also this application sends text message to the participants on their corrosponding phone number. This applicaion sends the certificate of participantion and certification of merit at the same time.

### Features of the project
+ Filter eligible participants.
+ Choose templates for the certificate of participation/merit.
+ Upload image of the participant receiving certificate.
+ Upload images of the event album.
+ Sends certificate to the individual participant.
+ Downloads all generated certificates.

### Technologies used
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) &nbsp; ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) &nbsp; ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) &nbsp; ![Material UI](https://img.shields.io/badge/Material%20UI-007FFF?style=for-the-badge&logo=mui&logoColor=white) &nbsp; ![Tailwind Css](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

# Getting Started

## Setting up virtual environment
+ Clone the project
```shell
git clone git@github.com:SiddhantTotade/cergen.git
```
+ Open the project in the terminal. The below command opens the project in VS-Code but you can choose any editor
```shell
code .
```
+ In the terminal create a virtual environment. Prefer root directory for `venv`
  + The below command create a virtual environment in a specific directory
```shell
python -m venv <name_of_venv>
```
OR
  + The below command create a virtual envvironment in the current directory
```shell
python -m venv .
```
+ After creating `venv`, Activate it. Go to the directory in which the `venv` exists and type command
```shell
source bin/activate
```
+ Deactivate the virtual environment.
```shell
deactivate
```
Before installing the `requirements.txt` check if there is something exists or not. If the command shows nothing then nothing is installed yet 
```shell
pip freeze
```
+ After activating `venv`, install the `requirements.txt`.
```shell
pip install -r requirements.txt
```

## First - Running Django Server
+ Clone the project in your PC or Laptop.
```shell
git clone git@github.com:SiddhantTotade/cergen.git
```
+ Open the project in a terminal and type the following command
```shell
source bin/activate
```
+ Change directory to 'app'
```shell
cd app
```
+ Run the django serever
```shell
python manage.py runserver
```

## Second - Running React Server
+ Now, open another terminal and change directory to cert_gen_sen_app_frontend
```shell
cd cert_gen_sen_app_frontend
```
+ Inside react directory, run command to install node modules
```shell
npm install
```
+ After installing node modules, start the react server
```shell
npm start
```
+ Also you need to configure tailwind css for this project. Follow this guide to configure
```shell
https://tailwindcss.com/docs/guides/create-react-app
```

#### Leave a star if you like the project. :star:
### Enjoy :relaxed: :relaxed:

## Project Images
<div align="center" gap="10px" display="flex">

<img src="https://github.com/SiddhantTotade/certificate-generator-and-sender/blob/main/app_images/app_image_1.png" width="400px" />
<img src="https://github.com/SiddhantTotade/certificate-generator-and-sender/blob/main/app_images/app_image_2.png" width="400px" />
<img src="https://github.com/SiddhantTotade/certificate-generator-and-sender/blob/main/app_images/certificate_before.png" width="400px" />
<img src="https://github.com/SiddhantTotade/certificate-generator-and-sender/blob/main/app_images/certificate_after.png" width="400px" />

<div/>
