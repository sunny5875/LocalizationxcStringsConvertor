import os
import json
import pandas as pd

def xcstrings_to_csv(input_path, output_path):
    # 입력 파일이 존재하는지 확인
    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    # localizable.xcstrings 파일을 읽어서 JSON 파싱
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 데이터프레임으로 변환
    df_data = {'Key': [], 'Korean': [], 'English': []}

    for key, value in data["strings"].items():
        korean_translation = value.get("localizations", {}).get("ko", {}).get("stringUnit", {}).get("value", "")
        english_translation = value.get("localizations", {}).get("en", {}).get("stringUnit", {}).get("value", "")
        
        df_data['Key'].append(key)
        df_data['Korean'].append(korean_translation)
        df_data['English'].append(english_translation)

    df = pd.DataFrame(df_data)

    # 데이터프레임을 CSV 파일로 저장
    df.to_csv(output_path, index=False)
    print(f"Conversion successful. CSV file saved to '{output_path}'.")

# 입력 파일 경로와 출력 파일 경로를 지정
input_file_path = 'Localizable.xcstrings'
output_file_path = 'output.csv'

# xcstrings를 CSV로 변환
xcstrings_to_csv(input_file_path, output_file_path)
