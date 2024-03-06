import pandas as pd
import json
import numpy as np

def csv_to_xcstrings(input_path, output_path, version="1.0"):
    # CSV 파일을 데이터프레임으로 읽어들임
    df = pd.read_csv(input_path)

    # Localizable.xcstrings 형식으로 변환
    xcstrings_data = {"sourceLanguage": "en", "version": version, "strings": {}}

    for _, row in df.iterrows():
        key = row["Key"]
        korean_translation = row["Korean"]
        english_translation = row["English"]

        # NaN 값 처리
        if pd.isna(korean_translation) or korean_translation == "NaN":
            korean_translation = ""

        if pd.isna(english_translation) or english_translation == "NaN":
            english_translation = ""

        # Localizable.xcstrings 형식으로 데이터 추가
        xcstrings_data["strings"][key] = {
            "localizations": {
                "ko": {
                    "stringUnit": {
                        "state": "translated",
                        "value": korean_translation
                    }
                },
                "en": {
                    "stringUnit": {
                        "state": "translated",
                        "value": english_translation
                    }
                }
            }
        }

    # Localizable.xcstrings 형식의 JSON을 파일로 저장
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(xcstrings_data, file, ensure_ascii=False, indent=2)

    print(f"Conversion successful. Localizable.xcstrings file saved to '{output_path}'.")

# 입력 파일 경로와 출력 파일 경로를 지정
input_file_path = 'output.csv'
output_file_path = 'Localizable2.xcstrings'

# CSV를 Localizable.xcstrings로 변환
csv_to_xcstrings(input_file_path, output_file_path, version="1.0")
