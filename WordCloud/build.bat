copy WordCloud.py "WordCloud - copy.py"
move C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages\wordcloud\wordcloud.py C:\Users\Administrator\AppData\Roaming\wordcloud.py
copy wordcloudlib.py C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages\wordcloud\wordcloud.py
C:\Users\Administrator\AppData\Roaming\Python\Python37\Scripts\PyInstaller -F -c -i WordCloud.ico --version-file=file_version_info.txt WordCloud.py
del C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages\wordcloud\wordcloud.py
move C:\Users\Administrator\AppData\Roaming\wordcloud.py C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages\wordcloud\wordcloud.py
del WordCloud.py
move "WordCloud - copy.py" WordCloud.py
pause