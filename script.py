from github import Github
import json
import sys
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

Token = ""
RepositoryName = ""

# 레이블 객체
Repository = [{"Repository": RepositoryName}]
Labels = []

# 레포지토리 정보 가져오기
def GithubRepository(access_token, repository_name):
    githubObject = Github(access_token)
    repository = githubObject.get_user().get_repo(repository_name)
    return repository

# 레포지토리 레이블 가져오기
def PatchLabel():
    repository = GithubRepository(Token, RepositoryName)
    labels = repository.get_labels()
    for label in labels:
        print(label)
        Labels.append({"name": label.name, "color": label.color,
                      "description": label.description, "hex": "#" + label.color})
    Repository.append(Labels)

    with open('labels.json', 'w', encoding='UTF-8-sig') as f:
        f.write(json.dumps(Repository, ensure_ascii=False))

# 레포지토리 레이블 제거
def DeleteDefaultLabel():
    repository = GithubRepository(Token, RepositoryName)
    labels = repository.get_labels()
    # 기본 레이블만 제거
    for label in labels:
        if label.raw_data["default"] == True:
            label.delete()
        else:
            label.delete()

# 레포지토리 레이블 생성
def CreateLabel():
    Labels = []
    repository = GithubRepository(Token, RepositoryName)

    with open('labels.json', 'r', encoding='UTF-8-sig') as file:
        Labels = json.load(file)

    for label in Labels[1]:
        repository.create_label(
            label["name"], label["color"], label["description"])
        print(label)

# Github Action
if __name__ == "__main__":
    Token = os.environ['TOKEN']
    RepositoryName  = os.environ['REPO']

PatchLabel()
DeleteDefaultLabel()
CreateLabel()