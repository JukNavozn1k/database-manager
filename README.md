
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
    <img src="https://cdn.icon-icons.com/icons2/1508/PNG/512/officedatabase_104402.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SQL Database Manager</h3>

  <p align="center">
    A non-commercial DB-Manager
    <br/>
    <a href="https://github.com/JukNavozn1k/GlebTube/releases"><strong>Get release!</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">View Demo</a>
    ·
    <a href="https://github.com/JukNavozn1k/GlebTube/issues">Report Bug</a>
    ·
  </p>
</div>



## About project

### Description
This project allows you to manage a SQL database using a web interface. 
The project is an alternative to the standard django admin panel.

### Roadmap

- [x] Add db-manager constructor
- [ ] Add the ability to sort by column
- [ ] Add the ability for user authentication and authorization


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these steps.




### Installation

_To execute the following commands, you need to install python and pip_

1. Clone the repo
   ```sh
   git clone https://github.com/JukNavozn1k/database-manager
   ```
2. Install poetry via pip
   ```pip
   pip install poetry
   ```
3. Install poetry packages
   ```python
   poetry install
   ```
4. Run venv via poetry
   ```python
   poetry shell
   ```
5. Make migrations & migrate db
   ```python
   python manage.py makemigrations && python manage.py migrate
   ```
6. Run server localy
   ```python
   python manage.py runserver
   ```
