# π Lalabel

- `Github Issue Lable` ννλ¦Ώμ μμ±νκ³  λ€λ₯Έ λ ν¬μ§ν λ¦¬μ λ³΅μ¬ν©λλ€.

## π·οΈ κΈ°λ₯(Function)

- μμ±λ `Label` ννλ¦Ώμ λ€λ₯Έ λ ν¬μ§ν λ¦¬μμ μ¬μ©ν©λλ€.

## π‘ μ¬μ© μμ (Usage Example)

1. `Personal access tokens` λ°κΈ ν©λλ€.
2. λ ν¬μ§ν λ¦¬`(Repository)` ν¬ν¬`(Fork)`ν©λλ€.
3. λ ν¬μ§ν λ¦¬`(Repository)` `Actions secrets` μ€μ ν©λλ€.
    - `TOKEN` : `Personal access tokens`
    - `REPO`  : `Repository` - λΌλ²¨ κ°μ Έμ¬ λ ν¬μ§ν λ¦¬ μ΄λ¦
4. λΌλ²¨`(Label)` [ννλ¦Ώ(Template)](./labels.json) μμ ν©λλ€.

    ```javascript
    [
        { "Repository": "λ ν¬μ§ν λ¦¬ μ΄λ¦" },
        [
            {
            "name": "μ΄λ¦",
            "color": "μμ",
            "description": "μ€λͺ",
            "hex": ""
            }
        ]
    ]
    ```

5. λΈλ°μΉ`(Branch)` μμ± ν `Full Request` μμ²­ν©λλ€.
6. `Github Action` μλ£ ν λμ λ ν¬μ§ν λ¦¬`(Repository)` λΌλ²¨μ νμΈν©λλ€.

## π» κ°λ° νκ²½(Develop Environment)

### π§° μμ€ν νκ²½(System Environment)

||μ΄μμ²΄μ (OS)|μΈμ΄(Language)|μ’μμ±(Dependency)|
|-|:-:|:-:|:-:|
|λͺμΉ­(Name)|![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)|![PYTHON](https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=Python&logoColor=white)|![PY-PI](https://img.shields.io/badge/PYPI-3775A9?style=flat-square&logo=PyPI&logoColor=white)|
|λ²μ (Version)|`11`|`3.11`|[requirements](./requirements.txt)|

### ποΈ λΌμ΄λΈλ¬λ¦¬(Libraries)

- Python ν¨ν€μ§ μ’μμ±

``` bash
pip freeze > requirements.txt
```

- Python ν¨ν€μ§ λ³΅μ

``` bash
pip install -r requirements.txt
```

## π μ λ³΄(Information)

### ποΈ μ μ(Author)

- [Yeonghyeon Kim](https://github.com/yeong-hyeon-kim/) β codechemi@gmail.com

### βοΈ λΌμ΄μΌμ€(License)

- λ€μ λΌμ΄μΌμ€λ₯Ό μ€μνλ©° [License](./License)μμ μμΈν μ λ³΄λ₯Ό νμΈν  μ μμ΅λλ€.

## π λΉκ³ (Remark)

### β οΈ λμ λ ν¬μ§ν λ¦¬μ μμ±λ λΌλ²¨μ μ κ±°λκ³  [ννλ¦Ώ(Template)](./labels.json) λ΄μ©μΌλ‘ μμ±λ©λλ€
