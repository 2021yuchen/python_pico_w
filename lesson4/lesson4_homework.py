try:
    # 輸入身高（公分）與體重（公斤）
    height_cm = int(input("請輸入身高(公分): "))
    weight_kg = int(input("請輸入體重(公斤): "))

    # 檢查輸入的數值是否為合理範圍
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("身高和體重必須是正數")

    # 將身高轉換為公尺
    height_m = height_cm / 100

    # 計算 BMI 值
    bmi = weight_kg / (height_m ** 2)

    # 輸出 BMI 值
    print(f"您的BMI值為{bmi:.1f}")

    # 判斷 BMI 狀況
    if bmi < 18.5:
        print("您的體重過輕")
    elif 18.5 <= bmi < 24:
        print("正常範圍")
    elif 24 <= bmi < 27:
        print("您的體重過重")
    elif 27 <= bmi < 30:
        print("輕度肥胖")
    elif 30 <= bmi < 35:
        print("中度肥胖")
    else:
        print("重度肥胖")

except ValueError as e:
    print(f"輸入格式錯誤: {e}")

except Exception as e:
    print(f'錯誤訊息: {e}')
    
print("應用程式結束")
