from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
from gtts import gTTS
import os
import random
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
	file1 = "./lists/dictation_answers.csv"
	file2 = "./lists/words.csv"
	answer_list = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
	dct = {"Answers": answer_list}
	df = pd.DataFrame(dct)
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("index.html")

@app.route("/listen", methods=["GET", "POST"])
def listen(w1=None, w2=None, w3=None, w4=None, w5=None, w6=None, w7=None, w8=None, w9=None, w10=None):

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	wo1 = df.iat[0, 0]
	wo2 = df.iat[1, 0]
	wo3 = df.iat[2, 0]
	wo4 = df.iat[3, 0]
	wo5 = df.iat[4, 0]
	wo6 = df.iat[5, 0]
	wo7 = df.iat[6, 0]
	wo8 = df.iat[7, 0]
	wo9 = df.iat[8, 0]
	wo10 = df.iat[9, 0]

	if request.method == "POST":
		df.iat[0, 0] = request.form.getlist("word_1")[0]
		df.iat[1, 0] = request.form.getlist("word_2")[0]
		df.iat[2, 0] = request.form.getlist("word_3")[0]
		df.iat[3, 0] = request.form.getlist("word_4")[0]
		df.iat[4, 0] = request.form.getlist("word_5")[0]
		df.iat[5, 0] = request.form.getlist("word_6")[0]
		df.iat[6, 0] = request.form.getlist("word_7")[0]
		df.iat[7, 0] = request.form.getlist("word_8")[0]
		df.iat[8, 0] = request.form.getlist("word_9")[0]
		df.iat[9, 0] = request.form.getlist("word_10")[0]
		df1 = df.replace(np.nan, '', regex=True)
		df1.to_csv(file1, mode='w', index=False)
		if request.form['submit_button'] == 'Play1':
			return redirect(url_for("speak", wrd=0))
		if request.form['submit_button'] == 'Play2':
			return redirect(url_for("speak", wrd=1))
		if request.form['submit_button'] == 'Play3':
			return redirect(url_for("speak", wrd=2))
		if request.form['submit_button'] == 'Play4':
			return redirect(url_for("speak", wrd=3))
		if request.form['submit_button'] == 'Play5':
			return redirect(url_for("speak", wrd=4))
		if request.form['submit_button'] == 'Play6':
			return redirect(url_for("speak", wrd=5))
		if request.form['submit_button'] == 'Play7':
			return redirect(url_for("speak", wrd=6))
		if request.form['submit_button'] == 'Play8':
			return redirect(url_for("speak", wrd=7))
		if request.form['submit_button'] == 'Play9':
			return redirect(url_for("speak", wrd=8))
		if request.form['submit_button'] == 'Play10':
			return redirect(url_for("speak", wrd=9))
		if request.form['submit_button'] == 'SUBMIT':
			return redirect(url_for("result1"))
	else:
		return render_template("listen.html", w1 = wo1, w2 = wo2, w3 = wo3, w4 = wo4, w5 = wo5, w6 = wo6, w7 = wo7, w8 = wo8, w9 = wo9, w10 = wo10)

@app.route("/read", methods=["GET", "POST"])
def read(image=None):

	answers = []
	for i in range(10):
		answers.append('')
	if request.method == "POST":

		file_check = './lists/table.csv'

		df_check = pd.read_csv(file_check)
		length = df_check.shape[0]
		val = 0
		for i in range(length):
			val = i
			if df_check.iat[i, 5] == 1:
				break
		u = val + 1
		nam = 'read' + str(u)
		ans_file = './lists/' + nam + '/answers.csv'
		
		answers[0] = request.form.getlist("read_1")[0]
		answers[1] = request.form.getlist("read_2")[0]
		answers[2] = request.form.getlist("read_3")[0]
		answers[3] = request.form.getlist("read_4")[0]
		answers[4] = request.form.getlist("read_5")[0]
		answers[5] = request.form.getlist("read_6")[0]
		answers[6] = request.form.getlist("read_7")[0]
		answers[7] = request.form.getlist("read_8")[0]
		answers[8] = request.form.getlist("read_9")[0]
		answers[9] = request.form.getlist("read_10")[0]

		dict_ans = {'Answers': answers}
		print(answers)
		df_ans = pd.DataFrame(dict_ans)
		df1 = df_ans.replace(np.nan, '', regex=True)
		df1.to_csv(ans_file, mode='w', index=False)
		

		if request.form['submit_button'] == 'SUBMIT':
			return redirect(url_for("result4"))
	else:
		file_check = './lists/table.csv'
		files = []
		df_check = pd.read_csv(file_check)
		length = df_check.shape[0]
		for i in range(length):
			df_check.iat[i, 5] = 0
		df_check.to_csv(file_check, mode='w', index=False)
		for i in range(length):
			files.append(df_check.iat[i, 0])
		nam = random.choice(files)
		str_num = nam[4:]

		num = int(str_num)
		print(num)
		df_check.iat[num-1, 5] = 1
		df_check.to_csv(file_check, mode='w', index=False)
		dir_name = './lists/' + nam
		img_name = './static/img/' + nam + '.jpeg'
		print(img_name)
		ans_file = dir_name + '/' + 'answers.csv'
		print(ans_file)
		return render_template("read.html", image = img_name)

