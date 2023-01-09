from github import Github
from operator import length_hint
import json
import sys
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

Token = ""
RepositoryName = ""

# def RepositoryInfo():
#     LocalStorage = []
#     with open('labels.json', 'r', encoding='UTF-8-sig') as file:
#         LocalStorage = json.load(file)
        
#     if len(LocalStorage) != 0:
#        RepositoryName = LocalStorage[0]["Repository"]
#        LabelCount = length_hint(LocalStorage[1])
        

# 레포지토리 정보 가져오기
def GithubRepository():
    githubObject = Github(Token)
    repository = githubObject.get_user().get_repo(RepositoryName)
    return repository

# 레포지토리 레이블 가져오기
def PatchLabel():
    # 내부 정보 확인
    ##########################################################
    LocalStorage = []
    LabelCount = 0
    
    with open('labels.json', 'r', encoding='UTF-8-sig') as file:
        LocalStorage = json.load(file)
        
    if len(LocalStorage) != 0:
       LocalName = LocalStorage[0]["Repository"]
       LocalLabelCount = length_hint(LocalStorage[1])
       
       RepositoryName = LocalName
       LabelCount = LocalLabelCount
    ##########################################################
    
    if LabelCount == 0:
        # 레이블 객체
        Labels = []
        Repository = [{"Repository": RepositoryName}]
        
        repository = GithubRepository(Token, RepositoryName)
        labels = repository.get_labels()
        
        if labels.totalCount != 0:
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
    
    if labels.totalCount != 0:
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

# 레포지토리 정보 확인
# RepositoryInfo()

# 대상 레포지토리 라벨 가져오기
PatchLabel()
# 대상 레포지토리 라벨 지우기
DeleteDefaultLabel()
# 사용자 지정 라벨 템플릿 등록
CreateLabel()