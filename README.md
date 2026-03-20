# Capstone Political Profile: Core Values of VSX

## Description:
This is a political profile with core values for Victor Sifiso Xaba, a political candidate. The core values are 10 selections of a political candidate's values.

## Table of Contents:
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)
- [GitHub Repository](#github-repository)

## Installation:

### Run locally
To view the core values or the political profile of VSX locally, follow the steps below:
1. Clone the repository:`git clone https://github.com/Victor-Sifiso-Xaba/capstone-politicalprofile.git`
2. Working directory: cd capstone-politicalprofile
3. Create a virtual environment: `python -m venv venv`
4. Activate virtual environment (Windows): `venv\Scripts\activate` 
4. Activate virtual environment (Linux/Max): `source venv/bin/activate`
5. Install all dependencies: `pip install -r requirements.txt`
6. Apply the migrations: `python capstone/manage.py migrate`
7. Run the server: `python capstone/manage.py runserver`
8. Visit the link: http://127.0.0.1:8000/

### Run with Docker
To view the core values or the political profile of VSX on Docker, follow the steps below:
1. Build the image: `docker build -t politicalprofile .`
2. Run the container: `docker run -p 8000:8000 politicalprofile`
3. Visit the link: http://127.0.0.1:8000/

## Usage

1. Browse the homepage to view the political profile and explore the 10 core values.
2. Navigate using the menu: Admin, Political Profile, Polls, Login.
3. Browse through the collection of 10 core values.
4. Browse on any value to see a zoom of the core value.
5. Click the "Learn More" button to find out the description of the core value.

## Screenshots:

![Capstone-Political Profile Website  Screenshot](capstone_political_profile_screenshot.png)

## Credits

- Developed by [iMuhluri](https://www.linkedin.com/in/victor-sifiso-xaba)
- Core values designs by [Victor Sifiso Xaba - VSX](https://www.linkedin.com/in/victor-sifiso-xaba)

## Github Repository:
[Capstone Political Profile Repository - Core Values of VSX](https://github.com/Victor-Sifiso-Xaba/capstone-politicalprofile)