# _interest
![image](https://github.com/user-attachments/assets/e720286c-9c46-4358-ba84-998b1db59e07)

_interest is a Pinterest-like web application designed for users to discover, collect, and share images and content based on their interests. The project is built with a modern tech stack to ensure a smooth and scalable experience.

## Features
- User authentication and profile management
- Create, edit, and delete image collections (boards)
- Upload and organize images (pins) with descriptions and tags
- Search and explore trending content
- Like, comment, and share pins
- Responsive and intuitive user interface

## Tech Stack
- **Frontend**: Angular for a dynamic and interactive user experience
- **Backend**: Django for a robust and scalable server-side architecture
- **Database**: PostgreSQL for reliable data storage and management

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/_interest.git
   cd _interest
   ```
2. Set up the backend:
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
3. Set up the frontend:
   ```sh
   cd frontend
   npm install
   ng serve
   ```
4. Open the app in your browser at `http://localhost:4200/`