@app.route("/student", methods=["GET", "POST"])
def student():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)
	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("student.html")

@app.route("/instructions_1", methods=["GET", "POST"])
def instructions_1():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)
	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("instructions_1.html")

@app.route("/instructions_2", methods=["GET", "POST"])
def instructions_2():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)
	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("instructions_2.html")

@app.route("/teacher", methods=["GET", "POST"])
def teacher():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)
	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("teacher.html")

@app.route("/teacher_1", methods=["GET", "POST"])
def teacher_1():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("teacher_1.html")

@app.route("/teacher_2", methods=["GET", "POST"])
def teacher_2():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)


	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("teacher_2.html")

@app.route("/teacher_3", methods=["GET", "POST"])
def teacher_3(x=None):

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length = df_check.shape[0]
	print(length)
	nam = df_check.iat[length-1, 0]
	print(nam)
	return render_template("teacher_3.html", x=nam)

@app.route("/addwords", methods=["GET", "POST"])
def addwords():

	if request.method == 'POST':
		inp = request.form.getlist('inputWords')[0]
		inp_len = len(inp)
		wow_words = []
		word = ''
		for i in range(inp_len):
			if i == inp_len-1 and inp[i]==';':
				wow_words.append(word.strip())
			elif i == inp_len-1:
				word = word + inp[i]
				wow_words.append(word.strip())
			elif inp[i] == ';':
				wow_words.append(word.strip())
				word = ''
			else:
				word = word + inp[i]

		dict_wow = {'Words': wow_words}
		df_3 = pd.DataFrame(dict_wow)
		file_3 = './lists/web_of_words.csv'
		df_3.to_csv(file_3, mode='a', header=False, index=False)
		return redirect(url_for("result2"))


	else:

		file_check = './lists/table.csv'
		df_check = pd.read_csv(file_check)
		length_check = df_check.shape[0]
		for i in range(length_check):
			df_check.iat[i, 5] = 0
		df_check.to_csv(file_check, mode='w', index=False)

		file1 = "./lists/dictation_answers.csv"
		df = pd.read_csv(file1)
		length=df.shape[0]
		for i in range(length):
			df.iat[i, 0] = '-'
		df.to_csv(file1, mode='w', index=False)

		wow = "./lists/web_of_words.csv"
		file2 = "./lists/words.csv"
		df_w = pd.read_csv(wow)
		list_wow = []
		list_word = []
		length_w = df_w.shape[0]
		for i in range(length_w):
			list_wow.append(df_w.iat[i, 0])

		for i in range(10):
			rand_word = random.choice(list_wow)
			list_word.append(rand_word)
			list_wow.remove(rand_word)

		dict_word = {'Words': list_word}
		df_word = pd.DataFrame(dict_word)
		df_word.to_csv(file2, mode='w', index=False)
		return render_template("addwords.html")

