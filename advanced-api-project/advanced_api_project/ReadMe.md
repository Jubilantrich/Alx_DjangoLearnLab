## Advanced API Features

### Filtering
To filter books by attributes, use query parameters:
- /api/books/?title=Sample Book
- /api/books/?author=John Doe&publication_year=2023

### Searching
To perform a search on title and author fields, use the search parameter:
- /api/books/?search=Sample

### Ordering
To order results, use the ordering parameter:
- Ascending by title: /api/books/?ordering=title
- Descending by publication_year: /api/books/?ordering=-publication_year