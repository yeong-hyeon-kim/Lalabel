from github import Github
from operator import length_hint
import json
import sys
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# Token = ""
# RepositoryName = ""

# 레포지토리 정보 가져오기


def GithubRepository():
    githubObject = Github(Token)
    print(RepositoryName)
    repository = githubObject.get_user().get_repo(RepositoryName)

    print("Get GithubRepository!")

    return repository

# 레포지토리 레이블 가져오기


def FetchLabel():
    # 내부 정보 확인
    LocalStorage = []
    LabelCount = 0

    # 저장된 라벨 읽기
    with open('labels.json', 'r', encoding='UTF-8-sig') as file:
        LocalStorage = json.load(file)

    if len(LocalStorage) != 0:
        # 레포지토리 이름
        LocalName = LocalStorage[0]["Repository"]
        # 라벨 갯수
        LocalLabelCount = length_hint(LocalStorage[1])
        global RepositoryName

        # 기본으로 설정된 레포지토리 이름을 'labels.json' 값으로 설정합니다.
        RepositoryName = LocalName
        LabelCount = LocalLabelCount
    if LabelCount == 0:
        # 레이블 객체
        Labels = []
        Repository = [{"Repository": RepositoryName}]

        # 레포지토리 객체
        repository = GithubRepository()
        labels = repository.get_labels()

        # 라벨 파일에 추가
        if labels.totalCount != 0:
            for label in labels:
                print(label)
                Labels.append({"name": label.name, "color": label.color,
                               "description": label.description, "hex": "#" + label.color})
            Repository.append(Labels)

            with open('labels.json', 'w', encoding='UTF-8-sig') as f:
                f.write(json.dumps(Repository, ensure_ascii=False))

        print("Fetch Labels!")

# 레포지토리 레이블 제거


def DeleteDefaultLabel():
    # 레포지토리 객체
    repository = GithubRepository()
    # 레포지토리 라벨 객체
    labels = repository.get_labels()

    if labels.totalCount != 0:
        # 기본 레이블만 제거
        for label in labels:
            print(label)
            label.delete()

        print("Delete Labels!")


# 레포지토리 레이블 등록
def CreateLabel():
    Labels = []
    repository = GithubRepository()

    with open('labels.json', 'r', encoding='UTF-8-sig') as file:
        Labels = json.load(file)

    for label in Labels[1]:
        repository.create_label(
            label["name"], label["color"], label["description"])
        print(label)

    print("Create Labels!")


# Github Repository Secrets
if __name__ == "__main__":
    Token = os.environ['TOKEN']
    RepositoryName = os.environ['REPO']

# 대상 레포지토리 라벨 가져오기
FetchLabel()
# 대상 레포지토리 라벨 지우기
DeleteDefaultLabel()
# 사용자 지정 라벨 템플릿 등록
CreateLabel()