@app.route("/addwords_2", methods=["GET", "POST"])
def addwords_2():

	if request.method == 'POST':
		rio = []
		dict_check = {'Name': [], 'Number': [], 'Image': [], 'Text File': [], 'CSV File': []}
		for i in range(10):
			rio.append('')
		rio[0] = request.form.getlist("riWord_1")[0]
		rio[1] = request.form.getlist("riWord_2")[0]
		rio[2] = request.form.getlist("riWord_3")[0]
		rio[3] = request.form.getlist("riWord_4")[0]
		rio[4] = request.form.getlist("riWord_5")[0]
		rio[5] = request.form.getlist("riWord_6")[0]
		rio[6] = request.form.getlist("riWord_7")[0]
		rio[7] = request.form.getlist("riWord_8")[0]
		rio[8] = request.form.getlist("riWord_9")[0]
		rio[9] = request.form.getlist("riWord_10")[0]

		file_check = './lists/table.csv'
		isExist1 = os.path.exists(file_check)
		if isExist1 == False:
			nam = 'read1'
			num = 1
			dir_n = './lists/read1'
			os.mkdir(dir_n)
			img = './static/img/read1.jpeg'
			textf = './lists/read1/read1.txt'
			os.mknod(textf)
			csvf = './lists/read1/read1.csv'
			u = 0
			with open(textf, 'w') as the_file:
				for i in range(10):
					line = rio[i]+'\n'
					the_file.write(line)

			dict_csvf = {'Words': rio}
			df_csvf = pd.DataFrame(dict_csvf)
			df_csvf.to_csv(csvf, mode='w', index=False)
			dict_check = {'Name': [nam], 'Number': [num], 'Image': [img], 'Text File': [textf], 'CSV File': [csvf], 'Use': [u]}
			df_check = pd.DataFrame(dict_check)
			df_check.to_csv(file_check, mode='w', index=False)

		else:
			df_c = pd.read_csv(file_check)
			length_c = df_c.shape[0]
			l_num = df_c.iat[length_c - 1, 1]
			s = 'length = ' + str(l_num)
			print(s)
			num = l_num + 1
			read_n = 'read' + str(num)
			dir_name = './lists/' + read_n
			os.mkdir(dir_name)
			textf = dir_name + '/' + read_n + '.txt'
			os.mknod(textf)
			csvf = dir_name + '/' + read_n + '.csv'
			img =  './static/img/' + read_n + '.jpeg'
			u = 0
			with open(textf, 'w') as the_file:
				for i in range(10):
					line = rio[i]+'\n'
					the_file.write(line)

			dict_csvf = {'Words': rio}
			df_csvf = pd.DataFrame(dict_csvf)
			df_csvf.to_csv(csvf, mode='w', index=False)
			dict_c1 = {'Name': [read_n], 'Number': [num], 'Image': [img], 'Text File': [textf], 'CSV File': [csvf], 'Use': [u] }
			df_c1 = pd.DataFrame(dict_c1)
			df_c1.to_csv(file_check, mode='a', header=False, index=False)
		return redirect(url_for('teacher_3'))


	else:
		file1 = "./lists/dictation_answers.csv"
		df = pd.read_csv(file1)
		length=df.shape[0]
		for i in range(length):
			df.iat[i, 0] = '-'
		df.to_csv(file1, mode='w', index=False)

		wow = "./lists/web_of_words.csv"
		file2 = "./lists/words.csv"
		df_w = pd.read_csv(wow)
		list_wow = []
		list_word = []
		length_w = df_w.shape[0]
		for i in range(length_w):
			list_wow.append(df_w.iat[i, 0])

		for i in range(10):
			rand_word = random.choice(list_wow)
			list_word.append(rand_word)
			list_wow.remove(rand_word)

		dict_word = {'Words': list_word}
		df_word = pd.DataFrame(dict_word)
		df_word.to_csv(file2, mode='w', index=False)
		return render_template("addwords_2.html")

@app.route("/about", methods=["GET", "POST"])
def about():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("about.html")

@app.route("/result2", methods=["GET", "POST"])
def result2():

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	file2 = "./lists/words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)
	return render_template("result2.html")

