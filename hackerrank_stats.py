# hackerrank_stats.py

import requests

def fetch_hackerrank_stats(username):
    url = f"https://www.hackerrank.com/rest/contests/master/hackers/tharunkumarvmt/profile"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['model']
        return {
            "problems_solved": data.get("solved_challenges", 0),
            "followers": data.get("followers", 0)
        }
    else:
        print("Error fetching data")
        return None

def update_readme(stats):
    with open("README.md", "r") as file:
        lines = file.readlines()

    # Find the section to update in README.md
    for i, line in enumerate(lines):
        if "📊 **Stats**" in line:
            # Update the line below with the dynamic stats
            lines[i + 1] = f"| **Problems Solved**: {stats['problems_solved']} | **Followers**: {stats['followers']} |\n"
    
    # Write the updated README content
    with open("README.md", "w") as file:
        file.writelines(lines)

if __name__ == "__main__":
    username = "yourusername"  # Replace with your actual HackerRank username
    stats = fetch_hackerrank_stats(username)
    if stats:
        update_readme(stats)
