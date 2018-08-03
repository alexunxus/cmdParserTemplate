# cmdParserTemplate
command parser interface for python

## Getting started:
You have 5 commands in commonCmd.py, they are HELp, DOfile, HIStory, Quit, USAGE

Why are some of the character is in upper case and another in lower? Let me explain. If the character is in upper case, 
that means you should always type this character if you want to execute that command, and the character in lower case is
not compulsory. But note that if you type a character that doesn't match these in lower case, the command will not be executed.

For example,the following command can call command "HELp" successfully.
```
cmd> help
cmd> hel
cmd> Help
cmd> HElp
cmd> HEL
```
On the other hand, the following command will not call "HELp" successfully.
```
cmd> hell
cmd> he lp
cmd> h
cmd> he
```


### Help
When you type help in the cmd parser, it will print the usage of all commands
```
cmd> help
HIStory: HIStory
DOfile: DOfile < file > [-Replace]
Quit: Quit [ -Force ]
HELp: HELp [ command ]

```

If you add specific command after the term "help", the cmd will print the usage of that specific command

```
cmd> help quit
Quit: Quit [ -Force ]
```

### Dofiles
One can input dofiles directly when running main.py, like:
```
bash $ python main.py -File do1
```

or typing DOfile and the file you want to execute, like:
```
cmd> dofile do1
# will execute the commands in do1
```
### History
The command history (without any argument) can print out the history of commands, like
```
cmd> help
HIStory: HIStory
DOfile: DOfile < file > [-Replace]
Quit: Quit [ -Force ]
HELp: HELp [ command ]

cmd> help quit
Quit: Quit [ -Force ]

cmd> history
0 .  None
1 .  help
2 .  help quit 

```
### Quit
Typing "Quit" will let you quit the command.
```
cmd> q -f
```

### USAGE
Check your time usage of this program. For example,
```
cmd> help
HIStory: HIStory
DOfile: DOfile < file > [-Replace]
Quit: Quit [ -Force ]
HELp: HELp [ command ]
USAGE: print time usage

cmd> history
0 .  help
1 .  history

cmd> his
0 .  help
1 .  history
2 .  his

cmd> usage
Period used time: 0.00 s
Total time usage: 0.00 s

cmd> 

```
