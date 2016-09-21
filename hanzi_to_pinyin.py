# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json



def get_Pinyin(word=''):
	apikey = "9b0349210a58b04fdde6d841f6cb93d2"
	url = 'http://apis.baidu.com/sillystudio/service/topy?words='+ urllib.quote(word) +'&accent=0&traditional=0&letter=0&oc=0&type=json'
	req = urllib2.Request(url)
	req.add_header("apikey", apikey)

	resp = urllib2.urlopen(req)
	content = resp.read()
	if(content):
		code = json.loads(content)['code']
		pinyin = json.loads(content)['py']
		#ws = json.loads(content)['ws']
		#print(content)
		if code == '200':
			print pinyin
			return pinyin
		else:
			print "fail"

def main():
	input = open('name_word.txt','r')
	words = input.readlines()
	output  = open('hanzi_pinyin_map.csv','w')
	for w in words:
		w = w.strip()
		print "check the word: "+w
		pinyin = get_Pinyin(w)
		output.write(w+','+pinyin.encode('ascii','ignore')+'\n');
	output.close()


#start process
if __name__ == '__main__':
    main()
