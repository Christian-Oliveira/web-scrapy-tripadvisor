<h1 align="center">
	<img src="https://scrapy.org/img/scrapylogo.png"  alt="Logo Scrapy"  width="240"><br><br>
    Web Scraping Tripadvisor - Extract Comment's Users
</h1>

<div>
    <p align="center">
        <a href="https://www.linkedin.com/in/christian-d-oliveira/" target="_blank">
            <img src="https://img.shields.io/static/v1?label=Author&message=Christian&color=red&style=for-the-badge&logo=LinkedIn" alt="Author: Christian">
        </a>
        <a href="https://www.python.org/">
            <img src="https://img.shields.io/static/v1?label=Language&message=Python&color=blue&style=for-the-badge&logo=Python" alt="Language: Python">
        </a>
        <a href="https://scrapy.org/">
            <img src="https://img.shields.io/static/v1?label=Framework&message=Scrapy&color=00ba6d&style=for-the-badge&logo=?logo=https://scrapy.org/img/scrapylogo.png" alt="Framework: Scrapy">
        </a>
    </p>
</div>

## Table of Contents

<p align="center">
 <a href="#about">About</a> •
 <a href="#features">Features</a> •
 <a href="#revised-concepts">Revised Concepts</a> • 
 <a href="#installation">Installation</a> • 
 <a href="#getting-started">Get Started</a>
</p>

## 📌About

<div>
    <p align="center">
        Construction of an application to extract information as comment's users of the website <strong>Tripadvisor</strong> (<em>tripadvisor.com.br</em>) and export to JSON or CSV.
    </p>
</div>

## 🚀Features

- Extract comment's users of the website Tripadvisor
- Export comments to JSON and CSV

## 👓Revised Concepts

- Crawlers
- Spiders
- Extract informations in Wensites
- Selectors in HTML and CSS

## 📕Installation

**You must have already installed**
- [Python >= 3.8](https://www.python.org/)

**Let's divide it into 3 steps.**
1. Clone this repository
2. Install dependencies
3. Initializing the BackEnd
  ---
### 1. Clone this repository
```
git clone https://github.com/Christian-Oliveira/web-scrapy-tripadvisor.git
```
---
### 2. Create and activate virtualenv
```
python -m venv .venv
```
in Linux and MacOS
```
source name_virtualenv/bin/activate
```
in Windows
```
name_virtualenv/Scripts/Activate
```

### 3. Intall the dependencies

Go to project folder and run the code
```
pip install -r requirements.txt
``` 

## 🎮Getting Started

Run the crawler with the following command:
1. To export JSON
```
scrapy crawl comments -o comments.json
```
2. To export CSV
```
scrapy crawl comments -o comments.csv
```