@app.route("/result1")
def result1(a_1=None, b_1=None, c_1=None, a_2=None, b_2=None, c_2=None, a_3=None, b_3=None, c_3=None, a_4=None, b_4=None, c_4=None, a_5=None, b_5=None, c_5=None, a_6=None, b_6=None, c_6=None, a_7=None, b_7=None, c_7=None, a_8=None, b_8=None, c_8=None, a_9=None, b_9=None, c_9=None, a_10=None, b_10=None, c_10=None):
	file1 = './lists/dictation_answers.csv'
	file2 = './lists/words.csv'
	df1 = pd.read_csv(file1)
	df1 = df1.replace(np.nan, '', regex=True)
	df2 = pd.read_csv(file2)


	a1 = df1.iat[0, 0]
	b1 = df2.iat[0, 0]
	if a1.lower() == b1.lower():
		c1 = 'Perfection'
	else:
		c1 = 'We will improve!'

	a2 = df1.iat[1, 0]
	b2 = df2.iat[1, 0]
	if a2.lower() == b2.lower():
		c2 = 'Perfection'
	else:
		c2 = 'We will improve!'

	a3 = df1.iat[2, 0]
	b3 = df2.iat[2, 0]
	if a3.lower() == b3.lower():
		c3 = 'Perfection'
	else:
		c3 = 'We will improve!'

	a4 = df1.iat[3, 0]
	b4 = df2.iat[3, 0]
	if a4.lower() == b4.lower():
		c4 = 'Perfection'
	else:
		c4 = 'We will improve!'

	a5 = df1.iat[4, 0]
	b5 = df2.iat[4, 0]
	if a5.lower() == b5.lower():
		c5 = 'Perfection'
	else:
		c5 = 'We will improve!'

	a6 = df1.iat[5, 0]
	b6 = df2.iat[5, 0]
	if a6.lower() == b6.lower():
		c6 = 'Perfection'
	else:
		c6 = 'We will improve!'

	a7 = df1.iat[6, 0]
	b7 = df2.iat[6, 0]
	if a7.lower() == b7.lower():
		c7 = 'Perfection'
	else:
		c7 = 'We will improve!'

	a8 = df1.iat[7, 0]
	b8 = df2.iat[7, 0]
	if a8.lower() == b8.lower():
		c8 = 'Perfection'
	else:
		c8 = 'We will improve!'

	a9 = df1.iat[8, 0]
	b9 = df2.iat[8, 0]
	if a9.lower() == b9.lower():
		c9 = 'Perfection'
	else:
		c9 = 'We will improve!'

	a10 = df1.iat[9, 0]
	b10 = df2.iat[9, 0]
	if a10.lower() == b10.lower():
		c10 = 'Perfection'
	else:
		c10 = 'We will improve!'

	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)

	df = pd.read_csv(file1)
	df = df.replace(np.nan, '', regex=True)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'
	df.to_csv(file1, mode='w', index=False)

	wow = "./lists/web_of_words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)

	return render_template("result1.html", a_1=a1, b_1=b1, c_1=c1, a_2=a2, b_2=b2, c_2=c2, a_3=a3, b_3=b3, c_3=c3, a_4=a4, b_4=b4, c_4=c4, a_5=a5, b_5=b5, c_5=c5, a_6=a6, b_6=b6, c_6=c6, a_7=a7, b_7=b7, c_7=c7, a_8=a8, b_8=b8, c_8=c8, a_9=a9, b_9=b9, c_9=c9, a_10=a10, b_10=b10, c_10=c10)

