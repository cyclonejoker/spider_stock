import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.mail import MailSender
logger=logging.getLogger(__name__)
class SendEmail(object):

    def __init__(self,sender,crawler):
        self.sender = sender
        crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        mail_host = crawler.settings.get('MAIL_HOST') # 发送邮件的服务器
        mail_port = crawler.settings.get('MAIL_PORT') # 邮件发送者
        mail_user = crawler.settings.get('MAIL_USER') # 邮件发送者
        mail_pass = crawler.settings.get('MAIL_PASS') # 发送邮箱的密码不是你注册时的密码，而是授权码！！！切记！

        sender = MailSender(mail_host,mail_user,mail_user,mail_pass,mail_port) #由于这里邮件的发送者和邮件账户是同一个就都写了mail_user了
        h = cls(sender,crawler)

        return h

    def spider_idle(self,spider):
        logger.info('idle spider %s' % spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)
        body = 'spider[%s] is closed' %spider.name
        subject = '[%s] good!!!' %spider.name
        # self.sender.send(to={'zfeijun@foxmail.com'}, subject=subject, body=body)
        return self.sender.send(to={'zfeijun@foxmail.com'}, subject=subject, body=body)