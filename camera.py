import cv2
import imutils
import time
import requests

# 店内にいる人数のカウント変数
current_people_count = 0

# フレームサイズと横線の位置を定義
FRAME_WIDTH = 600
HORIZONTAL_LINE_POSITION = FRAME_WIDTH // 2  # フレームの真ん中に線を引く

# 人を検出するためのHOG + SVMのプリセット
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# ビデオキャプチャを初期化
cap = cv2.VideoCapture(0)  # カメラ映像の取得（0はデフォルトカメラ）

# カメラが正常に開けたか確認
if not cap.isOpened():
    print("カメラを開けませんでした。")
    exit()

time.sleep(2.0)  # カメラの準備のため少し待つ

# 通過のフラグを初期化
person_passed = False

# 店内の人数をDjango APIに保存する関数
def update_people_count_in_django(current_count):
    url = f"https://people-count-ngyx.onrender.com/counter/update-count/{current_count}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"店内人数を更新しました: {current_count}")
        else:
            print("人数の更新に失敗しました。")
    except Exception as e:
        print(f"APIリクエスト中にエラーが発生しました: {e}")

while True:
    # フレームを取得
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした。終了します。")
        break

    frame = imutils.resize(frame, width=FRAME_WIDTH)

    # フレーム内の人を検出
    (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # フレームに横線を引く（入退店の基準）
    cv2.line(frame, (HORIZONTAL_LINE_POSITION, 0), (HORIZONTAL_LINE_POSITION, frame.shape[0]), (0, 255, 255), 2)

    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 矩形の中心を計算
        center_x = x + w // 2

        # 中心が線の左側にいて、まだ通過していない場合
        if center_x < HORIZONTAL_LINE_POSITION and not person_passed:
            # 左から右に通過したとみなす (入店)
            current_people_count += 1
            person_passed = True  # 通過フラグを立てる

        # 中心が線の右側に戻り、通過フラグが立っている場合
        elif center_x > HORIZONTAL_LINE_POSITION and person_passed:
            # 右から左に通過したとみなす (退店)
            current_people_count -= 1
            person_passed = False  # フラグをリセット

    # 現在の店内人数を画面に表示
    cv2.putText(frame, f"total: {current_people_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # フレームを表示
    cv2.imshow("店内人数カウント", frame)

    # 人数が更新されたらDjangoに保存
    update_people_count_in_django(current_people_count)

    # 'q'キーを押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()
