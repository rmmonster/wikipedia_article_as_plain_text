# wikipedia plain text

## Wikipedia article as plain text

wikipedia plain text is a CLI tool to download wikipedia articles as plain text via command line.

This tool does not enforce the [proper conduct requested by the wikipedia API](https://www.mediawiki.org/wiki/API:Etiquette). The author trusts the user to [conduct themselves properly](https://meta.wikimedia.org/wiki/Don%27t_be_a_jerk).

### Install

Required tools:
- [git](https://git-scm.com/)
- [poetry](https://python-poetry.org/)

```
git clone https://github.com/rmmonster/wikipedia_article_as_plain_text.git
cd wikipedia_article_as_plain_text
poetry install
```

### Usage

#### For the introductory paragraph

```
cd wikipedia_article_as_plain_text
poetry run download 'Article Name'
```

#### For the full article

```
cd wikipedia_article_as_plain_text
poetry run download --full 'Article Name'
```

## Disclaimer

The tool was written with the help of AI tools.

## License

[CC0](https://creativecommons.org/public-domain/#cc0)
