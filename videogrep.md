# Videogrep

Videogrep lets you make supercuts based on the spoken word content of videos. In order for it to work you need to have either a subtitle file (ending with ```.srt```), a vtt file (ending with ```.vtt```) or a transcription.

Documentation can be found at: [http://antiboredom.github.io/videogrep/](http://antiboredom.github.io/videogrep/)

## Installation

Videogrep can be used as a desktop app for Mac, and a also as a command line program. The desktop app is easier to use, but less powerful than the command line program.

### Mac desktop app

[Download it here.](http://saaaam.s3.amazonaws.com/VideoGrep.app.zip)


### Command line program

```
pip install videogrep
```
(you may also need to add ```sudo``` before the ```pip```)

If this doesn't work you probably don't have pip installed. To get install it, first download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run:
```python get-pip.py```


## Basic Use

For a single video:

```
videogrep --input my_video.mp4 --search 'some word or phrase' --output my_new_video.mp4
```

For multiple videos:

```
videogrep --input *.mp4 --search 'some word or phrase' --output my_new_video.mp4
```

## Advanced Use

### Regular Expressions
A regular expression is a special syntax for doing advanced text search. You add special characters to your search to specify different options. Here's a [good intro](http://www.regular-expressions.info/quickstart.html). And here's [another one](http://www.decontextualize.com/teaching/rwet/regular-expressions/) focused on Python, by Allison Parrish.

Some quick examples useful for videogrep:

```Trump``` would match with a line that contains the word "trump" anywhere in it.

```Trump|Clinton``` would match with a line containing either the word "Trump" or "Clinton"

```^Trump``` would match with a line starting with the word "Trump".

```Trump$``` would match with a line ending with the word "Trump".

You can just put regular expressions into videogrep like a normal search:

```
videogrep --input myvideo.mp4 --search '^why|^because' --output questions_and_answers.mp4
```


### Searching for categories of words

**Note:** You must first install pattern.en to search for word categories. To do so, run `pip install pattern` 

You can add the ```--search-type``` flag to search for grammatical patterns or categories of words.

To search for grammatical patterns, add ```--search-type pos``` to the command, and then search for parts of speech tags instead of words. 

For example, "NN" means singular noun, "VB" means basic verb, and "VBG" means gerund (a verb ending in "ing"). These are known as Penn Treeband tags, and you can see a full list of them [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

So, to get all the lines of speech containing gerunds:

```
videogrep --input myvideo.mp4 --search-type pos --search 'VBG' --output gerunds.mp4
```

You could also combine this with the regular expression search. So, to find all lines starting with a gerund, just add a carat character before "VBG":

```
videogrep --input myvideo.mp4 --search-type pos --search '^VBG' --output gerunds.mp4
```


You can also search for "hypernyms" or categories of words. For example, to search for all the words that are 'liquids' you can enter:

```
videogrep --input myvideo.mp4 --search-type hyper --search 'liquids' --output liquids.mp4
```

### Transcribing videos

Transcribing videos is useful when a subtitle file isn't available, or you want to make a supercut from individual words rather than phrases.

You can transcribe videos using the desktop app. If you want to do it on the command line, first install pocketsphinx:

```
brew tap watsonbox/cmu-sphinx
brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase
brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxtrain # optional
brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx
```

To transcribe a video, just add the ```--transcribe``` flag like so:

```
videogrep --input myvideo.mp4 --transcribe
```

It'll take a while. When it's done, you can tell videogrep to use the transcription by adding the ```--use-transcript``` flag:

```
videogrep --input myvideo.mp4 --use-transcript --search "trump"
```

The ```--search-type``` flag will work with transcribed videos also.

## Common workflows

Here are a few examples of how you might use videogrep:

#### Download videos from youtube and make supercuts with their .vtt files

1) Download a video and .vtt subtitle file from youtube, and save the video as an mp4:

```
youtube-dl https://www.youtube.com/watch?v=CWck2xoZkJM -f 22 --write-auto-sub
```

2) Show the most frequently used words from the video

```
videogrep --input biden.mp4 --use-vtt --ngrams 1
```

3) Extract all the sentences that have the word "president" in them and save to a file called `president.mp4`

```
videogrep --input biden.mp4 --use-vtt --search "president" --output president.mp4
```

4) Extract all the individual words "president"

```
videogrep --input biden.mp4 --use-vtt --search "president" --search-type "word" --output president.mp4
```

#### Transcribe a video you already have downloaded and use the transcription

1) Transcribe a video

```
videogrep --input somevideo.mp4 --transcribe
```

2) Show most frequently used words

```
videogrep --input somevideo.mp4 --use-transcript --ngrams 1
```

3) Create a supercut with the word "whatever"

```
videogrep --input somevideo.mp4 --use-transcript --search "whatver" --search-type "word" --output whatever.mp4
```

#### Download an entire playlist from youtube and make a supercut

1) Download a playlist as a series of mp4s and also save subtitle (.vtt) files

```
youtube-dl https://www.youtube.com/playlist?list=PLRJNAhZxtqH_3Nl-7n1vhgTUHyFSuQ0nI -f 22 --write-auto-sub
```

2) Create a supercut with the entire playlist

```
videogrep --input *.mp4 --use-vtt --search "question" --search-type "word" --output questions.mp4
```


## Using Videogrep from Python

You can also use videogrep from a Python script rather than the command line.

Here's an example of how to automatically create a supercut of the most common phrase in any video file. I used a similar process to create [this twitter bot](http://twitter.com/cspanfive).

```python
import sys
from pattern.en import ngrams
import videogrep
from collections import Counter

videofile = sys.argv[1]
subtitlefile = videofile.replace('.mp4', '.srt')

lines = open(subtitlefile).read()
grams = ngrams(lines, n=3)

most_common = Counter(grams).most_common(1)

phrase = most_common[0][0]
phrase = ' '.join(phrase)

print phrase

outputfile = videofile + '.most_common.mp4'
videogrep.videogrep([videofile], outputfile, phrase, 're')
```







