# wikipedia plain text

## Wikipedia article as plain text

wikipedia plain text is a CLI tool to download wikipedia articles as plain text via command line.

### Install

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

