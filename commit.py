import datetime as dt
import os

bg = 3 # number of commits for the background divided by 2
fg = 15

start = dt.date(2020, 6, 8)

today = dt.date.today()
row = today.weekday()
col = (today - start).days // 7

with open("pattern.csv", "r") as f:
    value = f.readlines()[row].split(";")[col]
value = fg if value == "x" else bg

commit_and_push = """
echo Hello World >> README.md
git add .
git commit -m "Hello World\!"
git push

echo #Hello World > README.md
git add .
git commit -m "Hello World\!"
git push
"""

for _ in range(value):
    os.system(commit_and_push)
