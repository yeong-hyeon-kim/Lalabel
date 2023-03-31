# 📕 Lalabel

- `Github Issue Lable` 템플릿을 작성하고 다른 레포지토리에 복사합니다.

## 🏷️ 기능(Function)

- 작성된 `Label` 템플릿을 다른 레포지토리에서 사용합니다.

## 💡 사용 예제(Usage Example)

1. `Personal access tokens` 발급 합니다.
2. 레포지토리`(Repository)` 포크`(Fork)`합니다.
3. 레포지토리`(Repository)` `Actions secrets` 설정합니다.
    - `TOKEN` : `Personal access tokens`
    - `REPO`  : `Repository` - 라벨 가져올 레포지토리 이름
4. 라벨`(Label)` [템플릿(Template)](./labels.json) 수정합니다.

    ```javascript
    [
        { "Repository": "레포지토리 이름" },
        [
            {
            "name": "이름",
            "color": "색상",
            "description": "설명",
            "hex": "색상코드"
            }
        ]
    ]
    ```

5. 브런치`(Branch)` 생성 후 `Full Request` 요청합니다.
6. `Github Action` 완료 후 대상 레포지토리`(Repository)` 라벨을 확인합니다.

## 💻 개발 환경(Develop Environment)

### 🧰 시스템 환경(System Environment)

||운영체제(OS)|언어(Language)|종속성(Dependency)|
|-|:-:|:-:|:-:|
|명칭(Name)|![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)|![PYTHON](https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=Python&logoColor=white)|![PY-PI](https://img.shields.io/badge/PYPI-3775A9?style=flat-square&logo=PyPI&logoColor=white)|
|버전(Version)|`11`|`3.11`|[requirements](./requirements.txt)|

### 🗂️ 라이브러리(Libraries)

- Python 패키지 종속성

``` bash
pip freeze > requirements.txt
```

- Python 패키지 복원

``` bash
pip install -r requirements.txt
```

## 🔍 정보(Information)

### 🖋️ 저자(Author)

- [Yeonghyeon Kim](https://github.com/yeong-hyeon-kim/) – codechemi@gmail.com

### ⚖️ 라이센스(License)

- 다음 라이센스를 준수하며 [License](./License)에서 자세한 정보를 확인할 수 있습니다.

## 📖 비고(Remark)

### ⚠️ 대상 레포지토리에 생성된 라벨은 제거되고 [템플릿(Template)](./labels.json) 내용으로 생성됩니다
