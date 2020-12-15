from github import Github

g = Github("npradaschnor", "05032016Liz")

repo = g.get_repo("npradaschnor/Pima-Indians-Diabetes-Dataset")
contents = repo.get_views_traffic()
contents = repo.get_views_traffic(per="week")
print(contents)