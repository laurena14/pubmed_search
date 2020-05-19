from pymed import PubMed
import json

email=input("Please enter your email:")
user_input=input("I want to search for...")

pubmed = PubMed(tool="MyTool", email=email)
results = pubmed.query(user_input, max_results=5)

results_list = []
output = []

for article in results:
    results_as_dict = article.toDict()
    results_list.append(results_as_dict)

for article in results_list:
    pubmed_id = article['pubmed_id'].partition('\n')[0]
    output.append({u'pubmed_id':pubmed_id,
                       u'title':article['title'],
                       u'abstract':article['abstract']})

with open('output_results.json', 'w') as outfile:
    json.dump(output, outfile, indent=4)
    