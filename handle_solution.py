import sqlite3

## input 

no_sm = "j,sh,x"
no_ym = "i,an,ian"

sd = "1,134,14,13" # "12,234,23,1"
sm = "-,-,-,-"
ym = "-,-,-,-"

possible_smym = '''
sm,y,234
ym,u,134
'''
#sm,y,234


## sqlite3 select condition

condition_txt = " where "

sm = sm.split(",")
for i in [0,1,2,3]:
	if sm[i] != "-":
		condition_txt += "sm%s='%s' and " % (i+1, sm[i])

ym = ym.split(",")
for i in [0,1,2,3]:
	if ym[i] != "-":
		condition_txt += "ym%s='%s' and " % (i+1, ym[i])

sd = sd.split(",")
for i in [0,1,2,3]:
	sd_loc = sd[i]
	if sd_loc != "-":
		tmp = ["sd"+str(i+1)+"="+each for each in sd_loc]
		condition_txt += "(" + " or ".join(tmp) + ") and "

def gen_or(smym,loc,word):
    global condition_txt
    word = "'"+word+"'"
    tmp = [smym+each for each in loc]
    condition_txt += "(" + " or ".join([each+"="+word for each in tmp]) + ") and "

for line in possible_smym.strip().split("\n"):
	if line != "":
		smym,word,loc = line.split(",")
		gen_or(smym,loc,word)

no_sm = ["'"+each+"'" for each in no_sm.split(",")]
for each in no_sm:
	if each != "":
		condition_txt += "sm1!="+each+" and "
		condition_txt += "sm2!="+each+" and "
		condition_txt += "sm3!="+each+" and "
		condition_txt += "sm4!="+each+" and "

no_ym = ["'"+each+"'" for each in no_ym.split(",")]
for each in no_ym:
	if each != "":
		condition_txt += "ym1!="+each+" and "
		condition_txt += "ym2!="+each+" and "
		condition_txt += "ym3!="+each+" and "
		condition_txt += "ym4!="+each+" and "


#print('''cursor.execute("select chengyu from chengyu '''+condition_txt[:-5]+''' ")''')

## query

conn= sqlite3.connect("chengyu.db")
cursor = conn.cursor()

cursor.execute("select chengyu from chengyu " +condition_txt[:-5])
print(cursor.fetchall())
