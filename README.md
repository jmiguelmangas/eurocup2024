# UEFA Euro 2024 Tracker

This project is a comprehensive web application designed to track the UEFA Euro 2024 tournament. It includes features for displaying team information, tracking match results, and updating standings dynamically. The backend is built using Flask, and the frontend is developed using React.

## Features

- **Team Information**: View detailed information about each team, including players and their positions.
- **Match Tracking**: Input match results and dynamically update team standings.
- **Group Standings**: View the current standings of each group, updated in real-time as match results are entered.
- **Responsive Design**: The application is fully responsive and works well on both desktop and mobile devices.

## Technologies Used

- **Backend**: Flask, Pandas
- **Frontend**: React, Axios, CSS
- **Data**: JSON, CSV

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/euro2024-tracker.git
   cd euro2024-tracker


## Setup the backend

Create a virtual environment and activate it:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
bash
Copiar código
pip install -r requirements.txt
Start the Flask server:
bash
Copiar código
python server.py

## Setup the frontend

Navigate to the frontend directory:
bash
Copiar código
cd frontend
Install the required packages:
bash
Copiar código
npm install
Start the React development server:
bash
Copiar código
npm start
Access the application
Open your web browser and navigate to http://localhost:3000

## Project Structure
backend: Contains the Flask server and related files.
frontend: Contains the React application and related files.
data: Contains data files such as player information and match results.

## Usage
View Teams: Click on a team to view detailed information about the players.
Update Match Results: Enter match results to update the standings.
View Standings: Standings are updated automatically based on the entered match results.

## Contributing

Fork the repository
Create a new feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/YourFeature)
Open a pull request

## License
This project is licensed under the MIT License.git 