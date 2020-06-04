# Passcat

Passcat lets you generate cryptographically secure, memorable passphrases.

## Installation

``pip install passcat``

## Usage

Basic usage:

```
$ passcat
throng disregard overall trimming playpen persevere
```

Specify the number of words to use in the passphrase:

```
$ passcat 5
relight usage geologic tumbling disown
```

Show available wordlists:

```
$ passcat -l

Eff
English
French
German
Indonesian
Italian
Spanish
```

Specify a wordlist other than EFF:

```
$ passcat -w spanish
latitar reglamentaria apanuscadora consultable carbunclo duplicar paragueria cincoanal
```

Specify the path to an alternate wordlist:

``$ passcat -f /path/to/wordlist/file.txt``

## License

This code is released under a free software [license](LICENSE.txt) and you are welcome to fork it.