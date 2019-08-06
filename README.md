# qmh

Update from 2019 summer:

Virtual environment: source /myqmh/myqmhvenv/bin/activate
How each new feature is added: see "tutorials" in folder "Yuying Rong" in Friends Asylum Google Drive

REMAINING TASKS
1) All copy-pasted d3 graphs had fixed dimension which would not display properly on smaller screens; I thought they all needed to be remade.
2) In-text glossary fetching is not enabled on every page. I had to add the same code under every function in "views.py" so every page could load "glossary_dict" which the get_item custom tag would grab glossary info from. I believed that a smarter way for all functions to inherit these lines must exist.
3) I wanted to add all bibliography info to a model object, but bib info wasn't full and I did not have the time. Once added, I would like to create another custom tag to grab info from the database.
