#module: pak_html_util.encoder.py
#version: 0.1
#author: andrew christ
#email: andrew.christ@gmail.com
#last update: 7-18-2015
#notes:

#import built in modules

#import custom packages

def encode_image(file_name, alt_text):
	return '<img src="'+file_name+'" alt="'+alt_text+'" >'

def encode_file_link(file_name, link_text):
	return '<a href="'+file_name+'">'+link_text+'</a>'


#---------------------------------------------
def gen_complete_page(file_name, backgrnd_color, title_txt, intro_txt_list, html_content):
	html=[]
	html.append('<!DOCTYPE html>')
	html.append('<html>')
	html.append('<body style="background-color:'+backgrnd_color+'">')
	html.append('<h2>'+title_txt+'</h2><br>')

	for i in intro_txt_list:
		html.append('<p>'+i+'</p>')

	for i in html_content:
		html.append(i+'<br>')

	html.append('</body>')
	html.append('</html>')

	return html

#---------------------------------------------