@app.route("/result4")
def result4(x_1=None, y_1=None, z_1=None, x_2=None, y_2=None, z_2=None, x_3=None, y_3=None, z_3=None, x_4=None, y_4=None, z_4=None, x_5=None, y_5=None, z_5=None, x_6=None, y_6=None, z_6=None, x_7=None, y_7=None, z_7=None, x_8=None, y_8=None, z_8=None, x_9=None, y_9=None, z_9=None, x_10=None, y_10=None, z_10=None):
	 
	file_check = './lists/table.csv'
	df_check = pd.read_csv(file_check)
	length_check = df_check.shape[0]
	val = 0
	for i in range(length_check):
		val = i
		if df_check.iat[i, 5] == 1:
			break

	for i in range(length_check):
		df_check.iat[i, 5] = 0
	df_check.to_csv(file_check, mode='w', index=False)
	u = val + 1
	name = 'read' + str(u) 
	print(name)
	file11 = './lists/'+ name + '/answers.csv'
	file12 = './lists/'+ name + '/' + name + '.csv'
	print(file12)
	df11 = pd.read_csv(file11)
	df11 = df11.replace(np.nan, '', regex=True)
	df12 = pd.read_csv(file12)
	print(df11)
	print(df12)

	x1 = df11.iat[0, 0]
	y1 = df12.iat[0, 0]
	if x1 == y1:
		z1 = 'Perfection'
	else:
		z1 = 'We will improve!'

	x2 = df11.iat[1, 0]
	y2 = df12.iat[1, 0]
	if x2 == y2:
		z2 = 'Perfection'
	else:
		z2 = 'We will improve!'

	x3 = df11.iat[2, 0]
	y3 = df12.iat[2, 0]
	if x3 == y3:
		z3 = 'Perfection'
	else:
		z3 = 'We will improve!'

	x4 = df11.iat[3, 0]
	y4 = df12.iat[3, 0]
	if x4 == y4:
		z4 = 'Perfection'
	else:
		z4 = 'We will improve!'

	x5 = df11.iat[4, 0]
	y5 = df12.iat[4, 0]
	if x5 == y5:
		z5 = 'Perfection'
	else:
		z5 = 'We will improve!'

	x6 = df11.iat[5, 0]
	y6 = df12.iat[5, 0]
	if x6 == y6:
		z6 = 'Perfection'
	else:
		z6 = 'We will improve!'

	x7 = df11.iat[6, 0]
	y7 = df12.iat[6, 0]
	if x7 == y7:
		z7 = 'Perfection'
	else:
		z7 = 'We will improve!'

	x8 = df11.iat[7, 0]
	y8 = df12.iat[7, 0]
	if x8 == y8:
		z8 = 'Perfection'
	else:
		z8 = 'We will improve!'

	x9 = df11.iat[8, 0]
	y9 = df12.iat[8, 0]
	if x9 == y9:
		z9 = 'Perfection'
	else:
		z9 = 'We will improve!'

	x10 = df11.iat[9, 0]
	y10 = df12.iat[9, 0]
	if x10 == y10:
		z10 = 'Perfection'
	else:
		z10 = 'We will improve!'

	file1 = './lists/dictation_answers.csv'
	file2 = './lists/words.csv'
	df = pd.read_csv(file1)
	length=df.shape[0]
	for i in range(length):
		df.iat[i, 0] = '-'

	wow = "./lists/web_of_words.csv"
	df_w = pd.read_csv(wow)
	list_wow = []
	list_word = []
	length_w = df_w.shape[0]
	for i in range(length_w):
		list_wow.append(df_w.iat[i, 0])

	for i in range(10):
		rand_word = random.choice(list_wow)
		list_word.append(rand_word)
		list_wow.remove(rand_word)

	dict_word = {'Words': list_word}
	df_word = pd.DataFrame(dict_word)
	df_word.to_csv(file2, mode='w', index=False)

	# df111 = df11.replace(np.nan, '', regex=True)
	# for i in range(10):
	# 	df111.iat[i, 0] = ''

	df11.to_csv(file11, mode = 'w', index=False )

	return render_template("result4.html", x_1=x1, y_1=y1, z_1=z1, x_2=x2, y_2=y2, z_2=z2, x_3=x3, y_3=y3, z_3=z3, x_4=x4, y_4=y4, z_4=z4, x_5=x5, y_5=y5, z_5=z5, x_6=x6, y_6=y6, z_6=z6, x_7=x7, y_7=y7, z_7=z7, x_8=x8, y_8=y8, z_8=z8, x_9=x9, y_9=y9, z_9=z9, x_10=x10, y_10=y10, z_10=z10)


@app.route("/<int:wrd>", methods=["GET", "POST"])
def speak(wrd):
	file1 = "./lists/dictation_answers.csv"
	df = pd.read_csv(file1)
	wo1 = df.iat[0, 0]
	wo2 = df.iat[1, 0]
	wo3 = df.iat[2, 0]
	wo4 = df.iat[3, 0]
	wo5 = df.iat[4, 0]
	wo6 = df.iat[5, 0]
	wo7 = df.iat[6, 0]
	wo8 = df.iat[7, 0]
	wo9 = df.iat[8, 0]
	wo10 = df.iat[9, 0]
	words = pd.read_csv("./lists/words.csv")
	
	language = 'en'
	word = str(words.iat[int(wrd), 0])
	myobj = gTTS(text=word, lang=language, slow=False)
	myobj.save("welcome.mp3")
	os.system("mpg123 welcome.mp3")
	return redirect(url_for("listen", w1 = wo1, w2 = wo2, w3 = wo3, w4 = wo4, w5 = wo5, w6 = wo6, w7 = wo7, w8 = wo8, w9 = wo9, w10 = wo10))

if __name__ == "__main__":
	app.run(debug=True)
