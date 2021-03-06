import cv2

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.jpg')

# shape : 画像の形状を返す。
# (列数, 行数, チャンネル数)
# チャンネルとは? : http://www.cg-ya.net/2dcg/aboutimage/basic-knowledge-degitalimage/
# (例) : (382, 640, 3)
print(img.shape)

# 三次元配列を返す。
# (例)
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# [34 51 40], [50 81 60]などは、色の状態(BGR)を表します。
# ※ 左からBGR[B, G, R]形式を表しています。左からRGB[R, G, B]形式でないことをご注意ください。
# BGRに関する公式ドキュメント : https://docs.opencv.org/4.5.2/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
print(img)

# 色の状態(BGR)のBの部分を255(白色)にする。
# : の意味 : 「全ての」を表す。
# 参考 -> https://qiita.com/ken_yoshi/items/4cbe3abb7d46c5252fdd
img[:, :, (0)] = 255

# imwrite : 画像の保存を行う関数
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
cv2.imwrite('./output.jpg', img)
