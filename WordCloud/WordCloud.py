import wordcloud
from imageio import imread
import sys
import getopt
import jieba
import chardet
def displayUsage():
    print("WordCloud Usage:\n")
    print("Simple Mode:Drag the text file to the executable or 'WordCloud input'\n")
    print("Full Mode:WordCloud input [encoding] [mask] [fontpath] [background] [width] [height] [output]")
    print("*Arguments with [ ] are OPTIONAL.")
    print("-i *.* or --input      = *.* :Path of input.")
    print("-e *   or --encoding   = *   :Encode of input.Default to automatically detection")
    print("-m *.* or --mask       = *.* :Path of mask for word cloud generation.")
    print("-f *.* or --fontpath   = *.* :Path of font for the words in the word cloud.")
    print("-b *   or --background = *   :Background color of the word cloud.Defaulted to white.")
    print("-w *   or --width      = *   :Width of the word cloud.Defaulted to 1200.")
    print("-h *   or --height     = *   :Height of the word cloud.Defaulted to 600.")
    print("-o *.* or --output     = *.* :Path of output.Defaulted to 'output.png'.\n")
    print("Example:WordCloud -i report.txt -e utf-8 --mask=src\cloud.png -f DroidSansMono.ttf -b black -o report.png")
    sys.exit(0)
def simple_mode():
    fp=open(sys.argv[1],"rb")
    dat=fp.read()
    detection=chardet.detect(dat)
    enc=detection['encoding']
    if detection['language']=="Chinese":
        ftp="msyh.ttc"
    else:
        ftp="DroidSansMono.ttf"
    fp.close()
    fp=open(sys.argv[1],"r",encoding=enc)
    txt=fp.read()
    fp.close()
    txt=jieba.lcut(txt)
    txt=" ".join(txt)
    w=wordcloud.WordCloud(font_path=ftp)
    w.generate(txt)
    w.to_file("output.png")
def full_mode():
    msk="null"
    bgc="black"
    ofn="output.png"
    detectenc=True
    detectlan=True
    width=1200
    height=600
    try:
        opts,args=getopt.getopt(sys.argv[1:],"i:e:m:f:b:w:h:o:",["input=","encoding=","mask=","fontpath=","background=","output="])
    except getopt.GetoptError:
        displayUsage()
    for opt,arg in opts:
        if opt in ("-i","--input"):
            ifn=arg
        if opt in ("-e","--encoding"):
            enc=arg
            detectenc=False
        if opt in ("-m","--mask"):
            msk=arg
        if opt in ("-f","--fontpath"):
            ftp=arg
            detectlan=False
        if opt in ("-b","--background"):
            bgc=arg
        if opt in ("-w","--width"):
            width=arg
        if opt in ("-h","--height"):
            height=arg
        if opt in ("-o","--output"):
            ofn=arg
    if detectenc==True:
        fp=open(ifn,"rb")
        dat=fp.read()
        enc=chardet.detect(dat)['encoding']
        fp.close()
    if detectlan==True:
        fp=open(ifn,"rb")
        dat=fp.read()
        lan=chardet.detect(dat)['language']
        if lan=="Chinese":
            ftp="msyh.ttc"
        else:
            ftp="DroidSansMono.ttf"
        fp.close()
    fp=open(ifn,"r",encoding=enc)
    txt=fp.read()
    fp.close()
    txt=jieba.lcut(txt)
    txt=" ".join(txt)
    if msk=="null":
        w=wordcloud.WordCloud(font_path=ftp,background_color=bgc,width=int(width),height=int(height))
    else:
        mk=imread(msk)
        w=wordcloud.WordCloud(mask=mk,font_path=ftp,background_color=bgc,width=int(width),height=int(height))
    w.generate(txt)
    w.to_file(ofn)

if __name__=="__main__":
    argc=len(sys.argv)
    if argc<=1 :
        displayUsage()
    elif argc==2 :
        simple_mode()
    else:
        full_mode()
