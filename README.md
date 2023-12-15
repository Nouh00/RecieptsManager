# Django Receipt Tracker

## Introduction

This is a simple Django application that allows users to manually enter and track their receipt information. The application focuses on basic CRUD (Create, Read, Update, Delete) operations and user authentication.

## Features

- User authentication (register, login, logout)
- Receipt management (create, list, detail, update, delete)
- Basic testing for models and views


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Nouh00/RecieptsManager.git
    ```

2. Change into the project directory:

    ```bash
    cd RecieptsManager
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the application.

3. Register a new user or log in with existing credentials.

4. Use the application to manage your receipts.

## Testing

Run the tests using the Django test runner:

```bash
python manage.py test reciepts.tests
```
