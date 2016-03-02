
#--------------------------------------------------
#--------------------------------------------------
#module: module_template.py
#version: 0.1
#author: andrew christ
#email: andrew.christ@gmail.com
#last update: 2015
#notes:
#--------------------------------------------------
#--------------------------------------------------
#import built in modules
import os
#import custom packages
import pak_html.encoder
import pak_fileOps.fileUtility
#--------------------------------------------------

#Variables
#directory where the index file should go:
web_html_dir=os.getcwd()+"/test_html"
#full path to data directory:
web_data_dir=os.getcwd()+"/test_data"
#folder name for data in this syntax "../folder_name/"
web_data_folder="../test_data/"

#--------------------------------------------------
def main():
	print("marmotsoft ")
	print("fileserver bot ")

	#get file list
	fileList=list_files()

	#clean file list of unneeded things like hidden files

	#generate html
	htmlData=gen_html(fileList)

	#create index file
	build_index(htmlData)

	print("Goodbye")

#--------------------------------------------------

#--------------------------------------------------
def list_files():
	temp= os.listdir(web_data_dir)
	return temp
#--------------------------------------------------

#--------------------------------------------------
def gen_html(items):
	content=[]
	intro_txt=[]
	intro_txt.append('Generated by Marmotsoft Fileserver Bot')
	for i in items:
		temp=pak_html.encoder.encode_file_link(web_data_folder+i,i)
		#temp+='<br>'
		content.append(temp)

	complete=pak_html.encoder.gen_complete_page('index.html','LightSteelBlue',
	'Marmot Files', intro_txt, content)

	return complete
#--------------------------------------------------

#--------------------------------------------------
def build_index(html_data):
	filepath=web_html_dir+'/index.html'
	pak_fileOps.fileUtility.deleteFile(filepath)
	pak_fileOps.fileUtility.writeFile(filepath, html_data)

#--------------------------------------------------

main()
