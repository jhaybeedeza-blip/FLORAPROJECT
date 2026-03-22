import sqlite3, json
db = r'c:\Users\Acer\Desktop\django_lesson\sitenijb\db.sqlite3'
conn = sqlite3.connect(db)
cur = conn.cursor()
rows = cur.execute("PRAGMA table_info('homepage_unsentmessage')").fetchall()
print(json.dumps(rows, indent=2))
print('\nApplied migrations for app "homepage":')
try:
	migs = cur.execute("SELECT app, name FROM django_migrations WHERE app='homepage' ORDER BY id").fetchall()
	print(json.dumps(migs, indent=2))
except Exception as e:
	print('Could not query django_migrations:', e)
