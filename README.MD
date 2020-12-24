### Why web scraping?

| Data analysis | Machine learning|
|---|---|
|Data analysis relies 100% on large amounts of data(datasets).<br>The more data you have the more accurate your data analysis will be.| Machine learning requires a huge amounts of data.<br>The more data you have the more your system can learn!|

#### Why web scraping
* Lead generation
* Real estate listings
* Price minotoring
* Stock market tracking
* Drop shipping

#### When to / not use web scraping
* Terms of services & the Robot.txt
* Does the website have a public API?
* Does the API have any limitations?
* Does the API provide all the data you want?
* Is the API free/paid?

### Selectors
`//elementName[@attribute='value']`
`//elementName[@id='value']`
`//elementName0@class='value']`

### Position
```
Ul
  li      //li[1]
  li      //li[position() = 1 or position() = 2]
  li      //li[position() = 1 and contains(@text, 'hello')]
```

### starts-with(), contains(), ends-with()

### //elementName[predicate]

### Axes
`axisName::elementName`

<table>
  <tr>
    <td>Going UP</td>
    <td>Going DOWN</td>
  </tr>
  <tr>
    <td>
      parent: `//p[@id='outside']/parent::node()`<br>
      ancestor: `/p[@id='outside']/ancestor::node()`<br>
      preceding: excluding its ancestors<br>
      preceding-sibling
    </td>
    <td>
      child: return children<br>
      following: all the elements that are after the closing tag<br>
      following-sebling: return all the elements after the closing tag but should the same parent<br>
      descendant: return the descendants
    </td>
  </tr>
</table>

### Scrapy
* setup environment
  - install Anaconda
  - install dependencies `conda install scrapy pylint autopep8 -y`
* run scrapy
`scrapy crawl <name>`

* Errors
  - ValueError: Missing scheme in request url: http or https protocol related error - usu. relative url
  - DEBUG: Filtered offsite request to 'www..': extra '//' error

### Export dataset
`scrapy crawl <name> -o <filename:json, csv, xml>` - easy json format: alt+shft+f

### Chewy.com project
* chewy.com/robots.txt
* disable javascript by choosing cmd+shft+P from browser inspect

```
scrapy startproject chewy
cd chewy
scrapy genspider pharmacy www.chewy.com/b/pharmacy-2515
```

### Debugging Spiders
```
scrapy parse --spider=pharmacy -c parse_product -d 2 <item_url>
```

### Crawl spider structure
```
scrapy genspider -l
basic
crawl
csvfeed
xmlfeed
```

### imdb project
```
scrapy startproject imdb
cd imdb
scrapy genspider -t crawl best_movies imdb.com

## rules
Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
Rule(LinkExtractor(restrict_xpaths=('//a[@class="active"]')), callback='parse_item', follow=True),
Rule(LinkExtractor(restrict_css=('//a[@class="active"]')), callback='parse_item', follow=True),
```