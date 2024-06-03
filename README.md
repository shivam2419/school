# School Website

# Image :
![School Website](School-Website-images/image1.png)

**For more images, go on folder 'School_Website-images' in the repo...**
## Overview

This is a school website project aimed at facilitating the admission process for potential students. The website features a user-friendly interface for registering admission queries and includes an admin panel for administrators to manage and respond to these queries efficiently.

## Features

- **User Registration**: Students and parents can register admission queries through a simple form on the website.
- **Admin Panel**: Administrators have access to an admin panel where they can view, manage, and respond to admission queries.
- **Responsive Design**: The website is designed to be responsive, ensuring optimal viewing and interaction experience across various devices and screen sizes.
- **Database Integration**: Utilizes SQLite3 database for storing user data and admission queries.
- **Technologies Used**: HTML, CSS, JavaScript, Python, Django, SQLite3.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/school-website.git
   ```
2. Navigate to the project directory:
   ```bash
   cd school-website
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the website at `http://localhost:8000` in your web browser.

## Usage

- **User Registration**: Visit the website and navigate to the registration form. Fill in the required details and submit the form to register your admission query.
- **Admin Panel**: Administrators can access the admin panel by visiting `http://localhost:8000/admin` in their web browser. Log in using admin credentials to view, manage, and respond to admission queries.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request with a detailed explanation of your changes.
