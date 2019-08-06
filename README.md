# qmh

Update in 2019 summer:

- Templates: adopted most website pages to conciser, cleaner template scripts.
- Data visualizations: migrated some graphs through copy-pasting; re-wrote all Bokeh graphs with Plotly JS; created one new graph with HTML/CSS.
  - The pure HTML/CSS graph has visible issues (extra lines), and is not responsive.
  - The D3.js graphs copy-pasted as-were are not responsive, either because of their nature or the units, such as px, that scaled the graphs.
- Static images: the "images" folder in "static/images" (i.e. static/images/images/) contains potentially useful images which are NOT in use in the website; images in the outer "images" folder contain images in use.
- The project: re-structured the directory hierarchy to the regular structure; the "my" in naming, e.g. "myqmh", "myAsylum", was used to distinguish the new project I was working on with the old "FriendsAsylum" project name on the server. Feel free to change.
- Stylesheets: "base.css" styles mostly just what is in "base.html"; repetitive features, such as "buttons", in almost all pages, are styled in "elements.css".

Virtual environment: source /myqmh/myqmhvenv/bin/activate
How each new feature is added: see "tutorials" in folder "Yuying Rong" in Friends Asylum Google Drive

REMAINING TASKS
- All copy-pasted d3 graphs had fixed dimension which would not display properly on smaller screens; I thought they all needed to be remade.
- In-text glossary fetching is not enabled on every page. I had to add the same code under every function in "views.py" so every page could load "glossary_dict" which the get_item custom tag would grab glossary info from. I believed that a smarter way for all functions to inherit these lines must exist.
- I wanted to add all bibliography as object to Models, but bib info wasn't full and I did not have the time. Once added, I would like to create another custom tag to grab info from the database, and then enable an topple-show feature for clickable citations. However, it still needs to be consulted whether to carry out these steps.
