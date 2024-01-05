import requests

# Replace 'MY_ACCESS_TOKEN' with your actual Github personal access token 
access_token = 'MY_ACCESS-TOKEN'

# Github GraphQL API endpoint
url = 'https://api.github.com/graphql'

# GraphQL query to get information about a specific repository
query = '''
{
  repository(owner: "aryaparasharmrt", name: "GraphQL") {
    name
    description
    stargazers {
      totalCount
    }
    forks {
      totalCount
    }
}
}
'''

headers = {
  'Authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json',
  }

# Make the GraphQL request
response = requests.post(url, json={'query': query}, headers=headers)

if response.status_code == 200:
  data = response.json()
  repository_info = data['data']['repository']

  print(f"Repository: {repository_info['name']}")
  print(f"Description: {repository_info['description']}")
  print(f"Stargazers: {repository_info['stargazers']['totalCount']}")
  print(f"Forks: {repository_info['forks']['totalCount']}")
else:
  print(f"Error: {response.status_code}, {response.text}")





















