from newspaper import Article
import csv

#A new article from TOI
url =  "https://www.programiz.com/python-programming/working-csv-files"

#For different language newspaper refer above table
toi_article = Article(url, language="en") # en for English

#To download the article
toi_article.download()

#To parse the article
toi_article.parse()

#To perform natural language processing ie..nlp
toi_article.nlp()


#To extract title
print("Article's Title:")
p=toi_article.text
print(p)
print("nn")

#To extract text
print("Article's Text:")
c=toi_article.text
print(c)
print("nn")

#To extract summary
print("Article's Summary:")
a=toi_article.summary
print(a)
print("nn")

#To extract keywords
print("Article's Keywords:")
b=toi_article.summary
print(b)



csvData = ['news article scraping',p, 'news'] 

with open('articles.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    # writer.writerows(csvData)
    # writer = csv.writer(csvFile)
    writer.writerow(csvData)

csvFile.close()
