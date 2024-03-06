# Localization.xcstrings to Csv file
2024, Localizable.xcstrings를 csv 파일로 변경하는 코드입니다!

### 사용 방법
#### xcstrings ➡️ csv
- `pip install pandas`로 pandas 설치 (M1의 경우 호환이 안되는 경우가 발생할 수 있습니다. 그런 경우 아래처럼 venv로 가상환경 만들어서 pandas를 설치해주면 됩니다)
```
arch -x86_64 /usr/bin/python3 -m venv venv
source venv/bin/activate  # 또는 activate.bat (Windows)
pip install pandas
``` 
- Localizable.xcstrings를 main.py가 있는 곳에 복사(혹시 이름이 다르다면 main.py에 path에도 반영해줘야 합니다)
- `python main.py` 실행
- output.csv 파일 생성

#### csv ➡️ xcstrings
- `pip install pandas`로 pandas 설치 (M1의 경우 호환이 안되는 경우가 발생할 수 있습니다. 그런 경우 아래처럼 venv로 가상환경 만들어서 pandas를 설치해주면 됩니다)
```
arch -x86_64 /usr/bin/python3 -m venv venv
source venv/bin/activate  # 또는 activate.bat (Windows)
pip install pandas
``` 
- output.csv main_reverse.py가 있는 곳에 복사(혹시 이름이 다르다면 main.py에 path에도 반영해줘야 합니다)
- `python main_reverse.py` 실행
- Localizable2.xcstrings 파일 생성
