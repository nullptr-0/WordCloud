# WordCloud
<b>A Python Commandline WordCloud Generator</b>

## Dependencies
1. wordcloud
2. imageio (imread)
3. sys
4. getopt
5. jieba
6. chardet

## WordCloud Usage
1. Simple Mode:Drag the text file to the executable or 'WordCloud <input>'

2. Full Mode:WordCloud input [encoding] [mask] [fontpath] [background] [width] [height] [output]<>

    > - Arguments with [ ] are OPTIONAL.

    Argument | Usage
    ------------ | -------------
    -i x.x or --input      = x.x | Path of input.
    -e x   or --encoding   = x | Encode of input.Default to automatically detection.
    -m x.x or --mask       = x.x | Path of mask for word cloud generation.
    -f x.x or --fontpath   = x.x | Path of font for the words in the word cloud.
    -b x   or --background = x | Background color of the word cloud.Defaulted to white.
    -w x   or --width      = x | Width of the word cloud.Defaulted to 1200.
    -h x   or --height     = x | Height of the word cloud.Defaulted to 600.
    -o x.x or --output     = x.x | Path of output.Defaulted to 'output.png'.

3. Example:WordCloud -i report.txt -e utf-8 --mask=src\cloud.png -f DroidSansMono.ttf -b black -o report.png")

## Bugs Report & New Ideas
Send an issue and/or E-mail me at 959220793@qq.com

## Contact Me
> - E-mail: 959220793@qq.com
> - QQ: 959220793
> - Tel (In the mainland of China ONLY): 18309182230
