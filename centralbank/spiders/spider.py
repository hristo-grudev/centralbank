import scrapy

from scrapy.loader import ItemLoader
from ..items import CentralbankItem
from itemloaders.processors import TakeFirst


class CentralbankSpider(scrapy.Spider):
	name = 'centralbank'
	start_urls = ['https://www.centralbank.ie/news-media',
	              'https://www.centralbank.ie/news-media/blog'
	              ]

	def parse(self, response):
		post_links = response.xpath('//div[@class="sf_cols row equal-height new-landing-4cols"]//div[@class="spotlight fixed-lines"]//a/@href|//div[@class="spotlight fixed-lines spotlight-wide new-story"]/div[@class="spotlight-content "]/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//article//h1//text()').get()
		description = response.xpath('//article//text()[normalize-space() and not(ancestor::h1| ancestor::div[@class="news-tags"])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="news-tags"]/span/text()').get()

		item = ItemLoader(item=CentralbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
