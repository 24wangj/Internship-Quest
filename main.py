import requests


def google_search(query, api_key, cse_id, num_results=5):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id,
        "num": num_results
    }
    response = requests.get(search_url, params=params)

    # Ensure we got a valid response
    if response.status_code == 200:
        results = response.json()
        if 'items' in results:
            # Extract and print titles and links of search results
            for item in results['items']:
                print("Title:", item['title'])
                print("Link:", item['link'])
                print()  # Print a blank line for readability
        else:
            print("No search results found.")
    else:
        print("Error:", response.status_code, response.text)


# Replace these with your actual API Key and CSE ID
API_KEY = "AIzaSyDs9LGJw0jI7ok_lvFXHdK0xCJ7wO5TIC4"
CSE_ID = "77170425770244c34"

# Search for a keyword
google_search("Internships", API_KEY, CSE_ID)
