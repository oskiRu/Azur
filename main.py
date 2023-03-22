import requests, argparse, colorama
from colorama import Fore


parser = argparse.ArgumentParser(description='Username for the research')
parser.add_argument('-u', '--user', type=str, required=True, help='Username')

args = parser.parse_args()
username = args.user
i = 0

rep_repo = requests.get(f'https://api.github.com/users/{username}/repos').json()

for repo_data in rep_repo:
    rep_data_repo = requests.get(f"https://api.github.com/repos/{username}/{repo_data['name']}/commits").json()
    print(f"{Fore.GREEN}{repo_data['name']}:{Fore.WHITE}")

    for data_repo in rep_data_repo:    
        try:
            if "@users.noreply.github.com" in data_repo['commit']['author']['email']:
                pass
            else:
                print(f"    {data_repo['commit']['author']['email']}")
                i+=1
        except:
            pass


print("\n\n")
print(f"{Fore.GREEN}{len(rep_repo)} Repo found !")
if i == 0:
    print(f"{Fore.RED}Nothing found...")
else:
    print(f"{Fore.GREEN}{i} Result found !")
