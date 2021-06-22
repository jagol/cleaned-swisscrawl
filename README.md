# Clean SwissCrawl

**Note: We do not provide any SwissCrawl data, due to distribution regulartions. To obtain the data please visit: https://icosys.ch/swisscrawl**

Since the SwissCrawl corpus was automatically scraped from the internet it contains some non-Swiss German text. We tried to clean the corpus by annotating a small subset of the SwissCrawl and predicting on the rest if it is Swiss German or not using a bootstrapping procedure. 


In this repository we provide the sentences that were labelled as Swiss German by our system. Since we cannot provide the sentences themselves, we offer a script which maps the predicted labels to the original SwissCrawl via ids.

Usage:
`python3 label_swisscrawl.py -s <path-to-swisscrawl.csv> -o <path-to-output-file.csv>`

Note: the SwissCrawl ids are generated enumerating the SwissCrawl sentences as provided by its authors in version `swisscrawl-2019-11-23.csv`.
