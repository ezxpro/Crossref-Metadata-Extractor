# CROSSREF Journal DOI Retriever

-------------------------

This is supposed to receive the ISSN of a journal as an input and return a JSON file with metadata from it, including the name, the issue number and publication date.

I'm using the Crossref Unified API for this purpose, it's a public, free API, and as long as you don't thrash their servers with too many requests AND provide your email in your queries (so they can contact you if you mess up), you can use it freely.

To modify the queries and to get the fields you want you'll need to take a look into [the Crossref API documentation]\(https://api.crossref.org/swagger-ui/index.html#/Journals/get_journals__issn__works\) and change the requests in the code as you like, it should be pretty straightforward to use.

This is very rough around the edges, I wrote this because I intend to create a list of DOI number and title of every article in every issue of a given journal.

I'm just publishing this because one day it might be useful to someone, so there's no interactivity here, the ISSN and the JSON file name are hardcoded, but it should be easy to modify this script to make it interactive and maybe pass the output file path and the ISSN as parameters. Otherwise, just open the python script, specify the ISSN (either as a single number or separated by a dash) and the JSON output file and run the script, it should be fine.
