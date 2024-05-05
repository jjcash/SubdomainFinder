# Subdomain Finder

## Overview
This project is a simple Python application that utilizes the Shodan API to find subdomains for a given domain. It provides a graphical user interface (GUI) for users to input a domain and an API key, and then retrieve and display the subdomains associated with that domain.

## Purpose
This project was developed as a part of my college coursework for the class "Segurança em Desenvolvimento de Sistemas de Informação" (Security in Information Systems Development). It serves as a practical exercise in understanding security considerations related to system development, particularly in the context of identifying potential vulnerabilities such as exposed subdomains.

## Features
- Allows users to input a domain and an API key for the Shodan service.
- Retrieves subdomains associated with the specified domain using the Shodan API.
- Displays the retrieved subdomains in a text area within the graphical user interface.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the `infoGatherUi.py` file to launch the application.
4. Enter the domain and API key in the respective fields.
5. Click the "Run" button to retrieve and display the subdomains.
6. Optionally, click the "Export to JSON" button to export the subdomains to a JSON file.

## Dependencies
- Python 3.x
- Requests library (for making HTTP requests)
- Tkinter library (for creating the graphical user interface)

## Note
- Ensure that you have a valid API key for the Shodan service. You can sign up for an account and obtain an API key [here](https://account.shodan.io/register).
