
# FritzNetMonitor

FritzNetMonitor is a Python-based project that uses Flask to monitor network traffic over a Fritzbox router. The application displays the connected devices to the network in a table format and offers real-time data presentation via a local web server.

## Project Structure

The project follows the structure outlined below:

```
fritznetscan/
├── app.py               # Flask Webserver
├── fritzreader.py       # Connection to FritzBox & Data Retrieval
├── static/
│   └── style.css        # Optional Styling
├── templates/
│   └── dashboard.html   # HTML Dashboard (Jinja2)
└── requirements.txt     # Python dependencies
```

## Installation

To get started with FritzNetMonitor, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd fritznetscan
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the FritzBox credentials and address in `fritzreader.py`.

4. Run the application:

   ```bash
   python app.py
   ```

   The web server will start, and you can access the dashboard by opening your browser and navigating to `http://127.0.0.1:5000`.

## Features

- Displays connected devices in a table format.
- Real-time data retrieval from a FritzBox router.
- Local web server using Flask to render data dynamically.

## Requirements

- Python 3.x
- Required Python packages in `requirements.txt`:

   - `flask`
   - `fritzconnection`

## Troubleshooting

If you encounter issues with connecting to the FritzBox, ensure that:
- The FritzBox is accessible from your machine.
- The credentials and IP address are correct.
- There are no firewalls blocking the connection.

## License

This project is licensed under the MIT License.

