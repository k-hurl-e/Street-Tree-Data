# Street-Tree-Data

## Overview
Street-Tree-Data is a web application designed to display the most common street trees in various New York City neighborhoods. It leverages data from the NYC Open Data platform to provide users with an interactive way to explore urban forestry in their communities.

## Features
- **Neighborhood Search**: View the most common street trees by neighborhood.
- **Data Visualization**: Graphs and charts to visualize tree distributions.
- **API Integration**: Uses NYC Open Data API to fetch up-to-date tree data.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/k-hurl-e/Street-Tree-Data.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Street-Tree-Data
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application locally:
    ```bash
    flask run app.py
    ```

## Usage
- Access the web app in your browser.
- Enter a neighborhood to view the most common street trees in that area.

## Project Structure
- `app.py`: Main application logic.
- `treedata.py`: Handles data fetching and processing.
- `visuals.py`: Generates visualizations for tree data.
- `static/`: Contains static files like CSS and images.
- `templates/`: HTML templates for rendering the web pages.

## Technologies Used
- **Python**
- **Flask**: Web framework
- **Sodapy**: For interacting with the NYC Open Data API
- **Matplotlib/Plotly**: Data visualization libraries

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Tree Census Data sourced from NYC Open Data. All data is from the 2015 Tree Census. 

![Screenshot-2023-09-12-at-9 33 12-AM](https://github.com/user-attachments/assets/6150214e-cc3c-4658-8fb8-71ec05314d97)
