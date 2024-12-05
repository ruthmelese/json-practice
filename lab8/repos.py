#!/usr/bin/env python3

import json
import csv

with open('../data/schacon.repos.json', 'r') as file:
    repositories = json.load(file)

with open('chacon.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for repo in repositories[:5]:  
        repo_name = repo.get("name", "N/A")
        repo_url = repo.get("html_url", "N/A")
        last_updated = repo.get("updated_at", "N/A")
        repo_visibility = repo.get("visibility", "N/A")
        
        csv_writer.writerow([repo_name, repo_url, last_updated, repo_visibility])
