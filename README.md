# Algorithms Visualizer 

<div id="logo" align="center">
    <br />
    <img src="./icons/3d.png" alt="Logo" width="200"/>
    <h1>Algorithms Visualizer</h1>
    <h3>A small project built in Python using Pygame to make algorithm visualization easy.</h3>
</div>

***

## Introduction

This project provides a simple visualizer for different algorithms.
- Supported Algorithms: Currently, the visualizer supports Bubble Sort and Selection Sort.
- Interactive Visualization: Users can run algorithms step-by-step using the Return or Space key, making it easier to follow the logic and flow of each algorithm.
- Upcoming Enhancements: I'm actively working on adding Insertion Sort, which will be available soon.
- Future Plans: In addition to sorting algorithms, I plan to incorporate other algorithms like Merge Sort, Quick Sort, as well as search algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS)

>PS: This is my first GUI project, and I'm still learning Python. I welcome any constructive criticism or feedback to help improve the project. Your insights are invaluable as I continue to develop and refine this visualizer!

***

## Installation

### Prerequisites

Make sure you have `Python 3.8 or later` installed on your machine.

#### Installing Python 3
##### Windows

- Download and run Python Installer:
    - Go to the [Python Downloads page](https://www.python.org/downloads/windows/)
    - Download the latest stable version
    - Open the downloaded .exe file to start the installer.
    - Important: Check the box that says "Add Python 3.x to PATH" before clicking "Install Now."

- Verify Installation:
    - Open Command Prompt by pressing Win + R, typing cmd, and pressing Enter.
    - Type `python --version` and press Enter.
    - You should see the Python version you installed.

##### MacOS
- Download and run Python Installer:
  - Go to the [Python Downloads page](https://www.python.org/downloads/macos/).
  - Download the latest stable version.
  - Open the downloaded .pkg file to start the installer. Follow the prompts in the installer to complete the installation.
    
- Verify Installation:
  - Open Terminal (you can find it via Spotlight search by pressing Cmd + Space and typing Terminal).
  - Type `python3 --version` and press Enter.
  - You should see the Python version you installed.

##### Linux
- Ubuntu/Debian-based Systems:
  ```sh
  sudo apt update && sudo apt install python3 python3-pip
  ```
- Fedora
  ```sh
  sudo dnf check-update && sudo dnf install python3 python3-pip
  ```
- Arch based
  ```
    sudo pacman -Sy python3 python3-pip
  ```

You will also need to install `Pygame` version `2.1.0 or later`.

#### Installing Pygame
After installing Python 3, you will need to install Pygame. You can do this using pip:
```sh
pip3 install pygame
```
>Note-If you are using windows make sure you run in this command in cmd or powershell in administrator mode.

#### Cloning repository
Clone this repo using command below to your desired location
```sh
git clone https://github.com/dazzlingdark/algorithm_visualizer.git
```
### Running the program
Just navigate inside the cloned directory and run the `main.py` file to start the program
```sh
python3 main.py
```



