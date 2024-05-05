from tkinter import *
from tkinter import ttk, messagebox
from urllib.parse import urlparse
import requests
import json

def get_subdomains(domain, api_key):
    if domain is None:
        raise ValueError("Domain cannot be None")
    if api_key is None:
        raise ValueError("API Key cannot be None")

    url = f"https://api.shodan.io/dns/domain/{domain}?key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        results = response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch subdomains from Shodan API: {str(e)}")
    
    subdomains = results.get('data', [])
    
    if not subdomains:
        raise ValueError(f"No subdomains found for {domain}")

    return subdomains

def export_to_json(domain, api_key, filename):
    try:
        subdomains = get_subdomains(domain, api_key)
        
        filename = f"{domain}_subdomains.json"
        
        # Write results to JSON file
        with open(filename, 'w') as f:
            json.dump(subdomains, f, indent=4)
        
        print(f"Results exported to {filename} successfully.")
        return filename  # Return the generated filename
    except Exception as e:
        print(f"Failed to export results: {str(e)}")


# Function to handle button click event
def export_to_json_button():
    domain = domain_entry.get()
    api_key = api_entry.get()
    filename = "subdomains.json"
    
    try:
        export_to_json(domain, api_key, filename)
        messagebox.showinfo("Export Successful", "Results exported to subdomains.json successfully.")
    except Exception as e:
        messagebox.showerror("Export Failed", f"Failed to export results: {str(e)}")

# Modify the main function to use the updated get_subdomains function
def main(domain, api_key, console_output):
    # Check if domain is not None
    if domain is None:
        console_output.config(state=NORMAL)
        console_output.insert(END, "Domínio inválido. Tente novamente.\n")
        console_output.config(state=DISABLED)
        return

    # Retrieve subdomains for the domain
    try:
        subdomains = get_subdomains(domain, api_key)
    except Exception as e:
        console_output.config(state=NORMAL)
        console_output.insert(END, f"Falha ao buscar subdomínios para {domain}: {str(e)}\n")
        console_output.config(state=DISABLED)
        return

    # Extract and display both IP addresses and full URLs
    if subdomains:
        console_output.config(state=NORMAL)
        console_output.insert(END, f"Subdomínios encontrados para {domain}:\n")
        for subdomain in subdomains:
            ip_address = subdomain.get('value', 'N/A')
            full_url = subdomain.get('subdomain', 'N/A')
            console_output.insert(END, f"IP: {ip_address}, URL: {full_url}\n")
        console_output.config(state=DISABLED)
    else:
        console_output.config(state=NORMAL)
        console_output.insert(END, "Nenhum subdomínio encontrado.\n")
        console_output.config(state=DISABLED)

# Create the main window
root = Tk()
root.title("Subdomain Finder")
root.geometry("600x400")

# Create a frame for the input
input_frame = Frame(root)
input_frame.pack(pady=20)

# Labels and entry widgets
ttk.Label(input_frame, text="Domínio alvo:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
domain_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
domain_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="API Key:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
api_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
api_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to trigger the search
run_button = ttk.Button(input_frame, text="Run", command=lambda: main(domain_entry.get(), api_entry.get(), console_output), style="TButton")
run_button.grid(row=2, columnspan=2, pady=10)

# Create a button to export results to JSON
export_button = ttk.Button(input_frame, text="Export to JSON", command=export_to_json_button)
export_button.grid(row=3, columnspan=2, pady=10)

# Text widget for displaying output
console_output = Text(root, wrap="word", width=60, height=15, font=("Helvetica", 12), state=DISABLED)
console_output.pack(pady=20, padx=20)

root.mainloop()