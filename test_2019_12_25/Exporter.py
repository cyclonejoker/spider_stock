from scrapy.exporters import JsonLinesItemExporter

# 自定义Exporter类,继承父类
class CustomJsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        # 直接调用父类的构造,只是将其ensure_ascii设置为False,这样就可以支持中文
        super(CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)
# 启用自定义的Exporter
FEED_EXPORTERS = {
    # 当导出到json文件时使用该类
    'json': 'scrapylzh.settings.CustomJsonLinesItemExporter'
}