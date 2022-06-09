str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
splits = str.split()
one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 1文字を取り出す単語の番号リスト
ans = {}
for i, word in enumerate(splits):
  if i + 1 in one_ch:
    ans[word[:1]] = i + 1  # リストにあれば1文字を取得
  else:
    ans[word[:2]] = i + 1  # なければ2文字を取得

print(ans)