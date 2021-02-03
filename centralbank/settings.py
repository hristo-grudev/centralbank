BOT_NAME = 'centralbank'

SPIDER_MODULES = ['centralbank.spiders']
NEWSPIDER_MODULE = 'centralbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'centralbank.pipelines.CentralbankPipeline': 100,

}