import requests

def get_data_from_api(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # This parses the response content as JSON
        return data
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
        return None

# Example API URL
api_url = "http://compras.dados.gov.br/fornecedores/v1/fornecedores.json?uf=DF"

# Call the function to make the API request
api_data = get_data_from_api(api_url)

# Print the JSON response
print(api_data)