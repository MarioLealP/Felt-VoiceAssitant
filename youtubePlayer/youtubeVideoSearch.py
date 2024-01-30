import requests
from apiKeys import youtubeAPI

def search_youtube_api(query):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': youtubeAPI,
    }

    try:
        # Make a request to the YouTube Data API search endpoint
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        json_data = response.json()

        # Check if there are search results
        if 'items' in json_data and json_data['items']:
            # Extract the video ID of the first result
            video_id = json_data['items'][0]['id']['videoId']

            # Construct the video URL
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            # Print the URL with UTF-8 encoding
            print(f"The URL of the first search result on YouTube is: {video_url.encode('utf-8').decode('utf-8')}")

            return video_url
        else:
            print("Error: No search results found.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {e}")
        return None
    except ValueError as e:
        print(f"Error: Failed to parse JSON response - {e}")
        return None
