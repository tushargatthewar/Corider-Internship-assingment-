# Corider Internship assingment 
 Tushar gatthewar
# Flask CRUD Application

## Project Overview
This project is a simple Flask application that implements CRUD (Create, Read, Update, Delete) operations for managing user data using MongoDB. Users can register, update their details, view a list of users, and delete user accounts. The application is designed to be easily scalable and maintainable, following best practices in Flask development.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Testing the API](#testing-the-api)
- [Burp Suite Testing Documentation](#burp-suite-testing-documentation)
- [Code Structure](#code-structure)
- [Conclusion](#conclusion)

## Features
- User Registration
- User Profile Update
- User List Display
- User Deletion
- Built-in error handling for form submissions

## Technologies Used
- Flask: A micro web framework for Python.
- MongoDB: NoSQL database for storing user data.
- Docker: Containerization platform to run the application.
- HTML/CSS: For frontend UI.
- Burp Suite: For testing and debugging API endpoints.

## Setup Instructions

cCorider-Internship-assingment-/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       ├── create_user.html
│       └── update_user.html
├── main.py
└── requirements.txt
            


### Prerequisites
- Python 3.x
- MongoDB installed and running
- Docker (optional)

### Cloning the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/username/repo.git
cd repo

###setup
Running the Application

Build the Docker image:
docker build -t Corider-Internship-assingment- .


Run the Docker container:
docker run -p 5000:5000 Corider-Internship-assingment-


Running Locally
python main.py