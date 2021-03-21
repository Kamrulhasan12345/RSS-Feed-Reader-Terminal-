import parser

async def urls(urls):
  return [await parser.parse(url) for url in urls]