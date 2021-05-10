driving = input("運転したことがありますか")

if driving != "あります" and driving != "ありません" :
	print("あります/ありませんを入力してください")
	raise SystemExit

age = input("あなたの年齢は？")
age = int(age)
if driving == "あります" :
	if age >= 18:
		print("問題なし")
	else:
		print("交通違反")
elif driving == "ありません":
	if age >= 18:
		print("運転免許取得できますね")
	else:
		print("あと数年で運転免許取得できますね")
else:
	print("あります/ありませんを入力してください")