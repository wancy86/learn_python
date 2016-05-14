import logging
# 默认界别: WARNING
# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# logging.basicConfig(level=logging.INFO)
# logging.FileHandler("test.log")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:\n %(message)s\n',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='a')
n = 10
logging.debug('n = %d' % n)
