![Bandwidth Monitor](icon.png)

# Bandwidth Monitor (macOS)

A lightweight macOS menu bar app to monitor your network bandwidth (upload and download speeds). This open-source tool provides real-time speed updates directly in your menu bar, making it easy to keep an eye on your network activity. It's built with Python and [`rumps`](https://github.com/jaredks/rumps) and boasts a compact codebase of under 30 lines of core logic.

## Features

- Real-time upload and download speed monitoring.
- Display in macOS menu bar.
- Minimal resource usage.
- Open-source and free to use.
- Simple setup.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/dhanushreddy291/macos-bandwidth-monitor](https://github.com/dhanushreddy291/macos-bandwidth-monitor)
    cd macos-bandwidth-monitor
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Build the application:**

    ```bash
    python setup.py py2app -A
    ```

4.  **Find the app:** The `app` bundle will be located in the `dist` folder.

5.  Add it to login items: Open the app and go to `Settings -> General -> Login Items` and add the app to the list.

## Usage

Double-click the `Bandwidth Monitor` in the `dist` folder to launch the application. The bandwidth speeds will be displayed in your menu bar.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
